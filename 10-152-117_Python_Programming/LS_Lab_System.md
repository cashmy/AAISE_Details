# PYTHON PROGRAMMING LAB SYSTEM - LS-Py v2

**Course:** `10-152-117 Python Programming`

---

# Purpose

This artifact defines the current lab and assignment system for `10-152-117
Python Programming`.

It replaces the earlier weekly lab concept map with a structure aligned to the
current course plan, assignment progression ladder, assignment week/day matrix,
lecture outlines, demos, and master rubric system.

Primary source artifacts:

- `Python_Programming_High_Level_Course_Plan_v1.md`
- `APL_Assignment_Progression_Ladder.md`
- `Assignment_Week_Day_Matrix.md`
- `Unit-Week_Descriptions.md`
- `MRS-Py_Master_Rubric_System.md`
- `Assignments/`
- `Demos/`

---

# Course Lab Philosophy

This course is a compressed 8-week Python foundation course.

The lab system is designed to help beginners become capable novice programmers
who can:

- make small Python programs work
- trace and explain what the code is doing
- debug and revise with evidence
- use files, structured data, and introductory API-style data
- use AI support only when it fits the assignment stage
- complete and explain a small capstone project

Unlike the HTML/CSS/JavaScript course, this course does not rely on one evolving
semester project. It uses short, targeted assignments with late integration in
the capstone.

---

# Standard Learning Pattern

Each lab sequence should preserve this instructional rhythm:

```text
concept frame -> instructor demo -> guided practice -> student lab ->
explanation / checkpoint
```

Individual sessions may contain more than one part of this rhythm. The rhythm
should not be interpreted as one full lecture day followed by isolated lab days.

The instructor demo should be similar enough to the assignment that students can
transfer the concept, but different enough that students must think rather than
copy.

---

# Standard Assignment Pattern

Most student-facing assignments use the same structure:

- Context
- Objective
- Task
- Requirements
- AI Use
- Submission Requirements
- Reflection / Explanation
- Evaluation Focus
- Success Criteria
- Instructor Notes

This consistency is intentional. Beginners benefit from predictable assignment
shape while the technical content changes.

---

# AI Involvement Progression

The course AI pattern is:

```text
Manual First -> Bounded AI Comparison / Debugging -> Accountable AI-Assisted
Project Work
```

## Phase 1 - Manual First

Weeks 1-2 keep normal student work manual-first.

Students should build confidence with:

- values
- variables
- input/output
- conditionals
- loops
- tracing behavior

AI may be demonstrated by the instructor, but it should not become the normal
student path for completing early assignments.

## Phase 2 - Bounded Comparison and Explanation

Weeks 3-4 allow limited AI comparison, explanation, or debugging support after a
manual baseline or manual diagnosis exists.

Students should learn that AI can help, but that ownership requires reading,
testing, modifying, and explaining the result.

## Phase 3 - Bounded Implementation Support

Weeks 5-6 allow more purposeful AI support around files, structured data, APIs,
and app-architecture recognition.

AI may help students compare parsing approaches, understand unfamiliar terms,
inspect examples, or generate a candidate implementation. Students must still
validate the result and explain how the program handles data.

## Phase 4 - Accountable AI-Assisted Capstone Work

Weeks 7-8 introduce RBA-informed framing and accountable capstone development.

Students may use AI strategically, but they must:

- define intent and scope before relying on AI
- identify AI-use boundaries
- inspect, test, and adapt AI output
- explain what decisions remained human decisions
- justify AI use in the final presentation

---

# Phase and Assignment Structure

## Phase 1 - Foundations + Manual Habits

**Weeks 1-2**

Primary goal:

Students learn that they can write, run, fix, and explain small Python programs.

Assignments:

- `A1 - First Programs`
- `A2 - Decisions in Code`
- `A3 - Loops and Repetition`

Lab emphasis:

- tiny working programs
- visible output
- input/output flow
- branch tracing
- loop stopping conditions
- explanation in plain language

AI stance:

- no AI for normal student work unless explicitly allowed by the instructor

## Phase 2 - Structure + Code Literacy

**Weeks 3-4**

Primary goal:

Students move from isolated code fragments toward organized, readable, testable
programs.

Assignments:

- `A4 - Function Builder`
- `A5 - List or Dictionary Mini-App`
- `A6 - Debug and Explain`
- `A7 - Reading Structured Code`

Lab emphasis:

- functions as named responsibilities
- parameters and return values
- lists and dictionaries
- basic state management
- debugging as normal practice
- expected-vs-actual reasoning
- reading simple class-based code at a recognition level

AI stance:

- bounded comparison, refactoring, debugging, or explanation after manual work
  begins

## Phase 3 - Data, Files, and Bounded AI Support

**Weeks 5-6**

Primary goal:

Students connect Python to persistent data, structured data, external data, and
larger application contexts.

Assignments:

- `A8 - Save and Load Utility`
- `A9 - Structured Data Reader`
- `A10 - Data Representation and App-Structure Preview`
- `A11 - API Data Fetcher`
- `A12 - Python App Architecture Preview`

Lab emphasis:

- saving and loading data
- text, CSV, and JSON exposure
- basic error handling
- data representation choices
- API request/response thinking
- JSON response inspection
- recognition-level Python application architecture
- Django MVT, templates, forms, and views as preview concepts

AI stance:

- bounded support for explanation, comparison, implementation help, and
  validation

Design note:

Weeks 5-6 are intentionally dense. This density is acceptable because students
also receive CSV/JSON exposure in `10-152-118 HTML/CSS/JavaScript`. In this
course, CSV/JSON work becomes reinforcement plus a deeper Python-side view of
reading, parsing, transforming, and explaining structured data.

## Phase 4 - RBA Mini-Unit + Capstone Application

**Weeks 7-8**

Primary goal:

Students use Python fundamentals, debugging, structured development, bounded AI
use, and RBA-informed framing to complete and explain a small capstone project.

Assignments:

- `A13 - RBA Project Framing Exercise`
- `A14 - Capstone Proposal and Approval`
- `A15 - Capstone Build`
- `A16 - AI Use Justification and Final Presentation`

Lab emphasis:

- intent-first project framing
- inputs, outputs, constraints, risks, and success criteria
- realistic scope control
- approved capstone implementation
- testing and revision
- final explanation and AI-use accountability

AI stance:

- strategic use allowed with accountability

---

# Demo-to-Lab Transfer Rule

For every major assignment, the instructor demo should follow this rule:

```text
same concept family, different scenario
```

The demo may show the pattern, but it should not give students the assignment
answer.

Examples:

- Demo a tip calculator; assignment uses a unit converter or total-cost
  estimator.
- Demo a shipping eligibility decision; assignment uses a grade or discount
  checker.
- Demo a grocery list manager; assignment uses a score tracker or task list.
- Demo a book JSON reader; assignment uses course progress or inventory data.
- Demo a simulated weather API response; assignment uses a different approved
  endpoint or provided JSON response.

This preserves adult-learning transfer while preventing mindless copying.

---

# Recommended Folder Relationship

Current folders:

```text
10-152-117_Python_Programming/
  Assignments/
  Assignment_Success_Examples/
  Demos/
  Lecture_Outlines/
  Slide_Decks/
```

The existing structure is appropriate.

Recommended future refinement:

- Keep student-facing assignment instructions in `Assignments/`.
- Keep instructor demo code and walkthroughs in `Demos/`.
- Keep withheld successful versions in `Assignment_Success_Examples/`.
- Add starter files only where setup friction would distract from the learning
  goal.

---

# Assignment Support Expectations

Each assignment should eventually have enough support for the instructor to run
it cleanly:

- student-facing assignment
- instructor demo or walkthrough
- optional starter file
- successful version or success example
- rubric alignment
- reflection or explanation prompt

Not every assignment needs a starter file. Early assignments may benefit from a
blank-file start, while later assignments may benefit from provided data files,
broken code, guided examples, or scaffolded folders.

---

# Evaluation Alignment

Evaluation should align to `MRS-Py_Master_Rubric_System.md`.

The six technical categories are:

- `T1 - Python Fundamentals`
- `T2 - Program Logic and Control Flow`
- `T3 - Code Organization and Structure`
- `T4 - Data Handling and Integration`
- `T5 - Debugging, Testing, and Validation`
- `T6 - AI/RBA-Assisted Development and Accountability`

Core abilities should be included where observable, especially:

- problem solving
- communication
- productivity
- value learning
- professionalism

Small assignments should use a limited number of rubric rows. The capstone and
final presentation should use broader rubric coverage.

---

# Failure Prevention

## If a student struggles early

Do:

- shrink the task
- return to a tiny working example
- focus on one working behavior
- ask the student to explain one line at a time
- use instructor support before AI becomes a replacement path

## If a student over-relies on AI

Do:

- ask what the code does
- ask what input produces what output
- ask which line controls the behavior
- ask what they changed or rejected
- require a manual explanation before accepting the work

## If a student is advanced

Do:

- add a small extension
- ask for cleaner structure
- ask for better validation
- ask for another test case
- ask for a comparison of two approaches

---

# Final System Statement

The Python lab system is designed to build confidence first, then structure,
then data handling, then accountable AI-assisted capstone work.

Students should not leave merely having produced Python code.

They should leave able to understand, debug, explain, revise, and take ownership
of small Python programs.
