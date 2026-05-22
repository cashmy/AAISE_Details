# LAB 1 - PRECISION AND CORRECTNESS

**Week 1 - Algorithms, Precision, and Correctness**

---

# Lab Identity

- **Unit:** Unit 1 - Algorithmic Foundations and Correctness
- **Primary Competency:** T1. Problem Framing and Algorithmic Analysis
- **Secondary Competencies:** T3, T5, C1, C2
- **AI Involvement Level:** Manual Only, with optional AI-assisted revision

---

# Context

An algorithm is only useful when its steps are precise enough to follow and
test.

In this lab, you will turn an everyday decision process into an algorithm,
identify assumptions, test edge cases, and revise the instructions when they
are ambiguous.

---

# Objective

Create a small algorithm that can be followed by a person or implemented in
Python.

Your work should demonstrate:

- clear inputs and outputs
- stated assumptions and constraints
- normal and edge-case testing
- revision based on evidence

---

# Instructor Demo Plan

## Demo Problem

Create instructions for deciding whether a student should pack a laptop charger
before leaving for campus.

Demo rules may include battery percentage, expected time on campus, and whether
reliable outlet access is available.

## What Students Should Notice

- an algorithm does not have to look like a formal math equation to be valid
- plain English, pseudocode, and Python code can represent the same decision
  process
- vague words such as "low", "long", or "might" create interpretation problems
- rules must be ordered carefully
- edge cases reveal hidden assumptions
- a working answer is not the same as a tested algorithm

## Algorithm Representation Bridge

Use the same decision process in three forms so students can see how an
algorithm moves from human reasoning to code.

Plain English:

```text
If the laptop battery is low, bring the charger.
If the student will be on campus for a long time and does not have reliable
outlet access, bring the charger.
Otherwise, the charger is optional.
```

Pseudocode:

```text
if battery_percent is below 40:
    recommend bringing charger
else if expected_hours is 4 or more and outlet_access is false:
    recommend bringing charger
else:
    charger is optional
```

Python-style logic:

```python
if battery_percent < 40:
    recommendation = "bring charger"
elif expected_hours >= 4 and not outlet_access:
    recommendation = "bring charger"
else:
    recommendation = "charger optional"
```

Instructor explanation:

This is an algorithm because the process is clear, repeatable, testable,
explainable, and implementable. The formal appearance is not the defining
feature. The repeatable reasoning is.

## Transfer Bridge

> In the demo, we turned a campus-preparation decision into precise rules. In the lab,
> you will turn a different decision process into precise rules and test it.

## Demo Evidence

- before/after instruction comparison
- small input/output table
- at least one edge case

Example demo evidence table:

| Test | Input Summary | Expected Output | Actual Output | Pass? |
| --- | --- | --- | --- | --- |
| 1 | Battery 25%, 2 hours on campus, outlet available | Bring charger | Bring charger | Yes |
| 2 | Battery 80%, 3 hours on campus, outlet unavailable | Charger optional | Charger optional | Yes |
| 3 | Battery 55%, 5 hours on campus, outlet unavailable | Bring charger | Bring charger | Yes |
| 4 | Battery exactly 40%, 4 hours on campus, outlet unavailable | Bring charger | Charger optional | No |
| 5 | Battery 39%, 1 hour on campus, outlet unavailable | Bring charger | Bring charger | Yes |

Instructor note:

Use the failed or unexpected result in Test 4 to show how an edge case exposes
ambiguity. The algorithm may need to clarify whether "below 40" or "40 and
below" counts as a low battery.

## Stop Point

Stop after demonstrating revision on one flawed rule. Students should still
identify and repair ambiguity in their own scenario.

---

# Student Lab Task

Choose or use an instructor-assigned scenario:

- cafeteria meal recommendation
- help desk ticket priority
- parking fee calculation
- event registration eligibility
- library late-fee decision

Your task is to create a precise algorithm for the scenario.

---

# Requirements

Your submission must include:

1. A short problem statement.
2. A list of inputs and outputs.
3. At least `3` assumptions or constraints.
4. Pseudocode or Python code for the decision process.
5. At least `5` test cases:
   - `3` normal cases
   - `2` edge cases
6. A before/after revision note showing one improvement you made.

---

# Evidence Requirements

Include an input/output table with expected and actual results.

Example structure:

| Test | Input Summary | Expected Output | Actual Output | Pass? |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |

---

# AI Boundary

Start manually.

You may use AI only after you have written your first version of the algorithm
and at least three test cases.

Allowed AI uses:

- ask AI to identify ambiguity
- ask AI to suggest edge cases
- ask AI to explain why one instruction may be unclear

You may not submit AI output without revising, testing, and explaining it.

---

# Submission Checklist

- problem statement included
- inputs and outputs identified
- assumptions or constraints listed
- pseudocode or Python included
- test table included
- revision note included
- AI-use note included, if applicable

---

# Reflection

Answer briefly:

> What was one ambiguous instruction in your first version, and how did testing
> help you improve it?

If you used AI:

> What did AI help you notice, and what did you change yourself?

---

# Success Criteria

Successful work:

- defines the problem clearly
- uses precise steps
- tests normal and edge cases
- revises based on evidence
- explains assumptions rather than hiding them

---

# Successful Version Release Note

A successful version may be released after submission. It should show one
possible complete solution, not the only acceptable solution.
