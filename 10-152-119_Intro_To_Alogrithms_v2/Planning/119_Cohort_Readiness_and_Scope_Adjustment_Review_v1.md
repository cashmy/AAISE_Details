# 119 Cohort Readiness and Scope Adjustment Review

Instructor review | October 8, 2026

## Finding

Raise the required application depth of the current draft and add selected practical concepts to the daily topic list. Retain the eight-week sequence and three-day schedule. The strongest opportunities are filtering, modular algorithm design, student-owned experiments, and peer review that leads to a tested revision.

The draft already requires multiple approaches, tests, traces, changed requirements, and explanations. Those expectations should remain. It is more developed than the original course, so the new cohort evidence does not establish that every proposed assignment would be too easy.

This review proposes changes for evaluation. It does not revise the existing topic list, reading guide, or rescope map, or create instructional content.

## Evidence and Limits

Instructor observations:

- Approximately half of students typically finished labs early in 117 and 118.
- Capstone audiences asked insightful questions about application operations and proposed improvements.
- Several students implemented filtering without explicit instruction on that topic.
- Many applications showed architectural thinking.

These observations support stronger expectations for transfer, decomposition, practical data operations, explanation, and revision. They do not establish that every student has the same readiness, nor that students already understand complexity, recursion, graph traversal, or mathematical similarity measures.

Early completion describes prior-course labs, not measured completion of the proposed 119 assignments. The existing estimates of roughly five hours per weekly assignment remain unverified. Architectural thinking does not require adding classes or a framework; well-chosen functions, modules, contracts, and data flow can demonstrate it.

## Findings in the Current Draft

| Priority | Evidence in the draft | Adjustment |
| --- | --- | --- |
| High | The topic list has no explicit filtering progression, despite the instructor's evidence of spontaneous transfer. Search, membership, and ranking are present, but they are different operations. | Add predicate-based filtering, combined criteria, and filter/order/lookup pipelines to suitable existing sessions. |
| High | Week 1 centers on a small decision function; architecture appears mainly through decomposition and refactoring. | Use structured records and require a contract between validation, decision/filtering, and output. Keep the initial baseline approachable. |
| High | Week 2's topic list says interpret an experiment, while its assignment already requires implementing and benchmarking alternatives. | Make student ownership of predictions, counted work, experimental controls, and interpretation explicit. This is clarification of existing depth, not a whole new assignment. |
| High | Week 5 Thursday limits memoization to tracing supplied code and labels a full memoized coin solver as stretch. | Add one scaffolded memoization modification and before/after call-count comparison as core practice. Keep a complete dynamic-programming solver optional. |
| Medium | Peer review is already mentioned, including a 15-minute lab allowance, but no consistent evidence or revision outcome is defined. | Specify one consequential peer question, one student response, and one tested revision or evidence-based rejection in each weekly submission. |
| Medium | Several stretch tasks are plausible candidates for deeper core work, but promotion of all of them would overload the week. | Select a small set of promotions: workload decision in Week 2, composed query pipeline in Week 4, bounded memoization in Week 5, bounded weighted-score revision in Week 7. |
| Medium | The rescope map fixes one integrated assignment every week, while the later reading guide and instructor permit one or two. | Choose assignment count by conceptual connection; two connected assignments fit Week 5 particularly well. |

References: [Daily Topic List v1](119_Daily_Lecture_Topic_List_Review_Draft_v1.md), [Reading Guide v1](119_Proposed_Reading_Selection_and_Daily_Guide_v1.md), and [Full Rescope Map v1](119_Full_Course_Rescope_Map_Review_Draft_v1.md).

## Daily Adjustment Map

The following reviews all 24 meeting slots. Additions fit inside existing sessions and labs; they do not imply longer lectures or extra required readings. Items marked retain already contain adequate new conceptual work.

| Session | Assessment | Proposed Topic / Depth Adjustment |
| --- | --- | --- |
| W01D01 Monday | Raise application level | Frame a structured-record problem; define inputs/outputs and separate validation, algorithm, and presentation responsibilities. Use a brief readiness check rather than extended syntax review. |
| W01D02 Tuesday | Add practical content | Introduce a filter predicate; test matching and nonmatching records, empty results, malformed inputs, and boundary rules. Distinguish selecting records from finding one record. |
| W01D03 Thursday | Raise required depth | Compose two filter criteria, refactor shared logic, and respond to a changed rule. Require regression evidence and an explanation of module/function boundaries. |
| W02D01 Monday | Retain core concepts | Explain growth by counting work in a familiar selection or lookup problem. The new abstraction is complexity reasoning, not Python collection syntax. |
| W02D02 Tuesday | Clarify stronger core ownership | Students define the measured operation, predict growth, implement alternatives, and identify a confound in the experiment. Supply harness mechanics, not their conclusions. |
| W02D03 Thursday | Promote bounded decision task | Require evidence-based selection for two query workloads and account for construction cost. An observed crossover or a justified finding that no crossover was observed is acceptable. |
| W03D01 Monday | Add practical application | Connect dictionary/set choices to stable identity, membership, and filtered views of records. Compare a list scan with keyed access without conflating their contracts. |
| W03D02 Tuesday | Retain new conceptual depth | Keep stack/queue operations and state transitions core. Require the student to explain FIFO/LIFO consequences in the workflow; multi-operation undo stays optional. |
| W03D03 Thursday | Raise architectural reasoning | Add a state-consistency invariant and explain whether filtered results are snapshots or live views. Test cancellation/update effects; keep trees/graphs as previews. |
| W04D01 Monday | Retain search depth | Make matching keys and duplicate-result behavior explicit. Keep linear/binary implementations and boundary tests; do not also require a lower-bound algorithm. |
| W04D02 Tuesday | Raise record-level application | Use structured records, key functions, ties, and stable ordering. Keep insertion sort core; guided merge-sort contrast remains sufficient. |
| W04D03 Thursday | Add composed pipeline | Combine filter, sort, and search through defined functions. Explain data flow, preserved preconditions, result semantics, and end-to-end cost after a changed requirement. |
| W05D01 Monday | Retain core and clarify ownership | Require recursive and iterative implementations with equivalent results, base-case tests, and a state/call trace. New recursion learning still needs explicit instruction. |
| W05D02 Tuesday | Clarify implementation expectation | Students implement or complete the greedy method and verify its counterexample against a supplied small-input exhaustive reference. Do not require a new exhaustive solver as well. |
| W05D03 Thursday | Promote limited memoization practice | Modify a scaffolded recurrence with memoization, verify unchanged results, and compare repeated-call counts and storage. General DP design remains guided/optional. |
| W06D01 Monday | Retain core and strengthen modeling | State graph directionality and omitted details; validate references. Require a model justification, not a large generated graph. |
| W06D02 Tuesday | Retain substantial core work | BFS/DFS, cycle handling, visited state, and O(V+E) reasoning already provide meaningful depth. Add independent trace explanation rather than another traversal algorithm. |
| W06D03 Thursday | Clarify existing adaptation | Implement the existing route restriction through an allowed-edge/node rule, retest, and explain the resulting path. Weighted-path implementation remains optional. |
| W07D01 Monday | Retain core and strengthen evidence | Compare two explainable scores on the same representation and manually verify selected results. Do not add several numeric distance metrics to the required task. |
| W07D02 Tuesday | Promote bounded score revision | Add a simple configurable weighted-feature score and explain its ranking effect. Reduce clustering to an optional preview so this is a substitution in lecture emphasis. |
| W07D03 Thursday | Raise critique specificity | Require one concrete example where missing data, weights, or coverage changes an outcome. Keep the bounded integrity check and distinguish its claims from ranking quality. |
| W08D01 Monday | Raise synthesis ownership | Use a short peer design review and response to an unfamiliar requirement. Assess the quality of reasoning rather than presentation polish. |
| W08D02 Tuesday | Retain timed final boundary | Use richer records, meaningful edge cases, and a justified design decision within the existing tasks. Do not add a fourth task or a full benchmark suite. |
| W08D03 Thursday | Retain individual defense | Require an evidence-backed response to a changed requirement. Ask about newly promoted concepts only if they were taught and practiced before the final. |

## Weekly Assignment Recommendations

One or two assignments should remain available. The patterns below are recommendations for later packet design, not a new grading scheme. Multiple checkpoints need not become separate graded assignments.

| Week | Recommended Pattern | Stronger Required Work | Keep Optional / Supplied |
| --- | --- | --- | --- |
| 1 | One staged record-processing assignment | Separate validation/rules/output; predicate and combined filtering; targeted tests; changed-rule revision; peer response | Supply record fixtures and test harness; configuration systems remain optional |
| 2 | One experiment with a workload-change revision | Correctness parity; owned count/prediction; controlled comparison; preprocessing account; workload recommendation with qualified crossover evidence | Supply generation/timing plumbing; precise crossover fitting and detailed memory profiling remain optional |
| 3 | One evolving registry/workflow | Operation contracts; queue/stack behavior; consistency invariant; cancellation/update tests; filtered-view semantics | Supply input driver; one bounded undo remains enough; multi-operation undo stays optional |
| 4 | One staged query pipeline, or two connected search/sort tasks | Student-owned search/sort algorithms; record-key ordering; filter/order/lookup composition; end-to-end evidence; changed requirement | Benchmark fixtures supplied; independent merge sort/lower-bound search remain optional |
| 5 | Two connected assignments | A: recursive/iterative aggregation. B: greedy counterexample and a short scaffolded memoization experiment with call-count comparison | Supply exhaustive reference and recurrence scaffold; full minimum-coin DP implementation stays optional |
| 6 | One graph model/traversal/path assignment | Existing BFS/DFS/path work; model justification; independent trace explanation; restriction-rule revision; tests | Supply fixtures/diagram aids; weighted shortest-path implementation stays optional |
| 7 | One staged ranking assignment containing a short integrity investigation | Baseline scores; top-k/ties; weighted-score revision; rank-change evidence; concrete limitation; digest interpretation | Supply serialization helper; full clustering, ML training, and multiple distance metrics stay optional |
| 8 | Existing two-part final | Transfer, individual explanation, tests/evidence, and a justified change | Familiar interfaces and surrounding I/O supplied; no extra large build |

These recommendations increase application complexity and ownership without requiring a full application shell every week. Reuse and extend existing assignments where their learning targets fit. Allow modules and classes when useful, but judge the algorithmic choices and interfaces rather than rewarding an architectural style for its own sake.

## Shared Completion Expectations

A working baseline is an early checkpoint. A complete weekly submission should show:

1. A working implementation satisfying a stated contract.
2. Meaningful tests, including a deliberate failure or boundary case where appropriate.
3. A comparison, changed requirement, or substantive refactor tied to that week's concepts.
4. Evidence supporting the student's claim about correctness, behavior, or efficiency.
5. A peer question and response, with a tested revision or a justified decision not to adopt the suggestion.
6. An individual explanation of one important design decision and any tool assistance.

Introduce peer review within the already planned lab time. Use approximately 10-15 minutes for a focused exchange, then apply the response during the revision period. Do not add lengthy weekly presentations or repeat the same reasoning in several separate documents.

Students may suggest improvements beyond the week's scope. They should identify those as future work rather than automatically implement them. This preserves thoughtful technical discussion without turning every useful suggestion into extra required development.

## Scaffolding and Workload

Retain fixtures, data generation, action drivers, and timing helpers where they remove setup unrelated to algorithmic learning. Gradually reduce supplied solution logic, predetermined expected results, and prewritten interpretations. A higher-level assignment can still have substantial scaffolding.

Teach the baseline first and make the comparison/revision stage required. Provide targeted support and checkpoints for students who need more time. Faster students can deepen evidence, investigate another case, or take an optional extension after completing the strengthened core.

Do not claim that these additions fit merely because half the cohort finished prior labs early. Capture time to baseline, time to complete core revision/evidence, help needed, and explanation quality while piloting Weeks 1, 2, and 5. Week 4 also merits review because its original core already includes three algorithm implementations.

If core work exceeds the class time plus the intended outside-class allowance, narrow redundant implementation or reporting before adding homework. If students finish early with accurate explanations and successful transfer, promote the next relevant extension. Finishing early with weak evidence calls for deeper requirements, not necessarily more named algorithms.

## Reading Implications

Keep the main Monday reading and optional Tuesday/Thursday pattern. Filtering, function boundaries, and practical benchmarking need short instructor examples/companions where the textbook summary does not identify exact coverage. They do not require assigning additional chapters.

For Week 5, provide the recurrence/memoization example through Thursday instruction and lab guidance. Its optional reading cannot become a prerequisite for the promoted core task. For Week 7, teach weighted scoring in the Tuesday demo; make room by limiting the clustering preview. No new ML chapter is needed.

Verify exact textbook sections later. These adjustments concern practical applications of the selected concepts, not a claim that the source map contains every proposed example.

## Version Alignment Before the Next Draft

The early rescope artifact predates later instructor decisions. Its next revision should:

- Allow one or two connected assignments per week instead of fixing all weeks to one submission pattern.
- Record the instructor's explanation of SWTC's documented versus scheduled hours, and remove the mismatch as an unresolved design blocker.
- Align preparation estimates with the later reading guide's 45-75 minute selected-reading range rather than the earlier 30-45 minute range.
- Carry the cohort observations into the readiness assumptions without applying the strongest examples to every student.
- Replace trace-only memoization and optional-only weighted scoring with the bounded core practice proposed here, if adopted.

Priority recommendation: strengthen Weeks 1-3 and add the selected Week 5/7 promotions. Retain the substantial search/sort and graph core, using richer application and explanation requirements there. Evaluate these changes before regenerating the IIM, lecture outlines, demos, and assignment packets.
