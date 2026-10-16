import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import sort_episodes as sorter
import undo_sort as undo


class UndoSortTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Daryl's undo ")
        self.root = Path(self.temp.name)
        self.rows = sorter.read_manifest(Path(sorter.__file__).with_name("episode_sort_manifest.csv"))
        self.original = {}
        for i, row in enumerate(self.rows):
            data = f"original {i}".encode()
            self.original[row["filename"]] = data
            (self.root / row["filename"]).write_bytes(data)
        with contextlib.redirect_stdout(io.StringIO()):
            sorter.sort_files(self.root, self.rows)

    def tearDown(self):
        self.temp.cleanup()

    def restore(self, preview=False):
        with contextlib.redirect_stdout(io.StringIO()):
            return undo.undo(self.root, preview)

    def test_restores_all_290_originals_and_repeat_run_is_safe(self):
        result = self.restore()
        self.assertEqual(result["restored"], 290)
        for row in self.rows:
            self.assertEqual((self.root / row["filename"]).read_bytes(), self.original[row["filename"]])
            self.assertFalse((self.root / row["folder"] / row["filename"]).exists())
        self.assertEqual(len(list(self.root.rglob("*.mkv"))), 290)
        self.assertEqual(self.restore(), {"restored": 0, "already_restored": 290})

    def test_original_location_conflict_stops_every_restore(self):
        conflict = self.root / self.rows[0]["filename"]
        conflict.write_bytes(b"new user file")
        with self.assertRaisesRegex(RuntimeError, "Both locations"):
            self.restore()
        self.assertEqual(conflict.read_bytes(), b"new user file")
        for row in self.rows:
            self.assertTrue((self.root / row["folder"] / row["filename"]).exists())

    def test_changed_sorted_file_stops_before_any_restore(self):
        row = self.rows[0]
        (self.root / row["folder"] / row["filename"]).write_bytes(b"edited video")
        with self.assertRaisesRegex(RuntimeError, "changed since"):
            self.restore()
        self.assertFalse(any((self.root / row["filename"]).exists() for row in self.rows))

    def test_resume_after_interrupted_undo(self):
        execute = undo.move_without_overwrite
        count = 0
        def interrupted(src, dst):
            nonlocal count
            count += 1
            if count == 11:
                raise OSError("interrupted")
            execute(src, dst)
        with patch.object(undo, "move_without_overwrite", side_effect=interrupted):
            with self.assertRaisesRegex(OSError, "interrupted"):
                self.restore()
        self.assertEqual(self.restore(), {"restored": 280, "already_restored": 10})

    def test_preview_does_not_restore_any_files(self):
        self.assertTrue(self.restore(preview=True)["preview"])
        self.assertFalse(any((self.root / row["filename"]).exists() for row in self.rows))

    def test_log_cannot_restore_outside_selected_root(self):
        log = self.root / "_Sorting Reports" / "Run 001" / "move-log.jsonl"
        event = {"action": "moving", "source": str(self.root.parent / "outside.mkv"),
                 "destination": str(self.root / "E01" / "outside.mkv"), "size": 1, "mtime_ns": 1}
        with log.open("a") as file:
            file.write(json.dumps(event) + "\n")
        with self.assertRaisesRegex(RuntimeError, "outside the selected"):
            self.restore()
        self.assertFalse(any((self.root / row["filename"]).exists() for row in self.rows))


if __name__ == "__main__":
    unittest.main()
