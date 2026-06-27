# Deck Source Continuity Brief

**10-152-118 Web Development Foundations**  
**Alternate Title:** HTML, CSS, and JavaScript

**Draft Status:** production continuity guide. Reading assignments are complete; revise only when deck-source production exposes a concrete mismatch.

---

# Purpose

This governance artifact preserves the working direction for creating and
refactoring the Web Development Foundations lecture deck sources.

The goal is not to redesign the course. The goal is to preserve the course's
intentional beginner sequence while applying the strongest deck-source lessons
from:

- `10-152-117 Python Programming Foundations`
- `10-152-119 Algorithmic Problem Solving`

This brief should be used before drafting or refactoring any Web Development
Foundations deck source.

---

# Confirmed Course Identity

Official course title:

```text
10-152-118 Web Development Foundations
```

Alternate title preserved for continuity:

```text
HTML, CSS, and JavaScript
```

The course remains browser-native and beginner-facing.

Do not turn this into:

- a React course
- a Node/full-stack course
- a jQuery course
- a professional front-end specialization course
- an AI-first web-building course

---

# Confirmed Course Rhythm

The course spans a 17-week semester.

Current production target:

- 34 slide decks total
- 2 slide decks per week across 17 weeks
- 16 video-recorded decks
- Monday deck is the primary live lecture/presentation deck
- Wednesday deck is the asynchronous recorded video deck
- Week 17 still has two capstone wrap-up/presentation support decks, but the
  final Wednesday deck may be presentation/troubleshooting support rather than
  a normal concept lecture

Use this rhythm unless the production map is updated:

```text
Monday/live deck
-> Tuesday guided lab
-> Wednesday recorded concept/iteration deck
-> Thursday application/refinement lab
```

Each weekly deck pair should support the same instructional arc:

```text
live framing and first guided capability
-> lab transfer
-> recorded concept deepening and/or iterative development
-> lab refinement and evidence
```

Wednesday decks should remain connected to Monday's live lecture and the
related lab assignment. Depending on the week, the Wednesday recording may:

- deepen a concept students first encountered Monday
- address common issues exposed by the lab
- model a focused iteration from a working MVP
- identify a small backlog item or improvement target
- revise the project/demo and explain the reasoning

The key rule is continuity. Wednesday should feel like the next thoughtful
iteration of the same learning arc, not a disconnected second topic.

---

# Source Artifacts To Treat As Canonical

Use these Web Development Foundations artifacts as primary context before
drafting deck sources:

- `IIM_Instructional_Intent_Map.md`
- `Weekly_Reading_and_Preparation_Guide.md`
- `HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
- `Unit-Week_Descriptions.md`
- `Assignments/Combined_Assignments.md`
- `Lecture_Outlines/Combined_Lectures_Outlines.md`
- `Projects/PageForge_Week_by_Week_Roadmap.md`
- `Projects/PageForge_Instructor_Companion.md`
- `STD_Slide_Template_Design_v1.4.md`
- `Slide_Decks/STD-01_Slide_Template_Design_System.md`, if present
- `118_Lecture_Production_Todo_and_Handoff.md`

Use these as pattern references, not content sources:

- `10-152-117_Python_Programming/Slide_Decks/Deck_Source_Continuity_Brief.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDS-AL_Lecture_Deck_Source_Design_Guide.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDST-AL_Lecture_Deck_Source_Template.md`

Do not derive deck structure from memory alone.

---

# PageForge Handling Rule

PageForge is an instructor-only modeling project.

Use PageForge to:

- model iterative development habits
- show how weekly course ideas can improve a real project over time
- demonstrate scope control, backlog thinking, revision, and explanation
- support instructor planning and demo continuity

Do not use PageForge as:

- a student starter project
- a copyable capstone solution
- a published finished example students can imitate directly
- a replacement for student project ownership

When PageForge appears in a deck source, identify whether it is:

- live demo support
- recorded demo support
- instructor-only notes
- a preserved milestone reference

The student-facing lesson should be the development habit, not the exact
PageForge implementation.

---

# Current Reading Status

The reading layer exists here:

```text
Weekly_Reading_and_Preparation_Guide.md
```

Current status:

- Weeks 1-17 have been instructor-curated.
- The current guide uses `Required`, `Skim`, and `Reference` labels.
- The guide intentionally protects cognitive load because students are also
  beginning Python, Introduction to Security, and English Composition.

Treat the reading guide as the pacing anchor for deck-source production. Do not
reopen the reading curation unless a concrete mismatch appears while building a
deck source.

---

# Reading Alignment Rule

Deck sources must use `Weekly_Reading_and_Preparation_Guide.md` as the
canonical reading-alignment source.

The deck source should translate reading into the beginner path. It should not
copy the textbook's full breadth into slide content.

Every deck source should include a `Reading Alignment` section with:

- assigned week
- related reading entries
- what is `Required`
- what is `Skim`
- what is `Reference`
- what students should not try to master yet
- any reading-to-lab bridge

Use this guiding rule:

```text
Assigned reading prepares students to receive instruction.
It does not replace lecture, demo, lab, or instructor explanation.
```

---

# Next-Reading Slide Pattern

Each deck should include a recurring closing or near-closing slide:

```text
How To Read Next Week's Material
```

This slide should help students interpret the reading labels.

Stable slide pattern:

- **Required:** Read slowly enough to recognize the main idea and vocabulary.
- **Skim:** Look for headings, examples, and terms that feel familiar or
  confusing. Do not memorize.
- **Reference:** Do not read straight through. Return to this during labs when
  you need help.
- **Before next time:** notice one idea that makes sense, one point that feels
  unclear, and one example you want to see worked through.

Add a rotating final line based on the next week:

- Do not try to memorize every tag or property.
- Focus on what the browser is doing.
- Read code examples for intent before syntax.
- Notice the problem the tool solves.
- Keep implementation questions for lab.

Do not invent next-week reading guidance if the curated reading entries are not
available. Use a clearly marked placeholder instead.

---

# Stable Instructional Progression

Preserve the five-phase course structure:

```text
Weeks 1-3   -> Foundations
Weeks 4-7   -> Behavior
Weeks 8-11  -> System Thinking
Weeks 12-15 -> System Integrity
Weeks 16-17 -> Capstone
```

Preserve the central course movement:

```text
structure -> style -> behavior -> systems -> integrity -> capstone ownership
```

Preserve the layer model:

```text
HTML       -> structure and meaning
CSS        -> appearance, layout, responsiveness, and usability
JavaScript -> logic, behavior, interaction, data, and state
Debugging  -> visual inspection, console tracing, browser tools, AI assistance
AI support -> explanation, comparison, refinement, and accountable acceleration
```

---

# Phase-Level Deck Responsibilities

## Phase 1 - Foundations

Weeks 1-3 should build safety, separation, and visible success.

Decks should repeatedly distinguish:

- HTML is structure and meaning.
- CSS is appearance and presentation.
- Layout is structure expressed in space.

Guardrails:

- Do not overload Week 1 with every HTML element.
- Do not turn Week 2 into exhaustive CSS reference.
- Use Week 3 to introduce box/space thinking, Flexbox, and responsiveness
  gently.
- Treat broader layout readings as vocabulary/context unless the lab requires
  direct use.

## Phase 2 - Behavior

Weeks 4-7 should introduce JavaScript separately, then integrate it with the
page.

Guardrails:

- Week 4 is JavaScript as programming. No DOM yet.
- Week 5 is DOM as bridge, not exhaustive DOM API mastery.
- Week 6 is debugging as process, not panic.
- Week 7 is structured behavior: functions, callbacks, and code organization.
- Avoid treating event handling or selector retrieval as a memorization target.

## Phase 3 - System Thinking

Weeks 8-11 should help students move from pages/features to systems.

Guardrails:

- Async should remain conceptual and visible.
- ES modules should be introduced as organization, not professional bundling.
- Data/API work should be small, controlled, and explainable.
- State should focus on remembered information and UI consistency.

## Phase 4 - System Integrity

Weeks 12-15 should improve working systems.

Guardrails:

- Performance should stay practical and observable.
- Security should coordinate with the concurrent Introduction to Security
  course and avoid specialist depth.
- UX refinement should improve usability, not become a design major.
- Forms and capstone planning should set up independent work without
  over-scoping projects.

## Phase 5 - Capstone

Weeks 16-17 should move students from guided build to independent explanation.

Guardrails:

- protect build time
- preserve final explanation requirements
- allow strategic AI use with student control
- require students to explain structure, styling, behavior, debugging, and major
  design decisions

---

# jQuery Handling Rule

jQuery is used as a third-party helper library, similar to adding a package to a
Python program.

Students are not learning jQuery as the main way to write JavaScript.

Decks should frame jQuery as:

- library recognition
- `<script>` loading awareness
- a helper for selected DOM/event tasks
- a comparison point against vanilla JavaScript
- a safety and dependency conversation when useful

Decks should not frame jQuery as:

- required fluency
- the default implementation model
- a replacement for understanding the DOM
- a second full syntax universe to memorize

Preferred phrasing:

```text
Vanilla JavaScript is the foundation.
jQuery shows how a helper library can shorten common tasks.
Read it for recognition and leverage, not memorization.
```

---

# Recommended Deck Source Structure

Each deck source should include:

1. Deck metadata
2. Session type: Monday live or Wednesday recorded
3. Lesson purpose
4. IIM alignment
5. Reading alignment
6. Review / prior work bridge
7. What we will use today
8. What we will not use yet
9. Assignments supported
10. Readiness target
11. Primary watch point
12. Demo set for the session
13. Slide sequence overview
14. Slide-by-slide source blocks
15. Demo execution notes
16. Lab / assignment bridge
17. Evidence / submission expectations
18. AI-use boundary when relevant
19. How to read next week's material
20. Image prompt notes
21. Instructor timing notes
22. Post-lecture notes

This can be lighter than the Algorithms deck source when the session is
lab-heavy or conceptually simple. It should still be specific enough that an
instructor can build a PowerPoint deck without reconstructing intent from
scattered files.

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
- Review
- Reading Review
- Demo
- Browser / DevTools
- Lab Bridge
- Recording Cue
- Evidence / Submission

Use one clear instructional job per slide.

---

# Student-Visible Text Guidance

Student-visible text should be concise, but not cryptic.

Use enough text for students to understand the slide after the recording or
after class, especially when the slide introduces:

- a new mental model
- a new vocabulary term
- a common beginner mistake
- a reading-to-lab bridge
- a debugging process
- an evidence expectation

Avoid:

- dense textbook copying
- exhaustive syntax tables
- long lists of HTML tags, CSS properties, DOM methods, or event types
- slogan-only slides that require the instructor's fresh memory

Preferred pattern:

```text
anchor idea
-> short clarifying sentence
-> small concrete example
```

---

# What We Will Use Today Rule

Every deck should name the working set for the session.

Use this pattern:

```text
Today we will use:
- concept / syntax / tool
- concept / syntax / tool

Today we will not use yet:
- related topic from the reading
- tempting but premature tool
- deeper syntax that appears in the textbook
```

This is especially important because the textbooks often include more depth
than a beginner class session should carry.

---

# Demo and Lab Alignment Rules

Each deck should preserve near transfer:

```text
lecture concept
-> instructor demo with similar concept
-> student lab with related but different task
```

The demo should:

- make the concept observable
- produce a visible browser result or console result
- be close enough for transfer
- remain different enough to prevent copying
- expose one likely beginner confusion point

The lab bridge should:

- name the related lab or assignment
- state what students must adapt
- identify required evidence
- remind students what is optional or not yet expected
- include AI-use boundaries when relevant

---

# Debugging and Evidence Expectations

Decks should treat debugging as a repeating course identity, not a single Week
6 topic.

Evidence may include:

- working page or feature
- screenshot of browser result
- console output
- before/after screenshot
- short README explanation
- bug/fix explanation
- validation note
- AI-use note when AI materially helped

Early evidence expectations should be small. Later weeks can require more
complete explanation.

---

# AI-Use Framing

Preserve the course-wide student-facing AI progression:

```text
manual native work -> assisted explanation/debugging -> strategic capstone use
```

AI may support:

- explanation
- debugging
- comparison
- refinement
- capstone acceleration

AI should not replace:

- student design judgment
- basic HTML/CSS/JS authorship
- debugging evidence
- final explanation of how the system works

Deck sources should include AI-use boundaries only when relevant. Do not force
AI discussion into early lessons where it distracts from manual first-contact
learning.

---

# Image Prompt Workflow

Images should support a slide's instructional job, not merely decorate the
deck.

Use `Image Prompt Notes` inside each deck source as a compact visual planning
table.

When image generation is needed, create a separate companion artifact after the
deck source is stable.

Recommended naming pattern:

```text
Week_01_Image_Prompts.md
Week_02_Image_Prompts.md
```

The companion artifact should include:

- image title
- slide or section supported
- instructional purpose
- constrained image prompt
- style consistency notes
- negative constraints
- save filename recommendation
- alt-text draft or alt-text intent

---

# Timing and Recording Notes

Because the course uses live and recorded decks, each deck source should include
timing and recording guidance.

Timing notes should identify:

- target duration
- compressible sections
- optional/reserve slides
- likely student pause points
- demo segments that may run long

Recorded Wednesday decks should include:

- clearer self-contained transitions
- fewer live-discussion dependencies
- explicit reading and lab bridge cues
- short pauses for students to try or predict
- reminders about what not to memorize yet
- a clear connection back to Monday's concept and the related lab
- either concept deepening, iterative development, or both

---

# Drift Risks To Avoid

Avoid these risks during Web Development Foundations deck production:

- treating the reading guide as an exhaustive textbook coverage mandate
- turning Week 5 into a DOM API survey
- turning jQuery into the course's main JavaScript model
- bringing AI use too early
- teaching React, Node, build tools, or full-stack workflow
- making Flexbox/media queries feel like mastery targets in first exposure
- overloading students who are also starting Python, Security, and English
  Composition
- making the demo identical to the lab
- omitting evidence expectations
- omitting the next-reading guidance slide
- writing instructor notes that only make sense while the design conversation is
  fresh

---

# Required Pre-Drafting Check

Before drafting any deck source, confirm:

1. Week number and session type: Monday live or Wednesday recorded
2. IIM purpose for that week/session
3. curated reading entries for that week
4. related assignment or lab
5. expected demo
6. what students should be able to do after the session
7. what is explicitly not required yet
8. evidence/submission expectation
9. AI-use boundary, if relevant
10. whether a next-reading slide can be filled or needs a placeholder

If these cannot be answered from local artifacts, inspect the reading guide,
lecture outline, assignment, and project roadmap before drafting.

---

# Recommended Production Order

Use Week 1 as the pilot for the Web Development Foundations deck-source
pattern.

Recommended first pass:

1. Confirm Week 1 live/recorded deck split.
2. Sanity-check Week 1 reading, assignment, and lecture outline.
3. Draft Week 1 Monday live deck source.
4. Draft Week 1 Wednesday recorded concept/iteration deck source.
5. Validate whether the structure is too heavy, too light, or just right.
6. Update this brief if the pilot reveals a better stable pattern.
7. Proceed through Weeks 2-4 before later batches.

Do not refactor all 34 decks in one blind pass.

---

# Working Definition of Complete Enough

A Web Development Foundations deck source is complete enough when an instructor
can answer:

- What is this session's teaching responsibility?
- What prior work does it review or bridge from?
- Which reading entries support it?
- Which assignment or lab does it support?
- Which demo should be shown?
- What should students do after the demo?
- What mistake or misconception should be anticipated?
- What evidence should students preserve?
- What should be said about AI, if anything?
- What should students read next, and how should they read it?
- What does success look like by the end of the session?

If those questions are clear, the deck source is doing its job.
