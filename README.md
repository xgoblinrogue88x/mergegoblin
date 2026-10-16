# MergeGoblin: Live from Daryl's House

A small Python tool for Windows: match already-downloaded clips to the channel's episode playlists, review the sequence, and batch-merge complete matches into MKV files with chapters. It does not download video, remove originals, or overwrite existing outputs.

Output format:

```text
Live from Daryl's House - E07 - Featured Artist.mkv
```

The episode number and featured artist/special name come from the playlist title, including the channel's `#10 - Daryl Hall hosts Chromeo…` format, never an artist-name guess from a local clip. E32 is named `Retrospective 2`, and E39 is named `New Years Eve Special`. Numbers 1–91 are in scope. Range collections such as `Episodes 1 - 10` are excluded. Windows-invalid characters in artist names are replaced with ` - `.

## Batch MKVToolNix: original quality and resolution

**Batch-MKVToolNix.bat** processes the complete, unambiguous episodes in your existing `work/plan.json`. It never re-encodes, resizes, changes frame rate, or converts audio. Your source files remain at their existing paths. Each accepted episode is written as one MKV with song chapters and the planned episode number/name.

1. Stop any old conversion job. Download and extract the updated ZIP into a new app folder.
2. Copy the existing **work** folder into that new app folder. This preserves your catalog, paths, matching choices, and verified playlist ordering. Do not move the source clips.
3. Install MKVToolNix if needed: `winget install --id MoritzBunkus.MKVToolNix --exact`. Your existing Python environment and FFmpeg/ffprobe setup are reused. If you kept ffprobe.exe in the old app's tools folder, copy that folder too.
4. Double-click **Batch-MKVToolNix.bat**. You do not need to open a Python file or enter a merge command.

Completed files go to **Videos/LFDH Original Quality**. Read **batch-summary.txt** there for the outcome of every episode. `_reports/E##/formats.txt` identifies each source's video/audio codec, track IDs, and dimensions. Diagnostic logs/options/chapters are kept in the same report folder. A previous completed output is skipped only when its receipt and file metadata still match; existing outputs are never overwritten.

The batch explicitly maps video-to-video and audio-to-audio, including clips with different track ordering. This addresses one possible cause of the E01 test failure. However, it cannot guarantee that E01 or all other episodes will append: actual codec incompatibility is not fixed by changing track mapping. Different video codecs, pixel/display dimensions, audio codecs, sample rates, or channel counts are held by the conservative preflight rather than changed. MKVToolNix can impose additional compatibility limits. Every episode held for these reasons remains available as its original separate clips. Different-resolution sources are not silently scaled to the first clip.

Incomplete/ambiguous episodes are skipped; the tool never drops missing clips to manufacture a supposedly complete episode. MKVToolNix warnings or failed output checks retain a **candidate.NEEDS-REVIEW.mkv** in the episode report folder, not an accepted final output. Other episodes continue processing. E02, E13 and E29 are absent from the supplied catalog and are listed as absent; no file is invented for them.

Before acceptance, the program checks duration and chapters, then hashes the compressed video and audio packets of the sources and output in order. The hashes and packet counts must match. This checks original-stream preservation without decoding or encoding. It requires extra disk reads, but avoids software video encoding. Rare lossless bitstream rewrites can fail the strict packet identity test too; those candidates are held for review. Packet preservation does not prove original media were uncorrupted or that editorial ordering/audio sync is correct. Check playback and transitions on a representative finished episode.

Full decoding validation is optional and never changes the media. To select just the first batch and also decode-check the results, use PowerShell in the app folder:

```powershell
& "$env:LOCALAPPDATA\MergeGoblin\venv\Scripts\python.exe" .\mkv_batch.py --episodes 1 3 4 5 6 7 8 9 10 --decode-check
```

Omit `--decode-check` for faster packet-verification-only operation. Omit `--episodes` to attempt all matched episodes. Optional `--output "D:\Original quality episodes"` selects a different output folder. Optional `--mkvmerge "C:\Custom tools\MKVToolNix\mkvmerge.exe"` selects a nonstandard MKVToolNix installation. No encoding preset or conversion option exists in this batch program.

The batch integration tests exercise actual MKVToolNix appending, three clips with alternating audio/video track order, packet identity, resolution preservation, resume behavior, mixed-codec/resolution holds, warnings, continuation after failures, source preservation, and episode selection. Actual Windows source files remain to be tested on the user's PC.

## Episode 1: MKVToolNix test without re-encoding

This is deliberately limited to E01. Keep the existing `work/plan.json`; do not rescan or download videos again. Install MKVToolNix from <https://mkvtoolnix.download/downloads.html#windows> if needed, or use:

```powershell
winget install --id MoritzBunkus.MKVToolNix --exact
```

Copy **e01_mkvmerge.py** and **Test-E01-MKVToolNix.bat** from the new ZIP into your existing app folder alongside mergegoblin.py and work. Stop any old conversion job before starting the test. Double-click **Test-E01-MKVToolNix.bat**. It looks for MKVToolNix in its standard installation folder, on PATH, or in this app's tools folder. Python, FFmpeg, and ffprobe are reused from the existing setup.

The test reads only E01's ordered source files and appends their tracks with mkvmerge. It does not make source copies, move your videos, or re-encode audio/video. It creates an episode folder under **Videos/LFDH MKVToolNix/E01 MKVToolNix Test** with the finished MKV, song chapters, an ordered source list, the exact mkvmerge options, a log, and result.json. Different codec configurations are left for MKVToolNix to assess instead of the app's conservative FFmpeg fast-join signature check.

An MKVToolNix warning or failed duration/chapter/decode check keeps the candidate as **NEEDS-REVIEW.mkv**, not an accepted finished file. Fatal append errors leave the log and no finished output. No existing output is overwritten. Check the result's transitions and audio sync manually even if automatic checks pass; successful decoding cannot establish perceptual correctness. These warnings and decoding checks matter when codec configuration changes between clips. Full decoding validation adds time even though appending does not re-encode.

From PowerShell in the app folder, the equivalent command is:

```powershell
& "$env:LOCALAPPDATA\MergeGoblin\venv\Scripts\python.exe" .\e01_mkvmerge.py --plan .\work\plan.json
```

Optional `--output "D:\Test output"` selects the parent folder. Optional `--mkvmerge "C:\Custom tools\MKVToolNix\mkvmerge.exe"` selects a custom executable. To repeat a test without replacing the prior output, select a new output parent and use the wrapper again. The saved options are available for inspection and target a separate manual-rerun.mkv; the wrapper provides the no-overwrite checks.

The compatible-file integration test checks that output compressed video and audio packet hashes equal the original packets in order, plus chapter and playback decoding checks. Additional tests cover mixed resolution, warning handling, preservation of originals, changed inputs, and refusal to overwrite outputs. Actual E01 media and the Windows launcher still need to be tested on your PC.

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

Conversion is slower and lossy. It uses the first clip's dimensions, letterboxes other aspect ratios, and outputs 30 fps H.264 with stereo AAC 48 kHz. CPU mode uses CRF 18 with the `veryfast` preset by default (older versions used `medium`). Originals remain available. Fast mode holds episodes with differing stream formats instead of risking broken joins.

### Faster conversion on the Beelink GTR5

Use `--convert --encoder auto --preset veryfast` to try the AMD hardware video encoder, falling back to faster CPU encoding if the initial hardware test fails. The conversion wizard also tries this automatically. The test actually initializes FFmpeg's `h264_amf` encoder; merely having an AMD GPU or an encoder in FFmpeg's list does not prove driver support. Hardware encoding requires an FFmpeg build with AMF plus working AMD graphics drivers. The Windows/GTR5 hardware path cannot be exercised in this Linux development environment; fallback and failure handling are tested, and real CPU conversion is tested.

AMD mode uses H.264 AMF's speed setting and constant QP 20, without B frames. Its quality and file size are not equivalent to x264 CRF 18. Both modes re-encode; faster encoding can require larger files for comparable visual quality. Scaling and other filters still run on the CPU, and full decoding validation still runs after joining.

For even faster CPU conversion, use `--encoder cpu --preset ultrafast` at the cost of larger files. Use `--preset medium` for the old CPU preset. If AMD passes its startup test but fails on an actual clip, the episode is held; rerun with `--encoder cpu`. There is no runtime guarantee before measuring your files on your PC. Completed episodes with matching receipts are reused regardless of the new encoding setting; unfinished episodes restart. Stop the old job with Ctrl+C and wait for the PowerShell prompt before starting a new one. Per-clip progress and join/validation stages are now printed.

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
& $mgPython mergegoblin.py merge --output "D:\Finished episodes" --episodes 1 3 4 5 6 7 8 9 10 --convert --encoder auto --preset veryfast --reviewed
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
