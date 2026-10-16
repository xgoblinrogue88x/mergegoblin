import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import e01_mkvmerge as e01
import mergegoblin as app


MKVMERGE = shutil.which("mkvmerge")


@unittest.skipUnless(MKVMERGE and shutil.which("ffmpeg") and shutil.which("ffprobe"), "MKVToolNix/FFmpeg required")
class E01IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Daryl's E01 ")
        self.root = Path(self.temp.name)
        self.inputs = self.root / "input"
        self.inputs.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def plan(self, mixed=False):
        clips = []
        for i, size in enumerate(("160x120", "320x240" if mixed else "160x120")):
            name = ("First song", "Second song; reprise")[i]
            path = self.inputs / (name + ".mkv")
            app.run([shutil.which("ffmpeg"), "-v", "error", "-nostdin", "-n", "-f", "lavfi", "-i",
                     f"color=c={'red' if i == 0 else 'blue'}:s={size}:r=30:d=0.4", "-f", "lavfi", "-i",
                     "sine=frequency=440:sample_rate=48000:duration=0.4", "-c:v", "libx264", "-bf", "0", "-pix_fmt", "yuv420p",
                     "-c:a", "aac", "-shortest", str(path)])
            stat = path.stat()
            clips.append({"path": str(path), "title": name, "chapter": name, "size": stat.st_size, "mtime_ns": stat.st_mtime_ns})
        return {"episodes": [{"number": 1, "issues": [], "clips": clips}, {"number": 3, "issues": ["Do not process"], "clips": []}]}

    def packet_hashes(self, path, stream):
        info = json.loads(app.run([shutil.which("ffprobe"), "-v", "error", "-select_streams", stream,
                                 "-show_packets", "-show_data_hash", "sha256", "-show_entries", "packet=data_hash", "-of", "json", str(path)]))
        return [p["data_hash"] for p in info["packets"]]

    def test_actual_append_preserves_compressed_packets_and_chapters(self):
        plan = self.plan()
        original = {p.name: p.read_bytes() for p in self.inputs.iterdir()}
        self.assertTrue(e01.merge_e01(plan, self.root / "output", MKVMERGE))
        folder = self.root / "output" / "E01 MKVToolNix Test"
        result = app.read_json(folder / "result.json")
        self.assertTrue(result["accepted"])
        self.assertEqual(result["mkvmerge_exit_code"], 0)
        output = Path(result["output"])
        self.assertEqual([c["tags"]["title"] for c in app.probe(output)["chapters"]], ["First song", "Second song; reprise"])
        for stream in ("v:0", "a:0"):
            expected = sum((self.packet_hashes(c["path"], stream) for c in plan["episodes"][0]["clips"]), [])
            self.assertEqual(self.packet_hashes(output, stream), expected)
        self.assertEqual(original, {p.name: p.read_bytes() for p in self.inputs.iterdir()})
        with self.assertRaisesRegex(RuntimeError, "already exists"):
            e01.merge_e01(plan, self.root / "output", MKVMERGE)

    def test_mixed_resolution_is_held_if_mkvmerge_warns_or_rejects(self):
        plan = self.plan(mixed=True)
        try:
            accepted = e01.merge_e01(plan, self.root / "output", MKVMERGE)
        except RuntimeError as error:
            self.assertIn("mkvmerge rejected", str(error))
        else:
            self.assertFalse(accepted)
            folder = self.root / "output" / "E01 MKVToolNix Test"
            result = app.read_json(folder / "result.json")
            self.assertTrue(result["problems"])
            self.assertIn("NEEDS-REVIEW", result["output"])
            self.assertTrue(Path(result["output"]).is_file())

    def test_warnings_do_not_get_accepted_even_when_decoding_passes(self):
        plan = self.plan()
        execute = subprocess.run
        def warning(args, **kwargs):
            result = execute(args, **kwargs)
            if args[0] == MKVMERGE:
                result.returncode = 1
                result.stdout += "\nWarning: test warning\n"
            return result
        with patch.object(e01.subprocess, "run", side_effect=warning):
            self.assertFalse(e01.merge_e01(plan, self.root / "output", MKVMERGE))
        folder = self.root / "output" / "E01 MKVToolNix Test"
        self.assertIn("test warning", (folder / "mkvmerge.log").read_text())
        self.assertFalse((folder / "Live from Daryl's House - E01 - Daryl Hall.mkv").exists())

    def test_changed_input_is_rejected_before_merge(self):
        plan = self.plan()
        Path(plan["episodes"][0]["clips"][0]["path"]).write_bytes(b"changed")
        with self.assertRaisesRegex(RuntimeError, "changed since scanning"):
            e01.merge_e01(plan, self.root / "output", MKVMERGE)


if __name__ == "__main__":
    unittest.main()
