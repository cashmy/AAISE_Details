# LAB AND DEMO PROMPT PACK - PYTHON PROGRAMMING

**10-152-117 Python Programming**

---

# Purpose

This instructor-facing prompt pack supports the final creation or refinement of
Python assignment support materials:

- instructor demos
- walkthrough notes
- optional starter files
- withheld successful versions
- small data files
- validation or testing guidance

It is designed for use with a Codex-capable LLM in VS Code or a similar coding
environment.

Important current-state note:

This course already has substantial demo and success-example coverage. This
prompt pack should not be treated as a plan to regenerate the whole assignment
system from scratch.

Its best use is targeted maintenance:

- refine an existing demo
- create a missing walkthrough note
- create a missing or improved successful version
- create a small starter/data file where setup friction is likely
- check demo/assignment separation
- update materials after assignment wording changes
- preserve the current AI-use and concept-understanding principles

The prompts assume the course pattern defined in:

- `../Python_Programming_High_Level_Course_Plan_v1.md`
- `../APL_Assignment_Progression_Ladder.md`
- `../Assignment_Week_Day_Matrix.md`
- `../LS_Lab_System.md`
- `../MRS-Py_Master_Rubric_System.md`
- `../Demos/README.md`
- `Assignments/`

---

# Operating Rules for Codex

Use these rules in every assignment/demo generation request.

```text
You are helping finalize instructor-owned materials for
10-152-117 Python Programming.

Preserve the lecture-demo-lab transfer model:
- the instructor demo must be related to the assignment
- the demo must not solve the assignment directly
- the assignment must require student reasoning, not transcription
- the demo and assignment should share a concept family and code pattern, but
  use different scenarios, data, names, or requirements

Keep the scope appropriate for an 8-week compressed beginner Python course.

Preserve the course AI progression:
- Weeks 1-2: manual-first, no AI for normal student work unless instructor
  explicitly allows it
- Weeks 3-4: bounded AI comparison, explanation, or debugging only after manual
  work begins
- Weeks 5-6: bounded AI support for files, data, APIs, and architecture
  recognition with validation and explanation
- Weeks 7-8: accountable AI-assisted project framing, capstone build, and final
  justification

Use beginner-readable Python.
Prefer the Python standard library.
Avoid unnecessary dependencies.
Do not turn recognition-level previews into full framework builds.
Do not expose successful-version content inside student-facing assignments.
Maintain ASCII-only Markdown unless the source file already uses otherwise.
Use clear headings, short requirements, and concrete deliverables.
```

---

# Current Coverage Sanity Check

As of the current course structure:

- `Demos/` already contains week-level demo folders for Weeks 1-8.
- `Assignment_Success_Examples/` already contains success examples for A1-A12.
- Week 7 and Week 8 already contain strong demo/reference examples for RBA
  framing, proposal shaping, capstone validation, AI-use justification, and
  final presentation.
- A13-A16 do not necessarily need full "successful code" examples because they
  are project-framing, proposal, capstone-build, and presentation/accountability
  assignments. They may benefit more from templates, annotated examples, and
  instructor review guides.

Recommended use by assignment range:

| Assignment Range | Existing Coverage | Prompt Pack Use |
|---|---|---|
| A1-A5 | Strong demos and success examples | Refine only if assignment wording changes |
| A6-A7 | Strong demo base; success examples exist | Useful for broken-code variants or reading-code variants |
| A8-A12 | Strong demos, data files, and success examples | Useful for data/API fallback updates or recognition-level walkthroughs |
| A13-A14 | Demo/reference examples exist | Use for framing/proposal templates and review examples |
| A15-A16 | Capstone demo/reference examples exist | Use for validation examples, AI-use justification examples, and presentation guidance |

Conclusion:

The full prompt set remains useful as a reusable operating kit, but normal use
should be selective rather than comprehensive.

---

# Recommended Folder Pattern

The current course structure is:

```text
10-152-117_Python_Programming/
  Assignments/
  Assignment_Success_Examples/
  Demos/
```

Recommended support pattern:

```text
Demos/
  Week_[NN]_[Theme]/
    ##_demo_name.py
    ##_demo_walkthrough.md

Assignment_Success_Examples/
  [assignment_success_file].py
  [assignment_success_notes].md
```

Starter files may be added only when useful. If a starter file is needed, place
it with a clear name and do not include the completed solution.

---

# Prompt 1 - Finalize Student Assignment

Use this prompt when an assignment exists and you want Codex to polish the
student-facing version.

```text
You are working in the 10-152-117 Python Programming course folder.

Task:
Finalize the student-facing assignment for [ASSIGNMENT NUMBER AND TITLE].

Read these files first:
- Python_Programming_High_Level_Course_Plan_v1.md
- APL_Assignment_Progression_Ladder.md
- Assignment_Week_Day_Matrix.md
- LS_Lab_System.md
- MRS-Py_Master_Rubric_System.md
- Assignments/[ASSIGNMENT FILE NAME].md

Produce:
- a polished student-facing assignment in Assignments/[ASSIGNMENT FILE NAME]

Requirements:
- preserve the assignment's week, phase, purpose, and AI allowance
- keep requirements beginner-readable and concrete
- include clear deliverables
- include a submission checklist
- include a reflection or explanation prompt
- align evaluation focus to the MRS categories
- keep the assignment realistic for the mapped session time
- do not include a complete solution
- do not make the task more advanced than the course plan supports

Before editing, briefly summarize the finalization approach.
After editing, list changed files and any design decisions.
```

---

# Prompt 2 - Build Instructor Demo

Use this prompt when the student assignment exists and you want a concrete
instructor demo with code and notes.

```text
You are working in the 10-152-117 Python Programming course folder.

Task:
Create or refine the instructor demo package for [ASSIGNMENT NUMBER AND TITLE].

Read these files first:
- LS_Lab_System.md
- APL_Assignment_Progression_Ladder.md
- Assignment_Week_Day_Matrix.md
- Assignments/[ASSIGNMENT FILE NAME].md
- Demos/README.md

Use the existing weekly demo folder if it exists:
- Demos/Week_[NN]_[Theme]/

Produce as appropriate:
- one beginner-readable demo .py file
- optional demo walkthrough .md file
- optional tiny data file if the demo needs data

Demo requirements:
- teach the same concept family as the assignment
- do not solve the same scenario, data set, or exact requirements
- include a short opening frame in notes or comments if helpful
- include what students should notice
- include a transfer bridge from demo to assignment
- include likely student mistakes or misconceptions
- include a clear stop point before the assignment answer

Code requirements:
- use beginner-readable Python
- prefer standard library only
- keep the file small enough to demo live
- use clear variable names
- include only helpful comments
- print visible output or evidence when useful

Before editing, briefly summarize how the demo will differ from the assignment.
After editing, list changed files and how the demo supports near transfer.
```

---

# Prompt 3 - Create Starter Files

Use this prompt when an assignment needs starter code, provided data, or broken
code.

```text
You are working in the 10-152-117 Python Programming course folder.

Task:
Create starter materials for [ASSIGNMENT NUMBER AND TITLE].

Read:
- LS_Lab_System.md
- Assignments/[ASSIGNMENT FILE NAME].md
- MRS-Py_Master_Rubric_System.md

Produce only the materials students should receive at the beginning of the
assignment.

Starter requirements:
- do not include the completed solution
- include TODO markers only where they clarify student work
- provide enough structure to reduce setup friction
- preserve the required student thinking
- include sample data only if it does not answer the assignment
- keep Python beginner-readable
- avoid unnecessary dependencies

Good uses of starter files:
- intentionally broken code for debugging
- provided CSV or JSON files
- API-style simulated JSON response
- recognition-level architecture example
- capstone framing template

After editing, list changed files and explain what remains for students to do.
```

---

# Prompt 4 - Create Successful Version

Use this prompt only for withheld instructor materials or post-assignment study
examples.

```text
You are working in the 10-152-117 Python Programming course folder.

Task:
Create the withheld successful version for [ASSIGNMENT NUMBER AND TITLE].

Read:
- LS_Lab_System.md
- Assignments/[ASSIGNMENT FILE NAME].md
- MRS-Py_Master_Rubric_System.md

Use or create an appropriate file in:
- Assignment_Success_Examples/

Produce:
- one complete acceptable solution, if code is appropriate
- optional success notes explaining assumptions, tests, and teaching points
- optional small data file only if needed

Successful version requirements:
- show one acceptable solution, not the only possible solution
- keep code beginner-readable
- include visible output, sample inputs, or testing evidence
- include a concise explanation of assumptions and tradeoffs
- include AI-use accountability only when the assignment permits AI
- do not make the solution so advanced that beginners cannot study it

After editing, list changed files and identify which rubric categories the
successful version illustrates.
```

---

# Prompt 5 - Create Complete Assignment Support Package

Use this prompt when you want Codex to create the support materials for one
assignment in a single pass.

```text
You are working in the 10-152-117 Python Programming course folder.

Task:
Create the complete instructor-support package for [ASSIGNMENT NUMBER AND TITLE].

Read:
- Python_Programming_High_Level_Course_Plan_v1.md
- APL_Assignment_Progression_Ladder.md
- Assignment_Week_Day_Matrix.md
- LS_Lab_System.md
- MRS-Py_Master_Rubric_System.md
- Assignments/[ASSIGNMENT FILE NAME].md
- Demos/README.md

Create or refine as appropriate:
- instructor demo code in the correct Demos/Week_[NN]_[Theme]/ folder
- optional demo walkthrough notes
- optional starter file or data file
- withheld success example in Assignment_Success_Examples/
- optional success notes

Package requirements:
- demo and assignment must be related but not identical
- starter materials must not include the solution
- successful version must remain withheld
- preserve the assignment AI-use rule
- use beginner-readable Python
- keep scope appropriate for the assigned week
- include visible output or validation evidence
- align with the MRS categories named in the assignment

After editing, provide a short file inventory and note any human review points.
```

---

# Assignment-Specific Prompt Context Blocks

Use one of these blocks with any of the prompts above.

## A1 - First Programs

```text
Assignment file:
Assignments/01_First_Programs.md

Core goal:
Students create 2-3 tiny Python programs using output, variables, strings,
numbers, expressions, and basic input/output if introduced.

Demo/assignment relationship:
Demo may use a greeting and small tip calculation. Assignment should use
different options such as a converter, total-cost estimator, or personalized
message builder.

AI level:
Manual first. No AI for normal student work unless the instructor explicitly
allows it.
```

## A2 - Decisions in Code

```text
Assignment file:
Assignments/02_Decisions_in_Code.md

Core goal:
Students build a small decision-based program using booleans, comparisons, and
if/elif/else logic.

Demo/assignment relationship:
Demo may use shipping or event eligibility. Assignment should use a different
scenario such as grade checker, discount checker, recommendation tool, weather
message, or login-style rule checker.

AI level:
Manual first. No AI for normal student work unless explicitly allowed.
```

## A3 - Loops and Repetition

```text
Assignment file:
Assignments/03_Loops_and_Repetition.md

Core goal:
Students build one loop-based program with repeated behavior, a clear stopping
point, and visible output.

Demo/assignment relationship:
Demo may use a countdown or repeated name entry. Assignment should use a
different loop scenario such as total accumulator, practice quiz loop, simple
menu, or number sequence generator.

AI level:
Manual first. No AI for normal student work unless explicitly allowed.
```

## A4 - Function Builder

```text
Assignment file:
Assignments/04_Function_Builder.md

Core goal:
Students create or refactor a small program so important pieces of logic are
placed into functions with parameters and/or return values.

Demo/assignment relationship:
Demo may refactor a temperature converter. Assignment should refactor or build
a different program such as a calculator, menu utility, or repeated
conditional/loop program.

AI level:
Limited comparison after a manual version or manual plan exists.
```

## A5 - List or Dictionary Mini-App

```text
Assignment file:
Assignments/05_List_or_Dictionary_Mini-App.md

Core goal:
Students build a small mini-app that uses a list or dictionary to store,
retrieve, and iterate over data.

Demo/assignment relationship:
Demo may use a grocery lookup or classroom roster. Assignment should use a
different domain such as score tracker, task list, inventory lookup, contact
lookup, or menu selector.

AI level:
Limited comparison or revision after a working manual version or clear manual
plan exists.
```

## A6 - Debug and Explain

```text
Assignment file:
Assignments/06_Debug_and_Explain.md

Core goal:
Students repair intentionally broken code, test the fix, and explain the bug
and evidence.

Demo/assignment relationship:
Demo may debug a broken discount or loop accumulator program. Assignment should
use different broken code involving functions, loops, or collections.

Starter need:
This assignment likely benefits from provided broken code.

AI level:
Bounded AI debugging only after manual diagnosis is attempted.
```

## A7 - Reading Structured Code

```text
Assignment file:
Assignments/07_Reading_Structured_Code.md

Core goal:
Students inspect, explain, and lightly modify a simple class-based Python
example and compare it with procedural or function-based structure.

Demo/assignment relationship:
Demo may use a simple `Book` or `Pet` class. Assignment should use a different
class such as `Student`, `Task`, `Product`, or `Ticket`.

Starter need:
This assignment likely benefits from provided structured example code.

AI level:
Bounded explanation support with verification against actual code.
```

## A8 - Save and Load Utility

```text
Assignment file:
Assignments/08_Save_and_Load_Utility.md

Core goal:
Students build a small program that writes data to a file, reads data back, and
handles basic failure paths.

Demo/assignment relationship:
Demo may save and load favorite movies. Assignment should use a different
domain such as note keeper, task list, progress tracker, saved preferences, or
score file.

AI level:
Bounded support after manual work begins, especially for comparing file
handling or improving error messages.
```

## A9 - Structured Data Reader

```text
Assignment file:
Assignments/09_Structured_Data_Reader.md

Core goal:
Students read CSV or JSON data and produce a useful filtered result, summary,
selected record display, or formatted report.

Demo/assignment relationship:
Demo may read a small book or snack inventory file. Assignment should use a
different provided CSV/JSON file such as course progress, simple products,
events, contacts, or scores.

Starter need:
This assignment likely benefits from a provided CSV or JSON file.

AI level:
Bounded comparison of parsing approaches or clarification of data structure.
```

## A10 - Data Representation and App-Structure Preview

```text
Assignment file:
Assignments/10_Data_Representation_and_App-Structure_Preview.md

Core goal:
Students compare multiple representations of the same information and explain
how representation affects use.

Demo/assignment relationship:
Demo may compare one customer record as text, CSV, JSON, dictionary, and simple
class. Assignment should use a different information type such as course,
product, task, event, or support ticket.

Starter need:
This assignment benefits from provided comparison examples.

AI level:
Bounded explainer only. Students must restate ideas in their own words.
```

## A11 - API Data Fetcher

```text
Assignment file:
Assignments/11_API_Data_Fetcher.md

Core goal:
Students retrieve or work with API-style data, inspect JSON response structure,
extract selected values, and validate code.

Demo/assignment relationship:
Demo may use a simulated weather response. Assignment should use a different
approved API, controlled endpoint, or instructor-provided simulated response.

Starter need:
This assignment may benefit from a simulated JSON fallback to avoid live API
fragility.

AI level:
Bounded implementation support allowed with validation and explanation.
```

## A12 - Python App Architecture Preview

```text
Assignment file:
Assignments/12_Python_App_Architecture_Preview.md

Core goal:
Students inspect a simple Python web-app flow and explain input, form handling,
view/controller-like logic, template output, and data movement.

Demo/assignment relationship:
Demo may inspect a tiny contact form flow. Assignment should inspect a
different guided example such as feedback form, event signup, or ticket request.

Starter need:
This assignment benefits from provided architecture example files or a guided
walkthrough. Keep it recognition-level.

AI level:
Bounded explanation or guided-inspection support with verification against the
actual example.
```

## A13 - RBA Project Framing Exercise

```text
Assignment file:
Assignments/13_RBA_Project_Framing_Exercise.md

Core goal:
Students frame a possible project before coding by identifying purpose, inputs,
outputs, constraints, structure, and AI-use boundaries.

Demo/assignment relationship:
Demo may compare weak and strong framing for a simple tracker project.
Assignment should ask students to frame their own possible capstone or approved
practice scenario.

Starter need:
This assignment may benefit from a framing template.

AI level:
Bounded AI support only after initial manual framing.
```

## A14 - Capstone Proposal and Approval

```text
Assignment file:
Assignments/14_Capstone_Proposal_and_Approval.md

Core goal:
Students submit a realistic, explainable, approved Python capstone proposal
with scope, features, structure, risks, and AI-use boundaries.

Demo/assignment relationship:
Demo may show how an oversized project is narrowed into an approved course-fit
proposal. Assignment should apply that process to each student's project.

Starter need:
This assignment may benefit from a proposal template.

AI level:
Bounded and disclosed after the student has an initial project idea.
```

## A15 - Capstone Build

```text
Assignment file:
Assignments/15_Capstone_Build.md

Core goal:
Students complete the approved capstone project using appropriate Python
fundamentals, useful structure, data handling when relevant, debugging,
validation, and accountable AI use.

Demo/assignment relationship:
Demo should focus on capstone work habits, testing, refactoring, or feature
slicing rather than building a full parallel capstone.

AI level:
Strategic AI use allowed with accountability.
```

## A16 - AI Use Justification and Final Presentation

```text
Assignment file:
Assignments/16_AI_Use_Justification_and_Final_Presentation.md

Core goal:
Students present the final capstone and explain what they built, how it works,
how they tested it, what they would improve, and how AI was used if applicable.

Demo/assignment relationship:
Demo may show a short sample explanation of a tiny project and a sample AI-use
justification. Assignment applies the structure to each student's project.

AI level:
AI may help prepare wording or polish materials if allowed, but cannot replace
understanding.
```

---

# Review Checklist for Generated Materials

Use this checklist after Codex creates or refines support materials.

- The demo and assignment are related but not identical.
- The student-facing assignment does not include the answer.
- The successful version is separated from starter materials.
- The AI boundary matches the assignment week.
- The Python is beginner-readable.
- The scope fits the mapped course session.
- Any data files are tiny and inspectable.
- Recognition-level preview work has not become a full advanced build.
- The material supports explanation and ownership, not only code completion.
- The generated materials align with the MRS categories named in the assignment.
