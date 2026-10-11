# State Consistency

DEM-W03D03 | Week 3, Thursday

Expose stale references and distinguish shallow aliases from independent snapshots.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Repair removes pending IDs missing from inventory. Deep copies are independent, not immutable.

## Code Landmarks

- `stale_ids`
- `repair_queue`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
STATE CONSISTENCY AND SNAPSHOTS
Invariant: every pending equipment ID exists in inventory.
After removal, stale IDs: ['E02']
Repair policy: remove stale requests: ['E02'] -> pending ['E01']

Current record:  {'id': 'E01', 'available': False}
Shallow list:    {'id': 'E01', 'available': False} (same mutable record)
Deep snapshot:   {'id': 'E01', 'available': True} (independent, but still mutable)
Hierarchy: nested ownership; network: general relationships (preview only).
```

## Explore

Why does copying the outer list not preserve the previous record values?

[All daily demos](../../README.md)
