# LAB 1 - PRECISION AND CORRECTNESS

**Week 1 - Algorithms, Precision, and Correctness**

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

# Task

Choose or use an instructor-assigned scenario:

- cafeteria meal recommendation
- help desk ticket priority
- parking fee calculation
- event registration eligibility
- library late-fee decision

Your task is to create a precise algorithm for the scenario.

Support artifact:

- `Lab_01_Full_English_Algorithm_Walkthroughs.md`

Use this support artifact if you need help seeing how an everyday scenario can
be turned into ordered algorithmic steps. Do not copy it as your final answer.

If you use the walkthrough:

Add a short explanation in your own words:

- What general pattern did the walkthrough show?
- How did you adapt that pattern to your own scenario?
- What part of the process did you still have to decide for yourself?

Your explanation should show that you understand the reasoning pattern, not only
the specific example.

If you do not use the walkthrough:

You may optionally add a short explanation of the general problem-solving
pattern your algorithm follows. This may be considered for enrichment if your
instructor allows it.

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

Your table should use your own scenario and your own test cases.

Demo example only:

The table below uses the instructor demo scenario about whether a student
should bring a laptop charger to campus. Your submitted table should use your
chosen lab scenario instead.

| Test | Input Summary | Expected Output | Actual Output | Pass? |
| --- | --- | --- | --- | --- |
| 1 | Battery 25%, 2 hours on campus, outlet available | Bring charger | Bring charger | Yes |
| 2 | Battery 80%, 3 hours on campus, outlet unavailable | Charger optional | Charger optional | Yes |
| 3 | Battery 55%, 5 hours on campus, outlet unavailable | Bring charger | Bring charger | Yes |
| 4 | Battery exactly 40%, 4 hours on campus, outlet unavailable | Bring charger | Charger optional | No |
| 5 | Battery 39%, 1 hour on campus, outlet unavailable | Bring charger | Bring charger | Yes |

The failed or unexpected result in Test 4 shows a possible edge-case issue. The
algorithm may need to clarify whether "below 40" or "40 and below" counts as a
low battery.

---

# AI Use

Start manually.

You may use AI only after you have written your first version of the algorithm
and at least three test cases.

Allowed AI uses:

- ask AI to identify ambiguity
- ask AI to suggest edge cases
- ask AI to explain why one instruction may be unclear

You may not submit AI output without revising, testing, and explaining it.

---

# Submission Requirements

Submit your lab through GitHub unless your instructor gives different
instructions.

Your lab folder should include:

- `README.md`
- your Python file or files, if Python code is used
- any support files required by your solution

Your `README.md` should include:

- problem statement
- inputs and outputs
- assumptions or constraints
- pseudocode or Python code
- test table
- revision note
- walkthrough-use explanation, if applicable
- AI-use note, if applicable

Schoology may still be used to submit a GitHub link, confirmation message,
exported PDF, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly:

> What was one ambiguous instruction in your first version, and how did testing
> help you improve it?

If you used AI:

> What did AI help you notice, and what did you change yourself?

---

# Evaluation Focus

This assignment is aligned to the Algorithms Master Rubric System.

## Primary Rubric Focus

- **T1 - Problem Framing and Algorithmic Analysis**

## Secondary Rubric Focus

- **T3 - Algorithm Implementation and Testing**
- **T4 - Correctness, Efficiency, and Tradeoff Evaluation**
- **T5 - Observable Algorithm Behavior and Communication Evidence**
- **C1 - Solve Problems**
- **C2 - Communicate Clearly**

## Optional / Light Focus

- **T6 - AI/Data Foundations and Responsible Tool Use**
- **C4 - Value Learning**

## Not Evaluated

- **T2 - Data Structures and Representation**
- **C3 - Work Productively**
- **C5 - Work Cooperatively**
- **C6 - Act Professionally**

---

# Success Criteria

Successful work:

- defines the problem clearly
- uses precise steps
- tests normal and edge cases
- revises based on evidence
- explains assumptions rather than hiding them
