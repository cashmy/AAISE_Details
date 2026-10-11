# Equipment Selection Synthesis

DEM-W08D01 | Week 8, Monday

Compare correct lookup strategies and adapt eligibility requirements.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Validated records have unique IDs. Raising the battery threshold changes results but not all record-inspection counts.

## Code Landmarks

- `eligible`
- `scan_requests`
- `indexed_requests`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
EQUIPMENT SELECTION SYNTHESIS: validated records with unique IDs

Request: available laptops, battery >= 50; queries=['E01', 'E04', 'E03', 'missing']
Selected results: ['E01', 'E04', None, None]
Equivalent approaches: True
Scan inspections=13; index construction inspections=4; lookup calls=4

Request: available laptops, battery >= 80; queries=['E01', 'E04', 'E03', 'missing']
Selected results: ['E01', None, None, None]
Equivalent approaches: True
Scan inspections=13; index construction inspections=4; lookup calls=4

Rule change: E04 no longer qualifies at 80. E01 must still qualify.
Counts establish observed work, not a universal runtime advantage.
A cached selection index must be rebuilt if its data or eligibility rule changes.
```

## Explore

What must be rebuilt when a cached index incorporates a changed eligibility rule?

[All daily demos](../../README.md)
