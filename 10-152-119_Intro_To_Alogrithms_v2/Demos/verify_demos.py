"""Run behavioral checks and independent console smoke tests for every daily demo."""

import argparse
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


def load_demo(path):
    name = "demo_" + path.parent.parent.name + "_" + path.parent.name
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def behavioral_check(path):
    console_check(path.with_name("test_demo.py"), expected_text="Checks passed.")


def search_contract_check(path):
    demo = load_demo(path)
    rows = [{"id": 4, "model": "Laptop"}, {"id": 1, "model": "Camera"},
            {"id": 7, "model": "Tablet"}, {"id": 2, "model": "Laptop"}]
    original_ids = [row["id"] for row in rows]
    for key, targets in ((demo.id_key, (1, 2, 4, 7, 0, 9)),
                         (lambda row: row["model"], ("Camera", "Laptop", "Tablet", "Missing"))):
        view = sorted(rows, key=key)
        for search in (demo.linear_search, demo.binary_search):
            for target in targets:
                calls = []

                def counted_key(record):
                    calls.append(record["id"])
                    return key(record)

                position, trace = search(view, target, key=counted_key)
                assert len(calls) == len(trace)
                assert (position is None) == (not any(key(row) == target for row in view))
                if position is not None:
                    assert key(view[position]) == target
                assert all(len(step) == (2 if search is demo.linear_search else 4) for step in trace)
            assert search([], targets[0], key=key) == (None, [])
    assert [row["id"] for row in rows] == original_ids
    assert demo.matches("Laptop", "Laptop") and not demo.matches("Laptop", "Camera")
    assert [demo.compare_values(value, 2) for value in (1, 2, 3)] == [-1, 0, 1]


def week4_continuity_check(paths):
    monday, tuesday, thursday = [load_demo(path) for path in paths]
    rows = [{"id": 4, "battery": 70}, {"id": 1, "battery": 50},
            {"id": 7, "battery": 70}, {"id": 2, "battery": 30}]
    for key, targets in ((monday.id_key, (1, 2, 4, 7, 99)),
                         (tuesday.battery_key, (30, 50, 70, 99))):
        ordered, _, _, _ = tuesday.insertion_sort(rows, key)
        assert ordered == sorted(rows, key=key)
        for target in targets:
            assert monday.linear_search(ordered, target, key) == thursday.linear_search(ordered, target, key)
            assert monday.binary_search(ordered, target, key) == thursday.binary_search(ordered, target, key)
    assert [row["id"] for row in tuesday.insertion_sort(rows, tuesday.battery_key)[0]] == [2, 1, 4, 7]


def pipeline_contract_check(path):
    demo = load_demo(path)
    rows = [{"id": 3, "battery": 80, "available": True},
            {"id": 1, "battery": 80, "available": False},
            {"id": 2, "battery": 79, "available": True}]
    selected = demo.filter_available(rows, 80)
    assert selected == rows[:1]
    view, _ = demo.order_for_search(selected, demo.id_key)
    assert demo.linear_search(selected, 3)[0] == demo.binary_search(view, 3)[0] == 0
    assert demo.binary_search(view, 1)[0] is None
    assert demo.filter_available(rows, 81) == []
    assert demo.order_for_search([], demo.id_key) == ([], 0)
    key_calls = []

    def counted_key(record):
        key_calls.append(record["id"])
        return record["id"]

    ordered, comparisons = demo.order_for_search(rows, counted_key)
    assert [row["id"] for row in ordered] == [1, 2, 3]
    assert len(key_calls) == 2 * comparisons


def console_check(path, arguments=(), expected_text=None, expected_code=0):
    """Check independent console execution, selecting the report for the menu demo."""
    loan_desk = path.parent.parent.name == "Week_01" and path.name == "main.py"
    # A different working directory detects accidental dependencies on the launch location.
    with tempfile.TemporaryDirectory() as working_directory:
        result = subprocess.run([sys.executable, str(path), *arguments], cwd=working_directory,
                                input="1\n0\n" if loan_desk else None,
                                capture_output=True, text=True, timeout=30)
    if result.returncode != expected_code:
        raise AssertionError(result.stdout + result.stderr)
    if expected_code:
        if "error:" not in result.stderr:
            raise AssertionError("invalid input did not produce an argparse error")
        return
    if path.name == "test_demo.py":
        if not result.stdout.rstrip().endswith("Checks passed."):
            raise AssertionError("regression checks did not complete: " + result.stdout)
    else:
        if not result.stdout.strip():
            raise AssertionError("demo produced no output")
        if "Checks passed." in result.stdout:
            raise AssertionError("regression banner leaked into application output")
    if loan_desk:
        if "Equipment Loan Desk" not in result.stdout or "Result:" not in result.stdout:
            raise AssertionError("loan-desk report is incomplete: " + result.stdout)
        for technical_text in ("invalid:", "Selected IDs:", "Teaching trace"):
            assert technical_text not in result.stdout, technical_text
    if result.stderr:
        raise AssertionError("unexpected stderr: " + result.stderr)
    if expected_text and expected_text not in result.stdout:
        raise AssertionError("missing expected evidence: " + expected_text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--week", type=int, choices=range(1, 9))
    args = parser.parse_args()
    folders = sorted(ROOT.glob("Week_*/Demo_*"))
    if args.week:
        folders = [folder for folder in folders if folder.parent.name == f"Week_{args.week:02}"]
    expected = 1 if args.week == 8 else 3 if args.week else 22
    if len(folders) != expected or any(not (folder / name).is_file()
                                      for folder in folders for name in ("main.py", "test_demo.py")):
        parser.error(f"expected {expected} complete demo folders")
    suite = unittest.TestSuite()
    for folder in folders:
        path = folder / "main.py"
        for label, check in (("behavior", behavioral_check), ("console", console_check)):
            suite.addTest(unittest.FunctionTestCase(
                lambda path=path, check=check: check(path),
                description=f"{folder.parent.name}/{folder.name}: {label}"))
    if args.week in (None, 4):
        week4 = sorted(ROOT.glob("Week_04/Demo_*/main.py"))
        for path in (week4[0], week4[2]):
            suite.addTest(unittest.FunctionTestCase(
                lambda path=path: search_contract_check(path),
                description=f"{path.parent.name}: callable-key search contract"))
        suite.addTest(unittest.FunctionTestCase(
            lambda: week4_continuity_check(week4), description="Week_04: Monday-to-Thursday contract continuity"))
        suite.addTest(unittest.FunctionTestCase(
            lambda: pipeline_contract_check(week4[2]), description="Week_04: eligibility boundaries and view contract"))
    variants = {
        "Demo_02_Benchmark_Controls": [(("--size", "20"), "BENCHMARK CONTROLS", 0),
                                      (("--size", "0"), None, 2)],
        "Demo_03_Memoization_Call_Counts": [(("--n", "0"), "F(0)=0", 0),
                                           (("--n", "20"), "F(20)=6765", 0),
                                           (("--n", "21"), None, 2)],
        "Demo_03_Restricted_Routes": [(("--blocked", "Lab", "Cafe"), "-> route: None", 0),
                                      (("--blocked",), "Blocked nodes: []", 0),
                                      (("--blocked", "Gym"), None, 2)],
        "Demo_02_Weighted_Song_Ranking": [(("--emphasis", "piano"), "Emphasize piano", 0),
                                         (("--emphasis", "rock"), None, 2)],
    }
    for folder in folders:
        for arguments, evidence, code in variants.get(folder.name, []):
            path = folder / "main.py"
            suite.addTest(unittest.FunctionTestCase(
                lambda path=path, arguments=arguments, evidence=evidence, code=code:
                    console_check(path, arguments, evidence, code),
                description=f"{folder.parent.name}/{folder.name}: {' '.join(arguments)}"))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
