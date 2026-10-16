"""Batch-append matched episodes with MKVToolNix. Never encode or resize."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import mergegoblin as app
from e01_mkvmerge import find_mkvmerge, publish, timestamp


def inspect_inputs(paths, mkvmerge, folder):
    rows, mappings = [], []
    for path in paths:
        info = json.loads(app.run([mkvmerge, "-J", str(path)]))
        tracks = info.get("tracks", [])
        types = Counter(t["type"] for t in tracks)
        if types != {"video": 1, "audio": 1}:
            raise RuntimeError(f"Expected exactly one video and one audio track: {path.name}. Found {dict(types)}; no tracks will be discarded automatically.")
        by_type = {t["type"]: t for t in tracks}
        row = {"file": str(path)}
        for kind in ("video", "audio"):
            track = by_type[kind]
            props = track.get("properties", {})
            row[kind] = {"id": track["id"], "codec": track.get("codec"), "codec_id": props.get("codec_id") or track.get("codec"),
                         "resolution": props.get("pixel_dimensions"), "display_dimensions": props.get("display_dimensions"),
                         "sample_rate": props.get("audio_sampling_frequency"),
                         "channels": props.get("audio_channels")}
        rows.append(row)
        mappings.append(by_type)
    app.write_json(folder / "formats.json", rows)
    lines = []
    for row in rows:
        lines.extend([Path(row["file"]).name,
                      "  Video: " + str(row["video"]), "  Audio: " + str(row["audio"])])
    (folder / "formats.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    differences = []
    for kind, keys in (("video", ("codec_id", "resolution", "display_dimensions")), ("audio", ("codec_id", "sample_rate", "channels"))):
        for key in keys:
            values = {str(row[kind][key]) for row in rows}
            if len(values) > 1:
                differences.append(f"{kind} {key}: " + ", ".join(sorted(values)))
    if differences:
        raise RuntimeError("Held to preserve original formats and resolution: " + "; ".join(differences) + f". See {folder / 'formats.txt'}. No conversion was performed.")
    return rows, mappings


def packet_digest(path, stream, digest=None):
    """Hash compressed packets in stream order; no decoding or encoding."""
    digest = digest if digest is not None else hashlib.sha256()
    args = [app.executable("ffprobe"), "-v", "error", "-select_streams", stream,
            "-show_packets", "-show_data_hash", "sha256", "-show_entries", "packet=data_hash", "-of", "compact=p=0", str(path)]
    count = 0
    with tempfile.TemporaryFile() as errors:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=errors, text=True, encoding="utf-8", errors="replace")
        try:
            for line in process.stdout:
                match = re.search(r"data_hash=SHA256:([0-9a-fA-F]{64})", line)
                if match:
                    digest.update(bytes.fromhex(match[1]))
                    count += 1
            code = process.wait()
        except BaseException:
            process.kill()
            process.wait()
            raise
        finally:
            process.stdout.close()
        errors.seek(0)
        error_text = errors.read().decode("utf-8", errors="replace").strip()
        if code or error_text or not count:
            raise RuntimeError(f"Could not verify compressed packets for {path.name}: {error_text or 'no packets found'}")
    return digest, count


def append_episode(episode, output, mkvmerge, decode_check=False):
    number = episode["number"]
    clips = episode["clips"]
    if episode["issues"] or not clips or any(not c.get("path") for c in clips):
        raise RuntimeError("Episode has unresolved or missing clips; originals were left alone.")
    paths = [Path(c["path"]).resolve() for c in clips]
    if len(paths) != len(set(paths)):
        raise RuntimeError("Episode contains the same input file more than once. Rescan first.")
    sources = []
    for clip, path in zip(clips, paths):
        stat = path.stat()
        if stat.st_size != clip["size"] or stat.st_mtime_ns != clip["mtime_ns"]:
            raise RuntimeError(f"File changed since scanning; rescan: {path.name}")
        sources.append({"path": str(path), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns,
                        "id": clip.get("id"), "chapter": clip.get("chapter", app.chapter_title(clip["title"]))})
    output = Path(output).resolve()
    name = episode["output"]
    if Path(name).name != name or "/" in name or "\\" in name or not name.lower().endswith(".mkv"):
        raise RuntimeError("Output name must be a plain MKV filename.")
    output.mkdir(parents=True, exist_ok=True)
    destination = output / name
    if destination in paths:
        raise RuntimeError("Output overlaps an input file.")
    folder = output / "_reports" / f"E{number:02}"
    folder.mkdir(parents=True, exist_ok=True)
    receipt_path = folder / "receipt.json"
    request = {"sources": sources, "method": "mkvmerge-original-streams-v1"}
    if destination.exists():
        if receipt_path.exists():
            saved = app.read_json(receipt_path)
            stat = destination.stat()
            if saved.get("request") == request and saved.get("size") == stat.st_size and saved.get("mtime_ns") == stat.st_mtime_ns:
                if decode_check and not saved.get("decode_checked"):
                    decode_output(destination)
                    saved["decode_checked"] = True
                    app.write_json(receipt_path, saved)
                return {"episode": number, "status": "ALREADY COMPLETED", "output": str(destination)}
        raise RuntimeError("Output already exists without a matching batch receipt. It will not be overwritten.")
    if (folder / "candidate.NEEDS-REVIEW.mkv").exists():
        raise RuntimeError("A previous candidate needs review. Select a new output folder to retry; existing files will not be overwritten.")
    rows, mappings = inspect_inputs(paths, mkvmerge, folder)
    durations = [app.media_info(path)[0] for path in paths]
    if shutil.disk_usage(output).free < sum(p.stat().st_size for p in paths) * 2.2:
        raise RuntimeError("Insufficient free disk space for this episode.")
    chapters = ET.Element("Chapters")
    edition = ET.SubElement(chapters, "EditionEntry")
    elapsed = 0
    for source, duration in zip(sources, durations):
        atom = ET.SubElement(edition, "ChapterAtom")
        ET.SubElement(atom, "ChapterTimeStart").text = timestamp(elapsed)
        display = ET.SubElement(atom, "ChapterDisplay")
        ET.SubElement(display, "ChapterString").text = source["chapter"]
        ET.SubElement(display, "ChapterLanguage").text = "eng"
        elapsed += duration
    chapter_path = folder / "chapters.xml"
    ET.ElementTree(chapters).write(chapter_path, encoding="utf-8", xml_declaration=True)
    (folder / "ordered-files.txt").write_text("\n".join(f"{i:02}. {s['chapter']}\n    {s['path']}" for i, s in enumerate(sources, 1)) + "\n", encoding="utf-8")
    # Map by track TYPE even if the files store audio/video in different orders.
    append_to = []
    for i in range(1, len(paths)):
        for kind in ("video", "audio"):
            append_to.append(f"{i}:{mappings[i][kind]['id']}:{i-1}:{mappings[i-1][kind]['id']}")
    with tempfile.TemporaryDirectory(prefix=f"E{number:02}-", dir=folder) as temporary:
        partial = Path(temporary) / "candidate.mkv"
        args = ["--output", str(partial), "--title", destination.stem, "--append-mode", "file",
                "--track-order", f"0:{mappings[0]['video']['id']},0:{mappings[0]['audio']['id']}", "--chapters", str(chapter_path)]
        if append_to:
            args.extend(["--append-to", ",".join(append_to)])
        for i, path in enumerate(paths):
            if i:
                args.append("+")
            args.extend(["--no-chapters", "--no-attachments", "--no-global-tags", "--no-track-tags", str(path)])
        options = folder / "mkvmerge-options.json"
        app.write_json(options, args)
        print(f"  E{number:02}: appending {len(paths)} clips without encoding or resizing...", flush=True)
        process = subprocess.run([mkvmerge, "@" + str(options)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
        (folder / "mkvmerge.log").write_text(f"Exit code: {process.returncode}\n{process.stdout}\n{process.stderr}", encoding="utf-8")
        args[1] = str(folder / "manual-rerun.mkv")
        app.write_json(options, args)
        if process.returncode not in (0, 1) or not partial.is_file():
            raise RuntimeError(f"MKVToolNix rejected the append. See {folder / 'mkvmerge.log'}.")
        problems = ["MKVToolNix reported warnings; see mkvmerge.log."] if process.returncode else []
        try:
            info = app.probe(partial)
            if abs(float(info["format"]["duration"]) - sum(durations)) > max(1, len(paths) * 0.1):
                raise RuntimeError("Output duration differs from the source total.")
            output_chapters = info.get("chapters", [])
            if [c.get("tags", {}).get("title") for c in output_chapters] != [s["chapter"] for s in sources]:
                raise RuntimeError("Chapter names/count differ from the planned clips.")
            elapsed = 0
            for chapter, duration in zip(output_chapters, durations):
                if abs(float(chapter["start_time"]) - elapsed) > 0.002:
                    raise RuntimeError("Chapter boundaries differ from the planned timestamps.")
                elapsed += duration
            print("  Verifying original compressed video/audio packets...", flush=True)
            for stream in ("v:0", "a:0"):
                digest, count = hashlib.sha256(), 0
                for path in paths:
                    digest, n = packet_digest(path, stream, digest)
                    count += n
                actual, actual_count = packet_digest(partial, stream)
                if digest.digest() != actual.digest() or count != actual_count:
                    raise RuntimeError(f"Compressed {stream} packets do not exactly match the original clips in order.")
            if decode_check:
                decode_output(partial)
        except (RuntimeError, ValueError, KeyError) as error:
            problems.append(str(error))
        if problems:
            candidate = folder / "candidate.NEEDS-REVIEW.mkv"
            publish(partial, candidate)
            return {"episode": number, "status": "NEEDS REVIEW", "candidate": str(candidate), "reasons": problems}
        publish(partial, destination)
        stat = destination.stat()
        app.write_json(receipt_path, {"request": request, "size": stat.st_size, "mtime_ns": stat.st_mtime_ns,
                                      "packets_verified": True, "decode_checked": decode_check})
        return {"episode": number, "status": "COMPLETED", "output": str(destination)}


def decode_output(path):
    print("  Performing optional full decoding check...", flush=True)
    app.run([app.executable("ffmpeg"), "-v", "error", "-xerror", "-nostdin", "-err_detect", "explode", "-i", str(path),
             "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])


def save_summary(output, results, missing=()):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    app.write_json(output / "batch-summary.json", results)
    lines = ["MKVTOOLNIX ORIGINAL-QUALITY BATCH", "No encoding or resizing. Only complete, compatible matches are appended.",
             "Compressed packet identity is checked. Check playback/transitions and audio sync manually.", ""]
    counts = Counter(r["status"] for r in results)
    lines.append("; ".join(f"{status}: {n}" for status, n in sorted(counts.items())))
    if missing:
        lines.append("Episode playlists absent from the plan: " + ", ".join(f"E{n:02}" for n in missing))
    for result in results:
        lines.extend(["", f"E{result['episode']:02} — {result['status']}"])
        lines.extend("  " + s for s in result.get("reasons", []))
        if result.get("output"):
            lines.append("  " + result["output"])
    (output / "batch-summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def batch(plan, output, episodes=None, mkvmerge=None, decode_check=False):
    mkvmerge = find_mkvmerge(mkvmerge)
    app.executable("ffprobe")
    if decode_check:
        app.executable("ffmpeg")
    selected = [e for e in plan["episodes"] if not episodes or e["number"] in episodes]
    if not selected:
        raise RuntimeError("No selected episodes found in the plan.")
    numbers = [e["number"] for e in selected]
    if any(not isinstance(n, int) or not 1 <= n <= 91 for n in numbers):
        raise RuntimeError("Plan contains an invalid episode number outside E01–E91.")
    if len(numbers) != len(set(numbers)):
        raise RuntimeError("Duplicate episode numbers in the plan; rescan before processing.")
    results = []
    missing = sorted((set(episodes) if episodes else set(range(1, 92))) - set(numbers))
    for episode in sorted(selected, key=lambda e: e["number"]):
        print(f"E{episode['number']:02}...", flush=True)
        try:
            if episode["issues"]:
                result = {"episode": episode["number"], "status": "SKIPPED — MATCHING", "reasons": episode["issues"]}
            else:
                result = append_episode(episode, output, mkvmerge, decode_check)
        except (RuntimeError, OSError, ValueError, KeyError) as error:
            result = {"episode": episode["number"], "status": "HELD", "reasons": [str(error)]}
        results.append(result)
        save_summary(output, results, missing)
        print(f"  {result['status']}", flush=True)
        for reason in result.get("reasons", [])[:2]:
            print("  " + reason, flush=True)
    print(f"Batch finished. Read {Path(output).resolve() / 'batch-summary.txt'}", flush=True)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default="work/plan.json")
    parser.add_argument("--output", default=str(Path.home() / "Videos" / "LFDH Original Quality"))
    parser.add_argument("--episodes", type=int, nargs="+")
    parser.add_argument("--mkvmerge")
    parser.add_argument("--decode-check", action="store_true", help="Also fully decode each result; slower, never re-encodes")
    args = parser.parse_args()
    results = batch(app.read_json(args.plan), args.output, args.episodes, args.mkvmerge, args.decode_check)
    return 1 if any(r["status"] in ("HELD", "NEEDS REVIEW") for r in results) else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Stopped. Original clips and completed episodes are retained.", file=sys.stderr)
        sys.exit(130)
