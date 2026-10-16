import copy
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import mergegoblin as app
import mkv_batch as batch


MKVMERGE = shutil.which("mkvmerge")


@unittest.skipUnless(MKVMERGE and shutil.which("ffmpeg") and shutil.which("ffprobe"), "MKVToolNix/FFmpeg required")
class BatchIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Daryl's batch ")
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def episode(self, number=1, reorder=False, mixed_codec=False, mixed_size=False):
        source = self.root / f"input{number}"
        source.mkdir()
        clips = []
        for i in range(3):
            path = source / f"Song {i + 1}.mkv"
            size = "320x240" if mixed_size and i == 1 else "160x120"
            codec = "mpeg4" if mixed_codec and i == 1 else "libx264"
            maps = ["-map", "1:a:0", "-map", "0:v:0"] if reorder and i == 1 else ["-map", "0:v:0", "-map", "1:a:0"]
            app.run([shutil.which("ffmpeg"), "-v", "error", "-nostdin", "-n", "-f", "lavfi", "-i",
                     f"color=c={'red' if i == 0 else 'blue'}:s={size}:r=30:d=0.4", "-f", "lavfi", "-i",
                     "sine=frequency=440:sample_rate=48000:duration=0.4", *maps, "-c:v", codec, "-bf", "0", "-pix_fmt", "yuv420p",
                     "-c:a", "aac", "-shortest", str(path)])
            stat = path.stat()
            clips.append({"path": str(path), "title": path.stem, "chapter": path.stem, "id": f"video{i:06}",
                          "size": stat.st_size, "mtime_ns": stat.st_mtime_ns})
        return {"number": number, "issues": [], "clips": clips, "output": f"Live from Daryl's House - E{number:02} - Guest.mkv"}

    def test_reordered_tracks_append_with_original_packets_and_resume(self):
        episode = self.episode(reorder=True)
        before = {Path(c["path"]): Path(c["path"]).read_bytes() for c in episode["clips"]}
        output = self.root / "output"
        result = batch.batch({"episodes": [episode]}, output, mkvmerge=MKVMERGE)[0]
        self.assertEqual(result["status"], "COMPLETED", result)
        receipt = app.read_json(output / "_reports" / "E01" / "receipt.json")
        self.assertTrue(receipt["packets_verified"])
        self.assertFalse(receipt["decode_checked"])
        info = app.probe(result["output"])
        self.assertEqual([s["codec_type"] for s in info["streams"]], ["video", "audio"])
        self.assertEqual([(s["width"], s["height"]) for s in info["streams"] if s["codec_type"] == "video"], [(160, 120)])
        self.assertEqual(len(info["chapters"]), 3)
        saved = Path(result["output"]).read_bytes()
        repeated = batch.batch({"episodes": [episode]}, output, mkvmerge=MKVMERGE, decode_check=True)[0]
        self.assertEqual(repeated["status"], "ALREADY COMPLETED")
        self.assertEqual(Path(result["output"]).read_bytes(), saved)
        self.assertTrue(app.read_json(output / "_reports" / "E01" / "receipt.json")["decode_checked"])
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_batch_continues_after_codec_mismatch_and_missing_clips(self):
        incompatible = self.episode(mixed_codec=True)
        complete = self.episode(number=5)
        incomplete = {"number": 3, "issues": ["Missing clip: Song"], "clips": []}
        results = batch.batch({"episodes": [incompatible, incomplete, complete]}, self.root / "output", mkvmerge=MKVMERGE)
        self.assertEqual([r["status"] for r in results], ["HELD", "SKIPPED — MATCHING", "COMPLETED"])
        self.assertIn("video codec_id", results[0]["reasons"][0])
        self.assertTrue((self.root / "output" / "_reports" / "E01" / "formats.txt").exists())
        self.assertFalse((self.root / "output" / incompatible["output"]).exists())
        self.assertEqual(len(app.read_json(self.root / "output" / "batch-summary.json")), 3)

    def test_different_resolutions_are_held_without_resizing(self):
        episode = self.episode(mixed_size=True)
        result = batch.batch({"episodes": [episode]}, self.root / "output", mkvmerge=MKVMERGE)[0]
        self.assertEqual(result["status"], "HELD")
        self.assertIn("resolution", result["reasons"][0])
        self.assertFalse((self.root / "output" / episode["output"]).exists())

    def test_warning_output_is_not_accepted_and_is_not_overwritten(self):
        episode = self.episode()
        execute = subprocess.run
        def warning(args, **kwargs):
            result = execute(args, **kwargs)
            if args[0] == MKVMERGE and args[1].startswith("@"):
                result.returncode = 1
                result.stdout += "\nWarning: test warning\n"
            return result
        with patch.object(batch.subprocess, "run", side_effect=warning):
            result = batch.batch({"episodes": [episode]}, self.root / "output", mkvmerge=MKVMERGE)[0]
        self.assertEqual(result["status"], "NEEDS REVIEW")
        self.assertTrue(Path(result["candidate"]).exists())
        self.assertFalse((self.root / "output" / episode["output"]).exists())
        again = batch.batch({"episodes": [episode]}, self.root / "output", mkvmerge=MKVMERGE)[0]
        self.assertEqual(again["status"], "HELD")

    def test_cli_selects_only_requested_episode(self):
        episode = self.episode()
        plan = self.root / "plan.json"
        app.write_json(plan, {"episodes": [episode, {"number": 3, "issues": ["missing"], "clips": []}]})
        app.run([sys.executable, str(Path(batch.__file__).resolve()), "--plan", str(plan), "--output", str(self.root / "output"),
                 "--episodes", "1", "--mkvmerge", MKVMERGE])
        results = app.read_json(self.root / "output" / "batch-summary.json")
        self.assertEqual([r["episode"] for r in results], [1])
        self.assertEqual(results[0]["status"], "COMPLETED")


if __name__ == "__main__":
    unittest.main()
