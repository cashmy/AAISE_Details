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
- individual files in `Assignments/`
- `Assignments/Success_Solutions/`
- `Demos/`
- `STD_Slide_Template_Design_v1.4.md`
- `Slide_Decks/STD-01_Slide_Template_Design_System.md`, if present
- `118_Lecture_Production_Todo_and_Handoff.md`

Use these as informative historical or aggregate references, not canonical
production sources:

- `Assignments/Combined_Assignments.md`
- `Lecture_Outlines/Combined_Lectures_Outlines.md`
- earlier lecture outlines or first-round deck drafts
- `Projects/PageForge_Week_by_Week_Roadmap.md`
- `Projects/PageForge_Instructor_Companion.md`

Use these as pattern references, not content sources:

- `10-152-117_Python_Programming/Slide_Decks/Deck_Source_Continuity_Brief.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDS-AL_Lecture_Deck_Source_Design_Guide.md`
- `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDST-AL_Lecture_Deck_Source_Template.md`

Do not derive deck structure from memory alone.

---

# Historical Artifact Handling Rule

Historical artifacts are useful because they preserve early decisions, draft
language, and possible examples.

They are not automatically canonical.

When historical artifacts conflict with newer course-production artifacts, use
the newer sources in this order:

1. `IIM_Instructional_Intent_Map.md`
2. `Weekly_Reading_and_Preparation_Guide.md`
3. current individual assignment files
4. `Demos/`
5. `Assignments/Success_Solutions/`
6. this continuity brief
7. `118_Lecture_Production_Todo_and_Handoff.md`

Use older outlines and aggregate files only to recover intent or phrasing that
still matches the current course plan.

---

# PageForge Handling Rule

PageForge is an instructor-only modeling project.

PageForge is optional enrichment for deck-source production.

Use PageForge when time and weekly fit allow it to:

- model iterative development habits
- show how weekly course ideas can improve a real project over time
- demonstrate scope control, backlog thinking, revision, and explanation
- support instructor planning and demo continuity

Do not require PageForge in every deck source.

The core lecture deck sequence is complete when it includes:

- reading alignment
- previous lab or success review when applicable
- weekly demo integration
- assignment or lab bridge
- evidence expectations

PageForge recordings may be added later as optional instructor enrichment. They
should not delay core lecture deck production.

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

If PageForge is not used in a deck source, no placeholder is required.

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

Each Wednesday recorded deck should include a recurring closing or near-closing
slide:

```text
How To Read Next Week's Material
```

This slide should help students interpret the reading labels.

Do not duplicate this slide in the Monday live deck. Monday may briefly preview
where the week is going, but the formal next-reading guidance belongs in the
Wednesday recording because that is the final lecture touchpoint before the next
week.

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

Recommended naming pattern:

```text
W01A_HTML_Foundations_Live.md
W01B_HTML_Iteration_Recorded.md
W02A_CSS_Foundations_Live.md
W02B_CSS_Refinement_Recorded.md
```

Use:

- `A` for Monday live decks
- `B` for Wednesday recorded decks
- compact topic names that match the weekly instructional focus

If a week requires a clearer long-form title, use the long-form title in deck
metadata and keep the filename compact.

Each deck source should include:

1. Deck metadata
2. Session type: Monday live or Wednesday recorded
3. Lesson purpose
4. IIM alignment
5. Reading alignment
6. Review / prior work bridge
7. What counts as success today
8. What we will use today
9. Optional scope boundary / what we will not use yet
10. Assignments supported
11. Readiness target
12. Primary watch point
13. Demo set for the session
14. Slide sequence overview
15. Slide-by-slide source blocks
16. Demo execution notes
17. Lab / assignment bridge
18. Evidence / submission expectations
19. AI-use boundary when relevant
20. Image prompt notes
21. Instructor timing notes
22. Post-lecture notes

This can be lighter than the Algorithms deck source when the session is
lab-heavy or conceptually simple. It should still be specific enough that an
instructor can build a PowerPoint deck without reconstructing intent from
scattered files.

---

# Monday Deck Pattern

Monday decks are live presentation decks.

Each Monday deck should normally include a short previous-lab bridge near the
beginning:

```text
Previous Lab Review / Success Path
```

Use this section to:

- review the prior assignment's goal
- show one successful implementation path from `Assignments/Success_Solutions/`
- normalize revision and recovery when appropriate
- connect the previous week's work to the new week's concept
- identify one common issue or improvement opportunity

This review should be focused. It is not a full reteaching of the prior lab.

Recommended Monday flow:

```text
1. Opening / why today matters
2. Previous Lab Review / Success Path
3. Reading-to-concept bridge
4. What Counts As Success Today
5. Today's Toolbox
6. Optional Parked For Later scope boundary
7. New concept explanation
8. Live/manual demo
9. Guided inspection of browser or console result
10. Lab / assignment bridge
11. Evidence expectations
```

For Week 1, there is no prior course lab. Replace the previous-lab bridge with
a course setup / starting-state orientation.

---

# Wednesday Deck Pattern

Wednesday decks are recorded concept-deepening and iterative-development decks.

Each Wednesday deck should connect directly to Monday's concept and the related
lab. Depending on the week, it may:

- deepen Monday's concept
- show a second version of the same demo idea
- model an improvement after a first working version
- address common beginner issues
- connect the demo to Thursday refinement work

Recommended Wednesday flow:

```text
1. Reconnect to Monday
2. Name the working problem or improvement target
3. What Counts As Success Today
4. Review the relevant part of the Monday demo or lab
5. Show the iterative/deepening demo
6. Inspect the result
7. Identify what changed and why
8. Bridge to refinement lab or assignment evidence
9. How to read next week's material
```

Wednesday should not feel like an unrelated second lecture. It should feel like
the next useful iteration.

---

# Demo Integration Rule

The `Demos/` folder is now a canonical deck-production source.

Each deck source should identify:

- demo folder
- demo file or files
- whether the demo is Monday starter, Wednesday iteration, or full-session demo
- where the demo appears in the slide sequence
- which lines or blocks should be typed live
- which larger sections may be pasted for time compression
- what browser, console, or DevTools result should be inspected
- what beginner mistake the demo is meant to expose

Going forward, most demos should use one slide, not separate setup and execution
slides. The demo slide should name the setup/context, what to watch, the key
action, the expected result, and the likely mistake.

Use this student-visible pattern when useful:

```text
Demo: [name]

Watch for:
- setup/context
- key action
- expected result
- likely mistake
```

Week 1 may keep two demo-related slides because first-contact scaffolding
requires extra room for file creation, naming, saving, opening, and refreshing.
After Week 1, use a second demo slide only when the setup itself is a genuine
conceptual step students must understand before the demonstration begins.

Use the demos as instructor demonstration material, not as student starter
code.

The instructor may type key lines live or in the recording to reinforce manual
code fluency. Larger sections may be copy/pasted when timing requires it, but
the deck source should indicate what should still be explained or inspected.

---

# Assignment Success Review Rule

The `Assignments/Success_Solutions/` folder is now a canonical source for
Monday review.

Success solutions should be framed as:

```text
one successful path
```

not:

```text
the only correct answer
```

Use success review to:

- show a completed working result
- connect code to assignment requirements
- support revision and recovery
- identify common gaps
- prepare students for the next layer of work

Do not let the success review consume the new lesson. It should be a concise
bridge from prior work into current work.

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

For PowerPoint notes transfer, format these slide-block labels in bold:

```text
**Instructor notes:**
**Transition cue:**
```

This makes the source easier to copy into the PowerPoint notes section while
preserving a readable distinction between instructor delivery guidance and
student-visible slide content.

---

# Student-Visible Text Guidance

Student-visible text should be concise enough for a slide, but complete enough
to stand as student study material after class or after the recording.

Do not compress most slides into one title plus one or two sentences. That
pattern looked clean in earlier Python deck work but repeatedly produced slides
that were too thin for student review. For Web Development Foundations, follow
the richer 119 Algorithms pattern: a slide should usually contain an anchor idea
plus 2-4 short bullets, cues, or concrete examples.

Use enough visible text for students to understand the slide without needing the
instructor's fresh memory, especially when the slide introduces:

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
- moving the real teaching content into instructor notes only

Slogan-only slides are allowed only when the slide's job is deliberately
emotional framing, transition, or closure. Even then, the next slide should
provide the concrete learning cues.

Preferred pattern:

```text
Anchor idea

- clarifying point
- beginner cue or example
- what to do / what to avoid
```

For demo, lab bridge, evidence, and reading-prep slides, prefer bullets over
paragraphs:

```text
What to watch:
- file name
- saved change
- browser refresh

What not to worry about yet:
- styling
- JavaScript
```

---

# What Counts As Success Today Rule

Preserve a recurring early student-facing slide named:

```text
What Counts As Success Today
```

Place it after the opening/framing slides and before `Today's Toolbox`.

This slide should define the reachable success condition for the current
session. It should be concrete, calming, and smaller than the full assignment
endpoint when the full endpoint depends on later weekly scaffolding.

Use this pattern:

```text
What counts as success today:

- visible result or observable change
- one concept applied correctly
- one thing students can explain
- one check they can use if it breaks
```

For Web Development Foundations, this slide should often prevent the wrong
success target:

- Week 1: existence and structure, not visual polish
- early CSS: one rule visibly applies, not a complete design system
- early JavaScript: one interaction works, not a full app
- async/API weeks: timing or response shape is understood, not production API
  mastery
- capstone weeks: next milestone is clearer, not the whole project finished

Do not use this slide as a full rubric. Use it as a short local target that
students can carry into the demo and lab.

Image generation note:

- Do not generate image prompts for `What Counts As Success Today` slides by
  default.
- Use PowerPoint SmartArt or another simple built-in graphic for this slide,
  consistent with the 117/118/119 course production pattern.
- Only include a generated-image prompt for this slide if the instructor
  explicitly requests one.

---

# What We Will Use Today Rule

Every deck should name the working set for the session.

Prefer a recurring student-facing slide named:

```text
Today's Toolbox
```

This slide works especially well for Web Development Foundations because each
week has many tempting nearby technologies. The slide should show what belongs
in today's hands, not everything students have seen in the reading.

Use this pattern for the active-tool slide:

```text
Today we will use:
- concept / syntax / tool
- concept / syntax / tool
```

This is especially important because the textbooks often include more depth
than a beginner class session should carry.

Visual pattern:

- use a toolbox, workbench, or simple tool tray for today's active concepts
- include 4-8 items, depending on the week
- use familiar labels such as `index.html`, `h1`, `p`, `href`, `save`,
  `refresh`, `querySelector`, or `fetch`
- avoid showing a dense wall of syntax

When deferred topics need to be named, put them on a separate optional slide
named:

```text
Parked For Later
```

Do not combine the active toolbox and parked items in one image. This models
separation of concerns: today's active tools are one concern; scope boundaries
are another concern.

Use the separate "Parked For Later" bookshelf/shelf visual only when the week
has a serious scope-risk boundary, such as CSS/JavaScript in Week 1, full
DOM/API breadth, async complexity, performance techniques, or security concepts.
For ordinary weeks, mention deferred items briefly in instructor notes rather
than creating a recurring parked-items slide.

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

# Assignment Scope Timing Rule

Do not introduce the full weekly assignment endpoint before students have seen
the prerequisite capability needed to understand that endpoint.

This is especially important in Web Development Foundations because weekly work
often unfolds as:

```text
Monday concept / first capability
-> Tuesday first working version
-> Wednesday concept deepening and/or iterative development
-> Thursday refinement toward the full weekly target
```

Monday decks should usually frame only the immediate Tuesday lab entry point.
They may name the formal assignment artifact, but the student-visible slide
should emphasize the first reachable build step.

Use Monday for:

- what students can attempt after today's live lesson
- the first file, first page, first style rule, first event, or first data read
- evidence students should preserve from the initial attempt
- reassurance that the full endpoint is not expected yet

Avoid Monday student-visible slides that prematurely require:

- multi-page integration before one page exists
- styling systems before first CSS rules are introduced
- JavaScript behavior before first DOM interaction is introduced
- async/API work before request/response timing has been introduced
- capstone-level integration before the relevant weekly scaffold exists

Wednesday decks should carry the full weekly assignment target when that target
depends on Monday plus the first lab iteration. Use Wednesday to name:

- how the first working version grows
- what the Thursday refinement should improve
- the full assignment target when students now have the needed mental model
- final evidence and reflection expectations

Week 1 example:

```text
Monday: create index.html and open one page in the browser.
Wednesday: grow one page into a small multi-page site with navigation.
```

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
- omitting the Wednesday next-reading guidance slide
- writing instructor notes that only make sense while the design conversation is
  fresh

---

# Required Pre-Drafting Check

Before drafting any deck source, confirm:

1. Week number and session type: Monday live or Wednesday recorded
2. IIM purpose for that week/session
3. curated reading entries for that week
4. related assignment or lab
5. expected demo folder and file
6. for Monday decks, prior assignment success solution if one exists
7. what students should be able to do after the session
8. what is explicitly not required yet
9. evidence/submission expectation
10. AI-use boundary, if relevant
11. whether PageForge is intentionally used or omitted
12. for Wednesday decks, whether the next-reading slide can be filled or needs a placeholder

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
