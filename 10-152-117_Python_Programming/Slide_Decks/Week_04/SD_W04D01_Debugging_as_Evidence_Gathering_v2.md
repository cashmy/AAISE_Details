# SLIDE DECK SOURCE - WEEK 4 DAY 1

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 4 / Monday |
| Date | September 7, 2026 |
| Weekly Theme | Debugging, Testing, and Reading Structured Code |
| Lecture Title | Debugging as Evidence Gathering |
| Assignments Supported | Assignment 6 - Debug and Explain |
| Readiness Target | Students can identify bug source evidence rather than only symptoms |
| Primary Watch Point | Print-debugging must be taught as intentional evidence, not random `print("here")` behavior |
| Source Version | v2 refactor |

---

# Session Purpose

This session reframes debugging as an evidence-gathering process.

Students should understand that bugs are not proof of failure. A bug is
information. The developer's job is to slow down, compare expected behavior to
actual behavior, find the first useful signal, and justify the fix.

The target pattern is:

```text
observe -> compare expected and actual -> trace evidence -> make one justified fix
```

---

# Review / Prior Work Bridge

Review from Week 3:

- functions organize logic into named responsibilities
- lists and dictionaries organize related data
- cleaner structure makes code easier to explain
- A4 and A5 required students to justify organization choices

Quick review questions:

- What was your code supposed to do?
- What output did you expect?
- Where would you look first if the output was wrong?
- What evidence would help you avoid guessing?

Bridge into Week 4:

This week, students move from writing and organizing code to inspecting,
repairing, validating, and explaining code.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 4
- textbook chapter areas: **Testing**, **Debugging and Profiling**, and **OOP,
  Decorators, and Iterators** for recognition later in the week

Day 1 reading focus:

- debugging techniques
- troubleshooting guidelines

Use this reading to support:

- syntax versus logic bugs
- expected versus actual behavior
- print-debugging as evidence
- fixing a bug and explaining the fix

Today's reading boundary:

Students should not worry yet about profiling tools, full pytest mastery,
formal test-driven development, or deep debugging-tool ecosystems.

---

# What We Will Use Today

Today we will use:

- expected versus actual comparison
- traceback reading at a beginner level
- syntax bug recognition
- logic bug recognition
- labeled print-debugging
- one-change-at-a-time repair
- debugging notes as evidence

Today we will skip for now and revisit later:

- full debugger workflow
- logging architecture
- pytest syntax mastery
- profiling
- AI-first debugging

---

# Assignments Supported

Primary support:

- Assignment 6 - Debug and Explain

A6 asks students to repair broken code and explain the debugging process.

Minimum assignment direction:

- identify at least two issues unless otherwise directed
- repair the code
- use simple checks or expected-vs-actual examples
- include debugging evidence
- explain what changed and why the fix works

---

# Readiness Target

By the end of the session, students should be able to:

- separate symptom from source
- describe expected behavior
- describe actual behavior
- use one labeled print statement to answer one debugging question
- identify one useful traceback or output clue
- make one justified fix
- explain why the fix is supported by evidence

---

# Primary Watch Point

The main risk is random repair.

Students may want to change code immediately because changing code feels like
progress. The instructor should keep the sequence visible:

```text
observe first -> form one hypothesis -> inspect one clue -> change one thing
```

Print-debugging should answer a specific question. It should not become noisy
console clutter.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/01_broken_syntax_example.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/02_logic_bug_expected_actual.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/03_logic_bug_fixed.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/09_print_debugging_grade_summary.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/10_print_debugging_order_total.py`

Instructor framing:

- `Demos/Instructor_Notes-Debugging_Process.md`

Recommended use:

1. Use Demo 1 for syntax-error recognition.
2. Use Demo 2 and Demo 3 for expected versus actual and justified repair.
3. Use Demo 9 or Demo 10 for disciplined print-debugging.

---

# Student Hands-On Bridge

Students should begin A6 by documenting the bug before changing code.

Suggested start:

```text
1. Run the broken code.
2. Record expected behavior.
3. Record actual behavior.
4. Identify one useful clue.
5. Add one labeled print or check.
6. Make one justified fix.
7. Run again and record evidence.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Reframe bugs as evidence, not failure |
| Today's Working Set | 4-5 | Core | Bound debugging tools and defer advanced testing/profiling |
| Expected vs Actual | 6-8 | Core / Demo | Teach symptom/source and comparison-based diagnosis |
| Print-Debugging | 9-12 | Core / Demo | Teach labeled evidence, signal, and one-question prints |
| Common Failures | 13-14 | Core | Prevent random edits and print spam |
| Assignment 6 Bridge | 15-17 | Lab Bridge / Evidence | Start A6 with notes, checks, and repair justification |
| Closing Check | 18 | Assessment / Evidence | Define successful debugging evidence |

---

# Slide-by-Slide Source

## Slide 1 - A Bug Is Information

**Delivery Category:** Review

**Student-Visible Text:**

A bug is information, not a verdict.

When code breaks or gives the wrong answer, the program is giving you clues.

Today, practice debugging by asking:

- What did I expect?
- What actually happened?
- Where is the first useful clue?
- What fix does the evidence justify?

**Instructor Notes:**

Use this to reset student anxiety. Debugging often feels personal to beginners.
Frame it as investigation and professional practice.

**Transition Cue:**

Before fixing the code, inspect what the program is telling you.

**Visual Notes:**

Use a bug/error symbol turning into a signal or evidence marker.

---

## Slide 2 - Build Becomes Inspect

**Delivery Category:** Review

**Student-Visible Text:**

In earlier weeks, you built small programs.

Now you inspect behavior when a program does not do what it should.

Debugging uses familiar skills:

- reading code
- running code
- tracing values
- explaining output

**Instructor Notes:**

Connect debugging to ownership of programs students already know how to build.

**Transition Cue:**

The first distinction is symptom versus source.

---

## Slide 3 - Symptoms Show Up, Sources Hide

**Delivery Category:** Core

**Student-Visible Text:**

A symptom is what you notice first.

The source is where the problem actually begins.

Examples:

- symptom: wrong final total
- source: tax calculated from the wrong value
- symptom: program will not run
- source: missing quote, colon, or parenthesis

**Instructor Notes:**

Students often fix the visible symptom instead of locating the source. Use this
language throughout the demos.

**Transition Cue:**

Expected versus actual helps separate symptom from source.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- expected versus actual
- tracebacks
- labeled print-debugging
- one-change-at-a-time repair
- simple evidence notes

These tools help you investigate before changing code.

**Instructor Notes:**

Keep the tooling beginner-sized. This is not a full debugger or testing-tool
survey.

**Transition Cue:**

Some debugging tools are useful later, but not today's required target.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip full debugger workflows, logging architecture, pytest mastery, and
profiling for now.

Today's required target is smaller:

- find useful evidence
- make a justified fix
- explain why the fix works

**Instructor Notes:**

This prevents pytest/profiling/tooling from becoming accidental hidden
requirements for A6.

**Transition Cue:**

Start with the simplest question: what should have happened?

---

## Slide 6 - Expected Versus Actual

**Delivery Category:** Core

**Student-Visible Text:**

Expected behavior is what should happen.

Actual behavior is what happened when the program ran.

Debugging begins when you compare:

- expected output
- actual output
- the difference between them

**Instructor Notes:**

Require expected-vs-actual language before students propose a fix. This slows
random repair.

**Transition Cue:**

Some bugs stop the program before output appears.

---

## Slide 7 - Demo 1: Syntax Error Signal

**Delivery Category:** Demo

**Student-Visible Text:**

A syntax error prevents Python from running the program.

Read the message for:

- file name
- line number
- error type
- the nearby code Python could not understand

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/01_broken_syntax_example.py`

The file contains the corrected version. To demo a syntax error, remove the
closing quote from the message line while presenting.

**Transition Cue:**

Other bugs let the code run, but the answer is wrong.

**Demo Connection:**

Primary demo file: `01_broken_syntax_example.py`

---

## Slide 8 - Demo 2: Logic Bug Expected vs Actual

**Delivery Category:** Demo

**Student-Visible Text:**

A logic bug can run without crashing and still produce the wrong result.

Trace:

- expected value
- actual value
- suspicious calculation
- corrected calculation
- evidence that the fix worked

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/02_logic_bug_expected_actual.py`

Then compare with:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/03_logic_bug_fixed.py`

Do not reveal the fix too fast. Ask what evidence points to the bad operation.

**Transition Cue:**

When the source is not obvious, print-debugging can reveal the signal.

**Demo Connection:**

Primary demo files: `02_logic_bug_expected_actual.py`, `03_logic_bug_fixed.py`

---

## Slide 9 - Ask One Question, Print One Clue

**Delivery Category:** Core

**Student-Visible Text:**

Print-debugging should answer a specific question.

Weak:

```python
print("here")
```

Better:

```python
print("subtotal before tax:", subtotal)
```

Every debug print should reveal a value or path you need to inspect.

**Instructor Notes:**

This is the discipline point. Print-debugging is valid, but random print spam
creates noise.

**Transition Cue:**

The next demos show how to look for the first place a value goes wrong.

---

## Slide 10 - Demo 3: Grade Summary Debugging

**Delivery Category:** Demo

**Student-Visible Text:**

Watch where the grade summary first goes wrong.

Trace:

- starting student
- running total
- added score
- calculated average
- first incorrect value

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/09_print_debugging_grade_summary.py`

Add suggested print statements one at a time. Do not turn on every checkpoint
at once unless you are comparing signal versus noise.

**Transition Cue:**

A plausible final number can still hide the wrong step.

**Demo Connection:**

Primary demo file: `09_print_debugging_grade_summary.py`

---

## Slide 11 - Demo 4: Order Total Debugging

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the calculation stages.

Useful checkpoints:

- line total
- subtotal
- discount
- tax
- final total

The bug is not just the wrong final number. The signal is the first wrong step.

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/10_print_debugging_order_total.py`

Focus on finding the first meaningful drift, not just fixing the final formula.

**Transition Cue:**

Debugging evidence should lead to one justified change.

**Demo Connection:**

Primary demo file: `10_print_debugging_order_total.py`

---

## Slide 12 - Evidence Before Repair

**Delivery Category:** Core

**Student-Visible Text:**

Good debugging evidence narrows the problem.

Evidence may be:

- a traceback line
- expected versus actual output
- a labeled debug print
- the first wrong value
- a simple check after the fix

Do not change several things before you know what the evidence says.

**Instructor Notes:**

Tie this directly to the A6 evidence requirement.

**Transition Cue:**

The first common failure is changing code too early.

---

## Slide 13 - Common Failure: Changing Code First

**Delivery Category:** Core

**Student-Visible Text:**

Changing code before observing can destroy the trail.

Instead:

- reproduce the problem
- record what happened
- inspect one clue
- change one thing
- run again

Random repair can make the bug disappear without building understanding.

**Instructor Notes:**

Be direct but not scolding. Students guess because they feel pressure. Give
them a better process.

**Transition Cue:**

The second common failure is too much unlabeled output.

---

## Slide 14 - Common Failure: Print Spam

**Delivery Category:** Core

**Student-Visible Text:**

Too many unlabeled print statements create noise.

Use fewer, better clues:

- label the value
- print near the suspicious line
- remove debug prints after the fix
- keep the evidence you need for the explanation

**Instructor Notes:**

This preserves print-debugging as a professional, intentional tool.

**Transition Cue:**

Now connect the process to Assignment 6.

---

## Slide 15 - Assignment 6 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 6, repair broken code and explain the debugging process.

Your work should show:

- the issue you found
- the evidence that helped
- the fix you made
- the check that proves the fix works

**Instructor Notes:**

Use this as the launch checklist. Students should know the assignment is not
only corrected code; it is diagnosis plus evidence plus explanation.

**Transition Cue:**

Start the notes before the fix.

**Lab Connection:**

Supports Assignment 6 - Debug and Explain.

---

## Slide 16 - Debugging Notes Template

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Use a short note pattern:

- Expected:
- Actual:
- Evidence:
- Fix:
- Check after fix:

This keeps the debugging story clear.

**Instructor Notes:**

This scaffold is especially helpful for students who can fix code but struggle
to explain the reasoning.

**Transition Cue:**

The final evidence should make the fix believable.

---

## Slide 17 - Evidence For A Debugging Submission

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Useful debugging evidence includes:

- corrected `.py` file
- expected-vs-actual comparison
- labeled debug output
- traceback clue
- simple check or test case
- explanation of why the fix works

The evidence should support the repair, not just decorate the submission.

**Instructor Notes:**

Keep pytest optional unless explicitly required. A6 can be satisfied with
simple checks and clear evidence.

**Transition Cue:**

Close with signal-finding as the success measure.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you found the first useful signal, you are debugging.

Before submitting A6, ask:

- What was wrong?
- What evidence showed it?
- What did I change?
- How did I check the fix?
- Can I explain the repair without guessing?

**Instructor Notes:**

Close around evidence, not speed. Debugging skill grows when students can
explain their path from symptom to source to fix.

**Transition Cue:**

Next session, we read different code structures without needing to master all
of object-oriented design.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one Week 3 structure explanation.
2. Introduce debugging loop from `Instructor_Notes-Debugging_Process.md`.
3. Demo syntax error recognition with Demo 1.
4. Demo expected-vs-actual logic bug with Demos 2 and 3.
5. Demo intentional print-debugging with Demo 9 or Demo 10.
6. Move students into A6 notes and first diagnosis.

Instructor pacing note:

If students struggle with the first logic bug, skip one print-debugging demo
and preserve lab time.

---

# Lab / Assignment Bridge

By the end of Day 1, students should have started A6 or have a clear debugging
plan.

Minimum A6 start target:

- broken code selected or provided
- expected behavior written
- actual behavior recorded
- one clue identified
- one debugging note started

---

# README / Submission Expectations

Suggested student evidence:

- corrected `.py` file
- debugging notes or short report
- expected-vs-actual example
- at least one piece of debugging evidence
- AI-use note if AI was permitted and used

---

# AI-Use Boundary

Bounded AI debugging assistance may be allowed only after a manual diagnosis
attempt, if the instructor permits it.

Students should record:

- what they tried first
- what evidence they gathered
- what AI suggested
- what they accepted, changed, or rejected
- how they verified the final fix

AI should help clarify evidence. It should not replace the student's debugging
process.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Bug as information | Bug/error signal transformed into evidence clue | Avoid panic imagery |
| 3 | Symptom vs source | Wrong output contrasted with earlier source line | Keep simple |
| 4 | Today's tools | Toolbox with expected/actual, traceback, labeled print, one change | Avoid advanced tools |
| 5 | Deferred tools | Shelf with labeled cards for deferred topics | Avoid warning signs |
| 6 | Expected vs actual | Two cards comparing expected output and actual output | Keep readable |
| 7 | Syntax error signal | Error message with file, line, error type highlighted | Avoid scary red screen |
| 8 | Logic bug comparison | Expected 80, actual 120, suspicious calculation highlighted | Keep numeric example simple |
| 9 | Labeled print | Weak `print("here")` vs labeled value print | Avoid shaming |
| 10 | Grade debug trace | Student records flowing through checkpoints, first wrong average highlighted | Avoid data overload |
| 11 | Order total trace | Subtotal, discount, tax, final total checkpoints | Keep stages visible |
| 13 | Change one thing | Ordered process: observe, inspect, change one thing, run again | Avoid chaotic visuals |
| 16 | Debug notes | Template card with expected, actual, evidence, fix, check | Keep text large |
| 17 | Evidence | Corrected file, debug output, expected/actual, explanation note | Keep documentation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Opening/review | 8 min | Use Slides 1 and 3 only | Ask students to name a recent bug symptom |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Briefly preview advanced tools |
| Expected/actual demos | 18 min | Use logic bug only | Have students write expected/actual |
| Print-debugging demo | 18 min | Use one demo only | Add checkpoints one at a time |
| Common failures | 8 min | Mention verbally | Compare print spam vs labeled print |
| Assignment bridge | 20+ min | Provide notes template only | Confer on evidence quality |
| Closing check | 4 min | Ask final questions verbally | Have students explain one clue |

---

# Post-Lecture Notes

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
