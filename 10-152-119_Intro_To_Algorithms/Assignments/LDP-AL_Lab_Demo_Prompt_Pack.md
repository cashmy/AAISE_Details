# LAB AND DEMO PROMPT PACK - ALGORITHMIC PROBLEM SOLVING

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This instructor-facing prompt pack supports the final creation of lab
assignments, instructor demos, starter files, and successful versions for
`10-152-119 Algorithmic Problem Solving`.

It is designed for use with a Codex-capable LLM in VS Code or a similar coding
environment.

The prompts assume the course pattern defined in:

- `LASO-AL_Lab_Assignment_System_Overview.md`
- `Lab_Progression_Ladder_v2.md`
- `../v2/IIM_Matrix_v2.md`
- `../v2/MRS-AL_Master_Rubric_System.md`
- `../v2/Textbook_Coverage_and_Reference_Map_v2.md`

---

# Operating Rules for Codex

Use these rules in every lab/demo generation request.

```text
You are helping finalize instructor-owned materials for
10-152-119 Algorithmic Problem Solving.

Preserve the lecture-demo-lab transfer model:
- the instructor demo must be related to the lab
- the demo must not solve the lab directly
- the lab must require student reasoning, not transcription
- the demo and lab should share a concept family, evidence type, and reasoning
  pattern, but use different scenarios or data

Keep the scope appropriate for an 8-week compressed introductory algorithms
course using Python.

Do not make the course web-based.
Do not add advanced theory beyond the stated week.
Do not turn the textbook into a coverage checklist.
Do not remove the AI boundary.
Do not expose successful-version content inside the student-facing assignment.
Assume the requested `Assignments/Lab_[NN]/` package folder does not already
exist unless the instructor explicitly says it does.
Do not spend time searching for prior lab packages to imitate. Use this prompt
pack, the instructor-facing lab draft, the student-facing lab file, and the
course alignment artifacts as the source of structure.
If a prior lab package does exist, use it only for basic folder naming
consistency. Do not copy its scenario, code structure, evidence values, or
scaffolding level unless the instructor explicitly requests that.
There is usually a student-facing lab file in
`Assignments/Student_Facing/`. Read it when creating demos, starters, or
successful versions so generated materials match what students will see.

Maintain ASCII-only Markdown unless the source file already uses otherwise.
Use clear headings, short requirements, and concrete deliverables.
```

---

# Clarifying-Question Gate

Before creating or modifying a lab package, Codex must briefly check for
ambiguity.

If any of the following are unclear, Codex must ask clarifying questions before
writing files:

- which lab number and title are being generated
- whether the package already exists or should be created fresh
- whether the instructor wants a generic starter or a scenario-specific starter
- how much code scaffolding is acceptable in the starter
- which demo scenario should be used
- which withheld success-version scenario should be used
- whether the student-facing lab file should be treated as authoritative
- what visible evidence format is required
- whether a timing harness, test runner, formatter, scoring function, traversal
  engine, or other helper structure is allowed
- whether any prior generated package should be used as a pattern

Default assumptions if the instructor does not specify otherwise:

- create a fresh `Assignments/Lab_[NN]/` package
- read the student-facing lab file if it exists
- use a demo scenario that is related to the lab but not the same
- use a success-version scenario that is different from the demo
- keep starter files generic unless a scenario-specific starter is explicitly
  requested
- preserve student reasoning by using TODOs, instructions, and brief pseudocode
  instead of completed helper infrastructure
- do not imitate prior generated lab packages beyond basic folder naming

This gate exists to prevent typicality-biased code generation, accidental
copying from another lab, and drift away from the course's lecture-demo-lab
transfer model.

---

# Recommended Folder Pattern

When asking Codex to create final files, use a lab-specific folder pattern such
as:

```text
Assignments/
  Lab_01_Precision_and_Correctness.md
  Lab_01/
    demo/
      demo_notes.md
      demo_code.py
    starter/
      lab_01_starter.py
    success/
      lab_01_success.py
      success_notes.md
```

The exact file names can be adjusted later, but each lab should eventually keep
student-facing material, demo material, starter files, and successful versions
clearly separated.

---

# Prompt 1 - Finalize Student Lab

Use this prompt when the drafted lab assignment exists and you want Codex to
create the polished final student-facing lab.

```text
You are working in the 10-152-119 Algorithmic Problem Solving course folder.

Task:
Finalize the student-facing lab assignment for [LAB NUMBER AND TITLE].

Read these files first:
- Assignments/LASO-AL_Lab_Assignment_System_Overview.md
- Assignments/Lab_Progression_Ladder_v2.md
- Assignments/[LAB FILE NAME].md
- v2/IIM_Matrix_v2.md
- v2/MRS-AL_Master_Rubric_System.md

Produce:
- a polished student-facing lab assignment in Assignments/[LAB FILE NAME]
- keep the instructor demo plan in the file only if the course pattern expects
  embedded instructor guidance; otherwise move demo-only content into a
  separate demo notes file and leave a concise instructor note

Requirements:
- preserve the lab's week, unit, competency alignment, and AI involvement level
- preserve the lab's evidence requirement
- keep the assignment realistic for a compressed 8-week course
- make the required student deliverables concrete
- avoid making the demo and lab identical
- include a clear submission checklist
- include a short reflection prompt
- include success criteria aligned to the MRS
- do not include a full solution in the student-facing assignment

Before editing, briefly summarize the finalization approach.
After editing, list changed files and any design decisions.
```

---

# Prompt 2 - Build Instructor Demo

Use this prompt when the student lab exists and you want a concrete instructor
demo with code, notes, and evidence.

```text
You are working in the 10-152-119 Algorithmic Problem Solving course folder.

Task:
Create the instructor demo package for [LAB NUMBER AND TITLE].

Read these files first:
- Assignments/LASO-AL_Lab_Assignment_System_Overview.md
- Assignments/Lab_Progression_Ladder_v2.md
- Assignments/[LAB FILE NAME].md
- Assignments/Student_Facing/[LAB FILE NAME].md, if it exists
- Lecture_Outlines/LOT-AL_Alignment-Based_Lecture_Outline_Template.md

Assume the lab-specific demo folder does not exist unless the instructor tells
you otherwise. Create:
- Assignments/Lab_[NN]/demo/

Produce:
- demo_notes.md
- demo_code.py, if code is useful for the lab
- optional demo_data.csv or small sample data file, if useful

Demo requirements:
- the demo must teach the same concept family as the lab
- the demo must not solve the same scenario, use the same data, or reveal the
  lab answer
- include a short opening frame
- include the demo problem
- include what students should notice
- for early labs, include an algorithm representation bridge that compares
  plain English, pseudocode, and Python-style logic for the same process
- include a transfer bridge from demo to lab
- include visible evidence such as a trace table, timing table, diagram,
  comparison table, ranking table, or traversal order
- include a stop point so students still have meaningful lab work
- include likely student misconceptions

Code requirements, if code is created:
- use beginner-readable Python
- keep dependencies to the standard library unless a dependency is explicitly
  justified
- print or generate visible evidence
- keep the file small enough to demo live
- use clear variable names
- include only helpful comments
- instructor demo code should use light ANSI color when color reinforces an
  observable distinction in the demo, especially for headings, pass/fail
  results, warnings, edge cases, timing signals, trace movement, comparison
  winners, and summary statements
- ANSI color should remain a presentation layer, not part of the assessed
  student requirement
- include a `NO_COLOR` environment-variable fallback when practical
- if color would be purely decorative and would not clarify the evidence, state
  that decision in the demo notes
- do not introduce third-party console formatting packages such as `rich`
  until a later lab explicitly benefits from that added dependency; if used,
  document the dependency in `Assignments/requirements.txt` and the lab's
  instructor notes

Before editing, briefly summarize how the demo will differ from the lab.
After editing, list changed files and how the demo supports near transfer.
```

---

# Prompt 3 - Create Starter Files

Use this prompt when a lab needs starter files or structured scaffolding.

```text
You are working in the 10-152-119 Algorithmic Problem Solving course folder.

Task:
Create starter files for [LAB NUMBER AND TITLE].

Read:
- Assignments/[LAB FILE NAME].md
- Assignments/Student_Facing/[LAB FILE NAME].md, if it exists
- Assignments/LASO-AL_Lab_Assignment_System_Overview.md

Assume the lab-specific starter folder does not exist unless the instructor
tells you otherwise. Create:
- Assignments/Lab_[NN]/starter/

Produce only the starter materials students should receive at the beginning of
the lab.

Starter requirements:
- do not include the completed solution
- include TODO markers only where they clarify student work
- provide enough structure to reduce setup friction
- preserve the required reasoning work
- include sample data only if it does not answer the lab
- keep Python beginner-readable
- prefer instructions, placeholders, and brief pseudocode over completed helper
  functions
- do not provide a fully working test runner, evidence formatter, comparison
  table generator, scoring function, traversal engine, or timing harness unless
  the lab specifically requires that structure to remove non-essential setup
  friction
- when a reusable function is central to the lab objective, provide the function
  name, docstring, parameter expectations, and TODO comments instead of the
  completed logic
- leave students responsible for the core algorithm, rule ordering, test case
  design, evidence table completion, and explanation
- if the starter includes code, it should be skeletal enough that running it
  clearly shows unfinished TODO work rather than producing a polished table

After editing, list changed files and explain what remains for students to do.
```

---

# Prompt 4 - Create Successful Version

Use this prompt only after the assignment has closed or when preparing withheld
instructor materials.

```text
You are working in the 10-152-119 Algorithmic Problem Solving course folder.

Task:
Create the withheld successful version for [LAB NUMBER AND TITLE].

Read:
- Assignments/[LAB FILE NAME].md
- Assignments/Student_Facing/[LAB FILE NAME].md, if it exists
- Assignments/LASO-AL_Lab_Assignment_System_Overview.md
- v2/MRS-AL_Master_Rubric_System.md

Assume the lab-specific success folder does not exist unless the instructor
tells you otherwise. Create:
- Assignments/Lab_[NN]/success/

Produce:
- success_solution.py, if code is appropriate
- success_notes.md
- optional_colorized_success_solution.py, when colorized console output helps
  make evidence easier to inspect
- optional_colorized_notes.md, when an optional colorized solution is created

Successful version requirements:
- show one complete acceptable solution, not the only possible solution
- include tests or visible evidence matching the assignment
- include a concise explanation of assumptions and tradeoffs
- include an AI-use accountability example if the lab permits AI
- make the solution readable for post-assignment study
- do not weaken the original assignment by making the successful version too
  generic
- keep `success_solution.py` plain and focused on the required solution
- if a colorized success version is created, it must preserve the same logic and
  evidence while changing only the presentation layer
- colorized success versions demonstrate refinement after correctness,
  observability, and explanation; they are not grading requirements
- use ANSI color first; do not use third-party presentation packages unless the
  lab explicitly benefits from the added dependency
- include a `NO_COLOR` environment-variable fallback when practical
- for fixed-width console tables, pad the visible text before applying ANSI
  color so color codes do not break column alignment
- document any optional colorized version as a usability/readability refinement
- Lab 07 may include a second optional Rich formatted success version when
  ranking tables, similarity scores, recommendation summaries, or AI/data
  evidence benefit from richer table/panel formatting
- Lab 07 may also include an optional Rich formatted demo version when the
  instructor wants to demonstrate how richer console UI can clarify structured
  ranking evidence before showing the success-version progression
- if a Rich version is created, keep it separate from the plain and ANSI
  versions, document the `rich` dependency in `Assignments/requirements.txt`,
  and explain the UI/UX comparison value in the corresponding Rich notes file

After editing, list changed files and identify which rubric categories the
successful version illustrates.
```

---

# Prompt 5 - Create Lab Folder Package

Use this prompt when you want Codex to build the complete instructor-support
package for one lab in a single pass.

```text
You are working in the 10-152-119 Algorithmic Problem Solving course folder.

Task:
Create the complete lab support package for [LAB NUMBER AND TITLE].

Before writing files:
- apply the Clarifying-Question Gate above
- state any assumptions you are making
- ask questions if any required choice is ambiguous
- do not continue into file creation until those ambiguities are resolved or the
  instructor explicitly accepts the assumptions

Read:
- Assignments/LASO-AL_Lab_Assignment_System_Overview.md
- Assignments/Lab_Progression_Ladder_v2.md
- Assignments/[LAB FILE NAME].md
- Assignments/Student_Facing/[LAB FILE NAME].md, if it exists
- Lecture_Outlines/LOT-AL_Alignment-Based_Lecture_Outline_Template.md
- v2/IIM_Matrix_v2.md
- v2/MRS-AL_Master_Rubric_System.md

Create:
- Assignments/Lab_[NN]/demo/demo_notes.md
- Assignments/Lab_[NN]/demo/demo_code.py, if useful
- Assignments/Lab_[NN]/starter/lab_[NN]_starter.py, if useful
- Assignments/Lab_[NN]/success/success_solution.py, if useful
- Assignments/Lab_[NN]/success/success_notes.md
- Assignments/Lab_[NN]/success/optional_colorized_success_solution.py, if
  color helps make the evidence easier to inspect
- Assignments/Lab_[NN]/success/optional_colorized_notes.md, if an optional
  colorized version is created

Package requirements:
- assume the target package folder does not exist unless told otherwise
- do not search for existing lab packages to imitate; use the listed source
  artifacts and the lab-specific context block
- demo and lab must be related but not identical
- starter files must not include the solution
- successful version must remain in the success folder
- use beginner-readable Python
- produce visible evidence
- keep scope appropriate for the week
- preserve AI-use rules
- starter materials must preserve student reasoning: use instructions,
  placeholders, TODO comments, and optional brief pseudocode instead of a
  completed harness when the harness would do the evidence-construction work
  for students
- keep the primary success version plain; optional colorized success versions
  may be included as a refinement layer only after the plain solution is
  correct, observable, and explainable
- colorization should reinforce meaningful distinctions such as pass/fail,
  edge cases, growth warnings, traversal order, comparison winners, or summary
  recommendations
- fixed-width table output should stay readable with and without color enabled
- optional colorized success versions should support the MVP development
  progression: Correct -> Observable -> Explainable -> Usable -> Refined

After editing, provide a short file inventory and note any human review points.
```

---

# Lab-Specific Prompt Context Blocks

Use one of these blocks with any of the prompts above.

## Lab 1 - Precision and Correctness

```text
Lab file:
Assignments/Lab_01_Precision_and_Correctness.md

Core goal:
Students convert a small decision process into precise algorithmic steps,
identify inputs/outputs/assumptions, test edge cases, and revise ambiguity.

Demo/lab relationship:
Demo should use a campus-preparation decision such as deciding whether a
student should pack a laptop charger before leaving for campus. Lab should use
a different decision scenario such as cafeteria recommendation, help desk
priority, parking fee, or registration eligibility.

Required demo scaffold:
Show that the same algorithm can be represented as:
- precise plain English
- pseudocode
- Python-style conditional logic

Use the demo to directly counter the beginner misconception that an algorithm
must look like formal mathematical notation to be valid. The teaching point is
that an algorithm is clear, repeatable, testable, explainable, and
implementable.

Evidence:
Before/after instruction comparison and input/output test table.

AI level:
Manual First -> AI-Assisted.
```

## Lab 2 - Growth and Big-O Intuition

```text
Lab file:
Assignments/Lab_02_Growth_and_Big_O_Intuition.md

Core goal:
Students compare two approaches as input size grows and explain observed timing
evidence using introductory Big-O vocabulary.

Demo/lab relationship:
Demo may compare list lookup vs set lookup. Lab should compare a different pair
such as nested duplicate counting vs dictionary counting, repeated sorting vs a
single pass, or nested pair search vs set-based lookup.

Evidence:
Timing table plus chart or formatted comparison table.

AI level:
Manual First -> AI-Assisted.
```

## Lab 3 - Data Structure Choice

```text
Lab file:
Assignments/Lab_03_Data_Structure_Choice.md

Core goal:
Students solve the same small problem with two data structures and explain
which representation better fits the access pattern.

Demo/lab relationship:
Demo may use attendance tracking with list vs dictionary. Lab should use a
different data-management scenario such as inventory lookup, score summary,
ticket status, menu search, contacts, or registration.

Evidence:
Operation comparison table and optional representation diagram.

AI level:
Manual First -> AI-Assisted.
```

## Lab 4 - Search and Sort Behavior

```text
Lab file:
Assignments/Lab_04_Search_and_Sort_Behavior.md

Core goal:
Students implement or simulate linear search and binary search, then explain
the sorted-data precondition and produce trace evidence.

Demo/lab relationship:
Demo may use book titles on a shelf. Lab should use a different data set such
as product IDs, usernames, ticket numbers, course codes, or attendee names.

Evidence:
Search trace table and sorted/unsorted comparison.

AI level:
Manual First -> AI-Assisted -> selective AI-Injected.
```

## Lab 5 - Strategy Comparison

```text
Lab file:
Assignments/Lab_05_Strategy_Comparison.md

Core goal:
Students solve or simulate one problem using two strategies and compare
correctness, readability, and growth.

Demo/lab relationship:
Demo may compare iterative and recursive handling of nested donation envelopes.
Lab should use a different small problem such as cumulative product, grouped
sum, decision tree, coin selection, scheduling, or shopping tradeoff.

Evidence:
Recursive call trace, decision tree, or strategy comparison table.

AI level:
AI-Assisted -> selective AI-Injected.
```

## Lab 6 - Graph Traversal and Modeling

```text
Lab file:
Assignments/Lab_06_Graph_Traversal_and_Modeling.md

Core goal:
Students model a small real or realistic system as a graph, represent it with
an adjacency list, and produce BFS or DFS traversal evidence.

Demo/lab relationship:
Demo may use a campus route map. Lab should use a different model such as a
workflow, escalation path, transit route, game map, prerequisites, social
network, or grid.

Evidence:
Graph diagram, adjacency list, and traversal table.

AI level:
AI-Assisted.
```

## Lab 7 - Similarity, Ranking, and Hashing

```text
Lab file:
Assignments/Lab_07_Similarity_Ranking_and_Hashing.md

Core goal:
Students make one introductory AI/data concept visible using similarity,
ranking, clustering, recommendation, or hashing, then explain assumptions and
limits.

Demo/lab relationship:
Demo may use tiny music recommendations from tags. Lab should use a different
data set or choose another approved option.

Evidence:
Similarity matrix, ranking table, cluster table, scatter plot, hash comparison,
or representation table.

AI level:
AI-Assisted -> selective AI-Injected.
```

## Week 8 - Final Synthesis Demo and Practice

```text
Lab file:
Assignments/Week_08_Final_Synthesis_Demo_and_Practice.md

Core goal:
Students complete a lecture-demo and formative practice activity that prepares
them for the two-part final assessment.

Demo/lab relationship:
Demo may compare support-ticket assignment approaches. Students should use the
practice prompts to rehearse explanation, evidence, assumptions, and AI
accountability. This is not a new full lab assignment.

Evidence:
Formative comparison table, explanation practice, assumptions, limitations, and
AI-use accountability.

AI level:
AI-Assisted -> AI-Injected; AI-Integrated optional only if explicitly framed.
```

---

# Review Checklist for Generated Materials

Use this checklist after Codex creates final lab or demo materials.

- The demo and lab are related but not identical.
- The student-facing lab does not include the answer.
- The successful version is separated from student starter materials.
- The primary successful version is plain and focused on required behavior.
- Any optional colorized success version preserves the same logic and changes
  only readability/presentation.
- The AI boundary is preserved.
- The visible evidence requirement is concrete.
- The Python is beginner-readable.
- The scope fits one compressed course week.
- The final files align with the MRS categories named in the lab.
- The activity supports algorithmic reasoning, not only code completion.
