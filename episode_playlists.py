"""Create episode folders with ordered playlists; never move or modify videos."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


PLAYER = r'''@echo off
setlocal EnableExtensions
pushd "%~dp0"
if errorlevel 1 goto folder_failed
set "LFDH_PLAYLIST=%CD%\Play Episode.m3u8"
set "LFDH_VLC_ARGS=--no-one-instance --no-random --no-loop --no-repeat --play-and-exit"
if exist "%ProgramFiles%\VideoLAN\VLC\vlc.exe" goto vlc_64
if exist "%ProgramFiles(x86)%\VideoLAN\VLC\vlc.exe" goto vlc_32
where vlc.exe >nul 2>nul
if not errorlevel 1 goto vlc_path
where mpv.exe >nul 2>nul
if not errorlevel 1 goto mpv_path
echo Install VLC from https://www.videolan.org/vlc/ or run:
echo winget install --id VideoLAN.VLC --exact
echo You can also open Play Episode.m3u8 using an installed media player.
popd
pause
exit /b 1
:vlc_64
"%ProgramFiles%\VideoLAN\VLC\vlc.exe" %LFDH_VLC_ARGS% "%LFDH_PLAYLIST%"
goto done
:vlc_32
"%ProgramFiles(x86)%\VideoLAN\VLC\vlc.exe" %LFDH_VLC_ARGS% "%LFDH_PLAYLIST%"
goto done
:vlc_path
vlc.exe %LFDH_VLC_ARGS% "%LFDH_PLAYLIST%"
goto done
:mpv_path
mpv.exe --shuffle=no --loop-playlist=no --loop-file=no --playlist="%LFDH_PLAYLIST%"
:done
set "LFDH_RESULT=%ERRORLEVEL%"
popd
exit /b %LFDH_RESULT%
:folder_failed
echo Cannot open the episode folder. Check its network connection.
pause
exit /b 1
'''


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, content):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    # Do not overwrite a pre-existing temporary file belonging to someone else.
    with temporary.open("xb") as file:
        file.write(content)
    temporary.replace(path)


def make_episode(episode, output):
    number = episode["number"]
    if not isinstance(number, int) or not 1 <= number <= 91:
        raise RuntimeError("Invalid episode number.")
    if episode["issues"] or not episode["clips"]:
        raise RuntimeError("Episode has unresolved or missing matches; no partial playlist was created.")
    clips, seen = [], set()
    for clip in episode["clips"]:
        if not clip.get("path"):
            raise RuntimeError("Episode contains an unmatched clip.")
        path = Path(clip["path"]).resolve()
        stat = path.stat()
        if stat.st_size != clip["size"] or stat.st_mtime_ns != clip["mtime_ns"]:
            raise RuntimeError(f"File changed since scanning; rescan: {path.name}")
        if path in seen:
            raise RuntimeError("Episode repeats a local clip; rescan before creating a playlist.")
        seen.add(path)
        title = re.sub(r"[\r\n]+", " ", clip.get("chapter") or clip["title"])
        clips.append((path, title))
    label = Path(episode["output"]).stem
    label = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " - ", label).rstrip(" .")[:160]
    if not label.startswith(f"Live from Daryl's House - E{number:02} - "):
        raise RuntimeError("Unexpected episode output name. Use the current reviewed plan.")
    folder = Path(output).resolve() / label
    if folder in seen:
        raise RuntimeError("Episode folder overlaps a source video.")
    m3u = ["#EXTM3U", "#PLAYLIST:" + label]
    for path, title in clips:
        m3u.extend(["#EXTINF:-1," + title, path.as_uri()])
    notes = [label, "", "PLAYBACK", "Double-click Play Episode.bat, or open Play Episode.m3u8 in VLC/mpv.",
             "Use normal playlist order; disable shuffle/repeat in your player.",
             "", "ORIGINALS", "The videos remain at their existing paths. Nothing was moved, copied, encoded or resized.",
             "Keep the original files accessible. Network shares must be connected during playback.",
             "These are separate videos played in order, not a merged video. Brief transitions can occur as codecs/resolutions change.",
             "", "ORDERED CLIPS"]
    for i, (path, title) in enumerate(clips, 1):
        notes.extend([f"{i:02}. {title}", f"    {path}"])
    contents = {"Play Episode.m3u8": ("\n".join(m3u) + "\n").encode("utf-8"),
                "Play Episode.bat": PLAYER.replace("\n", "\r\n").encode("ascii"),
                "Episode Info.txt": ("\n".join(notes) + "\n").encode("utf-8")}
    marker = folder / ".mergegoblin-playlist.json"
    folder.mkdir(parents=True, exist_ok=True)
    if marker.exists():
        saved = load(marker)
        if saved.get("generator") != "mergegoblin-playlists-v1" or saved.get("episode") != number:
            raise RuntimeError("Existing episode folder has an unknown ownership marker; it was left unchanged.")
        for name, digest in saved["files"].items():
            if name not in contents or not (folder / name).is_file() or hashlib.sha256((folder / name).read_bytes()).hexdigest() != digest:
                raise RuntimeError("An existing generated file was edited or removed; choose a new output folder to preserve your changes.")
        if all((folder / name).read_bytes() == data for name, data in contents.items()):
            return {"episode": number, "status": "ALREADY CREATED", "folder": str(folder), "clips": len(clips)}
    elif any((folder / name).exists() for name in contents):
        raise RuntimeError("An episode output file already exists without a generator marker; nothing was overwritten.")
    for name, data in contents.items():
        write(folder / name, data)
    saved = {"generator": "mergegoblin-playlists-v1", "episode": number,
             "files": {name: hashlib.sha256(data).hexdigest() for name, data in contents.items()}}
    write(marker, (json.dumps(saved, indent=2) + "\n").encode("utf-8"))
    return {"episode": number, "status": "CREATED", "folder": str(folder), "clips": len(clips)}


def create(plan, output, summary=None, episodes=None, all_matched=False):
    if episodes:
        wanted = set(episodes)
    elif all_matched:
        wanted = {e["number"] for e in plan["episodes"]}
    elif summary is not None:
        wanted = {r["episode"] for r in summary if r["status"] in ("HELD", "NEEDS REVIEW")}
    else:
        raise RuntimeError("The MKVToolNix batch summary was not found. Use --batch-summary to select it, or --all-matched to create playlists for every fully matched episode.")
    selected = [e for e in plan["episodes"] if e["number"] in wanted]
    numbers = [e["number"] for e in selected]
    if len(numbers) != len(set(numbers)):
        raise RuntimeError("Duplicate episode numbers in the plan. Rescan before proceeding.")
    results = []
    for episode in sorted(selected, key=lambda e: e["number"]):
        try:
            result = make_episode(episode, output)
        except (RuntimeError, OSError, ValueError, KeyError) as error:
            result = {"episode": episode["number"], "status": "HELD", "reason": str(error)}
        results.append(result)
        print(f"E{result['episode']:02}: {result['status']}" + (" — " + result["reason"] if result.get("reason") else ""), flush=True)
    for number in sorted(wanted - set(numbers)):
        results.append({"episode": number, "status": "HELD", "reason": "Episode is absent from the plan."})
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    counts = Counter(r["status"] for r in results)
    lines = ["EPISODE PLAYLIST FOLDERS", "Original videos remain untouched at their existing locations.",
             "Default selection: episodes held by the MKVToolNix batch. Existing merged MKVs are not modified.",
             "; ".join(f"{k}: {v}" for k, v in sorted(counts.items())), ""]
    for result in results:
        lines.append(f"E{result['episode']:02}: {result['status']} — {result.get('folder') or result.get('reason')}")
    if not wanted:
        lines.append("No episodes were held by the supplied MKVToolNix batch summary.")
    data = ("\n".join(lines) + "\n").encode("utf-8")
    report = output / "playlist-summary.txt"
    suffix = 2
    while report.exists() and report.read_bytes() != data:
        report = output / f"playlist-summary-{suffix}.txt"
        suffix += 1
    if not report.exists():
        write(report, data)
    print(f"\nOpen the episode folders in: {output}\nReport: {report}", flush=True)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default="work/plan.json")
    parser.add_argument("--batch-summary", default=str(Path.home() / "Videos" / "LFDH Original Quality" / "batch-summary.json"))
    parser.add_argument("--output", default=str(Path.home() / "Videos" / "LFDH Episode Playlists"))
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--episodes", type=int, nargs="+")
    selection.add_argument("--all-matched", action="store_true")
    args = parser.parse_args()
    summary = load(args.batch_summary) if not args.episodes and not args.all_matched and Path(args.batch_summary).exists() else None
    results = create(load(args.plan), args.output, summary, args.episodes, args.all_matched)
    return 1 if any(r["status"] == "HELD" for r in results) else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Stopped. Original videos were not changed.", file=sys.stderr)
        sys.exit(130)
