"""Append only episode 1 with MKVToolNix, preserving compressed video/audio."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import mergegoblin as app


def find_mkvmerge(explicit=None):
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.is_file():
            raise RuntimeError(f"mkvmerge executable not found: {path}")
        return str(path)
    local = Path(__file__).resolve().parent / "tools" / ("mkvmerge.exe" if os.name == "nt" else "mkvmerge")
    candidates = [local]
    for variable in ("ProgramFiles", "ProgramFiles(x86)"):
        if os.environ.get(variable):
            candidates.append(Path(os.environ[variable]) / "MKVToolNix" / "mkvmerge.exe")
    if os.environ.get("LOCALAPPDATA"):
        candidates.append(Path(os.environ["LOCALAPPDATA"]) / "Programs" / "MKVToolNix" / "mkvmerge.exe")
    for path in candidates:
        if path.is_file():
            return str(path)
    found = shutil.which("mkvmerge")
    if not found:
        raise RuntimeError("MKVToolNix not found. Install it from https://mkvtoolnix.download/downloads.html#windows, or run: winget install --id MoritzBunkus.MKVToolNix --exact")
    return found


def timestamp(seconds):
    milliseconds = round(seconds * 1000)
    hours, remainder = divmod(milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}000000"


def publish(source, destination):
    """Never replace an existing user file."""
    try:
        os.link(source, destination)
    except FileExistsError:
        raise
    except OSError:
        with destination.open("xb") as target, source.open("rb") as original:
            try:
                shutil.copyfileobj(original, target)
            except BaseException:
                target.close()
                destination.unlink()
                raise


def merge_e01(plan, output, mkvmerge=None):
    selected = [e for e in plan["episodes"] if e["number"] == 1]
    if len(selected) != 1 or selected[0]["issues"]:
        raise RuntimeError("The plan must contain exactly one fully matched E01. Rescan before this test.")
    episode = selected[0]
    clips = episode["clips"]
    if not clips:
        raise RuntimeError("E01 has no clips.")
    paths = [Path(c["path"]).resolve() for c in clips]
    if len(paths) != len(set(paths)):
        raise RuntimeError("E01 contains a repeated local file; rescan before testing.")
    for clip, path in zip(clips, paths):
        stat = path.stat()
        if stat.st_size != clip["size"] or stat.st_mtime_ns != clip["mtime_ns"]:
            raise RuntimeError(f"File changed since scanning; rescan: {path.name}")
    mkvmerge = find_mkvmerge(mkvmerge)
    ffmpeg = app.executable("ffmpeg")
    folder = Path(output).resolve() / "E01 MKVToolNix Test"
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "Live from Daryl's House - E01 - Daryl Hall.mkv"
    review = folder / "Live from Daryl's House - E01 - Daryl Hall.NEEDS-REVIEW.mkv"
    if destination.exists() or review.exists():
        raise RuntimeError(f"An E01 test output already exists in {folder}. Select a new output folder to retry.")
    if destination in paths or review in paths:
        raise RuntimeError("Output overlaps a source clip.")
    if shutil.disk_usage(folder).free < sum(p.stat().st_size for p in paths) * 2.2:
        raise RuntimeError("Not enough free disk space for the E01 test output.")
    durations = [app.media_info(p)[0] for p in paths]
    chapter_names = [c.get("chapter", app.chapter_title(c["title"])) for c in clips]
    root = ET.Element("Chapters")
    edition = ET.SubElement(root, "EditionEntry")
    cursor = 0
    for name, duration in zip(chapter_names, durations):
        atom = ET.SubElement(edition, "ChapterAtom")
        ET.SubElement(atom, "ChapterTimeStart").text = timestamp(cursor)
        display = ET.SubElement(atom, "ChapterDisplay")
        ET.SubElement(display, "ChapterString").text = name
        ET.SubElement(display, "ChapterLanguage").text = "eng"
        cursor += duration
    chapter_file = folder / "chapters.xml"
    ET.ElementTree(root).write(chapter_file, encoding="utf-8", xml_declaration=True)
    (folder / "ordered-files.txt").write_text("\n".join(f"{i:02}. {name}\n    {path}" for i, (name, path) in enumerate(zip(chapter_names, paths), 1)) + "\n", encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="e01-", dir=folder) as temporary:
        partial = Path(temporary) / "candidate.mkv"
        arguments = ["--output", str(partial), "--title", destination.stem, "--append-mode", "file", "--chapters", str(chapter_file)]
        for index, path in enumerate(paths):
            if index:
                arguments.append("+")
            arguments.extend(["--no-chapters", "--no-attachments", "--no-global-tags", "--no-track-tags", str(path)])
        options_file = folder / "mkvmerge-options.json"
        app.write_json(options_file, arguments)
        print(f"Appending only E01: {len(paths)} clips, no video/audio re-encoding...", flush=True)
        process = subprocess.run([mkvmerge, "@" + str(options_file)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
        log_file = folder / "mkvmerge.log"
        log_file.write_text(f"Exit code: {process.returncode}\n\n{process.stdout}\n{process.stderr}", encoding="utf-8")
        # MKVToolNix: 0 = success, 1 = warnings, 2+ = error.
        if process.returncode not in (0, 1) or not partial.is_file():
            raise RuntimeError(f"mkvmerge rejected E01. Read {log_file}\n{process.stdout[-2500:]}\n{process.stderr[-2500:]}")
        problems = []
        if process.returncode == 1:
            problems.append("mkvmerge reported warnings. Review mkvmerge.log before accepting the output.")
        print("Checking duration, chapters, and full decoding...", flush=True)
        try:
            info = app.probe(partial)
            if abs(float(info["format"]["duration"]) - sum(durations)) > max(1, len(paths) * 0.1):
                raise RuntimeError("Output duration does not match the source total.")
            chapters = info.get("chapters", [])
            if [c.get("tags", {}).get("title") for c in chapters] != chapter_names:
                raise RuntimeError("Output chapter names/count do not match the ordered clips.")
            elapsed = 0
            for chapter, duration in zip(chapters, durations):
                if abs(float(chapter["start_time"]) - elapsed) > 0.002:
                    raise RuntimeError("Output chapter start times differ from the expected boundaries.")
                elapsed += duration
            app.run([ffmpeg, "-v", "error", "-xerror", "-nostdin", "-err_detect", "explode", "-i", str(partial),
                     "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])
        except (RuntimeError, KeyError, ValueError) as error:
            problems.append(f"Validation failed: {error}")
        accepted = not problems
        target = destination if accepted else review
        publish(partial, target)
        result = {"episode": 1, "method": "mkvmerge append, no re-encoding", "output": str(target),
                  "accepted": accepted, "mkvmerge_exit_code": process.returncode,
                  "clips": len(paths), "expected_duration_seconds": sum(durations), "problems": problems,
                  "manual_check": "Check playback, transitions and audio sync; decoding validation cannot establish perceptual correctness."}
        app.write_json(folder / "result.json", result)
        # Leave a reusable command file after TemporaryDirectory cleanup.
        arguments[1] = str(folder / "manual-rerun.mkv")
        app.write_json(options_file, arguments)
        print(f"{'PASSED automatic checks' if accepted else 'NEEDS REVIEW'}: {target}", flush=True)
        for problem in problems:
            print(problem, flush=True)
        print(f"Order list and diagnostic files: {folder}", flush=True)
        return accepted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default="work/plan.json")
    parser.add_argument("--output", default=str(Path.home() / "Videos" / "LFDH MKVToolNix"))
    parser.add_argument("--mkvmerge", help="Optional full path to mkvmerge.exe")
    args = parser.parse_args()
    return 0 if merge_e01(app.read_json(args.plan), args.output, args.mkvmerge) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Stopped; source clips were not changed.", file=sys.stderr)
        sys.exit(130)
