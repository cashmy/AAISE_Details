# LAB 05 OPTION SOLUTION SKETCHES

**Lab:** Strategy Comparison  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches support instructor judgment across the allowed strategy options.
They are not student-facing walkthroughs and are not full runnable code.

For Lab 05, the student should compare strategies, not merely submit two
versions of code. The strongest evidence shows tests, a trace or comparison
table, and a context-dependent recommendation.

---

# Common Required Evidence

Every option should include:

- short problem statement
- Strategy A description before code
- Strategy B description before code
- two implementations or clear simulations
- at least four tests, including one edge case
- trace, decision tree, or comparison table
- recommendation
- note about when the preferred strategy might not be best

Suggested strategy table:

| Criterion | Strategy A | Strategy B | Notes |
| --- | --- | --- | --- |

---

# Option 1 - Factorial Or Cumulative Product

## Viable Framing

Compute factorial for a non-negative integer or cumulative product for a list
of numbers.

## Recommended Strategies

- iterative loop
- recursive function

## Expected Tests

- normal value, such as 5
- smallest valid value, such as 0 or empty list depending on framing
- value of 1
- larger but reasonable value

## Expected Recommendation

Iteration is often clearer for beginners and avoids recursion-depth concerns.
Recursion may match the mathematical definition more directly.

## Edge Cases

- factorial of 0
- negative input
- empty product list

## Grading Watch-Fors

- Student writes recursion without a base case.
- Student cannot explain why recursion stops.
- Student recommends recursion only because it looks advanced.

## Runnable Expansion Note

Print a trace showing each multiplication for the iterative version and each
recursive call depth for the recursive version.

---

# Option 2 - Sum Nested Or Grouped Values

## Viable Framing

Sum values grouped by category, day, student, or department.

## Recommended Strategies

- nested loops
- helper function per group
- optional recursion only for variable-depth nesting

## Expected Tests

- several groups with values
- one empty group
- one group with a single value
- all groups empty or total zero

## Expected Recommendation

Nested loops are straightforward for one-level grouping. Helper functions may
be clearer when group totals must be reused or displayed separately.

## Edge Cases

- empty group
- missing group
- non-numeric value if input validation is included

## Grading Watch-Fors

- Student uses recursion for one-level data without explaining why.
- Student calculates total but does not compare strategy clarity.
- Student ignores empty groups.

---

# Option 3 - Path Through A Simple Decision Tree

## Viable Framing

Choose a result by following a series of decisions, such as support routing,
eligibility, or recommendation.

## Recommended Strategies

- explicit `if` / `elif` decision chain
- data-driven tree representation

## Expected Tests

- path to first possible result
- path to a later result
- edge case or missing/unknown answer
- path that requires multiple decisions

## Expected Recommendation

Explicit conditionals may be clearer for a tiny tree. A data-driven tree may
be better if the tree changes often or needs to be displayed.

## Edge Cases

- unexpected answer
- incomplete decision path
- conflicting criteria

## Grading Watch-Fors

- Student creates only one strategy.
- Student does not show the path taken.
- Student cannot explain how the data-driven version represents the tree.

---

# Option 4 - Small Coin-Change Or Greedy Selection

## Viable Framing

Choose coins, points, or items to reach a target or maximize a simple score.

## Recommended Strategies

- greedy choice
- broader combination search or brute force for small data

## Expected Tests

- case where greedy works
- case where greedy may fail
- exact target
- no valid solution or impossible target

## Expected Recommendation

Greedy may be simple and fast when the rule fits the problem. Brute force or
combination search may be more reliable for small examples where greedy can
miss the best answer.

## Edge Cases

- target of zero
- impossible target
- tie between valid choices

## Grading Watch-Fors

- Student assumes greedy is always optimal.
- Student does not define the greedy rule.
- Student uses a data set where both strategies always behave identically and
  then makes a broad claim.

---

# Option 5 - Brute Force vs Greedy Scheduling Or Shopping

## Viable Framing

Choose activities, tasks, or shopping items under a budget, time limit, or
capacity limit.

## Recommended Strategies

- brute force combinations for a small data set
- greedy rule such as cheapest first, highest value first, shortest duration
  first, or earliest deadline first

## Expected Tests

- normal case with multiple valid choices
- case where greedy works well
- case where greedy misses a better combination
- no valid option or exact-limit case

## Expected Recommendation

Brute force may be more trustworthy for tiny data because it checks many
combinations. Greedy may be more practical for larger data if the rule is
reasonable, but it should be presented as a heuristic unless proven optimal.

## Edge Cases

- item exactly matches the limit
- two combinations tie
- no item fits

## Grading Watch-Fors

- Student does not state the selection goal.
- Student compares strategies using different data.
- Student calls greedy "best" without testing a counterexample.

---

# Cross-Option Grading Calibration

Strong work should:

- describe both strategies before code
- use the same problem and data for both strategies
- test normal and edge cases
- explain tradeoffs in plain language
- include a limitation for the recommended strategy
