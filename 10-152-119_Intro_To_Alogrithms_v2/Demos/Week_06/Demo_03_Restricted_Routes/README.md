# Restricted Routes

DEM-W06D03 | Week 6, Thursday

Reconstruct shortest-hop paths and apply blocked-node restrictions.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

Optional: `py -3.14 main.py --blocked Lab Cafe` blocks both routes. `py -3.14 main.py --blocked` applies no blocks. Default: Lab is blocked.

## Contract

BFS minimizes hops on an unweighted graph, not distance. None means unreachable or a blocked endpoint; unknown nodes are invalid.

## Code Landmarks

- `shortest_hop_path`
- `route_distance`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
RESTRICTED ROUTES: BFS minimizes hops, not distance
Baseline route: ['Library', 'Lab', 'Studio'] ; hops: 2 ; distance: 16
Parents: {'Library': None, 'Atrium': 'Library', 'Lab': 'Library', 'Cafe': 'Atrium', 'Studio': 'Lab'}
Blocked nodes: ['Lab'] -> route: ['Library', 'Atrium', 'Cafe', 'Studio']
Restricted hops: 3 ; distance: 3
Unreachable Annex: None
Start equals goal: ['Library']
A 3-hop path can be shorter in distance than this 2-hop path.
```

## Explore

Why can a three-hop route be shorter in distance than a two-hop route?

[All daily demos](../../README.md)
