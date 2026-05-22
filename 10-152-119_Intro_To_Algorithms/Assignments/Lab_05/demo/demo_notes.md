# LAB 05 DEMO NOTES - STRATEGY COMPARISON

**Demo Title:** Nested Donation Envelopes
**Related Lab:** Lab 05 - Strategy Comparison
**Concept Transfer Target:** Compare iterative and recursive strategies for the same problem
**Estimated Time:** 12-15 minutes

---

# Assumptions

- creating a fresh `Assignments/Lab_05/` package
- treating the student-facing Lab 05 file as authoritative
- using a generic starter rather than a scenario-specific starter
- using nested donation envelopes for the demo and a different problem for the
  withheld success version
- using a recursive call trace and a strategy comparison table as the visible
  evidence
- using light ANSI color in the instructor demo when it helps distinguish
  totals, recursive calls, strategy-fit signals, and key takeaways
- keeping the primary success version plain while providing optional colorized
  refinements separately when useful

---

# Opening Frame

Today we are moving from choosing one working algorithm to comparing two
different ways of thinking about the same problem. The goal is to show that a
strategy can be correct, but still be a weaker fit for the structure of the
data or the explanation we need to give.

---

# Demo Problem

Calculate the total value of nested donation envelopes.

Compare two strategies:

- iterative processing with an explicit work stack
- recursive processing of nested groups

The data contains integers and nested lists of integers so students can see why
the data shape influences the strategy fit.

---

# What Students Should Notice

- recursion needs a base case and a clear rule for nested groups
- iteration can still solve the problem, but it may need extra bookkeeping
- the same correct answer can come from different strategies
- a recursive trace makes hidden work visible
- the better strategy depends on the data shape, readability, and what needs to
  be explained

---

# Demo Evidence

Run `demo_code.py` to produce:

- one recursive call trace for the nested donation data
- the total from the iterative strategy
- the total from the recursive strategy
- a comparison table about correctness, readability, growth, and fit to data

Students should be able to explain why the recursive version matches the nested
shape more directly in this example, even though the iterative version still
works.

Console presentation note:

The demo uses light ANSI color to make totals, recursive trace actions,
strategy-fit notes, and the final takeaway easier to inspect. This is
instructor-demo presentation polish, not a student lab requirement.

---

# Transfer Bridge

> In the demo, we compared iterative and recursive thinking on nested donation
> envelopes. In the lab, students will compare two strategies for a different
> problem and justify which strategy is the better fit for that context.

---

# Stop Point

Stop after tracing one recursive path and reading the comparison table. Do not
turn the demo into a complete lab submission for cumulative product, grouped
sum, decision trees, coin selection, scheduling, or shopping tradeoffs.

---

# Likely Misconceptions

- students may assume recursive code is automatically more advanced or better
- students may focus only on whether the answers match and ignore readability
  or data fit
- students may forget to define a base case clearly
- students may compare strategies without naming the tradeoff that matters most

---

# Instructor Notes

- Keep the nested example small enough for students to follow the recursive
  calls by hand.
- Emphasize that both strategies are correct in the demo.
- Use the call trace to make the recursive work observable.
- Remind students that "best" is contextual, not absolute.
