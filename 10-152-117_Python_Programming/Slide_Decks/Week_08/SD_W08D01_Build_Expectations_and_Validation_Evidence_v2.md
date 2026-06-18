# Slide Deck Source - Week 8 Day 1

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 8 / Monday  
**Date:** October 5, 2026  
**Weekly Theme:** Capstone Build, Justification, and Presentation  
**Lecture Title:** Build Expectations and Validation Evidence  
**Session Type:** Required lecture plus capstone build work  
**Assignments Supported:** A15 - Capstone Build  
**Readiness Target:** Students can identify what part of their project matters most and how they will verify it.  
**Primary Watch Point:** Do not assume students know what validation evidence looks like unless modeled explicitly.

---

# Session Purpose

This is the main Week 8 lecture.

Students should already have an approved or provisionally approved capstone path
from Week 7. This session converts that approval into final build behavior:

- stay inside approved scope
- build the smallest meaningful working core
- collect validation evidence while building
- preserve run instructions and AI-use notes

The lecture should be compact so students retain meaningful capstone build time.

---

# Review / Prior Work Bridge

Review from Week 7:

- A14 defined project scope and approval boundaries.
- A15 began for approved or provisionally approved projects.
- The first build target should be small, testable, and explainable.

Bridge question:

> What makes a capstone project defensible, not merely runnable?

Today's answer:

> A defensible project has working behavior, validation evidence, run guidance,
> and an explanation the student owns.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 8

Today's reading focus:

- testing your application
- troubleshooting guidelines
- README/project layout guidance

Use this reading to support:

- capstone expectations
- validation evidence
- clear run instructions

Skim or save for later:

- advanced type hints
- static type checking
- package publishing
- performance profiling

---

# What We Will Use Today

Today we will use:

- approved scope
- smallest working core
- validation evidence
- expected versus actual output
- run instructions
- AI-use notes

Today we will not use:

- unapproved feature expansion
- presentation polish before the project runs
- package publishing
- advanced performance profiling

---

# Assignments Supported

Primary assignment:

- A15 - Capstone Build

Day 1 supports:

- final build focus
- validation evidence
- run instructions
- scope discipline

A16 is previewed only as a reason to preserve explanation and evidence while
building.

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/01_capstone_validation_example.py`
- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/02_capstone_validation_notes.md`
- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/06_run_instructions_example.md`

Optional preview:

- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/03_ai_use_justification_example.md`

---

# Capstone Support Artifacts For Week 8

These artifacts are not all full demos. They are final-work support models that
students can reference while finishing A15 and preparing A16.

Use directly on Day 1:

- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/02_capstone_validation_notes.md`
- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/06_run_instructions_example.md`

Preview or point to as needed:

- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/03_ai_use_justification_example.md`
- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/04_final_presentation_outline.md`
- `Demos/Week_08_Capstone_Build_Justification_and_Presentation/05_revision_after_reality_contact_example.md`

The goal is to reduce ambiguity around evidence, run guidance, AI-use
justification, revision notes, and presentation structure.

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-2 | Connect approval to defensible build work |
| Core Build Focus | 3-6 | Define meaningful behavior and validation evidence |
| Demo / Evidence | 7-8 | Model validation and run instructions |
| Assignment Bridge | 9-10 | Move students into A15 build work |
| Close | 11 | Define Monday success |

---

## Slide 1 - Finishing Code Is Not Enough

**Delivery Category:** Core

**Student-Visible Text:**

A capstone is not finished just because the code runs once.

It should run inside approved scope, produce meaningful behavior, and include
evidence that important behavior was checked.

**Instructor Notes:**

Open on quality and explainability. This should not sound like extra paperwork;
it is part of finishing well.

**Transition Cue:**

Connect this immediately to the Week 7 approval process: approved scope is only
useful if the final build can be defended.

---

## Slide 2 - From Approved Scope To Build Evidence

**Delivery Category:** Review

**Student-Visible Text:**

Week 7 approved the project direction.

Week 8 asks: what did you build, how do you know it works, and how can someone
else understand how to run it?

**Instructor Notes:**

Tie A14 directly into A15.

**Transition Cue:**

Now name the success pattern for today's build work so students know what to
prioritize during lab time.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

- stay inside approved scope
- identify the most important behavior
- validate that behavior with real evidence
- preserve run instructions
- record meaningful AI help if used
- prepare to explain the work in A16

**Instructor Notes:**

Ask students to write down the most important behavior for their own capstone.
That behavior becomes the anchor for validation, run instructions, and
presentation explanation.

**Transition Cue:**

Once the important behavior is named, show that evidence can be small and still
valid.

---

## Slide 4 - Evidence Can Be Small And Real

**Delivery Category:** Core

**Student-Visible Text:**

Validation evidence can be simple:

- expected versus actual output
- one successful run
- one boundary or error case
- short validation note
- screenshot or copied console output if required

Small evidence is acceptable when it is real.

**Instructor Notes:**

This demystifies validation. Do not turn it into a full testing lecture.

**Transition Cue:**

Evidence is useful to the instructor, but run instructions are what make the
project understandable to another person.

---

## Slide 5 - Run Instructions Are Part Of The Project

**Delivery Category:** Core

**Student-Visible Text:**

A project should tell someone how to run it.

Good run instructions include the file to run, required data files, setup notes
if needed, and the expected result.

**Instructor Notes:**

This prepares A16 and helps grading.

**Transition Cue:**

If AI helped during the build, the notes should be collected now while the
decisions are still fresh.

---

## Slide 6 - AI Notes Belong With The Build

**Delivery Category:** Core

**Student-Visible Text:**

If AI helped during the build, record it while the work is fresh.

Useful notes include what AI suggested, what you accepted, what you changed, and
how you verified the result.

**Instructor Notes:**

This prevents weak after-the-fact AI justification.

**Transition Cue:**

Now model the relationship between behavior and validation evidence.

---

## Slide 7 - Demo: Validation Evidence

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the behavior first.

Then watch the evidence that supports the claim that the behavior works.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_08_Capstone_Build_Justification_and_Presentation\01_capstone_validation_example.py`

Then use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_08_Capstone_Build_Justification_and_Presentation\02_capstone_validation_notes.md`

Run the validation example and connect it to `02_capstone_validation_notes.md`.

**Demo Connection:**

Primary demo files: `01_capstone_validation_example.py`,
`02_capstone_validation_notes.md`

**Transition Cue:**

After showing evidence, show the support artifact that helps someone else run
the project.

---

## Slide 8 - Demo: Run Instructions

**Delivery Category:** Demo

**Student-Visible Text:**

Run instructions should reduce confusion.

They should tell someone what to open, what to run, what files are needed, and
what successful output looks like.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_08_Capstone_Build_Justification_and_Presentation\06_run_instructions_example.md`

Show `06_run_instructions_example.md`.

Optional preview if useful:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_08_Capstone_Build_Justification_and_Presentation\03_ai_use_justification_example.md`

**Demo Connection:**

Primary demo artifact: `06_run_instructions_example.md`

**Transition Cue:**

Now convert the examples into the A15 build checklist students should use during
work time.

---

## Slide 9 - A15 Build Checklist

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For A15, focus on:

- approved scope
- working core behavior
- organized code
- data files if needed
- validation evidence
- run instructions
- AI-use notes if used

**Instructor Notes:**

This is the transition into work time.

**Transition Cue:**

Make the immediate target small enough that students can act on it before class
ends.

---

## Slide 10 - Today's Work Target

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Before class ends, try to have:

- one important behavior working or clearly attempted
- one validation note started
- README/run instructions started
- one next-step decision identified

**Instructor Notes:**

This gives a realistic day-one finish line.

**Transition Cue:**

Close quickly so students can move into build work with a concrete target.

---

## Slide 11 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> I know the most important behavior in my project, and I have started proving
> that it works.

**Instructor Notes:**

Close quickly and move to build support.

---

# Demo Execution Notes

Recommended order:

1. Show the behavior in `01_capstone_validation_example.py`.
2. Show how `02_capstone_validation_notes.md` records evidence.
3. Show `06_run_instructions_example.md`.
4. Mention AI-use notes only as needed, or preview `03_ai_use_justification_example.md`.

---

# Lab / Assignment Bridge

Students should spend most of the session on A15.

Instructor support should focus on:

- scope containment
- first working behavior
- validation evidence
- README/run instructions
- AI-use accountability

---

# README / Submission Expectations

Recommended capstone README sections:

```text
# Capstone Project

## Purpose

## Approved scope

## How to run

## Sample input/output

## Validation evidence

## Revisions or changes

## AI-use notes
```

---

# AI-Use Boundary

AI may help with debugging, comparison, refactoring suggestions, wording, or
structure review.

Students must still:

- keep the build aligned to approved scope
- inspect generated code
- test important behavior
- explain final decisions
- disclose meaningful AI assistance

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Code plus evidence | Running code paired with validation note | Avoid legal/audit look |
| 2 | Scope to evidence | Approved scope leading to build evidence and run guidance | Avoid paperwork feel |
| 3 | Today's success pattern | Scope, core behavior, validation, run instructions, AI notes, explanation | Avoid feature-sprawl imagery |
| 4 | Validation types | Expected/actual, run output, boundary check cards | Keep simple |
| 5 | Run instructions | Project folder with README/run steps | Avoid file explorer clutter |
| 6 | AI notes | AI contribution accepted, changed, verified, and explained | Avoid robot-centered imagery |
| 7 | Validation demo | Behavior connected to validation notes | Avoid testing-framework complexity |
| 8 | Run instructions demo | README/run instruction support artifact | Keep readable |
| 9 | A15 checklist | Compact build checklist | Avoid compliance styling |
| 10 | Work target | Four small day-one work targets | Avoid urgency/panic styling |
| 11 | Success check | Core behavior with evidence started | Keep simple |

---

# Instructor Timing Notes

Suggested timing:

- Opening and review: 5-8 minutes
- Core lecture: 15-20 minutes
- Demos: 10-15 minutes
- A15 work time: remaining time

This should be the only required lecture of Week 8.

---

# Post-Lecture Notes

Use after teaching:

- Did students start validation evidence early enough?
- Did run instructions remain clear and small?
- Which projects still need scope control?
- Which students may need Tuesday presentation staging?
