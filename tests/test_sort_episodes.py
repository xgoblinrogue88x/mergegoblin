from collections import Counter
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import sort_episodes as sorter


class SortTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Daryl's sort ")
        self.source = Path(self.temp.name)
        self.rows = sorter.read_manifest(Path(sorter.__file__).with_name("episode_sort_manifest.csv"))

    def tearDown(self):
        self.temp.cleanup()

    def populate(self):
        original = {}
        for index, row in enumerate(self.rows):
            data = f"Original file {index}: {row['filename']}".encode("utf-8")
            (self.source / row["filename"]).write_bytes(data)
            original[row["filename"]] = data
        return original

    def run_sort(self, preview=False):
        with contextlib.redirect_stdout(io.StringIO()):
            return sorter.sort_files(self.source, self.rows, preview)

    def test_all_290_files_move_once_with_original_names_and_bytes(self):
        original = self.populate()
        unrelated = self.source / "unrelated.txt"
        unrelated.write_text("keep me")
        result = self.run_sort()
        self.assertEqual(result["moved"], 290)
        self.assertEqual(result["episode_folders"], 36)
        for row in self.rows:
            self.assertFalse((self.source / row["filename"]).exists())
            self.assertEqual((self.source / row["folder"] / row["filename"]).read_bytes(), original[row["filename"]])
        self.assertEqual(len(list(self.source.rglob("*.mkv"))), 290)
        self.assertEqual(unrelated.read_text(), "keep me")
        repeated = self.run_sort()
        self.assertEqual(repeated["moved"], 0)
        self.assertEqual(repeated["already_sorted"], 290)

    def test_conflict_aborts_entire_sort_without_overwriting(self):
        original = self.populate()
        row = self.rows[0]
        folder = self.source / row["folder"]
        folder.mkdir()
        (folder / row["filename"]).write_bytes(b"existing user video")
        with self.assertRaisesRegex(RuntimeError, "No videos were moved"):
            self.run_sort()
        for name, data in original.items():
            self.assertEqual((self.source / name).read_bytes(), data)
        self.assertEqual((folder / row["filename"]).read_bytes(), b"existing user video")

    def test_missing_file_aborts_before_any_moves(self):
        original = self.populate()
        absent = self.rows[0]["filename"]
        (self.source / absent).unlink()
        with self.assertRaisesRegex(RuntimeError, "No videos were moved"):
            self.run_sort()
        for name, data in original.items():
            if name != absent:
                self.assertEqual((self.source / name).read_bytes(), data)

    def test_preview_does_not_create_episode_folders_or_move_videos(self):
        original = self.populate()
        result = self.run_sort(preview=True)
        self.assertTrue(result["preview"])
        for name, data in original.items():
            self.assertEqual((self.source / name).read_bytes(), data)
        self.assertFalse(any((self.source / row["folder"]).exists() for row in self.rows))

    def test_interrupted_sort_resumes_without_duplicate_files(self):
        original = self.populate()
        move = sorter.move_without_overwrite
        count = 0
        def interrupted(src, dst):
            nonlocal count
            count += 1
            if count == 11:
                raise OSError("Simulated interruption")
            move(src, dst)
        with patch.object(sorter, "move_without_overwrite", side_effect=interrupted):
            with self.assertRaisesRegex(OSError, "Simulated interruption"):
                self.run_sort()
        result = self.run_sort()
        self.assertEqual(result["already_sorted"], 10)
        self.assertEqual(result["moved"], 280)
        for row in self.rows:
            self.assertEqual((self.source / row["folder"] / row["filename"]).read_bytes(), original[row["filename"]])

    def test_manifest_coverage_and_special_assignments(self):
        self.assertEqual(len(self.rows), 290)
        self.assertEqual(len({sorter.key(row["filename"]) for row in self.rows}), 290)
        counts = Counter(row["episode"] for row in self.rows)
        self.assertEqual(counts[""], 14)
        self.assertEqual(counts["27"], 14)
        self.assertEqual(counts["32"], 7)
        for row in self.rows:
            if row["filename"].startswith("Daryl Hall Live in Jamaica - "):
                self.assertIn("unverified", row["folder"])
                self.assertEqual(row["episode"], "")
            if "Smokey Robinson - Sara Smile" in row["filename"]:
                self.assertEqual(row["episode"], "32" if "(Intro)" in row["filename"] else "22")
            if "Todd Rundgren - Better Watch Your Back" in row["filename"]:
                self.assertEqual(row["episode"], "23")


if __name__ == "__main__":
    unittest.main()
