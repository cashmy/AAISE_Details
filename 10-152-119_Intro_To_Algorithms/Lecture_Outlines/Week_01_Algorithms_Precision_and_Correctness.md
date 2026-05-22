# WEEK 1 LECTURE OUTLINE - ALGORITHMS, PRECISION, AND CORRECTNESS

**10-152-119 Algorithmic Problem Solving**

---

# 1. Session Identity

- **Week / Day:** Week 1 / Day 1
- **Unit:** Unit 1 - Algorithmic Foundations and Correctness
- **Weekly Theme:** Algorithms, Precision, and Correctness
- **Lecture Title:** From Ambiguous Instructions to Testable Algorithms

---

# 2. Alignment Anchor

- **Lab / Assignment Supported:** `Assignments/Lab_01_Precision_and_Correctness.md`
- **Readiness Target:** Students can define a small problem using inputs, outputs, assumptions, constraints, and tests.
- **Textbook Anchor:** Overview of algorithms; correctness; introductory problem analysis.
- **AI Involvement Level:** Manual First -> AI-Assisted
- **Primary Watch Point:** Students may treat "the code runs" as proof that the algorithm is correct.

---

# 3. Review / Bridge From Prior Week

Not applicable for Week 1.

Use this time to orient students to the course pattern:

- lecture concept
- instructor demo
- related but non-identical lab
- evidence and explanation
- AI allowed only within the stated boundary

---

# 4. Opening Frame

Today we are moving from "I can write steps" to "I can write steps that someone else or a computer can follow and test."

---

# 5. Course Positioning

This course builds on Python programming by asking students to slow down before coding:

- What problem is being solved?
- What information is needed?
- What assumptions are hidden?
- What evidence will show the solution works?

---

# 6. Core Concepts

- Algorithm: a precise procedure for solving a problem.
- Inputs and outputs: what the algorithm receives and produces.
- Constraints and assumptions: what must be true for the solution to work.
- Edge cases: inputs that test boundaries or hidden assumptions.
- Correctness: whether the solution gives expected results for the right reasons.
- Representation: the same algorithm can be shown as formal notation, plain
  English, pseudocode, or executable code.

Important beginner clarification:

Students may arrive believing that an algorithm must look like a formal math
procedure, equation, or table. That is one valid representation, but it is not
the only one. In this course, an algorithm is any clear, repeatable, testable
process for solving a problem.

The goal is to help students see that these are connected forms of the same
reasoning:

| Representation | What Students See | Course Meaning |
| --- | --- | --- |
| Formal / mathematical | equations, symbols, truth tables, formal rules | precise reasoning in compressed notation |
| Plain English | ordered human-readable steps | the decision process made understandable |
| Pseudocode | structured steps that resemble code | the bridge from thinking to implementation |
| Python code | functions, conditionals, loops, data structures | the algorithm made executable |

Use this phrase explicitly:

> In this course, an algorithm does not have to look mathematical to be real.
> It must be clear, repeatable, testable, explainable, and implementable.

---

# 7. Algorithm Visibility / Demo Plan

Use a non-lab decision demo: deciding whether a student should pack a laptop
charger before leaving for campus.

Show:

- vague rule version: "Bring your charger if you might need it."
- revised precise rule version using inputs:
  - current battery percentage
  - expected hours on campus
  - whether reliable outlet access is available
- representation comparison:
  - plain English
  - pseudocode
  - Python-style conditional logic
- small input/output table
- one edge case that exposes ambiguity

Evidence:

- before/after instruction comparison
- test table with expected and actual results

Example representation bridge:

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

Explain:

This is an algorithm because the decision process is ordered, repeatable,
testable, and can be translated into executable logic.

---

# 8. Hands-On / Lab Bridge

Students begin Lab 1 by choosing or receiving a small decision scenario.

Their goal is not to produce a clever program. Their goal is to produce a precise, testable algorithm with visible evidence.

---

# 9. Common Mistakes / Watch-Fors

- using vague words such as "small", "high", or "soon"
- skipping inputs and outputs
- writing code before defining the decision
- testing only one happy path

---

# 10. AI Use Frame

AI may critique ambiguity only after students write their first version and at least three tests.

Students remain responsible for the final wording, test cases, and explanation.

---

# 11. Explain / Checkpoint Questions

- What is the input?
- What is the output?
- What assumption must be true?
- What edge case could break this algorithm?
- What evidence shows that the revised version is better?

---

# 12. End-of-Class Success Check

By the end of this session, students should be able to write a small algorithm with stated assumptions and tests.

---

# 13. Materials / Artifacts Used

- `Assignments/Lab_01_Precision_and_Correctness.md`
- `Assignments/Lab_Progression_Ladder_v2.md`
- `v2/IIM_Matrix_v2.md`
