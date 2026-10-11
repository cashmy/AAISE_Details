# Checkout Queue and Undo

DEM-W03D02 | Week 3, Tuesday

Process checkout requests FIFO and reverse successful checkouts LIFO.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Undo restores availability and places the consumed request at the queue front. Only successful checkout actions are reversible.

## Code Landmarks

- `make_state`
- `enqueue`
- `checkout_next`
- `undo_checkout`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
CHECKOUT QUEUE AND UNDO: only checkout is reversible

Initial requests
  Availability: {'E01': True, 'E02': True}
  Pending FIFO: ['E01', 'E02']
  Undo LIFO:    []

E01: checked out
  Availability: {'E01': False, 'E02': True}
  Pending FIFO: ['E02']
  Undo LIFO:    [('E01', True)]

E02: checked out
  Availability: {'E01': False, 'E02': False}
  Pending FIFO: []
  Undo LIFO:    [('E01', True), ('E02', True)]

E02: checkout undone; request restored at front
  Availability: {'E01': False, 'E02': True}
  Pending FIFO: ['E02']
  Undo LIFO:    [('E01', True)]

The most recent checkout is undone first; FIFO request order is restored.
```

## Explore

What prior state must undo save, and what does it restore?

[All daily demos](../../README.md)
