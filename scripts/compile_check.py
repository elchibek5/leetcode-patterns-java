#!/usr/bin/env python3
"""Check that every solution compiles.

    python3 scripts/compile_check.py                  # all solutions
    python3 scripts/compile_check.py path/to/file ... # just these
    python3 scripts/compile_check.py --cxx g++-15     # pick the C++ compiler

Java files compile one by one, each in its own temp directory, with the
imports LeetCode adds for you prepended and LeetCode's helper classes
(ListNode, TreeNode, ...) supplied from scripts/java-stubs/ when the code
uses them. C++ files are checked with `g++ -std=c++17 -fsyntax-only`.
Exits 1 if anything fails. Standard library only.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STUBS_DIR = Path(__file__).resolve().parent / "java-stubs"
SOLUTION_DIRS = ("LeetCode_Problems", "Codeforces_Problems")

# Kept on the first line so javac's line numbers match the file.
JAVA_PRELUDE = "import java.util.*; import java.util.function.*; import java.util.stream.*; "

# Helper types LeetCode provides. A stub is copied in only when the solution
# uses the name and does not declare it itself.
STUBS = {
    "ListNode": "ListNode.java",
    "TreeNode": "TreeNode.java",
    "NestedInteger": "NestedInteger.java",
    "VersionControl": "VersionControl.java",
    "GuessGame": "GuessGame.java",
}

# `Node` means a different class depending on the problem.
NODE_VARIANTS = {
    "116": "Node.next.java",
    "117": "Node.next.java",
    "133": "Node.graph.java",
    "138": "Node.random.java",
    "429": "Node.nary.java",
    "559": "Node.nary.java",
    "589": "Node.nary.java",
    "590": "Node.nary.java",
}

PUBLIC_TOP_LEVEL = re.compile(r"^public\s+(?:(?:final|abstract)\s+)*(?:class|interface|enum|record)\s+(\w+)", re.M)
COMMENTS = re.compile(r"//[^\n]*|/\*.*?\*/", re.S)
TIMEOUT = 180  # seconds per file


@dataclass
class Result:
    path: str
    ok: bool
    output: str = ""


def strip_comments(source: str) -> str:
    return COMMENTS.sub(" ", source)


def declares(code: str, name: str) -> bool:
    return re.search(rf"\b(?:class|interface|enum|record)\s+{name}\b", code) is not None


def uses(code: str, name: str) -> bool:
    return re.search(rf"\b{name}\b", code) is not None


def problem_id(path: Path) -> str | None:
    m = re.match(r"(\d+)", path.name)
    return str(int(m.group(1))) if m else None


def stubs_for(path: Path, source: str) -> dict[str, Path]:
    """Map of file name to write in the build dir -> stub file to copy."""
    code = strip_comments(source)
    needed = {}
    for name, stub in STUBS.items():
        if uses(code, name) and not declares(code, name):
            needed[f"{name}.java"] = STUBS_DIR / stub
    if uses(code, "Node") and not declares(code, "Node"):
        variant = NODE_VARIANTS.get(problem_id(path) or "")
        if variant:
            needed["Node.java"] = STUBS_DIR / variant
    return needed


def check_java(path: Path, javac: str, release: str | None) -> Result:
    rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
    source = path.read_text(encoding="utf-8")
    m = PUBLIC_TOP_LEVEL.search(strip_comments(source))
    main_name = f"{m.group(1)}.java" if m else "Solution.java"
    with tempfile.TemporaryDirectory(prefix="compile-check-") as tmp:
        build = Path(tmp)
        (build / "out").mkdir()
        (build / main_name).write_text(JAVA_PRELUDE + source, encoding="utf-8")
        sources = [main_name]
        for target, stub in stubs_for(path, source).items():
            if target == main_name:
                continue
            shutil.copyfile(stub, build / target)
            sources.append(target)
        cmd = [javac, "-J-XX:TieredStopAtLevel=1", "-encoding", "UTF-8", "-proc:none", "-nowarn", "-Xlint:none",
               "-d", "out"]
        if release:
            cmd += ["--release", release]
        try:
            proc = subprocess.run(cmd + sources, cwd=build, capture_output=True, text=True, timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            return Result(rel, False, f"javac timed out after {TIMEOUT}s")
        output = (proc.stdout + proc.stderr).replace(str(build) + os.sep, "")
        if proc.returncode != 0 and main_name != path.name:
            output = output.replace(main_name, path.name)
        return Result(rel, proc.returncode == 0, output.strip())


def check_cpp(path: Path, cxx: str) -> Result:
    rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
    try:
        proc = subprocess.run([cxx, "-std=c++17", "-fsyntax-only", str(path)],
                              capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return Result(rel, False, f"{cxx} timed out after {TIMEOUT}s")
    return Result(rel, proc.returncode == 0, (proc.stdout + proc.stderr).strip())


def find_solutions() -> list[Path]:
    found = []
    for top in SOLUTION_DIRS:
        base = REPO_ROOT / top
        if base.is_dir():
            found += [p for p in base.rglob("*") if p.is_file() and p.suffix in (".java", ".cpp")]
    return sorted(found)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", type=Path, help="solution files to check (default: all)")
    parser.add_argument("--cxx", default="g++", help="C++ compiler (default: g++)")
    parser.add_argument("--javac", default="javac", help="Java compiler (default: javac)")
    parser.add_argument("--java-release", default="21",
                        help="compile against this Java release, as LeetCode does (default: 21; '' to skip)")
    parser.add_argument("-j", "--jobs", type=int, default=os.cpu_count() or 2, help="parallel compiler processes")
    args = parser.parse_args(argv)

    files = [p.resolve() for p in args.files] if args.files else find_solutions()
    java = [p for p in files if p.suffix == ".java"]
    cpp = [p for p in files if p.suffix == ".cpp"]
    for tool, needed in ((args.javac, java), (args.cxx, cpp)):
        if needed and shutil.which(tool) is None:
            print(f"error: {tool} not found on PATH", file=sys.stderr)
            return 2

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        java_results = list(pool.map(lambda p: check_java(p, args.javac, args.java_release or None), java))
        cpp_results = list(pool.map(lambda p: check_cpp(p, args.cxx), cpp))

    failures = [r for r in java_results + cpp_results if not r.ok]
    for r in failures:
        print(f"FAIL {r.path}\n{r.output}\n")
    java_ok = sum(r.ok for r in java_results)
    cpp_ok = sum(r.ok for r in cpp_results)
    print(f"Java: {java_ok}/{len(java_results)} compiled")
    print(f"C++:  {cpp_ok}/{len(cpp_results)} compiled ({args.cxx})")
    if failures:
        print(f"{len(failures)} solution(s) failed to compile.")
        return 1
    print("All solutions compile.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
