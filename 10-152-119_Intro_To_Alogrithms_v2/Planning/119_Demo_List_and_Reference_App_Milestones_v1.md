# 119 Demo List and Reference App Milestones

Instructor review draft v1, revised demo structure | October 8, 2026

## Design Basis

Provide at least one prepared practical demo for every teaching session: three per week in Weeks 1-7 and one synthesis demo on Monday of Week 8. Tuesday/Thursday of Week 8 remain individual assessment sessions. This list specifies 22 daily topic-demo packets plus 9 separate reference-app demonstration packets, not finished code.

Use two distinct demonstration layers:

- **Daily topic demos:** small practical examples in separate contexts, prepared to teach that day's concepts. They do not use Navigator code, resource records, or milestone snapshots.
- **Additional Navigator demos:** separately identified demonstrations of the evolving **Learning Resource Navigator**, normally after the week's daily demos. They reinforce previously demonstrated concepts through integration and useful output.

The milestone demo supplements the daily demos; it does not replace one or become a renamed daily example. Students learn the core concept through the daily lecture/demo and lab before seeing it integrated into the Navigator. The Navigator remains the instructor reference app, not the student's course-long assignment.

This proposal incorporates the [Scope Adjustment Review](119_Cohort_Readiness_and_Scope_Adjustment_Review_v1.md), including filtering, modular responsibilities, bounded memoization practice, and weighted-score revision. Where those recommendations raise depth beyond the earlier [Daily Topic List](119_Daily_Lecture_Topic_List_Review_Draft_v1.md), the change is explicit here. The [Reading Guide](119_Proposed_Reading_Selection_and_Daily_Guide_v1.md) continues to define Monday main selections and optional Tuesday/Thursday references.

Assignment IDs below are defined in the companion [Assignment List](119_Assignment_List_and_Progression_Map_v1.md). All new production work belongs in this refactor folder. Original course packages remain reuse sources.

Implementation target: Python 3.14.6, with occasional optional browser-runnable JavaScript comparisons. Daily demo code belongs under `Demos/Week_nn/Demo_nn_Descriptive_Name/`; the repository-level [Demos README](../Demos/README.md) indexes the planned folders. Each folder contains local instructor-only `notes.md`, excluded by `Demos/.gitignore`. Student-visible instructions belong in each completed demo's README.

The separate Navigator development location is `D:\@Coding_Projects\Python\Leanring_Resource_Navigator`. Follow PageForge's independently runnable, preserved milestone-snapshot approach when developing that application; do not place its milestones inside the daily demo repository.

## Independent Daily Demo Contexts

| Context / Small Tool | Sessions | Continuity and Boundary |
| --- | --- | --- |
| Equipment inventory and checkout examples | Weeks 1-4; Week 8 daily synthesis | Structured equipment records support rules, filtering, lookup, queue/undo, sorting, and a query pipeline. Each packet has its own runnable fixture; no accumulated app state or full menu/UI is required. |
| Nested donation envelopes | Week 5 Monday | Recursive/iterative aggregation on the same nested input; reuse the existing example where suitable |
| Coin-change investigation | Week 5 Tuesday | A bounded greedy claim and exhaustive-reference counterexample |
| Instrumented Fibonacci recurrence | Week 5 Thursday | Explicit memoization, call counts, correctness parity, and cache state |
| Campus route explorer | Week 6 | Adjacency representation, BFS/DFS, route reconstruction, and blocked connections on a small map |
| Music recommendation and playlist snapshot | Week 7 | Tags, baseline/weighted similarity, ranking explanations, coverage limitations, and local digest evidence |

These can be compact scripts or small tools rather than separately developed full applications. Context continuity reduces setup, but every daily packet must be usable independently. The support-ticket, expense, access-network, and learning-resource assignments remain transfer tasks with different fixtures, rules, or constraints.

## Reference Application and Useful Output

The Navigator loads a reviewed local catalog, selects resources by explicit criteria, supports lookup/ordering, explains recommendations, and exports a usable Markdown study guide. An optional HTML export may be added later; it is not required to establish course value.

Use real resource links and reviewed metadata following the [Data Sourcing Plan](119_Learning_Resource_Navigator_Data_Sourcing_Plan_v1.md). Instructor-assigned difficulty, study-time estimates, and topic relationships must remain identifiable as teaching judgments. Live APIs and external search are optional later extensions.

Suggested functional responsibilities: catalog loading/validation, filters, indexes/workflow state, search/sort, outline traversal, relationship exploration, ranking, and export. These are boundaries to demonstrate, not a requirement for eight modules or classes in every student solution.

The exported guide contains selected links, relevant metadata, explanations of selection/ranking, and optional outline/relationship notes. It does not claim to compute an optimal learning sequence. BFS/DFS order is not necessarily a prerequisite-valid order; shortest-hop relationships are not proof of shortest learning time. Dependency-respecting scheduling requires separate logic and is outside the core traversal milestone.

### Separate Navigator Demonstration List

`APP-*` identifiers belong to additional reference-app demos. `DEM-*` identifiers belong only to daily topic demos. M0-M7 remain application version labels.

| App Demo ID / Version | Scheduled Recognition | Weekly Concepts Reinforced | Functional Change / Evidence |
| --- | --- | --- | --- |
| APP-M0 / Basic Navigator | W01D01, after the daily demo; 5-8 minutes | Problem, input/output, and practical value | Briefly introduce the tool: load a reviewed fixture, select by one topic, and export a minimal Markdown list. Show purpose and baseline output, not a preview lecture on later algorithms. |
| APP-M1 / Reliable Selection | W01D03, after the daily demo; 10 minutes | Contracts, filters, validation, modular responsibilities, regression | Compare the baseline with validated combined filters; show one rule change, passing regression evidence, and selected-guide output. |
| APP-M2 / Workload Evidence | W02D03, after the daily demo; 10 minutes | Counts, fair measurement, setup/query cost, workload decisions | Show indexed ID lookup alongside repeated scans, one count/timing summary, and a qualified workload decision. Keep benchmark output separate from ordinary user output. |
| APP-M3 / Catalog State and Curation | W03D03, after the daily demo; 10 minutes | Identity, membership, queues/stacks, consistency | Process a local review queue, accept a candidate, undo one acceptance, and show consistent catalog/queue state. No live import dependency. |
| APP-M4 / Query Pipeline | W04D03, after the daily demo; 10 minutes | Search contracts, ordering, function composition, end-to-end behavior | Filter and order records, perform a key-correct search, and export the guide. Show why display order and the binary-search index may differ. |
| APP-M5 / Outline Summaries | W05D03, after the daily demo; 10 minutes | Recursive/iterative equivalence, traces, strategy fit | Summarize a nested guide outline with equivalent results and show a small trace. Revisit Monday's concepts; do not force coin change or Fibonacci into the app. |
| APP-M6 / Topic Relationships | W06D03, after the daily demo; 10 minutes | Modeling, traversal, visited state, path reconstruction, restrictions | Explore an instructor-authored topic graph and export relationship context. Explicitly distinguish shortest-hop connections from prerequisite scheduling or learning effort. |
| APP-M7 / Full Navigator | W07D03, after the daily demo; 10 minutes | Similarity, weights, ties, sensitivity, digest limitations | Export explainable recommendations and show one profile/weight change plus a local digest comparison. Use selected evidence, not a full replay of every previous feature. |
| APP-SYN / Basic-to-Full Recognition | W08D01, after the daily synthesis demo; 10 minutes | Integration and evidence-based judgment | Compare M0/M7 output for a common request and connect selected design decisions to earlier daily demos. No new feature or algorithm. |

Build M0 and the intended full M7 version after the seed catalog/schema and accepted contracts are established. Then create intermediate snapshots and milestone run sequences. Milestones should represent intentional changes from the basic to the full app, not an arbitrary retrospective division of features. Develop daily demo fixtures/code separately from these app snapshots.

Most daily demos target 12-18 minutes, with Week 8 daily synthesis up to 20 minutes. Navigator recognition is an additional, separately budgeted activity within the scheduled teaching period, not additional contact time. It must not consume the lab time assigned to core work or eliminate the day's concept demo.

### Teaching-Period Time Budget

| Meeting Type | Example Allocation | Total |
| --- | --- | ---: |
| Regular Monday, no app recognition | 5 min retrieval, 10 min framing, 15 min daily demo, 15 min worked reasoning, 5 min transition | 50 min |
| Week 1 Monday with APP-M0 | 5 min retrieval, 10 min framing, 12 min daily demo, 8 min separate app introduction, 10 min worked reasoning, 5 min transition | 50 min |
| Tuesday | 5 min retrieval, 15 min daily demo, 30 min worked analysis/practice, 10 min questions | 60 min |
| Thursday with weekly app milestone | 5 min retrieval, 15 min daily demo, 20 min worked analysis/practice, 10 min separate app milestone, 10 min questions | 60 min |
| Week 8 Monday with APP-SYN | 10 min framing, 20 min daily synthesis demo, 10 min separate app recognition, 10 min discussion/transition | 50 min |

These are planning examples, not rigid scripts. Shorten a milestone or defer it to a supplied recording if core instruction requires the time; do not silently remove core instruction or extend contact hours. The full-app demonstration need not incorporate every weekly algorithm. The Monday/Tuesday/Thursday lab allocations remain unchanged.

## Daily Demo List

### Week 1: Precision, Filtering, and Correctness

Reading anchor: Chapter 1, with optional Chapter 16 support.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W01D01 / Monday | From Equipment Request to Algorithm Contract | Interpret an equipment-loan request; clarify eligibility rules, bridge representations, compare a boundary failure with corrected results, and present the useful loan report through a small menu | Equipment inventory fixture | AL01: define record/rule contracts for support tickets |
| DEM-W01D02 / Tuesday | A Filter That Passes the Happy Path and Fails the Boundary | Select equipment by a stated battery/availability rule; test the exact threshold, nonmatches, empty results, and missing values; define invalid-value behavior | Equipment filter script | AL01: build and test ticket filters with independently chosen expected outcomes |
| DEM-W01D03 / Thursday | Combining Criteria Without Breaking Earlier Behavior | Combine equipment type and availability criteria, refactor repeated logic, and rerun regression tests; distinguish changed requirements from behavior-preserving refactoring | Equipment selection script | AL01: apply an issued rule change and explain a modular decision |

### Week 2: Growth and Controlled Experiments

Reading anchor: Chapter 1; optional scale orientation only.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W02D01 / Monday | How Much Work Does Repeated Equipment Lookup Perform? | Count inspected records for repeated scans, contrast indexed lookup, and include index construction; use tiny inputs and a short halving contrast for logarithmic intuition | Equipment lookup counter | AL02: define the counted operation and predict ticket-lookup growth |
| DEM-W02D02 / Tuesday | The Benchmark That Makes the Wrong Winner Look Fast | Compare unfair inputs/setup/printing costs with corrected repeated measurements; display parity checks and separate construction/query/end-to-end results | Equipment benchmark script with labeled generated inputs | AL02: implement alternatives, identify a confound, and produce reproducible evidence |
| DEM-W02D03 / Thursday | One Lookup or a Thousand? | Change query count and hit/miss patterns; compare costs and qualify observed crossover/no-crossover findings; discuss storage and average-case lookup assumptions | Equipment workload comparison | AL02: recommend an approach for two stated workloads using the student's evidence |

### Week 3: Representation, Queue/Stack State, and Consistency

Reading anchor: Chapter 2.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W03D01 / Monday | Inventory List, ID Index, and Membership Set | Compare lookup/update/membership on structured equipment records; demonstrate duplicate-ID policy and filtered views without treating ID lookup and arbitrary filtering as equivalent | Equipment registry script | AL03: select structures for a ticket registry and compare operations |
| DEM-W03D02 / Tuesday | Checkout Queue and One-Step Undo | Process equipment requests FIFO with a deque; record one checkout transition for LIFO undo; trace empty states and restored inventory availability | Equipment checkout state script | AL03: implement ticket processing and undo one defined state change |
| DEM-W03D03 / Thursday | Removed Equipment Still in the Queue | Introduce a stale equipment ID, show a consistency invariant and repair, then compare a saved availability snapshot with current state; briefly contrast hierarchy/network representations | Equipment state-consistency script | AL03: handle cancellation/update and explain snapshot semantics |

### Week 4: Search, Sort, and Query Composition

Reading anchor: Chapter 3; optional Chapter 4 support.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W04D01 / Monday | Search by the Key You Actually Sorted | Reveal callable key selection and equality first, then linear traversal, then binary ordered comparison with the same position/trace result contract; show absence and wrong ordering; distinguish unique IDs from duplicate models | Equipment search script | AL04: implement ticket search and define duplicate-key behavior |
| DEM-W04D02 / Tuesday | Ordering Records While Preserving Meaningful Ties | Reuse named callable keys in stable insertion sort; count comparisons/moves, compare `sorted()`, preserve ties, and change the key without rewriting the loop; merge remains a brief contrast | Equipment ordering script | AL05: implement record sorting and verify tied-key behavior |
| DEM-W04D03 / Thursday | Filter, Order, Find, Report | Separate eligibility from equality/ordered comparison; reuse Monday's search signatures/return contract, resolve positions against their own views, and compare preprocessing/query work after a rule change | Equipment query/report script | AL05: compose the ticket query pipeline, use a recovery search implementation if needed, and adapt a workload/key requirement |

October 9 scaffolding update: the three Week 4 Python demos, student READMEs, and local instructor notes now implement this modular progression. Four new runner checks cover callable-key contracts, cross-day continuity, and filter/view boundaries. The change reduces interface churn; it does not add algorithms, extend daily demo budgets, change assignment requirements, or establish measured student completion times. Optional sorting JS remains unchanged.

### Week 5: Recursion, Greedy Claims, and Repeated Work

Reading anchor: selected Chapter 4; supplied recursion/memoization companion as needed.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W05D01 / Monday | Totaling Nested Donation Envelopes Two Ways | Walk the same nested input recursively and with an explicit stack; show base cases, equivalent totals, and call/state traces; include traversal/flattening work in comparisons | Donation-envelope script | AL06: implement equivalent aggregation for a nested expense fixture |
| DEM-W05D02 / Tuesday | Greedy Change-Making: A Plausible Rule That Is Not Always Best | Use denominations 1, 3, 4 and target 6; contrast the greedy result with a supplied bounded exhaustive reference; state the optimization claim precisely | Coin-change script | AL07: implement/complete greedy logic and verify a counterexample on another issued case |
| DEM-W05D03 / Thursday | Same Answer, Less Repeated Work | Instrument a small nonnegative-integer Fibonacci recurrence, then add explicit memoization; compare calls, cache state, outputs, and memory implications with a fresh cache per run | Recurrence/call-counter script | AL07: modify a recurrence scaffold and demonstrate correct before/after call evidence |

### Week 6: Graph Representation, Traversal, and Paths

Reading anchor: selected Chapter 5.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W06D01 / Monday | Drawing the Campus Route Model | Build an adjacency list from a small campus map; explain edge direction/meaning, missing references, a cycle, and a disconnected building | Campus route fixture | AL08: define an access/workflow graph and justify what it leaves out |
| DEM-W06D02 / Tuesday | Watch the Frontier: BFS Versus DFS | Show queue/stack/visited states on the same campus graph with fixed neighbor order; explain cycle termination and introductory O(V+E) work | Campus traversal script | AL08: implement BFS and iterative DFS with independent trace explanations |
| DEM-W06D03 / Thursday | Fewest Connections Is Not Always the Shortest Walk | Reconstruct a BFS path, test start=goal/no-path, and block a connection; show why fewest edges need not minimize distance or time | Campus route/restriction script | AL08: apply a node/edge restriction, reconstruct a valid path, and explain the model's limits |

### Week 7: Explainable Ranking, Sensitivity, and Integrity

Reading anchor: small Chapters 6/12 selections; optional Chapters 14/16 support.

| Demo ID / Session | Practical Demo | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W07D01 / Monday | Two Similarity Scores, Different Song Recommendations | Compare shared-tag count with Jaccard similarity on a small song-tag/profile fixture; hand-check scores and define empty/missing-tag behavior | Music recommendation script | AL09: transfer scoring to the assigned real learning-resource subset/profile |
| DEM-W07D02 / Tuesday | Why This Song Moved Up the List | Add bounded nonnegative tag weights, show score contributions and deterministic ties, and change preferences/weights; clustering stays an optional short preview | Weighted music-ranking script | AL09: implement a weighted resource-ranking revision and explain changed/unchanged ranks |
| DEM-W07D03 / Thursday | A Playlist Digest Does Not Prove a Good Recommendation | Show a coverage/missing-tag limitation, then hash canonical local playlist metadata before/after an edit; distinguish digest, similarity, runtime hashing, and encryption | Music ranking/snapshot script; hashing metadata, not audio files | AL09: demonstrate one resource-ranking limitation and interpret an integrity check without claiming source authenticity |

### Week 8: Synthesis and Assessment

Reading anchor: selected Chapter 16; no new Tuesday/Thursday reading.

| Demo ID / Session | Practical Demo / Assessment | Behavior and Evidence to Show | Independent Context | Student Transfer |
| --- | --- | --- | --- | --- |
| DEM-W08D01 / Monday | Defend an Equipment Selection, Then Change the Request | Compare two correct approaches, question an efficiency/correctness claim, and respond to an unfamiliar filter/workload change using tests and evidence | Small equipment-selection fixture; no new app or algorithm | Formative individual prediction plus peer discussion; rehearsal for FINAL-P1/P2 |
| ASSESS-W08D02 / Tuesday | Final Part 1 | Brief task/environment clarification only; no solution demo during assessed work | Individual task fixtures | FINAL-P1 individual applied solution set |
| ASSESS-W08D03 / Thursday | Final Part 2 | Personalized explanation and adaptation prompts, not a new content demo | Student's Part 1 work | FINAL-P2 individual defense |

## Reuse Candidates

The original packages below are located under `../10-152-119_Intro_To_Algorithms/Assignments/`. Reuse is conceptual and provisional until code/output review. Do not copy a package unchanged merely because its topic matches.

| Existing Package | Target Demo | Reuse / Adjustment |
| --- | --- | --- |
| `Lab_01/demo/` charger decision | DEM-W01D01, DEM-W01D02 | Retain precise-rule framing and failure discussion; adapt to equipment availability/eligibility and structured filtering |
| `Lab_02/demo/` lookup growth | DEM-W02D01, DEM-W02D02, DEM-W02D03 | Reuse comparison shape in equipment data; add fair-workload parity and construction/query separation |
| `Lab_03/demo/` attendance representation | DEM-W03D01 | Reuse side-by-side representation reasoning; add equipment IDs, membership, and filtered-view semantics |
| `Lab_04/demo/` book-title search | DEM-W04D01 | Retain traces and sorted-data counterexample; define search keys/duplicates explicitly |
| `Lab_05/demo/` nested donation envelopes | DEM-W05D01 | Reuse nested/base-case framing; ensure iterative alternative processes equivalent nested input and accounts for preprocessing |
| `Lab_06/demo/` campus traversal | DEM-W06D01, DEM-W06D02 | Retain the campus context and graph/frontier concepts; add directionality and path/model-limit evidence |
| `Lab_07/demo/` music recommendation | DEM-W07D01, DEM-W07D02 | Retain music context, tag similarity, and explanation; add weighted contributions, deterministic ties, and local snapshot evidence |

Queue/undo, composed pipeline, greedy, explicit memoization, and integrity/sensitivity sequences need new or substantially expanded examples. Existing Week 8 synthesis material is an additional reuse candidate.

## Demo Packet Requirements

Each daily packet provides a runnable focused entry point, deterministic small fixtures, expected output/evidence, instructor run sequence, prediction questions, a selected failure/change case, and a clear transfer/stop point. Its code and data must not import or depend on Navigator modules/snapshots. Common generic test/printing helpers are acceptable.

Store instructor delivery guidance in `notes.md`: purpose, ordered run/build sequence, expected results to verify, prediction questions, misconceptions/correctness cautions, timing, and stop/transfer points. Preserve student-facing run requirements and explanations in `README.md`. The daily repository is intended for the SWTC-AAISE GitHub account; verify that no instructor notes are tracked before publishing.

Each additional app packet needs its own milestone snapshot, short before/after run sequence, useful output, one selected evidence artifact, and an explicit connection back to the week's daily demos. It reinforces concepts already taught rather than supplying an implementation prerequisite absent from the daily instruction. APP-M0 introduces purpose/output; APP-M5 reinforces recursion/iteration without forcing the week's unrelated strategy examples into the app.

Use small controlled equipment, donation, recurrence, campus, and song fixtures for daily demos. Clearly identify fictional teaching metadata; real music files or live services are unnecessary. Use 8-12 selected real catalog records for app recognition and 30-50 reviewed records for full-app usefulness. Use separately labeled generated data for large growth experiments; do not export synthetic benchmark links as study resources. Use controlled test records for malformed data rather than misrepresenting real providers.

Core student work must differ from the demonstrated solution through rules, data, constraints, workload, or required reasoning. Withhold full success solutions until the relevant submissions are complete. Students may inspect shared scaffolding without being given their graded algorithm implementation.

Prepare and test output before class, provide a plain-text fallback, and make focused demos usable without live network calls. All 22 daily Python packets are now implemented under `Demos/`, with embedded teaching fixtures, student READMEs containing expected output, and local instructor `notes.md`. The verification runner passes 58 Python checks on Python 3.14.7 and 3.12.10; exact 3.14.6 verification remains outstanding. W01D01 now provides a menu-selected loan-desk report and paused teaching walkthrough, with short purpose docstrings and no parser or technical trace machinery; this first presentation refactor awaits instructor evaluation before broader rollout. Two optional browser JS comparisons have eight passing structure/logic/event-wiring checks, not browser-layout verification. The separate Navigator full app, real catalog, and independent M0-M7 snapshots are now implemented; the archive passes 129 test methods on both Python 3.12.10 and 3.14.7. See [Navigator implementation status](119_LRN_Full_Version_Implementation_Status_v1.md). Instructor acceptance, the separate APP-SYN recognition packet, assignment packets, and assessment guides remain future deliverables.

## Standard Testing and Bounded Python Progression

All 22 daily demos now place regression assertions in separate `test_demo.py` files; applications do not execute them or print a check banner. See [demo authoring guidelines](119_Demo_Authoring_Guidelines_v1.md). The proposed first explicit `argparse` lesson is W02D02 (one integer size option, default, help, and safe range), followed by selective reinforcement in W05D03, W06D03, and W07D02. This placement still needs lecture-outline integration; it does not require parsers in every later demo or alter assignment scope. W01D01's printed teaching walkthrough is implemented; instructor evaluation and broader presentation refactors remain pending.

## Production Order and Evaluation

1. Review this list with the companion assignment list; confirm topic/demo/transfer fit.
2. Build the verified seed catalog, schema, and hand-checkable fixtures.
3. Specify and build daily demo packets in the separate contexts, piloting Weeks 1, 2, 4, and 5 first; these do not depend on completing the full app.
4. Establish M0/M7 contracts, implement the basic/full app versions, and derive separate milestone snapshots and recognition packets.
5. Produce assignment packets and the student pairing guide for the selected modes.
6. Regenerate the IIM/session outlines and reuse compatible lecture material against the accepted map.

Evaluate whether each daily session has one clear practical outcome, visible evidence, achievable demo time, and meaningful student transfer. Separately evaluate whether each app milestone visibly reinforces earlier demos and fits its additional recognition budget. Check the bounded Week 5/7 promotions against actual lab completion rather than assuming prior-course early finishes predict 119 timing.

Coverage: 22 independent daily teaching demos; 8 separate app demonstrations for M0-M7 plus APP-SYN recognition, totaling 9 additional app packets; and 2 assessment guides. Seven weekly milestone demonstrations are normally Thursday, with separate Week 1 basic-app introduction and Week 8 synthesis. No additional graded Week 8 lab and no course-long student app requirement.
