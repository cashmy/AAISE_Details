# Lookup Growth

DEM-W02D01 | Week 2, Monday

Count repeated scan work, index construction, and lookup calls.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Unique synthetic IDs; queries deliberately miss. API-operation counts are not CPU instruction counts.

## Code Landmarks

- `scan_lookup`
- `indexed_lookup`
- `halving_trace`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
LOOKUP GROWTH: controlled synthetic equipment IDs
Every query misses: count each inspected record, index entry, and query.
     n      q   scan inspections   index entries   indexed queries
     4      4                 16               4                 4
     8      8                 64               8                 8
    16     16                256              16                16
    32     32               1024              32                32

Scan work is O(q*n); here q=n, so it grows quadratically.
Index construction is O(n); queries are expected average-case O(q).
An indexed query is an API-operation count, not a CPU instruction count.
Halving contrast: [32, 16, 8, 4, 2, 1] -> logarithmic number of reductions
```

## Explore

What happens to the growth claim if q stays fixed while n doubles?

[All daily demos](../../README.md)
