from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

import episode_playlists as playlists


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Daryl's playlists ")
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.output = self.root / "output"

    def tearDown(self):
        self.temp.cleanup()

    def episode(self, number=1):
        clips = []
        for i, name in enumerate(("Z first # intro.mkv", "A second café.mkv")):
            path = self.source / f"E{number:02} {name}"
            path.write_bytes(f"original media {number} {i}".encode())
            stat = path.stat()
            clips.append({"path": str(path), "title": path.stem, "chapter": path.stem,
                          "size": stat.st_size, "mtime_ns": stat.st_mtime_ns})
        return {"number": number, "output": f"Live from Daryl's House - E{number:02} - Guest.mkv", "issues": [], "clips": clips}

    def test_playlist_order_unicode_and_source_bytes_preserved(self):
        episode = self.episode()
        before = {p: p.read_bytes() for p in self.source.iterdir()}
        result = playlists.make_episode(episode, self.output)
        folder = Path(result["folder"])
        lines = (folder / "Play Episode.m3u8").read_text(encoding="utf-8").splitlines()
        urls = [line for line in lines if not line.startswith("#")]
        decoded = [Path(unquote(urlsplit(url).path)) for url in urls]
        self.assertEqual(decoded, [Path(c["path"]) for c in episode["clips"]])
        self.assertIn("%23", urls[0])
        self.assertTrue(all(not urlsplit(url).fragment for url in urls))
        self.assertEqual(before, {p: p.read_bytes() for p in self.source.iterdir()})
        self.assertFalse(list(self.output.rglob("*.mkv")))
        self.assertTrue((folder / "Play Episode.bat").read_bytes().startswith(b"@echo off\r\n"))

    def test_default_selects_only_held_or_review_episodes(self):
        first, completed, third = self.episode(1), self.episode(3), self.episode(5)
        summary = [{"episode": 1, "status": "HELD"}, {"episode": 3, "status": "COMPLETED"},
                   {"episode": 5, "status": "NEEDS REVIEW"}]
        results = playlists.create({"episodes": [first, completed, third]}, self.output, summary)
        self.assertEqual([r["episode"] for r in results], [1, 5])
        self.assertEqual([r["status"] for r in results], ["CREATED", "CREATED"])
        self.assertFalse(any("E03" in p.name for p in self.output.iterdir()))

    def test_repeat_run_and_user_edits_are_preserved(self):
        episode = self.episode()
        result = playlists.make_episode(episode, self.output)
        self.assertEqual(playlists.make_episode(episode, self.output)["status"], "ALREADY CREATED")
        playlist = Path(result["folder"]) / "Play Episode.m3u8"
        playlist.write_text("User-edited playlist", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "edited or removed"):
            playlists.make_episode(episode, self.output)
        self.assertEqual(playlist.read_text(), "User-edited playlist")

    def test_incomplete_or_changed_sources_are_not_presented_as_complete(self):
        first, second = self.episode(1), self.episode(3)
        first["issues"] = ["Missing clip: Song"]
        Path(second["clips"][0]["path"]).write_bytes(b"changed")
        results = playlists.create({"episodes": [first, second]}, self.output, all_matched=True)
        self.assertTrue(all(r["status"] == "HELD" for r in results))
        self.assertFalse(list(self.output.rglob("*.m3u8")))

    def test_existing_unknown_output_is_not_overwritten(self):
        episode = self.episode()
        folder = self.output / Path(episode["output"]).stem
        folder.mkdir(parents=True)
        target = folder / "Play Episode.m3u8"
        target.write_bytes(b"user file")
        with self.assertRaisesRegex(RuntimeError, "nothing was overwritten"):
            playlists.make_episode(episode, self.output)
        self.assertEqual(target.read_bytes(), b"user file")

    def test_documented_cli_all_matched_needs_no_external_tools(self):
        import json
        plan = self.root / "plan.json"
        plan.write_text(json.dumps({"episodes": [self.episode()]}), encoding="utf-8")
        process = subprocess.run([sys.executable, str(Path(playlists.__file__).resolve()), "--plan", str(plan),
                                  "--output", str(self.output), "--all-matched"], capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(len(list(self.output.rglob("*.m3u8"))), 1)


if __name__ == "__main__":
    unittest.main()
