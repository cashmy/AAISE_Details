# BFS and DFS Frontiers

DEM-W06D02 | Week 6, Tuesday

Trace queue-based BFS and stack-based DFS with discovery tracking.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Discovery is marked when adding to the frontier. Fixed neighbor order gives deterministic traces; undirected edges have two adjacency entries.

## Code Landmarks

- `traverse`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
BFS AND DFS FRONTIERS: mark discovered when adding to frontier

BFS: (processed node | remaining frontier | discovered)
Library  | ['Atrium', 'Lab']         | ['Atrium', 'Lab', 'Library']
Atrium   | ['Lab', 'Cafe']           | ['Atrium', 'Cafe', 'Lab', 'Library']
Lab      | ['Cafe', 'Studio']        | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Cafe     | ['Studio']                | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Studio   | []                        | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Visit order: ['Library', 'Atrium', 'Lab', 'Cafe', 'Studio'] ; adjacency entries examined: 10

DFS: (processed node | remaining frontier | discovered)
Library  | ['Lab', 'Atrium']         | ['Atrium', 'Lab', 'Library']
Atrium   | ['Lab', 'Cafe']           | ['Atrium', 'Cafe', 'Lab', 'Library']
Cafe     | ['Lab', 'Studio']         | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Studio   | ['Lab']                   | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Lab      | []                        | ['Atrium', 'Cafe', 'Lab', 'Library', 'Studio']
Visit order: ['Library', 'Atrium', 'Cafe', 'Studio', 'Lab'] ; adjacency entries examined: 10

Neighbor order is fixed. DFS pushes neighbors in reverse for readable order.
Undirected edges appear twice in adjacency data. Work is O(V+E).
Visit order is not necessarily a route between consecutive entries.
```

## Explore

Why is traversal order not necessarily a connected route?

[All daily demos](../../README.md)
