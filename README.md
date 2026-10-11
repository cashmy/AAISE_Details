# AAISE Details

AAISE stands for **Associate of AI Software Engineering**.

This repository contains curriculum design materials for an AI-augmented associate degree pathway. It documents the structure, rationale, and course-level artifacts used to design foundational courses for the program.

## Repository Purpose

The materials in this repository focus on:

- defining an AI-augmented curriculum design process
- capturing course architecture and competency artifacts
- aligning course outcomes with institutional documentation needs
- preserving design rationale for rapid, structured course development

## Key Documents

### Program and Design Framework

- `CDP_Curriculum_Design_Protocol_v1.0.md`  
  Defines the Curriculum Design Protocol: a structured process for moving from course idea to deployable curriculum.

- `From Weeks to Minutes-A_Moment of Compressed Design.md`  
  Explains the thinking behind the protocol and the role of AI in accelerating curriculum design without losing coherence.

- `Fall_Semester_Blueprint_v1.0.md`  
  Placeholder for a broader semester-level blueprint.

- `10-152-170 Programming in Python (NWTC).pdf`  
  Reference source material related to the Python course.

## Course Artifact Collections

### `10-152-117_Python_Programming`
Python course design artifacts, including:

- learner profile
- outcome identity statement
- competency framework
- teaching doctrine
- course architecture
- lab system
- grading rubric
- WIDS competency framework

### `10-152-118_HTML_CSS_JS.md`
Web development course design artifacts, including:

- learner profile
- competency framework
- course architecture
- lab system
- grading rubric

> Note: despite the `.md` suffix, this is a directory that contains multiple markdown artifacts.

### `10-152-119_Intro_To_Algorithms`
Introduction to Algorithms course design artifacts, including:

- course architecture
- lab architecture
- rubric evaluation
- WIDS course competency framework
- reflection notes

### `10-152-119_Intro_To_Alogrithms_v2`
Separate Introduction to Algorithms refactor materials, preserving the original course folder. Includes the revised reading/session maps, cohort scope review, selective pairing plan, assignment progression, and independent daily demo plan.

The [refactored Instructional Intent Matrix v3](10-152-119_Intro_To_Alogrithms_v2/Planning/IIM_Matrix_v3.md) is the instructor working delivery spine: 24 meeting slots, 22 daily teaching demos, separate Navigator recognition, nine assignments and the two-part final, plus a detailed Week 1 timing template. It preserves the actual schedule and current reading/assessment boundaries; rubric updates and daily outlines/decks remain production work.

The [current Week 1 objectives and assignment scope](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Week_01_Objectives_and_Assignment_Scope_v1.md) reconciles six objectives, curated readings, the two-operation paired ticket assignment, individual class-repo submissions, the packet's rubric emphasis, and 310 gross lab minutes. The master rubric remains unchanged; formal peer review occurs once for AL06 in Week 5.

The [Textbook Coverage and Reference Map v3](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Textbook_Coverage_and_Reference_Map_v3.md) aligns all 16 chapters with the current reading pattern, daily sessions, stronger application depth, and demo/assignment progression. It remains an instructor review proposal; exact textbook headings/pages and preparation times still need verification.

The [Assignment Lab-Time Feasibility Review](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Assignment_Lab_Time_Feasibility_Review_v1.md) evaluates the proposed tasks against the scheduled labs, flags spare-capacity and overload risks, and recommends boundaries/splits for instructor decision before assignment packets are written.

The [updated assignment progression](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Assignment_List_and_Progression_Map_v1.md) carries the subsequent homework, pairing, breather-week, and modular-scaffolding decisions. The [W01D01 teaching comparison](10-152-119_Intro_To_Alogrithms_v2/Planning/119_W01D01_Demo_Comparison_and_Teaching_Review_v1.md) records the original presentation review. The subsequent [W01D01 loan-desk prototype](10-152-119_Intro_To_Alogrithms_v2/Demos/Week_01/Demo_01_Equipment_Request_Contract/README.md) now provides a human-readable report and staged instructor delivery notes without an early parser prerequisite. All 22 demos have separate `test_demo.py` files. The [demo authoring guidelines](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Demo_Authoring_Guidelines_v1.md) establish test separation and propose bounded `argparse` instruction beginning at W02D02. W01D01 now includes a menu-selected, paused teaching walkthrough with an isolated failure and correction, no leftover trace machinery, and purpose docstrings for every function. Broader presentation refactors remain pending.

The [daily demo collection](10-152-119_Intro_To_Alogrithms_v2/Demos/README.md) contains 22 console-first Python demonstrations organized by week and lecture day, student READMEs, automated checks, and two optional browser JavaScript comparisons. Target runtime: Python 3.14.6; verified locally on 3.14.7. No Django or MVT is involved.

Each demo has local instructor `notes.md`, excluded by the collection's `.gitignore`. `Demos` is intended to become its own student-accessible repository under SWTC-AAISE; it has not been published. The separate [Learning Resource Navigator full console application](D:/@Coding_Projects/Python/Leanring_Resource_Navigator/full/README.md) and [independent M0-M7 milestone archive](D:/@Coding_Projects/Python/Leanring_Resource_Navigator/milestones/README.md) are now implemented at the designated development location. The archive passes 129 test methods on Python 3.12.10 and 3.14.7; exact 3.14.6 verification and instructor acceptance remain outstanding.

## Common Artifact Pattern

Across the course folders, the repository uses a repeatable set of curriculum artifacts such as:

- **LP** — Learner Profile
- **OIS** — Outcome Identity Statement
- **CF** — Competency Framework
- **TD** — Teaching Doctrine
- **CAM** — Course Architecture Map
- **LS** — Lab System or Lab Series
- **GR** — Grading Rubric
- **WIDS** — Institutional competency documentation

## Intended Audience

This repository is most useful for:

- curriculum designers
- instructors building AI-native courses
- academic teams aligning new courses to institutional frameworks
- anyone studying how AI can support structured course development

## Notes

- This is primarily a curriculum documentation repository; the Algorithms v2 daily demo collection also contains executable teaching code and verification scripts.
- The materials emphasize structured reasoning, AI-assisted design, and institutional alignment.
## Week 1 Demo Presentation Update

Instructor planning artifacts are grouped in [Planning](10-152-119_Intro_To_Alogrithms_v2/Planning/): IIM, maps, scope/review documents, priorities, and course-level authoring guidelines. Assignments, Demos, PreCourse_Setup, and Reading_Assignments.md remain at the course root; the standalone demo guidelines remain in Demos.

The [AL01 student packet](10-152-119_Intro_To_Alogrithms_v2/Assignments/AL01/AL01_Ticket_Rules_and_Regression.md) contains the progressive paired task, optional full-English M/T/Th starter, fictional data, and brief individual README. Collaboration/submission guides and the separate instructor solution are created; [pre-rehearsal checks](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Week_01_Pre_Rehearsal_Check.md) pass. Outlines/decks, instructor rehearsal, posted deadline directions, and student distribution remain. See the [updated priority list](10-152-119_Intro_To_Alogrithms_v2/Planning/119_Week_01_Production_Priorities.md).

The Tuesday and Thursday algorithms demos now follow Monday's useful-report/teaching-walkthrough standard, with prediction pauses, purpose docstrings, separate regression tests, and screen-sharing colors. The standalone demo repository includes its own [authoring guidelines](10-152-119_Intro_To_Alogrithms_v2/Demos/Demo_Authoring_Guidelines.md).
