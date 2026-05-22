# LAB 2 - GROWTH AND BIG-O INTUITION

**Week 2 - Big-O and Growth Intuition**

---

# Context

Small inputs can hide inefficient behavior.

In this lab, you will run simple timing experiments and compare how different
approaches behave as input size grows.

---

# Objective

Collect evidence about algorithm growth and explain the difference between
timing measurements and Big-O reasoning.

Your work should demonstrate:

- controlled timing experiments
- comparison of at least two growth patterns
- a table or chart of results
- explanation of what the evidence suggests

---

# Task

Compare two approaches for a simple task.

Choose or use an instructor-assigned option:

- count duplicates with nested loops vs dictionary counting
- find a maximum with one loop vs repeated sorting
- check pair sums with nested loops vs a set-based approach
- build a string repeatedly vs collect pieces and join them

Support artifact:

- `Lab_02_Full_English_Algorithm_Walkthroughs.md`

Use this support artifact if you need help understanding how the two approaches
differ before you begin coding and timing. Do not copy it as your final answer.

If you use the walkthrough:

Add a short explanation in your own words:

- What general pattern did the walkthrough show?
- How did you adapt that pattern to your own comparison?
- What part of the process did you still have to decide for yourself?

Your explanation should show that you understand the reasoning pattern, not only
the specific example.

If you do not use the walkthrough:

You may optionally add a short explanation of the general comparison pattern
your work follows. This may be considered for enrichment if your instructor
allows it.

---

# Requirements

Your submission must include:

1. A short description of the task.
2. Two Python approaches that solve the same problem.
3. At least `4` input sizes.
4. A timing table.
5. A simple chart or clearly formatted comparison table.
6. A short explanation of the likely growth pattern for each approach.
7. A note about at least one limitation of your timing experiment.

---

# Evidence Requirements

Include a timing table.

Your table should use your own comparison and your own measured results.

Demo example only:

The table below uses an instructor demo comparing list membership lookup and
set membership lookup. Your submitted table should use your chosen lab
comparison instead.

| Input Size | Approach A Time | Approach B Time | What Changed? |
| --- | --- | --- | --- |
| 1,000 items | 0.0008 sec | 0.0001 sec | Both are fast at small size |
| 10,000 items | 0.0085 sec | 0.0001 sec | List lookup grows noticeably |
| 50,000 items | 0.0430 sec | 0.0002 sec | List lookup takes more repeated checking |
| 100,000 items | 0.0875 sec | 0.0002 sec | Set lookup remains nearly flat in this demo |

Demo comparison summary:

| Approach | Informal Growth Description | Evidence From Demo |
| --- | --- | --- |
| Manual list lookup | Time increases as the collection gets larger | The lookup takes longer at each larger input size |
| Set membership lookup | Time changes very little in this simple test | The lookup time stays almost the same across sizes |

These values are approximate placeholders for demonstration. Real timing values
can change based on the computer, code, number of trials, and background
activity.

You may use Python output, a spreadsheet, or a hand-built Markdown table.

---

# AI Use

Start manually.

You may use AI after you have:

- selected both approaches
- written or attempted both implementations
- collected at least one timing result

Allowed AI uses:

- ask AI to explain a growth pattern
- ask AI to identify flaws in your timing setup
- ask AI to help label a chart or table

AI may not replace your collected evidence.

---

# Submission Requirements

Submit your lab through GitHub unless your instructor gives different
instructions.

Your lab folder should include:

- `README.md`
- your Python file or files
- any support files required by your solution

Your `README.md` should include:

- both approaches
- input sizes
- timing evidence
- chart or comparison table
- growth explanation
- timing limitation
- walkthrough-use explanation, if applicable
- AI-use note, if applicable

Schoology may still be used to submit a GitHub link, confirmation message,
exported PDF, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly:

> What did the timing evidence show that was not obvious from a small input?

If you used AI:

> What did AI explain, and how did you verify it against your results?

---

# Evaluation Focus

This assignment is aligned to the Algorithms Master Rubric System.

## Primary Rubric Focus

- **T4 - Correctness, Efficiency, and Tradeoff Evaluation**
- **T5 - Observable Algorithm Behavior and Communication Evidence**

## Secondary Rubric Focus

- **T3 - Algorithm Implementation and Testing**
- **C1 - Solve Problems**
- **C2 - Communicate Clearly**

## Optional / Light Focus

- **T1 - Problem Framing and Algorithmic Analysis**
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

- compares approaches fairly enough for an introductory lab
- uses increasing input sizes
- separates evidence from opinion
- explains why small-input success may not scale
