# SLIDE DECK SOURCE - WEEK 2 DAY 3

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 2 / Thursday |
| Date | August 27, 2026 |
| Weekly Theme | Decision Logic and Repetition |
| Lecture Title | Combining Logic and Repetition |
| Assignments Supported | Assignment 2 - Decisions in Code; Assignment 3 - Loops and Repetition |
| Readiness Target | Students can build or fix a small logic-and-repetition program |
| Primary Watch Point | Do not let combined examples become too large for line-by-line reasoning |
| Source Version | v2 refactor |

---

# Session Purpose

This session combines the two main Week 2 control-flow ideas:

- decisions choose a path
- loops repeat a path

Students should see that combined logic is powerful, but it must stay small
enough to trace. The goal is not a full menu application. The goal is a small
program where the student can explain the condition, the repetition, the
update, and the stopping point.

---

# Review / Prior Work Bridge

Review from Week 2:

- Monday: conditions, comparisons, `if`, `elif`, `else`, and branch prediction.
- Tuesday: `for`, `while`, counters, accumulators, and stopping conditions.
- Assignment 2 asks students to build a small decision program.
- Assignment 3 asks students to build a small loop program.

Quick review questions:

- What condition is checked?
- Which branch runs?
- What repeats?
- What changes?
- What stops the loop?

Bridge into Day 3:

Today students combine decision and repetition patterns while keeping the
program small enough to explain.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 2
- textbook chapter area: **Conditionals and Iteration**

Day 3 reading focus:

- `break` and `continue`
- putting conditionals and loops together
- applying discounts or similar combined examples

Use this reading to support:

- menu-style logic
- repeated input patterns when introduced
- small programs that combine decisions and repetition

Today's reading boundary:

Students should not worry yet about advanced iterator behavior, generator
tools, compact one-line decisions, or large menu-driven applications.

---

# What We Will Use Today

Today we will use:

- conditions inside loops
- loops that depend on conditions
- simple validation patterns
- small menu-style recognition
- test values
- traceable output

Today we will skip for now and revisit later:

- large interactive applications
- nested loop-heavy designs
- advanced `break` / `continue` patterns
- data structures beyond simple values
- AI-generated combined programs

---

# Assignments Supported

Primary support:

- Assignment 2 - Decisions in Code
- Assignment 3 - Loops and Repetition

Day 3 should help students finish, test, revise, and explain both Week 2
assignments.

A2 completion target:

- a clear condition
- at least two possible outcomes
- output that matches the selected branch

A3 completion target:

- a loop that repeats intentionally
- clear stopping behavior
- output that proves repetition happened

---

# Readiness Target

By the end of the session, students should be able to:

- combine one condition with one loop pattern
- trace a program line by line without losing the path
- identify the branch condition
- identify the loop condition or range
- explain what changes during repetition
- test at least two outcomes or loop paths
- revise a program that became too large to explain

---

# Primary Watch Point

Combined logic can become confusing quickly.

The guardrail for this session is:

```text
If the student cannot trace the path, the program is too large.
```

Keep examples and assignment support focused on one condition and one
repetition pattern at a time.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_02_Decision_Logic_and_Repetition/07_input_loop_with_exit.py`
- `Demos/Week_02_Decision_Logic_and_Repetition/08_menu_with_conditionals.py`

Optional review demos:

- `Demos/Week_02_Decision_Logic_and_Repetition/03_discount_checker.py`
- `Demos/Week_02_Decision_Logic_and_Repetition/06_while_loop_countdown.py`

Recommended use:

1. Review one small decision or loop demo only if needed.
2. Use Demo 7 to show repeated input with an exit condition.
3. Use Demo 8 to show a small menu-style pattern.
4. Keep the demo discussion focused on traceability, not feature expansion.

---

# Student Hands-On Bridge

Students should use class time to finish or revise A2 and A3.

Recommended work sequence:

```text
1. Run the current version.
2. Test more than one path.
3. Explain what condition controls the branch.
4. Explain what repeats.
5. Explain what stops the loop.
6. Reduce scope if the program is hard to trace.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Reconnect choosing and repeating |
| Today's Working Set | 4-5 | Core | Bound integration and defer large application work |
| Combined Logic Model | 6-8 | Core | Show how conditions and loops work together |
| Validation and Menu Patterns | 9-12 | Core / Demo | Demonstrate repeated input and menu-style branching |
| Common Failures | 13-14 | Core | Prevent overbuilding and hidden infinite loops |
| Assignment Completion Bridge | 15-17 | Lab Bridge / Evidence | Close A2 and A3 with testing and explanation |
| Closing Check | 18 | Assessment / Evidence | Define Week 2 success |

---

# Slide-by-Slide Source

## Slide 1 - Choose And Repeat

**Delivery Category:** Review

**Student-Visible Text:**

This week, you learned two control-flow tools.

Decisions choose what happens. Loops repeat what happens.

Today, those ideas work together:

- a condition can choose a branch
- a loop can repeat a process
- a condition can also help decide when repetition stops

**Instructor Notes:**

Frame this as integration, not escalation. Students should feel that Thursday
uses familiar parts, even if the combination requires careful tracing.

**Transition Cue:**

Start by naming what Monday and Tuesday each contributed.

**Visual Notes:**

Use a branch icon and a loop icon flowing into one small program.

---

## Slide 2 - Monday Plus Tuesday

**Delivery Category:** Review

**Student-Visible Text:**

Monday: conditions choose branches.

Tuesday: loops repeat work.

Thursday's job is to keep both ideas explainable:

- What condition is checked?
- What repeats?
- What changes?
- What stops the process?

**Instructor Notes:**

Use this as a short retrieval practice moment. Ask students to answer these
questions verbally before showing any combined code.

**Transition Cue:**

The success target is still traceability.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

A combined program should still be traceable.

Use this path:

```text
input or value -> condition -> branch or loop -> update -> output
```

If the path is hard to explain, reduce the program.

**Instructor Notes:**

This is the guardrail slide. Integration can tempt students into building a
mini-application before the logic is stable.

**Transition Cue:**

Let's define today's working set.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- conditions inside loops
- loops controlled by conditions
- simple validation
- small menu-style logic
- test values and visible output

The goal is controlled combination, not feature count.

**Instructor Notes:**

This slide should help students see that combined logic has a bounded target.
It is not a license to build every possible feature.

**Transition Cue:**

Some tempting patterns are better saved for later.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip large interactive applications and complicated nested logic for
now.

Avoid adding features until the main path is clear.

Today, one condition plus one repetition pattern is enough for success.

**Instructor Notes:**

This is an important scope-control slide. Students who are eager may overbuild;
students who are anxious may think overbuilding is expected. Neither is the
goal.

**Transition Cue:**

Now let's see how a condition can control repetition.

---

## Slide 6 - Conditions Can Control Loops

**Delivery Category:** Core

**Student-Visible Text:**

A loop can use a condition to decide whether repetition should continue.

Example questions:

- Is the user done?
- Is the count still above zero?
- Is the input valid yet?
- Should the menu appear again?

**Instructor Notes:**

Connect this back to Monday's condition concept. The condition is still a
question, but now it can govern repetition.

**Transition Cue:**

Validation is one practical example of this pattern.

---

## Slide 7 - Validation Is Logic Plus Repetition

**Delivery Category:** Core

**Student-Visible Text:**

Validation often means repeating until the value is acceptable.

The pattern is:

- ask for a value
- check the value
- repeat if it is not acceptable
- continue when it is acceptable

This is logic and repetition working together.

**Instructor Notes:**

Keep validation conceptual unless the demo uses it directly. This is a strong
real-world anchor without needing a large program.

**Transition Cue:**

The first combined demo uses repeated input with an exit choice.

---

## Slide 8 - Demo 1: Input Loop With Exit

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the repeated prompt and the exit condition.

For each pass, identify:

- what input is requested
- what condition is checked
- whether the loop continues
- what value makes the loop stop

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/07_input_loop_with_exit.py`

If students are still shaky with `input()`, keep this demo short and focus on
the control-flow idea rather than input mechanics.

**Transition Cue:**

A menu is another common place where logic and repetition meet.

**Demo Connection:**

Primary demo file: `07_input_loop_with_exit.py`

---

## Slide 9 - Menu Logic Is A Pattern

**Delivery Category:** Core

**Student-Visible Text:**

A small menu program often repeats choices until the user exits.

The pattern is:

- show options
- get a choice
- use `if` / `elif` / `else`
- repeat or exit

The menu should stay small enough to explain line by line.

**Instructor Notes:**

Position menu logic as recognition and small practice, not as a demand that
students build a polished interface.

**Transition Cue:**

Let's watch the small menu pattern without expanding it too far.

---

## Slide 10 - Demo 2: Menu With Conditionals

**Delivery Category:** Demo

**Student-Visible Text:**

Watch how the menu combines two controls.

The loop controls repetition. The conditionals control the selected action.

Trace:

- the menu display
- the user's choice
- the matching branch
- the exit path

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/08_menu_with_conditionals.py`

Keep the menu small. Avoid adding options live unless students are clearly
ready. The purpose is structure, not feature count.

**Transition Cue:**

The more combined logic we add, the more important tracing becomes.

**Demo Connection:**

Primary demo file: `08_menu_with_conditionals.py`

---

## Slide 11 - Trace The Whole Path

**Delivery Category:** Core

**Student-Visible Text:**

Combined logic should be traced as a path.

For one run of the program, write or say:

- the starting value or input
- the condition checked
- the branch selected
- the loop update
- the final output

Tracing keeps the program understandable.

**Instructor Notes:**

This slide ties Thursday to later debugging and testing habits. A student who
can trace combined logic can usually find mistakes faster.

**Transition Cue:**

Testing should include more than the happy path.

---

## Slide 12 - Test More Than One Path

**Delivery Category:** Core

**Student-Visible Text:**

One successful run is not enough evidence.

For Week 2 work, test:

- a value that triggers one branch
- a value that triggers another branch
- a loop that runs more than once
- a value or choice that stops the loop

Testing proves that control flow behaves as intended.

**Instructor Notes:**

This bridges A2 and A3 evidence expectations. Keep it practical and small. Do
not turn this into formal testing syntax.

**Transition Cue:**

Two common failures show up when programs combine too much too soon.

---

## Slide 13 - Common Failure: Too Much At Once

**Delivery Category:** Core

**Student-Visible Text:**

Too many features can break understanding.

If the program is hard to trace, reduce it.

Good Week 2 scope:

- one clear decision
- one clear loop
- visible output
- a short explanation

**Instructor Notes:**

Normalize reducing scope as a smart development move. This connects with the
course's broader revision/recovery philosophy.

**Transition Cue:**

The second failure is hiding the stop condition.

---

## Slide 14 - Common Failure: Hidden Stop Logic

**Delivery Category:** Core

**Student-Visible Text:**

A loop should not hide its stopping point.

Before submitting, ask:

- What makes the loop continue?
- What makes the loop stop?
- Can the stop condition actually happen?
- Can I explain it without guessing?

**Instructor Notes:**

This reinforces Tuesday's infinite-loop prevention and applies it to combined
programs.

**Transition Cue:**

Now move from demo thinking into assignment completion.

---

## Slide 15 - Finish A2: Decisions In Code

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 2, check that your decision program has:

- one clear condition
- at least two possible outcomes
- output that matches the selected branch
- variable names that make the decision readable

Be ready to explain why each branch runs.

**Instructor Notes:**

Use this as a targeted completion checklist. Students should not add loops to
A2 unless approved or unless their design remains explainable.

**Transition Cue:**

Now check the loop assignment.

**Lab Connection:**

Closes Assignment 2 - Decisions in Code.

---

## Slide 16 - Finish A3: Loops And Repetition

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 3, check that your loop program has:

- one repeated action
- a clear update or advance
- a clear stopping point
- output that proves repetition happened

Be ready to explain the first pass, one middle pass, and the stopping moment.

**Instructor Notes:**

If students have a loop that works but cannot explain it, use the
repeat/change/stop pattern from Day 2 to recover the logic.

**Transition Cue:**

Both submissions need evidence, not just code.

**Lab Connection:**

Closes Assignment 3 - Loops and Repetition.

---

## Slide 17 - Evidence For Week 2

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Week 2 submissions should show both working code and reasoning.

Useful evidence:

- working `.py` files
- visible output
- more than one test value or path
- explanation of the decision
- explanation of the loop stopping point

The explanation proves that the code is yours to understand.

**Instructor Notes:**

Keep the evidence expectation concrete and light. This is not yet a large
documentation assignment, but the reasoning habit matters.

**Transition Cue:**

The final Week 2 question is whether the path is traceable.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Week 2 worked if you can trace the path.

For a small program, you should be able to explain:

- what value starts the logic
- what condition is checked
- what branch runs
- what repeats
- what changes
- what stops the loop

If you can explain that, the program is small enough and clear enough.

**Instructor Notes:**

Close Week 2 around traceability. This prepares students for Week 3, where
functions and data structures will begin organizing code and data more
intentionally.

**Transition Cue:**

Next week, we begin organizing code and data so programs are easier to grow and
explain.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one A2 branch example.
2. Review one A3 loop example only if needed.
3. Run `07_input_loop_with_exit.py`.
4. Identify input, condition, repeat path, and stop path.
5. Run `08_menu_with_conditionals.py`.
6. Trace one menu choice and one exit choice.
7. Use Slides 15-17 as student work checklists.
8. Give students substantial time to finish and ask questions.

Instructor pacing note:

If students are still shaky on A2 or A3 individually, do not spend too long on
the combined demos. The main instructional win is finishing Week 2 work with
clear reasoning.

---

# Lab / Assignment Bridge

By the end of Day 3, students should submit or be ready to submit both Week 2
assignments.

Minimum closure target:

- A2 decision program runs
- A2 has at least two possible outcomes
- A3 loop program runs
- A3 loop stops intentionally
- student can explain one tested path for each assignment

---

# README / Submission Expectations

Suggested student evidence:

- clear `.py` filenames
- code that runs without syntax errors
- visible output
- more than one test value or path where appropriate
- short A2 explanation: what condition is checked and what outcomes can happen
- short A3 explanation: what repeats and how the program knows when to stop

If using GitHub, students should keep the code and explanation together. Do not
let documentation mechanics obscure the logic and loop reasoning.

---

# AI-Use Boundary

AI is not allowed for normal A2 or A3 work unless the instructor explicitly
says otherwise.

Reason:

Students need manual-first practice with:

- conditions
- branch prediction
- loop tracing
- stopping conditions
- small-program explanation

If AI is allowed later for review, students must still explain the logic and
verify the output themselves.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Choose and repeat | Branch icon and loop icon joining into one small Python file | Avoid large app imagery |
| 2 | Monday plus Tuesday | Two-column recap: decisions choose, loops repeat | Keep text readable |
| 3 | Traceable path | Input/value flowing through condition, branch/loop, update, output | Avoid dense flowchart |
| 4 | Today's tools | Toolbox with condition-in-loop, loop-by-condition, validation, test values | Avoid advanced data structures |
| 5 | Scope control | One clear condition plus one loop versus cluttered feature list | Keep tone supportive |
| 7 | Validation loop | Invalid input repeats, valid input exits | Avoid security/password imagery |
| 8 | Input loop demo | Repeated prompt with exit condition highlighted | Make exit path visible |
| 9 | Menu pattern | Show options, get choice, branch, repeat/exit cycle | Keep menu small |
| 10 | Menu demo | User choice flowing to matching branch and exit option | Avoid too many choices |
| 11 | Trace path | One highlighted route through combined logic | Do not show full code wall |
| 12 | Test paths | Multiple small test cards: branch A, branch B, repeat, stop | Avoid formal test-framework imagery |
| 13 | Too much at once | Split visual: small traceable program vs cluttered mini-app | Do not shame ambition |
| 14 | Stop logic | Loop cycle with stop condition spotlighted | Avoid warning-heavy design |
| 17 | Week 2 evidence | Two `.py` files, output samples, short explanation notes | Keep documentation lightweight |
| 18 | Week 2 success | Traceable path checklist from value to output | Keep checklist readable |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students to answer all trace questions |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss scope reduction as a strength |
| Combined logic model | 12 min | Use Slides 6 and 7 only | Have students sketch a validation loop |
| Demo 1 | 12 min | Run one input path only | Trace continue and exit paths |
| Demo 2 | 12 min | Skip if A2/A3 need time | Trace multiple menu choices |
| Testing and failures | 12 min | Use Slides 12 and 14 only | Have students identify hidden stop logic |
| Assignment completion | 30+ min | Use checklists only | Confer individually on A2/A3 |
| Closing check | 5 min | Ask final trace questions verbally | Have students explain one submitted path |

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
