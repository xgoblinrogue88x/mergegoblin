UNDO THE EPISODE SORT

Extract this ZIP and double-click Undo-Sort.bat.
Select your ORIGINAL video folder: the folder that now contains the episode
subfolders and _Sorting Reports. Do not select an individual episode folder.

The program reads the original sorter's move logs and moves the logged videos
back to their original locations. No files are overwritten. All locations and
file sizes/timestamps are checked first; conflicts or changed/missing files stop
the undo before any files move. Files already restored are recognized, so you
can rerun after an interruption. Empty folders and sorting reports are retained.

Do not delete _Sorting Reports before undoing. If you have not run the sorter,
your videos have not moved and there is nothing to undo.

Python with Tcl/Tk is required; your existing MergeGoblin Python is reused.
The program does not undo any earlier merges, conversions, or other file actions.
