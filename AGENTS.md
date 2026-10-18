# AGENTS.md

Instructions for AI coding agents working in this repository.

## What this repo is

A study collection of competitive-programming solutions:

- `LeetCode_Problems/Java/{easy,medium,hard}/NNNN. Title.java`: LeetCode solutions in Java, one file per problem, in the folder for its difficulty.
- `Codeforces_Problems/ProblemSet/<code>.cpp`: Codeforces solutions in C++, named by problem code (`4A.cpp`, `479A.cpp`).
- `data/problems.json`: one entry per solution file. It is the single source for the index in `README.md` and for the stats card `leetcode-stats.svg`.
- `scripts/build_index.py`: keeps `data/problems.json`, the file names, the README index and the stats card in sync.
- `scripts/compile_check.py`: compiles every solution. `scripts/java-stubs/` holds stand-ins for LeetCode's helper classes.

## Data contract: `data/problems.json`

A JSON array of objects, UTF-8, 2-space indent, sorted by platform (`leetcode` first, then `codeforces`) and then by numeric id. `build_index.py --write` writes it in this canonical form; `--check` fails if it is not.

| Field | Type | Meaning |
|---|---|---|
| `platform` | `"leetcode"` or `"codeforces"` | Where the problem is from. |
| `id` | string | LeetCode problem number without padding (`"1"`), or Codeforces contest + index (`"4A"`). |
| `title` | string | Official title from the platform. |
| `slug` | string or null | LeetCode title slug (`"two-sum"`); null for Codeforces. |
| `url` | string or null | The problem's page; null if the platform has no matching problem. |
| `difficulty` | string, integer or null | LeetCode `"Easy"`, `"Medium"` or `"Hard"`; Codeforces integer rating; null if the platform gives none. |
| `tags` | list of strings | The platform's official topic tags. |
| `pattern` | string | The technique this code uses: exactly one value from the list below, or `"Unsorted"` for a new entry that has not been reviewed yet. |
| `key_idea` | string | At most 22 words, plain English: the insight a reader needs to rewrite this solution. Describe what the code does, not what an ideal solution would do. |
| `time` | string | Big-O time of this code. |
| `space` | string | Big-O auxiliary space of this code (see conventions). |
| `language` | `"Java"` or `"C++"` | Language of the file. |
| `path` | string | Repo-relative path with forward slashes. Unique. |

`title`, `slug`, `url`, `difficulty` and `tags` come from the platforms (`build_index.py` fetches them from the LeetCode GraphQL API and the Codeforces API). Never fill them from memory. If a file's code solves a different problem than its number says, keep the file's own title and set `slug`, `url` and `difficulty` to null and `tags` to `[]`; entry 325 is the current example.

### Patterns

Pick the one closest to the technique the code actually uses, not LeetCode's tag list. A brute force over an array is `Arrays & Hashing` or `Simulation`, whichever is closer.

1. Arrays & Hashing
2. Two Pointers
3. Sliding Window
4. Prefix Sum
5. Binary Search
6. Stack
7. Linked List
8. Trees
9. Heap / Priority Queue
10. Graphs
11. Backtracking
12. Dynamic Programming
13. Greedy
14. Intervals
15. Sorting
16. Bit Manipulation
17. Math
18. Strings
19. Simulation
20. Design
21. Trie
22. Union-Find
23. Topological Sort

The README lists patterns in this order and leaves out any with no solutions yet. `Unsorted` comes last when it is not empty.

### Complexity conventions

- Name variables as the problem does: `n` for the main input size, `m` for a second input, `k` and other letters as the problem defines them, `h` for tree height, `V` and `E` for graph size. Use `|s|` when it is clearer which string is meant.
- `space` is auxiliary space: it excludes the input and the returned output, and includes the recursion stack, helper structures and sorting's own memory (`O(log n)` for sorting a primitive array, `O(n)` for sorting objects).
- A map or array over a fixed alphabet (26 letters, ASCII) counts as `O(1)`.
- Write powers with `^` (`O(n^2)`, `O(2^n)`), products with `·` (`O(m·n)`), and add a qualifier when it matters: `O(1) amortized`, `O(n log n) expected`, `O(log n) add, O(1) median`.

### Counts

The README counts line and the stats card count LeetCode solutions by the folder they live in (`easy`, `medium`, `hard`), not by the `difficulty` field.

## Add a solution

1. Write the solution as LeetCode expects it: a `class Solution` (or the class a design problem names) with no imports, because LeetCode imports `java.util` and similar packages for you. Keep LeetCode's helper classes (`ListNode`, `TreeNode`, ...) out of the file; the judge provides them. For Codeforces, a complete C++17 program reading stdin.
2. Save it as `LeetCode_Problems/Java/<difficulty>/NNNN. Title.java` (number zero-padded to 4 digits, folder matching LeetCode's difficulty) or `Codeforces_Problems/ProblemSet/<code>.cpp`.
3. Run `python3 scripts/build_index.py --write`. It adds an entry with the official fields and `"pattern": "Unsorted"` and empty judgement fields. Use `--offline` to skip the network; the title then comes from the file name and the other official fields stay null.
4. Fill in `pattern`, `key_idea`, `time` and `space` for the new entry, then run `--write` again to re-render the README.
5. Validate (below).

Pushing a new file to `main` without steps 3 and 4 also works: the `index.yml` workflow runs `--write` and commits the result, leaving the judgement fields for someone to fill in. A pull request must include the `--write` result, because its check runs `--check`.

## Fix a solution

- Edit the file. If the technique or complexity changes, update its entry and run `--write`.
- To move a file to another difficulty folder, move it and run `--write`; the entry follows the file.
- `--write` fetches official fields only for files that have no entry yet. To refetch them for an existing entry (for example one added with `--offline`), note its judgement fields, delete the entry, run `--write`, and put the judgement fields back.
- If the code does not compile, make the smallest change that fixes it. Do not refactor working solutions.

## Validate

Run all of these before committing; CI runs the same:

```sh
python3 scripts/build_index.py --write       # sync data, names, README and stats card
python3 scripts/build_index.py --check       # must print "Index OK"
python3 scripts/compile_check.py             # must print "All solutions compile."
python3 -m unittest discover -s scripts      # unit tests for the index builder
```

`compile_check.py` needs `javac` (JDK 21 or newer) and a GCC `g++`. On macOS, where `g++` is Clang, pass the Homebrew compiler: `--cxx g++-15`. It accepts file paths to check only some solutions.

If a solution uses a LeetCode helper class that has no stub yet, add it to `scripts/java-stubs/` and to `STUBS` (or, for the problem-specific `Node` classes, `NODE_VARIANTS`) in `compile_check.py`.

## The coach skill

`skills/leetcode-coach/SKILL.md` is a skill for people practising with an agent, shipped as a Claude Code plugin through `.claude-plugin/`. It reads `pattern`, `key_idea`, `title` and `difficulty` from `data/problems.json`, so renaming or removing those fields breaks it. Validate the plugin with `claude plugin validate .` after changing anything under `skills/` or `.claude-plugin/`.

## Rules

- Never hand-edit `README.md` between `<!-- counts:start -->` and `<!-- counts:end -->` or between `<!-- index:start -->` and `<!-- index:end -->`, and never hand-edit `leetcode-stats.svg`. Change `data/problems.json` or the solution files and run `build_index.py --write`.
- Keep every LeetCode solution submittable on LeetCode as is: a `class Solution` (or the design class) with no imports.
- One solution per problem per language. Alternative approaches go in comments inside the same file; a second top-level `class Solution` does not compile.
- `pattern` must be one of the 23 values above or `Unsorted`.
- Official fields come from the platforms, never from memory.
