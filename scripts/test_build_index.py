"""Tests for build_index.py. Run with: python3 -m unittest discover -s scripts"""

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_index as bi  # noqa: E402

README = """# Fixture

<!-- counts:start -->
<!-- counts:end -->

## The index

<!-- index:start -->
<!-- index:end -->
"""


def entry(platform, pid, title, path, pattern, url, difficulty, key_idea="", time="O(n)", space="O(1)"):
    return {
        "platform": platform,
        "id": pid,
        "title": title,
        "slug": None,
        "url": url,
        "difficulty": difficulty,
        "tags": [],
        "pattern": pattern,
        "key_idea": key_idea,
        "time": time,
        "space": space,
        "language": "Java" if platform == "leetcode" else "C++",
        "path": path,
    }


FIXTURE = [
    entry("leetcode", "1", "Two Sum", "LeetCode_Problems/Java/easy/0001. Two Sum.java", "Arrays & Hashing",
          "https://leetcode.com/problems/two-sum/", "Easy", "Map value to index; look up target − x.", "O(n)", "O(n)"),
    entry("leetcode", "42", "Trapping Rain Water", "LeetCode_Problems/Java/hard/0042. Trapping Rain Water.java",
          "Two Pointers", "https://leetcode.com/problems/trapping-rain-water/", "Hard", "Move the lower side inward."),
    entry("codeforces", "4A", "Watermelon", "Codeforces_Problems/ProblemSet/4A.cpp", "Math",
          "https://codeforces.com/problemset/problem/4/A", 800, "Even and greater than 2.", "O(1)", "O(1)"),
]


def quiet(fn, *args, **kwargs):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(*args, **kwargs)
    return code, out.getvalue() + err.getvalue()


class RepoTestCase(unittest.TestCase):
    """A throwaway repo with the three fixture solutions, already indexed."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)
        for e in FIXTURE:
            p = self.root / e["path"]
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("class Solution {}\n", encoding="utf-8")
        self.write_entries(FIXTURE)
        (self.root / "README.md").write_text(README, encoding="utf-8")
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 0, output)

    def write_entries(self, entries):
        (self.root / "data").mkdir(exist_ok=True)
        (self.root / bi.DATA_FILE).write_text(bi.dump_json(entries), encoding="utf-8")

    def read_entries(self):
        return json.loads((self.root / bi.DATA_FILE).read_text(encoding="utf-8"))

    def run_cli(self, *args):
        return quiet(bi.main, [*args, "--root", str(self.root)])


class NormalizeFilenameTest(unittest.TestCase):
    def test_pads_number_to_four_digits(self):
        self.assertEqual(bi.normalize_leetcode_name("1. Two Sum.java"), "0001. Two Sum.java")

    def test_fixes_missing_dot_and_spacing(self):
        self.assertEqual(bi.normalize_leetcode_name("42.Trapping Rain Water.java"), "0042. Trapping Rain Water.java")
        self.assertEqual(bi.normalize_leetcode_name("15 3Sum.java"), "0015. 3Sum.java")

    def test_keeps_a_normalized_name(self):
        self.assertEqual(bi.normalize_leetcode_name("0001. Two Sum.java"), "0001. Two Sum.java")
        self.assertEqual(bi.normalize_leetcode_name("3959. Check Good Integer.java"), "3959. Check Good Integer.java")

    def test_rejects_a_name_without_a_number(self):
        self.assertIsNone(bi.normalize_leetcode_name("Two Sum.java"))


class CheckTest(RepoTestCase):
    def test_passes_on_a_fresh_index(self):
        code, output = self.run_cli("--check")
        self.assertEqual(code, 0, output)

    def test_fails_on_unknown_pattern(self):
        entries = self.read_entries()
        entries[0]["pattern"] = "Recursion"
        self.write_entries(entries)
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("unknown pattern 'Recursion'", output)

    def test_fails_when_a_file_has_no_entry(self):
        new = self.root / "LeetCode_Problems/Java/easy/0009. Palindrome Number.java"
        new.write_text("class Solution {}\n", encoding="utf-8")
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("0009. Palindrome Number.java has no entry", output)

    def test_fails_when_readme_is_out_of_date(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace("Trapping Rain Water", "Rain"), encoding="utf-8")
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("README.md index is out of date", output)

    def test_fails_on_duplicate_path(self):
        entries = self.read_entries()
        self.write_entries(entries + [dict(entries[0])])
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("duplicate path", output)

    def test_fails_on_invalid_json(self):
        (self.root / bi.DATA_FILE).write_text("[{", encoding="utf-8")
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("not valid JSON", output)

    def test_fails_on_broken_entries_and_write_refuses_them(self):
        entries = self.read_entries()
        entries[0]["platform"] = "LeetCode"
        del entries[1]["time"]
        entries[2]["tags"] = "math"
        self.write_entries(entries)
        for args in (("--check",), ("--write", "--offline")):
            code, output = self.run_cli(*args)
            self.assertEqual(code, 1, args)
            self.assertIn("platform must be one of leetcode, codeforces", output)
            self.assertIn("missing field(s) time", output)
            self.assertIn("tags must be a list of strings", output)
        self.assertNotIn("time", self.read_entries()[1])

    def test_fails_when_entry_id_disagrees_with_file_name(self):
        entries = self.read_entries()
        entries[0]["id"] = "9999"
        self.write_entries(entries)
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("id is '9999', but the file name says '1'", output)

    def test_fails_on_leetcode_file_outside_a_difficulty_folder(self):
        (self.root / "LeetCode_Problems/Java/0009. Palindrome Number.java").write_text("class Solution {}\n")
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("put LeetCode solutions in LeetCode_Problems/Java/easy, medium or hard", output)

    def test_fails_when_a_name_needs_normalizing(self):
        old = self.root / "LeetCode_Problems/Java/easy/0001. Two Sum.java"
        old.rename(old.with_name("1. Two Sum.java"))
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("should be named LeetCode_Problems/Java/easy/0001. Two Sum.java", output)


class WriteTest(RepoTestCase):
    def test_adds_unsorted_entry_offline_and_normalizes_name(self):
        new = self.root / "LeetCode_Problems/Java/medium/7. Reverse Integer.java"
        new.parent.mkdir(parents=True, exist_ok=True)
        new.write_text("class Solution {}\n", encoding="utf-8")
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 0, output)
        self.assertTrue((self.root / "LeetCode_Problems/Java/medium/0007. Reverse Integer.java").exists())
        added = [e for e in self.read_entries() if e["id"] == "7"][0]
        self.assertEqual(added["title"], "Reverse Integer")
        self.assertEqual(added["pattern"], "Unsorted")
        self.assertEqual((added["key_idea"], added["time"], added["space"]), ("", "", ""))
        self.assertIsNone(added["url"])
        self.assertIn("### Unsorted", (self.root / "README.md").read_text(encoding="utf-8"))
        code, output = self.run_cli("--check")
        self.assertEqual(code, 0, output)

    def test_rename_keeps_existing_judgement_fields(self):
        old = self.root / "LeetCode_Problems/Java/hard/0042. Trapping Rain Water.java"
        old.rename(old.with_name("42. Trapping Rain Water.java"))
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 0, output)
        kept = [e for e in self.read_entries() if e["id"] == "42"][0]
        self.assertEqual(kept["pattern"], "Two Pointers")
        self.assertEqual(kept["path"], "LeetCode_Problems/Java/hard/0042. Trapping Rain Water.java")

    def test_moving_a_file_to_another_folder_keeps_its_entry(self):
        old = self.root / "LeetCode_Problems/Java/hard/0042. Trapping Rain Water.java"
        new = self.root / "LeetCode_Problems/Java/medium/0042. Trapping Rain Water.java"
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)
        code, output = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("but the file is now LeetCode_Problems/Java/medium/0042. Trapping Rain Water.java", output)
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 0, output)
        moved = [e for e in self.read_entries() if e["id"] == "42"]
        self.assertEqual(len(moved), 1)
        self.assertEqual(moved[0]["pattern"], "Two Pointers")
        self.assertEqual(moved[0]["path"], "LeetCode_Problems/Java/medium/0042. Trapping Rain Water.java")

    def test_refuses_a_second_solution_for_the_same_problem(self):
        (self.root / "LeetCode_Problems/Java/easy/0001. Two Sum Again.java").write_text("class Solution {}\n")
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 1)
        self.assertIn("2 Java solutions for leetcode 1", output)

    def test_drops_entry_whose_file_is_gone(self):
        (self.root / "Codeforces_Problems/ProblemSet/4A.cpp").unlink()
        code, output = self.run_cli("--write", "--offline")
        self.assertEqual(code, 0, output)
        self.assertEqual([e["id"] for e in self.read_entries()], ["1", "42"])
        self.assertNotIn("## Codeforces", (self.root / "README.md").read_text(encoding="utf-8"))


class RenderTest(unittest.TestCase):
    def test_three_entry_fixture_renders_expected_rows(self):
        index = bi.render_index(FIXTURE)
        self.assertIn("| [Arrays & Hashing](#arrays--hashing) | 1 |", index)
        self.assertIn("| [Two Pointers](#two-pointers) | 1 |", index)
        self.assertIn("| [Codeforces](#codeforces) | 1 |", index)
        self.assertIn(
            "| [1](https://leetcode.com/problems/two-sum/) "
            "| [Two Sum](LeetCode_Problems/Java/easy/0001.%20Two%20Sum.java) "
            "| Easy | Map value to index; look up target − x. | O(n) | O(n) |",
            index,
        )
        self.assertIn(
            "| [42](https://leetcode.com/problems/trapping-rain-water/) "
            "| [Trapping Rain Water](LeetCode_Problems/Java/hard/0042.%20Trapping%20Rain%20Water.java) "
            "| Hard | Move the lower side inward. | O(n) | O(1) |",
            index,
        )
        self.assertIn(
            "| [4A](https://codeforces.com/problemset/problem/4/A) "
            "| [Watermelon](Codeforces_Problems/ProblemSet/4A.cpp) "
            "| 800 | Math | Even and greater than 2. | O(1) | O(1) |",
            index,
        )
        self.assertLess(index.index("### Arrays & Hashing"), index.index("### Two Pointers"))
        self.assertLess(index.index("### Two Pointers"), index.index("## Codeforces"))

    def test_counts_line(self):
        self.assertEqual(
            bi.render_counts(FIXTURE),
            "**2 LeetCode** (1 Easy · 0 Medium · 1 Hard) and **1 Codeforces** solutions, organized by 3 techniques.",
        )

    def test_pipes_in_cells_are_escaped(self):
        row = bi.render_index([dict(FIXTURE[0], key_idea="add |a − b| to the total")])
        self.assertIn("add \\|a − b\\| to the total", row)

    def test_anchor_matches_github(self):
        self.assertEqual(bi.github_anchor("Heap / Priority Queue"), "heap--priority-queue")
        self.assertEqual(bi.github_anchor("Union-Find"), "union-find")

    def test_stats_card_shows_folder_counts(self):
        svg = bi.render_svg(FIXTURE)
        self.assertIn('font-size="85">2</text>', svg)
        self.assertIn('width="220" height="10" fill="#008a3e"', svg)


if __name__ == "__main__":
    unittest.main()
