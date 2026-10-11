# Benchmark Controls

DEM-W02D02 | Week 2, Tuesday

Compare equivalent workloads with clearly separated setup and query timings.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

Optional: `py -3.14 main.py --size 20` (size range 1-20000; default 2000).

## Python Connection: Command-Line Input

This demo is the proposed first introduction to Python's standard-library `argparse`. The existing small parser block accepts one `--size` argument, converts it to an integer, and supplies 2000 when omitted. `args.size` feeds data generation; it does not change the lookup rules. An explicit range check limits work to 1-20000 records.

```powershell
py -3.14 main.py --help
py -3.14 main.py --size 20
py -3.14 main.py --size 0
```

The final command intentionally demonstrates a rejected value. Parser setup and data generation are outside the timed algorithm regions.

## Contract

Timings use five repetitions and a median. Results, not exact times or speed ratios, are reproducible.

## Code Landmarks

- `scan`
- `build_index`
- `query_index`
- `indexed_end_to_end`
- `measure`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

Timing placeholders below deliberately replace machine-dependent measurements. In the workload demo, the measured winner can also vary.

```text
BENCHMARK CONTROLS: unique IDs, identical hit/miss queries
Misleading comparison: scan queries vs prebuilt-index queries, labeled as total.
The index-only number omits construction. It is not an end-to-end result.

Median of 5 runs; data generation and printing are outside measurements.
scan queries (no setup needed)        <varies> ms
index construction only               <varies> ms
queries on an existing index          <varies> ms
fresh index + all queries             <varies> ms
Timings vary; independently measured medians need not add exactly.
```

## Explore

Which measured region belongs in a claim about total cost?

[All daily demos](../../README.md)
