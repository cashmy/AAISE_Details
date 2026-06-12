# SLIDE DECK - WEEK 5 DAY 2

* Course: 10-152-117 Python Programming
* Week / Day: Week 5 / Tuesday
* Date: September 15, 2026
* Weekly Theme: Files, Errors, and Data Persistence
* Lecture Title: Structured Data and Basic Error Handling
* Assignments Supported: A8 - Save and Load Utility; A9 - Structured Data Reader
* Readiness Target: students can save/load simple structured data and explain at least one likely error path
* Primary Watch Point: assignment success assumes students can distinguish file-not-found from bad-data problems

---

### SLIDE 1 - OPENING FRAME

Saved data
has shape.

---
Cue:
- Frame today as a move from plain stored text into structured information.
- Keep the word “shape” central because it is beginner-friendly.

Visual:
- Layout: Compare
- Content:
  - plain text sample
  - CSV sample
  - JSON sample
- Purpose:
  - show that stored data can be organized in recognizable forms

### SLIDE 2 - COURSE POSITIONING

Yesterday: persistence.
Today: structure and failure paths.

---
Cue:
- Connect Tuesday directly to Monday’s save/load work.
- Show that responsible persistence includes understanding data shape and likely errors.

Visual:
- Layout: Flow
- Content:
  - save/load
  - structured format
  - error handling
- Purpose:
  - position error handling as part of mature file work

### SLIDE 3 - CORE IDEA

CSV and JSON
organize information differently.

---
Cue:
- Keep the contrast practical.
- Avoid drifting into full format history or deep nesting theory.

Visual:
- Layout: Split contrast
- Content:
  - CSV as rows and columns
  - JSON as labeled structure
- Purpose:
  - help students choose and interpret format by shape

### SLIDE 4 - CORE IDEA

Loading data
is not enough.

---
Cue:
- Push students beyond dumping raw file contents.
- Ask what useful value, field, or summary the program can extract.

Visual:
- Layout: Sequence
- Content:
  - load file
  - select value
  - meaningful output
- Purpose:
  - center Assignment 9 on interpretation, not just access

### SLIDE 5 - DEMO ANCHOR

Watch the structure.
Then watch the selection.

---
Cue:
- Use before the JSON, CSV, and reader demos.
- Point student attention to chosen fields and summaries.

Visual:
- Layout: Annotated example
- Content:
  - structured file on one side
  - selected value or summary on the other
- Purpose:
  - focus the demo on useful extraction

### SLIDE 6 - SYSTEM

Not every failure
means the same thing.

---
Cue:
- Introduce the distinction between missing file and bad data as the key system idea.
- Keep the language plain and concrete.

Visual:
- Layout: Two-path flow
- Content:
  - file missing path
  - invalid data path
- Purpose:
  - show that different errors need different explanations

### SLIDE 7 - COMMON FAILURE

“It failed”
is not enough.

---
Cue:
- Push students to name the failure mode specifically.
- Reinforce that one likely error path must be explainable.

Visual:
- Layout: Contrast
- Content:
  - vague failure statement
  - specific cause statement
- Purpose:
  - improve clarity and accuracy in debugging and explanation

### SLIDE 8 - BRIDGE

Read the shape.
Handle one likely problem.

---
Cue:
- Bridge directly to Assignments 8 and 9.
- Keep the target bounded: one useful extraction plus one believable failure case.

Visual:
- Layout: Two-part panel
- Content:
  - structured data reader
  - simple `try/except` response
- Purpose:
  - connect the lecture content to the assignment deliverable

### SLIDE 9 - CLOSING

If you can read the structure
and name the failure,
you understand the file.

---
Cue:
- End on understanding rather than syntax volume.
- Reinforce that responsible file work includes both extraction and explanation.

Visual:
- Layout: Isolated focus
- Content:
  - structured sample
  - selected field
  - named error path
- Purpose:
  - close around the readiness target
