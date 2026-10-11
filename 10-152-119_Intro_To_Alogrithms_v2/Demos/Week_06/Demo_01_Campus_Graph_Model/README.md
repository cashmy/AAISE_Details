# Campus Graph Model

DEM-W06D01 | Week 6, Monday

Validate an adjacency-list model of a fictional campus.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

The graph is undirected with reciprocal adjacency. Edges describe direct walks, not distance, accessibility, or opening hours.

## Code Landmarks

- `validate_graph`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
CAMPUS GRAPH MODEL (fictional map)
Node = building; edge = an allowed direct walk; undirected, no distance weights.
Library  -> ['Atrium', 'Lab']
Atrium   -> ['Library', 'Cafe']
Lab      -> ['Library', 'Studio']
Cafe     -> ['Atrium', 'Studio']
Studio   -> ['Lab', 'Cafe']
Annex    -> []

Cycle: Library -> Atrium -> Cafe -> Studio -> Lab -> Library
Annex is a valid disconnected node, not a missing reference.
Broken model: ['Library: unknown node Gym']
Valid model:  []
This model omits distance, opening hours, accessibility, and travel time.
```

## Explore

How does a disconnected node differ from an unknown neighbor reference?

[All daily demos](../../README.md)
