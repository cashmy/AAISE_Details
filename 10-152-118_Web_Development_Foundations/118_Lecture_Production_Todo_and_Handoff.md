# 118 Lecture Production Todo and Handoff

**Course:** `10-152-118 HTML, CSS, and JavaScript`  
**Purpose:** ordered restart artifact for finishing/refactoring the lecture and slide-deck production work.

This file is designed so a new Codex session can start from scratch inside this workspace and understand the current objective without relying on prior chat context.

---

## Current Situation

The `117 Python Programming` and `119 Introduction to Algorithms` courses are fully complete. The `118 HTML, CSS, and JavaScript` course has substantial scaffold already present, but the lecture/deck layer needs a focused production pass.

The urgent need is not to redesign the whole course. The urgent need is to refactor and finish `118` lectures using the mature workflow and design insights from `117` and `119`.

Key pressure:

- `118` requires `16` lecture recordings.
- `8` of those require video recordings.
- There is approximately one week available for focused 118 work before Tech Trek/camp pressure disrupts the schedule.
- After camp, there is only one additional week before class starts.
- Minimum viable target: first `4` weeks of lectures finished and recorded before class starts.
- Preferred target: all slide decks finished before camp/travel disruption, leaving only remaining recordings for August.

---

## First Files To Read In A New Session

Read these first, in this order:

1. `10-152-118_HTML_CSS_JS.md/HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
2. `10-152-118_HTML_CSS_JS.md/Lecture_Outlines/Combined_Lectures_Outlines.md`
3. `10-152-118_HTML_CSS_JS.md/Assignments/Combined_Assignments.md`
4. `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDS-AL_Lecture_Deck_Source_Design_Guide.md`
5. `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDST-AL_Lecture_Deck_Source_Template.md`
6. `PowerPoint_Deck_Production_Workflow_v1.md`
7. `D:/@Artifact_Generation/109_RBA_Refaction_Based_Architecture/Case_Studies/RBA_Case_Study_High_Density_HOMSP_Operator_Dependent_Workflow_v1.md`
8. `10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md`
9. `10-152-117_Python_Programming/Assignment_Week_Day_Matrix.md`
10. `10-152-118_HTML_CSS_JS.md/Slide_Decks/STD-01_Slide_Template_Design_System.md`

Why these files matter:

- The `118` high-level plan defines the course arc.
- The `118` combined lectures and assignments define the current raw scaffold.
- The `119` guide/template define the strongest current deck-source production model.
- The PowerPoint workflow preserves the pass-based method for turning deck sources and image prompts into actual decks.
- The RBA/HOMSP case study explains the cognitive-load risk of high-throughput multi-AI slide production.
- The `117` matrices show how lecture content, demos, assignments, and readiness targets were aligned.
- The `118` slide template preserves any existing visual/design intent.

---

## Working Principle

Treat this as a production triage, not a blank-page course design project.

Preserve the existing `118` five-phase structure:

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

Do not expand this into a framework course. Keep it browser-native and beginner-facing.

---

## Required Production Chain

The successful `117` and `119` workflow followed a staged source-to-deck chain.
Use the same procedural order for `118`.

```text
course outline / course plan
-> detailed reading assignments or weekly prep expectations
-> lecture outline
-> lecture deck source with recommended visual notes
-> weekly image-generation prompt artifact
-> generated content images
-> pass-based PowerPoint deck construction
-> sequential validation
-> recording
```

Do not skip directly from the course outline to PowerPoint slides.

The image-generation prompt artifact should be created only after the lecture
deck source has enough visual notes to specify what each image is supposed to
teach. Images should support a slide's instructional job, not merely decorate
the deck.

If a dedicated `118` reading assignment artifact already exists, locate it and
use it before drafting deck sources. If it does not exist, create a minimal
weekly reading/prep artifact before beginning Week 1-4 deck-source production.

Likely places to inspect first:

- `Unit-Week_Descriptions.md`
- `HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
- `IIM_Instructional_Intent_Map.md`
- `Assignments/Combined_Assignments.md`
- `Lecture_Outlines/Combined_Lectures_Outlines.md`
- `Projects/PageForge_Week_by_Week_Roadmap.md`

---

## Ordered Todo List

### 0. Pre-Flyout WIDS And Title Update Tasks

These tasks come before the deeper `118` lecture production work because they
affect official course records and already-complete course materials.

Due before flyout to the Philippines:

- Update `117`, `118`, and `119` with new course titles. - Done
- Submit the updated `117`, `118`, and `119` course title changes on WIDS. - Done
- TODO: Update `117` and `119` PowerPoint slide decks with the new course titles. - Pending
- TODO: Update `117` and `119` PDF handouts with the new course titles. - Pending
- TODO: Re-upload the updated `117` and `119` PowerPoint decks and PDF handouts to WIDS.

Watch point:

- `117` and `119` are otherwise complete, so this should be treated as a
  controlled metadata/title update, not an opportunity to revise completed
  lecture content.

### 1. Confirm The Final Lecture Count And Week Mapping

- Decide whether the course needs `16` or `17` lecture units for production.
- Current scaffold contains `17` lecture outlines, including capstone presentation.
- User stated the production burden as `16` lectures.
- Resolve this before deck production begins.
- Likely interpretation to test:
  - `16` produced lecture decks
  - final presentation week may not need a full recorded lecture deck

Deliverable:

- Add a short `118_Lecture_Production_Map.md` or update this file with the confirmed mapping.

### 2. Build The 118 Lecture Production Tracker

Create a tracker that lists every lecture/week with:

- lecture title
- reading/prep source status
- existing outline path
- assignment supported
- demo/lab needs
- deck-source status
- image-prompt artifact status
- image-generation status
- PowerPoint status
- recording required? yes/no
- video recording required? yes/no
- priority tier
- open risks

Priority tiers:

- `P0`: Weeks 1-4, must be finished and recorded first.
- `P1`: Weeks 5-8, should be deck-complete before camp if possible.
- `P2`: Weeks 9-16, should be source/deck-complete before August recordings if possible.
- `P3`: final presentation/capstone support materials.

### 3. Create A 118 Lecture/Demo/Assignment Alignment Matrix

Use `117` as the model.

For each 118 lecture, map:

- reading/prep assignment or source material
- core lecture content
- recommended demo(s)
- assignment(s) supported
- readiness target
- assumptions/watch points

Special emphasis:

- Week 1 must produce a fast visible win.
- Week 4 JavaScript should be logic-first before DOM.
- Week 5 DOM should connect JavaScript to visible browser behavior.
- Week 6 debugging must teach process, not panic.
- AI use should remain delayed until students have enough judgment.

Deliverable:

- `Lecture_Content_and_Demo_Alignment_Matrix.md` inside the `118` folder.

### 4. Locate Or Create The 118 Reading Assignment Layer

Before deck-source drafting, confirm the reading/prep material for each week.

The goal is not to overbuild a textbook apparatus. The goal is to know what
students are expected to encounter before or around each lecture so the deck can
include an appropriate reading/prior-work review section.

If a dedicated reading assignment artifact exists:

- cite it in the production tracker
- map each reading/prep item to the relevant lecture

If no dedicated artifact exists:

- create a lean `Weekly_Reading_and_Preparation_Guide.md`
- base it on the high-level course plan, unit-week descriptions, assignments,
  and lecture outlines
- keep each week short and usable

Minimum weekly fields:

- week/lecture title
- prep focus
- assigned reading or prep material
- key terms to notice
- what students should bring into lecture
- connection to lab/assignment

### 5. Normalize The 118 Lecture Outline Titles And Typos

Current outline filenames include typos:

- `1_HTML-Somethine_Exists.md`
- `2_CSS-I_Can_Control_Apperance.md`

Before bulk production, decide whether to rename files or leave filenames alone and normalize only display titles.

Recommendation:

- If no external links depend on these filenames, rename them cleanly.
- If links may exist, leave filenames alone and correct titles inside generated deck sources.

Do not let filename cleanup consume the production week.

### 6. Create A 118 Deck-Source Template

Adapt the `119` deck-source template to 118.

The template should include:

- slide title
- student-facing slide body
- instructor notes
- visual notes
- demo cue
- lab bridge cue
- misconception warning
- timing/pacing guidance
- core/optional/reserve section labels

118-specific section flow:

1. Opening bridge
2. Reading or prior-work review
3. Lesson outcomes
4. Concept block
5. Visible example
6. Browser/dev-tool/demo cue
7. Check for understanding
8. Lab bridge
9. Wrap-up and next-step cue

Deliverable:

- `Lecture_Outlines/LDS-118_Lecture_Deck_Source_Design_Guide.md`
- `Lecture_Outlines/LDST-118_Lecture_Deck_Source_Template.md`

### 7. Produce Week 1-4 Deck Sources First

Create deck-source artifacts before PowerPoint production.

P0 deck sources:

1. Week 1 - HTML: Something Exists
2. Week 2 - CSS: I Can Control Appearance
3. Week 3 - Layout: Control Space
4. Week 4 - JavaScript: This Is Programming

Each deck source must include:

- the core concept sequence
- instructor notes that are clear after time has passed
- demo/lab bridge
- likely student misconceptions
- visual notes if useful
- recording notes

### 8. Create Week 1-4 Image Prompt Artifacts

After each Week 1-4 deck source is complete, create an image prompt artifact
for that week.

Each image prompt artifact should include:

- image title
- slide or section supported
- instructional purpose
- constrained image prompt
- style consistency notes
- negative constraints if needed
- save filename recommendation
- alt-text draft or alt-text intent

Do not generate images until the prompt artifact is aligned with the deck
source.

Deliverable pattern:

- `Lecture_Deck_Sources/Week_01_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_02_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_03_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_04_Image_Prompts.md`

If a `Lecture_Deck_Sources` folder does not exist for `118`, create it before
beginning this stage.

### 9. Generate Week 1-4 Content Images

Generate images from the prompt artifacts one at a time.

For each image:

- compare the result to the instructional purpose
- reject visually attractive but conceptually misleading images
- save accepted images in a week-specific folder
- record filename and placement in the prompt artifact or deck source

Recommended folder pattern:

- `Lecture_Deck_Sources/Images/Week_01/`
- `Lecture_Deck_Sources/Images/Week_02/`
- `Lecture_Deck_Sources/Images/Week_03/`
- `Lecture_Deck_Sources/Images/Week_04/`

### 10. Produce Week 1-4 PowerPoint Decks

Use the existing `118` slide design system unless there is a strong reason to revise.

Existing assets to inspect:

- `Slide_Decks/STD-01_Slide_Template_Design_System.md`
- `Slide_Decks/Week1_Lecture_Slides.pptx`
- `Slide_Decks/Week1_Lecture_Slides_Enhanced.pptx`
- `Slide_Decks/Week1_Lecture_Slides_Mon.pptx`
- `Slide_Decks/Images/`

Do not over-polish. These need to be teachable and recordable.

Use the pass-based workflow from `PowerPoint_Deck_Production_Workflow_v1.md`.

Recommended deck-production passes:

1. Copy or create the 118 template deck.
2. Create the day-level lecture deck from the template.
3. Generate or collect any needed visuals from constrained prompt artifacts.
4. Stage image slides at the end of the deck.
5. Add image titles and alt text.
6. Copy template slides to match the deck-source sequence.
7. Add slide titles.
8. Add student-facing text and instructor notes.
9. Move staged image slides into the instructional sequence.
10. Perform a full sequential validation pass.

Sequential validation must check:

- slide order
- title accuracy
- text fit and readability
- instructor notes
- demo/lab bridge accuracy
- image placement and conceptual accuracy
- alt text
- evidence expectations
- AI-use guidance
- success check
- visual consistency

The key production principle is controlled passes, not slide-by-slide improvisation.

### 11. Record Week 1-4 Lectures

Recording priority:

1. Week 1
2. Week 2
3. Week 3
4. Week 4

Recording rule:

- Record once the deck is coherent enough to teach.
- Do not wait for perfect slide aesthetics if the content is stable.

### 12. Batch Produce Week 5-8 Deck Sources

P1 deck sources:

5. DOM: Now It Connects
6. Debugging: Things Break, and I Can Fix Them
7. Structured Behavior
8. Async: Time Matters

These weeks are especially important because they move students from static web pages into behavior, debugging, and browser application thinking.

### 13. Batch Produce Week 5-16 Image Prompt Artifacts And Images

After each later deck source is complete, repeat the same image prompt artifact
workflow used for Weeks 1-4.

Do not generate image prompts before visual notes exist in the deck source.

### 14. Batch Produce Week 9-16 Deck Sources

P2 deck sources:

9. Modular Thinking
10. Data: Beyond the Page
11. State: Things Persist
12. Performance
13. Security Awareness
14. UX and Styling Refinement
15. Pre-Capstone Integration
16. Capstone Build

Keep these pragmatic. They should prepare students for capstone ownership, not simulate a professional specialization course.

### 15. Decide Whether Week 17 Needs A Full Deck

Current scaffold has:

- `17_Capstone_Presentations.md`

If the course production target is `16` lectures, Week 17 may need:

- presentation checklist
- grading/explanation rubric
- student-facing final demo guide
- no full recorded lecture

Make this decision explicitly.

### 16. Create Or Refactor Demos Only Where Needed

Do not build an enormous demo library unless required.

For each P0/P1 lecture, identify whether there is:

- an existing demo
- a small code example needed
- a broken example needed for debugging
- a starter/success pair needed for student transfer

Likely minimal demo needs:

- Week 1: simple multi-page HTML site
- Week 2: same site styled with CSS
- Week 3: layout/responsive revision
- Week 4: JavaScript console logic examples
- Week 5: DOM button/input interaction
- Week 6: intentionally broken HTML/CSS/JS examples

### 17. Preserve The AI-Use Progression

The 118 course should not start with AI as the main builder.

Preserve this progression:

```text
manual native work -> assisted explanation/debugging -> strategic capstone use
```

AI use should support:

- explanation
- debugging
- comparison
- refinement
- capstone acceleration

AI use should not replace:

- student design judgment
- basic HTML/CSS/JS authorship
- debugging evidence
- final explanation of how the system works

### 18. Use 119's Deck-Source Discipline

For each deck source, avoid generic slide text.

Include:

- what the instructor should say
- why the teaching move matters
- what student misconception it addresses
- what demo/example is being used
- how the lab depends on the lecture
- what can be skipped if time is tight

This is the main insight to carry from `119`.

### 19. Use The PowerPoint Workflow's Pass-Based Discipline

Do not attempt to create polished PowerPoint decks in one linear pass.

Separate the work into:

- template structure
- visual generation or collection
- image staging
- alt text
- slide skeleton
- student-facing content
- instructor notes
- image placement
- final sequential validation

This lowers cognitive load and reduces hidden errors such as duplicated slides, missing notes, mismatched images, and topic bleed from another lecture.

### 20. Use The RBA/HOMSP Case Study As A Risk Warning

The prior high-throughput 117 slide production process was powerful but operator-dependent.

It relied on a human coordinator actively managing:

- browser-based image generation
- PowerPoint design/alt-text support
- Codex semantic checking and artifact governance
- final human sequencing, judgment, and arbitration

This workflow can create major throughput, but it also creates risks:

- cognitive fatigue
- day-to-day topic conflation
- recency bias
- image-prompt drift
- slide-sequence mismatch
- AI compression of important scaffolding
- visually pleasing but conceptually weak images

For 118, use high-throughput HOMSP mode only when the current production lane is explicit.

Before starting a work block, name:

- the current lecture/deck
- the current artifact lane
- the AI/tool role being used
- the next human arbitration point
- the validation pass that will catch drift

If that cannot be named clearly, slow down and work on one artifact at a time.

### 21. Use 117's Alignment Discipline

For each lecture, confirm:

1. What must students be able to do after this lecture?
2. Which assignment depends on that ability?
3. Which demo supports that ability?
4. What hidden assumption could break student success?

This is the main insight to carry from `117`.

---

## Suggested Production Order For Tomorrow Morning

1. Read the first-context files listed above.
2. Confirm whether the final production target is `16` or `17` lectures.
3. Create the lecture production tracker.
4. Create the 118 lecture/demo/assignment alignment matrix skeleton.
5. Locate or create the weekly reading/prep layer.
6. Fill Weeks 1-4 in the matrix.
7. Draft the 118 deck-source guide/template.
8. Start Week 1 deck source.

If energy is limited, do only steps 1-5. That still gives the rest of the week a clean runway.

Do not start by building PowerPoint slides directly unless the deck source already exists and has been checked against the alignment matrix.

---

## Known Existing 118 Assets

Course-level:

- `HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
- `WIDS_Course_Competency_Framework_v2.md`
- `WIDS_COS_Course_Outcome_Summary_118_v3.pdf`
- `CAM_Course_Architecture.md`
- `IIM_Instructional_Intent_Map.md`
- `APL_Assignment_Progression_Ladder.md`

Assignments:

- `Assignments/Combined_Assignments.md`
- individual assignment files `1` through `17`

Lecture outlines:

- `Lecture_Outlines/Combined_Lectures_Outlines.md`
- individual lecture files `1` through `17`
- `Lecture_Outlines/LOT-01_Lecture_Outline_Template.md`

Projects/PageForge:

- `Projects/PageForge_Week_by_Week_Roadmap.md`
- `Projects/PageForge_Instructor_Companion.md`
- `Projects/PageForge_Design_Contract.md`
- `Projects/PageForge_Generation_Workflow.md`

Slide work:

- `Slide_Decks/STD-01_Slide_Template_Design_System.md`
- existing Week 1 PowerPoint experiments
- `Slide_Decks/Images/`

---

## Decisions To Avoid Re-Litigating

- Keep `118` browser-native: HTML, CSS, JavaScript, DOM, debugging, data/state, UX, capstone.
- Do not turn `118` into React, Node, or full-stack.
- Do not pull AI use too early.
- Do not redesign assignments unless lecture alignment exposes a concrete blocker.
- Prioritize Weeks 1-4 recordings over perfecting later-course polish.
- Prefer complete deck sources for all weeks before deep visual polish.

---

## Definition Of Done

Minimum done before class pressure:

- Weeks 1-4 deck sources complete.
- Weeks 1-4 PowerPoint decks complete enough to teach.
- Weeks 1-4 recordings complete.
- 118 production tracker exists and shows remaining work.

Preferred done before August recording push:

- All 16 lecture deck sources complete.
- All 16 PowerPoint decks complete enough to record.
- Week 17 capstone/presentation support decision made.
- Remaining recordings can be completed during August without major content design work.
