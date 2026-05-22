# LAB 03 DEMO NOTES - DATA STRUCTURE CHOICE

**Demo Title:** Attendance Tracking With a List and a Dictionary
**Related Lab:** Lab 03 - Data Structure Choice
**Concept Transfer Target:** Compare how representation changes lookup, update, and clarity
**Estimated Time:** 12-15 minutes

---

# Assumptions

- creating a fresh `Assignments/Lab_03/` package
- treating the student-facing Lab 03 file as authoritative
- using a generic starter rather than a scenario-specific starter
- using attendance tracking for the demo and a different scenario for the
  withheld success version
- using an operation comparison table as the visible evidence format

---

# Opening Frame

Today we are moving from solving a problem with code to choosing a structure
that makes the code fit the task. The goal is to show that a structure is not
better in the abstract. It is better when it matches the access pattern.

---

# Demo Problem

Track course attendance using:

- a list of names where repeated names represent multiple check-ins
- a dictionary mapping names to attendance counts

The core operation is recording one more attendance check-in and then inspecting
how easy it is to look up the updated count.

---

# What Students Should Notice

- a list is simple to start with, but repeated lookup and updating become more
  awkward
- a dictionary fits direct lookup and direct update more naturally
- the same scenario can be modeled in more than one way
- representation changes how much searching the code has to do
- the best structure depends on the operations you perform most often

---

# Demo Evidence

Run `demo_code.py` to produce:

- a side-by-side representation snapshot before and after one new check-in
- a comparison table for the key operations shown in the demo

Students should be able to point to the evidence and explain why the dictionary
representation is easier for direct lookup and updating in this example.

---

# Transfer Bridge

> In the demo, we compared list and dictionary representations for attendance
> tracking. In the lab, students will compare two different structures for a
> different data-management scenario and justify the better fit using specific
> operations.

---

# Stop Point

Stop after showing how one new attendance check-in changes each structure and
how that affects lookup. Do not expand the demo into a full inventory, contact,
menu, ticket, or registration solution. Students still need to choose and
justify their own scenario.

---

# Likely Misconceptions

- students may choose a structure only because it is familiar
- students may describe a structure as "better" without naming the operation
  pattern that makes it better
- students may assume two structures are interchangeable because both can store
  the same information
- students may ignore that code clarity also changes with representation

---

# Instructor Notes

- Keep the discussion focused on operations such as add, lookup, and update.
- Use the list version to make the repeated scan visible.
- Emphasize that the list is not wrong. It is just less convenient for this
  access pattern.
- Remind students that their lab comparison table needs specific operations,
  not only a general opinion.