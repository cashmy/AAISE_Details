# Memoization Call Counts

DEM-W05D03 | Week 5, Thursday

Compare uncached recurrence calls with fresh-cache memoization.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

Optional: `py -3.14 main.py --n 5` (n range 0-20; default 10).

## Contract

F(0)=0 and F(1)=1. Integer n is 0 through 20; every comparison starts with a fresh cache.

## Code Landmarks

- `validate`
- `uncached_fibonacci`
- `cached_fibonacci`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
MEMOIZATION: F(0)=0, F(1)=1; a new cache for every run
F(10)=55; uncached calls=177
Cached result=55; total calls=19; cache hits=8
Computed subproblems/cache entries=11; values={0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
Call counts include cache hits; cache entries count computations, not all calls.
Memoization avoids repeated work in exchange for stored results.
```

## Explore

Which counts include cache hits, and which count newly computed subproblems?

[All daily demos](../../README.md)
