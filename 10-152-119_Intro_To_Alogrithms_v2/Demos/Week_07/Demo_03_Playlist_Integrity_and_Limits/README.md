# Playlist Integrity and Limits

DEM-W07D03 | Week 7, Thursday

Separate metadata integrity evidence from recommendation quality.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

SHA-256 hashes canonical JSON metadata, not audio. Record/tag order is normalized. A digest does not establish authenticity or fairness.

## Code Landmarks

- `canonical_bytes`
- `digest`
- `rank`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
PLAYLIST INTEGRITY AND RECOMMENDATION LIMITS
Baseline ranking: [('S01', 1.0), ('S02', 0.3333333333333333)]
Missing S01 tags changes ranking: [('S02', 0.3333333333333333), ('S01', 0.0)]
The music did not change; the authored metadata did.

Canonical fields: ID, title, unique sorted tags; record order ignored.
Original SHA-256: de39dbcc9fa4dd2ca5761048751667ec9e17870aa6b5b3574cd021c4a0ea3d7f
Edited SHA-256:   1ce45f58e7c4cd3755473e3a977395d6211114e71da4dab40fa541f7c919dd8a
Title-only edit leaves tag ranking unchanged: [('S01', 1.0), ('S02', 0.3333333333333333)]
A digest checks this serialized snapshot, not authenticity, fairness, or source correctness.
Hashing metadata is not hashing audio, computing similarity, or encrypting data.
```

## Explore

Why does a title edit change the digest without changing tag-based ranking?

[All daily demos](../../README.md)
