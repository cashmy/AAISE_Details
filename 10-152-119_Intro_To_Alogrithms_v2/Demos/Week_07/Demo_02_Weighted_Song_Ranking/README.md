# Weighted Song Ranking

DEM-W07D02 | Week 7, Tuesday

Rank songs with normalized weighted similarity and explain contributions.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

Optional: `py -3.14 main.py --emphasis piano` (default: calm).

## Contract

Weights must be finite and nonnegative; unspecified tags weigh 1. A zero-weight union scores zero; ties use ID.

## Code Landmarks

- `weighted_similarity`
- `rank_songs`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
WEIGHTED SONG RANKING: sum matched weights / sum union weights
Unspecified tag weight=1; empty or zero-weight union score=0; ties use ID.

Baseline (all weights 1)
1. S01: score=1.000; matched={'calm': 1, 'piano': 1}; union weight=2
2. S03: score=0.500; matched={'piano': 1}; union weight=2
3. S02: score=0.333; matched={'calm': 1}; union weight=3
4. S04: score=0.000; matched={}; union weight=2

Emphasize calm (weight 4)
1. S01: score=1.000; matched={'calm': 4, 'piano': 1}; union weight=5
2. S02: score=0.667; matched={'calm': 4}; union weight=6
3. S03: score=0.200; matched={'piano': 1}; union weight=5
4. S04: score=0.000; matched={}; union weight=5
A defensible change in weights can change recommendations; no ML training is involved.
```

## Explore

Which score contribution changes when calm or piano receives weight 4?

[All daily demos](../../README.md)
