# SLIDE DECK SOURCE - WEEK 1 DAY 3

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 1 / Thursday |
| Date | August 20, 2026 |
| Weekly Theme | First Programs and Basic Values |
| Lecture Title | Putting Basic Values Together in Small Practical Programs |
| Assignments Supported | Assignment 1 - First Programs |
| Readiness Target | Students can complete 2-3 tiny programs and explain inputs, outputs, and value changes |
| Primary Watch Point | Avoid encyclopedic built-in types coverage; success depends on confidence, not breadth |
| Source Version | v2 refactor |

---

# Session Purpose

This session closes Week 1 by combining the smallest useful Python pieces into
small practical programs.

Students should see that they already have enough to build useful first
programs with:

- strings
- numbers
- variables
- simple expressions
- `print()`
- optional `input()`
- basic type awareness through use

The goal is not breadth. The goal is small, working, explainable programs.

---

# Review / Prior Work Bridge

Review from Days 1-2:

- Day 1: Python follows instructions, variables store values, and `print()`
  makes output visible.
- Day 2: numbers can be stored, expressions can create new values, and output
  can show calculated results.

Quick review questions:

- What value starts the program?
- What expression or assignment changes the value?
- What does the program print?
- Can you explain the value path in plain language?

Bridge into Day 3:

Today students combine the pieces they already have and finish Assignment 1 in a small,
controlled way.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 1
- textbook chapter areas: **A Gentle Introduction to Python** and **Built-In
  Data Types**

Day 3 reading focus:

- strings and text values
- numbers versus text
- names and values
- final considerations about choosing basic data representations

Use this reading to support:

- combining strings and numbers carefully
- explaining value flow
- avoiding confusion between text and numeric values

Today's reading boundary:

Students should not worry yet about the full inventory of Python data types,
collections, dates, advanced formatting, modules, packages, virtual
environments, or third-party libraries.

---

# What We Will Use Today

Today we will use:

- strings
- numbers
- variables
- simple expressions
- `print()`
- optional `input()` if stable
- basic type awareness

Today we will skip for now and revisit later:

- full built-in type coverage
- lists and dictionaries
- loops
- functions
- file saving
- AI-generated code
- package and environment management

---

# Assignments Supported

Primary support:

- Assignment 1 - First Programs

Day 3 should help students finish or substantially complete 2-3 very small
programs.

Good Assignment 1 options:

- greeting or introduction program
- simple calculator
- unit converter
- total-cost estimator
- personalized message builder

---

# Demo Set For This Session

Primary demo:

- `Demos/Week_01_First_Programs_and_Basic_Values/06_type_awareness.py`

Optional supporting demo:

- `Demos/Week_01_First_Programs_and_Basic_Values/05_input_number_conversion.py`

Instructor process note:

- `Demos/Instructor_Notes-Typing_vs_CopyPaste.md`

Use type awareness through practical values, not as a full type taxonomy.

---

# Student Hands-On Bridge

Students should finish or continue Assignment 1:

- 2-3 tiny programs
- visible output in each program
- clear variable names
- at least one value change or expression
- one brief explanation of value flow

Success today means:

```text
small + working + explainable
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect Week 1 pieces into integration day |
| Today's Working Set | 4-5 | Core | Name what to use and what to defer |
| Practical Value Combination | 6-9 | Core | Combine strings, numbers, variables, expressions, and output |
| Demo Bridge | 10-12 | Demo | Show type awareness and optional input conversion |
| Common Failure | 13-14 | Core | Prevent breadth overload and unexplained copied code |
| Hands-On Bridge | 15-16 | Lab Bridge | Finish Assignment 1 programs and evidence |
| Closing Check | 17 | Assessment / Evidence | Define Week 1 success |

---

# Slide-by-Slide Source

## Slide 1 - Put The Pieces Together

**Delivery Category:** Review

**Student-Visible Text:**

This week, you learned the smallest useful Python pieces.

Today, you combine them into tiny programs that run and make sense.

**Instructor Notes:**

Frame the day as integration, not expansion. Students may expect "more Python"
before they can build anything. Push back gently: they already have enough to
make several useful beginner scripts.

**Transition Cue:**

Start by naming what they already know.

**Visual Notes:**

Use a simple convergence visual: strings, numbers, variables, expressions, and
output flowing into a small `.py` file.

---

## Slide 2 - Week 1 Review

**Delivery Category:** Review

**Student-Visible Text:**

Monday made output visible.

Tuesday made numeric value flow visible.

**Instructor Notes:**

Ask students to recall one idea from each day:

- Monday: What does `print()` do?
- Tuesday: What does an expression create?

Keep this short. The point is to bridge into integration.

**Transition Cue:**

Now we focus on completing small programs, not collecting more topics.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Week 1 success is not a large program.

Week 1 success is a small program that runs, produces output, and can be
explained.

**Instructor Notes:**

This slide protects confidence. Students may compare their first script to apps
they use in daily life and feel the gap. Reframe success around the course's
actual beginner target.

**Transition Cue:**

To stay focused, we need to name today's working set.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

What we will use today:

strings, numbers, variables, simple expressions, `print()`, and optional
`input()`.

**Instructor Notes:**

This should feel like a toolbox students already recognize. The point is
integration, not a new list to memorize.

If `input()` is unstable or not introduced, state that assigned values remain a
valid path for Assignment 1.

**Transition Cue:**

Just as important: there are topics we are not responsible for yet.

**Visual Notes:**

Use a clean toolbox visual with the included tools.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

What we will skip for now and revisit later:

lists, dictionaries, loops, functions, files, packages, and AI-generated code.

**Instructor Notes:**

Keep this reassuring. These topics are not forbidden or unimportant. They are
future learning targets. Separating them from today's working set prevents the
textbook's breadth from turning into day-three anxiety.

**Transition Cue:**

With the working set clear, we can build small useful scripts.

**Visual Notes:**

Use a "parked for later" visual, not a warning or prohibition visual.

---

## Slide 6 - Small Can Still Be Useful

**Delivery Category:** Core

**Student-Visible Text:**

A useful first program does not have to be large.

It only needs a clear purpose, visible output, and values you can explain.

**Instructor Notes:**

Reframe usefulness away from size. A unit converter, total-cost estimator, or
personalized message builder is enough for Week 1.

**Transition Cue:**

The simplest useful programs combine values carefully.

---

## Slide 7 - Combine Values Carefully

**Delivery Category:** Core

**Student-Visible Text:**

Your program may use text and numbers together.

The important question is whether you can explain each value's role.

**Instructor Notes:**

Introduce type awareness through use. Do not launch into all built-in types.
Students need to know that text, whole numbers, decimal numbers, and boolean
values behave differently enough that they should pay attention.

**Transition Cue:**

This is where basic type awareness helps.

---

## Slide 8 - Type Awareness Through Use

**Delivery Category:** Core

**Student-Visible Text:**

Python values can have different types.

For Week 1, recognize text, whole numbers, decimal numbers, and true/false
values.

**Instructor Notes:**

Use practical names:

- string: text
- integer: whole number
- float: decimal number
- boolean: true/false

Avoid exhaustive coverage. The textbook covers more, but Assignment 1 needs practical
recognition.

**Transition Cue:**

Type awareness matters because output and explanation should remain clear.

---

## Slide 9 - Explain Every Main Line

**Delivery Category:** Core

**Student-Visible Text:**

Before submitting Assignment 1, ask: can I explain every main line?

If a line works but you cannot explain it, slow down and inspect it.

**Instructor Notes:**

This is the Day 3 thinking tool. It connects manual-first learning, debugging,
and later AI accountability without introducing AI as a coding shortcut.

**Transition Cue:**

Let's watch a small example that uses several value types without becoming
large.

---

## Slide 10 - Demo 1: Basic Type Awareness

**Delivery Category:** Demo

**Student-Visible Text:**

Watch how the program stores several different kinds of values.

The goal is recognition, not a full type inventory.

**Instructor Notes:**

Use:

`Demos/Week_01_First_Programs_and_Basic_Values/06_type_awareness.py`

Focus on:

- `student_name` as text
- `assignments_completed` as a whole number
- `average_score` as a decimal number
- `is_passing` as true/false

If using `type()`, explain it as an inspection tool. Do not turn the demo into
a type-system lecture.

**Transition Cue:**

If input is included, we need one more caution about numbers.

**Demo Connection:**

Primary demo file: `06_type_awareness.py`

---

## Slide 11 - Optional Demo: Input And Number Conversion

**Delivery Category:** Reserve

**Student-Visible Text:**

When users type into `input()`, Python receives text first.

For math, the text must be converted into a number.

**Instructor Notes:**

Use only if helpful:

`Demos/Week_01_First_Programs_and_Basic_Values/05_input_number_conversion.py`

This demo can support students who want an input-based calculator. If the class
is not ready, skip it and keep Assignment 1 on assigned values.

**Transition Cue:**

The next issue is not technical. It is how students should work with examples.

**Demo Connection:**

Optional demo file: `05_input_number_conversion.py`

---

## Slide 12 - Learning Move: Type It When It Is New

**Delivery Category:** Demo

**Student-Visible Text:**

Typing code can be part of learning.

Copying is not automatically wrong, but it should not replace understanding.

**Instructor Notes:**

Use:

`Demos/Instructor_Notes-Typing_vs_CopyPaste.md`

Keep this brief but explicit. In Week 1, typing examples helps students process
order, syntax, value names, and line relationships.

Connect this to Assignment 1: students should understand what they submit.

**Transition Cue:**

That leads to two common Week 1 traps.

---

## Slide 13 - Common Failure: Too Much Is Too Much

**Delivery Category:** Core

**Student-Visible Text:**

Trying to impress can make the first assignment harder than it needs to be.

Small, clean, and explainable is better than large and confusing.

**Instructor Notes:**

Name the trap kindly. Some students will overbuild because they think larger
means better. In Week 1, larger often means less explainable.

**Transition Cue:**

The other trap is using code that works but cannot be explained.

---

## Slide 14 - Common Failure: Working But Unexplained

**Delivery Category:** Core

**Student-Visible Text:**

Code that runs is not the whole goal.

You also need to explain what values the program uses and what output it
creates.

**Instructor Notes:**

This reinforces conceptual understanding over logic regurgitation. A simple
program with a clear explanation is stronger than a copied or overbuilt script
the student cannot discuss.

**Transition Cue:**

Now students can finish Assignment 1 with a clear target.

---

## Slide 15 - Hands-On Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Finish two or three tiny programs for Assignment 1.

Each program should run, show output, and make sense when you explain it.

**Instructor Notes:**

Recommended options:

- greeting or introduction program
- simple calculator
- unit converter
- total-cost estimator
- personalized message builder

Keep students out of feature sprawl. If a student is stuck, reduce scope until
the value flow is visible again.

**Transition Cue:**

The submission should preserve the work and one explanation.

**Lab Connection:**

This closes Assignment 1 - First Programs.

---

## Slide 16 - Evidence For Assignment 1

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Submit your `.py` files and be ready to explain one program.

Explain the starting values, any value changes, and the final output.

**Instructor Notes:**

Keep evidence requirements aligned with Assignment 1:

- `.py` file or files
- clear filenames
- code that runs
- readable output
- brief explanation of one program's value flow

If GitHub is introduced, reinforce that code and explanation should live
together eventually. Do not let GitHub mechanics overtake the Assignment 1 target.

**Transition Cue:**

The final Week 1 check is whether the programs run and make sense.

---

## Slide 17 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Week 1 worked if your small programs run and you can explain them.

Confidence comes from understanding what the code is doing.

**Instructor Notes:**

Ask:

- What values does one program use?
- What output does it produce?
- Where does a value change?
- Could you explain this script line by line to someone else?

Name the next step: Week 2 adds decisions and repetition.

**Transition Cue:**

Next week, programs begin making choices and repeating work.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one Day 2 numeric value path.
2. Run `06_type_awareness.py`.
3. Explain types through practical values only.
4. Optionally show input conversion if needed for student Assignment 1 choices.
5. Briefly discuss typing versus copy/paste as a learning move.
6. Move students quickly into Assignment 1 completion time.

Instructor pacing note:

Do not let type awareness become encyclopedic. The purpose is practical
recognition that supports first-program explanation.

---

# Lab / Assignment Bridge

By the end of Day 3, students should complete or be very close to completing
Assignment 1.

Minimum Assignment 1 closure target:

- 2-3 small programs
- visible output
- clear variable names
- at least one value change or expression
- one short explanation of value flow

---

# README / Submission Expectations

Keep documentation expectations beginner-sized.

Suggested student evidence:

- clear `.py` filenames
- code that runs without syntax errors
- readable output
- one short explanation of one program's values and output

If using GitHub, remind students that later courses will expect code and
documentation to stay together. For Assignment 1, do not overburden the first submission.

---

# AI-Use Boundary

AI is not allowed for normal Assignment 1 work unless the instructor explicitly says
otherwise.

Reason:

Students need manual-first practice with:

- typing code
- reading their own code
- running code
- recognizing values
- explaining output

AI can be discussed as a later support tool, but Week 1 fundamentals should be
experienced manually first.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Week 1 pieces combine | Strings, numbers, variables, expressions, output flowing into a small Python file | Avoid large app imagery |
| 4 | What we will use | Toolbox visual with strings, numbers, variables, expressions, `print()`, optional `input()` | Keep optional input visually secondary |
| 5 | What we skip | Parked-for-later area with lists, loops, functions, files, AI-generated code | Do not make skipped items look forbidden |
| 6 | Small useful program | Tiny calculator/converter producing useful output | Avoid overbuilt interface visuals |
| 8 | Type awareness | Four value cards: text, whole number, decimal number, true/false | Avoid full type taxonomy |
| 10 | Type demo | Small table of variable name, value, and type | Keep readable and beginner-friendly |
| 12 | Typing vs copy/paste | Two learning paths: type to learn, copy when understood | Avoid shaming copy/paste |
| 15 | Assignment 1 completion | Stack of 2-3 tiny `.py` files with output checks | Keep assignment visually small |
| 16 | Assignment 1 evidence | `.py` files plus short explanation note | Do not imply large README requirement yet |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students to trace one Day 2 value path |
| Working set | 6 min | Use Slide 4 only | Discuss why skipped topics are deferred |
| Practical combination | 15 min | Use Slides 6 and 9 only | Add examples from Assignment 1 options |
| Demo 1 | 12 min | Skip `type()` output if needed | Ask students to identify each value type |
| Optional input conversion | 0-8 min | Skip entirely | Support input-based Assignment 1 choices |
| Typing vs copy/paste | 5 min | Mention verbally | Use instructor narrative from notes |
| Hands-on bridge | 25+ min | Give one required completion path | Confer with students on Assignment 1 scope |
| Closing check | 5 min | Ask two questions verbally | Have students explain one program |

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

