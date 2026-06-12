# SLIDE DECK - WEEK 5 DAY 1

* Course: 10-152-117 Python Programming
* Week / Day: Week 5 / Monday
* Date: September 14, 2026
* Weekly Theme: Files, Errors, and Data Persistence
* Lecture Title: Programs That Remember
* Assignments Supported: A8 - Save and Load Utility
* Readiness Target: students can explain what a program writes, where it goes, and how it is loaded back
* Primary Watch Point: avoid jumping to JSON too early if plain file mental model is not clear first

---

### SLIDE 1 - OPENING FRAME

Programs can remember
after they close.

---
Cue:
- Frame this as a meaningful jump in usefulness.
- Keep the concept concrete: memory beyond one run.

Visual:
- Layout: Before / After
- Content:
  - program run ends
  - saved file remains
- Purpose:
  - make persistence feel visible and practical

### SLIDE 2 - COURSE POSITIONING

Before: temporary values.
Now: stored information.

---
Cue:
- Connect file work to variables and collections students already know.
- Emphasize that persistence extends prior knowledge rather than replacing it.

Visual:
- Layout: Flow
- Content:
  - variable in program
  - arrow to file
  - arrow back into program
- Purpose:
  - show the save/load cycle as one connected system

### SLIDE 3 - CORE IDEA

Writing stores data
outside the running program.

---
Cue:
- Keep the wording physical and visible.
- Point out the actual file location when possible.

Visual:
- Layout: Flow
- Content:
  - program box
  - arrow to named file
  - stored text lines
- Purpose:
  - give students a clear mental model of where data goes

### SLIDE 4 - CORE IDEA

Reading brings
saved data back.

---
Cue:
- Pair this tightly with writing.
- Repeat that save and load are one workflow, not two unrelated tricks.

Visual:
- Layout: Reverse flow
- Content:
  - saved file
  - arrow into program
  - displayed content
- Purpose:
  - reinforce retrieval as part of persistence

### SLIDE 5 - DEMO ANCHOR

Watch the file appear.
Then watch it return.

---
Cue:
- Use before the write/read demos.
- Direct attention to the full cycle, not just syntax.

Visual:
- Layout: Sequence
- Content:
  - create file
  - open file content
  - load and display
- Purpose:
  - focus the demo on persistence as a useful loop

### SLIDE 6 - THINKING TOOL

What is saved?
Where is it now?

---
Cue:
- Use these questions repeatedly during examples.
- This helps prevent file work from feeling abstract.

Visual:
- Layout: Two-question panel
- Content:
  - saved content prompt
  - file location prompt
- Purpose:
  - anchor student reasoning in a concrete mental model

### SLIDE 7 - COMMON FAILURE

File syntax can hide
the real idea.

---
Cue:
- Remind students that the concept matters more than the exact line form today.
- Keep plain text central before moving to structured formats.

Visual:
- Layout: Contrast
- Content:
  - code syntax on one side
  - save/load purpose on the other
- Purpose:
  - prevent mechanics from overshadowing persistence

### SLIDE 8 - BRIDGE

Save one thing.
Load it back clearly.

---
Cue:
- Bridge directly to Assignment 8.
- Keep the target small, useful, and explainable.

Visual:
- Layout: Simple workflow
- Content:
  - enter note or task
  - save file
  - reload and display
- Purpose:
  - connect the lecture to a bounded utility task

### SLIDE 9 - CLOSING

If the program can save it
and recover it,
it can remember.

---
Cue:
- End with persistence as the success definition.
- Reinforce usefulness rather than technical vocabulary.

Visual:
- Layout: Isolated focus
- Content:
  - save/load loop
  - remembered value highlighted
- Purpose:
  - close around the day’s readiness target
