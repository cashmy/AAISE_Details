# SLIDE DECK SOURCE - WEEK 4 DAY 3

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 4 / Thursday |
| Date | September 10, 2026 |
| Weekly Theme | Debugging, Testing, and Reading Structured Code |
| Lecture Title | Validation, Testing, and Justifying a Fix |
| Assignments Supported | Assignment 6 - Debug and Explain; Assignment 7 - Reading Structured Code |
| Readiness Target | Students can show simple validation evidence and explain why a fix works |
| Primary Watch Point | Pytest is recognition-plus-light-practice only; do not accidentally make it a hidden required syntax target |
| Source Version | v2 refactor |

---

# Session Purpose

This session closes Week 4 by connecting repair, validation, and explanation.

Students should understand that a fix is stronger when it is checked. They do
not need full testing-tool mastery yet, but they do need evidence that the
program now behaves as intended.

The target pattern is:

```text
fix -> check expected behavior -> record evidence -> justify why the fix works
```

---

# Review / Prior Work Bridge

Review from Week 4:

- Monday: debugging uses evidence before repair
- Tuesday: structured code can be read by identifying parts
- A6 requires bug diagnosis, repair, evidence, and explanation
- A7 requires structured-code reading, a small modification, and explanation

Quick review questions:

- What was the bug or structural issue?
- What evidence showed the problem?
- What changed?
- How do you know the change worked?

Bridge into Day 3:

Today students learn to make a repair believable by showing checks and
explaining the result.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 4
- textbook chapter areas: **Testing** and **Debugging and Profiling**

Day 3 reading focus:

- testing your application
- test-driven development as a concept
- debugging techniques review

Use this reading to support:

- simple test cases
- expected output checks
- pytest recognition
- explaining why a fix works

Today's reading boundary:

Students should not worry yet about test-driven development as a required
workflow, pytest syntax mastery, mocking, profiling, full OOP design, or
professional testing architecture.

---

# What We Will Use Today

Today we will use:

- expected-versus-actual checks
- simple test cases
- boolean check output
- optional `assert`
- pytest recognition
- repair justification
- Week 4 submission evidence

Today we will skip for now and revisit later:

- required pytest mastery
- mocking as a requirement
- full test suites
- performance profiling
- test-driven development workflow

---

# Assignments Supported

Primary support:

- Assignment 6 - Debug and Explain
- Assignment 7 - Reading Structured Code

Day 3 should help students finish, validate, and explain both assignments.

A6 completion target:

- corrected code
- evidence of the bug
- evidence that the fix works
- explanation of the repair

A7 completion target:

- modified structured example
- class/function parts identified
- comparison explanation
- evidence that the modification runs

---

# Readiness Target

By the end of the session, students should be able to:

- create simple expected-versus-actual checks
- use multiple test values
- recognize what `assert` does
- recognize pytest as a professional testing tool
- avoid treating pytest as a hidden requirement
- explain what validation evidence supports a fix
- finish A6 and A7 with code plus reasoning

---

# Primary Watch Point

The main risk is scope creep into testing syntax.

Use this boundary:

```text
Required: show evidence that the fix works.
Optional/exposure: pytest syntax and professional test tooling.
```

If pytest is shown, repeatedly state whether it is required or only a
recognition-level demonstration.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/04_simple_test_cases.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/05_assert_basics.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/11_pytest_unit_tests_demo.py`

Optional review demos:

- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/03_logic_bug_fixed.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/08_class_based_task_tracker.py`

Recommended use:

1. Use Demo 4 for simple print-based checks.
2. Use Demo 5 only if students are ready for `assert`.
3. Use Demo 11 as pytest recognition, not a new required syntax target.

---

# Student Hands-On Bridge

Students should use class time to finish A6 and A7 with evidence.

Recommended work sequence:

```text
1. Run the corrected or modified code.
2. Check more than one value or path.
3. Record what was expected.
4. Record what actually happened.
5. Explain why the result supports the fix or modification.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect diagnosis, structure reading, and validation |
| Today's Working Set | 4-5 | Core | Bound testing topics and defer pytest mastery |
| Simple Validation | 6-9 | Core / Demo | Teach expected/actual checks and multiple cases |
| Assert and Pytest Recognition | 10-12 | Demo / Core | Show testing progression without hidden requirement |
| Justification | 13-14 | Core | Connect checks to believable repair claims |
| Assignment Closeout | 15-17 | Lab Bridge / Evidence | Close A6 and A7 with submission evidence |
| Closing Check | 18 | Assessment / Evidence | Define successful validation and explanation |

---

# Slide-by-Slide Source

## Slide 1 - A Fix Is Stronger When It Is Checked

**Delivery Category:** Review

**Student-Visible Text:**

A fix is not complete just because the error disappeared.

A believable fix has evidence.

Today, focus on:

- what changed
- what was checked
- what evidence supports the result
- how you explain the fix or modification

**Instructor Notes:**

Frame validation as part of repair, not an extra chore.

**Transition Cue:**

Monday found evidence. Today proves the repair.

**Visual Notes:**

Use a simple bug -> fix -> check progression.

---

## Slide 2 - Evidence, Repair, Validation

**Delivery Category:** Review

**Student-Visible Text:**

Week 4 follows a professional pattern:

- gather evidence
- repair or modify
- validate behavior
- explain the result

Validation is how you move from "I think it works" to "I checked that it
works."

**Instructor Notes:**

Connect directly back to A6 and A7. This is the week closeout logic.

**Transition Cue:**

One successful run is not enough evidence.

---

## Slide 3 - One Run Is Not Enough

**Delivery Category:** Core

**Student-Visible Text:**

One successful run may only prove one path.

Better evidence checks more than one case:

- normal value
- boundary value
- value that should fail or choose another path
- modified behavior after a change

More checks create stronger confidence.

**Instructor Notes:**

Keep this practical. The goal is not formal test coverage, but students should
see why one run can miss problems.

**Transition Cue:**

Let's name today's testing and validation tools.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- expected-versus-actual checks
- simple test cases
- multiple values
- optional `assert`
- pytest recognition
- repair justification

These tools help us support claims about code behavior.

**Instructor Notes:**

Keep the distinction between required evidence and optional tooling visible.

**Transition Cue:**

Some testing topics are intentionally saved for later.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip required pytest mastery, mocking, full test suites, profiling, and
test-driven development workflow for now.

Today's required target is:

- show the check
- explain the repair
- justify why the result is believable

**Instructor Notes:**

This protects students from assuming pytest is now a hidden grading target.

**Transition Cue:**

Start with the simplest useful check.

---

## Slide 6 - Expected Behavior Can Be Checked

**Delivery Category:** Core

**Student-Visible Text:**

Expected behavior can be checked with simple output.

Example pattern:

```text
Input: 69
Expected: False
Actual: False
Result: matches
```

The check should connect directly to the behavior you are claiming.

**Instructor Notes:**

Use expected-vs-actual as the bridge from debugging to validation.

**Transition Cue:**

Now watch a few simple cases check one function.

---

## Slide 7 - Demo 1: Simple Test Cases

**Delivery Category:** Demo

**Student-Visible Text:**

Watch one function checked with several values.

Trace:

- input value
- expected result
- actual result
- whether the result matches

Different values can reveal different problems.

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/04_simple_test_cases.py`

Keep this print-based and readable.

**Transition Cue:**

Some checks can stop the program when a claim is false.

**Demo Connection:**

Primary demo file: `04_simple_test_cases.py`

---

## Slide 8 - Boundaries Matter

**Delivery Category:** Core

**Student-Visible Text:**

Boundary values often reveal logic mistakes.

For a passing score rule, useful checks include:

- `90` should pass
- `70` should pass
- `69` should not pass

The cutoff value is where mistakes often hide.

**Instructor Notes:**

This builds testing judgment without formal tooling.

**Transition Cue:**

`assert` is one lightweight way to express expected behavior.

---

## Slide 9 - Optional Demo: Assert Basics

**Delivery Category:** Demo

**Student-Visible Text:**

`assert` checks whether a statement is true.

If the statement is false, Python raises an error.

Use it as a lightweight check, not as a new assignment burden unless your
instructor requires it.

**Instructor Notes:**

Use only if students are ready:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/05_assert_basics.py`

Clarify whether `assert` is required. By default here, it is exposure/light
practice.

**Transition Cue:**

Professional tools use the same idea in a more repeatable form.

**Demo Connection:**

Optional demo file: `05_assert_basics.py`

---

## Slide 10 - Testing Tool Progression

**Delivery Category:** Core

**Student-Visible Text:**

Validation can grow over time.

Beginner progression:

- expected-versus-actual print checks
- `assert` checks
- pytest recognition
- later: full test suites and professional workflows

The idea is the same: check behavior against an expectation.

**Instructor Notes:**

This positions pytest as a future-facing tool without overloading A6/A7.

**Transition Cue:**

Now look at pytest as recognition-level exposure.

---

## Slide 11 - Demo 2: Pytest Recognition

**Delivery Category:** Demo

**Student-Visible Text:**

Pytest is a professional tool for repeatable checks.

Today, recognize:

- test function names
- input values
- expected results
- assertion statements
- pass/fail output

You are not expected to master pytest syntax today unless instructed.

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/11_pytest_unit_tests_demo.py`

Run with:

```text
python -m pytest 11_pytest_unit_tests_demo.py
```

State explicitly that this is recognition-plus-light-practice unless you decide
otherwise.

**Transition Cue:**

Testing evidence supports a claim about the repair.

**Demo Connection:**

Recognition demo file: `11_pytest_unit_tests_demo.py`

---

## Slide 12 - Common Failure: Tool Confusion

**Delivery Category:** Core

**Student-Visible Text:**

Do not confuse the tool with the goal.

The goal is not "use the fanciest testing tool."

The goal is:

- identify expected behavior
- check actual behavior
- record useful evidence
- explain why the result supports your claim

**Instructor Notes:**

This prevents pytest from becoming a prestige target.

**Transition Cue:**

Now turn evidence into a justification.

---

## Slide 13 - Explain Why The Fix Works

**Delivery Category:** Core

**Student-Visible Text:**

A good fix explanation connects evidence to the change.

Use this pattern:

- The bug was...
- I found it because...
- I changed...
- I checked...
- The result shows...

This makes the repair believable.

**Instructor Notes:**

This is directly aligned to A6 reflection and A7 modification explanation.

**Transition Cue:**

The check and the explanation belong together.

---

## Slide 14 - Show The Check, Explain The Repair

**Delivery Category:** Core

**Student-Visible Text:**

Evidence without explanation is incomplete.

Explanation without evidence is weak.

Strong submissions include:

- corrected or modified code
- visible check or output
- short explanation of what changed
- reason the result is acceptable

**Instructor Notes:**

Bridge to submissions. Students should not submit only code when reasoning is
part of the grade.

**Transition Cue:**

Now close A6.

---

## Slide 15 - Finish A6: Debug And Explain

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 6, check that your submission includes:

- corrected `.py` file
- at least one debugging clue
- expected-vs-actual or test evidence
- explanation of the bug
- explanation of why the fix works

**Instructor Notes:**

Use this as an A6 closeout checklist. Keep pytest optional unless explicitly
required.

**Transition Cue:**

Now close A7.

**Lab Connection:**

Closes Assignment 6 - Debug and Explain.

---

## Slide 16 - Finish A7: Reading Structured Code

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 7, check that your submission includes:

- modified `.py` file
- class or structure explanation
- attributes and methods identified
- one working modification
- comparison to procedural or function-based code

**Instructor Notes:**

A7 validation may be as simple as running the modified file and showing the new
behavior.

**Transition Cue:**

Both assignments need evidence and explanation.

**Lab Connection:**

Closes Assignment 7 - Reading Structured Code.

---

## Slide 17 - Evidence For Week 4

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Week 4 evidence should show that you inspected, changed, and checked the code.

Useful evidence includes:

- corrected or modified files
- expected-vs-actual examples
- debug output or traceback clue
- simple checks or test cases
- explanation in your own words
- AI-use note if AI was permitted and used

**Instructor Notes:**

This integrates the week. Students should preserve reasoning, not only final
files.

**Transition Cue:**

Close with believable repair as the success target.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can prove what changed, the fix is believable.

Before submitting Week 4 work, ask:

- What was wrong or unfamiliar?
- What did I change?
- What did I check?
- What evidence supports the result?
- Can I explain it in my own words?

**Instructor Notes:**

Close on evidence-backed ownership. Week 5 will extend this into files,
exceptions, and data persistence.

**Transition Cue:**

Next week, programs begin saving, loading, and handling data more persistently.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one A6 bug and one A7 structure question.
2. Run `04_simple_test_cases.py`.
3. Discuss normal, boundary, and alternate values.
4. Optionally run `05_assert_basics.py`.
5. Run or inspect `11_pytest_unit_tests_demo.py` as recognition-level exposure.
6. Use Slides 15-17 as completion checklists.
7. Give students substantial time to close A6 and A7.

Instructor pacing note:

If students need more assignment time, skip pytest execution and simply show
its structure for recognition.

---

# Lab / Assignment Bridge

By the end of Day 3, students should submit or be ready to submit A6 and A7.

Minimum closure target:

- A6 corrected code runs
- A6 includes debugging evidence and explanation
- A7 modified code runs
- A7 includes class/structure explanation
- any AI use is documented if permitted

---

# README / Submission Expectations

Suggested student evidence:

- corrected or modified `.py` files
- sample output or checks
- debugging notes
- structured-code reading responses
- AI-use note if permitted and used

---

# AI-Use Boundary

AI may support debugging or explanation only when permitted and bounded.

Students remain responsible for:

- attempting manual diagnosis or reading first
- verifying AI suggestions against the code
- deciding what to accept, change, or reject
- explaining the final result in their own words

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Bug-fix-check | Simple bug -> fix -> check progression | Avoid complex testing tool imagery |
| 2 | Week 4 arc | Evidence -> repair -> validation -> explanation | Keep clean |
| 3 | One run not enough | Single run contrasted with multiple checked cases | Avoid formal coverage dashboards |
| 4 | Today's tools | Toolbox with expected/actual, test cases, assert, pytest recognition | Avoid making pytest dominant |
| 5 | Deferred testing topics | Parked shelf: pytest mastery, mocking, full suites, profiling | Reassuring tone |
| 6 | Expected behavior check | Input, expected, actual, result match card | Keep text readable |
| 7 | Simple test cases | Three value cards checking one function | Avoid dense code |
| 8 | Boundary values | Passing score boundary: 90, 70, 69 | Make cutoff visible |
| 10 | Testing progression | Ladder from print checks to assert to pytest recognition | Avoid implying all required |
| 11 | Pytest recognition | Small test file card with pass/fail output | Label as recognition |
| 13 | Fix explanation | Bug/evidence/change/check/result explanation chain | Keep concise |
| 15 | A6 closeout | Corrected file, clue, check, explanation | Keep documentation light |
| 16 | A7 closeout | Modified class file with class/attribute/method notes | Avoid full OOP diagram |
| 17 | Week 4 evidence | Files, checks, notes, AI-use note if used | Keep organized |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Opening/review | 8 min | Use Slides 1 and 2 only | Ask students to state one fix claim |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Clarify pytest boundary |
| Simple checks | 15 min | Use one test value | Add boundary discussion |
| Assert/pytest | 10 min | Skip pytest execution | Inspect pytest file structure |
| Justification | 10 min | Use Slide 13 only | Have students draft one explanation |
| Assignment closeout | 30+ min | Use checklists only | Confer individually on evidence |
| Closing check | 5 min | Ask final questions verbally | Have students share one validation claim |

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
