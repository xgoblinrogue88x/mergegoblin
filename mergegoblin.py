"""Playlist-guided local merging. Source media are never written or removed."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import difflib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

CHANNEL = "https://www.youtube.com/@realdarylhall/playlists"
VIDEO_EXTENSIONS = {".mkv", ".mp4", ".webm", ".mov", ".m4v", ".avi"}
EPISODE = re.compile(r"\b(?:episode|ep\.?|e)\s*[#:\-]?\s*(\d{1,3})\b", re.I)
HASH_EPISODE = re.compile(r"^\s*#\s*(\d{1,3})\s*(?=[\-–—:]|$)")


def episode_number(title):
    # The channel uses '#10 - Daryl Hall hosts Chromeo…', not 'Episode 10'.
    # Collections such as 'Episodes 1 - 10' must never become single episodes.
    if re.search(r"\bepisodes\b", title, flags=re.I):
        return None
    match = HASH_EPISODE.search(title) or EPISODE.search(title)
    if not match:
        return None
    # Also reject singular labels used for a numeric range.
    if re.match(r"\s*[-–—]\s*\d+\b", title[match.end():]):
        return None
    number = int(match[1])
    return number if 1 <= number <= 91 else None


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def normal(text):
    text = re.sub(r"\s*\(Live From Daryl['’]s House\)\s*", " ", text, flags=re.I)
    return literal_normal(text)


def literal_normal(text):
    """Keep show labels so different titled uploads remain distinguishable."""
    text = unicodedata.normalize("NFKD", text).casefold()
    return "".join(c for c in text if c.isalnum() and not unicodedata.combining(c))


def filename_title(path):
    # yt-dlp's optional trailing video ID is not part of the title.
    return re.sub(r"\s*\[[A-Za-z0-9_-]{11}\]$", "", path.stem)


def guest(title):
    prefix = title.split(" - ", 1)[0]
    return re.sub(r"^Daryl Hall\s*(?:&|and)\s*", "", prefix, flags=re.I).strip()


def chapter_title(title):
    title = re.sub(r"\s*\(Live From Daryl['’]s House\)\s*", " ", title, flags=re.I).strip()
    return title.split(" - ", 1)[-1].strip()


def safe_name(text):
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', " - ", text).rstrip(" .")[:180]


def episode_label(title):
    body = re.sub(r"^\s*(?:#\s*\d+|(?:episode|ep\.?|e)\s*#?\s*\d+)\s*[-–—:]?\s*", "", title, flags=re.I)
    body = re.sub(r"\s+(?:on|of)\s+Live From Daryl['’]s House.*$", "", body, flags=re.I)
    body = re.sub(r"^Daryl Hall hosts\s+", "", body, flags=re.I)
    body = re.sub(r"^Daryl Hall['’]s\s+", "", body, flags=re.I)
    return body.strip().replace("’", "'").replace('"', "") or "UNRESOLVED"


def fetch_catalog(path):
    try:
        import yt_dlp
    except ImportError as exc:
        raise RuntimeError("Install dependencies: python -m pip install -r requirements.txt") from exc
    # Metadata only. Never download videos or bypass TLS verification.
    options = {"extract_flat": True, "skip_download": True, "ignoreerrors": False,
               "quiet": True, "retries": 3, "socket_timeout": 30}
    def extract(ydl, url):
        try:
            return ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError as error:
            raise RuntimeError(f"Could not read YouTube metadata. Update yt-dlp and check access on this machine.\n{error}") from error

    with yt_dlp.YoutubeDL(options) as ydl:
        print("Reading channel playlists (metadata only)...", flush=True)
        channel = extract(ydl, CHANNEL)
        if not channel or channel.get("entries") is None:
            raise RuntimeError("YouTube returned no playlist listing. No catalog saved.")
        entries = list(channel["entries"])
        discovery_path = Path(path).with_name("channel-playlists.json")
        write_json(discovery_path, {"source": CHANNEL, "playlists": [
            {"id": (e or {}).get("id"), "title": (e or {}).get("title")} for e in entries]})
        episodes, ignored = [], []
        for entry in entries:
            if not entry:
                raise RuntimeError("Channel contains an unreadable playlist entry; retry before merging.")
            title = entry.get("title") or ""
            number = episode_number(title)
            if number is None:
                ignored.append({"title": title, "id": entry.get("id")})
                continue
            playlist_id = entry.get("id")
            if not playlist_id or not re.fullmatch(r"[A-Za-z0-9_-]+", playlist_id):
                raise RuntimeError(f"Unusable playlist ID for {title!r}.")
            url = f"https://www.youtube.com/playlist?list={playlist_id}"
            print(f"Reading E{number:02}: {title}", flush=True)
            info = extract(ydl, url)
            if not info or info.get("entries") is None:
                raise RuntimeError(f"Could not read {url}; no new catalog saved.")
            clips = []
            for index, clip in enumerate(info["entries"], 1):
                clips.append({"id": (clip or {}).get("id"),
                              "title": (clip or {}).get("title") or "[Unavailable video]",
                              "playlist_index": (clip or {}).get("playlist_index") or index})
            episodes.append({"number": number, "title": title, "url": url, "clips": clips})
    if not episodes:
        raise RuntimeError(f"No single-episode playlists recognized. Titles and IDs were saved to {discovery_path} for inspection.")
    catalog = {"source": CHANNEL, "episodes": episodes, "ignored_playlists": ignored}
    write_json(path, catalog)
    print(f"Saved {len(episodes)} episode playlists to {path}")
    return catalog


def make_plan(folder, catalog, matches=None):
    folder = Path(folder).resolve()
    if not folder.is_dir():
        raise RuntimeError(f"Input folder does not exist: {folder}")
    files = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS)
    if not files:
        raise RuntimeError("No video files found in the selected folder.")
    matches = matches or {}
    by_name = {p.name: p for p in files}
    for video_id, filename in matches.items():
        if not isinstance(filename, str) or filename not in by_name:
            raise RuntimeError(f"Manual match {video_id!r} must name a video in the selected folder.")
    titles = defaultdict(list)
    literal_titles = defaultdict(list)
    ids = defaultdict(list)
    claims = defaultdict(set)
    for file in files:
        titles[normal(filename_title(file))].append(file)
        literal_titles[literal_normal(filename_title(file))].append(file)
        match = re.search(r"\[([A-Za-z0-9_-]{11})\]$", file.stem)
        if match:
            ids[match[1]].append(file)
            claims[file].add(match[1])
    for video_id, filename in matches.items():
        claims[by_name[filename]].add(video_id)
    if any(len(values) > 1 for values in claims.values()):
        raise RuntimeError("One local file is assigned to different video IDs. Correct matches.json before scanning.")
    catalog_titles = defaultdict(set)
    catalog_literals = defaultdict(set)
    for episode in catalog["episodes"]:
        for clip in episode["clips"]:
            if clip.get("id"):
                catalog_titles[normal(clip["title"])].add(clip["id"])
                catalog_literals[literal_normal(clip["title"])].add(clip["id"])
    episode_counts = Counter(e["number"] for e in catalog["episodes"])
    episodes = []
    for episode in sorted(catalog["episodes"], key=lambda x: x["number"]):
        number = episode["number"]
        if not isinstance(number, int) or not 1 <= number <= 91:
            raise RuntimeError(f"Invalid episode number in catalog: {number!r}")
        clips, issues, notes = [], [], []
        seen_ids = set()
        if episode_counts[number] != 1:
            issues.append("Multiple playlists claim this episode number; resolve against an episode guide.")
        for clip in episode["clips"]:
            title = clip["title"]
            identity_conflict = False
            video_id = clip.get("id")
            if video_id and video_id in seen_ids:
                notes.append(f"Removed repeated playlist entry for video {video_id}: {title}")
                continue
            if video_id:
                seen_ids.add(video_id)
            override = matches.get(video_id)
            candidates = [by_name[override]] if override else ids.get(video_id, [])
            match_method = "manual" if override else "video_id" if candidates else None
            if not candidates:
                candidates = literal_titles.get(literal_normal(title), [])
                match_method = "exact_title"
                identities = catalog_literals[literal_normal(title)]
                if not candidates:
                    candidates = titles.get(normal(title), [])
                    match_method = "normalized_title"
                    identities = catalog_titles[normal(title)]
                candidates = [p for p in candidates if not claims[p] or claims[p] == {video_id}]
                if candidates and len(identities) > 1:
                    issues.append(f"Title belongs to different YouTube video IDs; explicit match needed: {title} ({', '.join(sorted(identities))})")
                    identity_conflict = True
                    candidates = []
            candidate = candidates[0] if len(candidates) == 1 else None
            row = {"title": title, "chapter": chapter_title(title), "id": video_id,
                   "match_method": match_method if candidate else None, "path": str(candidate) if candidate else None}
            if candidate:
                stat = candidate.stat()
                row.update(size=stat.st_size, mtime_ns=stat.st_mtime_ns)
            else:
                if not identity_conflict:
                    issues.append(f"{'Ambiguous' if candidates else 'Missing'} clip: {title}")
                close = difflib.get_close_matches(normal(title), list(titles), n=3, cutoff=0.7)
                row["suggestions"] = [str(p) for key in close for p in titles[key]]
            clips.append(row)
        if not clips:
            issues.append("Playlist has no visible clips.")
        artist = episode_label(episode["title"])
        episodes.append({"number": number, "playlist_title": episode["title"],
                         "playlist_url": episode["url"],
                         "output": safe_name(f"Live from Daryl's House - E{number:02} - {artist}") + ".mkv",
                         "issues": issues, "notes": notes, "clips": clips})
    uses = defaultdict(list)
    for episode in episodes:
        for clip in episode["clips"]:
            if clip["path"]:
                uses[clip["path"]].append((episode, clip["id"]))
    for path, used in uses.items():
        identities = {video_id for _, video_id in used}
        if len(used) > 1 and (len(identities) > 1 or None in identities):
            for episode, _ in used:
                issue = f"Local file matched to different or unknown video IDs: {Path(path).name}"
                if issue not in episode["issues"]:
                    episode["issues"].append(issue)
        elif len(used) > 1:
            numbers = sorted({e["number"] for e, _ in used})
            for episode, _ in used:
                episode["notes"].append(f"Verified shared video {next(iter(identities))} in episodes {numbers}: {Path(path).name}")
    found = {e["number"] for e in episodes}
    return {"version": 2, "input_folder": str(folder),
            "notice": "Playlist order needs human review; complete means matched to visible playlist, not verified broadcast completeness.",
            "undiscovered_episodes": sorted(set(range(1, 92)) - found),
            "unmatched_files": [str(p) for p in files if str(p) not in uses], "episodes": episodes}


def save_report(plan, path):
    ready = sum(not e["issues"] for e in plan["episodes"])
    lines = ["LIVE FROM DARYL'S HOUSE — MERGE REVIEW", "", plan["notice"],
             f"Fully matched with no holds: {ready} of {len(plan['episodes'])} discovered episodes.",
             "Missing episode playlists: " + ", ".join(f"E{n:02}" for n in plan["undiscovered_episodes"]), ""]
    for episode in plan["episodes"]:
        status = "HOLD" if episode["issues"] else "MATCHED — review order"
        lines.extend([f"{status}: {episode['output']}", episode["playlist_title"], episode["playlist_url"]])
        for i, clip in enumerate(episode["clips"], 1):
            lines.append(f"  {i:02}. {clip['title']} => {Path(clip['path']).name if clip['path'] else 'NOT MATCHED'}")
            if not clip["path"] and clip.get("id"):
                lines.append(f"      Expected video: https://www.youtube.com/watch?v={clip['id']}")
            for suggestion in clip.get("suggestions", []):
                lines.append(f"      Possible match (not selected): {Path(suggestion).name}")
        lines.extend("  ! " + issue for issue in episode["issues"])
        lines.extend("  Note: " + note for note in episode.get("notes", []))
        lines.append("")
    lines.append("LOCAL FILES NOT ASSIGNED TO A PLAYLIST:")
    lines.extend(plan["unmatched_files"])
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def executable(name):
    local = Path(__file__).resolve().parent / "tools" / (name + ".exe" if os.name == "nt" else name)
    found = str(local) if local.is_file() else shutil.which(name)
    if not found:
        raise RuntimeError(f"{name} not found. Put ffmpeg.exe and ffprobe.exe in tools, or install FFmpeg on PATH.")
    return found


def run(args, timeout=None):
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    if process.returncode:
        raise RuntimeError(f"{Path(args[0]).name} failed:\n{process.stderr[-6000:]}")
    return process.stdout


def probe(path):
    return json.loads(run([executable("ffprobe"), "-v", "error", "-show_streams", "-show_format", "-show_chapters", "-show_data", "-of", "json", str(path)]))


def media_info(path):
    info = probe(path)
    streams = info["streams"]
    videos = [s for s in streams if s["codec_type"] == "video"]
    audios = [s for s in streams if s["codec_type"] == "audio"]
    if len(videos) != 1 or len(audios) != 1 or len(streams) != 2:
        raise RuntimeError(f"Expected one video and one audio stream, with no additional streams: {path}")
    duration = float(info["format"]["duration"])
    if duration <= 0:
        raise RuntimeError(f"Invalid duration: {path}")
    fields = ("codec_type", "codec_name", "codec_tag_string", "profile", "level", "width", "height", "pix_fmt",
              "sample_aspect_ratio", "r_frame_rate", "time_base", "sample_rate", "channels", "channel_layout",
              "color_range", "color_space", "color_transfer", "color_primaries", "extradata")
    signature = tuple(tuple(s.get(k) for k in fields) for s in streams)
    return duration, signature, info


def metadata_escape(text):
    return re.sub(r"([\\=;#\n\r])", lambda m: " " if m[0] in "\n\r" else "\\" + m[0], text)


PRESETS = ("ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow")


def video_encoding_args(encoder, preset):
    if preset not in PRESETS:
        raise RuntimeError(f"Unsupported CPU preset: {preset}")
    if encoder == "amd":
        return ["-c:v", "h264_amf", "-quality", "speed", "-rc", "cqp", "-qp_i", "20", "-qp_p", "20", "-bf", "0"]
    if encoder == "cpu":
        return ["-c:v", "libx264", "-preset", preset, "-crf", "18"]
    raise RuntimeError(f"Unsupported encoder: {encoder}")


def resolve_encoder(encoder, preset):
    if encoder not in ("cpu", "amd", "auto"):
        raise RuntimeError(f"Unsupported encoder: {encoder}")
    if encoder == "cpu":
        video_encoding_args("cpu", preset)
        return "cpu"
    try:
        # Test real driver initialization, not just whether FFmpeg lists AMF.
        run([executable("ffmpeg"), "-v", "error", "-nostdin", "-f", "lavfi", "-i",
             "color=size=1280x720:rate=30:duration=0.1", "-frames:v", "3",
             *video_encoding_args("amd", preset), "-f", "null", "-"], timeout=20)
    except (RuntimeError, subprocess.TimeoutExpired, OSError) as error:
        if encoder == "amd":
            raise RuntimeError(f"AMD hardware encoding is unavailable. Try --encoder cpu --preset veryfast.\n{error}") from error
        print(f"AMD hardware encoding unavailable; using CPU preset {preset}.", flush=True)
        return "cpu"
    print("AMD hardware encoding test passed; using h264_amf.", flush=True)
    return "amd"


def merge_episode(episode, output_folder, convert=False, preset="veryfast", encoder="cpu"):
    if episode["issues"]:
        raise RuntimeError("Episode has unresolved matching issues.")
    output_folder = Path(output_folder).resolve()
    output_folder.mkdir(parents=True, exist_ok=True)
    name = episode["output"]
    if Path(name).name != name or not name.lower().endswith(".mkv") or "/" in name or "\\" in name:
        raise RuntimeError("Output must be a plain MKV filename.")
    destination = output_folder / name
    receipt = destination.with_suffix(".receipt.json")
    clips = episode["clips"]
    if not clips:
        raise RuntimeError("Episode contains no clips.")
    paths = [Path(c["path"]).resolve() for c in clips]
    if len(set(paths)) != len(paths) or destination in paths:
        raise RuntimeError("Duplicate input clip or output overlaps an input.")
    source_state = []
    for clip, path in zip(clips, paths):
        stat = path.stat()
        if stat.st_size != clip["size"] or stat.st_mtime_ns != clip["mtime_ns"]:
            raise RuntimeError(f"File changed since scanning; rescan: {path.name}")
        source_state.append({"path": str(path), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns,
                             "title": clip["title"], "chapter": clip.get("chapter", chapter_title(clip["title"]))})
    request = {"sources": source_state, "convert": convert, "number": episode["number"]}
    if destination.exists():
        if receipt.exists():
            saved = read_json(receipt)
            if saved.get("request") == request and saved.get("output_size") == destination.stat().st_size and saved.get("output_mtime_ns") == destination.stat().st_mtime_ns:
                print(f"Already completed: {name}", flush=True)
                return "skipped"
        raise RuntimeError(f"Output already exists without a matching completion receipt: {name}")
    inspected = [media_info(p) for p in paths]
    if not convert and len({item[1] for item in inspected}) != 1:
        raise RuntimeError("Video/audio formats differ. Use --convert to normalize, then merge (slower).")
    # Conservative staging allowance, including a copy fallback on filesystems without hard links.
    needed = sum(p.stat().st_size for p in paths) * (8 if convert else 3.2)
    if shutil.disk_usage(output_folder).free < needed:
        raise RuntimeError("Insufficient free space for this merge and its temporary files.")
    ffmpeg = executable("ffmpeg")
    with tempfile.TemporaryDirectory(prefix="mergegoblin-", dir=output_folder) as temporary:
        temporary = Path(temporary)
        durations, sources = [], []
        for index, (path, (duration, _, info)) in enumerate(zip(paths, inspected)):
            staged = temporary / f"clip{index:04}.mkv"
            if convert:
                print(f"  Converting clip {index + 1}/{len(paths)} with {encoder}: {path.name}", flush=True)
                first_video = next(s for s in inspected[0][2]["streams"] if s["codec_type"] == "video")
                width, height = int(first_video["width"]) // 2 * 2, int(first_video["height"]) // 2 * 2
                filters = f"scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,format=yuv420p"
                run([ffmpeg, "-v", "error", "-xerror", "-nostdin", "-n", "-i", str(path), "-map", "0:v:0", "-map", "0:a:0",
                     "-map_metadata", "-1", "-map_chapters", "-1", "-vf", filters, "-af", "aresample=48000,asetpts=PTS-STARTPTS",
                     *video_encoding_args(encoder, preset), "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k", str(staged)])
                duration = media_info(staged)[0]
            else:
                # Simple staging names avoid Windows apostrophe/backslash escaping in concat lists.
                try:
                    os.link(path, staged)
                except OSError:
                    shutil.copy2(path, staged)
            durations.append(duration)
            sources.append(staged)
        listing = temporary / "inputs.txt"
        listing.write_text("".join(f"file '{p.name}'\nduration {d:.9f}\n" for p, d in zip(sources, durations)), encoding="utf-8")
        elapsed = 0
        metadata = [";FFMETADATA1", "title=" + metadata_escape(destination.stem)]
        for clip, duration in zip(clips, durations):
            end = elapsed + round(duration * 1000)
            metadata.extend(["[CHAPTER]", "TIMEBASE=1/1000", f"START={elapsed}", f"END={end}",
                             "title=" + metadata_escape(clip.get("chapter", chapter_title(clip["title"])))])
            elapsed = end
        chapter_file = temporary / "chapters.txt"
        chapter_file.write_text("\n".join(metadata) + "\n", encoding="utf-8")
        partial = temporary / "merged.mkv"
        print("  Joining clips and writing chapters...", flush=True)
        run([ffmpeg, "-v", "error", "-xerror", "-nostdin", "-n", "-f", "concat", "-safe", "1", "-i", str(listing),
             "-f", "ffmetadata", "-i", str(chapter_file), "-map", "0:v:0", "-map", "0:a:0", "-map_metadata", "1", "-map_chapters", "1", "-c", "copy", str(partial)])
        merged = probe(partial)
        if abs(float(merged["format"]["duration"]) - elapsed / 1000) > max(0.5, len(clips) * 0.05):
            raise RuntimeError("Output duration differs from the clip total; output not accepted.")
        chapters = merged.get("chapters", [])
        if len(chapters) != len(clips) or [c.get("tags", {}).get("title") for c in chapters] != [c.get("chapter", chapter_title(c["title"])) for c in clips]:
            raise RuntimeError("Chapter verification failed; output not accepted.")
        cursor = 0
        for chapter, duration in zip(chapters, durations):
            end = cursor + round(duration * 1000)
            if abs(float(chapter["start_time"]) - cursor / 1000) > 0.001 or abs(float(chapter["end_time"]) - end / 1000) > 0.001:
                raise RuntimeError("Chapter timestamp verification failed; output not accepted.")
            cursor = end
        # Decode the entire result to catch corrupt joins; no re-encoding here.
        print("  Checking the complete episode for decoding errors...", flush=True)
        run([ffmpeg, "-v", "error", "-xerror", "-nostdin", "-i", str(partial), "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])
        # Hard-link publication is atomic and never overwrites an existing output.
        try:
            os.link(partial, destination)
        except FileExistsError:
            raise
        except OSError:
            with destination.open("xb") as target, partial.open("rb") as source:
                try:
                    shutil.copyfileobj(source, target)
                except BaseException:
                    target.close()
                    destination.unlink()
                    raise
        stat = destination.stat()
        write_json(receipt, {"request": request, "output_size": stat.st_size, "output_mtime_ns": stat.st_mtime_ns,
                             "encoding": {"encoder": encoder, "preset": preset} if convert else None})
    print(f"Completed: {name}", flush=True)
    return "merged"


def merge_plan(plan, output, numbers=None, convert=False, preset="veryfast", encoder="cpu"):
    executable("ffmpeg")
    executable("ffprobe")
    ready = [e for e in plan["episodes"] if not e["issues"] and (not numbers or e["number"] in numbers)]
    if not ready:
        raise RuntimeError("No complete, unambiguous episodes selected. Read the review report.")
    # Reuse is valid for retrospective episodes only when video identity agrees.
    uses = defaultdict(list)
    for episode in ready:
        for clip in episode["clips"]:
            uses[str(Path(clip["path"]).resolve())].append(clip.get("id"))
    if any(len(values) > 1 and (len(set(values)) != 1 or None in values) for values in uses.values()):
        raise RuntimeError("Selected episodes assign a local file to different or unknown video IDs.")
    if convert:
        encoder = resolve_encoder(encoder, preset)
    errors = []
    for episode in ready:
        print(f"Processing E{episode['number']:02} ({len(episode['clips'])} chapters)...", flush=True)
        try:
            merge_episode(episode, output, convert, preset, encoder)
        except (RuntimeError, OSError, ValueError, KeyError) as exc:
            errors.append(f"E{episode['number']:02}: {exc}")
            print(f"HELD: {errors[-1]}", flush=True)
    if errors:
        raise RuntimeError(f"{len(errors)} episode(s) held. Other completed outputs are retained.\n" + "\n".join(errors))


def choose_folder(title):
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    try:
        result = filedialog.askdirectory(title=title)
    finally:
        root.destroy()
    if not result:
        raise RuntimeError("Folder selection cancelled.")
    return result


def scan(folder, catalog_path, plan_path, refresh=False, matches_path=None):
    catalog = fetch_catalog(catalog_path) if refresh or not Path(catalog_path).exists() else read_json(catalog_path)
    matches = read_json(matches_path) if matches_path else None
    plan = make_plan(folder, catalog, matches)
    write_json(plan_path, plan)
    report = Path(plan_path).with_suffix(".txt")
    save_report(plan, report)
    ready = sum(not e["issues"] for e in plan["episodes"])
    print(f"{ready} fully matched episode(s); {len(plan['unmatched_files'])} unassigned files.\nReview: {report.resolve()}")
    return plan, report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("wizard", help="Windows folder picker and guided scan/review/merge")
    fetch = sub.add_parser("catalog", help="Fetch public YouTube playlist metadata only")
    fetch.add_argument("--catalog", default="work/catalog.json")
    scanning = sub.add_parser("scan", help="Match local files without changing media")
    scanning.add_argument("--input", required=True)
    scanning.add_argument("--catalog", default="work/catalog.json")
    scanning.add_argument("--plan", default="work/plan.json")
    scanning.add_argument("--refresh", action="store_true")
    scanning.add_argument("--matches", help="Optional JSON mapping YouTube video IDs to exact local filenames")
    merging = sub.add_parser("merge", help="Merge complete episodes from a reviewed plan")
    merging.add_argument("--plan", default="work/plan.json")
    merging.add_argument("--output", required=True)
    merging.add_argument("--episodes", type=int, nargs="+")
    merging.add_argument("--convert", action="store_true", help="Re-encode to consistent H.264/AAC; slower, lossy")
    merging.add_argument("--preset", choices=PRESETS, default="veryfast", help="CPU encoding speed (default: veryfast); faster presets generally produce larger files")
    merging.add_argument("--encoder", choices=("cpu", "amd", "auto"), default="cpu", help="auto tests AMD hardware encoding, falling back to CPU; requires --convert")
    merging.add_argument("--reviewed", action="store_true", required=True, help="Confirm episode identities and playlist sequence were reviewed")
    args = parser.parse_args(argv)
    if args.command == "catalog":
        fetch_catalog(args.catalog)
    elif args.command == "scan":
        scan(args.input, args.catalog, args.plan, args.refresh, args.matches)
    elif args.command == "merge":
        if not args.convert and (args.encoder != "cpu" or args.preset != "veryfast"):
            raise RuntimeError("--encoder and --preset apply to --convert mode only.")
        merge_plan(read_json(args.plan), args.output, args.episodes, args.convert, args.preset, args.encoder)
    else:
        executable("ffmpeg")
        executable("ffprobe")
        folder = choose_folder("Choose the folder containing your downloaded clips")
        matches = "work/matches.json" if Path("work/matches.json").exists() else None
        plan, report = scan(folder, "work/catalog.json", "work/plan.json", matches_path=matches)
        if os.name == "nt":
            os.startfile(str(report.resolve()))
        if not any(not e["issues"] for e in plan["episodes"]):
            print("No fully matched episodes yet. Read the report and resolve matches, then scan again.")
            return
        print("\nCheck the report's episode numbers, guest names and clip order against the linked playlists.")
        print("MATCHED means complete relative to the visible playlist; it does not certify original broadcast completeness.")
        if input("Type MERGE after reviewing, or press Enter to stop: ").strip() != "MERGE":
            return
        output = choose_folder("Choose a separate folder for finished episodes")
        convert = input("Use slower format conversion for every episode? Type CONVERT, or Enter for lossless joins: ").strip() == "CONVERT"
        merge_plan(plan, output, convert=convert, encoder="auto" if convert else "cpu")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(f"\nERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopped. Original clips are unchanged.", file=sys.stderr)
        sys.exit(130)
