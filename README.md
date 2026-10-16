# MergeGoblin: Live from Daryl's House

A small Python tool for Windows: match already-downloaded clips to the channel's episode playlists, review the sequence, and batch-merge complete matches into MKV files with chapters. It does not download video, remove originals, or overwrite existing outputs.

Output format:

```text
Live from Daryl's House - E07 - Featured Artist.mkv
```

The episode number and featured artist/special name come from the playlist title, including the channel's `#10 - Daryl Hall hosts Chromeo…` format, never an artist-name guess from a local clip. E32 is named `Retrospective 2`, and E39 is named `New Years Eve Special`. Numbers 1–91 are in scope. Range collections such as `Episodes 1 - 10` are excluded. Windows-invalid characters in artist names are replaced with ` - `.

## What has actually been checked

The supplied filename list contains **201 files and 25 guest groups**, after normalizing two spelling variations. Names are suitable for automatic matching, but do not encode episode order or number. Guster has one file, Todd Rundgren two, and Jose Feliciano three; these counts are reasons to check completeness, not proof of missing clips.

**Playlist discovery has now been checked against the user's actual channel export:** its titles/IDs identify 88 individual episode playlists, with E02, E13, and E29 absent from that listing. The parser regression test uses that export, including both Todd Rundgren appearances (E23 and E40), range collections, and unrelated playlists. Actual clip lists and their order still need to be fetched and checked on your PC: this development environment's network proxy returns HTTP 403 for YouTube. Do not treat a missing playlist as proof the episode never existed.

The merger has been exercised with real FFmpeg-generated video clips on Linux, including chapter names/times, incompatible formats, conversion, corrupt inputs, preservation of originals, and repeat runs. The Windows launcher and file-picker workflow still require a Windows run. Actual downloaded videos were not supplied, so their media properties have not been checked.

The supplied catalog and local-filename inventory were also replayed against the corrected scanner. That predicts **27 fully matched episodes**, up from 21. This is filename/metadata validation, not validation of the actual videos. E07 contains a repeated entry for the same YouTube ID; the second occurrence is omitted. Six performances shared with E32 have identical IDs in their original episodes. Eli Reed's `Pick A Number` has different IDs in E27 and E32 despite an identical title, so neither version is assigned by title alone.

When updating the downloaded tool, copy the existing **work** folder into the new extracted app folder before running Start.bat. This reuses your catalog and explicit matches while regenerating the plan; there is no need to fetch all playlist metadata again. Keep your downloaded videos in their existing folder.

## Windows setup

1. Install **Python 3.12 or newer** from <https://www.python.org/downloads/windows/>. Enable **Add python.exe to PATH** and include Tcl/Tk. The `py` launcher is optional: Start.bat also checks `python`, `python3`, and standard Python installation folders. Alternatively run `winget install --id Python.Python.3.12 --exact` in PowerShell.
2. Install **FFmpeg**, including `ffprobe`. One option in PowerShell is:

   ```powershell
   winget install --id Gyan.FFmpeg --exact
   ```

   Reopen your terminal afterward. Alternatively follow the Windows download links at <https://ffmpeg.org/download.html>, and put `ffmpeg.exe` and `ffprobe.exe` in a `tools` folder beside `mergegoblin.py`. Both executables are required. The app does not download executable binaries itself.

3. Extract this tool into its own folder, separate from your video collection. Double-click **Start.bat**. Local folders and UNC network shares are supported by the launcher. It uses `pushd` to temporarily map network paths and keeps its Python environment locally at `%LOCALAPPDATA%\MergeGoblin\venv`. An initial CMD warning about UNC paths can still appear before the script starts; the script then switches to the mapped folder. Moving the app to a local folder is also fine; your videos can stay on the NAS.
4. Choose the folder containing your 201 clips. The first scan reads public playlist metadata from <https://www.youtube.com/@realdarylhall/playlists>. No YouTube account or Tartube database is required for public metadata.
5. Read **work/plan.txt**, which opens automatically. Check the episode number, featured artist, and chapter sequence against its playlist link. Playlist order is the proposed sequence; the uploader can reorder it, and it is not independent proof of original broadcast order.
6. Type **MERGE** to process the fully matched episodes, or press Enter to stop after the scan. Choose a separate output folder. Press Enter for fast, lossless joining; type **CONVERT** only if you want all selected clips normalized to H.264/AAC.

Conversion is slower and lossy. It uses the first clip's dimensions, letterboxes other aspect ratios, and outputs 30 fps, H.264 CRF 18, stereo AAC 48 kHz. Originals remain available. Fast mode holds episodes with differing stream formats instead of risking broken joins.

## Review rules

- Embedded video IDs or explicit matches are preferred. Otherwise full titles are tried before titles normalized to remove the show suffix. This distinguishes the two differently titled `I Miss You` intro uploads. Punctuation/case/accent variations are ignored. Separate song intros remain separate chapters.
- A title mapping to different YouTube video IDs requires an explicit identity match; a single similarly named local file cannot silently stand in for both. Similar titles are suggestions only. Missing clips, unresolved duplicate candidates, duplicate episode numbers, or conflicting video identities hold an episode back.
- A video can legitimately appear in its original episode and a retrospective when its YouTube ID agrees. It is a separate chapter in each output. Duplicate occurrences of the same video ID within one playlist are omitted after the first, with a report note. Clip order otherwise remains the playlist order.
- Mixed guest names are expected in retrospectives and specials; the output name comes from the playlist rather than the first clip. Parenthetical band names on individual clip titles do not hold an otherwise matched episode back.
- **Complete means matched to every visible playlist entry.** YouTube can hide unavailable entries, and a playlist can omit episode material. The app cannot certify a full original broadcast from playlist data alone.
- Episodes without visible explicitly numbered playlists are listed as undiscovered. All other playlist titles/IDs are saved under `ignored_playlists` in `work/catalog.json` for diagnosis. The complete discovered listing is also saved to `work/channel-playlists.json` before fetching clips, including when no episode titles are recognized. An unexpected title format should be inspected, not assigned a guessed number.
- A filename match cannot prove two files contain different footage or that a segment does not overlap another. Review questionable clips; the app does not trim, deduplicate by video content, or invent missing material.

### Resolve a title mismatch

Keep your source filenames unchanged. Create `work/matches.json` mapping the video ID shown in `work/plan.json` to the exact filename in your downloads folder:

```json
{
  "abcdefghijk": "Daryl Hall & Guest - Local spelling (Live From Daryl's House).mkv"
}
```

Run Start.bat again. It applies these explicit choices and regenerates the report. The app does not accept a path outside the selected folder. Only make an override after checking the clip's identity.

An explicit match reserves that file for its selected video ID. A different ID with an identical title will remain unmatched. For the two `Pick A Number` uploads, compare <https://www.youtube.com/watch?v=Vl6gZwnM4hw> (E27) and <https://www.youtube.com/watch?v=8Rry_PXRPPY> (E32) with your local file before choosing. Different IDs do not prove different footage, but identical titles do not prove identical footage either. To represent both IDs, use separately identified local files; the tool does not assign one file to conflicting IDs. Missing-clip rows in the report include their expected YouTube links.

For a deliberately incomplete episode or corrected order, the catalog is editable JSON: make a separate copy, document the correction, and scan that copy using `--catalog`. Removing unavailable entries makes the resulting output partial; do not mistake this for recovered material. The default behavior holds incomplete episodes.

## Command-line use

Use the local virtual environment created by Start.bat, or install `requirements.txt` into your own Python environment. Commands below are run in PowerShell from this tool's folder:

```powershell
$mgPython = "$env:LOCALAPPDATA\MergeGoblin\venv\Scripts\python.exe"
& $mgPython mergegoblin.py catalog
& $mgPython mergegoblin.py scan --input "D:\Daryl clips"
& $mgPython mergegoblin.py scan --input "D:\Daryl clips" --refresh
& $mgPython mergegoblin.py scan --input "D:\Daryl clips" --matches work/matches.json
& $mgPython mergegoblin.py merge --output "D:\Finished episodes" --reviewed
& $mgPython mergegoblin.py merge --output "D:\Finished episodes" --episodes 7 12 --convert --reviewed
```

`--reviewed` confirms you checked episode identity and order. It does not bypass held matches. Cached metadata is reused unless `--refresh` is specified. If YouTube extraction fails, no new catalog or merge plan is accepted; update yt-dlp (`python -m pip install --upgrade yt-dlp`) and inspect the reported error. Public access can still fail because of regional restrictions, authentication challenges, removals, or YouTube changes. No first-run guarantee is possible before that live scan.

## Output validation and resuming

Each output is checked for total duration and chapter titles/count, then fully decoded with FFmpeg before publication. This detects corrupt media/joins but does not establish perceptual A/V synchronization or correct editorial sequence. Fast mode preserves compressed video/audio; full decoding for verification still takes time.

Successful outputs have `.receipt.json` sidecars recording input paths, sizes, timestamps, titles, and conversion mode. Repeating the same job skips completed outputs with matching receipts and unchanged output size/timestamp. Files with changed metadata require a rescan. This is metadata-based resume validation, not a cryptographic content check. Existing files without a matching receipt are held; they are never overwritten. Interrupted staging files are normally cleaned up; an abrupt process termination can leave a `mergegoblin-*` temporary directory in the output folder, which can be removed when the tool is not running.

Reserve substantial free space. Fast mode checks for approximately 3.2 times the episode's source size to allow staging/copy fallbacks. Conversion checks 8 times as a heuristic; conversion size varies and that is not an upper bound. The process handles one episode at a time and keeps already-completed episodes if a later episode fails.

## Development checks

```text
python -m unittest discover -s tests -v
```

Tests use the standard library; real-media integration checks require FFmpeg and ffprobe. No YouTube video downloads are performed.
