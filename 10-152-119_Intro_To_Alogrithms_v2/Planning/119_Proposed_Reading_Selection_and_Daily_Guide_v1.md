# 119 Proposed Reading Selection and Daily Guide

Status: Instructor review draft v1, October 8, 2026.

Source: `Textbook_Coverage_and_Reference_Map_v2.md`, summarizing *50 Algorithms Every Programmer Should Know*, 2nd edition, Imran Ahmad.

Alignment update, October 9, 2026: [Textbook Coverage and Reference Map v3](119_Textbook_Coverage_and_Reference_Map_v3.md) is the current coverage proposal for this refactor. It preserves this guide's Monday-main/Tuesday-Thursday-optional reading pattern and incorporates the later demo/assignment scope promotions. The original v1 selections and wording below remain a planning baseline, not regenerated exact readings.

This proposal extracts the chapter/topic information from the coverage map into a Monday/Tuesday/Thursday reading and instructional structure. It is a planning guide, not a verified page-level student reading list. Topic descriptions below are selection targets, not quoted textbook section headings. Exact headings, page ranges, and code-example suitability require checking against the actual textbook before publication.

## 1. Proposed Reading Pattern

Assign one main reading selection before Monday. It introduces the week's concepts and vocabulary, including a preview of ideas that will receive deeper treatment on Tuesday and Thursday. Monday does not need to teach every concept in that selection.

Provide optional supporting/reference selections for Tuesday and Thursday. These can revisit a passage, explain a second approach, or offer enrichment. Students should be able to complete required work through the main reading, instruction, prepared demos, and supplied lab resources without completing optional readings.

| Day | Reading expectation | Instructional purpose |
| --- | --- | --- |
| Monday: 2 hours combined lecture/lab | Main selected reading before class | Establish the week's problem, vocabulary, representations, and initial approach |
| Tuesday: 1 hour lecture + 2 hours lab | Optional supporting selection or targeted rereading | Deepen implementation, trace behavior, test assumptions, and compare approaches |
| Thursday: 1 hour lecture + 2 hours lab | Optional reference or targeted rereading | Apply changed requirements, investigate tradeoffs, refactor, and explain evidence |

Suggested main-reading target: 45-60 minutes most weeks; up to 75 minutes for a carefully bounded, example-heavy selection in Weeks 3-5. Week 8 uses a shorter synthesis selection. Optional supporting reading should normally take 10-20 minutes per day and should never imply reading a whole additional chapter.

These are proposed time budgets, not measured textbook reading times. They expand the earlier rescope draft's 30-45 minute preparation estimate. When selecting exact pages, include reading, tracing examples, and brief preparation within the target rather than allocating the entire budget to prose alone. Check the effect on the overall outside-class workload before adopting longer selections.

Use a brief prediction or question as preparation, not an additional substantial written assignment. Reading code means tracing and explaining it; it does not automatically mean reproducing every implementation.

## 2. Extracted Chapter Selection Inventory

This inventory preserves the source map's distinction between core fundamentals, guided bridge material, optional reference, and deferred content. The Monday assignments proposed later select portions of these categories; they do not assign entire chapters.

| Chapter / title in source map | Useful selection targets | Proposed role |
| --- | --- | --- |
| 1. Overview of Algorithms | Algorithm characteristics; design techniques; selection/validation; performance; time/space; best/worst/average cases; Big-O; explainability | Main readings for Weeks 1-2; targeted reuse later |
| 2. Data Structures Used in Algorithms | Lists/dictionaries/sets; operation costs; stacks/queues; introductory trees and graph representation | Main Week 3 reading; representation references in Weeks 6-7 |
| 3. Sorting and Searching Algorithms | Linear/binary search; sorted-data preconditions; one simple sort; merge-sort contrast; algorithm choice | Main Week 4 reading and supporting references |
| 4. Designing Algorithms | Correctness/performance/scalability; brute force; divide and conquer; greedy; dynamic programming recognition; strategy comparison | Selected main Week 5 reading; support in Weeks 4 and 8 |
| 5. Graph Algorithms | Vocabulary; directed/undirected relationships; adjacency lists; BFS/DFS; paths and traversal | Selected main Week 6 reading |
| 6. Unsupervised Machine Learning Algorithms | Similarity/distance; Euclidean/Manhattan distance; cosine recognition; grouping/clustering; k-means intuition | Small Week 7 main selection and optional clustering reference |
| 7. Traditional Supervised Learning Algorithms | Explainable decision-tree branching; classification/regression vocabulary | Optional Week 7 enrichment only |
| 8. Neural Network Algorithms | Neural networks and training | Deferred |
| 9. Algorithms for Natural Language Processing | Cleaning/tokenization; text-to-number representation; term-document/TF-IDF concepts | Optional Week 7 representation reference |
| 10. Understanding Sequential Models | RNN/GRU/LSTM and sequence training | Deferred |
| 11. Advanced Sequential Modeling Algorithms | Attention, transformers, LLM internals | Deferred |
| 12. Recommendation Engines | Similarity; ranking; content-based recommendation; collaborative-filtering recognition | Small Week 7 main selection; optional Week 6 bridge |
| 13. Algorithmic Strategies for Data Handling | Representation/storage/speed tradeoffs; compression; optional Huffman example | Optional Week 3 or Week 7 enrichment |
| 14. Cryptography | Hashing, identity/integrity, hash choice, distinction from encryption | Optional Week 7 Thursday reference; concepts taught in class |
| 15. Large-Scale Algorithms | Scale changes decisions; future distributed-processing context | Optional orientation in Weeks 2 and 8; detailed implementation deferred |
| 16. Practical Considerations | Explainability; ethics/bias; traceability; misleading evidence; limits; when to use algorithms | Main Week 8 selection; optional support in Weeks 1 and 7 |

For Chapters 4-6, 12, and 16, assigning a small selected passage as Monday preparation is a proposed scheduling choice. It does not promote every guided topic in those chapters to required implementation depth.

## 3. Weekly Selection and Daily Lecture Guide

The daily topics are proposals derived from the source map and the three-day schedule. They should guide the next IIM revision, practical demo design, assignment mapping, and lecture-material reuse review. They are not regenerated lecture outlines.

### Week 1: Algorithms, Precision, and Correctness

**Monday main selection:** Chapter 1 material on algorithm characteristics, representing a solution, selecting/validating an approach, and explainability. Emphasize precise steps, problem boundaries, and expected results. Leave detailed performance analysis and Big-O for Week 2.

**Reading target:** 45-60 minutes including one small example trace.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | From a problem statement to precise inputs, outputs, assumptions, and algorithmic steps | Chapter 1 selection above; read for the logic and validation of a solution | Main assigned selection |
| Tuesday | Correctness, expected outcomes, boundary cases, and failure diagnosis | Reread Chapter 1's selected validation discussion; use instructor test examples where the map provides no specific textbook treatment | Optional support |
| Thursday | Revision, explainability, limits of a working solution | Chapter 16 selected discussion of traceability, explainability, and limits | Optional reference |

Preparation prompt: What assumption could make a seemingly correct set of instructions fail?

Demo/application direction: a rule-based decision, a defective validator, then a changed rule. Existing Lab 1 can become a baseline followed by testing and revision. One staged assignment is a natural fit.

### Week 2: Big-O, Growth, and Measurement

**Monday main selection:** Chapter 1 material on performance analysis, time/space complexity, common growth patterns, Big-O, and best/worst/average cases. Use small examples to connect input size to work performed. Distinguish introductory growth reasoning from formal proofs.

**Reading target:** 45-60 minutes including comparing two growth examples.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Counting work; constant, linear, quadratic, and logarithmic growth | Chapter 1 performance/Big-O selection above | Main assigned selection |
| Tuesday | Experimental evidence: timing, operation counts, and unfair comparisons | Targeted rereading of Chapter 1 performance analysis; instructor benchmark notes supply experimental details not established by the map | Optional support |
| Thursday | Workload-dependent choices, preprocessing cost, memory, and scale | Chapter 1 selection/complexity reread; a short Chapter 15 orientation passage only if useful | Optional reference |

Preparation prompt: Which approach grows faster, and what work are you counting?

Demo/application direction: repeated scanning versus indexed lookup, an unreliable benchmark, then a changed query workload. Expand existing Lab 2 into a controlled investigation and interpretation task. Keep distributed computing out of required reading.

### Week 3: Data Structures and Representation

**Monday main selection:** Chapter 2 selected material on lists, dictionaries, sets, common operation costs, stacks, and queues. Read familiar Python syntax quickly; focus on access patterns, identity, membership, ordering, and state. Include only a brief preview of tree and graph representations.

**Reading target:** 60-75 minutes, with one comparison table or state trace. Trim repeated syntax examples when confirming exact sections.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Choosing list/dictionary/set representations by task and operation | Chapter 2 core structures and operation-cost selection | Main assigned selection |
| Tuesday | Stack/queue behavior, FIFO/LIFO, and state transitions | Chapter 2 stack/queue examples, reread as needed | Optional support |
| Thursday | Representation consistency; hierarchies versus general relationships | Chapter 2 introductory trees/graph representation; Chapter 13 representation/storage tradeoffs as enrichment | Optional reference |

Preparation prompt: Which structure fits lookup by ID, duplicate detection, and processing in arrival order, and why?

Demo/application direction: record lookup, a service queue/undo stack, then conflicting or stale state. Existing Lab 3 can be one evolving workflow or two linked tasks: structure comparison followed by queue/stack application. DataFrames and full compression implementations remain optional.

### Week 4: Searching, Sorting, and Preconditions

**Monday main selection:** Chapter 3 selected linear search, binary search, sorted-data preconditions, one simple sorting algorithm, and algorithm-selection discussion. Recommend insertion sort as the implementation target. Include a short merge-sort overview for divide-and-conquer recognition rather than all its implementation details.

**Reading target:** 60-75 minutes including a search trace and a few sorting steps.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Linear/binary search, narrowing the search space, and correctness preconditions | Chapter 3 search selections above | Main assigned selection |
| Tuesday | Simple sorting behavior, comparisons/moves, library operations, divide-and-conquer contrast | Chapter 3 chosen simple sort and merge-sort overview, reread as needed | Optional support |
| Thursday | End-to-end cost: sorting first, repeated queries, and choosing an approach | Chapter 3 algorithm-choice discussion; Chapter 4 selected correctness/performance/scalability discussion | Optional reference |

Preparation prompt: What must be true before binary search is a valid choice?

Demo/application direction: sorted/unsorted search, insertion-sort traces, then sort-once/search-many comparison. Existing Lab 4 can become one catalog investigation or separate connected search and sort/comparison assignments. Shell sort, interpolation search, and implementing every sort remain optional.

### Week 5: Algorithm Design and Strategy Comparison

**Monday main selection:** Chapter 4 selected correctness/performance/scalability, brute force, divide and conquer, greedy strategy, and strategy-comparison material. Give dynamic programming only a brief recognition preview. Prioritize one worked example per selected strategy rather than large framework-dependent examples.

**Reading target:** 60-75 minutes including comparison of two approaches.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Recursive/iterative reasoning, base cases, decomposition, and divide-and-conquer | Chapter 4 selected design/decomposition material; instructor recursion/iteration companion where textbook coverage is not established by the map | Main assigned selection plus supplied companion if needed |
| Tuesday | Brute force versus greedy choices; proving a claim with a counterexample | Chapter 4 selected brute-force/greedy examples, reread as needed | Optional support |
| Thursday | Repeated subproblems, memoization/DP recognition, and strategy tradeoffs | Chapter 4 small DP example; Chapter 1 validation/selection reread | Optional reference |

Preparation prompt: What evidence would challenge a claim that a locally best choice always produces the best overall answer?

Demo/application direction: nested-data recursion/iteration, a greedy counterexample, then repeated-work comparison. Existing Lab 5 may support two linked assignments: recursive/iterative implementation and a scaffolded strategy investigation. Recursion is part of the proposed instruction, but the source map does not identify an exact recursion section; verify or supply that reading explicitly. Complexity classes such as NP-completeness, PageRank, linear programming, and Spark are not required selections.

### Week 6: Graphs, Traversal, and Paths

**Monday main selection:** Chapter 5 selected graph vocabulary, nodes/edges, directed/undirected relationships, adjacency lists, BFS, DFS, and path/traversal intuition. Preview both traversals; students need not master their implementations before Monday.

**Reading target:** 45-60 minutes including drawing a small graph and predicting traversal behavior.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Modeling a real system as a graph and choosing a representation | Chapter 5 vocabulary/representation selection above | Main assigned selection |
| Tuesday | BFS/DFS frontier behavior, visited-state tracking, and cycles | Chapter 5 BFS/DFS examples, reread as needed | Optional support |
| Thursday | Traversal versus route discovery; path reconstruction; shortest-hop and model limits | Chapter 5 path/traversal material; Chapter 12 relationship/recommendation context only if a suitable passage is verified | Optional reference |

Preparation prompt: What relationships does your graph represent, and which real-world details does it omit?

Demo/application direction: a campus/workflow graph, queue/stack traversal traces, then route reconstruction and changed restrictions. Extend existing Lab 6 through modeling, traversal, and revision. Provide instructor path-reconstruction guidance if the selected book treatment does not supply it. Centrality, fraud analytics, and full weighted-path algorithms stay outside the required selection.

### Week 7: Similarity, Recommendation, and Hashing

**Monday main selection:** A tightly curated combination of Chapter 6 similarity/distance concepts and Chapter 12 similarity, ranking, and content-based recommendation. Emphasize representation and an explainable score. Introduce clustering only as grouping related items; reserve detailed examples for optional support.

**Reading target:** 45-60 minutes total across both chapters, not 45-60 minutes per chapter. Choose one primary worked example and trim duplicated explanations.

| Day | Potential lecture focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Representing items/features and defining similarity | Small Chapter 6 + Chapter 12 combined selection above | Main assigned selection |
| Tuesday | Ranking, explanation, sensitivity to features, and a clustering preview | Chapter 12 ranking/content-based example; Chapter 6 grouping/k-means intuition as enrichment | Optional support |
| Thursday | Assumptions, coverage/bias, and identity/integrity versus similarity | Chapter 14 selected hashing/encryption distinction; Chapter 16 bias/explainability discussion | Optional reference |

Preparation prompt: How could a change in representation change which recommendation appears best?

Demo/application direction: item similarity, a ranking that changes with representation, then an integrity check and limitations. Existing Lab 7 can become a common ranking task with revision, or a ranking assignment plus a short hashing investigation. Teach the required hashing concepts and library usage in class; optional Chapter 14 reading cannot be a hidden prerequisite.

The map supports general similarity and ranking topics; it does not verify a textbook section for shared-tag/Jaccard scoring, deterministic tie handling, or canonical digest serialization. These are candidate instructor examples and may need supplied companion notes. Chapter 7 decision-tree logic, Chapter 9 text representation, and Chapter 13 data handling remain a future-reference menu, not additional expected reading that week.

### Week 8: Practical Considerations and Final Synthesis

**Monday main selection:** Chapter 16 selected explainability, traceability, misleading evidence, bias, limits of algorithms, and when an algorithm is appropriate. Connect the reading to examples students already implemented.

**Reading target:** 30-45 minutes including reflection on one previous lab's evidence.

| Day | Potential lecture / assessment focus | Reading selection / guide | Status |
| --- | --- | --- | --- |
| Monday | Evidence-based judgment, assumptions, limitations, and final rehearsal | Chapter 16 selection above | Main assigned synthesis selection |
| Tuesday | Final Part 1: applied solution set | Previously used Chapters 1-5 and 12 as permitted references under the final's published rules | Optional review; no new reading |
| Thursday | Final Part 2: explanation and adaptation | Student's submitted code/evidence and previously taught concepts; references subject to the final's published rules | Optional preparation; no new reading |

Preparation prompt: Which claim in your previous work is supported by evidence, and which needs a qualification?

Demo/application direction: Monday synthesis comparison and explanation rehearsal. Tuesday/Thursday remain assessment sessions rather than new content lectures. Chapter 4 strategy comparison and Chapter 15 scale orientation may be available for voluntary reference, but neither introduces new assessed material in the final week.

## 4. Keeping Optional Reading Optional

- Every required concept introduced on Tuesday/Thursday must be explained through instruction, a prepared practical demo, and sufficient lab resources.
- Do not assess an optional passage's terminology or implementation unless it has also been taught as core content.
- Label optional passages by purpose: revisit an explanation, support an implementation, or explore beyond the required depth.
- Choose a small useful reference for a specific question; avoid presenting a large list as an implied expectation.
- Provide companion notes where the coverage map does not establish the needed textbook treatment, especially testing/benchmark mechanics, recursion, path reconstruction, and chosen ranking/hash details.
- Distinguish required learning from required independent implementation. A guided trace can establish recognition without assigning a full algorithm build.

## 5. How This Guide Informs the Refactor

Use the proposed daily progression to revise the IIM at session level. The chapter summaries supply candidate content; actual competencies, contact time, and student readiness determine its selected depth. Do not reuse the old weekly reading allocations without testing them against the three-session structure.

For each accepted session, identify at least one prepared demo showing a practical use of its core concept. Then map existing assignments to that progression and decide whether one staged assignment or two connected assignments best support the week. Preserve substantive iteration, refactoring, changed requirements, and comparison as valid assessed work.

Audit the existing outlines/deck sources alongside this mapping for reusable explanations, worked examples, diagrams, and questions. Regenerate outlines only after the reading/topic/demo/assignment relationships are accepted.

| Next planning artifact | Information supplied by this guide | Remaining work |
| --- | --- | --- |
| Revised IIM | Three daily instructional purposes per week | Confirm outcomes, timing, and competency evidence |
| Exact reading list | Chapter/topic selection targets, main/optional status, time budgets | Verify headings/pages against the textbook and sample the reading workload |
| Demo map | Practical progression for each week | Select/adapt existing demos and specify each daily packet |
| Assignment map | Candidate iteration/refactor and one/two assignment patterns | Review existing requirements and allocate substantive work to each lab |
| Lecture reuse audit | Daily topics and depth boundaries | Retain/adapt/relocate/retire current material |
| Regenerated outlines | Accepted content relationships | Produce session-level outlines and later revise decks |

## 6. Evaluation Points

The proposed main-reading spine is Chapter 1 across Weeks 1-2, Chapter 2 in Week 3, Chapter 3 in Week 4, selected Chapter 4 in Week 5, selected Chapter 5 in Week 6, small combined Chapters 6/12 selections in Week 7, and selected Chapter 16 in Week 8.

Evaluate the following before moving to exact selections and the revised IIM:

1. Whether the Monday selections introduce enough of each week's concepts to support all three teaching days.
2. Whether the 45-75 minute preparation range fits the cohort and concurrent coursework; trim exact sections rather than simply increase homework.
3. Whether Week 7's similarity/recommendation focus and optional hashing reference provide the desired downstream bridge.
4. Whether the guided strategy/graph readings need short instructor companions for the selected practical examples.
5. Whether one evolving assignment or two connected assignments better fit each accepted weekly progression.

This draft leaves the source coverage map, existing IIM, reading allocations, assignments, and lecture content unchanged. It does not reopen the already explained institutional-versus-scheduled hours difference.
