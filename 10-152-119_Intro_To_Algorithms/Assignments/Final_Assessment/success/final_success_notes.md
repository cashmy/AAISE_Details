# FINAL ASSESSMENT SUCCESS EXAMPLES

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This folder contains post-final success examples for the three Part 1 final
tasks.

These files should be released only after the final has been completed and
graded, unless the instructor decides otherwise.

---

# Important Note For Students

These are examples of acceptable solutions.

They are not the only correct solutions.

A different solution may also be correct if it:

- solves the assigned task
- uses reasonable assumptions
- includes evidence
- can be explained
- identifies limitations or tradeoffs

---

# Files

| File | Task |
| --- | --- |
| `task_1_equipment_checkout_solution.py` | Equipment checkout eligibility |
| `task_2_duplicate_registration_solution.py` | Duplicate registration detection |
| `task_3_support_resource_recommendation_solution.py` | Support resource recommendation |

---

# What These Examples Demonstrate

## Task 1

The equipment checkout example demonstrates a clear rule order:

1. deny requests that cannot be allowed
2. route incomplete or higher-risk requests to review
3. approve requests only after required conditions are met

Alternate valid solutions may use different rules or thresholds if the
assumptions are stated and tested.

## Task 2

The duplicate registration example compares a direct nested-loop approach with
a set-supported approach.

The set-supported approach is a better fit for larger inputs because it avoids
comparing every record to every other record.

Alternate valid solutions may use dictionaries, counters, or other reasonable
structures.

## Task 3

The support resource recommendation example uses simple tag-overlap similarity.

The recommendation is useful but limited because all tags are weighted equally
and the model ignores quality, difficulty, time required, and user preference.

Alternate valid solutions may use different tags, scoring rules, ranking notes,
or recommendation thresholds.

---

# How Students Should Use These

Students should use these examples to compare against their own work after the
final.

Useful reflection questions:

- What did this example do similarly to my solution?
- What did this example do differently?
- Did my evidence prove the same kind of behavior?
- Did I explain my assumptions clearly?
- What would I improve if I revised my solution?

The goal is learning closure, not retroactive replacement of the student's
submitted work.
