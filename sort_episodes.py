"""Move the known 290 videos into episode folders. No media processing."""
import argparse
import csv
import json
import os
from pathlib import Path
import sys
import unicodedata


def key(name):
    return unicodedata.normalize("NFC", name).casefold()


def read_manifest(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))
    seen = set()
    for row in rows:
        name, folder = row["filename"], row["folder"]
        if any(not s or s in (".", "..") or "/" in s or "\\" in s or any(ord(c) < 32 for c in s) for s in (name, folder)):
            raise RuntimeError("Invalid path component in sorting manifest.")
        if key(name) in seen:
            raise RuntimeError(f"Duplicate filename in sorting manifest: {name}")
        seen.add(key(name))
    if not rows:
        raise RuntimeError("Sorting manifest is empty.")
    return rows


def inspect(source, rows):
    source = Path(source).resolve()
    if not source.is_dir():
        raise RuntimeError("Select the folder containing the original videos.")
    found = {}
    for path in source.iterdir():
        if path.is_file():
            if key(path.name) in found:
                raise RuntimeError(f"Case-insensitive filename collision: {path.name}")
            found[key(path.name)] = path
    jobs = []
    for row in rows:
        src = found.get(key(row["filename"]), source / row["filename"])
        folder = source / row["folder"]
        if folder.is_symlink() or (folder.exists() and not folder.is_dir()):
            raise RuntimeError(f"Destination folder is a symlink or an existing file: {folder}")
        dst = folder / src.name
        status = "MOVE"
        if src.is_symlink() or dst.is_symlink():
            status = "CONFLICT — SYMLINK"
        elif src.exists() and dst.exists():
            status = "CONFLICT — BOTH LOCATIONS EXIST"
        elif not src.exists() and dst.is_file():
            status = "ALREADY SORTED"
        elif not src.is_file():
            status = "MISSING"
        stat = src.stat() if status == "MOVE" else None
        jobs.append({**row, "source": str(src), "destination": str(dst), "status": status,
                     "size": stat.st_size if stat else None, "mtime_ns": stat.st_mtime_ns if stat else None})
    known = {key(r["filename"]) for r in rows}
    untouched = [str(p) for k, p in found.items() if k not in known]
    return source, jobs, untouched


def report_folder(source):
    base = source / "_Sorting Reports"
    if base.is_symlink() or (base.exists() and not base.is_dir()):
        raise RuntimeError("The sorting report location is a symlink or file; no videos were moved.")
    base.mkdir(exist_ok=True)
    number = 1
    while True:
        path = base / f"Run {number:03}"
        try:
            path.mkdir()
            return path
        except FileExistsError:
            number += 1


def move_without_overwrite(src, dst):
    if os.name == "nt":
        # Windows rename refuses an existing target and stays on the same volume.
        os.rename(src, dst)
    else:
        # POSIX rename can replace a target; link/unlink avoids that behavior.
        os.link(src, dst)
        src.unlink()


def sort_files(source, rows, preview=False):
    source, jobs, untouched = inspect(source, rows)
    reports = report_folder(source)
    with (reports / "sorting-plan.csv").open("x", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(jobs[0]))
        writer.writeheader()
        writer.writerows(jobs)
    count = lambda status: sum(j["status"] == status for j in jobs)
    print(f"Known files: {len(jobs)}; to move: {count('MOVE')}; already sorted: {count('ALREADY SORTED')}; missing: {count('MISSING')}", flush=True)
    print(f"Sorting plan: {reports / 'sorting-plan.csv'}", flush=True)
    blocked = [j for j in jobs if j["status"] not in ("MOVE", "ALREADY SORTED")]
    if blocked:
        for job in blocked[:10]:
            print(f"  {job['status']}: {job['filename']}", flush=True)
        raise RuntimeError(f"{len(blocked)} file(s) are missing or conflict. No videos were moved. Check the selected folder and sorting-plan.csv.")
    if preview:
        print("Preview only. No videos were moved.", flush=True)
        return {"moved": 0, "already_sorted": count("ALREADY SORTED"), "preview": True, "report": str(reports)}
    moved = 0
    with (reports / "move-log.jsonl").open("x", encoding="utf-8") as log:
        for job in jobs:
            if job["status"] != "MOVE":
                continue
            src, dst = Path(job["source"]), Path(job["destination"])
            stat = src.stat()
            if stat.st_size != job["size"] or stat.st_mtime_ns != job["mtime_ns"]:
                raise RuntimeError(f"A source file changed while sorting: {src.name}. Stopped; rerun to resume after checking it.")
            if dst.parent.is_symlink():
                raise RuntimeError("Destination folder became a symlink. Stopped without moving this file.")
            dst.parent.mkdir(exist_ok=True)
            log.write(json.dumps({"action": "moving", **job}, ensure_ascii=False) + "\n")
            log.flush()
            move_without_overwrite(src, dst)
            log.write(json.dumps({"action": "moved", "source": str(src), "destination": str(dst)}, ensure_ascii=False) + "\n")
            log.flush()
            moved += 1
            print(f"[{moved}/{count('MOVE')}] {job['folder']} / {src.name}", flush=True)
    result = {"moved": moved, "already_sorted": count("ALREADY SORTED"), "total_accounted_for": len(jobs),
              "episode_folders": len({j["folder"] for j in jobs}), "unrecognized_files_left_untouched": untouched,
              "report": str(reports)}
    with (reports / "result.json").open("x", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    print(f"\nDone: moved {moved}; already sorted {result['already_sorted']}; accounted for {len(jobs)} files.", flush=True)
    print(f"Episode folders are inside: {source}", flush=True)
    return result


def choose_source():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    try:
        folder = filedialog.askdirectory(title="Select the folder containing the 290 original videos")
    finally:
        root.destroy()
    if not folder:
        raise RuntimeError("Folder selection cancelled; nothing was moved.")
    return folder


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", help="Folder containing the videos; a folder picker opens if omitted")
    parser.add_argument("--manifest", default=str(Path(__file__).with_name("episode_sort_manifest.csv")))
    parser.add_argument("--preview", action="store_true", help="Write the sorting plan without moving files")
    args = parser.parse_args()
    sort_files(args.source or choose_source(), read_manifest(args.manifest), args.preview)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Stopped. Files already sorted remain in their episode folders. Rerun to resume.", file=sys.stderr)
        sys.exit(130)
