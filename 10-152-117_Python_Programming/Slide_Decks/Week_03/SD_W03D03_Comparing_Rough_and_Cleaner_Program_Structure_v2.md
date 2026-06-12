# SLIDE DECK SOURCE - WEEK 3 DAY 3

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 3 / Thursday |
| Date | September 3, 2026 |
| Weekly Theme | Organizing Code and Data |
| Lecture Title | Comparing Rough and Cleaner Program Structure |
| Assignments Supported | Assignment 4 - Function Builder; Assignment 5 - List or Dictionary Mini-App |
| Readiness Target | Students can compare a rough solution to a cleaner organized one |
| Primary Watch Point | Bounded AI use depends on manual baseline existing first; do not invert that sequence |
| Source Version | v2 refactor |

---

# Session Purpose

This session teaches students to compare a rough working solution with a
cleaner organized solution.

Students should understand that "working" is necessary but not always enough.
Code also needs to be readable, explainable, and easier to change. Functions
and data structures give students tools for improving the shape of a program
after the first version works.

The target pattern is:

```text
working baseline -> compare structure -> revise one meaningful thing -> explain the improvement
```

---

# Review / Prior Work Bridge

Review from Week 3:

- Monday: functions name responsibilities and reduce repeated logic.
- Tuesday: lists and dictionaries store related data.
- A4 asks students to organize logic with functions.
- A5 asks students to organize data with a list or dictionary.

Quick review questions:

- What job does each function own?
- What data is stored?
- How is the data accessed?
- What part of the code is easiest to explain?
- What part is hardest to change?

Bridge into Day 3:

Today students use comparison and revision to improve program structure without
losing the small-program focus.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 3
- textbook chapter areas: **Functions, the Building Blocks of Code** and
  **Built-In Data Types**

Day 3 reading focus:

- scopes and name resolution
- a few useful function tips
- final considerations about data structures

Use this reading to support:

- rough versus cleaner program structure
- why organization matters
- why manual baseline work should come before AI critique

Today's reading boundary:

Students should not worry yet about full namespace theory, advanced import
patterns, recursive functions, lambdas, decorators, generators, or advanced
data-structure techniques.

---

# What We Will Use Today

Today we will use:

- rough working code
- cleaner organized code
- function responsibility
- list/dictionary choice
- comparison questions
- small revision
- explanation of improvement

Today we will skip for now and revisit later:

- broad architecture redesign
- full professional refactoring
- advanced AI-assisted rewrite workflows
- class-based design
- large project restructuring

---

# Assignments Supported

Primary support:

- Assignment 4 - Function Builder
- Assignment 5 - List or Dictionary Mini-App

Day 3 should help students finish, revise, and explain both assignments.

A4 completion target:

- at least two clear functions
- meaningful function names
- correct function calls
- explanation of each function's job

A5 completion target:

- list or dictionary data
- retrieval, lookup, or loop behavior
- visible output
- explanation of why the structure fits

---

# Readiness Target

By the end of the session, students should be able to:

- compare two versions of a small program
- identify one structural improvement
- explain why a function improves readability
- explain why a data structure fits the task
- avoid over-rewriting working code
- use AI only after a manual baseline, if permitted
- justify the final version in plain language

---

# Primary Watch Point

The main risk is letting AI or broad revision replace the learning.

Use this sequence:

```text
manual baseline -> human comparison -> optional AI critique -> human decision
```

If the manual version does not exist, students should stay manual.

---

# Demo Set For This Session

Primary demo:

- `Demos/Week_03_Organizing_Code_and_Data/07_structure_comparison.py`

Optional review demos:

- `Demos/Week_03_Organizing_Code_and_Data/02_function_refactor.py`
- `Demos/Week_03_Organizing_Code_and_Data/06_list_of_dictionaries.py`

Recommended use:

1. Use Demo 7 as the primary rough-versus-organized comparison.
2. Review Demo 2 or Demo 6 only if students need a reminder of functions or
   data structures.
3. Keep the comparison concrete: what changed, why it helps, and what stayed
   small.

---

# Student Hands-On Bridge

Students should use class time to finish or revise A4 and A5.

Recommended work sequence:

```text
1. Run the current version.
2. Identify one hard-to-explain part.
3. Choose one meaningful improvement.
4. Revise only that part.
5. Run the code again.
6. Explain what improved and why.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect functions and data structures to comparison |
| Today's Working Set | 4-5 | Core | Bound revision and defer broad redesign |
| Correctness vs Clarity | 6-8 | Core | Separate running code from explainable structure |
| Comparison Demo | 9-11 | Demo / Core | Analyze rough vs organized code with concrete criteria |
| AI Boundary | 12-13 | Core | Preserve manual baseline before optional AI critique |
| Assignment Completion Bridge | 14-17 | Lab Bridge / Evidence | Close A4/A5 with revision and explanation |
| Closing Check | 18 | Assessment / Evidence | Define successful structural judgment |

---

# Slide-by-Slide Source

## Slide 1 - Working Code Can Still Improve

**Delivery Category:** Review

**Student-Visible Text:**

Working code is important, but it is not the only goal.

Code can run and still be hard to read, explain, or change.

Today, compare structure by asking:

- What got clearer?
- What got easier to change?
- What became easier to explain?
- What stayed small enough to trace?

**Instructor Notes:**

Frame this as judgment, not criticism. Students are learning how developers
improve code after first contact with reality.

**Transition Cue:**

This week's tools give us ways to improve structure.

**Visual Notes:**

Use rough working code beside a cleaner organized version.

---

## Slide 2 - Functions Plus Data Structures

**Delivery Category:** Review

**Student-Visible Text:**

Functions organize logic.

Lists and dictionaries organize information.

Cleaner programs often use both:

- named jobs
- related data grouped together
- output that is easier to explain

**Instructor Notes:**

Connect Monday and Tuesday directly. The day is not a new topic so much as an
evaluation and improvement day.

**Transition Cue:**

The success pattern starts with a working baseline.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Working baseline -> compare structure -> revise one meaningful thing -> explain
the improvement.

A useful revision should make the program:

- clearer
- easier to test
- easier to change
- easier to explain

**Instructor Notes:**

This protects against both overbuilding and aimless polishing. One meaningful
improvement is enough.

**Transition Cue:**

Let's name what we will use today.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- rough working code
- cleaner organized code
- function responsibility
- list/dictionary choice
- comparison questions
- small revision

The goal is better structure, not more features.

**Instructor Notes:**

Keep the working set aligned to A4 and A5. This is not an architecture lecture.

**Transition Cue:**

Some tempting revision paths are too large for today.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip broad redesign, class-based architecture, and large AI rewrites
for now.

Today's revision should be small enough to explain:

- one function improvement
- one data-structure improvement
- one clearer name
- one removed repetition

**Instructor Notes:**

This is scope control. Students may assume "cleaner" means rewriting
everything. Keep the target on one meaningful improvement.

**Transition Cue:**

Now separate correctness from clarity.

---

## Slide 6 - Correct Is Not The Same As Clear

**Delivery Category:** Core

**Student-Visible Text:**

Correct code produces the expected result.

Clear code helps a human understand how the result happens.

Both matter because:

- programs need to run
- people need to read them
- future changes need to be possible

**Instructor Notes:**

Say this plainly. Students may still equate "it works" with "it is finished."
Week 3 introduces the idea that structure has value.

**Transition Cue:**

Cleaner structure should make explanation easier.

---

## Slide 7 - Cleaner Structure Is Easier To Explain

**Delivery Category:** Core

**Student-Visible Text:**

Cleaner structure usually makes the program easier to talk through.

Look for:

- clear function names
- related data grouped together
- less repeated logic
- output that matches the program's purpose

If you can explain it better, the structure probably improved.

**Instructor Notes:**

Tie organization directly to the course's emphasis on explanation and ownership.

**Transition Cue:**

The demo shows a rough version and a cleaner version side by side.

---

## Slide 8 - Comparison Questions

**Delivery Category:** Core

**Student-Visible Text:**

Use comparison questions instead of vague opinions.

Ask:

- What changed?
- Why does it help?
- What became easier?
- What stayed the same?
- What would I change next?

**Instructor Notes:**

This gives students a repeatable judgment tool. It also prepares them for
bounded AI critique after a manual baseline.

**Transition Cue:**

Now apply those questions to the structure comparison demo.

---

## Slide 9 - Demo: Rough vs Organized Structure

**Delivery Category:** Demo

**Student-Visible Text:**

Watch both versions run.

Then compare:

- repeated code
- function responsibility
- name clarity
- how easy each version is to change

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/07_structure_comparison.py`

Run the rough version and organized version. Ask which would be easier to
extend and why.

**Transition Cue:**

Now identify specific improvements, not just "better-looking" code.

**Demo Connection:**

Primary demo file: `07_structure_comparison.py`

---

## Slide 10 - What Changed?

**Delivery Category:** Core

**Student-Visible Text:**

A useful comparison names specific changes.

Examples:

- repeated output formatting moved into a function
- status logic received a clear name
- task data became easier to reuse
- one change affects multiple outputs

Specific changes are easier to justify than general impressions.

**Instructor Notes:**

This slide keeps comparison grounded in evidence. Students should avoid saying
"it looks cleaner" without explaining why.

**Transition Cue:**

After identifying changes, decide whether the change actually helps.

---

## Slide 11 - What Got Easier?

**Delivery Category:** Core

**Student-Visible Text:**

An improvement should make something easier.

Ask whether the revision made it easier to:

- read
- test
- change
- reuse
- explain

If nothing got easier, the revision may not be useful yet.

**Instructor Notes:**

This is the practical evaluation heuristic. It prevents cosmetic-only changes
from being mistaken for meaningful refactoring.

**Transition Cue:**

AI can help compare code, but only after the student has a baseline.

---

## Slide 12 - Manual Baseline Comes First

**Delivery Category:** Core

**Student-Visible Text:**

AI critique only helps learning after you have your own baseline.

Use this order:

1. Build or revise manually.
2. Run and inspect your version.
3. Compare structure yourself.
4. Use AI only if permitted.
5. Decide what to keep, change, or reject.

**Instructor Notes:**

Be explicit. If the manual version is missing, the student has nothing to
compare and little basis for judgment.

**Transition Cue:**

If AI is used, students still own the final decision.

---

## Slide 13 - AI Suggestions Are Not Automatic Answers

**Delivery Category:** Core

**Student-Visible Text:**

If AI suggests a refactor, you still decide whether it fits.

Explain:

- what AI suggested
- what you accepted
- what you changed
- what you rejected
- why the final version makes sense

AI can suggest structure. You must understand and justify it.

**Instructor Notes:**

This reinforces AI accountability without demonizing the tool. The student must
remain the semantic decision-maker.

**Transition Cue:**

Now apply the comparison process to A4 and A5.

---

## Slide 14 - Finish A4: Function Builder

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 4, check that your function structure is explainable.

Your program should have:

- at least two functions
- meaningful function names
- correct function calls
- one clear responsibility per function
- explanation of how the functions work together

**Instructor Notes:**

Use this as an A4 completion checklist. Students should be able to explain each
function without reading every line mechanically.

**Transition Cue:**

Now check the data mini-app.

**Lab Connection:**

Closes Assignment 4 - Function Builder.

---

## Slide 15 - Finish A5: List Or Dictionary Mini-App

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 5, check that your data structure is useful.

Your program should have:

- list or dictionary data
- a lookup, retrieval, or loop
- visible output
- a structure choice you can explain
- code that stays small enough to trace

**Instructor Notes:**

Students may store data but forget to use it. Push toward visible behavior and
structure-choice explanation.

**Transition Cue:**

Both assignments need a short improvement or structure explanation.

**Lab Connection:**

Closes Assignment 5 - List or Dictionary Mini-App.

---

## Slide 16 - Revision Evidence

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Revision evidence should explain what improved.

Useful explanation:

- what changed
- why it changed
- how the new version is clearer
- what you tested after the change
- what you would improve next

**Instructor Notes:**

This prepares students for later revision recovery and capstone habits. Keep it
small enough for Week 3.

**Transition Cue:**

The final submission should preserve code and reasoning.

---

## Slide 17 - Evidence For Week 3

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Week 3 submissions should show organization and explanation.

Useful evidence includes:

- working `.py` files
- function responsibility explanation
- data structure choice explanation
- visible output
- AI-use note if AI was permitted and used

The goal is not just code that runs. The goal is code you can explain.

**Instructor Notes:**

If GitHub/README expectations are active, this can become the short explanation
section for each assignment.

**Transition Cue:**

Close with justification as evidence of understanding.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can justify the improvement, you understand it.

Before submitting Week 3 work, ask:

- What did I organize?
- What got clearer?
- What became easier to change?
- What evidence shows it still works?
- Can I explain the final structure?

**Instructor Notes:**

Close on explainable improvement. Week 4 will use this structure awareness to
support debugging, testing, and reading other code.

**Transition Cue:**

Next week, we use structure and evidence to debug, test, and read code more
carefully.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one A4 function responsibility.
2. Review one A5 structure choice.
3. Run `07_structure_comparison.py`.
4. Compare rough and organized versions using Slides 10-11.
5. Discuss manual baseline before optional AI critique.
6. Move students into A4/A5 completion and revision.

Instructor pacing note:

If students need more assignment time, keep the demo short and spend the rest
of the session on conferences and targeted revision.

---

# Lab / Assignment Bridge

By the end of Day 3, students should submit or be ready to submit both Week 3
assignments.

Minimum closure target:

- A4 has at least two clear functions
- A4 function responsibilities can be explained
- A5 uses a list or dictionary meaningfully
- A5 structure choice can be explained
- code runs after revision

---

# README / Submission Expectations

Suggested student evidence:

- clear `.py` filenames
- code that runs without syntax errors
- brief function responsibility explanation
- brief data structure choice explanation
- visible output or sample run
- AI-use note if permitted and used

---

# AI-Use Boundary

AI use, if permitted, must come after a manual baseline.

Acceptable bounded use:

- ask AI to compare two structures
- ask AI to identify repeated code
- ask AI to suggest a refactor
- ask AI to explain tradeoffs

Student responsibility:

- decide what to keep, change, or reject
- verify the code still runs
- explain the final version
- avoid submitting code they cannot defend

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Working but improvable | Rough working code versus cleaner version | Avoid shaming rough code |
| 2 | Functions plus data | Function boxes and data structure cards working together | Keep beginner-level |
| 3 | Revision pattern | Baseline -> compare -> revise -> explain | Avoid heavy agile/process imagery |
| 4 | Today's tools | Toolbox with baseline, comparison, function responsibility, data choice | Avoid architecture jargon |
| 5 | Deferred revision topics | Parked-for-later shelf: broad redesign, classes, large AI rewrites | Keep calm and supportive |
| 6 | Correct vs clear | Two cards: expected output and human readability | Avoid implying correctness is optional |
| 7 | Explainable structure | Clear function names and grouped data | Keep code minimal |
| 8 | Comparison questions | Question cards: what changed, why helps, what got easier | Avoid clutter |
| 9 | Demo comparison | Rough output block and organized function output | Keep specific changes visible |
| 11 | What got easier | Five icons/cards: read, test, change, reuse, explain | Avoid generic productivity imagery |
| 12 | Manual baseline first | Ordered flow: manual baseline -> compare -> optional AI critique | Do not show AI as first step |
| 13 | AI accountability | AI suggestion card filtered through human decision | Avoid robot taking over visual |
| 14 | A4 completion | Two function cards with responsibility labels | Keep scope small |
| 15 | A5 completion | List/dictionary data plus visible output | Keep structure choice visible |
| 17 | Week 3 evidence | `.py` files, explanation notes, output sample | Keep documentation lightweight |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask students to name one improvement |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss why large redesign waits |
| Correctness vs clarity | 12 min | Use Slide 6 only | Compare two small examples |
| Demo comparison | 15 min | Run only organized version after showing rough code | Annotate concrete changes |
| AI boundary | 8 min | State verbally | Discuss acceptable AI critique prompts |
| Assignment completion | 30+ min | Use A4/A5 checklists only | Confer individually on revisions |
| Closing check | 5 min | Ask final questions verbally | Have students justify one improvement |

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
