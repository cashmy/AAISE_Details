# Slide Deck Source - Week 5 Day 2

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 5 / Tuesday  
**Date:** September 15, 2026  
**Weekly Theme:** Files, Errors, and Data Persistence  
**Lecture Title:** Structured Data and Basic Error Handling  
**Assignments Supported:** A8 - Save and Load Utility; A9 - Structured Data Reader  
**Readiness Target:** Students can save/load simple structured data and explain at least one likely error path.  
**Primary Watch Point:** Students must distinguish file-not-found problems from bad-data problems.

---

# Session Purpose

This session moves from plain text persistence into structured data.

Students should see that CSV and JSON are not just "file types." They are shapes
for information. Once the shape is understood, a program can select useful
values instead of merely printing raw content.

The session also introduces basic error handling as a normal part of responsible
file work.

---

# Review / Prior Work Bridge

Review from Day 1:

- writing saves information outside the running program
- reading loads saved information back
- the file is a visible part of the system

Bridge question:

> What changes when the saved information has rows, columns, labels, or nested
> pieces?

Today's answer:

> The program must understand the data shape before it can use the data well.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 5
- Textbook areas: **Exceptions and Context Managers** and **Files and Data Persistence**

Today's focus:

- exceptions
- tracebacks
- handling exceptions
- checking for file and directory existence
- data interchange formats
- working with JSON
- CSV as structured data support

Skim or save for later:

- custom JSON encoding and decoding
- pickle
- shelve
- configuration file systems
- databases

---

# What We Will Use Today

Today we will use:

- CSV as rows and columns
- JSON as labeled structure
- `try`
- `except`
- file-not-found handling
- invalid data handling
- selected-value output

Today we will not use yet:

- full data pipelines
- custom serializers
- databases
- advanced exception class design
- large nested API payloads

---

# Assignments Supported

Assignments supported:

- A8 - Save and Load Utility
- A9 - Structured Data Reader

A8 continues the save/load cycle.

A9 asks students to read structured data and produce useful output, such as:

- filtered list
- selected record
- summary count
- formatted report

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_05_Files_Errors_and_Data_Persistence/03_save_tasks_json.py`
- `Demos/Week_05_Files_Errors_and_Data_Persistence/04_load_tasks_json.py`
- `Demos/Week_05_Files_Errors_and_Data_Persistence/05_read_csv_summary.py`
- `Demos/Week_05_Files_Errors_and_Data_Persistence/06_missing_file_handling.py`
- `Demos/Week_05_Files_Errors_and_Data_Persistence/07_invalid_json_handling.py`

Supporting data:

- `sample_tasks.json`
- `sample_study_sessions.csv`
- `sample_bad_tasks.json`

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Move from plain persistence to structured data |
| Working Set | 4-5 | Name formats and error tools |
| Data Shape | 6-9 | Compare CSV, JSON, raw output, and selected values |
| Error Paths | 10-12 | Separate missing file from invalid data |
| Assignment Bridge | 13-15 | Continue A8 and launch A9 |
| Close | 16 | Define success for structured data work |

---

## Slide 1 - Saved Data Has Shape

**Delivery Category:** Core

**Student-Visible Text:**

Yesterday, we saved and loaded plain text.

Today, we work with saved data that has structure: rows, columns, labels, and
values that a program can select.

**Instructor Notes:**

Use "shape" as the beginner-friendly anchor. Students do not need formal data
modeling language yet.

**Transition Cue:**

Yesterday made files visible. Today asks what happens when the saved information
has structure the program must understand.

**Visual Notes:**

Plain text note beside a small CSV table and JSON object.

---

## Slide 2 - Review: The File Is Part Of The Program's World

**Delivery Category:** Review

**Student-Visible Text:**

When a program reads a file, the file becomes part of the program's world.

If the file is missing, damaged, or shaped differently than expected, the
program needs a reasonable response.

**Instructor Notes:**

This bridges persistence to error handling. The file is no longer a passive
side detail.

**Transition Cue:**

Once the file becomes part of the program's world, the file's shape becomes part
of the program's responsibility.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

- identify the file shape
- read the file
- select useful values
- handle one likely problem
- explain what the program did

That pattern matters more than memorizing every file-format detail.

**Instructor Notes:**

Use this as the day's north star. Students should understand that opening the
file is not enough; the program must use the structure meaningfully.

**Transition Cue:**

Before we get into JSON or CSV, name the small toolset students are expected to
use today.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- CSV rows and columns
- JSON labels and values
- `try` / `except`
- selected-value output
- one clear error path

**Instructor Notes:**

Name the small working set. Students should know this is not a full data
engineering unit.

**Transition Cue:**

Now narrow the field further so advanced storage topics do not crowd the core
learning target.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- databases
- custom JSON encoding
- large data pipelines
- advanced exception design
- configuration systems

Today we read small structured files and respond to likely problems.

**Instructor Notes:**

This is another cognitive-load protection slide.

**Transition Cue:**

With the boundaries set, start with the structure that most closely connects to
Week 3 dictionaries: JSON labels and values.

---

## Slide 6 - JSON Uses Labels

**Delivery Category:** Core

**Student-Visible Text:**

JSON often stores data with labels.

Those labels help the program ask for a specific value instead of treating the
whole file as one block of text.

**Instructor Notes:**

Connect JSON labels to dictionaries from Week 3.

**Transition Cue:**

JSON uses labels. CSV uses position in rows and columns. That is the next shape
students need to recognize.

**Demo Connection:**

Prepares `03_save_tasks_json.py` and `04_load_tasks_json.py`.

---

## Slide 7 - CSV Uses Rows And Columns

**Delivery Category:** Core

**Student-Visible Text:**

CSV data is usually organized like a table.

Each row represents one record, and each column represents one kind of value.

**Instructor Notes:**

Use a small sample. This is also a useful bridge to the HTML/CSS/JS exposure
students may have had with data tables or structured records.

**Transition Cue:**

Whether the structure is JSON or CSV, the important move is the same: do not
stop at loading the file.

**Demo Connection:**

Prepares `05_read_csv_summary.py`.

---

## Slide 8 - Loading Is Not The Finished Result

**Delivery Category:** Core

**Student-Visible Text:**

Reading a file is only the first step.

The program should select, summarize, filter, or format information so the
output becomes useful.

**Instructor Notes:**

This slide prevents "I printed the raw data" from being mistaken for the goal of
A9.

**Transition Cue:**

Now show that idea in code: load structured JSON and choose values that matter.

---

## Slide 9 - Demo 1: Save And Load JSON Tasks

**Delivery Category:** Demo

**Student-Visible Text:**

Watch for the data shape:

- list of tasks
- labels inside each task
- selected values when loaded

**Instructor Notes:**

Relate the JSON shape back to list/dictionary thinking. Do not linger on every
punctuation mark unless students ask.

Use with:
`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\03_save_tasks_json.py`

Then use with:
`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\04_load_tasks_json.py`

**Transition Cue:**

JSON shows labeled structure. Now shift to CSV, where the useful output comes
from rows and columns.

**Demo Connection:**

Primary demo files: `03_save_tasks_json.py`, `04_load_tasks_json.py`

---

## Slide 10 - Demo 2: Read A CSV Summary

**Delivery Category:** Demo

**Student-Visible Text:**

CSV data often supports small reports.

Instead of printing every row, the program can count, total, filter, or display
selected records.

**Instructor Notes:**

Make the useful output explicit. Ask, "What did the program choose from the
file?"

Use with:
`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\05_read_csv_summary.py`

**Transition Cue:**

Once students have seen useful extraction, introduce the next responsibility:
naming what went wrong when file work fails.

**Demo Connection:**

Primary demo file: `05_read_csv_summary.py`

---

## Slide 11 - Not Every Failure Means The Same Thing

**Delivery Category:** Core

**Student-Visible Text:**

Different problems need different explanations.

- missing file: the program cannot find what it was told to read
- invalid data: the file exists, but the contents do not match expectations

**Instructor Notes:**

This is essential for A8/A9 explanations. Students should name the failure mode
instead of saying only, "It broke."

**Transition Cue:**

Now show both failure types so students can see why the responses should be
different.

---

## Slide 12 - Demo 3: Missing File And Invalid JSON

**Delivery Category:** Demo

**Student-Visible Text:**

Error handling should make the problem understandable.

The goal is not to hide failure. The goal is to respond clearly enough that a
human knows what happened.

**Instructor Notes:**

Run missing-file handling first, then invalid JSON. Ask students to describe how
the two problems differ.

Use with:
`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\06_missing_file_handling.py`

Then use with:
`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\07_invalid_json_handling.py`

**Transition Cue:**

After seeing useful output and failure paths, name the most common weak
submission pattern explicitly.

**Demo Connection:**

Primary demo files: `06_missing_file_handling.py`, `07_invalid_json_handling.py`

---

## Slide 13 - Common Failure: Raw Data Dumping

**Delivery Category:** Core

**Student-Visible Text:**

Raw data is not always useful output.

For A9, show that your program understands the structure by selecting or
summarizing meaningful values.

**Instructor Notes:**

This sets grading expectations without sounding punitive.

**Transition Cue:**

Now convert the warning into the assignment target: read a structure and produce
one useful result.

---

## Slide 14 - Assignment 9 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 9, read a provided CSV or JSON file and produce one useful result.

Good targets include a filtered list, selected record, summary count, or simple
formatted report.

**Instructor Notes:**

Keep the task bounded. A small correct reader beats a large confused data
project.

**Transition Cue:**

Before students begin, make the evidence requirements visible so code and
explanation stay connected.

---

## Slide 15 - Evidence For A8 And A9

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should show:

- code file
- required data file if requested
- readable output
- short explanation of the data shape
- one likely error path if required
- AI-use note if AI materially helped

**Instructor Notes:**

Tie this to GitHub/README habits. The explanation is part of the evidence, not
extra decoration.

**Transition Cue:**

Close by returning to the success pattern in one sentence students can say back.

---

## Slide 16 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> My program read this file shape, selected these useful values, and handled this
> likely problem clearly.

**Instructor Notes:**

This is the verbal readiness target for finishing A8 and starting A9.

**Transition Cue:**

Move into lab time. Students should identify the file shape before writing or
changing code.

---

# Demo Execution Notes

Recommended order:

1. Show the JSON sample file.
2. Run `03_save_tasks_json.py`.
3. Run `04_load_tasks_json.py`.
4. Show the CSV sample.
5. Run `05_read_csv_summary.py`.
6. Run `06_missing_file_handling.py`.
7. Run `07_invalid_json_handling.py`.

If students are overloaded, run only one structured format deeply and use the
other as a comparison.

---

# Lab / Assignment Bridge

A8 should be checked for:

- save behavior
- load behavior
- file evidence
- explanation

A9 should begin with:

- identifying the file shape
- choosing one useful output
- naming one likely issue

---

# README / Submission Expectations

For A9, the README should answer:

```text
## What file did my program read?

## What shape does the data use?

## What useful output did my program produce?

## What problem did I handle or check for?

## AI-use note, if used
```

---

# AI-Use Boundary

Manual first:

- inspect the file yourself
- identify labels, columns, or records
- decide what output is useful

AI may help later with:

- explaining CSV or JSON structure
- comparing parsing approaches
- improving an error message

AI must not replace the student's ability to explain how the program accessed
the data.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Data shapes | Plain note, CSV table, JSON object side by side | Keep examples tiny |
| 2 | File as system part | Program, file, and possible problem states connected | Avoid scary error imagery |
| 3 | Today's success pattern | Identify shape, read file, select values, handle problem, explain result | Avoid format overload |
| 4 | Working set | CSV, JSON, try/except, selected output tools | Avoid dense syntax |
| 5 | Saved for later | Parked shelf for databases, serializers, pipelines | Avoid warning tone |
| 6 | JSON labels | Labeled JSON fields connected to displayed values | Avoid dense nesting |
| 7 | CSV rows/columns | Small table with one row and column highlighted | Avoid spreadsheet complexity |
| 8 | Useful output | Raw file content transformed into selected summary | Avoid implying raw dump is enough |
| 9 | JSON task demo | List of labeled task objects becoming selected task output | Keep JSON tiny |
| 10 | CSV summary demo | CSV table producing count or total summary | Avoid chart/dashboard feel |
| 11 | Error types | Two clear paths: missing file vs invalid data | Do not make it scary |
| 12 | Error demo | Missing file and invalid JSON as two understandable messages | Avoid red alert screens |
| 13 | Raw dump failure | Raw data dump contrasted with useful selected output | Avoid shaming tone |
| 14 | A9 bridge | Structured data reader path: file shape to useful result | Keep assignment scope small |
| 15 | Evidence | Checklist with code, data file, README, output | Avoid audit/legal styling |

---

# Instructor Timing Notes

Suggested timing:

- Review and data-shape framing: 10 minutes
- JSON and CSV concepts: 15 minutes
- Demos: 25 minutes
- Error-path discussion: 10 minutes
- Lab bridge: remaining time

If time runs short, prioritize one structured data demo plus one error demo.

---

# Post-Lecture Notes

Use after teaching:

- Did students confuse CSV and JSON shapes?
- Did they print raw data instead of selecting useful values?
- Did error handling feel clear or mechanical?
- Does A9 need a more constrained provided data file?
