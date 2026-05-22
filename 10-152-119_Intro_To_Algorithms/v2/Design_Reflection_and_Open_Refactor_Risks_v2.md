# Design Reflection and Open Refactor Risks v2

## Purpose

This artifact captures the current reflection point for
`10-152-119 Algorithmic Problem Solving` so that downstream work does not rely
on conversation history.

The current architecture is strong enough to pause and proceed later into demo
coding, lab solutions, starter files, and lecture slide decks. However, several
design risks may require refactoring once concrete materials are built.

## Current Stable Decisions

The course is currently designed as an 8-week compressed course.

The stable structure is:

- Labs 1-7 form the graded lab progression.
- Week 8 is not a full additional lab week.
- Week 8 uses one final synthesis/demo practice day.
- The last two class days are reserved for the two-part final:
  - Part 1 - Applied Solution Set
  - Part 2 - Personalized Explanation Defense

The course is not web-based by default.

Python remains the primary implementation language.

The textbook is a reference spine, not a full coverage contract.

AI use follows the program model:

```text
Manual First -> AI-Assisted -> AI-Injected -> AI-Integrated
```

For this course, AI-Integrated remains optional or preview-level.

## Completed Artifact State

The active course system now includes:

- high-level course plan
- unit and week descriptions
- WIDS course competency framework
- IIM matrix in Markdown and spreadsheet form
- textbook coverage and reference map
- lab assignment system overview
- lab progression ladder
- Labs 1-7
- Week 8 final synthesis demo/practice artifact
- final assessment model
- WIDS-friendly final assessment rubric
- lab/demo prompt pack for later Codex-supported development
- master rubric system
- lecture outline template
- weekly lecture outlines for Weeks 1-8

## Pending Build Tasks

The next major work phases are:

1. Build demo code and demo notes for Labs 1-7.
2. Build starter files where useful.
3. Build successful versions for Labs 1-7 for post-assignment release.
4. Build final assessment task set and instructor question-generation workflow.
5. Create lecture PowerPoint decks.
6. Refine lecture outlines after demos and decks reveal actual pacing.

## Open Refactor Risk 1 - One Weekly Outline vs Two Sessions

Current state:

- Each week has one weekly lecture outline.
- The outline includes prior-week review, concept frame, demo, lab bridge, AI
  use frame, and checkpoint questions.

Potential issue:

The actual instructional rhythm may work better as two lecture/demo sessions
per week rather than one lecture day and two lab-heavy days.

Possible future model:

```text
Day 1 - review, concept frame, first demo, lab start
Day 2 - targeted review, second concept/demo, lab refinement
Day 3 - lab work, support, evidence review, or final defense activity
```

Why this might be needed:

- each session may need a review bridge
- each session may need a demo
- students may benefit from smaller concept loads
- compressed courses can overload students if lecture is too concentrated

Do not refactor yet.

Trigger for refactor:

- after one or two PowerPoint decks are drafted
- after demo code reveals actual time-on-task
- if a weekly outline becomes too dense to teach in one session

Likely refactor if triggered:

- split each weekly outline into Day 1 and Day 2 outlines
- preserve one weekly overview file if useful
- align Day 1 and Day 2 with demo files and lab checkpoints

## Open Refactor Risk 2 - Algorithm Specificity

Current state:

- Labs and outlines identify algorithm families and evidence types.
- Some exact algorithms, data sets, and code paths are intentionally not locked
  yet.

Potential issue:

The course may not yet be specific enough about the actual algorithms students
will implement, simulate, trace, or compare.

Examples:

- Which exact Big-O timing comparisons will be used?
- Which search/sort examples are required versus optional?
- Which recursion examples are reasonable for this student level?
- Which graph traversal examples are small enough but still meaningful?
- Which similarity/ranking/hashing option should be the standard Week 7 lab?

Do not over-specify from architecture alone.

Trigger for refactor:

- when demo code is created
- when starter files reveal excessive ambiguity
- when a lab solution requires too many unstated assumptions
- when a weekly lecture outline cannot name the exact evidence students will
  produce

Likely refactor if triggered:

- revise each lab to name the exact required algorithm or approved options
- add demo-specific data sets
- add expected evidence templates
- update lecture outlines to reference the exact demo and lab files

## Open Refactor Risk 3 - Topic Breadth and Lecture Granularity

Current state:

- Some lecture topics are intentionally broad at the outline level.
- Big-O, search/sort, graph traversal, and AI/data bridge topics are especially
  broad.

Potential issue:

Some topics may require expanded lecture treatment or more precise topic
boundaries.

Example:

Big-O includes many classifications and ideas:

- constant
- linear
- quadratic
- logarithmic
- best case
- worst case
- average case
- time complexity
- space complexity
- timing evidence versus theoretical analysis

This may be too much for a single generic lecture block unless it is tightly
scoped.

Do not expand all topics preemptively.

Trigger for refactor:

- slide deck drafts expose too much content for one session
- demo code requires more setup than expected
- student-facing readings become too broad
- a topic needs separate "must know", "guided demo", and "reference only"
  layers

Likely refactor if triggered:

- split a weekly lecture into smaller concept modules
- add "Must Know / Guided Demo / Reference Only" sections to lecture outlines
- revise textbook coverage notes for the affected week
- adjust lab requirements to match the narrowed lecture target

## Open Refactor Risk 4 - Final Assessment Timing

Current state:

- Week 8 reserves the last two class days for the final.
- Day 1 is final synthesis demo/practice.

Potential issue:

The final Part 1 solution set and Part 2 explanation defense may require more
or less time than expected depending on the number and size of tasks.

Trigger for refactor:

- final task set takes longer than one class day to complete
- personalized question generation becomes too heavy for instructor workflow
- the online interactive test format requires more setup than expected

Likely refactor if triggered:

- reduce the number of Part 1 tasks
- make Part 2 shorter and more targeted
- prepare reusable question templates by task type
- allow Part 1 submission before the final class session if needed

## Decisions Intentionally Deferred

The following decisions should be made later, after concrete materials exist:

- exact demo code for each week
- exact data sets for each lab
- whether each lab needs starter files
- format and number of successful-version files
- whether lecture decks should be weekly or session-based
- whether Week 7 standardizes on similarity/ranking, clustering, or hashing
- exact final Part 1 task count
- exact Part 2 delivery format in the LMS or other online tool

## Future Work Order Recommendation

Recommended next sequence:

1. Build Lab 1 demo, starter, and successful version.
2. Build Lab 2 demo, starter, and successful version.
3. Draft Week 1 and Week 2 slide decks.
4. Reassess whether weekly outlines should split into Day 1 and Day 2.
5. Continue demo/solution coding for Labs 3-7.
6. Build final Part 1 task set.
7. Build final Part 2 question-generation workflow.
8. Refactor artifacts only where concrete materials expose a real mismatch.

## Reflection Summary

The current design is coherent and ready for a pause.

The most important unresolved question is not whether the course architecture
works. It is whether the actual teaching materials reveal that the architecture
needs finer operational granularity.

The safest approach is to keep the current architecture stable, build one or two
real demo/deck packages, and then refactor from evidence rather than from
speculation.
