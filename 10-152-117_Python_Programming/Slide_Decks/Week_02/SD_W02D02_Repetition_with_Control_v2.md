# SLIDE DECK SOURCE - WEEK 2 DAY 2

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 2 / Tuesday |
| Date | August 25, 2026 |
| Weekly Theme | Decision Logic and Repetition |
| Lecture Title | Repetition with Control |
| Assignments Supported | Assignment 3 - Loops and Repetition |
| Readiness Target | Students can explain what repeats and what stops repetition |
| Primary Watch Point | If repeated input is shown, make sure students understand state change clearly |
| Source Version | v2 refactor |

---

# Session Purpose

This session introduces loops as controlled repetition.

Students should understand that a loop is not just "doing something many
times." A useful loop has a purpose, a repeated action, and a clear reason to
stop.

The target pattern is:

```text
repeat action -> update or advance -> check stopping point
```

---

# Review / Prior Work Bridge

Review from Week 2 Day 1:

- A condition asks a `True` / `False` question.
- `if`, `elif`, and `else` choose between paths.
- Branch prediction helps students explain decision logic.
- Assignment 2 focuses on one small decision-based program.

Quick review questions:

- What value is being checked?
- What condition is tested?
- Which branch runs?
- What output appears?

Bridge into Day 2:

Today, the program does not only choose once. It repeats an action in a
controlled way.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 2
- textbook chapter area: **Conditionals and Iteration**

Day 2 reading focus:

- looping
- the `for` loop
- iterating over a range
- iterating over a sequence
- the `while` loop

Use this reading to support:

- repeated behavior
- counters
- accumulators
- stopping conditions

Today's reading boundary:

Students should not worry yet about advanced iterator behavior, iterating over
multiple sequences, assignment expressions, `itertools`, or generator tools.

---

# What We Will Use Today

Today we will use:

- `for` loops
- `range()`
- counters
- accumulators
- `while` loops
- stopping conditions
- loop prediction

Today we will skip for now and revisit later:

- nested loops
- advanced iterators
- generator tools
- `break` and `continue` as a main focus
- large menu programs
- AI-generated loop logic

---

# Assignments Supported

Primary support:

- Assignment 3 - Loops and Repetition

Assignment 3 asks students to build one small loop-based program.

Possible options include:

- counting program
- repeated-input collector
- simple menu loop
- number sequence generator
- practice quiz loop
- total accumulator

Today's lecture should make students ready to identify what repeats, what
changes, and what stops the loop.

---

# Readiness Target

By the end of the session, students should be able to:

- identify the repeated action
- identify the value or sequence that changes
- explain when the loop stops
- distinguish a `for` loop from a `while` loop at a beginner level
- recognize why a missing update can cause an infinite loop
- test a loop with small, visible output

---

# Primary Watch Point

The main risk is students seeing loops as magic repetition.

Each loop example should answer three visible questions:

- What repeats?
- What changes or advances?
- What stops the loop?

If students cannot answer those three questions, the loop is too complex for
the moment.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_02_Decision_Logic_and_Repetition/04_for_loop_counting.py`
- `Demos/Week_02_Decision_Logic_and_Repetition/05_for_loop_accumulator.py`
- `Demos/Week_02_Decision_Logic_and_Repetition/06_while_loop_countdown.py`

Optional bridge demo:

- `Demos/Week_02_Decision_Logic_and_Repetition/07_input_loop_with_exit.py`

Recommended use:

1. Use Demo 4 to show predictable fixed repetition.
2. Use Demo 5 to show accumulation as a value that changes over time.
3. Use Demo 6 to show a `while` loop with a visible stopping condition.
4. Use Demo 7 only if students are ready for repeated input.

---

# Student Hands-On Bridge

Students should begin Assignment 3 by choosing one small loop pattern.

Suggested start:

```text
1. Name what repeats.
2. Name what changes each time.
3. Name what stops the loop.
4. Predict the first three outputs.
5. Code the smallest working version.
```

The first version should be intentionally small. Larger behavior can wait until
the loop can be explained.

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect decisions to controlled repetition |
| Today's Working Set | 4-5 | Core | Bound loop topics and defer advanced iteration |
| Loop Mental Model | 6-8 | Core | Teach repeat/change/stop as the loop reading pattern |
| For Loops | 9-10 | Core / Demo | Show fixed repetition and range-based counting |
| Accumulators and Updates | 11-12 | Core / Demo | Show changing state across repetitions |
| While Loops | 13-15 | Core / Demo | Show condition-controlled repetition and infinite-loop risk |
| Assignment 3 Bridge | 16-17 | Lab Bridge / Evidence | Start A3 with loop evidence and explanation |
| Closing Check | 18 | Assessment / Evidence | Define successful loop understanding |

---

# Slide-by-Slide Source

## Slide 1 - Repeat On Purpose

**Delivery Category:** Review

**Student-Visible Text:**

Loops let a program repeat work instead of writing the same code again and
again.

Good repetition is controlled repetition.

Today, watch for:

- what repeats
- what changes
- what stops the loop

**Instructor Notes:**

Make control the theme. Students often hear "loop" and think only "repeat."
The deeper beginner target is knowing why the loop starts, what happens each
time, and why it ends.

**Transition Cue:**

Yesterday the program chose between paths. Today the program can repeat a path.

**Visual Notes:**

Use a repeated action with a visible stop point.

---

## Slide 2 - Logic Chooses, Loops Repeat

**Delivery Category:** Review

**Student-Visible Text:**

Decision logic chooses what happens.

Loop logic repeats something on purpose.

Week 2 now has two control-flow tools:

- branches for choosing
- loops for repeating

**Instructor Notes:**

Connect Tuesday directly to Monday. This helps students see loops as the next
control-flow idea, not an unrelated syntax topic.

**Transition Cue:**

The first question for every loop is simple: what repeats?

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Repeat action -> update or advance -> check stopping point.

If you can explain those three parts, you understand the loop.

For every loop, ask:

- What code repeats?
- What becomes different?
- How does the loop stop?

**Instructor Notes:**

This pattern mirrors the assignment's key learning target. Return to it during
each demo and during student work time.

**Transition Cue:**

Let's define the tools in today's working set.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- `for`
- `range()`
- counters
- accumulators
- `while`
- stopping conditions

These tools let a program repeat work without duplicating the same lines.

**Instructor Notes:**

Keep the working set concrete. Students should leave knowing that `for` often
fits known repetition and `while` often fits condition-controlled repetition.

**Transition Cue:**

Some loop topics are real Python topics, but they are not today's job.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip nested loops, advanced iterators, generator tools, and large menu
programs for now.

Today's job is to understand one loop clearly.

A good beginner loop is small enough to trace:

- first pass
- second pass
- last pass

**Instructor Notes:**

This slide keeps the reading and possible Python breadth from expanding beyond
the assignment. Day 3 can combine loops with conditionals; Day 2 should focus
on loop control.

**Transition Cue:**

Start with the most visible loop question: what repeats?

---

## Slide 6 - Ask What Repeats

**Delivery Category:** Core

**Student-Visible Text:**

The repeated block is the work the loop performs each time.

Before running a loop, identify the repeated action.

Examples:

- print a number
- add to a total
- ask for another value
- count down toward zero

**Instructor Notes:**

Keep attention on the body of the loop. Students may stare at the keyword and
miss the actual repeated behavior.

**Transition Cue:**

The second question is what changes.

---

## Slide 7 - Ask What Changes

**Delivery Category:** Core

**Student-Visible Text:**

A controlled loop usually has something that changes or advances.

That change may be:

- the next number from `range()`
- a counter value
- a running total
- a user choice
- a condition becoming false

**Instructor Notes:**

This prepares students for both `for` and `while`. In a `for` loop, Python
advances through the sequence. In a `while` loop, the program often needs an
explicit update.

**Transition Cue:**

The third question protects us from accidental infinite loops.

---

## Slide 8 - Ask What Stops It

**Delivery Category:** Core

**Student-Visible Text:**

Every useful loop needs a clear stopping point.

The stop may come from:

- reaching the end of a range
- reaching the end of a sequence
- a condition becoming false
- a user choosing to exit

If nothing can stop, the loop may run forever.

**Instructor Notes:**

Introduce infinite-loop risk conceptually here, before showing the `while`
demo. The goal is not fear; it is intentional control.

**Transition Cue:**

The simplest first loop is a `for` loop with a known range.

---

## Slide 9 - `for` Loops: Known Repetition

**Delivery Category:** Core

**Student-Visible Text:**

A `for` loop is useful when the program knows what it is repeating over.

Common beginner pattern:

```python
for number in range(5):
    print(number)
```

The range controls how many times the loop runs.

**Instructor Notes:**

Keep the initial example small. Explain that `range(5)` produces a sequence of
values the loop can step through. Avoid deep iterator vocabulary.

**Transition Cue:**

Let's watch a fixed counting loop run.

---

## Slide 10 - Demo 1: Counting With `for`

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the loop variable change each time the loop runs.

For each pass, identify:

- the current value
- the repeated output
- when the range is finished

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/04_for_loop_counting.py`

Run as written. Then change the range value and ask students how many lines
will print.

**Transition Cue:**

Loops often do more than print. They can build a result over time.

**Demo Connection:**

Primary demo file: `04_for_loop_counting.py`

---

## Slide 11 - Accumulators Build A Result

**Delivery Category:** Core

**Student-Visible Text:**

An accumulator is a variable that collects or builds a value over repeated
steps.

Common pattern:

```python
total = 0
for number in range(1, 4):
    total = total + number
```

The total changes each time the loop runs.

**Instructor Notes:**

This is a major beginner moment. Slow down around `total = total + number`
because students often find it strange at first. It means "calculate a new
total using the old total."

**Transition Cue:**

Let's watch the total change during the loop.

---

## Slide 12 - Demo 2: Accumulator Loop

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the running total.

For each loop pass, explain:

- what number is added
- what the old total was
- what the new total becomes

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/05_for_loop_accumulator.py`

Consider drawing a small table with columns for pass, number, old total, and
new total. This makes the state change visible.

**Transition Cue:**

`for` loops often know their range. `while` loops depend on a condition.

**Demo Connection:**

Primary demo file: `05_for_loop_accumulator.py`

---

## Slide 13 - `while` Loops: Condition-Controlled Repetition

**Delivery Category:** Core

**Student-Visible Text:**

A `while` loop repeats while a condition is `True`.

Basic shape:

```python
while condition:
    repeat_this()
```

The loop stops when the condition becomes `False`.

**Instructor Notes:**

Connect directly back to Monday: a `while` loop uses a condition too, but now
the condition controls repetition instead of a one-time branch.

**Transition Cue:**

The condition only helps if something changes.

---

## Slide 14 - Missing Updates Cause Trouble

**Delivery Category:** Core

**Student-Visible Text:**

If the condition never changes, the loop may never stop.

For a `while` loop, always ask:

- What condition starts the loop?
- What line changes the condition?
- What value makes the loop stop?

**Instructor Notes:**

This is the infinite-loop prevention slide. Keep it calm and practical. The
student goal is not to avoid loops; it is to control them.

**Transition Cue:**

Now watch a `while` loop with an obvious countdown.

---

## Slide 15 - Demo 3: `while` Countdown

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the countdown change.

For each pass, identify:

- the current value
- the output
- the update
- the moment the loop stops

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/06_while_loop_countdown.py`

Pause before the update line. Ask what would happen if that line were missing.
Do not intentionally trap the class in an infinite loop unless you are ready to
show how to interrupt it safely.

**Transition Cue:**

If the class is ready, repeated input is a practical use of a `while` loop.

**Demo Connection:**

Primary demo file: `06_while_loop_countdown.py`

---

## Slide 16 - Optional Demo: Input Loop With Exit

**Delivery Category:** Reserve

**Student-Visible Text:**

Repeated input is useful when the user may enter several values.

The program should still have a clear exit condition.

Watch for:

- the repeated prompt
- the user's choice
- the condition that ends the loop

**Instructor Notes:**

Use only if students are ready:

`Demos/Week_02_Decision_Logic_and_Repetition/07_input_loop_with_exit.py`

This is a bridge toward more practical loop programs, but it can overload
students if `input()` is still unstable. Skip it if needed.

**Transition Cue:**

Now students can start A3 with a bounded loop pattern.

**Demo Connection:**

Optional demo file: `07_input_loop_with_exit.py`

---

## Slide 17 - Assignment 3 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 3, build one small program that repeats in a controlled way.

A good first version should include:

- one repeated action
- one clear stop point
- visible output
- no infinite loop

Before coding too much, write what repeats and what stops it.

**Instructor Notes:**

Point students toward manageable choices: counting program, total accumulator,
number sequence, or simple practice loop. If they choose a menu loop or
repeated-input collector, keep the scope tight.

**Transition Cue:**

The evidence should show repetition and control.

**Lab Connection:**

Supports Assignment 3 - Loops and Repetition.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can explain the loop, you control it.

Before submitting A3, test:

- what happens on the first pass
- what changes after one pass
- how the loop stops
- whether the output proves repetition happened

**Instructor Notes:**

Close around explainable repetition. This prepares students for Thursday, when
conditionals and loops are combined.

**Transition Cue:**

Next session, decisions and loops work together in small programs.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one Day 1 branch prediction example.
2. Run `04_for_loop_counting.py`.
3. Change the `range()` value and predict output count.
4. Run `05_for_loop_accumulator.py`.
5. Trace old total, added value, and new total.
6. Run `06_while_loop_countdown.py`.
7. Identify the update that moves the loop toward stopping.
8. Use `07_input_loop_with_exit.py` only if the class is ready for repeated input.
9. Move students into A3 planning and first implementation.

Instructor pacing note:

Do not force all loop types equally if the class needs more time. A clear `for`
loop and one well-explained `while` loop are better than several shallow
examples.

---

# Lab / Assignment Bridge

By the end of Day 2, students should have started Assignment 3 or have a clear
loop plan.

Minimum A3 start target:

- selected loop problem
- statement of what repeats
- statement of what changes or advances
- statement of what stops the loop
- first small version running or sketched

---

# README / Submission Expectations

Suggested student evidence:

- clear `.py` filename
- code that runs without syntax errors
- visible repeated output
- no infinite loop
- short answer to: "What repeats in your program, and how does your program
  know when to stop?"

If using GitHub, students should keep code and explanation together, but this
assignment should remain focused on loop reasoning.

---

# AI-Use Boundary

AI is not allowed for normal Assignment 3 work unless the instructor explicitly
says otherwise.

Reason:

Students need manual-first practice with:

- identifying repeated behavior
- tracing state changes
- controlling stopping conditions
- recognizing infinite-loop risk
- explaining each loop pass

AI can be used later for explanation or review when permitted, but it should
not replace the first manual encounter with loops.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Controlled repetition | Repeated action with a visible stop point | Avoid endless spiral imagery |
| 2 | Branch vs loop | Split visual: branch chooses, loop repeats | Keep both simple |
| 3 | Loop pattern | Three-step cycle: repeat, update, stop | Do not overcomplicate with nested arrows |
| 4 | Today's tools | Toolbox with `for`, `range()`, counter, accumulator, `while` | Avoid advanced iterator terms |
| 5 | Deferred topics | Parked-for-later topics: nested loops, generators, large menus | Do not make deferred topics look forbidden |
| 6 | Repeated block | Simple code block with repeated action highlighted | Keep code minimal |
| 7 | Changing state | Value changing across loop passes | Make state change obvious |
| 8 | Stop point | Loop cycle with exit door or stop marker | Avoid warning-heavy visuals |
| 10 | For loop demo | Range values stepping through output lines | Keep values readable |
| 12 | Accumulator demo | Table showing old total, added value, new total | Avoid spreadsheet complexity |
| 15 | While countdown | Countdown loop with update and stop condition | Make update line visually central |
| 17 | Assignment bridge | Small loop project options as cards | Avoid making one option required |
| 18 | Evidence | `.py` file with repeated output and short explanation note | Keep documentation lightweight |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students to compare branch vs loop |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss why nested loops wait |
| Loop mental model | 12 min | Use repeat/change/stop only | Have students label a loop snippet |
| For loop demo | 12 min | Run as written only | Change ranges and predict output count |
| Accumulator demo | 15 min | Skip detailed table | Build a pass-by-pass trace table |
| While loop demo | 15 min | Use countdown only | Discuss missing-update risk |
| Optional input loop | 0-8 min | Skip entirely | Bridge to repeated input pattern |
| Assignment bridge | 15+ min | Assign one common option | Confer with students on loop scope |
| Closing check | 4 min | Ask two questions verbally | Have students explain first/last pass |

---

# Post-Lecture Notes

Use after delivery to record what worked, what needs adjustment, and what
should change in the next course run.

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
