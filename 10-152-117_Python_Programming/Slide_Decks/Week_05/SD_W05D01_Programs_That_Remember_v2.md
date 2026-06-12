# Slide Deck Source - Week 5 Day 1

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 5 / Monday  
**Date:** September 14, 2026  
**Weekly Theme:** Files, Errors, and Data Persistence  
**Lecture Title:** Programs That Remember  
**Assignments Supported:** A8 - Save and Load Utility  
**Readiness Target:** Students can explain what a program writes, where it goes, and how it is loaded back.  
**Primary Watch Point:** Do not jump to JSON before the plain file mental model is clear.

---

# Session Purpose

This session introduces persistence as a practical shift in program usefulness.

Until now, most student programs have produced output and then disappeared when
the program ended. Today, students see that a program can write information to a
file, close, and later read that information back.

The day should remain concrete:

- what was saved
- where it was saved
- how it was loaded
- how the visible output proves the cycle worked

---

# Review / Prior Work Bridge

Review from Week 4:

- Debugging starts with evidence, not guessing.
- Expected output helps us recognize when a program behaves correctly.
- Reading code means following responsibility and flow.

Bridge question:

> If a program prints a task list correctly, what happens to that list after the
> program closes?

Today's answer:

> Unless we save it somewhere, it is gone.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 5
- Textbook areas: **Exceptions and Context Managers** and **Files and Data Persistence**

Today's focus:

- working with files and directories
- opening files
- using a context manager to open a file
- reading from and writing to a file

Skim or save for later:

- binary file handling
- file compression
- custom serialization
- databases
- advanced context manager design

---

# What We Will Use Today

Today we will use:

- file names
- text files
- `open()`
- `with`
- write mode and read mode
- simple save/load thinking

Today we will not use yet:

- JSON as the first file model
- databases
- binary files
- custom encoders
- complex folder structures

---

# Assignments Supported

Primary assignment:

- A8 - Save and Load Utility

Students should leave able to begin a small utility that:

- writes information to a file
- reads information from a file
- shows the loaded information clearly
- explains what was saved and loaded

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_05_Files_Errors_and_Data_Persistence/01_write_text_file.py`
- `Demos/Week_05_Files_Errors_and_Data_Persistence/02_read_text_file.py`

Supporting sample file:

- `Demos/Week_05_Files_Errors_and_Data_Persistence/sample_note.txt`

Optional preview only if time permits:

- `Demos/Week_05_Files_Errors_and_Data_Persistence/03_save_tasks_json.py`

Do not let the optional JSON preview become the main teaching path today.

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Position persistence as the next step after output |
| Working Set | 4-5 | Name what will and will not be used today |
| Core Concept | 6-9 | Explain write/read/context-manager flow |
| Demos | 10-11 | Show file creation and file reading |
| Assignment Bridge | 12-14 | Launch A8 with evidence and README expectations |
| Close | 15 | Define success for the session |

---

## Slide 1 - Programs Can Remember

**Delivery Category:** Core

**Student-Visible Text:**

Until now, most of our programs have only worked while they were running.

Today we add persistence: the program can save information outside itself and
load that information again later.

**Instructor Notes:**

Frame this as a meaningful usefulness upgrade. Students are not learning file
syntax as an isolated trick; they are learning how a program remembers.

**Transition Cue:**

Before we save anything, we need to notice what has been temporary so far.

**Visual Notes:**

Before/after visual: program window closes, but a small file remains.

---

## Slide 2 - Review: Output Is Not Storage

**Delivery Category:** Review

**Student-Visible Text:**

Printing a value shows it, but it does not save it.

If the program ends and the value only lived in a variable, that value is gone.

**Instructor Notes:**

Connect to previous assignments. A printed total, name, score, or task is visible
but not persistent.

**Transition Cue:**

So the new question is: where can the information live after the program closes?

---

## Slide 3 - The Save / Load Cycle

**Delivery Category:** Core

**Student-Visible Text:**

Persistence is a cycle:

- create or collect information
- write it to a file
- close or rerun the program
- read the file back
- display or use the loaded information

**Instructor Notes:**

This is the mental model for the day. Say it more than once. The syntax is
secondary to the cycle.

**Visual Notes:**

Circular flow: Program -> File -> Program.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- a file name
- `open()`
- `with`
- write mode
- read mode
- visible output after loading

**Instructor Notes:**

This slide reduces cognitive load. Students need to know the working set is
small and practical.

**Transition Cue:**

And just as important, here is what we are not trying to master today.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- databases
- binary files
- file compression
- custom JSON encoding
- complex folder and deployment issues

Today's goal is simple: save text, load text, explain the cycle.

**Instructor Notes:**

Use this to protect students from textbook breadth. The book is valuable, but
the class target is intentionally narrower.

---

## Slide 6 - Writing Stores Data Outside The Program

**Delivery Category:** Core

**Student-Visible Text:**

Writing means the program places data into a file.

The file becomes the evidence that the program saved something outside the
running program.

**Instructor Notes:**

When demoing, physically show the file in the folder if possible. Make the file
real, not abstract.

**Demo Connection:**

Prepares `01_write_text_file.py`.

---

## Slide 7 - Reading Brings Saved Data Back

**Delivery Category:** Core

**Student-Visible Text:**

Reading means the program opens an existing file and brings its contents back
into the program.

The program can then print, process, or reuse that loaded information.

**Instructor Notes:**

Pair reading and writing tightly. Students often treat them as unrelated syntax
until the save/load loop is repeated clearly.

**Demo Connection:**

Prepares `02_read_text_file.py`.

---

## Slide 8 - Why `with` Matters

**Delivery Category:** Core

**Student-Visible Text:**

`with open(...) as file:` creates a safe working block for the file.

When the block ends, Python handles the file cleanup for us.

**Instructor Notes:**

Avoid overexplaining context managers. Use a practical definition: it opens the
file for the block and closes it afterward.

**Transition Cue:**

Now we can look at the code shape without letting the syntax hide the purpose.

---

## Slide 9 - File Modes Are Intent Signals

**Delivery Category:** Core

**Student-Visible Text:**

The file mode tells Python what we intend to do.

- `"w"` means write
- `"r"` means read

Wrong mode, wrong behavior.

**Instructor Notes:**

Keep this beginner-level. Mention that write mode can replace a file, but do not
turn this into a full file-mode survey.

---

## Slide 10 - Demo 1: Write A Text File

**Delivery Category:** Demo

**Student-Visible Text:**

Watch for three things:

- the file name
- the text being written
- the file appearing or changing on disk

**Instructor Notes:**

Type or paste the smallest useful version first. After running it, open the file
so students can see the saved result.

**Demo Connection:**

Primary demo file: `01_write_text_file.py`

---

## Slide 11 - Demo 2: Read A Text File

**Delivery Category:** Demo

**Student-Visible Text:**

Now the program reads saved text back in.

The proof is not just that the code runs. The proof is that saved information
returns as visible output.

**Instructor Notes:**

Ask students to identify what came from the file rather than from a variable
typed into the program.

**Demo Connection:**

Primary demo file: `02_read_text_file.py`

---

## Slide 12 - Common Failure: The File Is Invisible In Your Thinking

**Delivery Category:** Core

**Student-Visible Text:**

A common beginner mistake is treating the file like magic.

Instead, keep asking:

- What did I save?
- What file did it go into?
- What did I load back?

**Instructor Notes:**

This is the day one file-I/O thinking tool. It will matter again for JSON, CSV,
and APIs.

---

## Slide 13 - Assignment 8 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 8, build a small save/load utility.

Possible options include a note keeper, task list, saved preference, tracker, or
stored score.

**Instructor Notes:**

Make the assignment feel small. The win is a clear save/load cycle, not a large
application.

**Lab Connection:**

Supports A8 - Save and Load Utility.

---

## Slide 14 - Evidence For A8

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should make the save/load behavior visible:

- Python file
- sample saved file if requested
- short README explanation
- one note about what is saved and loaded
- AI-use note if AI materially helped

**Instructor Notes:**

Keep README expectations small but real. This prepares later course
documentation habits without overloading the first file assignment.

---

## Slide 15 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> My program saved this information in this file, then loaded it back and showed
> it clearly.

**Instructor Notes:**

This is the verbal check for the day. If students can explain this, they are
ready to start A8.

---

# Demo Execution Notes

Recommended order:

1. Show the folder before running the write demo.
2. Run `01_write_text_file.py`.
3. Open the created or modified text file.
4. Run `02_read_text_file.py`.
5. Ask students to identify which output came from the file.

Optional, only if students are comfortable:

6. Briefly show `03_save_tasks_json.py` as "where this goes next," not as a
   requirement for today.

---

# Lab / Assignment Bridge

Students should begin A8 by choosing or confirming a small utility idea.

Good starting choices:

- one saved note
- two or three saved tasks
- one saved preference
- a simple saved progress message

Students should avoid:

- full menu systems unless they are already comfortable
- multi-file applications
- databases
- complex user accounts

---

# README / Submission Expectations

For A8, the README can be short:

```text
# Save and Load Utility

## What the program saves

## Where it saves the data

## How to run the program

## What I checked

## AI-use note, if used
```

---

# AI-Use Boundary

Manual first:

- write or trace the save/load cycle yourself
- identify what file is involved
- run the program and inspect the result

AI may help later with:

- explaining file mode differences
- comparing two save/load patterns
- improving error messages

AI must not replace the student's explanation of what was saved and loaded.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Persistence concept | Program closes while a saved file remains visible | Avoid cloud/database imagery |
| 3 | Save/load cycle | Circular flow: program writes file, file feeds program | Keep labels large |
| 4 | Working set | Simple tool tray with file name, open, with, read/write | Avoid dense code |
| 10 | Write demo | Code block pointing to a newly created text file | Do not imply hidden automation |
| 14 | Evidence | Small checklist with code, data file, README, explanation | Avoid legal/compliance feel |

---

# Instructor Timing Notes

Suggested timing:

- Review and opening: 8 minutes
- Core file model: 15 minutes
- Demos: 20 minutes
- Assignment bridge: 10 minutes
- Lab start / questions: remaining time

If time runs short, skip the JSON preview. Protect the plain text save/load
mental model.

---

# Post-Lecture Notes

Use after teaching:

- Did students understand where the file was created?
- Did file path confusion consume more time than expected?
- Was A8 too broad or appropriately bounded?
- Should JSON be introduced earlier or held until Day 2?
