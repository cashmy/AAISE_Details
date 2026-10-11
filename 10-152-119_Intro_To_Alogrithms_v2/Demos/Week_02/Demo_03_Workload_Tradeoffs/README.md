# Workload Tradeoffs

DEM-W02D03 | Week 2, Thursday

Choose a representation using query count, hit patterns, and construction cost.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

The few-query case is one early hit; the many-query case mixes hits and misses. Timed winners can vary.

## Code Landmarks

- `scan`
- `indexed`
- `milliseconds`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

Timing placeholders below deliberately replace machine-dependent measurements. In the workload demo, the measured winner can also vary.

```text
WORKLOAD TRADEOFFS: 2,000 synthetic equipment records

one early hit: q=1
  Scan inspections: 1
  Indexed work: 2000 entries + 1 lookup API calls
  Scan median: <varies> ms; fresh-index median: <varies> ms
  Faster in this measured workload: scan (not a universal winner)

many mixed queries: q=300
  Scan inspections: 400100
  Indexed work: 2000 entries + 300 lookup API calls
  Scan median: <varies> ms; fresh-index median: <varies> ms
  Faster in this measured workload: fresh index (not a universal winner)

An index needs additional storage. Reusing it changes the cost model.
Counts describe different operations; do not treat them as equal-duration units.
```

## Explore

When would keeping an index between requests change your recommendation?

[All daily demos](../../README.md)
