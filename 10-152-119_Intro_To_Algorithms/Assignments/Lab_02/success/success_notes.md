# LAB 02 SUCCESS NOTES - GROWTH AND BIG-O INTUITION

This package shows one acceptable successful version for Lab 02. It is not the
only correct answer because the student-facing lab allows multiple comparison
options.

---

# Chosen Comparison

Count duplicates with:

- nested loops
- dictionary counting

This stays in the same concept family as the lab while staying different from
the instructor demo, which compares manual list lookup and set membership.

---

# Task Description

Both approaches solve the same problem: count how many times each value appears
in a list.

The successful version compares how the two correct approaches behave as the
list size increases.

---

# Inputs and Outputs

## Inputs

- a list of repeated integer values
- several input sizes

## Outputs

- a dictionary of counts for each distinct value
- timing evidence for both approaches
- a short comparison summary

---

# Assumptions and Constraints

- both approaches must return the same counts before the timing comparison is
  considered meaningful
- the input data is generated in a consistent way for both approaches
- timing values are approximate and depend on the machine and background
  activity
- four input sizes are enough for an introductory comparison, but not enough to
  prove every performance claim

---

# Evidence Included

`success_solution.py` prints:

- a timing table with four input sizes
- a same-output check showing both approaches solve the same task
- a comparison summary table
- a limitation note about the timing setup

This aligns to the student-facing requirement for timing evidence plus a chart
or clearly formatted comparison table.

---

# Interpretation

- nested-loop counting repeats a full scan for each item, so the timing grows
  quickly as the list gets larger
- dictionary counting updates counts in one pass, so the timing grows more
  slowly in this simple experiment
- the timing table is evidence of a pattern, not a formal proof by itself

---

# Limitation Note

One important limitation is that the results come from one computer using a
small set of input sizes and a small number of timing trials. Different machines
or more trials could change the exact values, even if the overall pattern stays
similar.

---

# AI-Use Accountability Example

Lab 02 starts manually and allows AI only after the student has selected both
approaches, attempted both implementations, and collected at least one timing
result.

Example disclosure a student could make:

> After collecting my first timing row, I asked AI to explain why one approach
> was growing faster. AI suggested that the nested-loop version repeated more
> comparisons. I kept that explanation only after checking it against my code,
> my timing table, and the fact that both approaches still produced the same
> counts.

---

# Rubric Categories Illustrated

- `T3` Algorithm Implementation and Testing
- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly