"""Undo logged episode sorting without overwriting or guessing file locations."""
import argparse
import csv
import json
import os
from pathlib import Path
import sys


def original_moves(root):
    root = Path(root).resolve()
    base = root / "_Sorting Reports"
    if base.is_symlink() or not base.is_dir():
        raise RuntimeError("The selected folder has no original _Sorting Reports directory. Nothing was moved.")
    moves = {}
    for run in sorted(base.glob("Run *")):
        if run.is_symlink() or not run.is_dir():
            raise RuntimeError("An original sorting report directory is not a regular directory.")
        path = run / "move-log.jsonl"
        if not path.exists():
            continue
        if path.is_symlink():
            raise RuntimeError("An original move log is a symlink. Nothing was moved.")
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if not line.strip():
                continue
            event = json.loads(line)
            if event.get("action") != "moving":
                continue
            raw_src, raw_dst = Path(event["source"]), Path(event["destination"])
            if not raw_src.is_absolute() or not raw_dst.is_absolute():
                raise RuntimeError("The move log contains a relative path. Nothing was moved.")
            if raw_src.is_symlink() or raw_dst.is_symlink() or raw_dst.parent.is_symlink():
                raise RuntimeError("A logged video location is now a symlink. Nothing was moved.")
            src, dst = raw_src.resolve(), raw_dst.resolve()
            if src.parent != root or dst.parent.parent != root or src.name != dst.name:
                raise RuntimeError("A logged move points outside the selected original folder. Select the original folder; nothing was moved.")
            if dst.parent.name == "_Sorting Reports":
                raise RuntimeError("Invalid media destination in the move log.")
            record = {"original": str(src), "sorted": str(dst), "size": int(event["size"]), "mtime_ns": int(event["mtime_ns"])}
            previous = moves.get(str(src))
            if previous and previous["sorted"] != str(dst):
                raise RuntimeError("The move logs disagree on a file's destination. Nothing was moved.")
            moves[str(src)] = record
    if not moves:
        raise RuntimeError("No logged video moves were found. There is nothing to undo from this sorter.")
    return root, list(moves.values())


def inspect(root):
    root, moves = original_moves(root)
    errors = []
    for move in moves:
        original, sorted_path = Path(move["original"]), Path(move["sorted"])
        if original.exists() and sorted_path.exists():
            errors.append(f"Both locations contain a file: {original.name}")
            continue
        if not original.exists() and not sorted_path.exists():
            errors.append(f"File is missing from both locations: {original.name}")
            continue
        current = original if original.exists() else sorted_path
        if not current.is_file():
            errors.append(f"Not a regular video file: {current}")
            continue
        stat = current.stat()
        if stat.st_size != move["size"] or stat.st_mtime_ns != move["mtime_ns"]:
            errors.append(f"File was changed since the sort: {current}")
            continue
        move["status"] = "ALREADY RESTORED" if current == original else "RESTORE"
    if errors:
        raise RuntimeError("Undo stopped before moving any files:\n" + "\n".join(errors[:15]))
    return root, moves


def move_without_overwrite(source, destination):
    if os.name == "nt":
        os.rename(source, destination)
    else:
        os.link(source, destination)
        source.unlink()


def undo(root, preview=False):
    root, moves = inspect(root)
    already = sum(m["status"] == "ALREADY RESTORED" for m in moves)
    pending = [m for m in moves if m["status"] == "RESTORE"]
    print(f"Videos to restore: {len(pending)}; already restored: {already}.", flush=True)
    if not pending:
        print("The logged videos are already back in their original locations.", flush=True)
        return {"restored": 0, "already_restored": already}
    base = root / "_Sorting Reports"
    number = 1
    while True:
        report = base / f"Undo {number:03}"
        try:
            report.mkdir()
            break
        except FileExistsError:
            number += 1
    with (report / "undo-plan.csv").open("x", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(moves[0]))
        writer.writeheader()
        writer.writerows(moves)
    if preview:
        print(f"Preview only. Nothing moved. Plan: {report / 'undo-plan.csv'}", flush=True)
        return {"restored": 0, "already_restored": already, "preview": True}
    restored = 0
    with (report / "undo-log.jsonl").open("x", encoding="utf-8") as log:
        for move in pending:
            original, current = Path(move["original"]), Path(move["sorted"])
            if original.exists() or original.is_symlink() or current.is_symlink() or current.parent.is_symlink():
                raise RuntimeError(f"File locations changed during undo: {original.name}. Stopped without overwriting.")
            stat = current.stat()
            if stat.st_size != move["size"] or stat.st_mtime_ns != move["mtime_ns"]:
                raise RuntimeError(f"File changed during undo: {current.name}. Stopped without moving it.")
            move_without_overwrite(current, original)
            log.write(json.dumps({"restored": str(original), "from": str(current)}, ensure_ascii=False) + "\n")
            log.flush()
            restored += 1
    print(f"Restored {restored} videos to {root}. Empty episode folders and reports were left in place.", flush=True)
    return {"restored": restored, "already_restored": already}


def choose_folder():
    import tkinter as tk
    from tkinter import filedialog
    window = tk.Tk()
    window.withdraw()
    try:
        path = filedialog.askdirectory(title="Select the ORIGINAL video folder containing _Sorting Reports and the episode folders")
    finally:
        window.destroy()
    if not path:
        raise RuntimeError("Selection cancelled. Nothing was moved.")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", help="Original folder containing _Sorting Reports and the episode folders")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()
    undo(args.source or choose_folder(), args.preview)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Stopped. Rerun Undo-Sort.bat to finish restoring the remaining videos.", file=sys.stderr)
        sys.exit(130)
