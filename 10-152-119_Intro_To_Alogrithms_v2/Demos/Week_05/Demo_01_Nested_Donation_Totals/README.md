# Nested Donation Totals

DEM-W05D01 | Week 5, Monday

Traverse the same nested donations recursively and with an explicit stack.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

On systems without the Windows Python launcher, use `python main.py` with a Python 3.14 interpreter. Target: Python 3.14.6; verified locally on Python 3.14.7. No third-party packages, network access, web framework, or sibling-demo imports are required. Fixtures are embedded in `main.py`; the program does not write files.

## Contract

Leaves are nonnegative integer units, not floating-point currency; bool and malformed leaves are rejected. Empty groups total zero.

## Code Landmarks

- `recursive_total`
- `iterative_total`

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Expected Default Run

```text
NESTED DONATION TOTALS: nonnegative integer units, not floating-point currency
Input: [10, [5, [2, 3], []], 7]

Recursive calls -> 27
  root: enter group of 3
  root[0]: leaf 10
  root[1]: enter group of 3
  root[1][0]: leaf 5
  root[1][1]: enter group of 2
  root[1][1][0]: leaf 2
  root[1][1][1]: leaf 3
  root[1][1]: return 5
  root[1][2]: enter group of 0
  root[1][2]: return 0
  root[1]: return 10
  root[2]: leaf 7
  root: return 27

Explicit stack -> 27
  root: expand group of 3; pending=['root[2]', 'root[1]', 'root[0]']
  root[0]: add 10; total=10; pending=['root[2]', 'root[1]']
  root[1]: expand group of 3; pending=['root[2]', 'root[1][2]', 'root[1][1]', 'root[1][0]']
  root[1][0]: add 5; total=15; pending=['root[2]', 'root[1][2]', 'root[1][1]']
  root[1][1]: expand group of 2; pending=['root[2]', 'root[1][2]', 'root[1][1][1]', 'root[1][1][0]']
  root[1][1][0]: add 2; total=17; pending=['root[2]', 'root[1][2]', 'root[1][1][1]']
  root[1][1][1]: add 3; total=20; pending=['root[2]', 'root[1][2]']
  root[1][2]: expand group of 0; pending=['root[2]']
  root[2]: add 7; total=27; pending=[]

Both traverse the same nested input; no free pre-flattening step.
Recursion stores pending work in calls; iteration stores it in an explicit stack.
```

## Explore

Which iterative state replaces pending recursive calls?

[All daily demos](../../README.md)
