# LAB 5 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 5 - Recursion, Iteration, and Strategy Patterns**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 5 strategy comparison options before writing code or creating evidence.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how two valid strategies can solve the same problem in
different ways.

---

# How To Use This Artifact

For your chosen problem:

1. Read the matching walkthrough.
2. Write a short problem statement.
3. Describe Strategy A before coding.
4. Describe Strategy B before coding.
5. Create at least four tests, including an edge case.
6. Compare correctness, readability, growth, and fit.
7. Recommend one strategy for your specific problem.

Do not copy the wording directly as your final answer. Your submitted work must
include your own problem framing, strategy descriptions, tests, evidence,
recommendation, limitation note, and AI-use note if applicable.

---

# What Makes This A Strategy Comparison?

This lab is not asking for only one working answer.

It asks you to show that there can be more than one way to solve a problem.
Both strategies may be correct, but one may be clearer, easier to test, more
efficient, or a better fit for the data.

The recommendation should include a condition. For example:

> For this small problem, Strategy A is clearer. For a much larger input,
> Strategy B may become more appropriate.

---

# Option 1 - Factorial Or Cumulative Product

First, define the calculation. A factorial multiplies a number by every
positive whole number below it. A cumulative product multiplies a series of
values together.

Strategy A could use iteration. Start with a result value of one. Look at each
number in order and multiply the result by that number. When the loop ends,
return the result.

Strategy B could use recursion. Define the result in terms of a smaller version
of the same problem. For factorial, the result for `n` can use the result for
`n - 1`. The recursive strategy must include a stopping case so it does not
continue forever.

Questions to guide your comparison:

- Which strategy is easier to trace?
- What is the stopping condition?
- What should happen for zero or an empty input?
- Which strategy is easier for a beginner to debug?

---

# Option 2 - Sum Nested Or Grouped Values

First, define the data. The values may be grouped by category, day, student, or
department.

Strategy A could use nested loops. First, look at one group. Then look at each
value inside that group and add it to a running total. Continue until all
groups have been processed.

Strategy B could separate the problem into smaller helper steps. One helper
could total one group. Another step could call that helper for each group and
combine the results.

If the grouping can be nested at different depths, a recursive strategy may
also be possible, but only if the stopping case is clear.

Questions to guide your comparison:

- Are all groups the same shape?
- Is the data nested only one level, or multiple levels?
- Which strategy makes the data shape clearer?
- What edge case tests an empty group?

---

# Option 3 - Path Through A Simple Decision Tree

First, define the decision tree. Each decision should lead to another question
or to a final result.

Strategy A could use a sequence of `if` and `elif` statements. Start with the
first decision. Based on the answer, move to the next relevant decision. Stop
when a final result is reached.

Strategy B could represent the tree as data. Each node could store a question
and possible next nodes. The algorithm follows the selected path until it
reaches a final result.

The first strategy may be easier for a very small tree. The second strategy may
be easier to update when the tree grows.

Questions to guide your comparison:

- How many decisions are in the tree?
- Does the tree need to change often?
- Which strategy makes the path easier to show?
- What input should test an unexpected answer?

---

# Option 4 - Small Coin-Change Or Greedy Selection

First, define the goal. The problem may ask for a combination of coins, points,
items, or choices that reaches a target.

Strategy A could use a greedy approach. At each step, choose the largest or
best-looking option that still fits. Continue until the target is reached or no
choice is possible.

Strategy B could try more combinations. Instead of always choosing the largest
option first, it can test different combinations and keep the best valid one.

The greedy strategy may be simple and fast, but it may miss the best answer in
some problems. The broader search strategy may find a better answer, but it may
do more work.

Questions to guide your comparison:

- What makes a choice "best" at each step?
- Can a greedy choice block a better final result?
- What test case reveals the weakness of greedy selection?
- Which strategy is reasonable for a small data set?

---

# Option 5 - Brute Force vs Greedy Scheduling Or Shopping

First, define the scenario. You may need to choose tasks for a schedule, items
for a shopping cart, or activities that fit within a limit.

Strategy A could use brute force. Try every reasonable combination, check which
combinations are valid, and select the best result according to your rule.

Strategy B could use a greedy rule. For example, choose the cheapest item first,
the highest-value item first, the shortest task first, or the task with the
earliest deadline first.

Brute force may be easier to trust for a tiny data set because it checks many
possibilities. Greedy may be easier to explain and faster, but it depends on
whether the rule actually fits the problem.

Questions to guide your comparison:

- What does "best" mean in your scenario?
- What limit or constraint must be followed?
- Which greedy rule did you choose?
- Does your test data include a case where greedy might make a poor choice?

---

# Your Turn

After reading the walkthrough for your option, describe both strategies before
coding.

Your next step is not to find the one perfect algorithm. Your next step is to
compare two reasonable strategies and explain which one fits your problem
better.
