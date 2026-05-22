# LAB 03 SUCCESS NOTES - DATA STRUCTURE CHOICE

This package shows one acceptable successful version for Lab 03. It is not the
only correct answer because the student-facing lab allows multiple scenarios and
structure pairings.

---

# Assumptions

- fresh `Assignments/Lab_03/` package
- student-facing Lab 03 file treated as authoritative
- generic starter rather than scenario-specific scaffolding
- demo scenario different from the withheld success-version scenario
- comparison table used as the main evidence format

---

# Chosen Scenario

Simple contact lookup

Structures compared:

- list of dictionaries
- dictionary of dictionaries

This stays in the same concept family as the lab while remaining different from
the attendance-tracking demo.

---

# Problem Statement

Store and manage a small contact list so a user can add a contact, look up a
contact by name, update a phone number, and display all contacts.

The successful version solves the same problem with two different data
representations and compares which one better fits the task.

---

# Inputs and Outputs

## Inputs

- contact records with `name`, `phone`, and `email`
- operation requests such as add, lookup, update, and display

## Outputs

- updated data structures
- operation evidence for both representations
- a comparison table
- a short recommendation

---

# Assumptions and Tradeoffs

- each contact name is treated as a unique key in the dictionary representation
- both structures contain equivalent contact information before comparison
- direct lookup by name matters more in this scenario than preserving a simple
  list-only representation
- the list-of-dictionaries structure is still readable, but it requires
  scanning for lookup and update operations
- the dictionary-of-dictionaries structure makes direct lookup and update
  easier, but display formatting may require a little more work

---

# Evidence Included

`success_solution.py` prints:

- operation evidence showing both structures after add, lookup, update, and
  display work
- a comparison table with operation-by-operation fit statements
- a concise recommendation naming the better overall structure

This aligns to the student-facing requirement for implementation or simulation,
three compared operations, a comparison table, and a final recommendation.

---

# Recommendation Summary

The dictionary-of-dictionaries structure is the better overall fit for this
scenario because the main access pattern is direct lookup and update by name.

The list-of-dictionaries structure still works, but it is less convenient when
the most common operations require finding one contact quickly.

---

# AI-Use Accountability Example

Lab 03 starts manually and allows AI only after the student has selected the
two structures and written an initial comparison.

Example disclosure a student could make:

> After writing my first comparison, I asked AI to critique whether a dictionary
> was really a better fit than a list for contact lookup. AI suggested that the
> keyed lookup pattern matched the dictionary better. I accepted that point only
> after checking my own add, lookup, and update operations and rewriting the
> final recommendation in my own words.

---

# Rubric Categories Illustrated

- `T2` Data Structures and Representation
- `T3` Algorithm Implementation and Testing
- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly