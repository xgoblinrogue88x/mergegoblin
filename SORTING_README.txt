SORT THE 290 VIDEOS INTO EPISODE FOLDERS

1. Extract this ZIP into its own folder. Keep its three program/data files together.
2. Double-click Sort-Into-Episode-Folders.bat.
3. Select the folder currently containing all 290 videos.

The videos are MOVED into episode subfolders inside the folder you select.
Their filenames and contents are unchanged. There is no media processing.
The sorter uses the included episode_sort_manifest.csv, not any old work/plan.json.
You can open that CSV in Excel to see every assignment and its basis.

Assignments: 276 files in 35 numbered episode folders, plus 14 files grouped
under "Jamaica Special (episode unverified)": 290 files in 36 folders total.
The supplied numbered playlists do not establish the Jamaica special's number,
so the sorter does not invent one.

Shared retrospective performances are assigned once to the original episode.
Segments found only in the retrospective playlist stay in the retrospective folder.
Supplemental Eli Reed segments go to E27; the two Todd Rundgren title variants
go to E23. These guest/title-based decisions are labelled in the CSV.
Incomplete episodes get folders too. No completeness or media-format checks run.

The sorter checks that every one of the 290 known filenames is either in the
source folder or already in its expected destination. Missing files, symlinks,
and conflicting destinations stop the run before any videos move. Additional
unrecognized files are left where they are. Existing files are never overwritten.

A sorting plan and move log are saved under _Sorting Reports in the source
folder. If interrupted, files already moved stay in their folders; rerun the
same launcher and select the same source folder to continue. Review any error
first. To undo manually, use the log's source/destination paths; never overwrite
files that may have been created or edited afterward.

Optional preview only: open PowerShell in this extracted folder and run:
& "$env:LOCALAPPDATA\MergeGoblin\venv\Scripts\python.exe" .\sort_episodes.py --preview

The launcher reuses your existing Python installation. It also works with
python/py/python3 on PATH when Tcl/Tk is installed. No other tools are needed.

Six tests cover the full 290-file move, original bytes/names, repeat runs,
interruption/resume, preview, missing files and refusal to overwrite conflicts.
The Windows launcher still needs to run on your PC.
