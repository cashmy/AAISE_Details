# Instructional Intent Matrix v2

## Purpose

This matrix translates the `10-152-119 Introduction to Algorithms v2` unit
structure into an instructor-facing weekly plan.

It uses the compressed-course pattern from `10-152-117 Python Programming` as
the primary model: longer live sessions, direct concept framing, guided lab
movement, and refinement work. This course does not include a required
video/asynchronous lecture component in the IIM.

## Matrix

| Wk | Unit / Week Theme | Mon Concept / Demo | Tue Lab / Guided Practice | Thu Lab / Refinement | Instructor Keywords | AI Integration | Tooling Layer | Tooling Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Unit 1 - Algorithmic Foundations and Correctness | Mode: precision, correctness, and growth intuition before strategy complexity |  |  |  |  |  |  |
| 1 | Algorithms, Precision, and Correctness | Establish algorithms as precise problem-solving procedures; define inputs, outputs, constraints, assumptions, and expected outcomes; distinguish ambiguity from precision through small examples | Translate a small problem into pseudocode and Python; create normal and edge-case tests | Revise a flawed or ambiguous algorithm; compare human and AI-generated instructions for hidden assumptions | algorithm, input, output, constraint, assumption, edge case, pseudocode, correctness | Manual First -> AI-Assisted | Native Python + optional AI explainer | AI may interpret or critique instructions, but students frame the problem first |
| 2 | Big-O and Growth Intuition | Introduce time/space intuition, input growth, and constant/linear/quadratic/logarithmic patterns; frame Big-O as comparison vocabulary rather than exact timing | Run timing experiments with increasing input sizes; record results in a table | Create or inspect a simple chart/table of growth behavior; explain why small-input success may not scale | Big-O, growth, time complexity, space complexity, scale, timing, performance | Manual First -> AI-Assisted | Native Python + table/chart output | AI can help explain timing patterns after students collect evidence |
|  | Unit 2 - Data Structures, Search, Sort, and Growth | Mode: representation choices and classic algorithm behavior |  |  |  |  |  |  |
| 3 | Data Structures for Algorithmic Thinking | Frame data structures as choices that shape access, lookup, traversal, and clarity; connect lists, dictionaries, sets, stacks, queues, trees, and graphs to access patterns | Solve the same problem using two structures, such as list vs dictionary or stack vs queue | Compare structure diagrams and evidence; explain which representation fits which problem | list, dictionary, set, stack, queue, tree, graph, lookup, traversal, representation | Manual First -> AI-Assisted | Native Python structures | AI can suggest alternate representations, but students justify the structure choice |
| 4 | Searching and Sorting | Introduce linear search, binary search, sorted-data preconditions, sorting as scale comparison, and the difference between learning implementations and library use | Implement and compare linear and binary search; demonstrate binary search failure when assumptions are violated | Trace or visualize a simple sort; compare manual implementation with Python built-ins | linear search, binary search, sorted data, precondition, sort, library, assumption | Manual First -> AI-Assisted -> selective AI-Injected | Native Python + optional AI code critique | AI may generate an alternate implementation only after students create or trace one |
|  | Unit 3 - Strategy Patterns and Observable Behavior | Mode: compare strategies and make algorithm behavior visible |  |  |  |  |  |  |
| 5 | Recursion, Iteration, and Strategy Patterns | Introduce recursion/base cases, iteration, brute force, divide and conquer, greedy strategy, and dynamic programming as recognition patterns; contrast simple success with strategy fit | Solve a small problem using two strategies; trace recursive or decision behavior | Compare correctness, readability, and growth; identify when a greedy approach fails | recursion, base case, iteration, brute force, divide and conquer, greedy, dynamic programming | AI-Assisted -> selective AI-Injected | Native Python + traces/diagrams | AI can propose an alternate strategy after manual framing; generated code requires justification |
| 6 | Graphs, Paths, and Models of Real Systems | Introduce graphs as models of relationships, movement, networks, and workflows; define graph vocabulary, BFS, DFS, traversal order, and path intuition | Model a grid, workflow, or relationship network; represent it with an adjacency list | Visualize traversal order or path discovery; compare BFS and DFS behavior | node, edge, graph, adjacency list, BFS, DFS, traversal, path, model | AI-Assisted | Native Python + visual/tangible diagram | AI may critique graph representation or explain traversal, not replace the model |
|  | Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation | Mode: connect algorithms to AI/data foundations and responsible decision-making |  |  |  |  |  |  |
| 7 | Similarity, Clustering, Recommendation, and Hashing | Introduce similarity/distance, clustering, recommendation, hashing, and representation as AI/data foundations; distinguish hashing from encryption | Build a small similarity, clustering, ranking, or hashing activity with visible evidence | Compare outputs and assumptions; explain what the algorithm can and cannot claim | similarity, distance, clustering, recommendation, ranking, hashing, representation | AI-Assisted -> selective AI-Injected | Native Python + chart/table/diagram; optional notebook | AI can help compare or generate a small variant, but students validate assumptions and explain the idea |
| 8 | Tradeoffs, Explainability, and Final Assessment | Pull together correctness, efficiency, readability, assumptions, bias, explainability, responsible AI/tool use, and communication of tradeoffs through a compact synthesis demo | Final Part 1 - Applied Solution Set; students complete bounded algorithmic tasks with evidence | Final Part 2 - Personalized Explanation Defense; students explain submitted work, assumptions, evidence, limitations, and AI use if applicable | tradeoff, explainability, bias, validation, assumption, evidence, stakeholder explanation | AI-Assisted -> AI-Injected; AI-Integrated optional/preview | All approved course layers | Week 8 uses one synthesis/demo day followed by two final assessment days |

## AI Progression Summary

```text
Weeks 1-2 -> Manual First with AI-Assisted explanation or critique
Weeks 3-4 -> Manual First plus AI-Assisted representation/code critique
Weeks 5-6 -> AI-Assisted with selective AI-Injected alternatives
Weeks 7-8 -> AI-Injected where justified; AI-Integrated optional or preview-level
```

## Tooling Progression Summary

```text
Native Python first
-> tables, traces, charts, and diagrams for visible evidence
-> optional notebook or lightweight visualization when it clarifies behavior
-> AI only after student framing, evidence, or implementation exists
```
