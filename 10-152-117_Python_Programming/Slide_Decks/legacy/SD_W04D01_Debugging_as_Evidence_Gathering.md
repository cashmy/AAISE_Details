# SLIDE DECK - WEEK 4 DAY 1

* Course: 10-152-117 Python Programming
* Week / Day: Week 4 / Monday
* Date: September 7, 2026
* Weekly Theme: Debugging, Testing, and Reading Structured Code
* Lecture Title: Debugging as Evidence Gathering
* Assignments Supported: A6 - Debug and Explain
* Readiness Target: students can identify bug source evidence rather than only symptoms
* Primary Watch Point: print-debugging must be taught as intentional evidence, not random `print("here")` behavior

---

### SLIDE 1 - OPENING FRAME

A bug is information.
Not a verdict.

---
Cue:
- Use this to reset student anxiety right away.
- Frame debugging as a normal engineering activity rather than failure.

Visual:
- Layout: Isolated focus
- Content:
  - one bug icon or error symbol
  - one signal / information icon
- Purpose:
  - shift mindset from panic to investigation

### SLIDE 2 - COURSE POSITIONING

Before: build the code.
Now: inspect the behavior.

---
Cue:
- Connect debugging to ownership of the programs students already know how to build.
- Emphasize that reading evidence is the new skill layer.

Visual:
- Layout: Flow
- Content:
  - write code
  - run code
  - inspect result
- Purpose:
  - show debugging as the next stage of code ownership

### SLIDE 3 - CORE IDEA

Symptoms show up.
Sources hide.

---
Cue:
- Teach the difference between what is visible and where the problem started.
- Ask students which part is easy to see and which part takes work.

Visual:
- Layout: Contrast
- Content:
  - wrong output on one side
  - earlier code location on the other
- Purpose:
  - install the source-vs-symptom distinction

### SLIDE 4 - CORE IDEA

Expected
versus actual.

---
Cue:
- Treat this as the day’s core debugging tool.
- Ask students to say both parts out loud before touching the code.

Visual:
- Layout: Split
- Content:
  - expected behavior box
  - actual behavior box
- Purpose:
  - make comparison the center of diagnosis

### SLIDE 5 - DEMO ANCHOR

Watch where the value
first goes wrong.

---
Cue:
- Use before the print-debugging demos.
- Direct attention to the first meaningful drift, not every line of output.

Visual:
- Layout: Traced flow
- Content:
  - input value
  - several checkpoints
  - first incorrect value highlighted
- Purpose:
  - focus the demo on evidence gathering, not noise

### SLIDE 6 - THINKING TOOL

Ask one question.
Print one clue.

---
Cue:
- Turn print-debugging into a disciplined act.
- Reinforce that every print statement should answer something specific.

Visual:
- Layout: Two-step flow
- Content:
  - question about value or path
  - labeled debug print
- Purpose:
  - prevent random print spam and encourage intentional debugging

### SLIDE 7 - COMMON FAILURE

Changing code first
destroys evidence.

---
Cue:
- Be direct here.
- Explain that random edits can erase the trail students need.

Visual:
- Layout: Contrast
- Content:
  - left: inspect first
  - right: edit first and lose clarity
- Purpose:
  - discourage trial-and-error patching without diagnosis

### SLIDE 8 - BRIDGE

Gather evidence.
Then justify the fix.

---
Cue:
- Bridge directly into Assignment 6.
- Keep the sequence visible: observe, trace, explain, repair.

Visual:
- Layout: Ordered flow
- Content:
  - expected vs actual
  - labeled debug output
  - repair decision
- Purpose:
  - connect the lecture process to the assignment requirement

### SLIDE 9 - CLOSING

If you found
the first real signal,
you are debugging.

---
Cue:
- End with signal-finding as the success marker.
- Reinforce that debugging is evidence, not luck.

Visual:
- Layout: Isolated focus
- Content:
  - one trace path
  - one highlighted first signal
- Purpose:
  - close around the readiness target for the day
