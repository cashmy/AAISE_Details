# Introduction to Algorithms: Daily Demos

Python demonstrations for SWTC course 10-152-119, Introduction to Algorithms.

## Status and Runtime

Target runtime: **Python 3.14.6**. This folder is being prepared as a standalone student-accessible GitHub repository under [SWTC-AAISE](https://github.com/SWTC-AAISE). No remote repository has been created or uploaded by this preparation step.

All 22 daily demos are implemented as independent console-first Python programs, with embedded fixtures, student READMEs, expected-output traces, and local instructor delivery notes. Weeks 1-7 have three demos each; Week 8 has the Monday synthesis demo.

Python is the primary language. Every Python demo uses only the standard library: no package installation, live service, Django, or MVT is required. Two optional HTML/CSS/JavaScript comparisons accompany combined criteria (Week 1 Thursday) and stable sorting (Week 4 Tuesday). They open directly in a browser and are not dependencies of the Python demos.

## Quick Start

From this repository folder:

```powershell
py -3.14 Week_01/Demo_01_Equipment_Request_Contract/main.py
py -3.14 verify_demos.py
py -3.14 verify_demos.py --week 4
```

Without the Windows Python launcher, substitute `python` using a Python 3.14 interpreter. Each demo can also be run as `py -3.14 main.py` from its own folder. All scripts work from unrelated working directories. Run `py -3.14 test_demo.py` from any demo folder for its separate regression checks and `Checks passed.` banner. Application runs do not execute assertions or display that banner. Do not use Python's `-O` flag for verification; the test scripts reject it.

The Python verification runner includes 58 checks: separate regression-script execution, independent application execution, accepted/rejected CLI variations, and Week 4 callable-key/search-contract continuity. All pass on **Python 3.14.7 and 3.12.10**; the exact requested patch release **3.14.6** was not installed and has not been tested. The seven former W01D01 CLI checks were removed with its parser; threshold, invalid-input, and presentation assertions remain in its separate test script.

Optional JS logic and event-wiring checks use Node.js, not required for the browser examples or Python demos:

```powershell
node --test verify_optional_js.cjs
```

The eight JS checks cover logic/event wiring using a small DOM test double and the separate HTML/CSS/JS file structure; they do not constitute browser rendering or accessibility verification. Benchmark timings and measured winners vary across runs; deterministic operation counts and correctness results are the comparison anchors.

## Organization

```text
Demos/
  README.md
  .gitignore
  Week_01/
    Demo_01_Equipment_Request_Contract/
    Demo_02_Filter_Boundaries/
    Demo_03_Combined_Criteria/
  ...
  Week_08/
    Demo_01_Equipment_Selection_Synthesis/
```

Each demo folder contains:

- `main.py`: the runnable Python demonstration, without regression assertions.
- `test_demo.py`: separate assertions importing the local application's functions; run directly before delivery.
- `README.md`: student-visible purpose, prerequisites, run instructions, and expected behavior.
- Fixtures are embedded in the script; expected default output is in its README. Demos do not write output files.
- Selected folders also contain `optional_js/index.html`, `optional_js/styles.css`, and `optional_js/main.js` for browser comparisons, separating structure, presentation, and behavior.

Each folder also has a local **`notes.md` for instructor delivery**. It contains delivery order, prediction questions, correctness/measurement cautions, stop points, and transfer guidance. The repository's `.gitignore` excludes these files at every nesting level, so ordinary Git staging will not publish them. Student-facing instructions belong in the demo README, not in the excluded notes.

## Demo Index

All folders below contain runnable code and delivery documentation.

| ID | Folder | Focus |
| --- | --- | --- |
| DEM-W01D01 | [Equipment Request Contract](Week_01/Demo_01_Equipment_Request_Contract/README.md) | Problem contracts and modular responsibilities |
| DEM-W01D02 | [Filter Boundaries](Week_01/Demo_02_Filter_Boundaries/README.md) | Predicate filtering, boundary cases, and validation |
| DEM-W01D03 | [Combined Criteria](Week_01/Demo_03_Combined_Criteria/README.md) | Combined filters, refactoring, and regression |
| DEM-W02D01 | [Lookup Growth](Week_02/Demo_01_Lookup_Growth/README.md) | Operation counts and growth |
| DEM-W02D02 | [Benchmark Controls](Week_02/Demo_02_Benchmark_Controls/README.md) | Fair timing and experimental controls |
| DEM-W02D03 | [Workload Tradeoffs](Week_02/Demo_03_Workload_Tradeoffs/README.md) | Construction/query costs and workload decisions |
| DEM-W03D01 | [Inventory Representations](Week_03/Demo_01_Inventory_Representations/README.md) | Lists, dictionaries, and sets |
| DEM-W03D02 | [Checkout Queue and Undo](Week_03/Demo_02_Checkout_Queue_and_Undo/README.md) | FIFO queues, LIFO undo, and state |
| DEM-W03D03 | [State Consistency](Week_03/Demo_03_State_Consistency/README.md) | Stale entries, invariants, and snapshots |
| DEM-W04D01 | [Search Preconditions](Week_04/Demo_01_Search_Preconditions/README.md) | Linear/binary search and matching keys |
| DEM-W04D02 | [Stable Record Sorting](Week_04/Demo_02_Stable_Record_Sorting/README.md) | Insertion sort, record keys, and stable ties |
| DEM-W04D03 | [Query Pipeline](Week_04/Demo_03_Query_Pipeline/README.md) | Filtering, ordering, search, and total cost |
| DEM-W05D01 | [Nested Donation Totals](Week_05/Demo_01_Nested_Donation_Totals/README.md) | Recursion and explicit-stack iteration |
| DEM-W05D02 | [Greedy Counterexample](Week_05/Demo_02_Greedy_Counterexample/README.md) | Greedy choices and a verified counterexample |
| DEM-W05D03 | [Memoization Call Counts](Week_05/Demo_03_Memoization_Call_Counts/README.md) | Repeated work, memoization, and cache state |
| DEM-W06D01 | [Campus Graph Model](Week_06/Demo_01_Campus_Graph_Model/README.md) | Graph representation and model assumptions |
| DEM-W06D02 | [BFS and DFS Frontiers](Week_06/Demo_02_BFS_and_DFS_Frontiers/README.md) | Frontier/visited behavior and termination |
| DEM-W06D03 | [Restricted Routes](Week_06/Demo_03_Restricted_Routes/README.md) | Path reconstruction, restrictions, and hop limits |
| DEM-W07D01 | [Song Similarity](Week_07/Demo_01_Song_Similarity/README.md) | Shared-tag and Jaccard scoring |
| DEM-W07D02 | [Weighted Song Ranking](Week_07/Demo_02_Weighted_Song_Ranking/README.md) | Weights, deterministic ranking, and explanations |
| DEM-W07D03 | [Playlist Integrity and Limits](Week_07/Demo_03_Playlist_Integrity_and_Limits/README.md) | Recommendation limits and local digest evidence |
| DEM-W08D01 | [Equipment Selection Synthesis](Week_08/Demo_01_Equipment_Selection_Synthesis/README.md) | Evidence-based comparison and changed requirements |

Weeks 1-7 have three daily demos each. Week 8 has one synthesis demo; Tuesday and Thursday are assessment meetings rather than additional demos.

### Week 1 User-Facing Demos

All three Week 1 demos offer a useful loan-desk report, a guided teaching walkthrough, or exit. Monday has six steps; Tuesday and Thursday have five. Tuesday emphasizes purposeful boundary tests and repair; Thursday uses named functions for refactor parity and a changed laptop requirement. All separate teaching evidence from ordinary output, include purpose docstrings and readable colors, and retain assertions in test_demo.py. Instructor notes target 12-18 minutes. Later weeks still need individual presentation reviews.

W01D01 also uses ANSI foreground colors for headings, results, and cautions, with white-on-blue Python examples (`0;37;44`) for screen sharing. Redirected output remains plain text; `NO_COLOR` disables colors. Its README links the supplied `console_color_generator.py` and sample PNG as student references. These files are not imported by the application.

### Bounded Python Progression

Introduce `argparse` explicitly in Week 2 Tuesday's Benchmark Controls demo: one `--size` option, integer conversion, a default, generated help, and a safe range check. Reuse it selectively for recurrence size (Week 5 Thursday), route restrictions (Week 6 Thursday), and ranking emphasis (Week 7 Tuesday). These are small supporting Python lessons, not additional algorithm units. The repository-local [demo authoring guidelines](Demo_Authoring_Guidelines.md) define presentation, testing separation, and the proposed progression.

### Week 4 Scaffold

Monday now reveals key selection, equality matching, linear traversal, and ordered binary traversal in stages. Tuesday reuses named callable keys for stable sorting. Thursday composes eligibility and separate display/search views without changing the search signatures or their (position, trace) return contract. Each packet remains independently runnable; no shared module or sibling import is required.

The Week 4 READMEs include updated output, and local instructor notes specify reveal order within the existing 12-18 minute daily budget. The runner adds four checks for callable criteria, contract continuity, and eligibility/view boundaries. Library sort comparator-call counts can vary between Python versions; they are not universal algorithm constants.

## Separate Reference Application

The Learning Resource Navigator is a separate application and milestone archive. It does not live in this repository, and daily demos will not import its code or depend on its data. Additional milestone demonstrations reinforce the week's daily topics.

Its development location is `D:\@Coding_Projects\Python\Leanring_Resource_Navigator`. The full console version is implemented there; the simple version and preserved milestones are not yet built. A public repository link can be added after publication. Daily demos use controlled equipment, donation, recurrence, campus, and song fixtures; the Navigator uses a separate source-reviewed catalog with proposed teaching metadata awaiting instructor approval.

## Publication Checks

Before publishing, verify runnable code and student README instructions, check expected behavior, and confirm no instructor notes are tracked. The default `notes.md` exclusion does not remove a file that was previously committed or deliberately force-added.

Keep instructor delivery notes in their local folders. The standalone repository should retain its own `.gitignore` when copied or initialized for GitHub.
