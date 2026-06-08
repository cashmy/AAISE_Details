# Deck Source Continuity Brief

**10-152-117 Python Programming**

---

# Purpose

This governance artifact preserves the updated direction for refactoring the
Python slide deck artifacts after completion of the `10-152-119 Algorithmic
Problem Solving` deck source system.

The Python deck set was created earlier and remains structurally useful, but it
now needs a stronger production-guidance layer. The goal is not to redesign the
course. The goal is to apply the strongest lessons from the Algorithms deck
source process while preserving the Python course's different rhythm, skill
sequence, and assignment pattern.

This brief should be used before revising any Python slide deck artifact.

---

# Confirmed Course Rhythm

The course meets three days per week:

- Monday
- Tuesday
- Thursday

Each session is approximately two hours. The current slide deck system is
organized as one deck per class meeting:

```text
SD_W01D01_<main_topic>.md
SD_W01D02_<main_topic>.md
SD_W01D03_<main_topic>.md
...
SD_W08D03_<main_topic>.md
```

For now, preserve the lecture-each-day model.

Each deck should support approximately:

- 45-60 minutes of lecture, explanation, and demonstration
- a short review or bridge from prior work
- one or more small instructor demos
- guided practice or lab transition time
- remaining class time for student work, questions, and individual support

Do not convert the Python course into the Algorithms weekly deck model unless
the instructional schedule is intentionally redesigned later.

---

# Current Deck Status

Existing slide deck artifacts are located in:

```text
Slide_Decks/Week_01
Slide_Decks/Week_02
Slide_Decks/Week_03
Slide_Decks/Week_04
Slide_Decks/Week_05
Slide_Decks/Week_06
Slide_Decks/Week_07
Slide_Decks/Week_08
```

There are currently 24 day-level deck artifacts:

| Week | Deck Count | Existing Structure |
| --- | ---: | --- |
| Week 1 | 3 | First programs and basic values |
| Week 2 | 3 | Decisions and repetition |
| Week 3 | 3 | Functions, lists, dictionaries, structure |
| Week 4 | 3 | Debugging, testing, code literacy |
| Week 5 | 3 | Files, errors, persistence, data representation |
| Week 6 | 3 | APIs, external data, app architecture recognition |
| Week 7 | 3 | RBA and capstone framing |
| Week 8 | 3 | Capstone build, revision, presentation, ownership |

These decks are valid as early artifacts. They should be treated as
historical-footprint documents and alignment anchors, not as final production
deck sources.

---

# Source Artifacts To Treat As Canonical

Use these Python artifacts as the primary local context before revising decks:

- `Assignment_Week_Day_Matrix.md`
- `Lecture_Content_and_Demo_Alignment_Matrix.md`
- `IIM_Instructional_Intent_Map.md`
- `MRS-Py_Master_Rubric_System.md`
- `LS_Lab_System.md`
- `APL_Assignment_Progression_Ladder.md`
- `Conceptual_Understanding_vs_Logic_Regurgitation_Principle.md`
- `Assignments/LDP-Py_Lab_Demo_Prompt_Pack.md`
- `Slide_Decks/STD-Py_Alignment_Based_Slide_Deck_Template.md`
- `Slide_Decks/Slide_Deck_System_Meta_Review.md`

Use these Algorithms artifacts as pattern references, not as content sources:

- `10-152-119_Intro_To_Algorithms/Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Deck_Sources/Week_01_Deck_Source_Algorithms_Precision_and_Correctness.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Deck_Sources/Week_02_Deck_Source_Growth_and_Big_O_Intuition.md`

The Python course should borrow the deck-source discipline, not the Algorithms
course's weekly pacing or assessment model.

---

# Major Difference From Algorithms

The Algorithms course uses:

- 8 weekly lecture deck sources
- one primary lab per week for Weeks 1-7
- a two-part final in Week 8
- heavier conceptual synthesis per deck

Python uses:

- 24 day-level decks
- 16 assignments across 8 weeks
- many intentionally small demos
- a capstone assigned early enough to allow independent build time
- a stronger skill-acquisition and fluency-building rhythm

Therefore, Python decks should be more compact than Algorithms deck sources,
but more specific than the current conceptual slide anchors.

---

# Assignment Pattern To Preserve

The current assignment map is intentional:

| Week | Assignment Pattern |
| --- | --- |
| Week 1 | A1 only |
| Week 2 | A2 and A3 |
| Week 3 | A4 and A5 |
| Week 4 | A6 and A7 |
| Week 5 | A8, A9, and A10 |
| Week 6 | A10, A11, and A12 |
| Week 7 | A13 and A14 |
| Week 8 | A15 and A16 |

Important capstone note:

- A14 is assigned in Week 7 so students can gain approval early.
- A15 is the capstone build.
- A16 is the AI-use justification and final presentation.
- Week 8 should protect time for building, validating, revising, and explaining.

Do not collapse the 16-assignment structure merely to resemble Algorithms.

---

# Refactor Goal

The revised deck sources should improve:

- slide-level specificity
- instructor-note clarity
- demo-to-lab transfer
- visual prompt usefulness
- predictable review and bridge structure
- README and GitHub submission expectations
- AI-use framing and evidence requirements
- handoff quality for future instructors

The revised deck sources should not become:

- full lecture transcripts
- dense textbook replacements
- code dumps
- rigid scripts that prevent live teaching judgment
- generic Python tutorial slides

---

# Recommended Revised Deck Source Structure

Each revised day-level deck source should include:

1. Deck metadata
2. Session purpose
3. Course position / prior bridge
4. Assignments supported
5. Readiness target
6. Primary watch point
7. Demo set for the session
8. Student lab or hands-on bridge
9. Slide sequence overview
10. Slide-by-slide source blocks
11. Demo execution notes
12. Lab / assignment bridge
13. README / submission expectations when relevant
14. AI-use boundary when relevant
15. Image prompt notes
16. Instructor timing notes
17. Post-lecture notes

This structure may remain lighter than the Algorithms deck source structure,
but it should be specific enough that the instructor can build a PowerPoint
deck without reconstructing the intent from scattered artifacts.

---

# Slide-Level Block Requirements

Each slide block should include:

- slide number and title
- delivery category
- student-visible slide text
- instructor notes
- transition cue
- visual notes when useful
- demo connection when applicable
- lab or assignment connection when applicable

Recommended delivery categories:

- Core
- Optional
- Reserve
- Demo
- Lab Bridge
- Review
- Assessment / Evidence

Use one clear instructional job per slide.

---

# Slide Count Guidance

The older Python template recommended 7-9 slides with a soft maximum of 10.
That guidance preserved simplicity, but it may now be too compressed for
PowerPoint production and instructor handoff.

Use this revised guidance:

- target range: 10-16 source slides per day
- soft maximum: 18 source slides
- shorter decks are acceptable when the session is lab-heavy
- longer decks require clear optional or reserve labeling

The final PowerPoint may use fewer slides than the source if the instructor
combines ideas visually. The source artifact may preserve additional guidance
for handoff and future revision.

---

# Stable Python Session Flow

Use this recurring micro-arc:

```text
brief review / prior lab bridge
-> today's capability
-> concept in plain language
-> syntax or structure shape
-> instructor demo
-> common beginner failure
-> corrected or improved version
-> hands-on bridge
-> README / evidence expectation when relevant
-> AI-use boundary when relevant
-> success check
```

Not every session needs every element, but every session should preserve:

- what students are learning to do
- how they will see it demonstrated
- how they will practice it
- what evidence shows they succeeded

---

# Demo Handling Rules

Python has a high number of intentionally small demos. That is a strength if
the demos are handled as teaching moves rather than a checklist.

For each day-level deck, identify:

- primary demo
- optional supporting demo(s)
- demos to skip if students need more lab time
- demo section that should be typed or pasted live
- demo section that should be explained rather than fully typed
- likely student confusion point exposed by the demo

Use this distinction:

- Demo code teaches the concept.
- Lab code lets students transfer the concept.
- Success examples validate assignment scope.
- Starter code should scaffold only where it does not steal the learning.

The demo should be similar enough to the lab for transfer, but not so identical
that students can mindlessly copy.

---

# Lab and Assignment Bridge Rules

Every deck should explicitly state which assignment it supports.

For decks that launch or continue a lab, include:

- what students should start today
- what they should have completed by the end of the session
- what evidence they should preserve
- what README or explanation element is expected
- what AI use is allowed or discouraged

For decks that support multiple assignments, name the boundary clearly:

```text
This concept supports A8 directly.
This preview prepares A10, but A10 remains recognition-level.
```

This prevents bridge topics from becoming hidden requirements.

---

# GitHub, README, and Evidence Integration

The current Python course conceptualized GitHub and documentation expectations,
but they are not as fully defined as the later Algorithms system.

Future deck refactors should backfill a light but consistent evidence pattern:

- code file(s)
- sample run output or screenshots when appropriate
- short README explanation
- test or validation evidence when appropriate
- AI-use note when AI materially helped
- reflection or justification when required by the assignment

Early weeks should keep README expectations very small. Later weeks can require
more complete documentation.

Do not overload Week 1 students with professional documentation complexity.
Introduce the expectation gradually and repeatedly.

---

# AI-Use Framing

Preserve the course-wide student-facing AI progression:

1. Manual first
2. AI-assisted for explanation, clarification, and limited research
3. AI-injected only when students justify and explain output
4. AI-integrated only when the task and maturity level make it appropriate

For Python 117, the strongest principle is:

```text
Conceptual understanding matters more than logic regurgitation.
```

Decks should reinforce that students must understand:

- what the program is supposed to do
- what the inputs and outputs are
- what each major step is responsible for
- how they know it worked
- what AI contributed if AI was used
- why the final output is acceptable

AI should not be framed as a shortcut around reading, tracing, explaining, or
testing.

---

# Student Anxiety and Beginner Framing

Python 117 includes many students who may be early in their programming
identity. Decks should repeatedly normalize:

- small wins
- visible output
- mistakes as evidence
- tracing before guessing
- debugging as investigation
- code reading as a learnable skill
- revision as learning, not failure

Avoid language that implies students should already "just know" syntax,
environment setup, GitHub, APIs, JSON, testing, or project scope control.

---

# Sanity-Check Gate Before Deck Refactor

Before refactoring any deck, check:

1. Which assignment(s) does this session support?
2. Which demos are currently mapped?
3. Are the demos too many, too large, or appropriately small?
4. Does the deck support a one-hour lecture target?
5. Does the deck preserve enough lab time?
6. Is the slide text too conceptual or too generic?
7. Is there a common beginner failure that should be made explicit?
8. Is there a README / evidence expectation for this point in the course?
9. Is AI use relevant for this session?
10. Does the deck need an image prompt note?

If these cannot be answered from local artifacts, inspect the lecture outline,
assignment, demo folder, and success example before revising.

---

# Recommended Refactor Order

Use Week 1 as the pilot.

Recommended first pass:

1. Sanity-check Week 1 assignments, demos, success example, and decks.
2. Refactor `SD_W01D01_What_a_Python_Program_Does.md`.
3. Validate whether the new structure is too heavy, too light, or just right.
4. Refactor Week 1 Day 2 and Day 3 using the same pattern.
5. Update this brief if the pilot reveals a better stable structure.
6. Proceed week by week.

Do not refactor all 24 decks in one blind pass.

---

# Historical Artifact Rule

Existing deck files should not be dismissed simply because they are less
specific than the newer Algorithms sources.

They are valuable because:

- they preserve the original instructional intent
- they show the earlier state of the course design
- they reveal whether later revisions are drift or evolution
- they provide actual data for sanity checks

When a deck is heavily refactored, preserve the old version only if it provides
meaningful design-history value. Otherwise, update in place with careful scope
control.

---

# Working Definition of "Complete Enough"

A revised Python deck source is complete enough when an instructor can answer:

- What is today's teaching responsibility?
- What prior work does it review or bridge from?
- Which assignment does it support?
- Which demo should be shown?
- What should students do after the demo?
- What mistake or misconception should be anticipated?
- What evidence should students preserve?
- What should be said about AI, if anything?
- What does success look like by the end of the session?

If those questions are clear, the deck source is doing its job.

