# SLIDE DECK SOURCE - WEEK 2 DAY 1

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 2 / Monday |
| Date | August 24, 2026 |
| Weekly Theme | Decision Logic and Repetition |
| Lecture Title | How Programs Make Decisions |
| Assignments Supported | Assignment 2 - Decisions in Code |
| Readiness Target | Students can predict which branch runs and explain why |
| Primary Watch Point | Keep examples small; do not mix in loop complexity yet |
| Source Version | v2 refactor |

---

# Session Purpose

This session introduces decision logic as the first major step beyond programs
that run straight from top to bottom.

Students should understand that a condition asks a question, Python evaluates
that question as `True` or `False`, and the program uses that result to choose
which block of code runs.

The target is not complex business logic. The target is branch prediction:

```text
condition is checked -> branch is selected -> output reflects the decision
```

---

# Review / Prior Work Bridge

Review from Week 1:

- Python follows instructions in order.
- Variables hold values that can be used later.
- Expressions can produce new values.
- `print()` makes the result visible.
- Assignment 1 required small programs that run and can be explained.

Quick review questions:

- What value does the program start with?
- What line changes or calculates a value?
- What output does the user see?
- Can you explain why that output appears?

Bridge into Week 2:

Last week, most programs followed one path. Today the program begins choosing
between paths.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 2
- textbook chapter area: **Conditionals and Iteration**

Day 1 reading focus:

- conditional programming
- the `if` statement
- `elif`
- `else`
- nesting `if` statements

Use this reading to support:

- branch prediction
- small decision programs
- explaining why a branch runs

Today's reading boundary:

Students should not worry yet about pattern matching, the ternary operator,
advanced iterators, assignment expressions, the walrus operator, or generator
tools.

---

# What We Will Use Today

Today we will use:

- boolean values: `True` and `False`
- comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=`
- `if`
- `elif`
- `else`
- branch prediction
- small test values

Today we will skip for now and revisit later:

- loops
- repeated input
- `break` and `continue`
- pattern matching
- compact one-line conditional expressions
- AI-generated decision logic

---

# Assignments Supported

Primary support:

- Assignment 2 - Decisions in Code

Assignment 2 asks students to build one small decision-based program.

Possible options include:

- grade checker
- discount checker
- eligibility checker
- simple recommendation tool
- temperature or weather-message program
- login-style rule checker using sample values

Today's lecture should make students ready to start A2 without inflating the
assignment into a large application.

---

# Readiness Target

By the end of the session, students should be able to:

- identify the value being checked
- identify the comparison being made
- predict whether the condition is `True` or `False`
- predict which branch runs
- change a test value and predict the new output
- explain the result in plain language

---

# Primary Watch Point

The main risk is moving too quickly from a single `if` statement into nested or
combined logic.

Students need enough time to see that:

- `=` stores a value
- `==` compares values
- a condition produces `True` or `False`
- indentation controls which statements belong to a branch
- only the selected branch runs

If students cannot predict a branch before running the code, the example is too
large for this moment.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_02_Decision_Logic_and_Repetition/01_booleans_comparisons.py`
- `Demos/Week_02_Decision_Logic_and_Repetition/02_if_elif_else_grade_check.py`

Optional bridge demo:

- `Demos/Week_02_Decision_Logic_and_Repetition/03_discount_checker.py`

Recommended use:

1. Use Demo 1 to show comparisons producing `True` / `False`.
2. Use Demo 2 to show one selected branch in a multi-branch program.
3. Use Demo 3 only if students are ready to see a practical A2-style pattern.

---

# Student Hands-On Bridge

Students should begin Assignment 2 by choosing one small decision problem and
writing a few test values before coding too much.

The first working version can use fixed sample values. User input is optional
unless the instructor requires it.

Suggested start:

```text
1. Name the decision.
2. Name the value being checked.
3. Write the condition.
4. Predict the output for two or three values.
5. Code the smallest working version.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect Week 1 value flow to Week 2 branching |
| Today's Working Set | 4-5 | Core | Name what students use and what they can defer |
| Boolean and Comparison Model | 6-8 | Core | Show conditions as questions with True/False answers |
| Branch Structure | 9-12 | Core / Demo | Introduce `if`, `elif`, `else`, indentation, and selected branches |
| Common Failures | 13-14 | Core | Prevent assignment/comparison and indentation confusion |
| Assignment 2 Bridge | 15-16 | Lab Bridge / Evidence | Start A2 with small test values and explanation |
| Closing Check | 17 | Assessment / Evidence | Define successful branch prediction |

---

# Slide-by-Slide Source

## Slide 1 - Programs Can Choose

**Delivery Category:** Review

**Student-Visible Text:**

Last week, most programs followed one path from top to bottom.

This week, programs begin choosing between possible paths.

Decision logic lets a program react to the data it has.

Today, watch for:

- the value being checked
- the condition being tested
- the output that happens because of the result

**Instructor Notes:**

Use this as the conceptual jump from Week 1 to Week 2. The point is not that
students are starting over. They are reusing values, expressions, and output,
but now the program can decide which output should appear.

**Transition Cue:**

Before the program can choose, it needs a value to check.

**Visual Notes:**

Use a straight path from Week 1 that splits into two visible branches for Week
2.

---

## Slide 2 - Week 1 Becomes Week 2

**Delivery Category:** Review

**Student-Visible Text:**

Week 1 gave us values and visible output.

Week 2 adds questions that choose which output should happen.

A decision program still uses the same basic pieces:

- variables hold values
- comparisons ask questions about those values
- `print()` shows the result of the chosen path

**Instructor Notes:**

Ask students to name one Week 1 value example: score, price, age, temperature,
or quantity. Then ask what question a program might ask about that value.

Examples:

- Is the score passing?
- Is the purchase large enough for a discount?
- Is the age old enough?

**Transition Cue:**

Those questions become conditions.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Condition checked -> branch selected -> output shown.

If you can predict that path, you understand the decision logic.

For every decision program, practice asking:

- What condition is checked?
- Is the condition `True` or `False`?
- Which branch runs?
- What output should appear?

**Instructor Notes:**

Install this pattern early and return to it all day. It gives students a
simple mental model for reading decision code.

**Transition Cue:**

Let's name the specific tools we will use today.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- `True` and `False`
- comparisons such as `>=`, `==`, and `!=`
- `if`, `elif`, and `else`
- branch prediction before running the code

These tools are enough to build a small decision program.

**Instructor Notes:**

Keep this as the working set. Students will see that conditionals are built
from a small group of pieces, not a giant new language.

**Transition Cue:**

Just as important, several topics can wait.

**Visual Notes:**

Use a small toolbox visual with boolean values, comparison symbols, and branch
keywords.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip loops, repeated input, pattern matching, and compact one-line
conditionals for now.

Today's job is to understand one decision path clearly.

That means the program should be small enough that you can trace:

- the starting value
- the condition
- the branch
- the final output

**Instructor Notes:**

The reading may include more material than today's lecture needs. This slide
protects cognitive load. Loops arrive tomorrow, but they should not compete
with first-contact branching.

**Transition Cue:**

The first decision tool is the boolean value.

---

## Slide 6 - Conditions Ask Questions

**Delivery Category:** Core

**Student-Visible Text:**

A condition is a question the program can answer as `True` or `False`.

Example: `score >= 70`

Read the condition in plain language:

- Is the score greater than or equal to 70?
- If yes, the result is `True`.
- If no, the result is `False`.

**Instructor Notes:**

Translate comparisons into spoken questions:

- Is the score greater than or equal to 70?
- Is the age at least 16?
- Is the password attempt equal to the sample value?

The spoken question helps students see code as meaning, not symbols only.

**Transition Cue:**

Now we need the comparison symbols that create those answers.

---

## Slide 7 - Comparison Operators

**Delivery Category:** Core

**Student-Visible Text:**

Comparisons create boolean results.

`>`, `<`, `>=`, `<=`, `==`, and `!=`

Common readings:

- `>=` means greater than or equal to
- `==` means equal to
- `!=` means not equal to

These do not print by themselves unless you ask Python to show the result.

**Instructor Notes:**

Do not rush past `==` and `!=`. Students will recognize some symbols from
math, but `==` is a programming-specific adjustment for many beginners.

Use two or three concrete examples:

```python
age >= 16
score == 100
status != "closed"
```

**Transition Cue:**

Let's see comparisons produce visible `True` and `False` values.

---

## Slide 8 - Demo 1: Boolean Comparisons

**Delivery Category:** Demo

**Student-Visible Text:**

Before running each comparison, predict the result.

Will Python answer `True` or `False`?

For each line, identify:

- the value being checked
- the comparison operator
- the expected boolean result

Then run the program to confirm your prediction.

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/01_booleans_comparisons.py`

Run once as written. Then change one value at a time:

- `age`
- `minimum_age`
- `score`
- `passing_score`

Ask students to predict the boolean result before running the file again.

**Transition Cue:**

A boolean result becomes more useful when it controls a branch.

**Demo Connection:**

Primary demo file: `01_booleans_comparisons.py`

---

## Slide 9 - The `if` Statement

**Delivery Category:** Core

**Student-Visible Text:**

`if` means: run this block only when the condition is `True`.

The condition decides whether the indented code runs.

Basic shape:

```python
if condition:
    do_this()
```

The indented line belongs to the branch.

**Instructor Notes:**

Point directly at indentation. Beginners often understand the condition but
miss that indentation controls the branch body.

Use a tiny structure:

```python
if score >= 70:
    print("Passing")
```

**Transition Cue:**

When there are multiple possible outcomes, we can add more branches.

---

## Slide 10 - `elif` and `else`

**Delivery Category:** Core

**Student-Visible Text:**

`elif` checks another condition.

`else` handles what is left when earlier conditions did not run.

Use this structure when there are multiple possible outcomes:

- `if` starts the decision
- `elif` adds another possible condition
- `else` catches the remaining case

**Instructor Notes:**

Explain `elif` as "else if" in plain language. Keep `else` simple: it is the
fallback branch.

Stress that Python checks from top to bottom and stops once a matching branch
is selected in the chain.

**Transition Cue:**

The next demo shows why prediction matters before running the code.

---

## Slide 11 - Demo 2: Grade Check Branches

**Delivery Category:** Demo

**Student-Visible Text:**

Change the score.

Predict the grade branch before running the program.

For each score, explain:

- which condition is checked first
- which condition becomes true
- which grade is printed
- why later branches do or do not run

**Instructor Notes:**

Use:

`Demos/Week_02_Decision_Logic_and_Repetition/02_if_elif_else_grade_check.py`

Suggested test values:

- `95`
- `84`
- `72`
- `59`
- boundary values such as `90`, `80`, `70`, and `60`

Pause before each run and ask: which branch should run, and why?

**Transition Cue:**

The order of the branches matters because Python reads the chain from top to
bottom.

**Demo Connection:**

Primary demo file: `02_if_elif_else_grade_check.py`

---

## Slide 12 - Branch Order Matters

**Delivery Category:** Core

**Student-Visible Text:**

Python checks a branch chain from top to bottom.

The first matching branch wins.

Order matters when more than one condition could be true.

Place the most specific or highest-priority checks where they belong in the
chain.

**Instructor Notes:**

This prevents a major beginner mistake. If a broad condition appears before a
more specific one, the specific branch may never run.

Use a verbal example before code:

```text
If a score is at least 60, it is also at least 70? No.
If a score is at least 95, it is also at least 90? Yes.
So the order must match the intended logic.
```

**Transition Cue:**

Two common syntax problems can hide this logic from students.

---

## Slide 13 - Common Failure: `=` Is Not `==`

**Delivery Category:** Core

**Student-Visible Text:**

`=` stores a value.

`==` compares two values.

Example:

```python
score = 84     # store the value
score == 84    # ask if the value matches
```

Mixing these up changes the meaning of the program.

**Instructor Notes:**

Keep this blunt and memorable. Connect it back to Week 1:

- `score = 84` stores a value.
- `score == 84` asks whether the value matches.

This is one of the highest-value beginner warnings for Week 2.

**Transition Cue:**

The second common failure is indentation.

**Visual Notes:**

Use a split visual: assignment on one side, comparison on the other.

---

## Slide 14 - Common Failure: Indentation Changes Meaning

**Delivery Category:** Core

**Student-Visible Text:**

Indented lines belong to the branch.

Unindented lines run after the branch is finished.

In Python, indentation is structure.

When reading a branch, ask:

- Which lines are inside the branch?
- Which lines run no matter what?

**Instructor Notes:**

Show a tiny before/after example if helpful. Students may think indentation is
only formatting. In Python, it defines structure.

Recommended phrasing:

```text
Indentation is not decoration. It tells Python what belongs together.
```

**Transition Cue:**

Now we can connect the idea to Assignment 2.

---

## Slide 15 - Assignment 2 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 2, build one small program that makes a clear decision.

Start with two or three test values before adding more features.

A good first version should include:

- one main value to check
- at least one comparison
- at least two possible outputs
- readable variable names

**Instructor Notes:**

Point students toward manageable options:

- grade checker
- eligibility checker
- temperature message
- simple recommendation
- sample login-style rule checker

If using the discount checker demo, clarify that students should not simply
submit the demo. They should use the pattern in a different small decision
problem or an approved variation.

**Transition Cue:**

A decision program is only clear if it can be tested with more than one value.

**Lab Connection:**

Supports Assignment 2 - Decisions in Code.

---

## Slide 16 - Evidence For A Decision Program

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should show at least two possible outcomes.

Be ready to explain what condition is checked and why each branch runs.

Useful evidence includes:

- a working `.py` file
- sample values or scenarios
- visible output
- a short explanation of the decision

**Instructor Notes:**

Recommended evidence:

- one working `.py` file
- readable variable names
- visible output
- two or more test values or scenarios
- brief explanation of the checked condition and possible outcomes

Keep README expectations light if this is still early in GitHub practice.

**Transition Cue:**

Before students begin, show one optional practical bridge if the class is ready.

---

## Slide 17 - Optional Demo: Practical Decision Pattern

**Delivery Category:** Reserve

**Student-Visible Text:**

A practical decision program still follows the same pattern:

check a condition -> choose a branch -> show the result.

In the demo, watch how the program:

- checks the purchase total
- decides whether a discount applies
- calculates the final total only when needed
- prints a result that matches the decision

**Instructor Notes:**

Use only if students are ready:

`Demos/Week_02_Decision_Logic_and_Repetition/03_discount_checker.py`

This demo bridges toward A2, but it should not become the only model students
can imagine. Ask them to name other decision contexts after the demo.

**Transition Cue:**

The closing check is whether they can predict the branch before running code.

**Demo Connection:**

Optional demo file: `03_discount_checker.py`

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can predict the branch and explain the output, you understand the logic.

Run the code to confirm your reasoning, not to replace it.

Before submitting A2, test your program with:

- one value that should trigger the first branch
- one value that should trigger another branch
- one boundary value if your decision has a cutoff

**Instructor Notes:**

Close with branch prediction as the day's success measure.

Ask:

- What value is being checked?
- What condition is being tested?
- Is the condition `True` or `False`?
- Which branch runs?
- What output should appear?

**Transition Cue:**

Next session, the program will not only choose. It will repeat.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one Week 1 value flow example.
2. Run `01_booleans_comparisons.py`.
3. Change one value and ask for `True` / `False` predictions.
4. Introduce the `if` block shape and indentation.
5. Run `02_if_elif_else_grade_check.py`.
6. Test boundary values and ask which branch should run.
7. Show `=` versus `==` explicitly.
8. If time allows, show `03_discount_checker.py` as the practical bridge.
9. Move students into A2 setup with small test values.

Instructor pacing note:

Do not use all three demos if students need more time with the first two. Demo
3 is valuable, but the A2 launch matters more.

---

# Lab / Assignment Bridge

By the end of the session, students should have started Assignment 2 or have a
clear plan for it.

Minimum A2 start target:

- one selected decision problem
- one variable/value being checked
- one condition
- two or three planned test values
- expected output for each planned test value

---

# README / Submission Expectations

Keep documentation expectations early and practical.

Suggested student evidence:

- clear `.py` filename
- code that runs without syntax errors
- visible output
- at least two scenarios or test values
- short answer to: "What condition does your program check, and what different
  outcomes can happen?"

If using GitHub, remind students that code and explanation should live together
as a habit, but do not let repository mechanics become the center of the
decision-logic assignment.

---

# AI-Use Boundary

AI is not allowed for normal Assignment 2 work unless the instructor explicitly
says otherwise.

Reason:

Students need manual-first practice with:

- writing a condition
- tracing `True` / `False`
- predicting a branch
- changing test values
- explaining why output changes

AI may be used later for explanation or review when permitted, but it should
not replace the first manual encounter with branching logic.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Straight path becomes branch | A simple path from a Python file that splits into two possible output paths | Avoid complex flowcharts |
| 3 | Success pattern | Three-step flow: condition checked, branch selected, output shown | Keep text readable |
| 4 | Today's tools | Toolbox with `True`, `False`, comparison symbols, `if`, `elif`, `else` | Avoid adding loops |
| 5 | Deferred topics | Parked-for-later area with loops, repeated input, pattern matching | Do not imply topics are unimportant |
| 6 | Condition as question | Question mark over `score >= 70`, producing `True` or `False` cards | Keep beginner-friendly |
| 7 | Comparison symbols | Six comparison operators arranged as small cards with one example each | Avoid math-heavy layout |
| 9 | If block shape | Condition line with indented branch body highlighted | Make indentation visually obvious |
| 11 | Branch prediction | Score value flowing into grade-check branches with one highlighted path | Do not show too many branches at once |
| 13 | Equals comparison contrast | `=` as storage and `==` as comparison in side-by-side panels | Avoid making this look like an error message only |
| 14 | Indentation | Indented code block visually grouped under an `if` statement | Do not use dense code |
| 15 | Assignment bridge | Small decision-program options as cards: grade, eligibility, weather, recommendation | Avoid making one option look required |
| 16 | Evidence | `.py` file plus two test values and short explanation note | Keep documentation lightweight |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students to trace one A1 value flow |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss textbook topics to defer |
| Boolean model | 12 min | Use one comparison example | Ask students to write spoken questions |
| Demo 1 | 10 min | Run as written only | Change values and predict outcomes |
| Branch structure | 12 min | Use Slides 9 and 10 only | Type a tiny `if` block live |
| Demo 2 | 15 min | Use two score values | Test boundary values |
| Common failures | 8 min | Mention indentation verbally | Show broken and corrected snippets |
| Assignment bridge | 15+ min | Skip optional demo | Help students choose A2 scope |
| Closing check | 4 min | Ask two questions verbally | Have students explain one branch aloud |

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
