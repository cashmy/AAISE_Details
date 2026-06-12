# SLIDE DECK SOURCE - WEEK 1 DAY 2

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 1 / Tuesday |
| Date | August 18, 2026 |
| Weekly Theme | First Programs and Basic Values |
| Lecture Title | Values Move from Input to Output |
| Assignments Supported | Assignment 1 - First Programs |
| Readiness Target | Students can trace values from numeric expression to printed result |
| Primary Watch Point | If `input()` is introduced, keep it shallow; if not, Assignment 1 must allow assigned variables only |
| Source Version | v2 refactor |

---

# Session Purpose

This session expands Day 1 from visible output into visible value movement.

Students should see that Python can:

- store numbers as values
- use expressions to create new values
- store calculation results
- print the result
- optionally collect a simple value with `input()`

The goal is not calculator complexity. The goal is traceability:

```text
starting value -> expression -> result value -> printed output
```

---

# Review / Prior Work Bridge

Review from Day 1:

- Python follows instructions line by line.
- `print()` makes output visible.
- strings are text values.
- variables refer to stored values.

Quick review questions:

- What does `print()` do?
- In `student_name = "Jordan"`, what is the variable name?
- What is the stored value?
- If the stored value changes, what can change in the output?

Bridge into Day 2:

Day 1 used mostly text values. Day 2 adds numeric values and expressions so the
program can calculate, not just display fixed text.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 1
- textbook chapter areas: **A Gentle Introduction to Python** and **Built-In
  Data Types**

Day 2 reading focus:

- numbers
- strings
- simple values
- basic type awareness
- basic expressions

Use this reading to support:

- numeric values
- simple calculations
- value changes
- output formatting at a beginner level

Today's reading boundary:

Students should not worry yet about complex numbers, decimals, fractions,
collections, dates, advanced formatting, modules, packages, or virtual
environments.

---

# What We Will Use Today

Today we will use:

- numeric variables
- simple expressions
- `+`, `-`, `*`, and `/`
- result variables
- `print()`
- optional `input()` only if the class is ready

Today we will not use yet:

- loops
- functions
- lists or dictionaries
- file saving
- AI-generated code
- advanced numeric types

---

# Assignments Supported

Primary support:

- Assignment 1 - First Programs

Day 2 prepares the calculator, converter, and total-cost style options in Assignment 1.

Students may still use assigned variables instead of `input()` if input has not
been introduced or is not stable yet.

---

# Demo Set For This Session

Primary demo:

- `Demos/Week_01_First_Programs_and_Basic_Values/03_numbers_expressions.py`

Optional demos:

- `Demos/Week_01_First_Programs_and_Basic_Values/04_input_optional.py`
- `Demos/Week_01_First_Programs_and_Basic_Values/05_input_number_conversion.py`

Use Demo 4 only if students are comfortable with Day 1 value flow.

Use Demo 5 only if the class is ready for the idea that `input()` returns text
and numeric input must be converted before math. Otherwise, save that for later
or show it as a brief instructor-only preview.

---

# Student Hands-On Bridge

Students should try one small practical script:

- a simple calculator
- a unit converter
- a total-cost estimator

Minimum expectation:

- start with assigned numeric variables
- calculate one result
- print the result
- change one starting value
- rerun the program
- explain what changed

Optional extension:

- replace one assigned value with `input()` if introduced in class

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect Day 1 output to Day 2 value flow |
| Numeric Values and Expressions | 4-7 | Core | Show numbers, operators, expressions, and result variables |
| Traceability | 8-9 | Core | Make value tracing the reasoning habit |
| Demo Bridge | 10-12 | Demo | Demonstrate calculation and optional input |
| Common Failure | 13-14 | Core | Preempt losing values and input confusion |
| Hands-On Bridge | 15-16 | Lab Bridge | Begin numeric Assignment 1 option work |
| Closing Check | 17 | Assessment / Evidence | Define success for Day 2 |

---

# Slide-by-Slide Source

## Slide 1 - From Output To Value Flow

**Delivery Category:** Review

**Student-Visible Text:**

Yesterday, we made output visible.

Today, we make values move through a program and produce a result.

**Instructor Notes:**

Connect directly to Day 1. Students already saw text values and variables.
Today's move is not a new world; it is the same value-flow idea with numbers
and expressions.

**Transition Cue:**

Start by naming what we already know how to do.

**Visual Notes:**

Use a two-step bridge: `print("Hello")` -> `total = price * quantity`.

---

## Slide 2 - Quick Review

**Delivery Category:** Review

**Student-Visible Text:**

A variable name refers to a stored value.

`print()` lets us see that value on the screen.

**Instructor Notes:**

Ask students to identify the name and value in:

```python
course_name = "Python Programming"
```

Then ask what `print(course_name)` displays.

Keep this quick. The purpose is activation, not reteaching.

**Transition Cue:**

If a string can be stored in a variable, a number can be stored too.

---

## Slide 3 - Today's Working Set

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use numbers, simple expressions, result variables, and `print()`.

`input()` is optional and only useful if it does not distract from value flow.

**Instructor Notes:**

This slide protects cognitive load. Name what students should focus on and
what they can safely ignore.

Explicitly say that assigned numeric variables are still a valid path for Assignment 1
if `input()` is not introduced or if it becomes distracting.

**Transition Cue:**

The first new idea is simple: numbers are values too.

---

## Slide 4 - Numbers Are Values Too

**Delivery Category:** Core

**Student-Visible Text:**

Python can store numbers just like it stores text.

Numbers can also be used in calculations.

**Instructor Notes:**

Use a direct comparison:

```python
student_name = "Jordan"
items_purchased = 3
```

Both are variables storing values. The difference is what Python can do with
those values.

**Transition Cue:**

Once numbers are stored, expressions can use them.

**Visual Notes:**

Show string and number examples side by side.

---

## Slide 5 - Expressions Create New Values

**Delivery Category:** Core

**Student-Visible Text:**

An expression combines values and produces a new value.

Example: `items_purchased * price_each` creates a subtotal.

**Instructor Notes:**

Keep operators practical:

- `+` adds
- `-` subtracts
- `*` multiplies
- `/` divides

Avoid turning this into a full math review. The teaching point is that an
expression produces a result the program can store or print.

**Transition Cue:**

The result of an expression usually deserves a clear name.

**Visual Notes:**

Show:

```text
items_purchased + price_each -> subtotal
```

Use multiplication in the actual expression if the visual allows it.

---

## Slide 6 - Result Variables

**Delivery Category:** Core

**Student-Visible Text:**

A result variable stores the answer from an expression.

Clear names help you explain what the answer means.

**Instructor Notes:**

Use:

```python
subtotal = items_purchased * price_each
```

Ask what `subtotal` stores and why that name is easier to explain than `x`.

This reinforces professional habits gently without overloading naming theory.

**Transition Cue:**

Now the program has a value worth showing.

---

## Slide 7 - Output Should Mean Something

**Delivery Category:** Core

**Student-Visible Text:**

Printing a number is better when the output tells us what the number means.

`print("Subtotal:", subtotal)` is clearer than printing `subtotal` alone.

**Instructor Notes:**

This slide prepares students for readable output in Assignment 1. It also reinforces that
output is communication, not just a proof that code ran.

Avoid formatting depth. Keep the pattern simple: label plus value.

**Transition Cue:**

The reasoning habit is to trace how the value reached the output.

---

## Slide 8 - Trace The Value

**Delivery Category:** Core

**Student-Visible Text:**

To understand a program, follow one value from start to finish.

Where did it start, what changed it, and where did it print?

**Instructor Notes:**

This is the thinking-tool slide for the day.

Use the questions repeatedly:

- Where did this value start?
- Which expression changed it?
- Where was the result stored?
- What line printed it?

**Transition Cue:**

Let's turn that into a concrete path.

**Visual Notes:**

Use arrows through: starting variable -> expression -> result variable ->
printed output.

---

## Slide 9 - The Day 2 Value Path

**Delivery Category:** Core

**Student-Visible Text:**

Starting values become expression results.

Expression results become printed output.

**Instructor Notes:**

Use the exact path:

```text
items_purchased -> subtotal -> tax_amount -> total -> printed output
```

Students do not need tax mastery. They need the habit of following the value.

**Transition Cue:**

Now we will watch that path in the numeric demo.

---

## Slide 10 - Demo 1: Numeric Calculation

**Delivery Category:** Demo

**Student-Visible Text:**

Watch how the starting numbers create the final total.

When one starting number changes, later values can change too.

**Instructor Notes:**

Use:

`Demos/Week_01_First_Programs_and_Basic_Values/03_numbers_expressions.py`

Recommended live move:

1. Start with `items_purchased` and `price_each`.
2. Calculate `subtotal`.
3. Print the subtotal.
4. Add `tax_rate`, `tax_amount`, and `total`.
5. Change `items_purchased`.
6. Rerun and compare output.

Ask after rerun:

- Which starting value changed?
- Which later values changed?
- Which line printed the final result?

**Transition Cue:**

This is enough for Assignment 1. Input is optional, and only helpful if it stays simple.

**Demo Connection:**

Primary demo file: `03_numbers_expressions.py`

---

## Slide 11 - Optional Demo: Simple `input()`

**Delivery Category:** Reserve

**Student-Visible Text:**

`input()` can collect a user response.

That response still becomes a value the program must trace.

**Instructor Notes:**

Use only if the class is ready:

`Demos/Week_01_First_Programs_and_Basic_Values/04_input_optional.py`

Keep it shallow:

- ask for a name
- store the response
- print a message using the stored value

Say explicitly that Assignment 1 may still use assigned variables if input has not been
fully introduced.

**Transition Cue:**

If input is used for numbers, there is one extra issue to respect.

**Demo Connection:**

Optional demo file: `04_input_optional.py`

---

## Slide 12 - Optional Demo: Numeric Input Needs Conversion

**Delivery Category:** Reserve

**Student-Visible Text:**

`input()` gives Python text.

For math, numeric input must be converted first.

**Instructor Notes:**

Use only if appropriate:

`Demos/Week_01_First_Programs_and_Basic_Values/05_input_number_conversion.py`

This is a common stumbling block. If the group is shaky, do not demonstrate
the error yet. Show the correct pattern briefly or save it for a later session.

Keep the focus on concept:

```text
typed response -> text -> converted number -> expression
```

**Transition Cue:**

Whether values are assigned or entered, the risk is losing track of where they
came from.

**Demo Connection:**

Optional demo file: `05_input_number_conversion.py`

---

## Slide 13 - Common Failure: Losing The Value

**Delivery Category:** Core

**Student-Visible Text:**

When several variables appear, it is easy to lose the path.

Slow down and ask: where did this value come from?

**Instructor Notes:**

Students may see several variables and stop tracing. Reinforce that tracing is
not extra work. It is how they understand the program.

Use the demo as the example:

- `items_purchased`
- `price_each`
- `subtotal`
- `tax_amount`
- `total`

**Transition Cue:**

The second risk is letting `input()` steal attention from the value path.

---

## Slide 14 - Common Failure: `input()` Can Distract

**Delivery Category:** Core

**Student-Visible Text:**

`input()` is useful, but it is not the main goal today.

The main goal is understanding how a value becomes output.

**Instructor Notes:**

This slide keeps the course aligned with Assignment 1. If students are excited by input,
that is fine, but comprehension matters more.

Say:

```text
If input helps your program, use it. If input makes the program confusing, use
assigned variables for now.
```

**Transition Cue:**

Now students can choose a small practical script and keep it traceable.

---

## Slide 15 - Hands-On Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Build one small script that starts with numbers and prints a result.

Good choices: calculator, converter, or total-cost estimator.

**Instructor Notes:**

Give students three controlled options:

- simple calculator
- unit converter
- total-cost estimator

Minimum version:

- assigned numeric variables
- one expression
- one result variable
- readable printed output

Optional extension:

- simple `input()` if introduced and stable

**Transition Cue:**

Before moving on, make sure the work has visible evidence.

**Lab Connection:**

This continues Assignment 1 - First Programs.

---

## Slide 16 - Evidence For Today

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Preserve the `.py` file and one example of output.

Be ready to explain the value path from starting number to printed result.

**Instructor Notes:**

Keep evidence light but real.

Students should be able to explain:

- starting value
- expression
- result variable
- printed output

If GitHub is already being introduced, this can become the first very small
example of preserving code and output together. Do not let that become the main
lesson.

**Transition Cue:**

The final check is whether students can trace the result.

---

## Slide 17 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

By the end of today, you should be able to store numbers, calculate a result,
and print it clearly.

You should also be able to trace where the printed result came from.

**Instructor Notes:**

Ask:

- What value started in this variable?
- What expression changed it?
- What was stored as the result?
- What printed at the end?
- If input was used, what did the user response become inside the program?

Name the next step: Day 3 will combine strings, numbers, and type awareness
into clearer first programs.

**Transition Cue:**

Next class, we combine these values more carefully and prepare to close Assignment 1.

---

# Demo Execution Notes

Recommended live sequence:

1. Begin with assigned numeric variables.
2. Create one result variable.
3. Print a labeled result.
4. Change one starting value.
5. Rerun and compare output.
6. Add optional `input()` only if it supports understanding.
7. Treat numeric conversion as reserve or instructor-modeled only if the group
   is ready.

Instructor pacing note:

The important part is not the arithmetic. The important part is whether
students can narrate the value path in plain language.

---

# Lab / Assignment Bridge

By the end of Day 2, students should have begun the numeric-value portion of
Assignment 1 or be ready to add it.

Minimum Day 2 student action:

- create or continue one `.py` file
- assign at least two numeric values
- use one expression
- store the result
- print a labeled result
- change one starting value and rerun

`input()` remains optional unless the instructor explicitly requires it.

---

# README / Submission Expectations

Keep documentation expectations small.

Suggested student evidence:

- clear `.py` filename
- code that runs without syntax errors
- readable output
- one sentence explaining how a starting number became a printed result

This prepares the later README habit without turning Week 1 into documentation
training.

---

# AI-Use Boundary

AI is not allowed for normal Day 2 Assignment 1 work unless the instructor explicitly
says otherwise.

Reason:

Students need manual practice with:

- assigning numbers
- writing expressions
- printing results
- tracing value flow

AI can be discussed later as explanation or debugging support, but it should
not replace first contact with the mechanics.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Output to value flow | Day 1 text output transforming into Day 2 calculation output | Avoid making it look like a large app |
| 3 | Working set | Small toolbox of numbers, expressions, result variable, `print()` | Keep `input()` visually optional |
| 4 | Numbers as values | Side-by-side string variable and numeric variable | Keep type discussion light |
| 5 | Expression creates value | Starting values flowing into expression and subtotal | Avoid dense math notation |
| 8 | Trace value path | Arrows from starting value to expression to result to output | Make arrows clear |
| 10 | Numeric demo | Total-cost calculation with changed starting value and changed output | Do not show full code screenshot |
| 12 | Input conversion | User typed text becoming converted number before math | Use only if slide is included |
| 15 | Hands-on choices | Three mini-panels: calculator, converter, total-cost estimator | Keep examples beginner-friendly |
| 16 | Evidence | `.py` file plus labeled output and value path note | Keep documentation expectation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slide 1 only | Ask name/value review questions |
| Working set and values | 10 min | Combine Slides 3-4 | Add simple string vs number examples |
| Expressions and output | 15 min | Use Slides 5 and 7 only | Add operator prediction questions |
| Traceability | 8 min | Use Slide 8 only | Have students trace the demo path verbally |
| Demo 1 | 18 min | Show only subtotal and total | Change values and rerun multiple times |
| Optional input demos | 0-12 min | Skip entirely | Show simple input and conversion if ready |
| Hands-on bridge | 20+ min | Give one required script pattern | Let students choose Assignment 1 option |
| Closing check | 5 min | Ask two questions verbally | Have students explain their own value path |

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

