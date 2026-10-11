# 119 Textbook Coverage and Reference Map v3

Instructor review draft | October 9, 2026

Textbook: *50 Algorithms Every Programmer Should Know*, 2nd edition, Imran Ahmad.

Course: 10-152-119 Introduction to Algorithms, current refactor under `10-152-119_Intro_To_Alogrithms_v2`.

## 1. Purpose and Version Authority

This revision retains the original map's whole-book reference value while aligning selected coverage with the three-day schedule, stronger application depth, independent daily demos, assignment progression, and separate Learning Resource Navigator (LRN) recognition milestones.

It replaces the [original v2 coverage map](../../10-152-119_Intro_To_Algorithms/v2/Textbook_Coverage_and_Reference_Map_v2.md) as the working coverage proposal for this refactor. The original file remains unchanged. Version v3 denotes this document's revision, not a third course refactor.

Alignment sources:

- [Reading Selection and Daily Guide](119_Proposed_Reading_Selection_and_Daily_Guide_v1.md): Monday main selections, optional Tuesday/Thursday support, and preparation budgets.
- [Daily Lecture Topic List](119_Daily_Lecture_Topic_List_Review_Draft_v1.md): initial session-level sequence and depth limits.
- [Cohort Readiness and Scope Review](119_Cohort_Readiness_and_Scope_Adjustment_Review_v1.md): stronger filtering, modularity, experiment ownership, memoization, and weighted-score practice.
- [Demo and Reference-App Map](119_Demo_List_and_Reference_App_Milestones_v1.md) and [implemented daily demo index](../Demos/README.md): current practical instruction.
- [Assignment Progression](119_Assignment_List_and_Progression_Map_v1.md): nine regular assignments, selective collaboration, individual evidence, and the two-part final.
- [LRN Implementation Status](119_LRN_Full_Version_Implementation_Status_v1.md): separate full app and independent M0-M7 snapshots.

The earlier reading/topic/rescope drafts predate selected scope promotions. For this map, the later demo/assignment plans establish bounded memoization practice and weighted-score revision as core application, not optional-only extensions. This does not imply that every earlier document has already been regenerated or that instructor acceptance is complete.

**Source verification boundary:** Chapter titles and topic inventory are inherited from the original coverage summary, not newly checked against the full textbook. Topic descriptions are selection targets, not verbatim section headings. Exact headings, page ranges, edition-specific examples, and actual reading times remain unverified. No textbook passage is claimed to supply a particular demo implementation unless checked later.

## 2. Schedule, Readiness, and Coverage Labels

| Meeting | Actual Allocation | Reading Expectation |
| --- | --- | --- |
| Monday | 2 hours combined lecture/lab | Main selected reading before class |
| Tuesday | 1 hour lecture + 2 hours lab | Optional targeted rereading or support |
| Thursday | 1 hour lecture + 2 hours lab | Optional reference, rereading, or enrichment |

There are 24 meeting slots: 22 teaching sessions and two final-assessment sessions. Week 8 Tuesday/Thursday are assessments, not new content lectures. The documented institutional-versus-scheduled hours difference is understood and is not reopened as a design blocker.

Students have completed Python Foundations and are progressing through Web Foundations, including modularity, asynchronous JS, collections, decisions, and loops. Prior capstones showed filtering, architectural thinking, and useful peer questions. Assume familiar programming syntax; explicitly teach new algorithmic reasoning. These observations justify deeper application, not an assumption that every student already understands complexity, recursion, graphs, or similarity.

Python remains primary, with occasional optional JS comparisons. No Django/MVT, ML-training stack, live API, or UI framework is a prerequisite.

### Two Independent Dimensions

| Reading Status | Meaning |
| --- | --- |
| Main selection | Assigned bounded preparation before Monday; not a whole chapter by default |
| Optional support | Targeted Tuesday/Thursday rereading or companion passage; not needed to meet required outcomes |
| Optional enrichment | A voluntary extension beyond current course depth |
| Deferred | Future reference; no required reading or independent implementation |

| Instructional Depth | Meaning |
| --- | --- |
| Core | Teach, practice, and assess within the stated boundary |
| Guided | Worked trace, supplied reference, scaffold, or supported comparison; independent full implementation is not implied |
| Preview | Brief vocabulary or orientation only |
| Outside core | Optional enrichment or deferred material |

A main reading can introduce guided/preview concepts without making their full implementation required. Conversely, core instruction can use optional textbook support when required explanations, demos, and lab resources are supplied in class.

Preparation targets remain estimates: 45-60 minutes in most weeks; 60-75 in Weeks 3-5; 30-45 in Week 8. Include tracing/preparation within those totals. Optional support normally takes 10-20 minutes per day, not another chapter. These selections fit within the proposed regular-week total outside-class allowance of approximately 1-2 hours; two-assignment weeks do not double that allowance. Pilot and trim before adding workload.

## 3. Weekly Reading and Application Spine

| Week | Main Monday Selection Targets | Tue/Thu Optional Textbook Support | Required Application / Evidence | Main Reading Target |
| --- | --- | --- | --- | --- |
| 1 | Ch. 1: algorithm characteristics, problem boundaries, solution representation, selection/validation, explainability | Tue: Ch. 1 validation revisit. Thu: small Ch. 16 explainability/limits passage | Structured contracts, predicate/combined filtering, purposeful tests, rule revision, regression, modular responsibilities | 45-60 min |
| 2 | Ch. 1: performance, input size, time/space, Big-O, common growth, best/worst/average cases | Tue: performance revisit. Thu: selection/complexity revisit; Ch. 15 scale orientation only if useful | Owned count/prediction, equivalent algorithms, controlled measurement, setup/query/end-to-end evidence, two workload recommendations | 45-60 min |
| 3 | Ch. 2: lists/dictionaries/sets, operation costs, stacks/queues; brief hierarchy/network preview | Tue: stacks/queues revisit. Thu: introductory relationship representations; Ch. 13 tradeoffs as enrichment | Identity/membership choices, deque FIFO, bounded LIFO undo, consistency invariant, updates/cancellation, snapshot semantics | 60-75 min |
| 4 | Ch. 3: linear/binary search, preconditions, insertion sort, algorithm choice; short merge-sort contrast | Tue: selected sort/search examples. Thu: Ch. 3 choices; Ch. 4 correctness/performance/scalability | Student-owned search and stable insertion sort; record keys/ties; composed filter/order/search; total-cost and changed-requirement evidence | 60-75 min |
| 5 | Ch. 4: design/decomposition, correctness/performance/scalability, brute force, greedy, divide-and-conquer, small DP orientation; supplied recursion companion where needed | Tue: brute-force/greedy revisit. Thu: small repeated-subproblem/DP passage; Ch. 1 validation revisit | Recursive/explicit-stack parity; greedy counterexample against supplied exhaustive reference; scaffolded memoization modification and fresh-cache call evidence | 60-75 min total, including any assigned companion |
| 6 | Ch. 5: graph vocabulary, directionality, adjacency lists, BFS/DFS, paths/traversal | Tue: traversal examples. Thu: paths/traversal revisit; Ch. 12 relationship context only if a suitable passage is verified | Model justification, reference validation, BFS/iterative DFS, visited/frontier traces, BFS path reconstruction, restriction revision | 45-60 min |
| 7 | Small combined Ch. 6/12 selection: representation, similarity/distance, ranking, content-based recommendation; clustering only a brief orientation | Tue: Ch. 12 example; Ch. 6 clustering enrichment. Thu: selected Ch. 14 digest/encryption distinctions and Ch. 16 limitations | Shared-tag/Jaccard comparison, deterministic top-k, bounded weighted revision, matched-feature explanations, concrete sensitivity/coverage limitation, library digest interpretation | 45-60 min total across both chapters |
| 8 | Ch. 16: explainability, traceability, evidence, bias, assumptions, limits, appropriateness | Previously taught passages under published final rules; Ch. 4 review if useful. No new Tue/Thu reading | Monday synthesis/rehearsal; individual applied final and personalized explanation/adaptation | 30-45 min |

Reading prepares vocabulary and conceptual connections. Stronger assignment depth comes from implementation, comparison, revision, and explanation, not assigning more chapters.

## 4. Daily Textbook-to-Practice Map

`D01` = Monday; `D02` = Tuesday; `D03` = Thursday. `DEM-*` identifies a standalone daily demo. `APP-*` identifies additional LRN recognition, not the daily demo. Assignment IDs link conceptually to the [assignment map](119_Assignment_List_and_Progression_Map_v1.md); packets/weights remain future work.

| Session | Selected Focus / Textbook Support | Daily Practical Demo | Student Transfer |
| --- | --- | --- | --- |
| W01D01 | Problem contracts, precise steps, validation/rules/output boundaries; main Ch. 1 | DEM-W01D01: equipment request contract | AL01: individual ticket contract/baseline |
| W01D02 | Predicate filtering, normal/boundary/invalid cases, failure diagnosis; optional Ch. 1 revisit plus supplied testing guidance | DEM-W01D02: filter boundaries | AL01: filters/tests and paired review |
| W01D03 | Combined criteria, changed rules versus refactoring, regression/explanation; optional Ch. 16 | DEM-W01D03: combined criteria | AL01: revision and individual evidence; separate APP-M1 |
| W02D01 | Input size, counts, common growth, time/space; main Ch. 1 | DEM-W02D01: lookup growth | AL02: individual prediction and paired baseline |
| W02D02 | Fair inputs, repeated measurement, parity, setup/query boundaries; optional Ch. 1 plus supplied harness guidance | DEM-W02D02: benchmark controls | AL02: controlled experiment |
| W02D03 | Few/many queries, hit/miss effects, preprocessing and memory; optional Ch. 1/15 | DEM-W02D03: workload tradeoffs | AL02: changed workload and individual conclusion; APP-M2 |
| W03D01 | Lists/dictionaries/sets, stable identity, membership, filtered views; main Ch. 2 | DEM-W03D01: inventory representations | AL03: structure choices/contracts |
| W03D02 | FIFO/LIFO, deque, one reversible state change, empty states; optional Ch. 2 | DEM-W03D02: checkout queue and undo | AL03: processing/undo/state tests |
| W03D03 | Invariants, stale entries, cancellation, snapshots; hierarchy/network preview; optional Ch. 2/13 plus supplied state guidance | DEM-W03D03: state consistency | AL03: adaptation and individual explanation; APP-M3 |
| W04D01 | Linear/binary search, matching keys, empty/singleton/endpoints, duplicate-result policy; main Ch. 3 | DEM-W04D01: search preconditions | AL04: individual search implementations/evidence |
| W04D02 | Stable insertion sort, record keys/ties, comparisons/moves, library comparison; guided merge contrast; optional Ch. 3 | DEM-W04D02: stable record sorting | Finish AL04 checkpoint; AL05 sort baseline/review |
| W04D03 | Filter/order/search data flow, display/search views, reused setup, total cost; optional Ch. 3/4 | DEM-W04D03: query pipeline | AL05: pipeline/change/evidence; APP-M4 |
| W05D01 | Base cases, recursive state, explicit-stack alternative, decomposition; main Ch. 4 plus verified/supplied recursion support | DEM-W05D01: nested donation totals | AL06: individual nested expense aggregation |
| W05D02 | Greedy objective/assumptions, bounded exhaustive reference, optimality counterexample; optional Ch. 4 | DEM-W05D02: greedy counterexample | Finish AL06 checkpoint; AL07 greedy investigation |
| W05D03 | Repeated subproblems, bounded memoization modification, fresh-cache calls/storage, strategy choice; optional Ch. 4/1 plus supplied recurrence | DEM-W05D03: memoization call counts | AL07: recurrence evidence/individual explanation; APP-M5 reinforces outlines, not coin/Fibonacci |
| W06D01 | Graph meaning, directionality, adjacency validation, cycles/disconnection, omissions; main Ch. 5 | DEM-W06D01: campus graph model | AL08: individual access-network model |
| W06D02 | Queue/stack frontier, visited state, termination, introductory O(V+E); optional Ch. 5 | DEM-W06D02: BFS/DFS frontiers | AL08: paired traversal and individual trace explanation |
| W06D03 | Parent tracking, BFS shortest hops, no-path/start=goal, restrictions, weighted-cost limits; optional Ch. 5 plus supplied path guidance | DEM-W06D03: restricted routes | AL08: individual restriction response; APP-M6 |
| W07D01 | Features/tags, shared-count versus normalized overlap, empty/missing data, hand-checks; main Ch. 6/12 plus supplied scoring notes | DEM-W07D01: song similarity | AL09: assigned resource subset/profile, baseline scores |
| W07D02 | Top-k/ties, weights/defaults, score contributions, changed ranks; optional Ch. 12; clustering enrichment only | DEM-W07D02: weighted song ranking | AL09: bounded weighted revision/explanations |
| W07D03 | Coverage/bias, hash-table hashing versus digest, canonical metadata, digest versus encryption/authenticity; optional Ch. 14/16 plus supplied integrity helper | DEM-W07D03: playlist integrity and limits | AL09: concrete limitation/digest evidence; APP-M7 |
| W08D01 | Correctness/efficiency/readability, misleading claims, evidence, unfamiliar change; main Ch. 16 | DEM-W08D01: equipment selection synthesis | Formative rehearsal; separate APP-SYN recognition planned |
| W08D02 | Previously taught concepts under published final rules; no new reading/lecture | ASSESS-W08D02: no solution demo | FINAL-P1: individual applied solution set |
| W08D03 | Explanation, evidence, tradeoffs, adaptation; no new reading/lecture | ASSESS-W08D03: personalized prompts, no solution demo | FINAL-P2: individual defense/adaptation |

W01D01 also has a short APP-M0 introduction after the daily demo. Weekly APP-M1 through APP-M7 recognition is normally Thursday, approximately ten minutes within the existing teaching period. M0-M7 code exists separately; APP-SYN's dedicated recognition packet remains to be produced.

## 5. Whole-Book Coverage and Reference Inventory

This retains the original summary's breadth. Inventory entries describe reference opportunities, not assigned sections or claims of verified page-level coverage.

| Chapter | Inherited Topic / Reference Inventory | Current Course Selection and Boundary |
| --- | --- | --- |
| 1. Overview of Algorithms | Algorithm characteristics/design; performance, time/space, best/worst/average case, Big-O; selection/validation; exact/approximate/randomized approaches; explainability | Main selections W1-2. Core precision, correctness/evidence and applied growth. Exact/approximate/randomized approaches are recognition only; no formal proof unit. Revisit validation W5/8 as needed. |
| 2. Data Structures Used in Algorithms | Python types, lists, dictionaries, sets, tuples, common operation costs, stacks/queues, introductory trees/graphs; Series/DataFrames, matrices, vectors | Main W3. Core task-driven structures and bounded state operations, not syntax reteaching. Trees/graphs are previews before W6. Tuples are contrast; DataFrames/matrices/vectors are optional orientation, not an added analytics unit. |
| 3. Sorting and Searching Algorithms | Linear/binary search; selection/insertion/bubble/merge sorts; choices/preconditions; shell sort and interpolation search | Main W4. Core linear/binary search, stable insertion sort, key-based library comparison, composition. Merge sort is guided contrast. Other sorts/searches and full implementation of every method are outside core. |
| 4. Designing Algorithms | Correctness/performance/scalability; brute force, divide and conquer, greedy, DP, strategy comparison; P/NP/NP-complete/NP-hard; PageRank, linear programming, Spark example | Main selected W5; optional W4/8 support. Core recursive/iterative comparison, greedy investigation, bounded scaffolded memoization and judgment. General DP design remains guided/optional. Exact recursion/memoization passages need verification or companions. Complexity classes and named advanced applications remain optional/deferred. |
| 5. Graph Algorithms | Nodes/edges, directed/undirected relationships, adjacency representation, BFS/DFS, paths/traversal; centrality, social-network analysis, density, fraud case study | Main selected W6. Core small model, BFS/iterative DFS, cycle handling, unweighted BFS path/restrictions. Advanced analytics and weighted-path implementation are outside core. |
| 6. Unsupervised Machine Learning Algorithms | Similarity/distance; Euclidean/Manhattan/cosine; clustering, k-means, hierarchical clustering/DBSCAN; data-mining lifecycle, PCA, association rules, Apriori/FP-growth | Small main W7 selection with Ch. 12. Core representation/similarity transfer; chosen tag scoring is instructor-supplied unless verified. Numeric metrics/grouping are recognition or optional enrichment; clustering implementations, model training, PCA, and association-rule implementations are outside core. |
| 7. Traditional Supervised Learning Algorithms | Decision trees, classification/regression, confusion matrix/precision/recall; XGBoost, random forests, logistic regression, SVM, naive Bayes, weather example | Optional future-reference menu only. No scheduled core ML task or extra W7 reading. At most an explainable-branching preview if it does not displace required instruction. |
| 8. Neural Network Algorithms | Perceptrons, activations/training, Keras/TensorFlow, CNNs, GANs, transfer learning | Deferred. No neural-network implementation or training prerequisite. |
| 9. Algorithms for Natural Language Processing | Cleaning/tokenization, text-to-number representation, term-document/TF-IDF concepts; Word2Vec, sentiment analysis, pipelines | Optional representation reference only. No full NLP pipeline or required vectorization build. |
| 10. Understanding Sequential Models | RNNs, GRUs, LSTMs, sequence training | Deferred to later AI/ML work. |
| 11. Advanced Sequential Modeling Algorithms | Autoencoders, Seq2Seq, attention/self-attention, transformers, LLM internals | Deferred. Explainability/evaluation in 119 does not require teaching model architecture. |
| 12. Recommendation Engines | Similarity, ranking, content-based recommendation, collaborative-filtering vocabulary; movie recommender, similarity-matrix workflow, feedback/retraining | Small main W7 selection with Ch. 6. Core explainable scoring/ranking/sensitivity, not the book's full recommender. Optional W6 relationship context only after passage verification. Collaborative filtering remains recognition; full matrix/retraining workflows are outside core. |
| 13. Algorithmic Strategies for Data Handling | Representation/storage/speed tradeoffs, compression, Huffman coding; CAP, distributed storage, AWS, LZ77/advanced compression | Optional W3/W7 reference; not required compression implementation. Distributed/storage/cloud depth is deferred. |
| 14. Cryptography | Hashing, hash choice, integrity and encryption distinctions; ciphers, symmetric/asymmetric cryptography, TLS/PKI, blockchain, MITM defenses | Optional W7 Thursday support for core, library-based local integrity instruction. Dictionary hashing is taught with structures, not equated to cryptographic digests. Full security implementations are deferred. |
| 15. Large-Scale Algorithms | Scale-dependent decisions, Amdahl's law, cloud/distributed context; load balancing, CUDA/GPU, Spark/distributed computing | Optional orientation W2/8 only. No distributed/cloud/GPU implementation, extra framework, or final-week new requirement. |
| 16. Practical Considerations | Explainability, ethics/bias, traceability, misleading evidence/unfair outcomes, limits and appropriateness | Main selected W8; optional support W1/W7. Core evidence-backed critique of work students have already implemented, not abstract discussion detached from cases. |

### Updated Required-Depth Decisions

- **Week 1:** Raise application level through structured records, filtering, contracts, testing, and revision; do not turn Chapter 1 into remedial Python.
- **Week 2:** Students own predictions, counted operations, cases, confound identification, and workload interpretation. Supplied harnesses do not supply their conclusions.
- **Week 3:** Identity, state invariants, cancellation, and snapshot semantics deepen familiar collections; no general undo engine or full tree build.
- **Week 4:** Search and stable insertion sort remain substantive core. Keep merge sort guided and lower-bound search optional.
- **Week 5:** Bounded scaffolded memoization modification is core practice. Broad DP remains outside independent required design. Coin change and Fibonacci illustrate different problems, not competing solutions to one task.
- **Week 6:** BFS/DFS and unweighted path/restriction work are core, not merely a visual preview. Keep model and graph size small.
- **Week 7:** Weighted-feature revision is core. Clustering is optional preview/enrichment rather than a competing required unit. A correct score or digest does not establish recommendation quality or source authenticity.
- **Week 8:** Synthesis only; no substantial new algorithm, graded AL10, or hidden optional-reading requirement in the final.

## 6. Instructor Companions and Textbook Gaps

These are explicit course support needs, not newly asserted textbook content. Runnable demos exist, but student-facing companions and exact passage selections still require preparation/review. Git-ignored instructor notes are not a substitute for student-accessible required explanations.

| Gap / Companion | Session(s) | Supply or Verify |
| --- | --- | --- |
| Structured contracts, predicate/combined filtering, validation/rules/output separation | W01D01-D03 | Small record examples, expected behavior, invalid/missing-data policy, rule-change versus refactor distinction |
| Purposeful tests and regression evidence | W01D02-D03; recurring | Lightweight harness, boundary/failure examples, independently justified expected outcomes |
| Fair timing, counts, setup/query/end-to-end cost | W02D01-D03; W04D03 | Supplied measurement plumbing, reproducible inputs, units, expected average-case qualifications; no claimed universal measured winner |
| State invariants, saved snapshots, stale references, restoration | W03D01-D03 | Operation contracts, action traces, one bounded undo and consistency checks |
| Record keys, stable ties, duplicate-search semantics, distinct display/search views | W04D01-D03 | Worked record cases and pipeline contracts beyond generic numeric sort/search examples |
| Recursion/base cases and explicit-stack equivalence | W05D01 | Verify exact textbook treatment or supply a concise companion counted within Monday preparation |
| Greedy/reference counterexample and instrumented memoization | W05D02-D03 | Supplied bounded exhaustive reference; recurrence/counter scaffold; fresh-cache rules. No need to assign a second chapter |
| BFS parent tracking, route restrictions, reproducible neighbor order | W06D02-D03 | Path reconstruction guidance, cycle/disconnection cases, edge meaning and hop-versus-cost limitation |
| Shared-tag/Jaccard and normalized weighted scoring | W07D01-D02 | Formula, sets/union, defaults, nonnegative weights, empty/zero cases, top-k/ties and matched-feature explanations; exact textbook match unverified |
| Canonical metadata serialization and digest interpretation | W07D03 | Supplied serialization helper and standard-library usage; distinguish lookup hashes, digests, encryption, authenticity, fairness and source correctness |
| Evidence-backed adaptation and tool-use disclosure | Recurring; W08 | Short explanation models, concrete claim/limitation checks, final rules published before assessment |

Optional Tuesday/Thursday reading stays optional even when a required concept is introduced that day. Teach it and provide the needed resources without assuming the optional passage was read.

## 7. Demo, Assignment, and Reference-App Boundaries

The 22 daily demos use independent equipment, donation, recurrence, campus, and music contexts. The separate LRN uses real resource links and proposed teaching metadata. It demonstrates useful iterative integration; students are not required to build that full app.

The proposed assessed structure is nine regular assignments: AL01-03 in Weeks 1-3; AL04/05 in Week 4; AL06/07 in Week 5; AL08 in Week 6; AL09 in Week 7; then FINAL-P1/P2. Connected assignments have fresh entry fixtures/recovery scaffolds rather than an unavoidable course-long dependency.

Completion requires meaningful correctness evidence and a comparison, changed requirement, or substantive refactor where specified. Collaboration remains selective: do not impose paired programming or peer-review evidence on AL04, AL06, or the individual final. Paired/hybrid work retains each student's explanation and clearly identified authorship; remote partner activity fits breakout-room lab time.

LRN recognition follows APP-M0/M1 in Week 1 and APP-M2 through APP-M7 in Weeks 2-7, with Week 8 basic-to-full recognition planned separately. It does not replace the daily demo or expose a graded success solution.

Two distinctions are especially important:

- Daily stable insertion sorting demonstrates preservation of equal-key input order. LRN M4 display ordering uses explicit ID tie-breaks; it is not the same stability evidence.
- LRN M5 demonstrates recursive/explicit-stack outlines. It need not incorporate the week's coin-change or memoization example to reinforce a useful concept.

Optional JS demonstrates familiar cross-language connections, preserving separate HTML/CSS/JS layers. The full JS app remains future work with an approved UI brief and Design Contract update required first; its UI is not textbook coverage or a new 119 prerequisite.

## 8. Publication and Refactor Checklist

- [ ] Confirm this map's selected coverage/depth and the nine-assignment progression with the instructor.
- [ ] Verify edition-specific headings, pages, examples, and errata against the actual textbook; no page numbers are approved by this map.
- [ ] Select exact Monday passages within the stated total preparation budgets; reduce duplicated W7 material.
- [ ] Mark every Tue/Thu passage as optional support or enrichment; remove hidden prerequisites.
- [ ] Prepare/review the student-facing companions listed above; validate their teaching fit against the implemented demos.
- [ ] Pilot reading and lab completion time, support needs, and individual explanation quality before declaring workload adequate.
- [ ] Update the early reading guide/daily topic list and rescope/IIM drafts to carry the adopted scope promotions consistently.
- [ ] Audit existing outlines/decks for retain/adapt/relocate/retire decisions, then regenerate daily outlines against accepted sessions.
- [ ] Produce assignment packets, final-assessment guides/rules, and the selective paired-programming student guide.
- [ ] Rehearse the separate app recognition runs within their time budget and prepare APP-SYN without adding final-week content.

This is an instructor-facing coverage proposal, not the published student reading list, a regenerated IIM, an LMS packet, or an assertion that the entire textbook is assigned. Original course materials and code remain unchanged by this document refactor.
