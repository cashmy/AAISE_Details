# LAB 05 SUCCESS NOTES - STRATEGY COMPARISON

This package shows one acceptable successful version for Lab 05. It is not the
only correct answer because the student-facing lab allows multiple problems and
multiple strategy pairings.

---

# Assumptions

- fresh `Assignments/Lab_05/` package
- student-facing Lab 05 treated as authoritative
- generic starter rather than scenario-specific scaffolding
- demo scenario different from the withheld success-version problem
- recursive trace and strategy comparison table used as the main evidence
- primary success version kept plain and focused on required behavior

---

# Chosen Problem

Cumulative product of a list of numbers

Strategies compared:

- iterative multiplication through the list
- recursive multiplication using head and tail

This stays in the same concept family as the lab while remaining different from
the nested donation-envelope demo.

---

# Problem Statement

Compute the cumulative product of a list of numbers by comparing two valid
strategies and explaining which strategy better fits this specific problem.

The successful version includes tests, a recursive trace, a strategy comparison
table, a recommendation, and a note about when the preferred strategy might not
be best.

---

# Inputs and Outputs

## Inputs

- a list of integer values
- four test cases, including one edge case

## Outputs

- cumulative product from the iterative strategy
- cumulative product from the recursive strategy
- recursive trace evidence
- strategy comparison table
- final recommendation and limitation note

---

# Assumptions and Tradeoffs

- the empty-list edge case uses the standard empty-product value of `1`
- both strategies should return the same result before the tradeoff comparison
  is considered meaningful
- iteration is easier to read for a flat list problem like this one
- recursion is still valid, but it adds call overhead and depends on a clear
  base case
- the better strategy can change when the data shape changes

---

# Evidence Included

`success_solution.py` prints:

- four test results, including one edge case
- a recursive trace for one representative input
- a strategy comparison table across correctness, readability, growth, and fit
  to data
- a recommendation and a note about when that recommendation may change

This aligns to the student-facing requirement for two strategies, tests,
visible evidence, a recommendation, and a tradeoff note.

---

# Recommendation Summary

For cumulative product on a flat list, the iterative strategy is the better
overall fit because it is more direct and easier to explain for this specific
data shape.

The recursive strategy is still correct, but it is less natural here than it
would be for nested or tree-shaped data.

---

# AI-Use Accountability Example

Lab 05 allows AI after the student has framed the problem and described the
first strategy.

Example disclosure a student could make:

> After describing the iterative strategy, I asked AI to suggest a second
> strategy. It suggested recursion. I accepted that idea only after writing my
> own tests, checking the base case, and explaining in my own words why the
> recursive version was less natural for a flat list.

---

# Rubric Categories Illustrated

- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `T1` Problem Framing and Algorithmic Analysis
- `T3` Algorithm Implementation and Testing
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly