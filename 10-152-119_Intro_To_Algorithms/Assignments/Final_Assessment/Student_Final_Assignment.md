# FINAL ASSESSMENT - STUDENT INSTRUCTIONS

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This final assessment verifies that you can create small algorithmic solutions,
show evidence, and explain your reasoning.

This is not a capstone project and it is not a trick test. The goal is to show
that you can solve bounded problems, test your work, and explain assumptions,
tradeoffs, and AI use responsibly.

---

# Final Structure

The final has two parts.

```text
Part 1 - Applied Solution Set
Part 2 - Explanation Defense
```

Part 1 is the work you submit.

Part 2 is where you explain the work you submitted.

---

# Part 1 - Applied Solution Set

Complete all three tasks.

You may use the provided starter files. The starter files are there to reduce
setup friction, not to solve the final for you.

Your work should be submitted through GitHub unless your instructor gives
different instructions.

Your final folder should include:

```text
README.md
task_1_equipment_checkout.py
task_2_duplicate_registration.py
task_3_support_resource_recommendation.py
```

---

# Task 1 - Equipment Checkout Eligibility

## Scenario

A school technology desk needs a small decision algorithm to decide whether a
person may check out a device.

The decision may depend on information such as:

- account status
- required training completion
- whether the requested device is available
- whether the person has overdue equipment
- whether supervisor approval is needed

## Required Work

Create an algorithm that returns a clear decision such as:

```text
approved
denied
needs review
```

Your submission must include:

- inputs and outputs
- assumptions or constraints
- decision logic in Python
- at least `5` test cases
- at least `2` edge cases
- a short note about one ambiguity you had to make precise

---

# Task 2 - Duplicate Registration Detection

## Scenario

A workshop coordinator has a list of registration records. Some people may have
registered more than once.

You need to compare two approaches for detecting duplicate registrations.

## Required Work

Implement or complete two approaches:

1. A direct comparison approach, such as nested loops.
2. A structure-supported approach, such as a set or dictionary.

Your submission must include:

- both approaches
- evidence that both approaches detect the same duplicates
- at least `4` input sizes or test sets
- a timing table or comparison table
- a short explanation of which approach fits better and why
- at least one limitation of your comparison

---

# Task 3 - Support Resource Recommendation

## Scenario

A help desk team wants a simple recommendation tool that suggests support
resources based on a request profile.

Each support resource has tags. A request also has tags. Your algorithm should
compare the request profile to available resources and rank the resources.

Example tags might include:

```text
account, password, network, device, urgent, beginner, documentation, video
```

## Required Work

Create a small recommendation or ranking algorithm.

Your submission must include:

- a request profile
- at least `5` candidate resources
- a simple similarity or ranking rule
- a representation table or summary
- a ranking table
- a final recommendation
- assumptions and limitations

The scoring rule does not need to be advanced. It must be clear enough to
explain and test.

---

# AI Use

AI may be used in Part 1 if you use it responsibly.

If you use AI, your `README.md` must explain:

- what AI helped with
- what you changed
- what you tested
- what you still understand and own

AI may help you improve, debug, or explain your work. AI may not replace your
responsibility to understand and explain your submitted solution.

---

# Using Your Previous Work

You may use your own previous course submissions as a reference while completing
the final.

This is realistic professional practice. Developers often look back at their
own earlier code, notes, tests, and examples when solving a new problem.

If you reuse or adapt an idea from your own earlier work, make sure the final
submission fits the new task and that you can explain what you reused, what you
changed, and why it works here.

Part 2 may ask you to explain those choices.

---

# README Requirements

Your `README.md` is part of the final submission.

It should include:

- a short summary of each task
- evidence tables for each task
- assumptions and limitations
- a short explanation of tradeoffs
- AI-use note, if applicable
- any known issues

Use the provided `README_Final_Template.md` as a starting point.

---

# Part 2 - Explanation Defense

In Part 2, you will answer questions about your own Part 1 submission.

Questions may ask you to:

- walk through part of your code
- explain a test case
- identify an assumption or edge case
- compare two approaches
- explain a data structure choice
- explain your ranking or similarity rule
- explain what AI helped with, if AI was used
- describe what you would improve with more time

This is not meant to trick you. It verifies that you understand the work you
submitted.

---

# Success Criteria

Successful final submissions:

- include working or mostly working solutions
- include visible evidence
- explain assumptions and limitations
- compare approaches where required
- use AI responsibly if AI is used
- are organized enough for the instructor to review

Higher-scoring submissions do more than make the code run. They connect the
code to evidence, tradeoffs, and explanation.
