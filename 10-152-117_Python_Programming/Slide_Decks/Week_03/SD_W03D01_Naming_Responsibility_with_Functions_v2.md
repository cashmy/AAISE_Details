# SLIDE DECK SOURCE - WEEK 3 DAY 1

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 3 / Monday |
| Date | August 31, 2026 |
| Weekly Theme | Organizing Code and Data |
| Lecture Title | Naming Responsibility with Functions |
| Assignments Supported | Assignment 4 - Function Builder |
| Readiness Target | Students can explain what each function is responsible for |
| Primary Watch Point | Do not assume deep return-value fluency too fast; keep function count small and intentional |
| Source Version | v2 refactor |

---

# Session Purpose

This session introduces functions as a way to organize logic into named,
explainable responsibilities.

Students should understand that functions are not extra complexity for their
own sake. They are a way to take logic students already know and give that
logic a clear job, a name, and a reusable shape.

The target pattern is:

```text
repeated or related logic -> named responsibility -> function call -> clearer program
```

---

# Review / Prior Work Bridge

Review from Week 2:

- conditions choose between branches
- loops repeat work
- small programs should remain traceable
- A2 and A3 required students to explain decision and repetition paths

Quick review questions:

- Where did your Week 2 program repeat logic?
- Which parts of your code had clear jobs?
- Which parts were hard to explain line by line?
- If you had to reuse one part, what would you want to name?

Bridge into Week 3:

This week, students begin shaping code so it is easier to read, reuse, revise,
and explain.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 3
- textbook chapter area: **Functions, the Building Blocks of Code**

Day 1 reading focus:

- why use functions
- input parameters
- return values
- documenting your code

Use this reading to support:

- naming responsibility
- reducing repeated code
- writing small functions
- explaining what a function receives and returns

Today's reading boundary:

Students should not worry yet about recursion, anonymous functions, function
attributes, decorators, generators, advanced imports, or full namespace theory.

---

# What We Will Use Today

Today we will use:

- `def`
- function names
- function calls
- parameters
- return values
- responsibility statements
- small refactors

Today we will skip for now and revisit later:

- recursion
- lambdas
- decorators
- advanced import patterns
- large function libraries
- AI-generated refactors before a manual baseline exists

---

# Assignments Supported

Primary support:

- Assignment 4 - Function Builder

A4 asks students to create or refactor a small Python program that uses
functions to organize logic.

Minimum assignment direction:

- define at least two functions
- call each function correctly
- use meaningful function names
- avoid unnecessary repeated code
- explain what each function does

---

# Readiness Target

By the end of the session, students should be able to:

- identify repeated or related logic
- name one clear job for a function
- define a small function with `def`
- call a function
- recognize a parameter as information going in
- recognize a return value as information coming out
- explain why the refactored version is easier to understand

---

# Primary Watch Point

The main risk is treating functions as a syntax achievement rather than an
organization decision.

Do not reward function count by itself. A small program with two clear
functions is stronger than a scattered program with many tiny, unclear
functions.

The instructional question is:

```text
What job does this function own?
```

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_03_Organizing_Code_and_Data/01_repeated_code_before_functions.py`
- `Demos/Week_03_Organizing_Code_and_Data/02_function_refactor.py`
- `Demos/Week_03_Organizing_Code_and_Data/03_functions_input_process_output.py`

Recommended use:

1. Use Demo 1 as the rough repeated-code baseline.
2. Use Demo 2 to show a function naming repeated logic.
3. Use Demo 3 to show input/process/output responsibilities in a small program.

---

# Student Hands-On Bridge

Students should begin A4 by choosing a small program or earlier assignment that
has repeated or related logic.

Suggested start:

```text
1. Find repeated or related code.
2. Name the job.
3. Write one function for that job.
4. Call the function.
5. Explain what goes in and what comes out.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect Week 2 traceability to Week 3 organization |
| Today's Working Set | 4-5 | Core | Bound function topics and defer advanced function concepts |
| Why Functions | 6-8 | Core | Show repeated code as a signal and functions as named responsibility |
| Function Data Flow | 9-12 | Core / Demo | Teach `def`, calls, parameters, returns, and responsibility |
| Common Failures | 13-14 | Core | Prevent over-fragmenting and unclear function names |
| Assignment 4 Bridge | 15-17 | Lab Bridge / Evidence | Start A4 with a small refactor and explanation |
| Closing Check | 18 | Assessment / Evidence | Define successful function understanding |

---

# Slide-by-Slide Source

## Slide 1 - Code Can Work And Still Be Messy

**Delivery Category:** Review

**Student-Visible Text:**

A program can run correctly and still be hard to read, change, or explain.

Week 3 adds a new goal: shaping code so the purpose is easier to see.

Today, watch for:

- repeated code
- unclear responsibility
- logic that deserves a name
- code that becomes easier to explain after refactoring

**Instructor Notes:**

Normalize this as an evolution from Week 2, not criticism of student work.
Getting code to run is still important. Now students begin improving the shape
of working code.

**Transition Cue:**

Last week focused on program flow. This week starts with program shape.

**Visual Notes:**

Use a split visual: one long undivided code block versus a version with named
sections.

---

## Slide 2 - Flow Becomes Shape

**Delivery Category:** Review

**Student-Visible Text:**

Week 2 focused on control flow:

- conditions choose
- loops repeat
- output shows the result

Week 3 asks how that logic should be organized so another person can understand
it.

**Instructor Notes:**

Connect functions to skills students already have. Functions do not replace
conditions and loops; they hold and name useful pieces of logic.

**Transition Cue:**

One signal that code needs shaping is repetition.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Repeated or related logic can be named, separated, reused, and explained.

For each function, ask:

- What job does it own?
- What information does it need?
- What result or behavior does it produce?
- Where is it called?

**Instructor Notes:**

This is the main Week 3 Day 1 mental model. Keep returning to responsibility
language.

**Transition Cue:**

Let's name today's function tools.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- `def`
- function names
- function calls
- parameters
- return values
- small refactors

These tools help us give code a clear job and reuse that job safely.

**Instructor Notes:**

Keep the list practical. The purpose is to help students build A4, not to
teach every function feature in Python.

**Transition Cue:**

Some function topics are real, but they are not today's target.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip recursion, lambdas, decorators, and advanced imports for now.

Today's goal is smaller:

- find repeated or related logic
- name one clear responsibility
- write a function
- call it correctly

**Instructor Notes:**

This protects students from the textbook's breadth. Many function topics are
useful later, but A4 depends on practical function organization.

**Transition Cue:**

The first clue that a function may help is repeated code.

---

## Slide 6 - Repeated Code Is A Signal

**Delivery Category:** Core

**Student-Visible Text:**

Repeated code often means the program is doing the same job more than once.

That repeated job may deserve a function.

Look for repeated:

- calculations
- output formatting
- validation checks
- decision patterns

**Instructor Notes:**

Avoid saying every repeated line must become a function. Repetition is a signal
to inspect, not an automatic rule.

**Transition Cue:**

Let's look at a rough version before functions.

---

## Slide 7 - Demo 1: Repeated Code Before Functions

**Delivery Category:** Demo

**Student-Visible Text:**

Watch for repeated logic.

Before changing code, identify:

- which lines repeat
- what job those lines perform
- what would be annoying to update later

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/01_repeated_code_before_functions.py`

Do not immediately fix it. Let students see the pattern first.

**Transition Cue:**

Now we can give the repeated job a name.

**Demo Connection:**

Primary demo file: `01_repeated_code_before_functions.py`

---

## Slide 8 - A Function Owns One Clear Job

**Delivery Category:** Core

**Student-Visible Text:**

A function is a named piece of code with a clear responsibility.

Good function names usually describe the job:

- `calculate_total`
- `get_status`
- `show_result`

If the name is hard to choose, the job may not be clear yet.

**Instructor Notes:**

Use this slide to anchor naming as evidence of thinking. A vague name often
reveals a vague responsibility.

**Transition Cue:**

The function shape starts with `def`.

---

## Slide 9 - Function Shape

**Delivery Category:** Core

**Student-Visible Text:**

Basic function shape:

```python
def function_name(parameter):
    result = parameter + 1
    return result
```

The definition creates the function. The call runs it.

**Instructor Notes:**

Keep syntax explanation light but concrete. Students need to distinguish
definition from call.

**Transition Cue:**

Now compare the repeated version to a function version.

---

## Slide 10 - Demo 2: Refactor Into A Function

**Delivery Category:** Demo

**Student-Visible Text:**

Watch what changes after the repeated logic becomes a function.

Trace:

- the function definition
- the parameter going in
- the return value coming out
- the function call being reused

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/02_function_refactor.py`

Compare directly to Demo 1. The win is not only fewer lines; it is clearer
responsibility and easier reuse.

**Transition Cue:**

Functions also help separate different kinds of work.

**Demo Connection:**

Primary demo file: `02_function_refactor.py`

---

## Slide 11 - Values Come In, Results Come Out

**Delivery Category:** Core

**Student-Visible Text:**

Parameters are information the function receives.

Return values are information the function sends back.

For a beginner mental model:

```text
input value -> function job -> returned result
```

**Instructor Notes:**

Do not over-teach return-value theory. Use a simple box-and-arrow mental model.
Students need enough understanding to call and explain a small function.

**Transition Cue:**

The next demo separates a small program into responsibilities.

---

## Slide 12 - Demo 3: Input, Process, Output Responsibilities

**Delivery Category:** Demo

**Student-Visible Text:**

Watch how the program separates jobs:

- calculate the average
- decide the status
- show the result

Each function has a responsibility that can be named and explained.

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/03_functions_input_process_output.py`

Point out that the demo uses hardcoded values so attention stays on structure.

**Transition Cue:**

Functions help, but only when they are intentional.

**Demo Connection:**

Primary demo file: `03_functions_input_process_output.py`

---

## Slide 13 - Common Failure: More Functions Is Not Better

**Delivery Category:** Core

**Student-Visible Text:**

More functions does not automatically mean better structure.

A useful function should have:

- a clear job
- a meaningful name
- a reason to exist
- code that is easier to explain because of it

Tiny random fragments can make code harder, not easier.

**Instructor Notes:**

Preempt over-fragmenting. Students may think the assignment rewards function
count. It rewards explainable organization.

**Transition Cue:**

The other common failure is naming without meaning.

---

## Slide 14 - Common Failure: Vague Function Names

**Delivery Category:** Core

**Student-Visible Text:**

Names should help the reader understand the job.

Weak names:

- `do_it`
- `thing`
- `process`

Clearer names:

- `calculate_total`
- `get_status`
- `show_result`

**Instructor Notes:**

Use name quality as a gentle but powerful review tool. If a name is vague,
ask what job the function really owns.

**Transition Cue:**

Now students can begin Assignment 4 with a small refactor.

---

## Slide 15 - Assignment 4 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 4, build or revise one small program using functions.

A good first version should include:

- at least two functions
- meaningful function names
- correct function calls
- one parameter or return value if introduced
- behavior you can explain

**Instructor Notes:**

Encourage students to refactor earlier calculator, converter, decision, or loop
work if appropriate. This keeps the task grounded in logic they already know.

**Transition Cue:**

Start by planning the responsibilities before writing many functions.

**Lab Connection:**

Supports Assignment 4 - Function Builder.

---

## Slide 16 - Function Planning Checklist

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Before coding, write a short function plan.

For each function, list:

- name
- job
- information needed
- result or visible behavior

Then write the smallest version that proves the plan works.

**Instructor Notes:**

This gives struggling students a practical scaffold. It also gives stronger
students a lightweight design habit without turning A4 into a design document.

**Transition Cue:**

The submission needs evidence that the structure helped.

---

## Slide 17 - Evidence For A Function Program

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should show working code and explainable structure.

Useful evidence includes:

- one working `.py` file
- at least two functions
- readable names
- visible output or behavior
- a short explanation of each function's job

**Instructor Notes:**

If GitHub/README expectations are active, students can place the short
explanation with the code. Keep documentation lightweight but meaningful.

**Transition Cue:**

Close by returning to responsibility.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can name the job, you can shape the code.

Before submitting A4, ask:

- What does each function do?
- Where is each function called?
- What goes in?
- What comes out?
- Why is this clearer than one long block?

**Instructor Notes:**

Close on explanation as evidence of organization. This prepares students for
Tuesday, when data structures begin organizing information.

**Transition Cue:**

Next session, we organize related data with lists and dictionaries.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one Week 2 traceable logic example.
2. Run `01_repeated_code_before_functions.py`.
3. Ask what job repeats.
4. Run `02_function_refactor.py`.
5. Trace parameter, return value, and repeated calls.
6. Run `03_functions_input_process_output.py`.
7. Name each function's responsibility.
8. Move students into A4 planning and first implementation.

Instructor pacing note:

If students struggle with return values, keep the demo concrete. A function
that prints visible output can still support the organization concept, but A4
should include a parameter or return value when students are ready.

---

# Lab / Assignment Bridge

By the end of Day 1, students should have started Assignment 4 or have a clear
function plan.

Minimum A4 start target:

- selected small program or refactor target
- at least two planned functions
- each function has a named responsibility
- first function definition written or sketched

---

# README / Submission Expectations

Suggested student evidence:

- clear `.py` filename
- code that runs without syntax errors
- at least two functions
- visible behavior or output
- short explanation of each function's responsibility
- AI-use note only if AI was explicitly allowed for comparison or refactoring

---

# AI-Use Boundary

Limited AI comparison may be allowed only after students have a manual version
or manual plan, if the instructor permits it.

Students may not submit AI-generated code they cannot explain.

If AI is used, students should answer:

- What did AI suggest?
- What did you keep?
- What did you change or reject?
- Why does the final version make sense?

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Working but messy | Split contrast: working long code block versus shaped named parts | Avoid shaming rough code |
| 2 | Flow to shape | Conditions and loops flowing into functions | Keep previous topics recognizable |
| 3 | Success pattern | Repeated logic becoming named responsibility | Avoid abstract architecture diagrams |
| 4 | Today's tools | Toolbox with `def`, names, calls, parameters, returns | Avoid advanced function topics |
| 5 | Deferred function topics | Parked-for-later shelf: recursion, lambdas, decorators, imports | Keep reassuring tone |
| 6 | Repeated code signal | Short repeated snippets highlighted | Avoid unreadable code walls |
| 8 | Function responsibility | Function name card with one job label | Keep one job only |
| 9 | Function shape | Minimal `def` block with definition and call distinction | Make call vs definition clear |
| 10 | Refactor demo | Before/after repeated calculation to function call | Avoid too much code detail |
| 11 | Function data flow | Input value -> function box -> returned result | Keep beginner-friendly |
| 12 | IPO responsibilities | Three function boxes: calculate, decide, show | Do not imply full architecture |
| 13 | Too many functions | Reasonable split versus tiny random fragments | Avoid mocking over-structure |
| 15 | A4 bridge | Small program turning into two named functions | Keep scope small |
| 17 | Evidence | `.py` file, two function cards, output, explanation note | Keep documentation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students where Week 2 code repeated |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss why advanced topics wait |
| Repetition signal | 10 min | Use one repeated snippet | Have students mark repeated jobs |
| Demo 1 and 2 | 20 min | Run Demo 2 only | Compare before/after line by line |
| Parameters/returns | 12 min | Use box-and-arrow only | Trace values through one call |
| Demo 3 | 12 min | Name functions verbally | Ask students to label responsibilities |
| Assignment bridge | 20+ min | Provide one refactor target | Confer on function plans |
| Closing check | 4 min | Ask two questions verbally | Have students name two planned functions |

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
