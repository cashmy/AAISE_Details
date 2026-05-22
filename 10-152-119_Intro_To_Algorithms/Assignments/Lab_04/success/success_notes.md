# LAB 04 SUCCESS NOTES - SEARCH AND SORT BEHAVIOR

This package shows one acceptable successful version for Lab 04. It is not the
only correct answer because the student-facing lab allows multiple data sets.

---

# Assumptions

- fresh `Assignments/Lab_04/` package
- student-facing Lab 04 treated as authoritative
- generic starter rather than scenario-specific scaffolding
- demo scenario different from the withheld success-version scenario
- search trace tables and a sorted-vs-unsorted comparison used as the visible
  evidence
- primary success version kept plain and focused; no optional colorized success
  variant added here

---

# Chosen Data Set

Course codes

The successful version uses:

- a sorted course-code list for valid binary search
- an unsorted course-code list to demonstrate binary search failure conditions

This keeps the success version in the same concept family as the lab while
staying different from the book-title demo.

---

# Problem Statement

Implement linear search and binary search on a course-code data set, then show
how binary search depends on sorted data.

The successful version includes four required tests, trace evidence, and a
short explanation of the sorted-data precondition.

---

# Inputs and Outputs

## Inputs

- sorted list of course codes
- unsorted list of the same course codes
- target course code for each test case

## Outputs

- found index or not-found result for linear search
- found index or not-found result for binary search
- trace tables for selected searches
- precondition explanation

---

# Evidence Included

`success_solution.py` prints:

- a test summary covering the four required cases
- a linear search trace for a value near the beginning
- a binary search trace on sorted data
- a binary search trace on unsorted data
- a short precondition explanation

This aligns to the student-facing requirement for working implementations,
required tests, trace evidence, and explanation of the sorted-data requirement.

---

# Tradeoffs and Interpretation

- linear search is simpler and works on any list, but it may check many values
- binary search can reduce the search space quickly, but only when the data is
  sorted correctly
- a fast algorithm is not automatically a correct algorithm when its
  preconditions are violated
- using built-in tools may save time, but students still need to understand the
  assumptions those tools depend on

---

# AI-Use Accountability Example

Lab 04 starts manually and allows AI-generated or AI-revised code only after a
student has written or traced an initial attempt.

Example disclosure a student could make:

> After tracing my own binary search attempt, I asked AI to revise one part of
> the loop logic. I accepted the change only after rerunning my tests, checking
> the sorted-data case, and verifying that the unsorted binary search example
> still demonstrated why the precondition matters.

---

# Rubric Categories Illustrated

- `T3` Algorithm Implementation and Testing
- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly