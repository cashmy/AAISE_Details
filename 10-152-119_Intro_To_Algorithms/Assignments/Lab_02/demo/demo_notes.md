# LAB 02 DEMO NOTES - GROWTH AND BIG-O INTUITION

**Demo Title:** Lookup Growth Comparison
**Related Lab:** Lab 02 - Growth and Big-O Intuition
**Concept Transfer Target:** Compare how two correct approaches behave as input size grows
**Estimated Time:** 12-15 minutes

---

# Opening Frame

Today we are moving from "the code works" to "the work changes as input gets
larger." The goal is to show that measured timing is evidence, and Big-O is the
language we use to explain the pattern behind that evidence.

---

# Demo Problem

Compare two ways to check whether values appear in a collection:

- manual list lookup with a loop
- set membership lookup with `in`

The demo uses the same lookup task for both approaches, then repeats the task
across larger input sizes.

---

# What Students Should Notice

- two correct approaches can behave differently at larger sizes
- small inputs can hide meaningful efficiency differences
- timing values can vary from run to run, but the larger pattern still matters
- measured time is evidence, not the whole explanation by itself
- the amount of repeated work helps explain the timing pattern

---

# Demo Evidence

Run `demo_code.py` to produce two visible artifacts:

1. A timing table across several input sizes.
2. A formatted comparison summary that interprets the pattern.

The timing table should help students inspect:

- how list lookup changes as the list grows
- how set membership changes more slowly in this demo
- why the first row may not show a dramatic difference

Console presentation note:

The demo uses light ANSI color to make section headings, growth signals, and
reminders easier to read. This is instructor-demo presentation polish, not a
student lab requirement.

---

# Short Expected Growth Statement

- Manual list lookup should grow more noticeably because each lookup may scan a
  larger collection.
- Set membership should change less in this demo because the membership check
  does not repeatedly walk through every item.

Keep the language informal. The point is introductory growth intuition, not a
formal proof.

---

# Transfer Bridge

> In the demo, we compared list lookup and set membership on the same task. In
> the lab, students will compare a different pair of approaches, collect their
> own timing evidence, and explain what changes as the input size grows.

---

# Stop Point

Stop after reading the timing table and comparison summary. Do not build the
student chart for them, and do not switch into the same comparison options used
in the lab.

---

# Likely Misconceptions

- students may think one small timing result proves the full story
- students may assume faster on one run means always better in all contexts
- students may confuse measured seconds with the full meaning of Big-O
- students may ignore that background processes and number of trials affect
  timing values

---

# Instructor Notes

- Remind students that timing is noisy, so the pattern matters more than one
  exact number.
- Point out that both demo approaches are correct. The comparison is about the
  amount of work, not only correctness.
- Emphasize that students still need to choose and justify their own lab
  comparison.
- If the measured numbers differ across machines, keep the discussion focused on
  the trend, not the exact decimal values.
