# SLIDE DECK SOURCE - WEEK 1 DAY 1

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 1 / Monday |
| Date | August 17, 2026 |
| Weekly Theme | First Programs and Basic Values |
| Lecture Title | What a Python Program Does |
| Assignments Supported | A1 - First Programs |
| Readiness Target | Students can run a tiny program and explain what a variable stores |
| Primary Watch Point | Do not assume `input()` yet; keep setup friction from consuming the session |
| Source Version | v2 refactor |

---

# Session Purpose

This first session should make programming feel visible, small, and possible.

Students do not need a broad tour of Python today. They need to see that:

- a Python file contains instructions
- Python runs those instructions in order
- `print()` makes output visible
- strings are text values
- variables store values that can be reused

The emotional goal is confidence through visible success. The technical goal is
basic value flow.

---

# Course Position / Prior Bridge

This is the first course meeting, so there is no prior lab to review.

Use the opening to establish the course pattern:

```text
small visible program
-> explanation of what happened
-> small change
-> rerun
-> explain the changed output
```

This pattern will recur throughout the course.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 1
- textbook chapter area: **A Gentle Introduction to Python**

Day 1 reading focus:

- what programming is
- what Python is
- setting up the environment
- how to run a Python program
- Python's execution model
- a word about AI

Today's reading boundary:

Students should not worry yet about virtual environments, packages, modules,
namespaces, scopes, third-party libraries, or advanced style rules. Those
topics may appear in the textbook, but today focuses on running one tiny
program and explaining visible output.

---

# What We Will Use Today

Today we will use:

- `print()`
- strings
- variables
- running and rerunning a program
- visible output

Today we will not use yet:

- `input()`
- calculations
- loops
- functions
- AI-generated code
- packages or virtual environments

---

# Assignments Supported

Primary support:

- A1 - First Programs

A1 remains intentionally small. For Day 1, students should begin with greeting,
message, or variable-based output programs.

Do not require:

- `input()`
- calculations
- loops
- functions
- AI-generated code

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_01_First_Programs_and_Basic_Values/01_print_strings_variables.py`
- `Demos/Week_01_First_Programs_and_Basic_Values/02_strings_and_variable_updates.py`

Reserve demo:

- `Demos/Week_01_First_Programs_and_Basic_Values/03_numbers_expressions.py`

Use Demo 3 only if students are stable with strings, variables, and visible
output. It can also be saved for Day 2.

---

# Student Hands-On Bridge

Students should try one tiny program before the end of class:

- print a greeting
- store one text value in a variable
- print the variable
- change the value
- rerun the program
- explain what changed

This is the first small step toward A1.

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Opening and Course Frame | 1-3 | Core | Reduce anxiety and define today's win |
| Today's Working Set | 4 | Core | Name what students should focus on and defer |
| Program Execution Model | 5-6 | Core | Show line-by-line instructions and visible output |
| Values and Variables | 7-9 | Core | Separate strings, variable names, and stored values |
| Demo Bridge | 10-12 | Demo | Make value flow visible through small demos |
| Common Failure | 13-14 | Core | Preempt quotes and variable-name confusion |
| Hands-On Bridge | 15-16 | Lab Bridge | Begin A1 without overloading the day |
| Closing Check | 17 | Assessment / Evidence | Define success for the session |

---

# Slide-by-Slide Source

## Slide 1 - Make Something Happen

**Delivery Category:** Core

**Student-Visible Text:**

Your first goal is to make Python do something visible.

If you can run a tiny program and explain the output, you are doing real
programming.

**Instructor Notes:**

Open with confidence rather than complexity. Tell students that today's win is
not impressive code. Today's win is making Python do something visible and then
being able to explain what happened.

Avoid beginning with a long syllabus-style technical explanation. The first
technical emotion should be, "I can make this run."

**Transition Cue:**

Before we worry about large programs, we need one tiny program that runs.

**Visual Notes:**

Use a simple before/after visual: an empty editor on the left and a terminal
showing one line of output on the right.

---

## Slide 2 - Start Small, Build Outward

**Delivery Category:** Core

**Student-Visible Text:**

This course starts with small working programs and builds outward.

You are not expected to know everything today; you are expected to make one
small thing work.

**Instructor Notes:**

Position the course as cumulative. Students are not expected to know Python
today. They are expected to learn how small pieces work and then combine those
pieces over time.

This slide helps prevent day-one overload.

**Transition Cue:**

The first small piece is understanding what Python does with the lines we give
it.

**Visual Notes:**

Use a simple growth path: tiny program -> small utility -> structured program
-> capstone.

---

## Slide 3 - Today's Success

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

run the program, change one value, run it again, and explain what changed.

**Instructor Notes:**

Make the success target explicit. Students should not leave thinking that
success means knowing every symbol or term. Today, success means they can run a
program, change a value, rerun it, and explain the visible difference.

**Transition Cue:**

That means we need a simple model of what a program is.

**Lab Connection:**

This directly prepares A1, where students create 2-3 very small programs and
explain one of them.

---

## Slide 4 - Today's Working Set

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use `print()`, strings, variables, and visible output.

We will not use `input()`, calculations, loops, functions, or AI-generated code
yet.

**Instructor Notes:**

This slide protects Day 1 cognitive load. The textbook may mention more than
the class will use today, and students may already have heard terms like
functions, packages, or AI coding help.

Name the boundary plainly. Those topics are not bad or forbidden forever. They
are simply not today's working set.

**Transition Cue:**

Now that the working set is clear, we can focus on what Python does with the
lines in the file.

**Visual Notes:**

Use a small toolbox visual:

- included tools: `print()`, strings, variables, run/rerun
- deferred tools: `input()`, loops, functions, AI

---

## Slide 5 - A Program Is Instructions

**Delivery Category:** Core

**Student-Visible Text:**

Python follows the instructions in your file.

Most beginner programs run from top to bottom, one line at a time.

**Instructor Notes:**

Keep this concrete. Python is not guessing what the student meant. It runs
instructions in order, and small syntax details matter because they tell Python
what kind of instruction or value it is seeing.

This is not the time to explain all execution details. The mental model is:
top line, then next line, then next line.

**Transition Cue:**

If Python follows instructions, we need our first instruction that gives us
visible evidence.

**Visual Notes:**

Show three simple lines stacked vertically, with a highlight moving from top to
bottom.

---

## Slide 6 - `print()` Makes Output Visible

**Delivery Category:** Core

**Student-Visible Text:**

`print()` makes a value or message appear on the screen.

Visible output is your first evidence that the program ran.

**Instructor Notes:**

Treat `print()` as the first high-payoff tool. It lets students know the file
ran and lets them see a value.

Connect this to evidence language early: if output appears, something worked.
If the output changes after a value changes, that is evidence of value flow.

**Transition Cue:**

Now we need something for `print()` to show.

**Visual Notes:**

Show `print("Hello")` on one side and terminal output `Hello` on the other.

---

## Slide 7 - Strings Are Text Values

**Delivery Category:** Core

**Student-Visible Text:**

Text values are called strings.

In Python, quotes tell the program, "treat this as text."

**Instructor Notes:**

Introduce strings as text values, not as a complete type-system lecture. Show
that `"Hello"` is a value Python can print, while an unquoted bare word is read
as a name or instruction context.

Keep the language beginner-friendly:

- quoted text means text value
- unquoted words are not automatically text

**Transition Cue:**

Once we have a text value, we can either print it directly or store it first.

**Visual Notes:**

Use a simple contrast:

- `"Hello"` = text value
- `Hello` = not a string

---

## Slide 8 - Variables Store Values

**Delivery Category:** Core

**Student-Visible Text:**

A variable is a name that refers to a stored value.

The name and the value are related, but they are not the same thing.

**Instructor Notes:**

Slow down here. Separate the name from the value.

Use a physical analogy if useful: a label on a box is not the object inside the
box. The variable name lets us refer to the value later.

Avoid saying variables are "containers" too strongly if that creates confusion
later. For Day 1, "label for a stored value" is enough.

**Transition Cue:**

Now we can put the value flow together.

**Visual Notes:**

Show:

```text
student_name -> "Avery"
```

Keep the variable name visually distinct from the string value.

---

## Slide 9 - Value Flow

**Delivery Category:** Core

**Student-Visible Text:**

The basic flow today is simple:

create a value, store it in a variable, then use `print()` to show it.

**Instructor Notes:**

This is the core mental model for A1.

Use the exact value-flow pattern:

```text
value exists -> variable stores it -> output displays it
```

Do not introduce `input()` yet unless the class is moving unusually quickly.
Assigned values are legitimate for Day 1.

**Transition Cue:**

Let's watch that happen in a tiny program.

**Visual Notes:**

Use three connected blocks:

```text
"Python Programming" -> course_name -> print(course_name)
```

---

## Slide 10 - Demo 1: First Visible Program

**Delivery Category:** Demo

**Student-Visible Text:**

As the demo runs, watch for two things:

which values are stored, and which lines make output appear.

**Instructor Notes:**

Use:

`Demos/Week_01_First_Programs_and_Basic_Values/01_print_strings_variables.py`

Recommended live move:

1. Start with only `print("Welcome to class!")`.
2. Run it.
3. Add `course_name = "Python Programming"`.
4. Print `course_name`.
5. Add `student_name = "Jordan"`.
6. Print `student_name`.

After each run, ask:

- What appeared?
- Which line caused it?
- Which value is being stored?

**Transition Cue:**

The next useful idea is that a variable can point to a different current value
after we update it.

**Demo Connection:**

Primary demo file: `01_print_strings_variables.py`

---

## Slide 11 - Demo 2: Change One Value

**Delivery Category:** Demo

**Student-Visible Text:**

When a variable is assigned a new value, later output can change.

Run the program again and compare what is different.

**Instructor Notes:**

Use:

`Demos/Week_01_First_Programs_and_Basic_Values/02_strings_and_variable_updates.py`

Focus on:

- `status = "new"`
- output shows `new`
- `status = "learning"`
- output now shows `learning`

Do not rush into string concatenation. If shown, explain it as combining text
pieces, not as a major new requirement.

**Transition Cue:**

This is the first version of debugging and testing: change one thing and look
at what changed.

**Demo Connection:**

Primary demo file: `02_strings_and_variable_updates.py`

---

## Slide 12 - Optional Preview: Numbers Later

**Delivery Category:** Reserve

**Student-Visible Text:**

Numbers can move through the same value-flow pattern.

Today, this is only a preview unless the class is ready.

**Instructor Notes:**

Use only if students are stable with the first two demos and there is time.

Reference:

`Demos/Week_01_First_Programs_and_Basic_Values/03_numbers_expressions.py`

Frame this as a preview for Day 2, not as a Day 1 expectation. Students should
not leave thinking A1 must already include calculations if numbers have not
been taught carefully yet.

**Transition Cue:**

Before students begin, name the mistakes that are most likely to happen.

**Demo Connection:**

Reserve demo file: `03_numbers_expressions.py`

---

## Slide 13 - Common Failure: Missing Quotes

**Delivery Category:** Core

**Student-Visible Text:**

`"Hello"` is a string because it has quotes.

`Hello` without quotes is not automatically text to Python.

**Instructor Notes:**

Show this mistake calmly. The goal is not to scare students with errors. The
goal is to show that Python needs markers so it knows what is text.

If demonstrating the error live, do it briefly and then correct it immediately.

**Transition Cue:**

The second common mistake is confusing the variable name with the value.

**Visual Notes:**

Use side-by-side cards:

- Correct: `print("Hello")`
- Problem: `print(Hello)`

---

## Slide 14 - Common Failure: Name vs Value

**Delivery Category:** Core

**Student-Visible Text:**

The variable name is how we refer to the value.

Changing the stored value can change what the program prints later.

**Instructor Notes:**

Use `student_name = "Jordan"` as the anchor example.

Ask:

- What is the variable name?
- What is the stored value?
- What will `print(student_name)` display?

This reinforces explanation, not memorization.

**Transition Cue:**

Now students are ready for a very small hands-on move.

**Visual Notes:**

Show:

```text
student_name
     |
     v
"Jordan"
```

---

## Slide 15 - Hands-On Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Create one tiny program with a greeting and one variable.

Then change the variable value and rerun the program.

**Instructor Notes:**

Give students a bounded task:

1. Create a new `.py` file.
2. Print a greeting.
3. Store one text value in a variable.
4. Print that variable.
5. Change the stored value.
6. Rerun the program.

Keep the room moving. This is not the full A1 yet; it is the first foothold.

**Transition Cue:**

When you save your work, preserve the evidence that it ran.

**Lab Connection:**

This begins A1 - First Programs.

---

## Slide 16 - Evidence For Today

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Save the `.py` file and make sure it runs.

Be ready to explain one value you changed and how the output changed.

**Instructor Notes:**

Keep documentation expectations light. Today, students should preserve:

- the `.py` file
- a clear filename
- code that runs
- a short explanation of one value change

Do not turn Day 1 into a full GitHub or README lesson unless the class is ready.
If GitHub is introduced, treat it as where work will eventually live, not as
the main learning target today.

**Transition Cue:**

The final check is simple: can you run it and explain it?

**Assignment Connection:**

A1 later asks students to create 2-3 small programs and briefly explain one.

---

## Slide 17 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

By the end of today, you should be able to run a tiny Python program.

You should also be able to explain what one variable stores.

**Instructor Notes:**

End with the success definition. Students should be able to answer:

- What does `print()` do?
- What value is stored in this variable?
- If I change the value, what changes in the output?
- Why does text need quotes?

Name the next step: Day 2 will add numbers, expressions, and possibly simple
input/output flow.

**Transition Cue:**

Next class, we keep the same pattern and add numeric values.

---

# Demo Execution Notes

Recommended live sequence:

1. Type or paste the smallest possible `print()` example.
2. Run it immediately.
3. Add one string variable.
4. Print the variable.
5. Change the variable value.
6. Rerun and compare output.
7. Only preview numbers if the class is ready.

Instructor pacing note:

The demo should feel slow. For beginners, the invisible work is connecting file,
line, value, run button or command, and output window.

---

# Lab / Assignment Bridge

By the end of Day 1, students should have started or be ready to start the
first part of A1.

Minimum Day 1 student action:

- create one `.py` file
- print at least one line of text
- store one text value in a variable
- print that variable
- change one value and rerun

Do not require `input()` today.

---

# README / Submission Expectations

Keep Week 1 Day 1 documentation small.

Suggested student evidence:

- a clear `.py` filename
- code that runs without syntax errors
- one sentence explaining a value change

Formal README/GitHub expectations can be layered in later, but this session can
begin using the phrase "preserve evidence" so the idea is not new later.

---

# AI-Use Boundary

AI is not allowed for normal Day 1 work unless the instructor explicitly says
otherwise.

Reason:

Students need manual first contact with:

- typing code
- running code
- seeing output
- making one change
- explaining one result

AI can be discussed as a future support tool, but not as today's starting point.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | First visible success | Empty editor beside terminal with one friendly output line | Avoid complex IDE screenshots |
| 2 | Course growth path | Tiny program growing into structured project blocks | Do not imply a large project is expected now |
| 4 | Today's working set | Small toolbox showing `print()`, strings, variables, run/rerun, with deferred tools set aside | Do not make deferred tools look forbidden forever |
| 5 | Line-by-line execution | Three code lines with top-to-bottom highlight | Avoid dense code |
| 6 | `print()` output | Code-to-terminal before/after visual | Keep output large and readable |
| 8 | Variable stores value | Variable name connected to quoted text value | Keep label and value visually distinct |
| 9 | Value flow | Value -> variable -> print -> output path | Do not add input yet |
| 13 | Quotes matter | Quoted text vs unquoted word contrast | Avoid scary error imagery |
| 16 | Evidence | Saved `.py` file and one output line | Keep documentation expectation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Opening and course frame | 8 min | Use Slides 1 and 3 only | Add student reassurance and course pattern |
| Execution model | 10 min | Combine Slides 4 and 5 | Ask students to predict next line |
| Values and variables | 12 min | Use Slide 8 as summary anchor | Add name/value checks |
| Demo 1 and 2 | 20 min | Run only Demo 1 | Type the demo live and rerun after each change |
| Common failures | 8 min | Use only missing quotes | Briefly demonstrate and fix both mistakes |
| Hands-on bridge | 15+ min | Give only one tiny task | Let students begin A1 immediately |
| Closing check | 5 min | Ask two questions verbally | Have students explain a value change |

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
