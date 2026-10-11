# Song Similarity

DEM-W07D01 | Week 7, Monday

Contrast shared-tag counts with normalized Jaccard similarity.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Fictional song metadata only. Tags are sets; missing tags become empty, and empty union scores zero. Ties use ID.

## Code Landmarks

- `shared_count`
- `jaccard`
- `score_songs`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
SONG SIMILARITY: fictional tags, not objective musical truth
Profile: ['calm', 'piano'] ; empty union score=0; unknown tags become empty

ID     Count    Jaccard Matched tags
S01        2      1.000 ['calm', 'piano']
S02        1      0.333 ['calm']
S03        1      0.500 ['piano']
S04        0      0.000 []
S05        2      0.333 ['calm', 'piano']
Count order: ['S01', 'S05', 'S02', 'S03', 'S04']
Jaccard order: ['S01', 'S03', 'S02', 'S05', 'S04']
Normalization distinguishes a focused match from a broad tag collection.
```

## Explore

Why can a broad tag collection rank lower after normalization?

[All daily demos](../../README.md)
