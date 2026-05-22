# LAB 04 DEMO NOTES - SEARCH AND SORT BEHAVIOR

**Demo Title:** Searching Book Titles on a Shelf
**Related Lab:** Lab 04 - Search and Sort Behavior
**Concept Transfer Target:** Compare linear and binary search and make the sorted-data precondition visible
**Estimated Time:** 12-15 minutes

---

# Assumptions

- creating a fresh `Assignments/Lab_04/` package
- treating the student-facing Lab 04 file as authoritative
- using a generic starter rather than a scenario-specific starter
- using book titles for the demo and a different data set for the withheld
  success version
- using search trace tables and a sorted-vs-unsorted comparison as the visible
  evidence
- keeping the primary success version plain rather than adding an optional
  colorized success variant at this stage

---

# Opening Frame

Today we are moving from "searching through data" to "searching under the right
assumptions." The goal is to show that binary search can be powerful, but only
when the data is sorted in a way that matches the search logic.

---

# Demo Problem

Search for book titles in a shelf list.

Demonstrate:

- linear search on a list of titles
- binary search on a sorted list of titles
- binary search giving unreliable results on an unsorted version of the same
  data

---

# What Students Should Notice

- linear search can work on any list because it checks one value at a time
- binary search removes part of the search space at each step
- binary search depends on sorted data
- preconditions are part of correctness, not just an optional detail
- a fast-looking algorithm is not trustworthy when its assumptions are false

---

# Demo Evidence

Run `demo_code.py` to produce:

- a linear search trace
- a successful binary search trace on sorted data
- a failed binary search trace on unsorted data
- a sorted-vs-unsorted comparison summary

Students should be able to point to the trace steps and explain why binary
search narrows correctly on the sorted list and makes the wrong decisions on
the unsorted list.

---

# Transfer Bridge

> In the demo, we searched book titles and saw that binary search depends on
> sorted data. In the lab, students will search a different data set, produce
> their own traces, and explain when each search approach works or fails.

---

# Stop Point

Stop after one successful binary search example and one failed binary search on
unsorted data. Do not build the full student solution for product IDs,
usernames, ticket numbers, course codes, or attendee names.

---

# Likely Misconceptions

- students may assume binary search is always better because it is faster when
  it works
- students may overlook that sorted order is part of the algorithm's required
  setup
- students may confuse a lucky correct result on unsorted data with a valid
  method
- students may treat built-in sorting or searching as a replacement for
  understanding the precondition

---

# Instructor Notes

- Use the failed unsorted example to emphasize that preconditions belong in the
  correctness discussion.
- Keep the data set small enough that students can follow the trace manually.
- Ask students what the algorithm assumes before asking whether it is faster.
- The demo code uses light ANSI color only for readability. The color is not a
  student requirement and should not be treated as one.