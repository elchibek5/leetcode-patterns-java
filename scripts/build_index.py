#!/usr/bin/env python3
"""Build the problem index from data/problems.json.

    python3 scripts/build_index.py --write     # sync data, file names, README and stats card
    python3 scripts/build_index.py --check     # exit 1 if --write would change anything

--write adds an entry for every solution file that has none (official
fields fetched from LeetCode or Codeforces unless --offline), normalizes
LeetCode file names to "NNNN. Title.java", drops entries whose file is
gone, re-renders the README sections between the markers and the stats
SVG, and writes data/problems.json deterministically.

--check never touches the network. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = "data/problems.json"
README_FILE = "README.md"
SVG_FILE = "leetcode-stats.svg"
LEETCODE_DIR = "LeetCode_Problems/Java"
CODEFORCES_DIR = "Codeforces_Problems"

PATTERNS = [
    "Arrays & Hashing",
    "Two Pointers",
    "Sliding Window",
    "Prefix Sum",
    "Binary Search",
    "Stack",
    "Linked List",
    "Trees",
    "Heap / Priority Queue",
    "Graphs",
    "Backtracking",
    "Dynamic Programming",
    "Greedy",
    "Intervals",
    "Sorting",
    "Bit Manipulation",
    "Math",
    "Strings",
    "Simulation",
    "Design",
    "Trie",
    "Union-Find",
    "Topological Sort",
]
UNSORTED = "Unsorted"

FIELDS = [
    "platform", "id", "title", "slug", "url", "difficulty", "tags",
    "pattern", "key_idea", "time", "space", "language", "path",
]
PLATFORM_ORDER = {"leetcode": 0, "codeforces": 1}
LANGUAGES = {".java": "Java", ".cpp": "C++"}
DIFFICULTY_FOLDERS = ["easy", "medium", "hard"]

MARKERS = {
    "counts": ("<!-- counts:start -->", "<!-- counts:end -->"),
    "index": ("<!-- index:start -->", "<!-- index:end -->"),
}

LEETCODE_NAME = re.compile(r"^(\d+)\s*\.?\s*(.*?)\s*\.java$")
CODEFORCES_NAME = re.compile(r"^(\d+)([A-Z][0-9]?)\.cpp$")

REQUEST_DELAY = 0.3  # seconds between requests to the same platform


class FetchError(Exception):
    """The platform could not be reached or answered with something unusable."""


# --------------------------------------------------------------------------- names


def normalize_leetcode_name(filename: str) -> str | None:
    """'1. Two Sum.java' -> '0001. Two Sum.java'. None if the name has no problem number."""
    m = LEETCODE_NAME.match(filename)
    if not m or not m.group(2):
        return None
    return f"{int(m.group(1)):04d}. {m.group(2)}.java"


def parse_leetcode_name(filename: str) -> tuple[str, str] | None:
    """'0001. Two Sum.java' -> ('1', 'Two Sum')."""
    m = LEETCODE_NAME.match(filename)
    if not m or not m.group(2):
        return None
    return str(int(m.group(1))), m.group(2)


def parse_codeforces_name(filename: str) -> str | None:
    """'4A.cpp' -> '4A'."""
    m = CODEFORCES_NAME.match(filename)
    return m.group(1) + m.group(2) if m else None


def file_problem_id(platform: str, path: str) -> str | None:
    name = path.rsplit("/", 1)[-1]
    if platform == "leetcode":
        parsed = parse_leetcode_name(name)
        return parsed[0] if parsed else None
    return parse_codeforces_name(name)


def sort_key(entry: dict) -> tuple:
    m = re.match(r"(\d+)(.*)", str(entry.get("id") or ""))
    number, suffix = (int(m.group(1)), m.group(2)) if m else (sys.maxsize, str(entry.get("id")))
    platform = str(entry.get("platform"))
    return (PLATFORM_ORDER.get(platform, len(PLATFORM_ORDER)), platform, number, suffix, str(entry.get("path")))


# --------------------------------------------------------------------------- files


@dataclass
class SolutionFile:
    path: str          # repo-relative, forward slashes
    platform: str
    language: str


def list_solution_files(root: Path) -> list[SolutionFile]:
    files = []
    for base, platform, ext in ((LEETCODE_DIR, "leetcode", ".java"), (CODEFORCES_DIR, "codeforces", ".cpp")):
        top = root / base
        if not top.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(top):
            dirnames.sort()
            for name in sorted(filenames):
                if name.endswith(ext):
                    rel = (Path(dirpath) / name).relative_to(root).as_posix()
                    files.append(SolutionFile(rel, platform, LANGUAGES[ext]))
    return files


# --------------------------------------------------------------------------- fetching


def _http_json(url: str, payload: dict | None = None, headers: dict | None = None) -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(url, data=data, headers={"User-Agent": "Mozilla/5.0", **(headers or {})})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        raise FetchError(f"{url}: {exc}") from exc


LEETCODE_QUERY = (
    "query questionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {"
    " questionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters) {"
    " totalNum data { questionFrontendId title titleSlug difficulty topicTags { name } } } }"
)


def fetch_leetcode(problem_id: str) -> dict | None:
    """Official fields for one LeetCode problem number, or None if LeetCode has no such number."""
    payload = {
        "query": LEETCODE_QUERY,
        "variables": {"categorySlug": "", "skip": 0, "limit": 100, "filters": {"searchKeywords": problem_id}},
    }
    body = _http_json(
        "https://leetcode.com/graphql",
        payload,
        {"Content-Type": "application/json", "Referer": "https://leetcode.com/problemset/"},
    )
    try:
        questions = body["data"]["questionList"]["data"]
    except (KeyError, TypeError) as exc:
        raise FetchError(f"unexpected LeetCode response: {str(body)[:200]}") from exc
    for q in questions:
        if q.get("questionFrontendId") == problem_id:
            return {
                "title": q["title"],
                "slug": q["titleSlug"],
                "url": f"https://leetcode.com/problems/{q['titleSlug']}/",
                "difficulty": q["difficulty"],
                "tags": [t["name"] for t in q.get("topicTags") or []],
            }
    return None


_codeforces_cache: dict[str, dict] | None = None


def fetch_codeforces(code: str) -> dict | None:
    """Official fields for one Codeforces problem code such as '4A', or None if unknown."""
    global _codeforces_cache
    if _codeforces_cache is None:
        body = _http_json("https://codeforces.com/api/problemset.problems")
        if body.get("status") != "OK":
            raise FetchError(f"Codeforces API: {body.get('comment', body.get('status'))}")
        _codeforces_cache = {f"{p['contestId']}{p['index']}": p for p in body["result"]["problems"] if "contestId" in p}
    p = _codeforces_cache.get(code)
    if p is None:
        return None
    return {
        "title": p["name"],
        "slug": None,
        "url": f"https://codeforces.com/problemset/problem/{p['contestId']}/{p['index']}",
        "difficulty": p.get("rating"),
        "tags": list(p.get("tags") or []),
    }


# --------------------------------------------------------------------------- entries


def new_entry(f: SolutionFile, online: bool, log) -> dict | None:
    name = f.path.rsplit("/", 1)[-1]
    if f.platform == "leetcode":
        parsed = parse_leetcode_name(name)
        if parsed is None:
            return None
        problem_id, file_title = parsed
        fallback_title = file_title
    else:
        problem_id = parse_codeforces_name(name)
        if problem_id is None:
            return None
        fallback_title = problem_id
    official = None
    if online:
        official = fetch_leetcode(problem_id) if f.platform == "leetcode" else fetch_codeforces(problem_id)
        time.sleep(REQUEST_DELAY)
        if official is None:
            log(f"warning: {f.platform} has no problem {problem_id} ({f.path}); official fields left empty")
    official = official or {"title": fallback_title, "slug": None, "url": None, "difficulty": None, "tags": []}
    return {
        "platform": f.platform,
        "id": problem_id,
        **official,
        "pattern": UNSORTED,
        "key_idea": "",
        "time": "",
        "space": "",
        "language": f.language,
        "path": f.path,
    }


def ordered(entry: dict) -> dict:
    known = {k: entry.get(k) for k in FIELDS}
    extra = {k: v for k, v in entry.items() if k not in known}
    return {**known, **extra}


def dump_json(entries: list[dict]) -> str:
    return json.dumps(entries, indent=2, ensure_ascii=False) + "\n"


# --------------------------------------------------------------------------- rendering


def github_anchor(heading: str) -> str:
    """The id GitHub gives a Markdown heading."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def cell(value) -> str:
    """Escape text for a Markdown table cell."""
    text = "" if value is None else str(value)
    text = text.replace("\\", "\\\\")
    for ch in "|*_`<":
        text = text.replace(ch, "\\" + ch)
    return text.replace("\n", " ").strip()


def file_link(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def counts(entries: list[dict]) -> dict:
    leetcode = [e for e in entries if e.get("platform") == "leetcode"]
    by_folder = Counter()
    for e in leetcode:
        parts = str(e.get("path", "")).split("/")
        if len(parts) >= 2 and parts[-2] in DIFFICULTY_FOLDERS:
            by_folder[parts[-2]] += 1
    used = {e.get("pattern") for e in entries} & set(PATTERNS)
    return {
        "leetcode": len(leetcode),
        "easy": by_folder["easy"],
        "medium": by_folder["medium"],
        "hard": by_folder["hard"],
        "codeforces": sum(1 for e in entries if e.get("platform") == "codeforces"),
        "techniques": len(used),
    }


def render_counts(entries: list[dict]) -> str:
    c = counts(entries)
    technique_word = "technique" if c["techniques"] == 1 else "techniques"
    return (
        f"**{c['leetcode']} LeetCode** ({c['easy']} Easy · {c['medium']} Medium · {c['hard']} Hard) "
        f"and **{c['codeforces']} Codeforces** solutions, organized by {c['techniques']} {technique_word}."
    )


def number_cell(entry: dict) -> str:
    return f"[{cell(entry['id'])}]({entry['url']})" if entry.get("url") else cell(entry["id"])


def problem_cell(entry: dict) -> str:
    return f"[{cell(entry.get('title'))}]({file_link(entry['path'])})"


def render_index(entries: list[dict]) -> str:
    leetcode = sorted((e for e in entries if e.get("platform") == "leetcode"), key=sort_key)
    others = sorted((e for e in entries if e.get("platform") != "leetcode"), key=sort_key)
    groups = {p: [e for e in leetcode if e.get("pattern") == p] for p in PATTERNS + [UNSORTED]}
    sections = [p for p in PATTERNS + [UNSORTED] if groups[p]]

    lines = ["| Technique | Problems |", "|---|---:|"]
    for p in sections:
        lines.append(f"| [{cell(p)}](#{github_anchor(p)}) | {len(groups[p])} |")
    if others:
        lines.append(f"| [Codeforces](#codeforces) | {len(others)} |")

    for p in sections:
        lines += ["", f"### {p}", "", "| # | Problem | Difficulty | Key idea | Time | Space |", "|---|---|---|---|---|---|"]
        for e in groups[p]:
            lines.append(
                f"| {number_cell(e)} | {problem_cell(e)} | {cell(e.get('difficulty') or '—')} "
                f"| {cell(e.get('key_idea'))} | {cell(e.get('time'))} | {cell(e.get('space'))} |"
            )

    if others:
        lines += ["", "## Codeforces", "", "| # | Problem | Rating | Technique | Key idea | Time | Space |",
                  "|---|---|---|---|---|---|---|"]
        for e in others:
            rating = e.get("difficulty")
            lines.append(
                f"| {number_cell(e)} | {problem_cell(e)} | {cell(rating if rating is not None else '—')} "
                f"| {cell(e.get('pattern'))} | {cell(e.get('key_idea'))} | {cell(e.get('time'))} | {cell(e.get('space'))} |"
            )
    # The trailing blank line ends the last table before the closing marker;
    # without it GitHub can read the marker line as one more table row.
    return "\n".join(lines) + "\n"


def replace_between(text: str, start: str, end: str, body: str) -> str:
    i = text.find(start)
    j = text.find(end, i + len(start)) if i != -1 else -1
    if i == -1 or j == -1:
        raise ValueError(f"README.md is missing the {start} … {end} markers")
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


def render_readme(readme: str, entries: list[dict]) -> str:
    readme = replace_between(readme, *MARKERS["counts"], render_counts(entries))
    return replace_between(readme, *MARKERS["index"], render_index(entries))


def render_svg(entries: list[dict]) -> str:
    c = counts(entries)
    easy, medium, hard = c["easy"], c["medium"], c["hard"]
    total = easy + medium + hard
    if total == 0: total = 1

    # 3. DRAW DEATH NOTE SVG
    easy_width = int((easy / total) * 440)
    medium_width = int((medium / total) * 440)
    hard_width = int((hard / total) * 440)

    svg_content = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="blood-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4a0000" />
      <stop offset="50%" stop-color="#8a0303" />
      <stop offset="100%" stop-color="#ff0000" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .gothic {{ font-family: 'Times New Roman', serif; font-weight: 900; }}
    .typewriter {{ font-family: 'Courier New', Courier, monospace; font-weight: bold; }}
    @keyframes flicker {{
      0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{ opacity: 1; text-shadow: 0 0 12px #ff0000; }}
      20%, 22%, 24%, 55% {{ opacity: 0; text-shadow: none; }}
    }}
    @keyframes heartbeat {{
      0% {{ transform: scale(1); filter: drop-shadow(0 0 4px #ff0000); }}
      14% {{ transform: scale(1.05); filter: drop-shadow(0 0 15px #ff0000); }}
      28% {{ transform: scale(1); filter: drop-shadow(0 0 4px #ff0000); }}
      42% {{ transform: scale(1.05); filter: drop-shadow(0 0 15px #ff0000); }}
      70% {{ transform: scale(1); filter: drop-shadow(0 0 4px #ff0000); }}
    }}
    @keyframes inkBleed {{ from {{ width: 0; opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes typeIn {{ from {{ opacity: 0; transform: translateX(-15px); }} to {{ opacity: 1; transform: translateX(0); }} }}

    .flicker-text {{ animation: flicker 4s infinite; fill: #d40000; }}
    .pulse-number {{ transform-origin: 50px 300px; animation: heartbeat 2s infinite; fill: #ffffff; }}
    .rule-text {{ fill: #888888; font-size: 15px; opacity: 0; animation: typeIn 1s forwards; }}
    .ink-easy {{ animation: inkBleed 1.5s cubic-bezier(0.1, 0.9, 0.2, 1) forwards 1s; opacity: 0; }}
    .ink-medium {{ animation: inkBleed 1.5s cubic-bezier(0.1, 0.9, 0.2, 1) forwards 1.3s; opacity: 0; }}
    .ink-hard {{ animation: inkBleed 1.5s cubic-bezier(0.1, 0.9, 0.2, 1) forwards 1.6s; opacity: 0; }}
  </style>

  <rect width="800" height="400" fill="#030303" />
  <text x="400" y="350" class="gothic" font-size="300" fill="#0a0a0a" text-anchor="middle" font-style="italic">L.C.</text>

  <text x="40" y="70" class="gothic flicker-text" font-size="44" letter-spacing="3">LEETCODE NOTE</text>
  <text x="40" y="115" class="typewriter rule-text" style="animation-delay: 0.2s;" fill="#ffffff">How to use it:</text>
  <text x="40" y="140" class="typewriter rule-text" style="animation-delay: 0.5s;">The problem whose algorithm is</text>
  <text x="40" y="165" class="typewriter rule-text" style="animation-delay: 0.7s;">written in this repository</text>
  <text x="40" y="190" class="typewriter rule-text" style="animation-delay: 0.9s;">shall be solved.</text>

  <g transform="translate(40, 260)">
    <text x="0" y="0" class="typewriter" font-size="18" fill="#d40000" filter="url(#glow)">TOTAL ELIMINATED</text>
    <text x="0" y="75" class="gothic pulse-number" font-size="85">{total}</text>
  </g>

  <line x1="310" y1="40" x2="310" y2="360" stroke="#1a0000" stroke-width="3" />

  <g transform="translate(350, 170)">
    <text x="0" y="0" class="gothic" font-size="22" fill="#a0a0a0">Casualties (Easy)</text>
    <text x="440" y="0" class="typewriter" font-size="22" fill="#ffffff" text-anchor="end">{easy}</text>
    <rect x="0" y="15" width="440" height="10" fill="#111111" />
    <rect class="ink-easy" x="0" y="15" width="{easy_width}" height="10" fill="#008a3e" />
  </g>

  <g transform="translate(350, 250)">
    <text x="0" y="0" class="gothic" font-size="22" fill="#a0a0a0">Targets (Medium)</text>
    <text x="440" y="0" class="typewriter" font-size="22" fill="#ffffff" text-anchor="end">{medium}</text>
    <rect x="0" y="15" width="440" height="10" fill="#111111" />
    <rect class="ink-medium" x="0" y="15" width="{medium_width}" height="10" fill="#d47900" />
  </g>

  <g transform="translate(350, 330)">
    <text x="0" y="0" class="gothic" font-size="22" fill="#a0a0a0">Special Grade (Hard)</text>
    <text x="440" y="0" class="typewriter" font-size="22" fill="#ffffff" text-anchor="end">{hard}</text>
    <rect x="0" y="15" width="440" height="10" fill="#111111" />
    <rect class="ink-hard" x="0" y="15" width="{hard_width}" height="10" fill="url(#blood-gradient)" filter="url(#glow)"/>
  </g>
</svg>
"""
    return svg_content


# --------------------------------------------------------------------------- plan


@dataclass
class Plan:
    renames: list[tuple[str, str]] = field(default_factory=list)
    moved: list[tuple[str, str]] = field(default_factory=list)
    added: list[str] = field(default_factory=list)
    dropped: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    entries: list[dict] = field(default_factory=list)
    json_text: str = ""
    readme_text: str | None = None
    svg_text: str = ""


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def load_entries(root: Path, errors: list[str]) -> list[dict] | None:
    raw = read_text(root / DATA_FILE)
    if raw is None:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        errors.append(f"{DATA_FILE} is not valid JSON: {exc}")
        return None
    if not isinstance(data, list) or not all(isinstance(e, dict) for e in data):
        errors.append(f"{DATA_FILE} must be a JSON array of objects")
        return None
    return data


def validate(entries: list[dict], errors: list[str]) -> None:
    paths = Counter(e.get("path") for e in entries)
    for path, n in sorted(paths.items(), key=lambda kv: str(kv[0])):
        if n > 1:
            errors.append(f"duplicate path in {DATA_FILE}: {path} ({n} entries)")
    problems = Counter((e.get("platform"), e.get("id"), e.get("language")) for e in entries)
    for (platform, pid, language), n in sorted(problems.items(), key=str):
        if n > 1:
            errors.append(f"{n} {language} solutions for {platform} {pid}; keep one per problem per language")
    for e in entries:
        label = e.get("path") or f"{e.get('platform')} {e.get('id')}"
        missing = [k for k in FIELDS if k not in e]
        if missing:
            errors.append(f"{label}: missing field(s) {', '.join(missing)}")
        if e.get("pattern") not in PATTERNS and e.get("pattern") != UNSORTED:
            errors.append(f"{label}: unknown pattern {e.get('pattern')!r} (use one of the fixed list or {UNSORTED!r})")
        if e.get("platform") not in PLATFORM_ORDER:
            errors.append(f"{label}: platform must be one of {', '.join(PLATFORM_ORDER)}")
        if e.get("language") not in LANGUAGES.values():
            errors.append(f"{label}: language must be one of {', '.join(LANGUAGES.values())}")
        for key in ("id", "title", "pattern", "key_idea", "time", "space", "path"):
            if key in e and not isinstance(e[key], str):
                errors.append(f"{label}: {key} must be a string")
        for key in ("slug", "url"):
            if e.get(key) is not None and not isinstance(e[key], str):
                errors.append(f"{label}: {key} must be a string or null")
        difficulty = e.get("difficulty")
        if e.get("platform") == "codeforces":
            if difficulty is not None and (not isinstance(difficulty, int) or isinstance(difficulty, bool)):
                errors.append(f"{label}: Codeforces difficulty must be an integer rating or null")
        elif difficulty is not None and difficulty not in ("Easy", "Medium", "Hard"):
            errors.append(f"{label}: LeetCode difficulty must be Easy, Medium, Hard or null")
        tags = e.get("tags")
        if "tags" in e and (not isinstance(tags, list) or not all(isinstance(t, str) for t in tags)):
            errors.append(f"{label}: tags must be a list of strings")


def check_matches_file(e: dict, f: SolutionFile, errors: list[str]) -> None:
    """The entry must describe the file it points to."""
    if e.get("platform") != f.platform:
        errors.append(f"{f.path}: platform is {e.get('platform')!r}, but the file is a {f.platform} solution")
    if e.get("language") != f.language:
        errors.append(f"{f.path}: language is {e.get('language')!r}, but the file is {f.language}")
    expected = file_problem_id(f.platform, f.path)
    if expected is not None and str(e.get("id")) != expected:
        errors.append(f"{f.path}: id is {e.get('id')!r}, but the file name says {expected!r}")


def make_plan(root: Path, online: bool, log=print) -> Plan:
    plan = Plan()
    entries = load_entries(root, plan.errors)
    if entries is None:
        return plan

    # (b) LeetCode file names
    files = list_solution_files(root)
    renamed: dict[str, str] = {}
    for f in files:
        if f.platform != "leetcode":
            continue
        folder, name = f.path.rsplit("/", 1)
        if folder.rsplit("/", 1)[-1] not in DIFFICULTY_FOLDERS or folder.count("/") != LEETCODE_DIR.count("/") + 1:
            plan.errors.append(f"{f.path}: put LeetCode solutions in {LEETCODE_DIR}/easy, medium or hard")
        target = normalize_leetcode_name(name)
        if target is None:
            plan.errors.append(f"{f.path}: name must start with the problem number, like '0001. Two Sum.java'")
        elif target != name:
            renamed[f.path] = f"{folder}/{target}"
    taken = {f.path for f in files}
    for old, new in sorted(renamed.items()):
        if new in taken and new != old:
            plan.errors.append(f"cannot rename {old} to {new}: that file already exists")
        else:
            plan.renames.append((old, new))
            taken.add(new)
    rename_map = dict(plan.renames)
    on_disk = {rename_map.get(f.path, f.path): f for f in files}
    for f in on_disk.values():
        f.path = rename_map.get(f.path, f.path)
    for e in entries:
        if e.get("path") in rename_map:
            e["path"] = rename_map[e["path"]]

    # (c) entries whose file is gone; a file that only moved keeps its entry
    kept, gone = [], {}
    for e in entries:
        if e.get("path") in on_disk:
            kept.append(e)
        else:
            gone.setdefault((e.get("platform"), str(e.get("id")), e.get("language")), []).append(e)
    indexed = {e.get("path") for e in kept}
    unindexed = []
    for path in sorted(set(on_disk) - indexed):
        f = on_disk[path]
        candidates = gone.get((f.platform, file_problem_id(f.platform, path), f.language))
        if candidates:
            e = candidates.pop(0)
            plan.moved.append((str(e.get("path")), path))
            e["path"] = path
            kept.append(e)
        else:
            unindexed.append(path)
    plan.dropped = sorted(str(e.get("path")) for group in gone.values() for e in group)

    # (a) files with no entry
    for path in unindexed:
        f = on_disk[path]
        if f.platform == "codeforces" and parse_codeforces_name(path.rsplit("/", 1)[-1]) is None:
            plan.errors.append(f"{path}: name must be the problem code, like '4A.cpp'")
            continue
        entry = new_entry(f, online, log)
        if entry is not None:
            kept.append(entry)
            plan.added.append(path)

    validate(kept, plan.errors)
    for e in kept:
        check_matches_file(e, on_disk[e["path"]], plan.errors)
    plan.entries = sorted((ordered(e) for e in kept), key=sort_key)
    plan.json_text = dump_json(plan.entries)

    # (d) README and stats card
    readme = read_text(root / README_FILE)
    if readme is None:
        plan.errors.append(f"{README_FILE} not found")
    else:
        try:
            plan.readme_text = render_readme(readme, plan.entries)
        except ValueError as exc:
            plan.errors.append(str(exc))
    plan.svg_text = render_svg(plan.entries)
    return plan


# --------------------------------------------------------------------------- commands


def write(root: Path, online: bool) -> int:
    plan = make_plan(root, online)
    if plan.errors:
        for err in plan.errors:
            print(f"error: {err}", file=sys.stderr)
        return 1
    for old, new in plan.renames:
        os.rename(root / old, root / new)
        print(f"renamed {old} -> {new}")
    for old, new in plan.moved:
        print(f"moved entry {old} -> {new}")
    for path in plan.added:
        print(f"added {path}")
    for path in plan.dropped:
        print(f"dropped {path}")
    outputs = [(DATA_FILE, plan.json_text), (README_FILE, plan.readme_text), (SVG_FILE, plan.svg_text)]
    for rel, text in outputs:
        target = root / rel
        if read_text(target) != text:
            target.parent.mkdir(parents=True, exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            print(f"wrote {rel}")
    return 0


def check(root: Path) -> int:
    plan = make_plan(root, online=False, log=lambda _msg: None)
    problems = list(plan.errors)
    for old, new in plan.renames:
        problems.append(f"{old} should be named {new}")
    for old, new in plan.moved:
        problems.append(f"{DATA_FILE} lists {old}, but the file is now {new}")
    for path in plan.added:
        problems.append(f"{path} has no entry in {DATA_FILE}")
    for path in plan.dropped:
        problems.append(f"{DATA_FILE} lists {path}, which does not exist")
    if not plan.errors:
        changed_files = plan.renames or plan.moved or plan.added or plan.dropped
        if read_text(root / DATA_FILE) != plan.json_text and not changed_files:
            problems.append(f"{DATA_FILE} is not in canonical form (order, indentation or field order)")
        if plan.readme_text is not None and read_text(root / README_FILE) != plan.readme_text:
            problems.append(f"{README_FILE} index is out of date")
        if read_text(root / SVG_FILE) != plan.svg_text:
            problems.append(f"{SVG_FILE} is out of date")
    if problems:
        print("Index check failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        print("Run `python3 scripts/build_index.py --write` and commit the result.", file=sys.stderr)
        return 1
    print(f"Index OK: {len(plan.entries)} solutions.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="update data, file names, README and stats card")
    mode.add_argument("--check", action="store_true", help="exit 1 if --write would change anything")
    parser.add_argument("--offline", action="store_true", help="with --write: do not fetch official fields")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.check:
        return check(root)
    try:
        return write(root, online=not args.offline)
    except FetchError as exc:
        print(f"error: could not fetch official metadata: {exc}", file=sys.stderr)
        print("Nothing was written. Retry, or pass --offline to index without official fields.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
