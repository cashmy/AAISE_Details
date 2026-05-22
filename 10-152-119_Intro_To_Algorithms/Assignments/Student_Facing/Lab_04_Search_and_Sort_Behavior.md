# LAB 4 - SEARCH AND SORT BEHAVIOR

**Week 4 - Searching and Sorting**

---

# Context

Search and sort algorithms depend on assumptions.

In this lab, you will implement and compare search behavior, then demonstrate
how an algorithm can fail when its preconditions are not true.

---

# Objective

Implement and explain basic search behavior.

Your work should demonstrate:

- linear search
- binary search
- sorted-data preconditions
- trace evidence
- comparison with a built-in or alternate implementation

---

# Task

Use a data set such as:

- product IDs
- student usernames
- ticket numbers
- course codes
- event attendee names

Implement and compare search behavior on the data.

---

# Requirements

Your submission must include:

1. A data set with at least `12` values.
2. A linear search implementation.
3. A binary search implementation.
4. At least `4` test cases:
   - value found near the beginning
   - value found near the end
   - value not found
   - binary search attempted on unsorted data
5. A trace table for at least one search.
6. A short explanation of the sorted-data precondition.
7. Optional: comparison with Python's built-in search or sort behavior.

---

# Evidence Requirements

Include a search trace table.

Example structure for binary search:

| Step | Low | High | Mid | Mid Value | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Example structure for linear search:

| Step | Current Value | Match? |
| --- | --- | --- |
|  |  |  |

---

# AI Use

Start manually.

You may use AI to generate or revise a search implementation only after you
have written or traced your own attempt.

If AI generates code, you must:

- identify what it changed
- test it
- explain why it works
- explain the sorted-data precondition yourself

---

# Submission Requirements

Submit your files or written response as instructed.

Your submission should include:

- data set
- linear search
- binary search
- required tests
- trace table
- precondition explanation
- AI-use note, if applicable

---

# Reflection / Explanation

Answer briefly:

> Why is binary search not automatically better in every situation?

If you used AI:

> What part of the generated or revised code did you have to verify most
> carefully?

---

# Evaluation Focus

This assignment is aligned to the Algorithms Master Rubric System.

## Primary Rubric Focus

- **T3 - Algorithm Implementation and Testing**
- **T4 - Correctness, Efficiency, and Tradeoff Evaluation**
- **T5 - Observable Algorithm Behavior and Communication Evidence**

## Secondary Rubric Focus

- **T2 - Data Structures and Representation**
- **T6 - AI/Data Foundations and Responsible Tool Use**
- **C1 - Solve Problems**
- **C2 - Communicate Clearly**

## Optional / Light Focus

- **T1 - Problem Framing and Algorithmic Analysis**
- **C4 - Value Learning**

## Not Evaluated

- **C3 - Work Productively**
- **C5 - Work Cooperatively**
- **C6 - Act Professionally**

---

# Success Criteria

Successful work:

- implements or accurately simulates search behavior
- demonstrates the sorted-data requirement
- uses evidence to explain correctness
- distinguishes algorithm understanding from library convenience
