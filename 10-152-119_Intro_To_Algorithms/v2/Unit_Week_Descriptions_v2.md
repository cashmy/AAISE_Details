# Unit and Week Descriptions v2

## Purpose

This artifact provides the student-facing phase/unit structure for
`10-152-119 Introduction to Algorithms`.

The course should feel consistent with the broader bridge curriculum while still
respecting the distinctive role of algorithms: students are not mainly building
one product type; they are learning how to choose, test, compare, and explain
solution strategies.

Each unit description should help students understand what kind of difficulty
they are entering and why it matters.

## Unit 1 - Algorithmic Foundations and Correctness

Weeks: `1-2`

In this unit, you will learn how to describe problems clearly, turn problem
statements into step-by-step logic, and check whether a solution actually works.
You will also begin learning how algorithms change as the amount of data grows.

The goal is to move from "I can write code" toward "I can explain what problem
my code is solving, why it works, and how it behaves as the input changes."

### Week 1 - Algorithms, Precision, and Correctness

This week introduces algorithms as precise instructions for solving problems.
You will practice defining inputs, outputs, constraints, and assumptions before
implementation.

The goal is to understand that unclear thinking produces unreliable solutions,
even when the code runs.

### Week 2 - Big-O and Growth Intuition

This week introduces performance reasoning. You will compare how different
solutions behave as inputs grow and begin using Big-O vocabulary to describe
growth patterns.

The goal is not advanced math. The goal is to recognize why a solution that
works for small inputs may not work well at larger scale.

## Unit 2 - Data Structures, Search, Sort, and Growth

Weeks: `3-4`

In this unit, you will learn how data organization affects the solutions
available to you. You will work with common structures and classic searching and
sorting problems to see how assumptions, representation, and scale shape
algorithmic choices.

The goal is to understand that choosing a solution also means choosing how data
will be stored, accessed, compared, and changed.

### Week 3 - Data Structures for Algorithmic Thinking

This week focuses on structures such as lists, dictionaries, sets, stacks,
queues, trees, and graphs at an introductory level.

The goal is to learn that data structures are not just syntax; they shape what
your program can do clearly and efficiently.

### Week 4 - Searching and Sorting

This week uses searching and sorting to make algorithmic assumptions visible.
You will compare simple and more efficient approaches and learn why conditions
such as "the data is sorted" matter.

The goal is to connect correctness, preconditions, and performance in concrete
examples.

## Unit 3 - Strategy Patterns and Observable Behavior

Weeks: `5-6`

In this unit, you will compare different ways to approach problems. You will
work with recursion, iteration, brute force, divide-and-conquer, greedy
strategies, and graph traversal. Labs should make algorithm behavior visible
through traces, diagrams, grids, charts, or other tangible evidence.

The goal is to see algorithms as choices, not recipes.

### Week 5 - Recursion, Iteration, and Strategy Patterns

This week introduces common strategy patterns. You will compare recursive and
iterative thinking and examine when a direct solution should be replaced by a
more structured approach.

The goal is to explain not only what solution works, but why that strategy fits
the problem.

### Week 6 - Graphs, Paths, and Models of Real Systems

This week uses graphs to model relationships, movement, workflows, or networks.
You will compare traversal approaches such as breadth-first search and
depth-first search.

The goal is to recognize that many real systems can be represented as connected
parts, and that the representation changes what questions are easy to answer.

## Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation

Weeks: `7-8`

In this unit, you will connect algorithmic thinking to later work in AI, data
analytics, data modeling, and software systems. You will examine similarity,
clustering, recommendation, hashing, explainability, bias, and tradeoffs.

The goal is to leave the course able to make and explain algorithmic decisions,
not merely recognize algorithm names.

### Week 7 - Similarity, Clustering, Recommendation, and Hashing

This week introduces selected AI and data-facing algorithms. You will see how
systems can compare items, group records, rank options, and use hashing for
identity, lookup, or integrity.

The goal is to understand the algorithmic ideas underneath later AI and data
systems without turning this course into a machine-learning course.

### Week 8 - Tradeoffs, Explainability, and Final Assessment

This week pulls the course together around judgment and final demonstration of
learning. You will review how to compare possible solutions, evaluate
assumptions, explain tradeoffs, and consider when an algorithm or AI-generated
solution may be misleading.

The first class session should be used for synthesis, demo, and final
preparation. The last two class sessions should be allocated to the two-part
final assessment: the Applied Solution Set and the Personalized Explanation
Defense.

The goal is to submit working algorithmic solutions with evidence and then
explain your own work clearly.

## Student-Facing Throughline

Across the course, students move through this progression:

```text
define the problem clearly
-> verify that a solution works
-> understand how data structure affects the solution
-> compare solution strategies
-> observe algorithm behavior
-> connect algorithms to AI/data systems
-> explain tradeoffs responsibly
```

The most important outcome is algorithmic judgment: the ability to choose,
test, compare, and explain a solution strategy.
