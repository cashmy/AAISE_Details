# Inventory Representations

DEM-W03D01 | Week 3, Monday

Compare list scans, keyed dictionaries, and set membership.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Duplicate IDs are rejected. Indexed records are independent flat copies; this is not a general nested deep-copy guarantee.

## Code Landmarks

- `build_index`
- `scan_lookup`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
INVENTORY REPRESENTATIONS
List lookup E03: ({'id': 'E03', 'type': 'laptop', 'available': False}, 3)
Dictionary lookup E03: {'id': 'E03', 'type': 'laptop', 'available': False}
Unique equipment types: ['laptop', 'tablet']
Is camera a known type? False

Update in independent index: {'id': 'E01', 'type': 'laptop', 'available': False}
Original list record remains: {'id': 'E01', 'type': 'laptop', 'available': True}
Available records still require a filter: ['E02']
Duplicate policy: duplicate ID: E01
ID lookup, arbitrary filtering, and membership are different contracts.
```

## Explore

Which operations still require filtering after an ID index exists?

[All daily demos](../../README.md)
