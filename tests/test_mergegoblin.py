import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

import mergegoblin as app


def catalog(titles, number=7):
    return {"episodes": [{"number": number, "title": f"Episode {number} - Test Guest",
                           "url": "https://www.youtube.com/playlist?list=PLtest",
                           "clips": [{"id": f"video{i:06}", "title": t} for i, t in enumerate(titles)]}]}


class MatchingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def files(self, *titles):
        for title in titles:
            (self.root / (title + ".mkv")).write_bytes(b"fixture")

    def test_actual_channel_listing_finds_88_single_episodes(self):
        listing = Path(__file__).parent / "fixtures" / "channel_playlists.txt"
        rows = [line.split(" | ", 1) for line in listing.read_text(encoding="utf-8").splitlines() if line.strip()]
        found = {}
        for playlist_id, title in rows:
            number = app.episode_number(title)
            if number is not None:
                self.assertNotIn(number, found, f"Duplicate episode number: {title}")
                found[number] = title
        self.assertEqual(len(found), 88)
        self.assertEqual(set(range(1, 92)) - set(found), {2, 13, 29})
        self.assertIn("Chromeo", found[10])
        self.assertIn("Todd Rundgren", found[23])
        self.assertIn("Todd Rundgren", found[40])
        for title in ("Episodes 1 - 10", "Episodes 81 - 91", "Episode 1 - 10", "#1 - 10",
                      "Todd Rundgren", "Daryl Hall - Live at the Ryman Auditorium 2022", "#92 - Guest"):
            with self.subTest(title=title):
                self.assertIsNone(app.episode_number(title))

    def test_spelling_variants_and_playlist_order_preserve_intros(self):
        self.files("Daryl Hall & Plain White Ts - End", "Daryl Hall & Plain White T's - Song",
                   "Daryl Hall & Plain White T's - Song (Intro)")
        titles = ["Daryl Hall & Plain White T’s - Song (Intro)",
                  "Daryl Hall & Plain White T's - Song (Live From Daryl's House)",
                  "Daryl Hall & Plain White T's - End"]
        plan = app.make_plan(self.root, catalog(titles))
        episode = plan["episodes"][0]
        self.assertEqual(episode["issues"], [])
        self.assertIn("E07 - Plain White T's", episode["output"])
        self.assertEqual([c["title"] for c in episode["clips"]], titles)
        self.assertEqual(plan["unmatched_files"], [])
        self.assertEqual(len(plan["undiscovered_episodes"]), 90)

    def test_fuzzy_suggestions_never_selected(self):
        self.files("Daryl Hall & Smokey Robinson - Sara Smile Ohh Baby Baby (Intro)")
        title = "Daryl Hall & Smokey Robinson - Sara Smile Ooh Baby Baby (Intro)"
        episode = app.make_plan(self.root, catalog([title]))["episodes"][0]
        self.assertTrue(episode["issues"])
        self.assertIsNone(episode["clips"][0]["path"])
        self.assertTrue(episode["clips"][0]["suggestions"])

    def test_returning_guest_clip_not_assigned_to_two_episodes(self):
        title = "Daryl Hall & Guest - Song"
        self.files(title)
        data = catalog([title])
        data["episodes"].extend(catalog([title], 8)["episodes"])
        episodes = app.make_plan(self.root, data)["episodes"]
        self.assertTrue(all(any("more than once" in issue for issue in e["issues"]) for e in episodes))

    def test_duplicate_local_titles_held(self):
        title = "Daryl Hall & Guest - Song"
        self.files(title)
        (self.root / (title + ".mp4")).write_bytes(b"duplicate")
        episode = app.make_plan(self.root, catalog([title]))["episodes"][0]
        self.assertIn("Ambiguous", episode["issues"][0])

    def test_video_id_matches_renamed_file(self):
        self.files("renamed [video000000]")
        episode = app.make_plan(self.root, catalog(["Daryl Hall & Guest - Song"]))["episodes"][0]
        self.assertIsNotNone(episode["clips"][0]["path"])
        self.assertIn("E07 - Guest", episode["output"])

    def test_explicit_match_resolves_typo_without_renaming_original(self):
        title = "Daryl Hall & Guest - Misspelled"
        self.files(title)
        data = catalog(["Daryl Hall & Guest - Corrected"])
        plan = app.make_plan(self.root, data, {"video000000": title + ".mkv"})
        self.assertFalse(plan["episodes"][0]["issues"])
        with self.assertRaisesRegex(RuntimeError, "selected folder"):
            app.make_plan(self.root, data, {"video000000": "../outside.mkv"})

    def test_duplicate_episode_numbers_held(self):
        title = "Daryl Hall & Guest - Song"
        self.files(title)
        data = catalog([title])
        data["episodes"] *= 2
        self.assertTrue(all(e["issues"] for e in app.make_plan(self.root, data)["episodes"]))

    def test_fetch_metadata_only_and_skip_episodes_outside_range(self):
        calls = []
        class YoutubeDL:
            def __init__(self, options):
                self.options = options
                self.assert_options()
            def assert_options(self):
                assert self.options["skip_download"]
                assert not self.options.get("nocheckcertificate")
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def extract_info(self, url, download):
                calls.append(url)
                assert download is False
                if url == app.CHANNEL:
                    return {"entries": [{"id": "PLtest", "title": "#7 - Daryl Hall hosts Test Guest on Live From Daryl's House"},
                                        {"id": "PLother", "title": "Episode 92"},
                                        {"id": "PLunknown", "title": "Unnumbered music"},
                                        {"id": "PLcollection", "title": "Episodes 1 - 10"}]}
                return {"entries": [{"id": "abcdefghijk", "title": "Song"}, None]}
        with patch.dict(sys.modules, {"yt_dlp": types.SimpleNamespace(YoutubeDL=YoutubeDL)}):
            data = app.fetch_catalog(self.root / "catalog.json")
        self.assertEqual(len(calls), 2)
        self.assertEqual(len(data["ignored_playlists"]), 3)
        self.assertEqual(data["episodes"][0]["number"], 7)
        self.assertEqual(data["episodes"][0]["clips"][1]["title"], "[Unavailable video]")
        self.assertEqual(len(app.read_json(self.root / "channel-playlists.json")["playlists"]), 4)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg integration dependencies missing")
class VideoTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="Daryl's videos ")
        self.root = Path(self.temporary.name)
        self.inputs = self.root / "input"
        self.inputs.mkdir()
        self.output = self.root / "output"

    def tearDown(self):
        self.temporary.cleanup()

    def clip(self, title, size="160x120", color="red"):
        path = self.inputs / (title + ".mkv")
        app.run([shutil.which("ffmpeg"), "-v", "error", "-nostdin", "-n", "-f", "lavfi", "-i",
                 f"color=c={color}:s={size}:r=30:d=0.4", "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000:duration=0.4",
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(path)])
        return path

    def episode(self, mixed=False):
        titles = ["Daryl Hall & Guest - Song (Intro)", "Daryl Hall & Guest - Song #2; encore=great"]
        self.clip(titles[0])
        self.clip(titles[1], "320x240" if mixed else "160x120", "blue")
        return app.make_plan(self.inputs, catalog(titles))["episodes"][0]

    def test_real_merge_chapters_resume_and_changed_input(self):
        episode = self.episode()
        before = {p.name: p.read_bytes() for p in self.inputs.iterdir()}
        self.assertEqual(app.merge_episode(episode, self.output), "merged")
        result = app.probe(self.output / episode["output"])
        self.assertEqual(len(result["chapters"]), 2)
        self.assertEqual(result["chapters"][1]["tags"]["title"], "Song #2; encore=great")
        self.assertAlmostEqual(float(result["chapters"][1]["start_time"]),
                               app.media_info(Path(episode["clips"][0]["path"]))[0], delta=0.002)
        self.assertEqual(app.merge_episode(episode, self.output), "skipped")
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.inputs.iterdir()})
        path = Path(episode["clips"][0]["path"])
        path.write_bytes(path.read_bytes() + b"changed")
        with self.assertRaisesRegex(RuntimeError, "changed since scanning"):
            app.merge_episode(episode, self.output)

    def test_mixed_formats_held_then_conversion_passes(self):
        episode = self.episode(mixed=True)
        with self.assertRaisesRegex(RuntimeError, "formats differ"):
            app.merge_episode(episode, self.output)
        self.assertFalse((self.output / episode["output"]).exists())
        self.assertEqual(app.merge_episode(episode, self.output, convert=True), "merged")
        self.assertEqual(len(app.probe(self.output / episode["output"])["chapters"]), 2)

    def test_never_overwrites_existing_output(self):
        episode = self.episode()
        self.output.mkdir()
        target = self.output / episode["output"]
        target.write_bytes(b"user file")
        with self.assertRaisesRegex(RuntimeError, "already exists"):
            app.merge_episode(episode, self.output)
        self.assertEqual(target.read_bytes(), b"user file")

    def test_corrupt_input_never_publishes_output(self):
        title = "Daryl Hall & Guest - Song"
        (self.inputs / (title + ".mkv")).write_bytes(b"not a video")
        episode = app.make_plan(self.inputs, catalog([title]))["episodes"][0]
        with self.assertRaises(RuntimeError):
            app.merge_episode(episode, self.output)
        self.assertFalse((self.output / episode["output"]).exists())

    def test_documented_cli_scan_then_merge(self):
        episode = self.episode()
        catalog_path = self.root / "catalog.json"
        plan_path = self.root / "plan.json"
        app.write_json(catalog_path, catalog([c["title"] for c in episode["clips"]]))
        script = str(Path(app.__file__).resolve())
        app.run([sys.executable, script, "scan", "--input", str(self.inputs), "--catalog", str(catalog_path), "--plan", str(plan_path)])
        self.assertIn("MATCHED", plan_path.with_suffix(".txt").read_text(encoding="utf-8"))
        app.run([sys.executable, script, "merge", "--plan", str(plan_path), "--output", str(self.output), "--reviewed"])
        self.assertEqual(len(app.probe(self.output / episode["output"])["chapters"]), 2)


if __name__ == "__main__":
    unittest.main()
