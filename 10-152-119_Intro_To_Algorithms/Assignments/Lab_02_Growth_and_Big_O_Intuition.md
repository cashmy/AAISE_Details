# LAB 2 - GROWTH AND BIG-O INTUITION

**Week 2 - Big-O and Growth Intuition**

---

# Lab Identity

- **Unit:** Unit 1 - Algorithmic Foundations and Correctness
- **Primary Competency:** T4. Correctness, Efficiency, and Tradeoff Evaluation
- **Secondary Competencies:** T3, T5, C1, C2
- **AI Involvement Level:** Manual First -> AI-Assisted

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

# Instructor Demo Plan

## Demo Problem

Compare two ways to check whether a value appears in a collection:

- one direct membership check using a set
- one manual loop through a list

## What Students Should Notice

- timing small inputs can be noisy
- input size matters
- repeated work changes behavior
- measured time and Big-O are related but not identical

## Transfer Bridge

> In the demo, we compared lookup behavior. In the lab, you will compare a
> different pair of approaches and explain what changes as input grows.

## Demo Evidence

- timing table for several input sizes
- short statement of expected growth

Example demo timing table:

| Input Size | Manual List Lookup Time | Set Membership Time | What Changed? |
| --- | --- | --- | --- |
| 1,000 items | 0.0008 sec | 0.0001 sec | Both are fast at small size |
| 10,000 items | 0.0085 sec | 0.0001 sec | List lookup grows noticeably |
| 50,000 items | 0.0430 sec | 0.0002 sec | List lookup takes more repeated checking |
| 100,000 items | 0.0875 sec | 0.0002 sec | Set lookup remains nearly flat in this demo |

Example demo comparison summary:

| Approach | Informal Growth Description | Evidence From Demo |
| --- | --- | --- |
| Manual list lookup | Time increases as the collection gets larger | The lookup takes longer at each larger input size |
| Set membership lookup | Time changes very little in this simple test | The lookup time stays almost the same across sizes |

Instructor note:

These are heuristic placeholder values until the actual demo code is created.
Use them to show table structure and interpretation, then replace them with
measured values after the final demo code exists.

## Stop Point

Stop before producing a polished chart. Students should create their own table
or chart in the lab.

---

# Student Lab Task

Compare two approaches for a simple task.

Choose or use an instructor-assigned option:

- count duplicates with nested loops vs dictionary counting
- find a maximum with one loop vs repeated sorting
- check pair sums with nested loops vs a set-based approach
- build a string repeatedly vs collect pieces and join them

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

Example structure:

| Input Size | Approach A Time | Approach B Time | What Changed? |
| --- | --- | --- | --- |
|  |  |  |  |

You may use Python output, a spreadsheet, or a hand-built Markdown table.

---

# AI Boundary

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

# Submission Checklist

- two approaches included
- input sizes listed
- timing evidence included
- chart or comparison table included
- growth explanation included
- timing limitation included
- AI-use note included, if applicable

---

# Reflection

Answer briefly:

> What did the timing evidence show that was not obvious from a small input?

If you used AI:

> What did AI explain, and how did you verify it against your results?

---

# Success Criteria

Successful work:

- compares approaches fairly enough for an introductory lab
- uses increasing input sizes
- separates evidence from opinion
- explains why small-input success may not scale

---

# Successful Version Release Note

A successful version may be released after submission. It should include a
working timing example and a model explanation of the evidence.
