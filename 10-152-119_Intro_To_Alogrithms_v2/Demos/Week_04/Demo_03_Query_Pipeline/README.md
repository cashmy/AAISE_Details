# Query Pipeline

DEM-W04D03 | Week 4, Thursday | Refactored October 9, 2026

Compose eligibility, ordering, and Monday's familiar search contracts. Reuse functions rather than rebuild algorithms during integration.

## Run

From this demo folder:

```powershell
py -3.14 main.py
```

Without the Windows launcher, use python main.py with the intended interpreter. Target Python 3.14.6; verified on installed Python 3.14.7 and 3.12.10, not exact 3.14.6. Standard library only; no packages, network, framework, sibling-demo imports, or generated files.

`main()` presents the demonstration. Run `py -3.14 test_demo.py` separately for regression checks; a successful test run ends with `Checks passed.` Do not use Python's `-O` flag for verification.

## Modular Responsibilities

| Function | Responsibility |
| --- | --- |
| is_eligible(record, minimum_battery) | Arbitrary eligibility rule: availability and inclusive battery threshold |
| filter_available(records, minimum_battery) | Apply that predicate to produce a selected snapshot |
| id_key(record), battery_key(record) | Select values for ordering/comparison |
| matches(value, target), compare_values(value, target) | Equality and ordered comparison, as in Monday's demo |
| linear_search / binary_search | Same callable-key arguments and (position, trace) result contract as Monday |
| order_for_search(records, key=id_key) | Supplied library ordering with comparator-call instrumentation |

Filtering is not ID lookup. Its predicate can combine rules; binary search requires an ordered key, not that predicate.

Display and search lists are separate shallow views of the same selected records. Positions must be resolved against the specific list passed to the search. None means absent; position 0 is valid. Filtering/reordering does not mutate the original list, but these are not independent deep copies of the records.

Both workflows share one filter pass. The ID sort is done once and reused across queries; query totals exclude its construction work, which is reported separately. Record visits, comparator calls, and midpoint visits are different counted units, not equal-duration operations. Traces also allocate memory. No elapsed-time superiority or crossover is claimed.

A changed battery threshold rebuilds selection and its search view; the key, equality, and search algorithms stay unchanged. The intentionally battery-ordered ID search violates its precondition.

The default output below was captured on Python 3.14.7. Library sort comparator-call counts are implementation-dependent: this fixture reports six on 3.14.7 and four on 3.12.10. Ordering/results and counted search visits agree; do not require the same library sort count across runtimes.

## Expected Default Run

```text
QUERY PIPELINE: eligibility predicate -> views -> familiar search -> report
Reused search contract: (position in supplied view, trace); callable key
Eligible IDs: [3, 1, 2]
Battery-ordered display IDs: [3, 1, 2]
ID-ordered search view:      [1, 2, 3]
Invalid ID binary search in display, target 3: None
Same ID 3: linear position=0; binary position=2
Resolve positions against their own views: True
Correct search view, target 3: {'id': 3, 'battery': 20, 'available': True}
q=1: scan inspections=1; sort comparisons=6; binary midpoint inspections=2
q=12: scan inspections=24; sort comparisons=6; binary midpoint inspections=24
Filter scans 4 input records once; both workflows share that cost.
Counts describe visits/comparator calls, not equal-duration units or total timings.
Library sort comparator-call counts can differ between Python versions.
Traces allocate memory for teaching; both workflows reuse one filtered snapshot.
Changed battery threshold >=80: [1, 2]
ID 3 after the filter change: None
Filtering changes eligibility; it does not change the equality or search contract.
```

## Explore

Why are the linear/binary positions different for the same equipment? Which functions change for a new eligibility rule? What must change if the search key changes instead?

Each demo remains standalone. The additional Navigator APP-M4 recognition is separate from this daily demo.

[All daily demos](../../README.md)
