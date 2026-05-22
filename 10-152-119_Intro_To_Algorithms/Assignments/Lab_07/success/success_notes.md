# LAB 07 SUCCESS NOTES - SIMILARITY, RANKING, AND HASHING

This package shows one acceptable successful version for Lab 07. It is not the
only correct answer because the student-facing lab allows several approved
options.

---

# Assumptions

- fresh `Assignments/Lab_07/` package
- student-facing Lab 07 treated as authoritative
- generic starter rather than scenario-specific scaffolding
- demo scenario different from the withheld success-version option
- plain primary success version focused on required behavior
- optional colorized success version created because match versus mismatch is a
  meaningful observable distinction for this option

---

# Chosen Option

Hashing demonstration

This successful version compares original and current text records by computing
SHA-256 hashes and checking whether the hashes still match.

This stays in the same AI/data bridge family as the lab while remaining
different from the music-recommendation demo.

---

# Problem Statement

Represent a small set of text artifacts, compute hashes for original and current
versions, and use the comparison to show a simple integrity-checking workflow.

The successful version includes six items, a representation table, a hash
comparison table, assumptions, one limitation/risk, and a connection to data or
AI workflows.

---

# Inputs and Outputs

## Inputs

- six named text records
- original text for each record
- current text for each record

## Outputs

- truncated original and current hash values
- match or mismatch status for each record
- explanation of assumptions and limitations
- AI/data connection statement

---

# Assumptions and Limits

- exact text equality is the right integrity signal for this demonstration
- the same hash function is applied consistently across the original and current
  versions
- a mismatch means the content changed, but it does not explain the meaning or
  importance of that change
- hashing helps with identity and integrity checks, but it does not replace
  human review of why a record changed

---

# Evidence Included

`success_solution.py` prints:

- a data representation table
- a hash comparison table
- assumption and limitation statements
- a short AI/data connection note

This aligns to the student-facing requirement for a data set of at least six
items, representation explanation, visible evidence, assumptions, limitation or
risk, and AI/data connection.

---

# AI-Use Accountability Example

Lab 07 allows AI as a comparison partner after the student has selected the
data, representation, and algorithm idea.

Example disclosure a student could make:

> After building my first hashing example, I asked AI to critique one of my
> assumptions. AI pointed out that a hash mismatch does not tell me whether the
> change is meaningful. I accepted that critique only after checking my own
> records and rewriting the limitation note in my own words.

---

# Rubric Categories Illustrated

- `T5` Observable Algorithm Behavior and Communication Evidence
- `T6` AI/Data Foundations and Responsible Tool Use
- `T2` Data Structures and Representation
- `T3` Algorithm Implementation and Testing
- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `C1` Solve Problems
- `C2` Communicate Clearly
- `C4` Value Learning