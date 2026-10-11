# 119 Daily Lecture Topic List

Instructor review draft v1 | October 8, 2026

Source: [Proposed Reading Selection and Daily Guide v1](119_Proposed_Reading_Selection_and_Daily_Guide_v1.md).

Alignment update, October 9, 2026: [Textbook Coverage and Reference Map v3](119_Textbook_Coverage_and_Reference_Map_v3.md) maps the current proposed daily scope, including the later demo/assignment promotions for filtering, bounded memoization, and weighted scoring. The v1 rows below remain the earlier baseline; their guided/preview labels have not yet been regenerated to incorporate every promotion.

Purpose: scan and evaluate the proposed daily content scope across the entire eight-week course. This is a topic map, not a lecture outline or assignment specification.

Schedule: Monday is 2 hours combined lecture/lab; Tuesday and Thursday each have 1 hour lecture plus 2 hours lab. Topics below describe the lecture component, with implementation and extended practice continuing in lab. Python is the primary language; familiar syntax is assumed.

Depth key: **Core** = teach and practice; **Guided** = worked example or trace; **Preview** = brief recognition only. These labels describe instructional depth, not reading requirements. Monday has the main reading; Tuesday/Thursday references remain optional.

Session IDs: `D01` Monday, `D02` Tuesday, `D03` Thursday.

## Week 1: Algorithms, Precision, and Correctness

Reading anchor: Chapter 1; optional Chapter 16 support on Thursday.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W01D01 Monday | Defining an Algorithmic Problem | Algorithm characteristics; inputs/outputs; constraints and assumptions; decomposition; precise steps and pseudocode | Core: frame and trace a small practical problem; build on existing Python skills |
| W01D02 Tuesday | Correctness and Failure Diagnosis | Expected outcomes; normal/boundary/invalid cases; test selection; logic defects; tracing a failure | Core: connect tests to rules and assumptions |
| W01D03 Thursday | Revision and Explainability | Changed requirements; behavior-preserving refactoring; regression tests; traceability; limits of a working solution | Core: explain what changed and what evidence supports correctness |

## Week 2: Big-O, Growth, and Measurement

Reading anchor: Chapter 1; optional Chapter 15 scale orientation on Thursday.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W02D01 Monday | Counting Work and Describing Growth | Input size; operation counts; O(1), O(n), O(n^2), O(log n); time/space intuition | Core: practical growth reasoning; Guided: halving trace; no formal proofs |
| W02D02 Tuesday | Measuring Algorithm Behavior | Counts versus timing; comparable inputs; repeated measurements; setup/query separation; misleading benchmarks | Core: interpret a small controlled experiment; benchmarking mechanics use supplied guidance |
| W02D03 Thursday | Choosing for the Workload | Best/worst/average cases; few versus many queries; preprocessing cost; memory tradeoffs; scale-dependent choices | Core: justify an approach for a stated workload; Preview: distributed scale only if useful |

## Week 3: Data Structures and Representation

Reading anchor: Chapter 2; optional Chapter 13 representation tradeoffs on Thursday.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W03D01 Monday | Selecting Lists, Dictionaries, and Sets | Access patterns; lookup/update; identity and duplicates; membership; operation-cost tradeoffs | Core: choose representations by task rather than repeat introductory syntax |
| W03D02 Tuesday | Stacks, Queues, and State | LIFO/FIFO; stack operations; deque-backed queues; state transitions; empty-state behavior | Core: trace and apply one bounded workflow |
| W03D03 Thursday | Consistency and Relationships | Stale entries; consistency across structures; updates/cancellation; hierarchy versus network; representation tradeoffs | Core: consistency reasoning; Preview: trees and graphs; no full tree implementation |

## Week 4: Searching, Sorting, and Preconditions

Reading anchor: Chapter 3; optional Chapter 4 correctness/performance support on Thursday.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W04D01 Monday | Linear and Binary Search | Sequential search; halving the search space; sorted-data precondition; boundaries/absent values; duplicate-key behavior | Core: trace both searches and explain their contracts; implementation practice continues in lab |
| W04D02 Tuesday | Sorting Behavior and Library Use | Insertion-sort steps; comparisons/moves; key-based ordering; stable ordering; library sort versus manual implementation | Core: one simple sort and library comparison; Guided: short merge-sort/divide-and-conquer contrast |
| W04D03 Thursday | Search/Sort Pipeline Tradeoffs | Sort-once/search-many; end-to-end cost; matching sort/search keys; changed workloads; algorithm-selection evidence | Core: evaluate the complete workflow rather than query time alone |

## Week 5: Algorithm Design and Strategy Comparison

Reading anchor: Chapter 4; optional Chapter 1 validation/selection review. A recursion companion may be needed.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W05D01 Monday | Recursion, Iteration, and Decomposition | Base cases; recursive state/call traces; iterative alternatives; problem decomposition; divide-and-conquer connection | Core: one recursive/iterative comparison; Guided: divide-and-conquer connection; verify/supply recursion reading |
| W05D02 Tuesday | Brute Force and Greedy Choices | Exhaustive search; locally best decisions; optimality claims; counterexamples; strategy constraints | Core: investigate one bounded problem; use a supplied exhaustive reference |
| W05D03 Thursday | Repeated Work and Strategy Tradeoffs | Repeated subproblems; memoization; dynamic-programming recognition; correctness/performance/readability; strategy selection | Guided: one repeated-work trace; Preview: broader DP; Core: explain tradeoffs; no full DP unit |

## Week 6: Graphs, Traversal, and Paths

Reading anchor: Chapter 5; optional Chapter 12 relationship/recommendation context if suitable.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W06D01 Monday | Modeling a System as a Graph | Nodes/edges; directed/undirected relationships; adjacency lists; model assumptions; disconnected regions | Core: build and interpret one small model |
| W06D02 Tuesday | BFS and DFS Behavior | Queue/stack frontiers; visited tracking; cycles and termination; traversal order; introductory O(V+E) reasoning | Core: trace both traversals; implementation practice continues in lab |
| W06D03 Thursday | Finding and Explaining Paths | Traversal versus route discovery; parent tracking; path reconstruction; shortest-hop paths; no-path and weighted-cost limits | Core: unweighted BFS path; Guided: weighted-cost counterexample; no weighted-path implementation |

## Week 7: Similarity, Recommendation, and Hashing

Reading anchor: small Chapter 6/12 selections; optional Chapter 14/16 support on Thursday.

| Session | Lecture Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W07D01 Monday | Representation and Similarity | Items/features/tags; similarity versus distance; explainable scores; normalization; empty/missing data | Core: one simple representation and bounded scoring comparison; numeric metrics remain recognition/enrichment |
| W07D02 Tuesday | Ranking and Sensitivity | Top-k ranking; deterministic ties; matched-feature explanations; representation/profile changes; grouping/clustering intuition | Core: ranking and sensitivity; Preview: clustering; no model-training requirement |
| W07D03 Thursday | Algorithmic Limits and Data Integrity | Coverage and bias; assumptions; lookup hashing versus integrity digests; hashing versus encryption; what evidence does and does not establish | Core: bounded critique and library-based integrity check; no cryptographic algorithm design |

## Week 8: Practical Considerations and Final Synthesis

Reading anchor: Chapter 16; Tuesday/Thursday have no new reading or new content lectures.

| Session | Lecture / Assessment Topic | Topic List | Depth / Scope Limit |
| --- | --- | --- | --- |
| W08D01 Monday | Evidence-Based Algorithmic Judgment | Correctness/efficiency/readability; assumptions and limitations; misleading evidence; explainability; final rehearsal | Core synthesis: apply previously taught concepts; no substantial new algorithm |
| W08D02 Tuesday | Final Part 1: Applied Solution Set | Problem framing; representation/implementation; tests; observable evidence; tool-use disclosure | Assessment session: apply taught concepts; no new lecture scope |
| W08D03 Thursday | Final Part 2: Explanation and Adaptation | Solution walkthrough; correctness evidence; edge cases; tradeoffs; response to a changed requirement | Assessment session: verify individual understanding; no new lecture scope |

## Scope Checks for Evaluation

- **Week 4 Tuesday:** Keep insertion sort as the main worked algorithm; merge sort is a brief contrast.
- **Week 5 Monday:** Keep recursion/iteration centered on one problem; avoid a second full divide-and-conquer implementation.
- **Week 5 Thursday:** Memoization/DP remains guided recognition; strategy judgment is the main outcome.
- **Week 7 Tuesday:** Ranking is the main application; clustering receives a short preview.
- **Week 7 Thursday:** Keep hashing to a library demonstration and conceptual distinctions so assumptions/bias still receive attention.
- **Recurring concepts:** Testing, evidence, assumptions, and tradeoffs should deepen across weeks through new contexts rather than repeat the same introductory explanation.

For each row, evaluate whether the topic list supports one coherent lecture and practical demo, whether its depth fits the lecture period, and whether the subsequent lab provides enough application time. Use accepted rows to build the revised IIM and then map demos, existing assignments, and reusable lecture material.

Coverage: 24 meeting slots, comprising 22 teaching sessions and 2 final-assessment sessions. This draft summarizes the new reading guide and makes selected depth limits explicit; it does not replace the IIM or regenerate course content.
