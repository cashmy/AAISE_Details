# LAB 01 SUCCESS NOTES - PRECISION AND CORRECTNESS

This package shows one acceptable successful version for Lab 01. It is not the
only possible answer because the student assignment allows several different
decision scenarios.

---

# Chosen Scenario

Help desk ticket priority

This scenario stays in the same concept family as the lab but does not reuse
the instructor demo about bringing a laptop charger.

---

# Problem Statement

Create a precise algorithm that assigns a help desk ticket to one of these
results:

- `high`
- `medium`
- `low`
- `needs clarification`

The algorithm uses the ticket's severity, number of users affected, deadline,
blocked-work status, and whether the required information is complete.

---

# Inputs and Outputs

## Inputs

- `severity`
- `users_affected`
- `hours_until_deadline`
- `work_blocked`
- `has_required_info`

## Outputs

- priority label
- short reason for the decision

---

# Assumptions and Constraints

- severity is one of `low`, `medium`, `high`, or `critical`
- the ticket must include enough information to judge impact and urgency
- `users_affected >= 10` counts as a medium-priority threshold when higher
  rules do not apply
- blocked work matters more than a distant deadline
- the first matching rule wins so the ordering is part of the algorithm

---

# Evidence Included

`success_solution.py` prints a visible test table with:

- `4` normal cases
- `2` edge cases
- expected and actual outputs
- pass/fail results
- the reason attached to each priority decision

This supports the Lab 01 evidence requirement that students show expected and
actual results rather than only claiming that the algorithm works.

---

# Revision Note

One ambiguity in the early version was the phrase `many users affected`.
Testing the threshold case showed that the rule needed a precise number.

Before revision:

```text
If many users are affected, make the ticket medium priority.
```

After revision:

```text
If users_affected is 10 or more, make the ticket medium priority.
```

This makes the edge case testable and easier to explain.

---

# Tradeoffs

- a rule chain is easy for beginners to read and test
- the approach is less flexible than a weighted scoring system
- the first-match structure keeps the behavior explainable, but it depends on
  careful rule order

---

# AI-Use Accountability Example

Lab 01 starts manually and allows optional AI-assisted revision only after an
initial attempt and at least three test cases.

Example disclosure a student could make:

> After writing my first version and three tests, I asked AI to suggest edge
> cases. It suggested checking the exact user-count threshold and the missing
> information case. I kept those ideas, but I wrote the final wording of the
> rules, updated the threshold to `10 or more`, and reran every test myself.

---

# Rubric Categories Illustrated

- `T1` Problem Framing and Algorithmic Analysis
- `T3` Algorithm Implementation and Testing
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly