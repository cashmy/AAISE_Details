# 118 Lecture Production Todo and Handoff

**Course:** `10-152-118 Web Development Foundations`  
**Alternate Title:** `HTML, CSS, and JavaScript`  
**Purpose:** restart artifact for the next production phase: refactoring and creating the lecture deck source artifacts for the full course.

This file is designed so a new Codex session can restart the `118` lecture/deck work without relying on prior chat context.

---

## Current Situation

The reading/preparation layer is now complete.

The course has a much more complex reading and prep structure than `117` or `119` because it integrates:

- two Duckett textbooks:
  - `HTML & CSS: Design and Build Websites`
  - `JavaScript & jQuery: Interactive Front-End Web Development`
- course-authored supplemental materials where the textbooks are thin, dated, implicit, or too broad
- a 17-week course span
- iterative web-development scaffolding across weeks
- a capstone structure that grows from HTML/CSS/JS foundations into data, state, security, UX, performance, forms, proposal, build, and presentation
- a delayed and accountable AI-use progression

The next major phase is lecture deck source production.

Correct production count:

- `34` total slide deck source artifacts
- `2` decks per week
- Monday deck = live classroom presentation
- Wednesday deck = asynchronous recorded presentation for students to view independently
- `16` Wednesday decks are expected to be recorded as video
- Week 17 is capstone presentation/wrap-up support and is not expected to need a normal recorded Wednesday lecture

The older assumption that this was only `16` slide decks, or that only `8` needed video recording, has been superseded.

---

## First Files To Read In A New Session

Read these first, in this order:

1. `10-152-118_Web_Development_Foundations/Weekly_Reading_and_Preparation_Guide.md`
2. `10-152-118_Web_Development_Foundations/Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`
3. `10-152-118_Web_Development_Foundations/IIM_Instructional_Intent_Map.md`
4. `10-152-118_Web_Development_Foundations/HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
5. `10-152-118_Web_Development_Foundations/Lecture_Outlines/Combined_Lectures_Outlines.md`
6. `10-152-118_Web_Development_Foundations/Assignments/Combined_Assignments.md`
7. `10-152-118_Web_Development_Foundations/Projects/Project_Track_Guide.md`
8. `10-152-118_Web_Development_Foundations/Projects/PageForge_Week_by_Week_Roadmap.md`
9. `10-152-118_Web_Development_Foundations/Projects/PageForge_Instructor_Companion.md`
10. `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDS-AL_Lecture_Deck_Source_Design_Guide.md`
11. `10-152-119_Intro_To_Algorithms/Lecture_Outlines/LDST-AL_Lecture_Deck_Source_Template.md`
12. `10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md`
13. `10-152-117_Python_Programming/Assignment_Week_Day_Matrix.md`
14. `PowerPoint_Deck_Production_Workflow_v1.md`
15. `D:/@Artifact_Generation/109_RBA_Refaction_Based_Architecture/Case_Studies/RBA_Case_Study_High_Density_HOMSP_Operator_Dependent_Workflow_v1.md`

Why these files matter:

- The completed reading guide is now the pacing anchor.
- The continuity brief captures the 34-deck rhythm and recurring deck-source expectations.
- The instructional intent map keeps the decks aligned to course purpose.
- The lecture outlines and assignments provide the existing raw weekly scaffold.
- The project and PageForge files preserve the capstone/project model.
- The `117` and `119` artifacts preserve the mature production workflow.
- The PowerPoint and RBA/HOMSP workflow documents preserve the pass-based production discipline and fatigue-risk warnings.

---

## Completed Reading/Prep Layer

The following course-authored materials now exist in `Course_Materials/` and are reflected in the reading guide:

- `Week_08_Async_Time_Matters_Handout.md`
- `Week_08_How_To_Read_JSON_Student_Guide.md`
- `Week_09_Modular_Thinking_Multi_File_Organization_Handout.md`
- `Week_10_API_Guidance_For_Web_Projects.md`
- `Week_10_JSON_Reading_Quiz_Setup.md`
- `Week_10_JSON_Reading_Quiz_Key_Instructor.md`
- `Week_11_State_LocalStorage_Example.md`
- `Week_12_Performance_Avoiding_Unnecessary_Work.md`
- `Week_13_Browser_Security_Awareness_For_Web_Projects.md`
- `Week_14_UX_Responsive_Refinement_Checklist.md`
- `Week_15_Basic_Simulated_Login_Form_Handout.md`
- `Week_15_Capstone_Proposal_and_Scope_Guide.md`
- `Week_17_AI_Use_Explanation_Guide.md`
- `Week_17_Capstone_Presentation_and_Readiness_Checklist.md`

Shared/root support material:

- `Approved_API_List.md`
- `Standard_Student_AI_Use_Policy.md`

---

## Working Principle

Treat this as production sequencing, not blank-page course design.

Preserve the existing five-phase course structure:

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

Do not expand this into a framework, React, Node, full-stack, or deployment course.

Keep it browser-native and beginner-facing.

---

## Completed Production Activity Log

This section preserves work completed after the earlier handoff notes were
written. Some of these steps were not originally listed as explicit TODO items,
but they are now part of the course production record.

### Completed: Demo Spine For Weeks 1-15

Status:

- DONE.

Output:

- `Demos/README.md`
- `Demos/Week_01_HTML_Multi_Page_Site/`
- `Demos/Week_02_CSS_Appearance/`
- `Demos/Week_03_Layout_Responsive/`
- `Demos/Week_04_JavaScript_Logic/`
- `Demos/Week_05_DOM_Interaction/`
- `Demos/Week_06_Debugging_Process/`
- `Demos/Week_07_Structured_JavaScript/`
- `Demos/Week_08_Async_Time/`
- `Demos/Week_09_Modular_Thinking/`
- `Demos/Week_10_Data_APIs/`
- `Demos/Week_11_State_LocalStorage/`
- `Demos/Week_12_Performance/`
- `Demos/Week_13_Security_Reliability/`
- `Demos/Week_14_UX_Refinement/`
- `Demos/Week_15_Forms_Input/`

Each week now has a Monday starter demo and Wednesday iterative/deepening demo.
The demo notes now assume the instructor may manually type important lines live
or in recordings, while copy/pasting larger sections only for time compression.

Verification:

- JavaScript demo files were syntax-checked during production.
- JSON demo data was parsed where applicable.

### Completed: Assignment Success Solutions For Weeks 1-15

Status:

- DONE.

Output:

- `Assignments/Success_Solutions/README.md`
- `Assignments/Success_Solutions/Week_01_HTML_Multi_Page_Site/`
- `Assignments/Success_Solutions/Week_02_Styling_Visual_Design/`
- `Assignments/Success_Solutions/Week_03_Layout_Responsive_Design/`
- `Assignments/Success_Solutions/Week_04_Introduction_to_JavaScript/`
- `Assignments/Success_Solutions/Week_05_DOM_Interaction_Events/`
- `Assignments/Success_Solutions/Week_06_Debugging_Problem_Solving/`
- `Assignments/Success_Solutions/Week_07_Structured_JavaScript/`
- `Assignments/Success_Solutions/Week_08_Asynchronous_Behavior/`
- `Assignments/Success_Solutions/Week_09_Modular_Thinking/`
- `Assignments/Success_Solutions/Week_10_Data_APIs/`
- `Assignments/Success_Solutions/Week_11_State_Management/`
- `Assignments/Success_Solutions/Week_12_Performance_Efficiency/`
- `Assignments/Success_Solutions/Week_13_Security_Reliability/`
- `Assignments/Success_Solutions/Week_14_UX_Refinement/`
- `Assignments/Success_Solutions/Week_15_Forms_Input_Systems/`

Design decision:

- Success solutions use a continuous `Study Sprint` sample concept.
- They are intentionally separate from the lecture demos and PageForge.
- They show one successful path for revision/recovery support, not the only
  acceptable solution.

Verification:

- JavaScript files were syntax-checked during production.
- JSON data was parsed where applicable.

### Completed: PageForge Weekly Milestone Scaffold And Bridge

Status:

- DONE for Weeks 2-15 weekly milestone code.
- DONE for Week 15-to-final bridge documentation.
- Week 16-17 PageForge milestones remain optional if later recordings require
  frozen readiness states.

Separate workspace:

```text
D:\@Coding_Projects\HTML-CSS-JS\PageForge
```

Docs created or updated:

- `docs/PageForge_Weekly_Progression_Scaffold_v2.md`
- `docs/PageForge_Milestone_Index.md`
- `docs/PageForge_Milestone_Notes_Template.md`
- `docs/PageForge_Week15_to_Final_Bridge.md`

Milestones created:

- `milestones/week02-css-foundation/`
- `milestones/week03-responsive-builder-layout/`
- `milestones/week04-javascript-block-logic/`
- `milestones/week05-dom-block-builder/`
- `milestones/week06-debugged-interaction/`
- `milestones/week07-structured-javascript/`
- `milestones/week08-async-preview-timing/`
- `milestones/week09-modular-organization/`
- `milestones/week10-json-template-loading/`
- `milestones/week11-state-driven-builder/`
- `milestones/week12-performance-refinement/`
- `milestones/week13-safer-reliable-handling/`
- `milestones/week14-ux-refined-builder/`
- `milestones/week15-forms-and-simulated-login/`

Design decision:

- PageForge now uses one demonstrable end-of-week milestone per week.
- PageForge is optional instructor enrichment, not a required deck-source
  element.
- PageForge should not delay core deck-source production.

Verification:

- Milestone JavaScript files were syntax-checked.
- JSON template files were parsed.
- Week 10 onward should be reviewed through a local server because local JSON
  is loaded with `fetch()`.

### Completed: Deck Source Continuity Brief Update

Status:

- DONE.

Updated artifact:

- `Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`

Important updates:

- `Demos/` promoted to canonical deck-production input.
- `Assignments/Success_Solutions/` promoted to canonical Monday review input.
- Historical aggregate artifacts downgraded to informative references when
  they conflict with newer production artifacts.
- PageForge clarified as optional enrichment.
- Monday deck pattern added, including `Previous Lab Review / Success Path`.
- Wednesday deck pattern added for concept deepening and iterative development.
- Demo integration rules added.
- Assignment success review rules added.
- Deck naming convention added.
- Pre-drafting checklist updated.

### Completed: Assignment Alignment Corrections

Status:

- DONE for current known issues.

Notes:

- Week 12 performance assignment was aligned to repeated work, file/image size,
  conceptual pagination/chunking, and debounce/throttle recognition.
- Week 13 security assignment was aligned to browser security awareness, safe
  input/output, trust boundaries, XSS/CSRF/CORS recognition, and simulated-login
  limits.
- Week 15 forms/input work was separated from capstone proposal work.
- `Assignments/15C_Capstone_Submission_Form.md` exists and works with
  `Course_Materials/Week_15_Capstone_Proposal_and_Scope_Guide.md`.

Remaining:

- `Assignments/Combined_Assignments.md` may be stale. Regenerate only if it
  will be used as a current combined artifact.

---

## Required Production Chain

Use the staged source-to-deck chain from `117` and `119`.

```text
course outline / course plan
-> weekly reading and preparation guide
-> lecture outline
-> lecture/demo/assignment alignment matrix
-> lecture deck source with recommended visual notes
-> weekly image-generation prompt artifact
-> generated content images
-> pass-based PowerPoint deck construction
-> sequential validation
-> recording
```

Do not skip directly from outline to PowerPoint slides.

The image-generation prompt artifact should be created only after the deck source has enough visual notes to specify what each image is supposed to teach. Images should support a slide's instructional job, not merely decorate the deck.

---

## Ordered Todo List

### 0. Remaining Cross-Course Title/Metadata Cleanup

Status:

- New course titles have been identified and applied to course-title artifacts.
- `118` is now `Web Development Foundations`.
- The older title is preserved as an alternate title where useful.

Remaining:

- TODO: Update `117` and `119` PowerPoint slide decks with the new course titles.
- TODO: Update `117` and `119` PDF handouts with the new course titles.
- TODO: Re-upload updated `117` and `119` decks/handouts to Schoology if required.

Watch point:

- `117` and `119` are otherwise complete. Treat this as a controlled metadata/title update, not a content revision pass.

### 1. Create The 118 Lecture Production Map

Status:

- SUSPENDED / OPTIONAL.

Current decision:

- Not required for the immediate Week 1-4 slide-production push.
- The current RBA process, completed continuity brief, reading guide, demos,
  assignments, and success solutions provide enough local alignment to draft
  deck sources directly.
- This artifact may still be useful later as a governance/dashboard artifact if
  the process changes, multiple collaborators join, or all 34 decks need
  status tracking in one place.

Create a map for all 34 deck sources.

The map should show:

- week number
- Monday/live deck title
- Wednesday/recorded deck title
- unit/phase
- reading/prep anchor
- assignment/lab connection
- recording required? yes/no
- priority tier
- deck-source status
- PowerPoint status
- open risks

Production rule:

- Week 1-16 Wednesday decks are the expected recorded video decks.
- Week 17 should be treated as presentation/readiness support unless a later decision requires an additional recording.

Deliverable:

- `10-152-118_Web_Development_Foundations/118_Lecture_Production_Map.md`

### 2. Build The 118 Lecture/Demo/Assignment Alignment Matrix

Status:

- SUSPENDED / OPTIONAL.

Current decision:

- Not required for the immediate Week 1-4 slide-production push.
- The deck sources themselves should carry the needed alignment sections:
  reading alignment, demo integration, assignment/lab bridge, evidence
  expectation, and misconception/watch point.
- This matrix may still be useful for future course work if a different process
  requires a single cross-week alignment artifact.

Use `117` as the model.

For each week and deck/day, map:

- reading/prep assignment or source material
- core lecture content
- recommended demo
- assignment supported
- readiness target
- assumptions/watch points

Special emphasis:

- Week 1 must produce a fast visible win.
- Week 4 JavaScript should be logic-first before DOM.
- Week 5 DOM should connect JavaScript to visible browser behavior.
- Week 6 debugging must teach process, not panic.
- AI use should remain delayed until students have enough judgment.
- Week 8 async should bridge to Python async without making JavaScript async look magical.
- Week 13 security should stay browser/user-login aware, not become the concurrent security course.
- Weeks 16-17 should emphasize capstone ownership, explanation, and accountability.

Assignment sanity-check note:

- Week 12 performance assignment has been aligned to the new performance handout with beginner-safe anchors: repeated work, file/image size, pagination/chunking as a concept, and debounce/throttle as optional pattern recognition.
- Week 13 security assignment has been aligned to browser-security awareness: safe input/output, trust boundaries, XSS/CSRF/CORS recognition, simulated login limits, and no claim of real authentication.
- Week 15 forms assignment has been separated from capstone proposal work. The technical lab now centers forms/input systems and simulated-login caution; the existing capstone proposal workflow uses `Course_Materials/Week_15_Capstone_Proposal_and_Scope_Guide.md` plus `Assignments/15C_Capstone_Submission_Form.md`.
- Treat individual assignment files as the current assignment source. Regenerate or clean up `Assignments/Combined_Assignments.md` later if it will be used as a student-facing or instructor-facing combined artifact.
- A new success-solution lane has been started in `Assignments/Success_Solutions/`. Weeks 1-15 use a continuous `Study Sprint` sample site/concept to show one acceptable final result after the submission cycle, supporting revision recovery without reusing the lecture demo code. Week 15's success code supports the technical forms/input assignment only; the capstone proposal remains governed by its separate guide and submission form.

Deliverable:

- `10-152-118_Web_Development_Foundations/Lecture_Content_and_Demo_Alignment_Matrix.md`

### 3. Preserve The Completed Reading Guide

The reading layer is finished and should now be treated as the pacing anchor for deck production.

Do not reopen the full reading assignment curation unless a concrete inconsistency is found.

### 4. Normalize Lecture Outline Titles And Legacy Sources

Current lecture outline filenames include typos:

- `1_HTML-Somethine_Exists.md`
- `2_CSS-I_Can_Control_Apperance.md`

Current user intention:

- create `*_v2.md` deck/source artifacts with corrected titles
- preserve originals in a `Legacy` subfolder rather than overwriting them

Recommended:

- Do not spend production energy renaming every historical source file unless needed.
- Correct display titles in all new deck sources.
- Move true legacy originals only when the new source artifacts are created and validated.

### 5. Create Or Finalize The 118 Deck-Source Guide And Template

Status:

- GUIDE: COMPLETE ENOUGH via `Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`.
- TEMPLATE: OPTIONAL.

Current decision:

- Do not create a separate deck-source design guide during the immediate Week
  1-4 production push.
- The updated continuity brief is sufficient for current RBA deck-source work.
- A compact template may be created only if it speeds production; it is not a
  blocker.

Before creating new deck sources, review the existing continuity artifact:

- `Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`

Completed:

- DONE: Confirmed that it reflects the completed reading/prep guide.
- DONE: Confirmed that it reflects the corrected `34` deck / `16` recording model.
- DONE: Added stronger guidance for Monday/live versus Wednesday/recorded decks.
- DONE: Preserved the key rhythm that Wednesday decks should be an iterative progression from Monday's lecture and the related lab assignment, not a disconnected second topic.
- DONE: Tuned the recurring "how to read next week's material" slide guidance for this course.
- DONE: Tuned PageForge references so PageForge is optional instructor enrichment and not a required deck-source element.
- DONE: Added demos as canonical deck-production inputs.
- DONE: Added assignment success solutions as canonical Monday review inputs.

Remaining / optional:

Adapt the `119` deck-source guide/template to `118`.

Current pressure note:

- Under current time pressure, skip this unless the lack of a copy/paste
  template slows deck-source drafting.

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

Deliverables:

- `Lecture_Deck_Sources/LDS-118_Lecture_Deck_Source_Design_Guide.md`
- `Lecture_Deck_Sources/LDST-118_Lecture_Deck_Source_Template.md`

### 6. Produce Week 1-4 Deck Sources First

Priority:

- `P0`

Weeks:

1. HTML: Something Exists
2. CSS: I Can Control Appearance
3. Layout: Control Space
4. JavaScript: This Is Programming

Each week should produce two deck sources:

- Monday/live
- Wednesday/recorded

Each deck source must include:

- core concept sequence
- instructor notes that remain useful after time passes
- demo/lab bridge
- likely student misconceptions
- visual notes if useful
- recording notes for Wednesday decks

### 7. Create Week 1-4 Image Prompt Artifacts

After each Week 1-4 deck source is complete, create an image prompt artifact for that week.

Each image prompt artifact should include:

- image title
- slide or section supported
- instructional purpose
- constrained image prompt
- style consistency notes
- negative constraints if needed
- save filename recommendation
- alt-text draft or alt-text intent

Deliverable pattern:

- `Lecture_Deck_Sources/Week_01_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_02_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_03_Image_Prompts.md`
- `Lecture_Deck_Sources/Week_04_Image_Prompts.md`

### 8. Generate Week 1-4 Content Images

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

### 9. Produce Week 1-4 PowerPoint Decks

Use the existing `118` slide design system unless there is a strong reason to revise.

Existing assets to inspect:

- `Slide_Decks/STD-01_Slide_Template_Design_System.md`
- existing Week 1 PowerPoint experiments
- `Slide_Decks/Images/`

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

### 10. Record Week 1-4 Wednesday Decks

Recording priority:

1. Week 1 Wednesday
2. Week 2 Wednesday
3. Week 3 Wednesday
4. Week 4 Wednesday

Recording rule:

- Record once the deck is coherent enough to teach.
- Do not wait for perfect slide aesthetics if the content is stable.

### 11. Batch Produce Week 5-8 Deck Sources

Priority:

- `P1`

Weeks:

5. DOM: Now It Connects
6. Debugging: Things Break, and I Can Fix Them
7. Structured Behavior
8. Async: Time Matters

These weeks move students from static pages into behavior, debugging, and browser application thinking.

### 12. Batch Produce Week 9-15 Deck Sources

Priority:

- `P2`

Weeks:

9. Modular Thinking
10. Data: Beyond the Page
11. State: Things Persist
12. Performance
13. Security Awareness
14. UX and Styling Refinement
15. Forms and Capstone Proposal

Keep these pragmatic. They should prepare students for capstone ownership, not simulate a professional specialization course.

### 13. Produce Week 16-17 Capstone Support Deck Sources

Priority:

- `P3`

Weeks:

16. Capstone Build
17. Capstone Wrap-Up and Presentations

Week 16:

- build coaching
- integration checks
- scope repair
- debugging and explanation support
- Wednesday recorded support deck if needed

Week 17:

- presentation readiness
- final explanation
- AI-use accountability
- no normal recorded lecture expected unless the instructor later chooses otherwise

### 14. Add PageForge Week-By-Week Iterative Instructor Model Work

This is lower priority than the immediate deck-source pass, but it must remain
visible as optional instructor enrichment.

Context:

- PageForge is an instructor-only project model.
- The finished/current workspace exists separately at `D:\@Coding_Projects\HTML-CSS-JS\PageForge`.
- The instructor will iteratively add course concepts into PageForge week by week, similar to a capstone model.
- This project should not be published for students to copy.

Completed:

- DONE: Inspected the separate PageForge workspace at `D:\@Coding_Projects\HTML-CSS-JS\PageForge`.
- DONE: Created a refreshed one-milestone-per-week PageForge scaffold.
- DONE: Created or updated PageForge docs:
  - `docs/PageForge_Weekly_Progression_Scaffold_v2.md`
  - `docs/PageForge_Milestone_Index.md`
  - `docs/PageForge_Milestone_Notes_Template.md`
  - `docs/PageForge_Week15_to_Final_Bridge.md`
- DONE: Created PageForge milestone code for Weeks 2-15.
- DONE: Verified PageForge milestone JavaScript and JSON mechanically.
- DONE: Preserved PageForge as instructor-only and optional.

Remaining:

- OPTIONAL: Create `milestones/week16-capstone-build-readiness/` only if a frozen Week 16 PageForge recording state is useful.
- OPTIONAL: Create `milestones/week17-capstone-presentation-readiness/` only if a frozen Week 17 PageForge presentation state is useful.
- OPTIONAL: Add PageForge recordings as time permits or necessity emerges.

Possible deliverables:

- `Projects/PageForge_Week_by_Week_Roadmap_v2.md` if a course-folder mirror is still desired
- `Projects/PageForge_Instructor_Companion_v2.md` if a course-folder instructor companion is still desired
- `Projects/PageForge_Milestone_Map.md` if the separate PageForge docs need to be mirrored into the course folder
- optional Week 16-17 milestone snapshot folders or notes in the separate PageForge workspace

Watch point:

- PageForge should model iterative development and project ownership. It should not become a complete solution students can imitate directly for their own capstone.
- PageForge is not required in the core slide deck sources.

### 15. Create Or Refactor Demos Only Where Needed

Status:

- DONE for Weeks 1-15.
- Weeks 16-17 are capstone support weeks and do not require normal concept-demo folders unless later deck production exposes a specific need.

Do not expand the demo library further unless required.

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
- Week 8: `setTimeout`, `fetch`, and Promise timing examples
- Week 11: state/localStorage example
- Week 15: simulated login/form example

Initial demo spine created:

- `Demos/README.md`
- `Demos/Week_01_HTML_Multi_Page_Site/01_monday_hello_world/`
- `Demos/Week_01_HTML_Multi_Page_Site/02_wednesday_multi_page_structure/`
- `Demos/Week_02_CSS_Appearance/01_monday_first_styles/`
- `Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/`
- `Demos/Week_03_Layout_Responsive/01_monday_simple_layout/`
- `Demos/Week_03_Layout_Responsive/02_wednesday_responsive_cards/`
- `Demos/Week_04_JavaScript_Logic/01_monday_values_conditions/`
- `Demos/Week_04_JavaScript_Logic/02_wednesday_function_decision/`
- `Demos/Week_05_DOM_Interaction/01_monday_button_text_change/`
- `Demos/Week_05_DOM_Interaction/02_wednesday_input_feedback/`
- `Demos/Week_06_Debugging_Process/01_monday_broken_selector/`
- `Demos/Week_06_Debugging_Process/02_wednesday_multi_issue_debugging/`
- `Demos/Week_07_Structured_JavaScript/01_monday_messy_working_code/`
- `Demos/Week_07_Structured_JavaScript/02_wednesday_refactored_code/`
- `Demos/Week_08_Async_Time/01_monday_delayed_message/`
- `Demos/Week_08_Async_Time/02_wednesday_fetch_timing_shape/`
- `Demos/Week_09_Modular_Thinking/01_monday_one_file_responsibilities/`
- `Demos/Week_09_Modular_Thinking/02_wednesday_multi_file_organization/`
- `Demos/Week_10_Data_APIs/01_monday_json_shape/`
- `Demos/Week_10_Data_APIs/02_wednesday_json_to_page/`
- `Demos/Week_11_State_LocalStorage/01_monday_counter_state/`
- `Demos/Week_11_State_LocalStorage/02_wednesday_persistent_preference/`
- `Demos/Week_12_Performance/01_monday_repeated_work/`
- `Demos/Week_12_Performance/02_wednesday_debounced_filter/`
- `Demos/Week_13_Security_Reliability/01_monday_validate_and_output_safely/`
- `Demos/Week_13_Security_Reliability/02_wednesday_trust_boundaries/`
- `Demos/Week_14_UX_Refinement/01_monday_usability_friction/`
- `Demos/Week_14_UX_Refinement/02_wednesday_refined_interaction/`
- `Demos/Week_15_Forms_Input/01_monday_basic_form_submit/`
- `Demos/Week_15_Forms_Input/02_wednesday_simulated_login/`

Weeks 1-15 have been refactored into explicit Monday starter and Wednesday iterative/deepening demos. Weeks 16-17 are capstone support rather than normal concept-demo weeks.

Demo delivery convention:

- Finished demo files are reference states.
- In live lectures and recordings, default to manually typing the important lines and copy/pasting only selected sections for time compression.
- This reinforces manual code entry, syntax attention, incremental checking, and visible revision without making "manual typing" a repeated explicit lecture point.

Remaining demo decisions should be made during deck-source production, not by expanding this folder preemptively. Add demos only when a weekly deck needs a concrete visible example, a debugging specimen, or a starter/success pair.

### 16. Preserve The AI-Use Progression

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

### 17. Use 119's Deck-Source Discipline

For each deck source, avoid generic slide text.

Include:

- what the instructor should say
- why the teaching move matters
- what student misconception it addresses
- what demo/example is being used
- how the lab depends on the lecture
- what can be skipped if time is tight

This is the main insight to carry from `119`.

### 18. Use The PowerPoint Workflow's Pass-Based Discipline

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

### 19. Use The RBA/HOMSP Case Study As A Risk Warning

The prior high-throughput 117 slide production process was powerful but operator-dependent.

It relied on a human coordinator actively managing:

- browser-based image generation
- PowerPoint design/alt-text support
- Codex semantic checking and artifact governance
- final human sequencing, judgment, and arbitration

For 118, use high-throughput HOMSP mode only when the current production lane is explicit.

Before starting a work block, name:

- the current week/day deck
- the current artifact lane
- the AI/tool role being used
- the next human arbitration point
- the validation pass that will catch drift

If that cannot be named clearly, slow down and work on one artifact at a time.

### 20. Use 117's Alignment Discipline

For each lecture, confirm:

1. What must students be able to do after this lecture?
2. Which assignment depends on that ability?
3. Which demo supports that ability?
4. What hidden assumption could break student success?

This is the main insight to carry from `117`.

---

## Suggested Production Order For The Next Work Block

Immediate Week 1-4 production path:

1. Re-read the completed `Weekly_Reading_and_Preparation_Guide.md`.
2. Re-read `Deck_Source_Continuity_Brief.md`.
3. Draft Week 1 Monday and Wednesday deck sources directly.
4. Create Week 1 image prompt artifact after the deck sources stabilize.
5. Build Week 1 PowerPoint decks.
6. Record Week 1 Wednesday.
7. Repeat for Weeks 2-4.

Suspended/optional under current time pressure:

- `118_Lecture_Production_Map.md`
- `Lecture_Content_and_Demo_Alignment_Matrix.md`
- separate `LDS-118` deck-source design guide
- separate `LDST-118` template unless immediately useful

Do not start by building PowerPoint slides directly unless the deck source
already exists and has been checked against the continuity brief, reading guide,
demos, assignments, and evidence expectations.

---

## Known Existing 118 Assets

Course-level:

- `Weekly_Reading_and_Preparation_Guide.md`
- `HTML_CSS_JavaScript_High_Level_Course_Plan_v1.md`
- `WIDS_Course_Competency_Framework_v2.md`
- `WIDS_COS_Course_Outcome_Summary_118_v3.pdf`
- `CAM_Course_Architecture.md`
- `IIM_Instructional_Intent_Map.md`
- `APL_Assignment_Progression_Ladder.md`
- `HTML_CSS_JS_AI_Use_Addendum.md`

Assignments:

- `Assignments/Combined_Assignments.md`
- individual assignment files `1` through `17`
- `Assignments/15C_Capstone_Submission_Form.md`
- `Assignments/Success_Solutions/`

Lecture outlines:

- `Lecture_Outlines/Combined_Lectures_Outlines.md`
- individual lecture files `1` through `17`
- `Lecture_Outlines/LOT-01_Lecture_Outline_Template.md`

Course materials:

- Week 8-17 handouts and guides listed above
- root `Approved_API_List.md`
- root `Standard_Student_AI_Use_Policy.md`

Projects/PageForge:

- `Projects/Project_Track_Guide.md`
- `Projects/PageForge_Week_by_Week_Roadmap.md`
- `Projects/PageForge_Instructor_Companion.md`
- `Projects/PageForge_Design_Contract.md`
- `Projects/PageForge_Generation_Workflow.md`
- separate working codebase at `D:\@Coding_Projects\HTML-CSS-JS\PageForge`

Slide work:

- `Lecture_Deck_Sources/Deck_Source_Continuity_Brief.md`
- `Slide_Decks/STD-01_Slide_Template_Design_System.md`
- existing Week 1 PowerPoint experiments
- `Slide_Decks/Images/`

---

## Decisions To Avoid Re-Litigating

- Keep `118` browser-native: HTML, CSS, JavaScript, DOM, debugging, data/state, UX, capstone.
- Do not turn `118` into React, Node, or full-stack.
- Do not pull AI use too early.
- Do not treat jQuery as the main way to write JavaScript.
- Treat jQuery as a third-party helper/library analogy, similar to adding a package in Python.
- Do not redesign assignments unless lecture alignment exposes a concrete blocker.
- Prioritize Weeks 1-4 recordings over perfecting later-course polish.
- Prefer complete deck sources for all weeks before deep visual polish.
- Preserve PageForge as instructor-only unless explicitly changed.

---

## Definition Of Done

Minimum done before class pressure:

- `118_Lecture_Production_Map.md` exists and lists all 34 deck sources.
- `Lecture_Content_and_Demo_Alignment_Matrix.md` exists.
- Weeks 1-4 Monday and Wednesday deck sources are complete.
- Weeks 1-4 Wednesday decks are PowerPoint-complete enough to record.
- Weeks 1-4 Wednesday recordings are complete.

Preferred done before the August recording push:

- All 34 lecture deck sources complete.
- All Week 1-16 Wednesday PowerPoint decks complete enough to record.
- All Week 1-16 Wednesday recordings complete or scheduled.
- Week 17 capstone/presentation support deck decision confirmed.
- PageForge week-by-week instructor-model work is captured as a separate post-reading, post-deck-source lane.
