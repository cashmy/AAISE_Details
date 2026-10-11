# Instructional Intent Matrix v3

10-152-119 Introduction to Algorithms | Instructor working draft | October 9, 2026

## Purpose and Authority

Define the intended learning, instruction, practical demonstration, lab transfer, and observable evidence for every meeting of the eight-week course. This is the delivery spine for daily lecture outlines, slide decks, demo refactors, and assignment packets; it is not those completed materials.

This version supersedes the [original IIM v2](../../10-152-119_Intro_To_Algorithms/v2/IIM_Matrix_v2.md) for the current refactor. The original Markdown and spreadsheet are preserved. Version 3 identifies this document revision, not another course folder. Earlier rescope/topic drafts remain historical where they differ from the decisions below.

Current alignment sources:

- [Reading Assignments](../Reading_Assignments.md): instructor-curated reading selections and initial heading/page validation. Recent instructor clarification locates divide-and-conquer at pp. 88-90a, dynamic programming at pp. 90b-91, and greedy strategy at pp. 92-93. PageRank/linear programming is recommended, not required strategy work.
- [Coverage Map v3](119_Textbook_Coverage_and_Reference_Map_v3.md): conceptual coverage and instructional-depth boundaries, not an authority overriding subsequently curated reading requirements.
- [Assignment Progression](119_Assignment_List_and_Progression_Map_v1.md): nine regular assignments, collaboration/ownership, scaffolding, and final structure.
- [Week 1 objectives and assignment scope](119_Week_01_Objectives_and_Assignment_Scope_v1.md): finalized Week 1 production baseline, two ticket-selection operations, issued policy change, and rubric/time reconciliation. This later specification controls Week 1 details without changing the rest of the course.
- [Demo and Reference-App Map](119_Demo_List_and_Reference_App_Milestones_v1.md) and [implemented demo index](../Demos/README.md): independent daily demos and separate Navigator recognition.
- [Pairing/submission guide](../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md) and [GitHub guide](../PreCourse_Setup/GitHub_Class_Repository_and_Submission_Guide.md): current operating procedure. Partners rotate per assignment; public shared repositories support paired work, and complete individual class-repo copies are submitted. The older selective pairing plan is historical where it differs.
- [Demo Authoring Guidelines](119_Demo_Authoring_Guidelines_v1.md): problem-solving output, instructional walkthroughs, separate tests, purpose docstrings, and bounded Python enhancement.
- [Existing competency framework](../../10-152-119_Intro_To_Algorithms/v2/WIDS_Course_Competency_Framework_v3.md) and [existing MRS-AL](../../10-152-119_Intro_To_Algorithms/v2/MRS-AL_Master_Rubric_System.md): retained competency/category vocabulary and rubric framework. Assignment mappings follow completed packets; N/A categories receive automatic full points under the instructor's established practice, not a finding of demonstrated proficiency.

Page references below carry the instructor's validation record and supplied clarifications; they have not been independently checked against a textbook copy in this workspace. `a`/`b` identify section boundaries on the same printed page, not separate page numbers. Student-facing instructions should name the relevant start/stop headings.

## Schedule and Delivery Contract

| Meeting | Scheduled Time | Planning Instruction | Planning Lab |
| --- | ---: | ---: | ---: |
| Monday | 120 min combined lecture/lab | 50 min | 70 min |
| Tuesday | 180 min: lecture plus lab | 60 min | 120 min |
| Thursday | 180 min: lecture plus lab | 60 min | 120 min |
| Regular-week total | 480 min / 8 hours | 170 min | 310 min |

Monday's split is adaptable instructional planning, not a new official contact-hour classification. The scheduled eight-week delivery totals 64 clock hours; the existing institutional framework retains 72 hours. The instructor has acknowledged this distinction. This IIM does not reopen it as a blocker, amend institutional hours, add meetings, or count homework as contact time.

Weeks 1-7 contain three distinct lecture/demo/lab sequences. Week 8 Monday is synthesis; Tuesday and Thursday use their entire 180-minute meetings for individual assessment, not a new lecture plus ordinary lab. Total: 24 meeting slots, 22 teaching sessions with daily demos, and two final-assessment sessions.

Assign the weekly main reading before Monday. Tuesday/Thursday use optional rereading/support where useful; required concepts must be taught and supported without assuming optional passages were read. No required asynchronous video lecture component is introduced.

Daily topic demos normally occupy 12-18 minutes; Week 8 synthesis may use up to 20. Navigator recognition is additional and separately named but remains inside the scheduled instruction: APP-M0 uses 5-8 minutes on W01D01; APP-M1 through APP-M7 normally use about 10 minutes on the corresponding Thursday; APP-SYN uses about 10 minutes on W08D01. Do not replace the daily demo with a milestone or let app recognition displace essential instruction.

Individual homework is expected and can support completion beyond labs, especially in Week 4. Publish amounts, authorship, help permissions, and deadlines in each packet. The earlier 1-2-hour estimate is not an approved cap. Required partner coordination stays in synchronous breakout-room time; no assumed pairing speedup or unlimited homework spillover is built into the schedule.

## Learner and Scope Basis

Students have completed Python Foundations and are progressing through Web Foundations, including modularity, loops, decisions, collections, and asynchronous JS. Capstones demonstrated filtering, architectural judgment, and useful peer questions. Use these skills immediately; do not reteach the entire introductory language course or assume prior mastery of algorithm analysis, recursion, graphs, or similarity.

Increase depth through purposeful tests, comparison, independently justified expectations, changed requirements, and explanations. More features or more code are not automatic evidence of rigor. Week 1 intentionally includes collaboration adjustment; Week 5 intentionally protects lower-pressure consolidation. Optional extensions do not become required because students finish early.

Python console tools and the standard library are primary. Optional HTML/CSS/JS comparisons retain separate structure/style/behavior files and introduce no graded alternative implementation. No Django/MVT, live API, notebook, visualization package, or ML-training stack is required.

## Weekly Intent and Reading Anchors

These anchors support curriculum topics; [Reading Assignments](../Reading_Assignments.md) remains the complete curated reading list. Reading exposure does not make every textbook example a required implementation.

| Week / Unit | Main Instructional Intent | Reading Anchor | Assessed Transfer |
| --- | --- | --- | --- |
| 1 / Algorithmic foundations | Turn ambiguous requests into precise contracts; test and revise behavior | Ch. 1 pp. 3-7 and 9-12 before Performance Analysis; recommended Ch. 16 pp. 458-460 | AL01: ticket rules, filters, regression evidence |
| 2 / Algorithmic foundations | Connect input/workload to counted work, fair measurement, and qualified recommendations | Ch. 1 p. 12 beginning Performance Analysis through p. 24; Ch. 15 p. 438 reference | AL02: lookup workload investigation |
| 3 / Structures, search, sort | Choose representations by operation; manage identity, queue/undo state, and consistency | Ch. 2 pp. 25-53; Ch. 13 pp. 393-405 optional | AL03: ticket registry, queue, undo |
| 4 / Structures, search, sort | Implement key-correct search and stable insertion sorting; compose a valid pipeline | Ch. 3 pp. 55-77 | AL04: individual search; AL05: filter/sort/search pipeline |
| 5 / Strategy and behavior | Compare recursion/iteration; test greedy claims; reduce repeated work with bounded memoization | Ch. 4 pp. 79-82, skim 83-86, read 86-93; pp. 100-107 recommended only | AL06: nested expense aggregation; AL07: two bounded strategy investigations |
| 6 / Strategy and behavior | Model relationships; implement traversals, reconstruct unweighted paths, adapt restrictions | Ch. 5 pp. 109-117 and 125-132; network analysis pp. 117-125 optional | AL08: access network and restricted routes |
| 7 / AI/data bridges | Explain similarity/ranking, weighted revisions, sensitivity, and limited integrity evidence | Ch. 6 pp. 143-149 and Ch. 12 pp. 373-383; curated list governs other reading | AL09: explainable resource ranking and integrity |
| 8 / Synthesis and explanation | Evaluate evidence and defend/adapt previously taught algorithms individually | Ch. 16 pp. 457-474; no new Tuesday/Thursday reading | FINAL-P1 and FINAL-P2; Monday is formative |

Chapters 2/3 are broader reading exposure than the assessed implementation targets: no full tree build, implementation of every sort, or additional advanced search is implied. Chapter 16 connects ethics, bias, and the Tay case to students' own evidence and limitations, not a new final-week algorithm unit. Reading-time estimates in earlier maps remain provisional; do not claim measured fit from page counts.

## Daily Instructional Intent Matrix

`D01` = Monday; `D02` = Tuesday; `D03` = Thursday. Each teaching row specifies a lecture intent as well as lab work. `DEM-*` is the independent daily example; `APP-*` is additional Navigator recognition. Required evidence below is intent for packet development, not a newly published deadline or grading weight.

### Week 1: Precision, Correctness, and Revision

Keywords: algorithm, contract, input/output, assumption, predicate, boundary, expected/actual, regression, refactor. Primary: T1/T3/T5/C1/C5; Secondary: T2/T6/C2; Light: C3/C4/C6; T4 N/A. AL01 is paired development, not formal peer review.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W01D01 | Clarify a practical request; distinguish assumptions from explicit rules; connect English, pseudocode, and Python; locate validation, selection, and presentation responsibilities | DEM-W01D01: Equipment Loan Desk menu/report and paused walkthrough; isolate `>` versus `>=`. Additional APP-M0: useful basic Navigator output, 5-8 min | AL01 paired validation/open-ticket baseline and role adjustment; familiar Python | Working baseline and independently reasoned outcomes; no separate planning document |
| W01D02 | Define a filter predicate; distinguish ordinary, exact-boundary, invalid, and empty-result cases; diagnose a plausible defect using expected/actual evidence | DEM-W01D02: equipment filter boundary failure and correction; user-oriented result plus labeled instructional comparisons | AL01 paired follow-up v1/tests/repair in breakout rooms; rotate drivers with Git handoffs | Purposeful executable checks and reproduced defect/repair; brief README observations |
| W01D03 | Combine criteria clearly, explicitly bridge mandatory conditions and grouped OR alternatives; distinguish an issued rule change from behavior-preserving refactoring; explain changed and preserved expectations | DEM-W01D03: combined equipment criteria and regression. Additional APP-M1: reliable Navigator selection/output, about 10 min | AL01 paired rule-change/refactor; each student copies the final solution into their own class repo and adds personal README notes | Changed-rule/regression summary, readable result, separate tests, individual explanation |

Monday's simple boundary example illustrates precision; Tuesday develops systematic testing rather than replaying Monday's entire walkthrough. Thursday does not introduce a full application shell or solve the ticket assignment through the equipment demo.

### Week 2: Growth, Measurement, and Workload Choice

Keywords: input size, counted operation, Big-O, time/space, preprocessing, parity, confound, workload. Primary categories: T3/T4/T5; supporting T1/T2. Predictions and conclusions remain individual within AL02's paired experiment.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W02D01 | Define input size and the operation being counted; interpret constant/linear/quadratic/logarithmic growth; distinguish counting from exact elapsed time | DEM-W02D01: repeated equipment scans versus index construction/query counts, with a small halving contrast | AL02 individual predictions followed by paired baseline/alternative implementation on fresh ticket fixtures | Defined unit, growth prediction, equivalent outputs, small count table |
| W02D02 | Control inputs and repeated measurements; separate construction, query, and end-to-end cost; identify an unfair comparison | DEM-W02D02: misleading equipment benchmark repaired. Bounded Python introduction: one `argparse --size` option, default/help/type/range | AL02 paired controlled experiment with supplied timing/data-generation plumbing; students own algorithms, cases, and interpretation | Parity tests, method/confound explanation, four-size evidence across two workloads |
| W02D03 | Evaluate few/many queries, hit/miss behavior, index reuse, storage, and expected average-case lookup; qualify the recommendation | DEM-W02D03: changed equipment workload. Additional APP-M2: Navigator workload evidence, about 10 min | AL02 paired comparison and individual workload recommendations; no required crossover discovery | Setup/query/total evidence, limitations, two justified recommendations |

Introduce `argparse` explicitly in a 3-5-minute lecture segment, not as unmentioned plumbing or extra demo time. Formal proofs, distributed computing, and compulsory plotting remain outside scope.

### Week 3: Representation and Consistent State

Keywords: identity, membership, access pattern, dictionary, set, deque, FIFO/LIFO, invariant, snapshot. Primary categories: T2/T3/T4/T5; shared AL03 evidence plus individual contract/state explanations.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W03D01 | Match list/dictionary/set representations to lookup, update, and membership; define identity/duplicate policy and filtered-view semantics | DEM-W03D01: equipment inventory representations | AL03 paired operation comparison and registry baseline; supplied fresh fixtures avoid an AL01 dependency | Operation/structure comparison and justified contracts |
| W03D02 | Explain FIFO/LIFO through a bounded workflow; identify state changed and restored by one undo operation | DEM-W03D02: equipment checkout queue and one-step undo | AL03 paired deque processing and stack-backed undo; rotate roles and individually explain a transition | Action/state trace; empty-state, duplicate, and restoration tests |
| W03D03 | Maintain consistency across structures after update/cancellation; diagnose stale references; distinguish saved snapshots from live state; preview hierarchy/network | DEM-W03D03: stale equipment queue and snapshot. Additional APP-M3: Navigator curation state, about 10 min | AL03 paired consistency revision and individual invariant/snapshot explanation | Checked invariant, stale-entry/cancellation evidence, individual state reasoning |

No general undo engine, full tree implementation, or extra analytics package is required.

### Week 4: Search, Stable Sorting, and Composition

Keywords: named key, matching criterion, ordered comparison, precondition, linear/binary search, stable ties, insertion sort, pipeline. Primary categories: T1-T5 as task-specific evidence supports; no compulsory cooperation evidence in individual AL04.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W04D01 | Separate key/matching logic from traversal; progress through linear and binary search with one result contract; explain matching order and duplicate semantics | DEM-W04D01: modular equipment search preconditions, criteria -> linear traversal -> ordered binary traversal | AL04 individual search implementations/tests; planned individual continuation outside class permitted | Small traces; absent/endpoints/empty/singleton/duplicate tests; ordering failure and precondition explanation |
| W04D02 | Reuse a named key for stable insertion sorting; distinguish comparisons/moves and library use; recognize merge/divide-and-conquer without another implementation requirement | DEM-W04D02: stable equipment sorting; optional separate-layer browser JS comparison | Formative AL04 checkpoint/recovery, then AL05 individual sort baseline; nominal 30/90-min lab split remains flexible | Tied-key stability, ordered/reverse/shuffled tests, counts and `sorted()` parity |
| W04D03 | Compose eligibility, display order, and key-correct lookup; evaluate setup reuse and total workflow cost; adapt one requirement without interface churn | DEM-W04D03: equipment query pipeline. Additional APP-M4: Navigator pipeline/output, about 10 min | AL05 individual bounded investigation and pipeline, issued adaptation, tests and explanation; homework may complete packaging/evidence | Pipeline sketch, workload comparison, changed/preserved behavior, individual rationale |

Supply recovery search and measurement plumbing where needed, clearly labeled as not the student's AL04 implementation. Binary search requires an ordered key, not an arbitrary predicate. Stable insertion sorting stays student-owned; merge implementation and lower-bound search are optional.

### Week 5: Bounded Strategy Investigations

Keywords: base case, recursive state, explicit stack, decomposition, greedy claim, counterexample, repeated subproblem, memoization, fresh cache. Primary categories: T1/T3/T4/T5. This is intentionally a lower-pressure consolidation week, not a compulsory catch-up period.

Reading connection: divide-and-conquer pp. 88-90a; DP strategy pp. 90b-91; greedy pp. 92-93. Supply concise recursion/explicit-stack and instrumented-memoization support rather than claim that these passages directly provide the specific demos.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W05D01 | State a base case and processing state; compare recursive aggregation with an explicit-stack alternative on the same input; account for traversal/storage | DEM-W05D01: nested donation totals, two equivalent approaches | AL06 individual chosen-app aggregation (fundraiser, storage, project effort, or inventory) with bounded numeric/malformed-input policy; protect first recursion learning | Empty/flat/nested/mixed-depth parity, call/state trace, individual comparison |
| W05D02 | Distinguish a local choice from an optimality claim; use bounded exhaustive evidence to challenge a greedy result | DEM-W05D02: greedy coin-change counterexample, supplied exhaustive reference | Flexible AL06 completion checkpoint, then AL07 paired greedy investigation; do not enforce the old fixed lab split | Objective/constraints, reachable/unreachable cases, counterexample/reference comparison |
| W05D03 | Preserve recurrence outputs while reducing repeated calls with explicit memoization; interpret cache storage and fresh-run measurement | DEM-W05D03: bounded Fibonacci call/cache comparison; reinforce `argparse --n`. Additional APP-M5: Navigator recursive/iterative outline, about 10 min | AL06's one formal peer-review block: 30 min presentations/code/questions + 10-15 min Schoology writing; remaining 75-80 min for AL07 paired memoization/evidence and packaging, subject to rehearsal | Correctness parity, before/after calls/cache entries, fresh-cache rule, strategy limits |

Coin change and Fibonacci are different investigations, not competing solutions to one task. Broad independent DP design, PageRank, linear-programming implementation, and mandatory stretch work are not introduced.

### Week 6: Models, Traversals, and Restricted Paths

Keywords: node/edge, direction, adjacency, cycle, visited/frontier, BFS/DFS, parent, path, restriction, model limit. Primary categories: T2/T3/T4/T5. AL08 uses paired traversal/path development with a self-selected collaboration pilot and individual model/adaptation evidence. Partners rotate per assignment.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W06D01 | Define edge meaning and directionality; validate adjacency references; identify cycles/disconnection and omitted real-world details | DEM-W06D01: campus graph model | AL08 individual access-network model; use a common supplied implementation fixture afterward | Graph/text representation, reference checks, justified assumptions and omissions |
| W06D02 | Explain queue/stack frontier and visited-state behavior; implement BFS and iterative DFS; reason about termination and introductory O(V+E) | DEM-W06D02: campus BFS/DFS frontiers | AL08 self-selected pair/trio traversal implementation with reproducible neighbor order and individual checks | Small frontier/visited traces, cycle/coverage tests, individual traversal explanation |
| W06D03 | Reconstruct a BFS path using parents; handle start=goal/no path; apply restrictions; distinguish fewest hops from weighted distance/time | DEM-W06D03: restricted campus routes; explain multi-value `--blocked` input. Additional APP-M6: Navigator relationships, about 10 min | Shared AL08 path baseline, then individual restriction response and tests | Valid path/restriction evidence, no-path cases, model-limit explanation |

Bound the model to approximately 10-15 nodes. Use three pairs and one active trio for nine students, with role rotation and instructor-supported regrouping. Self-selection does not guarantee faster completion. Weighted shortest-path implementation is outside required scope.

### Week 7: Explainable Ranking and Limited Integrity Evidence

Keywords: features/tags, overlap, normalization, Jaccard, top-k, weight, deterministic tie, sensitivity, coverage, digest. Primary categories: T2/T3/T4/T5/T6; shared AL09 evidence plus individual limitations and assistance disclosure.

| Session | Lecture Intent / Learning Result | Daily Demo and Additional Recognition | Lab Transfer / Ownership | Observable Evidence |
| --- | --- | --- | --- | --- |
| W07D01 | Compare shared-tag counts and Jaccard on the same representation; define empty/missing/self-match policies and hand-check scores | DEM-W07D01: song similarity | AL09 paired baseline on an assigned, reviewed resource subset/profile different from the Navigator demo | Independent score checks, representation policy, baseline ranking evidence |
| W07D02 | Produce deterministic top-k results; explain feature contributions and one normalized weighted revision; investigate changed preferences | DEM-W07D02: weighted song ranking; explain `--emphasis` choices | AL09 paired weighted revision and ranking investigation; clustering is optional orientation, not a competing task | Weighted formula/default/zero cases, ties, matched features, changed/unchanged ranks |
| W07D03 | Demonstrate coverage/bias or missing-data limits; distinguish lookup hashing, canonical snapshot digest, encryption, and authenticity | DEM-W07D03: playlist integrity and limits. Additional APP-M7: full Navigator recognition, about 10 min | AL09 bounded sensitivity/integrity investigation using supplied serialization helper; individual limitation explanation | Concrete ranking limitation, before/after local digest, qualified claims and individual disclosure |

Provide the chosen scoring formulas and integrity helper. Students do not research dozens of URLs, reproduce the full Navigator, implement cryptographic algorithms, or train clustering models. A correct score or matching digest is not evidence of recommendation quality or source authenticity.

### Week 8: Synthesis and Individual Assessment

Keywords: evidence, correctness, efficiency, readability, assumption, limitation, explanation, adaptation. Use previously taught concepts only; no AL10 or additional application build.

| Session | Instructional / Assessment Intent | Demo or Assessment | Ownership and Activity | Observable Evidence |
| --- | --- | --- | --- | --- |
| W08D01 | Evaluate a claim, compare valid approaches, explain a limitation, and adapt one unfamiliar requirement using established concepts | DEM-W08D01: equipment-selection synthesis, up to 20 min. Additional APP-SYN: basic-to-full recognition, about 10 min | Formative individual prediction, guided discussion and rehearsal; remaining Monday time supports preparation | Qualified judgment, revised expectations, explanation; not another graded weekly assignment |
| W08D02 | Apply taught framing, representation, implementation, testing, and evidence skills to bounded unfamiliar tasks | FINAL-P1: full 180-min assessment meeting; briefing only, no solution demo | Individual applied solution set; publish allowed references/tools and equivalent variants | Student-owned code/tests/evidence, assumptions, assistance disclosure |
| W08D03 | Verify individual understanding and adapt a submitted solution to a small changed requirement | FINAL-P2: full 180-min personalized explanation/adaptation meeting; no new lecture | Individual work based on Part 1; no generative AI; written/interactive work with targeted oral follow-up to be scheduled | Walkthrough, edge-case reasoning, tradeoffs, justified adaptation, ownership evidence |

Part 1 retains a proposed 15-minute briefing, 150-minute work block, and 15-minute submission check. Task count/volume must be calibrated before publication, not accepted because planned durations sum correctly. Part 2 appointment lengths and independent work volume remain to be specified; nine serial 20-minute defenses leave no transition margin. The earlier final-only 70/30 split is a recommendation, not a newly adopted course-grade policy.

## Week 1 Production Timing Template

This is a lecture/lab pacing scaffold, not a completed lecture outline or slide script. Monday's readiness check is brief and uses familiar Python; setup material is already released and does not require rebuilding PreCourse_Setup before teaching begins.

| Session | Instruction Segments | Lab Segments | Total |
| --- | --- | --- | ---: |
| W01D01 | 5 min readiness/reading retrieval; 13 min contracts/representations; 16 min daily walkthrough; 7 min APP-M0; 9 min interpretation and AL01 handoff | 10 min pair setup/intent; 40 min paired baseline/checks; 15 min support/testing; 5 min checkpoint | 50 + 70 = 120 min |
| W01D02 | 5 min retrieval; 15 min predicates/test categories; 18 min daily demo; 10 min guided expected/actual practice; 12 min lab/pairing preparation | 10 min paired case predictions; 45 min paired filter/test work; 5 min checkpoint; 45 min paired repair/regression; 15 min individual README notes/close | 60 + 120 = 180 min |
| W01D03 | 5 min retrieval; 15 min changed rules versus refactor; 18 min daily demo; 10 min APP-M1; 12 min interpretation/handoff | 10 min paired change prediction; 45 min paired revision/regression; 5 min checkpoint; 45 min paired refinement/checks; 15 min individual copy/README/packaging | 60 + 120 = 180 min |

AL01 uses one shared application with driver/navigator rotation about every 20 minutes. Each student submits a complete copy through their own class-repo URL in Schoology, with individual README notes. Nine students use three pairs and an active trio. Questions and checking are normal paired work; the single formal review occurs in AL06, Week 5. Students independently schedule Zoom if additional joint time is needed.

AL01 uses a coverage checklist for ordinary, boundary, invalid, empty/no-match, grouped-condition, and preserved-behavior cases; no fixed check count or duplicate evidence table is required. Supply fixtures and a lightweight test scaffold, not a completed ticket filter. In demo code, extensive assertions remain in `test_demo.py`; explain a focused assertion there when revisiting prior exposure. Application-facing output remains readable.

Week 1 demos, AL01 packet/support/solution, and pairing/submission guides are created; pre-rehearsal code/document checks pass. Generate the three daily outlines/decks against the current baseline, then prepare student distribution. Actual rehearsal is the instructor's later task. Confirm the existing MRS framework first; finalize the AL01 mapping after its packet is complete. The course-wide mapping follows later assignments, not a mandatory bulk rubric rewrite before production. W01D01's menu/walkthrough, short docstrings, and screen-sharing colors form the current demonstration model, not a requirement to add menus to every later demo.

## Collaboration, Tooling, and Assessment Guardrails

| Area | Instructional Intent | Boundary |
| --- | --- | --- |
| Brief intent | State intended behavior and independently reason about expectations | No formal pseudocode, three-case pre-code gate, or complete manual implementation requirement in AL01 |
| Designated collaboration | Use substantive questions, rotating roles, tests, and justified responses in breakout rooms | No fixed speedup; shared code does not prove individual understanding; additional joint work uses independently scheduled Zoom sessions |
| Individual tasks | Preserve individual development in AL04, AL05, AL06, and the final | AL06 alone includes a formal presentation/code review with short Schoology posts and separate grading; no duplicate scoring |
| Bounded AI collaboration | Permit explanation, drafting, debugging, and refactoring within each packet's rules; review and test contributions | Student intent, understanding, and verification remain assessed; individual checks use no generative AI |
| Final tool boundaries | Publish references and assistance permissions before assessment | Part 1 permissions remain to be finalized; Part 2 uses no generative AI. Weekly permissions do not automatically carry into the final |
| Observable evidence | Match traces, comparisons, state diagrams, or tables to a concrete claim | User output is not a technical trace; a useful report does not replace independently justified correctness evidence |
| Python enhancement | Purpose docstrings and separate tests from Week 1; explicit argparse introduction in W02D02, selective reuse in W05D03/W06D03/W07D02 | New supporting Python concepts are explained in bounded segments, not silently inserted or required in every demo |
| Reference app | Recognize useful integration through distinct APP-M0-M7/APP-SYN runs | LRN is not the student project or a solution demonstration for graded tasks; no JS/MVT expansion this weekend |
| Rubric alignment | Retain T1-T6 and C1-C6 identifiers and existing descriptors; choose rows for observable task evidence | Confirm the framework before assignment drafting; finalize each mapping with its completed packet and before publication. The course-wide matrix follows actual assignments; this IIM sets no new points, category weights, or course percentages |

Technical category intent: T1 framing/analysis; T2 representation; T3 implementation/testing; T4 correctness/efficiency/tradeoffs; T5 observable evidence; T6 AI/data foundations and responsible tool use. Core abilities remain C1 problem solving, C2 communication, C3 productive work, C4 learning/revision, C5 designated cooperation, and C6 professionalism/accountability.

## Remaining Production Work

- Confirm MRS-AL's existing framework without a bulk rewrite. Finalize AL01's mapping with its completed packet before release; regenerate the AL01-AL09/FINAL-P1/P2 matrix as the remaining assignments are developed, rather than reuse the old seven-lab mapping unchanged.
- Week 1 demos, fixture/scaffold, instructor solution, and collaboration/submission guides are created and checked. Generate outlines/decks; prepare student distribution. Instructor rehearsal remains pending.
- Carry instructor-confirmed section boundaries into student reading instructions without reopening optional-reference curation or claiming independent textbook verification.
- Specify assignment releases/cutoffs, homework allowances, permitted tools, and final-assessment timing; do not convert provisional planning splits into high-stakes deadlines.
- Review later demos for human-readable problem-solving output and instructional fit; implementation/tests alone are not classroom acceptance.
- Prepare selective optional conceptual support: full AL06/AL08 walkthroughs, short AL04 scaffold, AL07 prompts, and AL03 only if needed. Create AL06's Schoology review form/rubric and verify Week 5 timing.
- Produce the dedicated APP-SYN recognition run and rehearse milestone demonstrations inside existing instruction time.
- Update already-released PreCourse_Setup only where necessary; this is lower priority than Monday-ready instruction and assessment materials.

This IIM is the new instructor working spine. It does not claim institutional approval, measured workload fit, completed rubric revision, regenerated outlines/decks, or automatic acceptance of all runnable demos.
