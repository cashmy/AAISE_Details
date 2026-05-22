# LAB 4 - SEARCH AND SORT BEHAVIOR

**Week 4 - Searching and Sorting**

---

# Lab Identity

- **Unit:** Unit 2 - Data Structures, Search, Sort, and Growth
- **Primary Competency:** T3. Algorithm Implementation and Testing
- **Secondary Competencies:** T1, T4, T5, C1, C2
- **AI Involvement Level:** Manual First -> AI-Assisted -> selective AI-Injected

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

# Instructor Demo Plan

## Demo Problem

Search for a book title in a small sorted shelf list.

Demonstrate:

- linear search on any list
- binary search on a sorted list
- binary search giving unreliable results when the list is not sorted

## What Students Should Notice

- binary search is powerful because it removes large parts of the search space
- binary search depends on sorted data
- preconditions are part of correctness
- built-in tools do not remove the need to understand assumptions

## Transfer Bridge

> In the demo, we searched book titles. In the lab, you will search a different
> data set and prove when each approach works or fails.

## Demo Evidence

- search trace table
- sorted vs unsorted example

## Stop Point

Stop after one successful and one failed binary search example. Students should
create their own search traces.

---

# Student Lab Task

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

Example structure:

| Step | Low | High | Mid | Mid Value | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

For linear search, use:

| Step | Current Value | Match? |
| --- | --- | --- |
|  |  |  |

---

# AI Boundary

Start manually.

You may use AI to generate or revise a search implementation only after you
have written or traced your own attempt.

If AI generates code, you must:

- identify what it changed
- test it
- explain why it works
- explain the sorted-data precondition yourself

---

# Submission Checklist

- data set included
- linear search included
- binary search included
- required tests included
- trace table included
- precondition explanation included
- AI-use note included, if applicable

---

# Reflection

Answer briefly:

> Why is binary search not automatically better in every situation?

If you used AI:

> What part of the generated or revised code did you have to verify most
> carefully?

---

# Success Criteria

Successful work:

- implements or accurately simulates search behavior
- demonstrates the sorted-data requirement
- uses evidence to explain correctness
- distinguishes algorithm understanding from library convenience

---

# Successful Version Release Note

A successful version may be released after submission. It should include working
linear and binary search examples plus trace evidence.
