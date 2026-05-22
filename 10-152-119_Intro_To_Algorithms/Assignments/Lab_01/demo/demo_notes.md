# LAB 01 DEMO NOTES - PRECISION AND CORRECTNESS

**Demo Title:** Laptop Charger Decision Algorithm
**Related Lab:** Lab 01 - Precision and Correctness
**Concept Transfer Target:** Turn an everyday decision into precise, testable rules
**Estimated Time:** 12-15 minutes

---

# Opening Frame

Today we are moving from vague everyday advice to testable algorithmic rules.
The goal is to show that an algorithm is not defined by formal notation. It is
defined by precision, repeatability, and evidence.

---

# Demo Problem

Decide whether a student should pack a laptop charger before leaving for
campus.

Inputs:

- `battery_percent`
- `expected_hours`
- `outlet_access`

Output:

- `bring charger` or `charger optional`

---

# What Students Should Notice

- an algorithm can begin in plain English
- vague words create hidden assumptions
- pseudocode and Python are just different representations of the same logic
- edge cases expose whether the rules are actually precise
- a result is more trustworthy when it is tested against expected outcomes

---

# Before / After Precision Check

## Before

```text
If the laptop battery is low, bring the charger.
If the student will be on campus for a long time and does not have reliable
outlet access, bring the charger.
Otherwise, the charger is optional.
```

Problems to surface with students:

- What counts as "low"?
- What counts as a "long time"?
- Does exactly 40 percent count as low?

## After

```text
If battery_percent is 40 or below, bring the charger.
Else if expected_hours is 4 or more and outlet_access is false, bring the
charger.
Otherwise, the charger is optional.
```

---

# Algorithm Representation Bridge

Use the revised version in all three forms.

## Precise Plain English

```text
If battery_percent is 40 or below, bring the charger.
Else if expected_hours is 4 or more and outlet_access is false, bring the
charger.
Otherwise, the charger is optional.
```

## Pseudocode

```text
if battery_percent <= 40:
    recommend bringing charger
else if expected_hours >= 4 and outlet_access is false:
    recommend bringing charger
else:
    charger is optional
```

## Python-Style Logic

```python
if battery_percent <= 40:
    recommendation = "bring charger"
elif expected_hours >= 4 and not outlet_access:
    recommendation = "bring charger"
else:
    recommendation = "charger optional"
```

Teaching point:

The algorithm stays the same even when the representation changes. What matters
is that the logic is clear enough to follow, test, and explain.

---

# Demo Evidence

Run `demo_code.py` twice through the printed sections:

1. Inspect the initial test table using the `< 40` rule.
2. Identify the failed boundary case at exactly `40` battery and `4` hours.
3. Inspect the revised test table using the `<= 40` rule.

The visible evidence should include:

- a before/after rule comparison
- an input/output test table
- one edge case that fails before revision and passes after revision

Console presentation note:

The demo uses light ANSI color to make section headings and pass/fail results
easier to read. This is instructor-demo presentation polish, not a student lab
requirement.

---

# Likely Misconceptions

- students may think plain English is not a real algorithm
- students may assume a working output means the rules are complete
- students may not notice that threshold values need exact wording
- students may forget that rule order changes the outcome

---

# Transfer Bridge

> In the demo, we turned a campus-preparation decision into precise rules and
> used test cases to expose ambiguity. In the lab, students will do the same
> thing with a different scenario, their own assumptions, and their own edge
> cases.

---

# Stop Point

Stop after revising the battery threshold and confirming the revised rule with
the test table. Do not turn the demo into a cafeteria, help desk, parking,
registration, or library example. Students still need to make those decisions
themselves.

---

# Instructor Notes

- Keep the live code small and readable.
- Ask students to predict Test 4 before running the initial version.
- Use the failure to model revision rather than to model perfection.
- Remind students that their lab may be written as pseudocode or Python, but it
  still needs inputs, outputs, assumptions, and test evidence.
