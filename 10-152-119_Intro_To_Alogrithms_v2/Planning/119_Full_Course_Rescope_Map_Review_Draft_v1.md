# 119 Introduction to Algorithms: Full Course Rescope Map

Status: Review draft v1, October 8, 2026. This is a proposed design for instructor evaluation. It does not replace existing lectures, demos, assignments, rubrics, or student-facing materials.

## 1. Design Basis and Recommendation

Build the course around three distinct lecture/demo/application sequences each week, culminating in one integrated weekly submission. Assume students can already write Python functions, loops, decisions, and basic collection operations. Use those skills immediately to investigate algorithm correctness, representation, growth, and strategy selection.

The recommended increase in rigor is depth of reasoning and application: multiple approaches to the same problem, explicit tests, observable behavior, changed requirements, and evidence-based explanations. Coding volume alone should not determine difficulty.

Confirmed instructor constraints:

- Monday: 2 hours, combined lecture and lab.
- Tuesday: 1 hour lecture plus 2 hours lab.
- Thursday: 1 hour lecture plus 2 hours lab.
- Python is the primary implementation language; occasional JavaScript connections are appropriate.
- Students have completed Python Foundations and are approximately halfway through Web Foundations, including more detailed JavaScript logic, modularity, async concepts, and basic data structures.
- This document is for evaluation before content refactoring.

Planning assumptions:

- Retain the existing eight-week duration and broad topic progression.
- Use seven integrated weekly assignments and the existing two-part final model.
- Use standard-library Python and a supplied local environment. Plots may be optional; readable tables and traces must always be sufficient.
- Assume basic Python readiness from the prerequisite, but verify it through a short Week 1 diagnostic. JavaScript exposure does not establish readiness for recursion, Big-O, or graph traversal.
- Estimate 1-2 hours of preparation and completion outside class per week in Weeks 1-7. This is a design target to pilot, not an institutional workload determination.

### Contact-Hour Reconciliation

| Item | Hours |
| --- | ---: |
| Monday each week | 2 |
| Tuesday each week | 3 |
| Thursday each week | 3 |
| Weekly total | 8 |
| Eight-week total | 64 |
| Current WIDS framework total | 72: 36 lecture + 36 lab |
| Difference requiring institutional reconciliation | 8 |

The schedule provides three meeting days with a lecture/demo component and lab component. It does not describe six separately scheduled meetings. The proposed Monday split below is instructional planning, not an official contact-hour classification.

An eight-week implementation of the supplied schedule cannot also provide 72 clock hours without another eight hours of recognized instruction. Determine whether the institution uses academic-hour conversions, additional scheduled instruction, another duration, or revised documentation. Do not silently count homework as contact time. The proposal uses the confirmed 64-hour schedule while leaving this administrative question visible.

## 2. Findings Carried Into the Rescope

| Original observation | Assessment from the existing artifacts | Design response |
| --- | --- | --- |
| No pre-designed demos | Reject the literal claim: Labs 1-7 each have runnable demo code and instructor notes. Confirm inadequate coverage for three teaching sessions per week. | Reuse suitable existing demos and specify a distinct demo for every teaching session. |
| Only one lecture per week | Confirm one weekly outline/deck structure rather than a complete Monday/Tuesday/Thursday sequence. A long deck or suggested two-session split does not establish three designed sessions. | Map three sessions with separate outcomes, demo evidence, and lab transfer. |
| Assignments under-scoped | Confirm a scope mismatch against the supplied hours. Several tasks permit a small example, limited testing, or one selected approach. Actual student completion time has not been measured. | Add staged implementations, comparison, failure diagnosis, and a changed-requirement checkpoint. Pilot completion times. |
| Students have stronger prerequisites | Supported by the instructor's cohort description; the framework also assumes Python foundations. | Begin with applied functions and structured records; provide targeted recovery support where the diagnostic shows a gap. |
| Course under-developed overall | Confirm incomplete session-level design and insufficient required depth. The competency framework and broad progression provide a useful foundation. | Develop the delivery and assessment system around that foundation. |

Existing minima illustrate the scope issue: Lab 1 allows a small scenario with five tests; Lab 4 requires a dataset of at least 12 items and four tests; Lab 7 allows one selected AI/data activity with at least six items. Those can be useful introductory exercises, but they do not by themselves define five-plus hours of weekly applied work for this cohort.

## 3. Weekly Delivery and Workload

### Standard Rhythm for Weeks 1-7

| Day | Lecture/demo allocation | Lab allocation | Intended checkpoint |
| --- | --- | --- | --- |
| Monday, 120 minutes | 50 minutes: retrieval or diagnostic, concept framing, worked demo, predictions | 70 minutes: frame the problem, trace behavior, build a baseline, check a peer's assumptions | A: contract, initial tests, trace, baseline attempt |
| Tuesday, 180 minutes | 60 minutes: deepen the concept, demonstrate a second approach or failure mode | 120 minutes: implement, test, instrument, receive targeted feedback | B: working core implementation and comparison evidence |
| Thursday, 180 minutes | 60 minutes: tradeoffs, counterexample or changed requirement, evidence interpretation | 120 minutes: transfer challenge, revision, technical review, explanation, submission | C: complete solution, evidence, revision, explanation |
| Weekly total | 170 minutes | 310 minutes | 480 minutes / 8 hours |

Each demo is normally 12-18 minutes within the lecture allocation, with prediction and interpretation around it. The rest of the lecture period includes worked analysis, questioning, and short practice. Avoid expanding a demonstration into a full student solution.

For a typical two-hour lab, reserve approximately 10 minutes for planning, 70 for implementation/testing, 20 for comparison or changed requirements, 15 for review/explanation, and 5 for saving checkpoint evidence. Adjust after observing student progress.

Monday lab time should establish a usable baseline. Tuesday lab time should produce a tested solution. Thursday lab time should require adaptation and judgment. Open completion time alone is not a sufficient third lab design.

### Submission and Assessment Pattern

One weekly assignment contains three checkpoints; it is not three unrelated homework assignments. Monday and Tuesday checkpoints receive brief formative feedback. Thursday produces the graded package. Set the LMS cutoff after class with a modest completion window consistent with program policy.

The standard package includes:

- A short input/output contract with constraints, assumptions, and expected behavior.
- Organized Python functions or modules and supplied/derived data.
- Executable tests with expected outcomes, including normal, boundary, and failure cases.
- One or two useful evidence artifacts: trace, count table, timing table, diagram, or ranking comparison.
- A concise explanation of the approach, alternatives, limitations, and revision.
- A tool-use statement, including an explicit statement when AI was not used.

Use meaningful test categories, not test-count compliance alone. Large inputs reveal growth; small inputs reveal behavior. Dataset size is an experimental choice, not a proxy for assignment rigor.

Suggested course-grade distribution for evaluation: weekly integrated assignments 60%, short individual reasoning checks 10%, final assessment 30%. Retain the final's proposed 70% Part 1 / 30% Part 2 split. These are proposed course weights; category scoring should continue to use MRS-AL rather than introduce a competing rubric.

## 4. Full Session Map

Session identifiers follow `W01D01` = Week 1 Monday, `D02` = Tuesday, and `D03` = Thursday. Each row names a teaching goal, a demo to prepare, an observable artifact, and the corresponding student application. Demo titles below are specifications; existing candidates are identified in Section 5. New demo code is not delivered by this proposal.

### Week 1: Contracts, Correctness, and Failure Diagnosis

Purpose: move from familiar Python syntax to precise, testable algorithmic behavior.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W01D01 Monday | Inputs/outputs, assumptions, decomposition, contracts; brief Python readiness diagnostic | Charger eligibility decision: ambiguous rules become explicit functions. Show a decision table and one misleading happy-path result. | Frame an equipment-checkout eligibility task. Define the contract, reason through cases, and attempt a baseline Python function. A: contract and trace. |
| W01D02 Tuesday | Boundary cases, validation, expected outcomes, logical errors, simple invariants | Broken booking validator: a plausible function mishandles a boundary or missing field. Predict output, run tests, and repair the rule. | Implement checkout eligibility and explainable denial reasons. Add independent expected-outcome tests and repair supplied defects. B: tested core functions. |
| W01D03 Thursday | Refactoring without changing behavior; changed requirements; explanation of correctness | Change a priority rule in the validator while keeping regression tests. Show which expectations change and which stay valid. | Add an instructor-issued eligibility rule. Revise code and affected tests, preserve previous valid behavior, and explain the revision to a peer. C: submission. |

Integrated assignment 1: **Equipment Checkout Rules and Test Evidence**.

- Required scope: structured records; validation separated from eligibility decisions; explicit reasons for decisions; a rule-change revision.
- Required evidence: at least eight purposeful tests spanning ordinary, boundary, malformed, and conflicting-rule cases; one branch trace; a before/after rule table.
- Supply a small fixture dataset and a starter test harness. Students own the rules and expected outcomes.
- Stretch: configurable rules or a compact generated test matrix.
- AI: manual framing and initial tests first; optional critique after the baseline. The diagnostic and short individual explanation use no generative AI.
- Scope estimate: 4-5 hours of active lab work inside the 310-minute allocation, plus preparation/completion within the 1-2 hour outside-class target.
- Primary alignment: T1, T3, T5; supporting T4 and core abilities.

### Week 2: Growth, Measurement, and Evidence Quality

Purpose: distinguish an algorithmic improvement from a fast-looking timing result.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W02D01 Monday | O(1), O(n), O(n^2), O(log n); operation counts; time/space intuition | Lookup growth comparison: count inspected records and contrast repeated scans with indexed lookup. Include index-construction cost. | Build a repeated membership-check baseline. Predict growth, define the counted operation, and collect counts on small inputs. A: prediction and baseline. |
| W02D02 Tuesday | Controlled benchmarks, repeated runs, noisy measurements, separating setup from queries | A misleading benchmark: setup, printing, or unmatched inputs change the conclusion. Show corrected count and timing tables. | Implement an indexed alternative and benchmark comparable workloads at multiple sizes. Separate construction, query, and end-to-end measurements. B: reproducible experiment. |
| W02D03 Thursday | Workload-dependent tradeoffs, memory costs, best/worst cases, limits of claims | One lookup versus many: compare workloads and explain when preprocessing may pay off. Use a halving trace for logarithmic intuition without requiring binary-search code yet. | Apply a changed workload: few versus many queries. Recommend an approach and explain why measured timing and operation growth need not match exactly. C: submission. |

Integrated assignment 2: **Membership Workload Investigation**.

- Required scope: repeated list-scan baseline and set/dictionary-based alternative; correctness parity; counted work; a controlled timing harness.
- Required evidence: four input sizes, two query workloads, hit/miss cases, repeated timings summarized consistently, and a preprocessing-cost account.
- Suggested input sizes: 100, 1,000, 5,000, 10,000. Bound the quadratic workload through query limits or a smaller subset to keep runs practical.
- Supply data generation and timing scaffolding. Students select cases, implement the approaches, and interpret evidence. Treat hash lookup as expected average-case behavior, not a universal constant-time guarantee.
- Stretch: estimate an empirical crossover and discuss memory overhead.
- AI: optional critique of a student's interpretation after data collection; the student must check each claim against the experiment.
- Scope estimate: approximately 5 hours of active lab work; 1-2 hours outside class.
- Primary alignment: T3, T4, T5; supporting T1, T2.

### Week 3: Representation and State

Purpose: choose structures by operations and behavioral requirements, rather than familiarity.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W03D01 Monday | Lists, dictionaries, sets; identity, duplicates, ordering, lookup/update | Attendance tracking with a list and dictionary: show repeated scans, duplicate records, and explicit key choices. | Model a support-ticket registry with a list baseline, dictionary index, and membership set. A: operation/structure table and baseline. |
| W03D02 Tuesday | Stack/queue behavior; FIFO/LIFO; `collections.deque`; state transitions | Service queue and undo stack: execute the same actions and display pending work, completed work, and rollback behavior. | Add FIFO processing and one bounded undo operation using supplied interfaces. Test empty states, duplicate IDs, and updates. B: stateful workflow. |
| W03D03 Thursday | Representation consistency, failure recovery, introductory trees and relationship diagrams | Conflicting representations: a queue contains an ID removed from the index. Show the inconsistency and a repair strategy. Briefly contrast a hierarchy with a general graph. | Handle cancellation or stale entries, check state consistency, and justify each structure. C: submission and walkthrough. |

Integrated assignment 3: **Ticket Registry, Queue, and Undo Workflow**.

- Required scope: list-based comparison; dictionary keyed by stable ID; membership tracking; deque-backed FIFO queue; stack-backed undo of one defined operation.
- Supply action parsing and a driver. Keep undo semantics bounded so this remains an algorithms task.
- Required evidence: an operation/structure comparison, a state trace, and tests covering empty queue, duplicates, cancellation, updates, and undo consistency.
- Trees are representation/recognition work this week; full tree implementations are enrichment.
- Stretch: multiple-operation undo or comparing FIFO to a supplied priority policy.
- AI: optional alternate-structure critique after students justify their initial choices.
- Scope estimate: approximately 5 hours of active lab work with the driver supplied; 1-2 hours outside class.
- Primary alignment: T2, T3, T4, T5.

### Week 4: Search, Sort, and Preconditions

Purpose: connect correctness conditions and preprocessing to the practical cost of queries.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W04D01 Monday | Linear/binary search, halving, loop boundaries, sorted-data contract | Book-title search: trace both searches and a selected unsorted-data counterexample. | Implement linear and binary search against one defined catalog-key contract. Test absent keys, endpoints, empty inputs, and duplicates. A: search baseline and traces. |
| W04D02 Tuesday | Insertion sort, comparisons/moves, stable ordering, built-in sort | Catalog ordering: animate through printed insertion-sort states; compare key-based built-in sorting and a guided merge-sort trace. | Implement insertion sort and compare it with `sorted()` on equivalent inputs. Test already-sorted, reverse, duplicate-key, and shuffled inputs. B: search/sort package. |
| W04D03 Thursday | One query versus repeated queries; preprocessing; key consistency; implementation versus library use | A fast lookup with the wrong sort key: show an invalid contract, then compare scan versus sort-once/search-many workloads. | Evaluate the full catalog pipeline and revise it for a changed query workload or ordering requirement. C: recommendation and submission. |

Integrated assignment 4: **Catalog Search and Ordering Investigation**.

- Required scope: student implementations of linear search, binary search, and insertion sort; built-in sort comparison; an explicit policy for duplicate keys.
- Required evidence: small hand-checkable traces, regression tests, comparison/move counts, and workload evidence including the sorting cost.
- Use small fixtures for traces and generated larger datasets for comparison. Cap insertion-sort experiment sizes so the lab is not dominated by waiting.
- Guided merge-sort behavior establishes divide-and-conquer vocabulary; an independent merge-sort implementation is a stretch target. Do not infer Python's built-in sorting algorithm from a merge-sort demo.
- Stretch: lower-bound duplicate search or a second sorting implementation.
- AI: optional inspection of a supplied or AI-generated alternative after the student's baseline is tested; identify a precondition or boundary defect.
- Scope estimate: approximately 5 hours of active lab work with benchmark/data scaffolding; 1-2 hours outside class.
- Primary alignment: T3, T4, T5; supporting T1, T2.

### Week 5: Recursion and Strategy Selection

Purpose: reason about strategy fit and recognize counterexamples to attractive shortcuts.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W05D01 Monday | Recursion/base cases, recursive state, iterative alternatives, trees | Nested donation envelopes: show a recursive call trace beside an explicit-stack traversal of nested totals. | Implement recursive and iterative aggregation for a supplied nested expense structure. A: base-case plan and call/state trace. |
| W05D02 Tuesday | Brute force, divide and conquer, greedy choices, optimality claims | Greedy change-making: denominations 1, 3, 4 and target 6 produce a counterexample. Compare the greedy result to a supplied exhaustive reference. | Analyze and adapt a scaffolded greedy/reference comparison on small inputs. State what the algorithm optimizes and when the claim fails. B: strategy evidence. |
| W05D03 Thursday | Repeated subproblems, memoization recognition, cost/readability/space tradeoffs | Repeated work in a small recursive problem: show call counts with and without memoization. Trace supplied code rather than build a full DP unit. | Test new denomination/target cases and recommend strategies under stated constraints. Explain the recursive/iterative aggregation tradeoff and the greedy counterexample. C: submission. |

Integrated assignment 5: **Strategy Comparison Portfolio**.

- Required scope: two student-owned aggregation implementations plus a bounded greedy-versus-reference investigation. Supply the exhaustive solver and its input limits.
- Required evidence: nested-input tests, base-case behavior, recursive/stack trace, a verified greedy counterexample, and a strategy decision table.
- Use nonnegative integer targets and positive integer denominations for the change-making investigation; define unreachable outcomes explicitly.
- Dynamic programming is guided recognition and tracing. A full DP solver, recurrence proof, or suite of strategy implementations is enrichment.
- Stretch: memoized minimum-coin implementation verified against the small exhaustive reference.
- AI: alternative suggestions after initial reasoning; any generated change must pass independent tests.
- Scope estimate: approximately 5 hours of active lab work with the reference solver supplied; 1-2 hours outside class.
- Primary alignment: T1, T3, T4, T5.

### Week 6: Graphs, Traversal, and Model Limits

Purpose: implement graph traversal and distinguish visiting nodes from finding a useful path.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W06D01 Monday | Nodes/edges, directed/undirected relationships, adjacency lists, model assumptions | Campus route map: draw the model and print adjacency data. Introduce a disconnected node and a cycle. | Model a supplied access network or workflow as an adjacency list. Validate node references and directionality. A: graph and contract. |
| W06D02 Tuesday | BFS/DFS, frontier, visited tracking, termination, traversal order | Traversal race: show queue versus stack state on the same graph, including a cycle. | Implement BFS and iterative DFS, record frontier/visited traces, and test disconnected and cyclic inputs. B: tested traversals. |
| W06D03 Thursday | Parent tracking, path reconstruction, shortest-hop versus weighted cost | Shortest in hops versus shortest in distance: BFS selects a path that is not the minimum-weight route. | Add BFS path reconstruction, handle no path and start=goal, then apply a changed edge restriction. Explain the model's limits. C: submission. |

Integrated assignment 6: **Network Traversal and Route Evidence**.

- Required scope: adjacency-list representation; BFS and iterative DFS; BFS parent tracking and path reconstruction; a route restriction revision.
- Required evidence: a hand-checkable graph of approximately 10-15 nodes, frontier/visited traces, correctness tests, and an explanation of why BFS finds a shortest-hop path in an unweighted graph.
- Include cycles, a disconnected region, and multiple possible routes. Specify neighbor order when comparing traversal order; valid DFS orders may differ.
- Teach O(V+E) reasoning for adjacency-list traversal at an introductory level. Avoid unnecessary weighted shortest-path implementation requirements.
- Stretch: use a supplied weighted-path reference to compare results or generate a larger graph.
- AI: optional model or trace critique; students must independently explain visited-state behavior and the reconstructed path.
- Scope estimate: approximately 5 hours of active lab work; 1-2 hours outside class.
- Primary alignment: T2, T3, T4, T5; supporting T1.

### Week 7: Similarity, Ranking, and Integrity

Purpose: build an explainable data/AI bridge and investigate how representation changes results.

| Session | Lecture focus | Prepared demo and visible evidence | Lab application / checkpoint |
| --- | --- | --- | --- |
| W07D01 Monday | Feature/tag representation, similarity scores, normalization, empty-data rules | Music recommendation: compare shared-tag count with Jaccard similarity and display how rankings change. | Represent a supplied resource catalog as tag sets. Define a user profile and two similarity methods with explicit empty-set behavior. A: representation and predictions. |
| W07D02 Tuesday | Ranking, top-k selection, tie handling, missing features, explanation | Same candidates, different ranking: change a profile or representation and show rank movement. Briefly group 2D points by distance to introduce clustering. | Implement deterministic top-k recommendations, explanation of matched features, and tests for ties, missing tags, empty profiles, and self-matches. B: tested ranking package. |
| W07D03 Thursday | Bias/coverage, sensitivity, hashing versus similarity, integrity evidence | Alter one catalog field: show ranking sensitivity and a SHA-256 digest change using a supplied canonical serialization function. | Revise a representation/profile, compare ranking outcomes, and perform a bounded integrity check. Explain what each piece of evidence establishes. C: submission. |

Integrated assignment 7: **Explainable Resource Recommendation and Data Audit**.

- Required scope: one common recommendation task rather than four unrelated selectable assignments; two simple similarity measures; deterministic ranking and explanations; a supplied-library integrity check.
- Supply approximately 30 catalog records and profiles. Use a smaller subset for hand-checkable scores. Students own representation decisions, scoring, ranking, tests, and interpretation.
- Required evidence: score/rank comparison, a changed-profile or changed-representation experiment, an integrity demonstration, and at least two limitations relating to coverage or assumptions.
- Clustering is a guided visual/trace bridge. Numeric distance and cosine similarity are recognition or enrichment; full model training is deferred.
- Distinguish runtime hashing for dictionary/set lookup from a reproducible cryptographic digest of serialized data. A matching digest does not establish data correctness, fairness, provenance, or authorship; hashing is not encryption.
- Stretch: weighted similarity, distance-based ranking, or a small clustering experiment with supplied tools.
- AI: selective critique or code support after the initial representation and scoring attempt, with tests and disclosure.
- Scope estimate: approximately 5 hours of active lab work with fixtures and serialization helper supplied; 1-2 hours outside class.
- Primary alignment: T6, T2, T3, T4, T5.

### Week 8: Synthesis and Two-Part Final

Purpose: assess transfer and individual understanding within the existing six-hour Tuesday/Thursday final window.

This week retains three meeting slots, but Tuesday and Thursday are assessment sessions. Do not require three new content lectures or add an eighth full graded lab.

| Session | Instruction / assessment focus | Prepared demonstration or prompt | Student work / checkpoint |
| --- | --- | --- | --- |
| W08D01 Monday, 120 minutes | 50 minutes of synthesis and demo; 70 minutes of rehearsal | Compare two approaches to a booking/resource problem. Include incorrect assumptions, misleading performance evidence, and an explainable correction. | Practice a small unfamiliar task and a peer explanation using contract, tests, evidence, and tradeoffs. Formative only. |
| W08D02 Tuesday, 180 minutes | Part 1: 15 minutes briefing, 150 minutes applied work, 15 minutes evidence/submission check | Equivalent bounded task variants and supplied fixtures. No solution demo during the assessment. | Submit the applied solution set, tests, evidence, assumptions, and tool-use statement. The usual lecture/lab periods become one assessment block. |
| W08D03 Thursday, 180 minutes | Part 2: 15 minutes briefing, 105 minutes individualized written/interactive defense and controlled adaptation, 45 minutes instructor verification/feedback, 15 minutes closing | Instructor-reviewed questions based on each student's submission; a small changed requirement requiring prediction and justification | Explain submitted work, interpret evidence, diagnose an edge case, and respond to the change. A predicted result or justified code edit may satisfy the adaptation prompt. |

Final scope proposal:

- Task A, approximately 45 minutes: select a representation and implement a bounded lookup/deduplication task with tests.
- Task B, approximately 45 minutes: complete a graph route or search task using familiar interfaces and unfamiliar data; supply surrounding input/output code.
- Task C, approximately 45 minutes: diagnose and repair a ranking/strategy defect, then explain an assumption or performance claim.
- Reserve approximately 15 minutes within the applied work block for cross-task evidence organization and disclosure. The briefing and final submission check remain outside that block.
- Provide equivalent task variants; do not require a full benchmark suite, a user interface, and several new algorithms during the final.
- Allow documented AI use in Part 1 if adopted in the final packet. Part 2 individual reasoning and adaptation should use no generative AI; identify permitted non-generative references in advance.
- Generate 4-8 personalized questions from the Tuesday submission, with instructor review and equivalent difficulty. Follow the existing explanation-defense model.
- Use written or interactive defenses as the cohort-wide default. Individual oral follow-ups should be targeted and short; 45 minutes cannot support full oral defenses for an unrestricted cohort size.
- Have students include a code-location index and evidence summary in Part 1 to reduce review time. Plan instructor question preparation between Tuesday and Thursday; it is work outside the class-contact allocation.
- Assess T1-T6 and appropriate individual core abilities. Do not infer C5 collaboration from an individual final.

## 5. Demo Production and Reuse Map

The seven existing lab demos are candidates to adapt, not substitutes for the full session map. Preserve their useful examples while making session purpose, evidence, and transfer explicit.

| Existing demo package | Proposed reuse | Additional demo work needed for that week |
| --- | --- | --- |
| `Assignments/Lab_01/demo/`: Laptop Charger Decision Algorithm | W01D01 contracts and decisions | Broken validator and regression/rule-change demos |
| `Assignments/Lab_02/demo/`: Lookup Growth Comparison | W02D01 growth and lookup | Misleading benchmark and workload/preprocessing demos |
| `Assignments/Lab_03/demo/`: Attendance Tracking With a List and a Dictionary | W03D01 representation choice | Queue/stack state and consistency-failure demos |
| `Assignments/Lab_04/demo/`: Searching Book Titles on a Shelf | W04D01 search/preconditions | Insertion-sort/library contrast and full query-pipeline demos |
| `Assignments/Lab_05/demo/`: Nested Donation Envelopes | W05D01 recursion/iteration | Greedy counterexample and repeated-subproblem demos |
| `Assignments/Lab_06/demo/`: Campus Route Map Traversal | W06D01 representation and selected W06D02 material | Separate frontier traces and shortest-hop/weighted-cost limitation demos |
| `Assignments/Lab_07/demo/`: Tiny Music Recommendation by Tag Similarity | W07D01 representation/similarity | Ranking sensitivity, clustering preview, and integrity distinction demos |
| Existing Week 8 synthesis/practice artifact | W08D01 final rehearsal | Rework the example to rehearse the expanded evidence expectations |

Production target: **22 teaching-session demo packets**: three in each of Weeks 1-7, plus Monday in Week 8. Tuesday and Thursday in Week 8 need assessment packets instead. A packet may contain two short connected runs; it does not need a large application.

Each prepared demo packet must contain:

1. A runnable Python example with deterministic small fixtures and a clear entry point.
2. A session outcome and one explicit connection to that day's lecture.
3. A run/build sequence sized to approximately 12-18 minutes, with prediction prompts.
4. Expected console output, trace, table, diagram, or chart and a plain-text fallback.
5. A selected counterexample or changed requirement that reveals an assumption.
6. A transfer task that changes the data, rules, or workload for students.
7. A stop point that leaves the central student work unfinished.
8. Instructor notes naming likely misconceptions and checks for understanding.

Validate candidate code before reuse. Existing runnable files establish that demos exist; their suitability for expanded learning goals requires review and execution during the later refactor.

## 6. Prerequisite Use, Python, and JavaScript Connections

Use Python functions, structured records, modules, file/JSON handling, debugging, and tests as available foundations. Supply recovery references for students who need them. Treat classes, packages, frameworks, and sophisticated test tooling as optional unless prerequisite artifacts demonstrate cohort readiness and the assignment benefits from them.

| Session | Optional JS connection | Limit |
| --- | --- | --- |
| W01D03 | Same function contract and boundary-case tests in Python and JS | 5-8 minutes within the existing lecture slot; no parallel JS assignment |
| W03D01 | Python dictionaries/sets beside JS `Map`/`Set`; discuss key/identity differences | 5-8 minutes; avoid asserting identical semantics |
| W04D02 | Comparator contracts and sorting behavior across languages, including JS default sort and mutation | 5-8 minutes; use an already prepared contrast |
| W08D01 | Async improves waiting/concurrency in appropriate workloads; it does not change the underlying asymptotic work of a poor algorithm | Brief conceptual connection only; no new async implementation requirement |

Use these connections to transfer judgment between languages. All required algorithms, tests, evidence, and final work remain in Python. If a JS contrast consumes time, reduce another lecture example rather than add contact hours.

## 7. Coverage Depth and Competency Alignment

### Required Depth

| Topic | Expected student performance |
| --- | --- |
| Framing/correctness | Define contracts, expected outcomes, edge cases, and meaningful tests; revise when requirements change |
| Complexity | Explain common growth classes, count work, interpret controlled timing, and distinguish setup/query costs |
| Data structures | Select and use lists, dictionaries, sets, stack behavior, deque-backed queues, and adjacency lists |
| Search/sort | Implement linear search, binary search, and one simple sort; use library sorting; justify preconditions and workload choices |
| Recursion/iteration | Implement both for one bounded nested-data task and explain state/base cases |
| Strategies | Investigate brute force and greedy; identify a counterexample; trace divide-and-conquer behavior |
| Graphs | Implement BFS/iterative DFS and reconstruct an unweighted BFS path; test cycle/disconnected behavior |
| AI/data bridge | Implement simple similarity/ranking, explain representation sensitivity, and use a library digest for an integrity demonstration |
| Explanation/tool use | Connect claims to evidence, critique limitations, disclose assistance, and defend individual understanding |

### Guided or Recognition Depth

Trees as representations; merge-sort traces; memoization/dynamic programming; clustering; numeric distances/cosine similarity; weighted-path intuition; distinction between hashing and encryption. Guided topics get short prediction or explanation checks, not independent full implementations.

### Deferred Depth

Balanced trees, formal complexity proofs and recurrence solving, full dynamic programming units, Dijkstra/A* implementations, machine-learning training, neural networks, NLP pipelines, distributed algorithms, cryptographic system design, and browser UI development.

More contact time should deepen core work before enlarging the advanced-topic list.

### Assessment Alignment

| Technical competency | Main instruction/practice | Major assessed evidence |
| --- | --- | --- |
| T1 Problem Framing and Algorithmic Analysis | Weeks 1-7; synthesis Week 8 | Contracts, assumptions, strategy plans, changed-requirement responses |
| T2 Data Structures and Representation | Weeks 2-4, 6-7 | Registry/workflow structures, catalog contracts, adjacency model, feature representation |
| T3 Algorithm Implementation and Testing | Weeks 1-7 | Student-owned functions, executable tests, defect repairs, final solutions |
| T4 Correctness, Efficiency, and Tradeoff Evaluation | Weeks 2-7 | Count/timing experiments, search/sort pipeline, counterexample, path/ranking limits |
| T5 Observable Behavior and Communication Evidence | Every week | Trace/table/diagram evidence with explanations tied to claims |
| T6 AI/Data Foundations and Responsible Tool Use | Tool accountability throughout; substantive bridge in Week 7 | Ranking/sensitivity/integrity work, limitation critique, validated tool use |

Cross-course abilities C1-C6 are observed through problem solving, explanations, checkpoint progress, revision, peer review, and professional accountability. Use pair tracing and test review to observe C5 during weekly labs, then require individual explanations to verify ownership. AI use alone does not establish T6 proficiency; the data/AI concepts and validation matter.

## 8. Reading and Preparation Map

The existing textbook coverage map remains the reference for chapter associations. The following is a proposed reading allocation based on that local map; page-level selections still need verification against the actual edition during content development.

| Week | Preparation focus | Reading source in existing local map |
| --- | --- | --- |
| 1 | Algorithms, contracts, assumptions, validation | Selected Chapter 1; brief Chapter 16 excerpt if useful |
| 2 | Growth classes, time/space, measurement | Selected Chapter 1 |
| 3 | Structure operations, stacks/queues, representation | Selected Chapter 2 |
| 4 | Search/sort behavior and preconditions | Selected Chapter 3; targeted Chapter 4 reference |
| 5 | Strategy patterns and recursive reasoning | Guided Chapter 4 |
| 6 | Graph representation and BFS/DFS | Selected Chapter 5 |
| 7 | Similarity/recommendation; hashing distinction | Short guided selections from Chapters 6, 12, and 14 |
| 8 | Evidence, explainability, bias, practical limits | Selected Chapter 16; course evidence review |

Target 30-45 minutes of preparation in Weeks 1-7, leaving roughly 30-75 minutes for completion within the proposed outside-class range. Use small directed excerpts and a prediction prompt. Week 7 especially needs tightly selected excerpts rather than three full chapters. Week 8 adds no substantial new reading obligation beyond final preparation.

## 9. Refactor Deliverables After Evaluation

| Artifact family | Proposed result | Dependency |
| --- | --- | --- |
| Course plan / competency metadata | Confirm schedule and reconcile 64 versus 72 hours; document selected depth | Instructor evaluation and institutional hour classification |
| Session matrix | 24 meeting entries with purpose, time, demo, lab, checkpoint, and evidence | Accepted sequence and scope |
| Lecture outlines / deck sources | 22 teaching outlines/deck sources plus two assessment-session guides | Session matrix |
| Demo library | 22 prepared packets, adapting existing examples where suitable | Session outcomes and assignment boundaries |
| Weekly assignments | Seven integrated packets with A/B/C checkpoints, tests, datasets, core/stretch scope | Weekly scope and demo transfer design |
| Starters and instructor solutions | Small scaffolds; withheld solutions; expected test/evidence outputs | Assignment contracts |
| Rubric alignment | Assignment-specific evidence mappings using MRS-AL; sample scoring calibrations | Completed assignments |
| Final assessment | Three bounded applied tasks, equivalent variants, question-generation guidance, individual defense | Pilot workload and final policy choices |
| LMS / student schedule | Day-level preparation, lab checkpoints, submission requirements, final timing | Stable artifact set |

Build and pilot Weeks 1, 2, and 4 first: they test prerequisite fit, experimental workload, and the densest implementation week. Use those results to calibrate the remaining packets before producing all decks.

Review acceptance criteria:

- Every regular teaching session has a distinct outcome, prepared demo, and transfer task.
- Every weekly assignment uses all three lab blocks for purposeful progression.
- Core work is achievable with the supplied scaffolds inside the planned lab time plus the stated outside-class target.
- Students must test, compare, and adapt their work; a single happy-path result is insufficient.
- Student explanations establish individual understanding even when collaboration or AI is allowed.
- Guided/enrichment topics cannot silently become required implementations.
- Final tasks fit the Tuesday work window, and Thursday defenses can scale to the actual cohort.
- Lecture/lab metadata reconciles with the institution's recognized hours before publication.

## 10. Evaluation Decisions

The instructor's evaluation should focus on these proposed choices:

| Decision | Recommendation in this draft | Consequence |
| --- | --- | --- |
| Overall architecture | Three designed sessions and one staged weekly assignment | More instructional coverage without 21 disconnected graded assignments |
| Academic level | Apply prerequisite Python immediately; verify through a short diagnostic | Less repeated syntax instruction; more testing, comparison, and adaptation |
| Content breadth | Retain the existing eight-week progression; strengthen core depth | Maintain downstream AI/data bridges without requiring advanced implementations |
| Week 3 scope | Scaffold the driver and keep undo to one operation | Representation/state reasoning fits the weekly time budget |
| Week 5 scope | Two aggregation implementations plus scaffolded strategy investigation | Strategy coverage remains concrete and bounded |
| Week 7 scope | Common recommendation task plus a small integrity exercise; clustering guided | Comparable assessed depth and a clearer AI/data bridge |
| Assessment | Seven weekly submissions, short individual checks, two-part final | Frequent feedback and visible ownership |
| Institutional hours | Reconcile the documented 72 hours with the confirmed 64-hour schedule | Accurate planning and metadata before release |

The 64-hour schedule is sufficient to build this proposed course if scaffolding and guided-topic boundaries are honored. Exact assignment times remain estimates until piloted. Evaluation can adjust these choices before any existing instructional content is refactored.

## Source Artifacts Reviewed

- `v2/Introduction_to_Algorithms_High_Level_Course_Plan_v2.md`
- `v2/WIDS_Course_Competency_Framework_v3.md`
- `v2/119_v2_Curated_Artifact_Map.md`
- `v2/Textbook_Coverage_and_Reference_Map_v2.md`
- `Scheduled_Assignment_Overview.md`
- `Lecture_Outlines/README.md` and the weekly lecture/deck organization
- `Assignments/README.md` and `LASO-AL_Lab_Assignment_System_Overview.md`
- `Assignments/Lab_Progression_Ladder_v2.md`
- Existing Lab 1, Lab 4, and Lab 7 scope requirements
- Existing Labs 1-7 demo notes/package inventory
- `Assignments/FINAL-AL_Final_Algorithmic_Reasoning_Assessment.md`

All paths above are relative to `10-152-119_Intro_To_Algorithms`. The instructor's confirmed schedule and cohort description are the controlling inputs for this proposal.
