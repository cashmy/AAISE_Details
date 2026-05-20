# Introduction to Algorithms High-Level Course Plan v2

## Course

`10-152-119` - `Introduction to Algorithms`

Credits: `TBD`  
Lecture/Lab: `TBD`  
Prerequisite: `10-152-117 Python Programming`

## Source Description

Learners develop algorithmic thinking by analyzing problems, selecting solution
strategies, implementing algorithms in Python, evaluating correctness and
efficiency, and comparing tradeoffs between approaches. The course emphasizes
Big-O reasoning, core data structures, searching, sorting, graph thinking,
strategy selection, and explainability. Students also receive selected exposure
to algorithms that support later AI, data analytics, and data-modeling work,
including similarity, clustering, recommendation, hashing, and algorithmic
ethics. The selected textbook provides broad reference coverage, while the
course itself focuses on a curated subset appropriate for the bridge sequence.

## Planning Position

This course should function as the bridge sequence's algorithmic judgment
course. It is less about producing one kind of software artifact and more about
helping students choose, test, compare, and explain solution strategies.

The central movement is:

```text
problem framing -> correctness -> data structures -> efficiency -> strategy
comparison -> visual/tangible algorithm behavior -> AI/data bridge concepts
```

Students should leave the course with practical intuition for questions such as:

- What problem am I actually solving?
- What are the inputs, outputs, constraints, and assumptions?
- What data structure makes this easier or harder?
- Does the solution work for edge cases?
- How does the solution behave as input grows?
- Is the simpler solution good enough?
- What does an AI-generated solution assume, hide, or get wrong?
- How do I explain the tradeoff to another developer or stakeholder?

The textbook should be used as a reference spine rather than a coverage
contract. Students should learn how to use it as a long-term reference book,
while the course selects the chapters and topics most relevant to first-year
algorithmic reasoning and downstream AI/data preparation.

## AI Use Progression

The course should use the program's broader AI involvement model, but it does
not need to reach the same endpoint as every other course.

```text
Manual First -> AI-Assisted -> AI-Injected -> AI-Integrated
```

For this course:

- Manual First means students frame the problem, identify assumptions, trace
  logic, and attempt a solution strategy before relying on tooling.
- AI-Assisted means AI may support explanation, research, vocabulary, examples,
  or critique after the student has established their own understanding.
- AI-Injected means AI may help produce or revise code, but students must
  justify, test, explain, and adapt the output.
- AI-Integrated means AI becomes a refraction-based collaborator inside a larger
  structured development process. This is optional for this course and should
  only appear if a final applied task has enough structure for students to
  preserve authorship and accountability.

The typical target for `10-152-119` is regular movement through Manual First,
AI-Assisted, and selected AI-Injected work. AI-Integrated practice may be named
or lightly previewed, but it is not required as a course-wide expectation.

## Delivery Frame

This plan assumes an 8-week compressed course, pending final confirmation of
credits and lecture/lab distribution.

Because the course is conceptually dense, each week should combine:

- short conceptual framing
- worked examples
- Python implementation
- visual or tangible demonstration where useful
- comparison of approaches
- explanation and reflection

The course should not be web-based by default. Visual/tangible learning can come
from console traces, tables, timing measurements, simple charts, notebooks,
grid-based simulations, graph diagrams, search/sort animations, or lightweight
visual outputs.

## Relationship to Concurrent and Later Courses

This course follows `10-152-117 Python Programming` and should assume students
have basic exposure to:

- variables, expressions, conditionals, loops, functions, lists, and
  dictionaries
- file and structured data basics
- debugging and explanation
- bounded AI-assisted development

It should coordinate with `10-152-118 HTML/CSS/JavaScript` by reinforcing that
visible behavior rests on underlying structure and logic, but it should not
become a browser-development course.

The course prepares students for:

- `10-152-120 Database Query and Design`, by building data-structure,
  search/filter, sorting, grouping, and scale intuition
- `10-152-121 Advanced Python Systems`, by strengthening Python-based
  implementation, testing, data handling, and performance reasoning
- `10-152-123 Modern Data Modeling for Systems`, by introducing representation,
  similarity, graph, ranking, hashing, and tradeoff thinking
- later AI and analytics courses, by previewing similarity, clustering,
  classification logic, text/data representation, recommendation, explainability,
  and bias

## High-Level Time Allocation

Suggested emphasis:

```text
20% problem framing, correctness, testing, assumptions, and explanation
20% Big-O, growth intuition, timing, and performance comparison
20% data structures: lists, dictionaries, sets, stacks, queues, trees, graphs
15% searching, sorting, recursion/iteration, and strategy comparison
10% visual/tangible labs that make algorithm behavior observable
10% AI/data bridge topics: similarity, clustering, recommendation, hashing,
    text/data representation, and explainability
5% AI-assisted comparison, critique, and adaptation
```

## 8-Week Draft Structure

The course is organized into four phases:

```text
Weeks 1-2 -> Algorithmic Foundations and Correctness
Weeks 3-4 -> Data Structures, Search, Sort, and Growth
Weeks 5-6 -> Strategy Patterns and Visual/Tangible Behavior
Weeks 7-8 -> AI/Data Bridges, Tradeoffs, and Explanation
```

### Week 1 - Algorithms, Precision, and Correctness

Purpose: establish what algorithms are and why precision, assumptions, and
correctness matter before efficiency is discussed.

Topics:

- What an algorithm is
- Inputs, outputs, constraints, and assumptions
- Ambiguity versus precision
- Manual tracing and pseudocode
- Correctness through test cases and edge cases

Lab direction:

- Write precise instructions or pseudocode for a simple task
- Translate a small algorithm into Python
- Test normal and edge cases
- Compare human-written and AI-generated instructions for hidden assumptions

### Week 2 - Big-O and Growth Intuition

Purpose: help students see how solutions behave as data grows.

Topics:

- Time and space intuition
- Constant, linear, quadratic, and logarithmic growth
- Best, worst, and average case at a beginner level
- Timing experiments versus theoretical reasoning
- Simplicity, readability, and performance tradeoffs

Lab direction:

- Run small timing comparisons in Python
- Generate a simple table or chart of growth behavior
- Explain why a solution that feels fine for 10 items may fail for 10,000
- Use Big-O as vocabulary for comparison, not as abstract math alone

### Week 3 - Data Structures for Algorithmic Thinking

Purpose: show how data representation shapes what algorithms can do efficiently
and clearly.

Topics:

- Lists, dictionaries, and sets
- Stacks and queues
- Introductory trees and graphs
- Lookup, insertion, traversal, and ordering intuition
- Choosing structures based on access patterns

Lab direction:

- Solve the same small problem with different data structures
- Compare lookup and membership behavior
- Use stacks or queues in a concrete scenario
- Draw or visualize structure where helpful

### Week 4 - Searching and Sorting

Purpose: connect classic algorithms to preconditions, correctness, and scale.

Topics:

- Linear search
- Binary search and sorted-data preconditions
- Simple sorts such as selection, insertion, or bubble sort
- Merge sort or another divide-and-conquer sort as a contrast
- Choosing when to implement, call a library, or explain an algorithm

Lab direction:

- Implement and compare linear and binary search
- Demonstrate how binary search fails when assumptions are violated
- Visualize a simple sort step by step
- Compare manual implementation with Python's built-in capabilities

### Week 5 - Recursion, Iteration, and Strategy Patterns

Purpose: introduce common algorithmic strategies without overloading students
with advanced theory.

Topics:

- Recursion and base cases
- Iterative alternatives
- Brute force
- Divide and conquer
- Greedy strategy
- Dynamic programming as recognition-level or light applied exposure

Lab direction:

- Solve a small problem recursively and iteratively
- Compare brute force with a more structured strategy
- Identify when greedy approaches work and when they fail
- Use visual traces for recursive calls or decision paths

### Week 6 - Graphs, Paths, and Models of Real Systems

Purpose: show students that algorithms often model relationships, movement,
workflow, or networks.

Topics:

- Graph vocabulary: nodes, edges, paths, directed/undirected relationships
- Adjacency lists or simple graph representation
- Breadth-first search
- Depth-first search
- Shortest-path intuition at an introductory level
- Real-world modeling examples

Lab direction:

- Model a grid, navigation problem, workflow, or simple network
- Visualize traversal order or path discovery
- Compare BFS and DFS behavior
- Explain what the graph representation includes and leaves out

### Week 7 - Similarity, Clustering, Recommendation, and Hashing

Purpose: create a bridge from algorithms into AI, analytics, and data modeling.

Topics:

- Similarity and distance as algorithmic ideas
- Euclidean, Manhattan, or cosine similarity at an intuitive level
- Clustering as grouping similar items
- Recommendation as similarity/ranking
- Hashing for lookup, identity, integrity, or security awareness

Lab direction:

- Compare items using a simple distance or similarity measure
- Visualize clustered points or grouped records
- Build a small recommendation/ranking example
- Demonstrate hashing as stable identity or integrity check

### Week 8 - Tradeoffs, Explainability, and Final Assessment

Purpose: consolidate the course around judgment, communication, responsible use
of algorithms and AI-assisted solutions, and the two-part final assessment.

Topics:

- Correctness versus efficiency versus readability
- Explainability and traceability
- Bias, bad assumptions, and misleading evidence
- When not to use an algorithm
- Evaluating AI-generated algorithmic solutions
- Communicating algorithmic choices

Synthesis/final direction:

- Use one compact lecture-demo to rehearse comparison, evidence, assumptions,
  limitations, and AI accountability
- Reserve the last two class days for the final:
  - Part 1 - Applied Solution Set
  - Part 2 - Personalized Explanation Defense
- Avoid assigning a full additional Week 8 lab

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Define algorithmic problems in terms of inputs, outputs, constraints, and
  assumptions.
- Represent solution logic using pseudocode, diagrams, or Python.
- Test algorithms for correctness using normal cases, edge cases, and expected
  outcomes.
- Explain Big-O growth at an introductory level and compare common complexity
  classes.
- Select basic data structures based on the needs of a problem.
- Implement and compare introductory searching, sorting, recursion/iteration,
  and graph traversal algorithms.
- Use visual or tangible evidence to explain algorithm behavior.
- Recognize how similarity, clustering, recommendation, hashing, and
  representation support later AI, analytics, and data-modeling work.
- Compare manual, library-supported, and AI-assisted solutions for correctness,
  readability, efficiency, assumptions, and maintainability.
- Communicate algorithmic tradeoffs clearly to technical and non-technical
  audiences.

## Notes for Future Detailed Design

- Confirm credits, hours, and exact delivery frame before finalizing weekly
  density.
- Build a textbook coverage map that clearly distinguishes required reading,
  guided reading, optional reference, and deferred material.
- Use Section 1 of the textbook as the main spine.
- Cherry-pick Sections 2 and 3 only where they support AI, analytics,
  data-modeling, security-awareness, or explainability foundations.
- Avoid turning this into a machine-learning course. ML topics should be
  conceptual bridges and small visual examples, not full model-training units.
- Avoid making the course web-based by default. Use visual outputs when they
  reveal algorithm behavior.
- Keep Python as the primary implementation language.
- Preserve AI accountability, but do not make every lab an equal-weight
  AI-versus-manual comparison. Use AI where comparison, critique, or assumption
  testing adds instructional value.
- Use the program AI progression consistently: Manual First, AI-Assisted,
  AI-Injected, and optional AI-Integrated. For this course, Manual First and
  AI-Assisted should be routine, AI-Injected should be selective and justified,
  and AI-Integrated should remain optional or preview-level.
- Replace inherited HTML/CSS/JavaScript lecture outlines with new v2 algorithm
  outlines only after the v2 week structure is stable.
