# W07A Structured Behavior Live

**10-152-118 Web Development Foundations**  
**Week 7 Monday Live Lecture**  
**Topic:** Structured Behavior - From Working To Clean

---

# Session Purpose

Week 7 shifts from fixing broken code to improving working code.

Students should leave Monday understanding that refactoring is not an admission
that code was wrong. Refactoring is the process of making working code easier
to read, test, explain, and maintain.

The practical target is intentionally small:

- identify responsibilities inside a working event handler
- extract behavior into named functions
- preserve the original behavior
- explain why the new structure is clearer

---

# IIM Alignment

Week 7 Monday:

- functions, callbacks, structure
- code organization basics

Tuesday lab:

- refactor messy code into functions

AI role:

- AI as Explainer
- AI may explain structure or suggest possible function responsibilities
- AI should not replace the student's first refactor or final explanation

---

# Reading Alignment

Assigned reading:

- **Required - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected pages
  on functions, scope, dot notation, and the document object as a
  built-in/global object: pp 85-103, 120-130
- **Reference - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected pages
  on objects and built-in methods: pp 104-119, 131-144

Reading-to-lab bridge:

- Reading gives vocabulary: function, parameter, argument, return value, scope,
  callback, event handler.
- Lecture shows why functions matter inside browser behavior.
- Tuesday lab asks students to refactor existing JavaScript into clearer
  functions.

What students should not try to master yet:

- all object patterns
- advanced scope edge cases
- every built-in method
- arrow-function style preferences
- module structure

---

# Prior Lab Review

Use the Week 6 success solution:

```text
Assignments/Success_Solutions/Week_06_Debugging_Problem_Solving/
```

Review rhythm:

1. Open the final site and verify the planner works.
2. Open the debugging report before showing code.
3. Connect each reported issue to the corrected code.
4. Emphasize observe, isolate, fix, verify.

Bridge:

```text
Last week we made broken code work.
This week we make working code easier to understand.
```

---

# Demo Set

Demo folder:

```text
Demos/Week_07_Structured_JavaScript/01_monday_messy_working_code/
```

Demo role:

- show working code that is still hard to read
- run the page first
- read the event handler aloud
- identify responsibilities that could become functions
- avoid fully refactoring everything Monday; Wednesday completes the iteration

---

# Slide Sequence Overview

1. Working Is Good - Clear Is Better
2. Previous Lab Review / Success Path
3. From Debugging To Refactoring
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. Code Can Work And Still Be Hard To Read
8. Function As A Named Responsibility
9. Callback: A Function Used Later
10. Scope: Where A Name Can Be Seen
11. AI Can Explain Structure, Not Replace Your Refactor
12. Useful AI Prompt Pattern
13. Demo: Messy Working Code
14. Find The Responsibilities
15. Tuesday Lab Bridge
16. Evidence Expectations
17. Closing

---

# Slide-By-Slide Source

### Slide 1 - Working Is Good - Clear Is Better

Student-visible text:

```text
Working code matters.

Clear working code matters more.

This week:
- behavior should still work
- code should be easier to read
- each function should have a clear job
- your explanation should match your structure
```

**Instructor notes:**

- Start by validating the Week 6 debugging work.
- Say plainly that refactoring is not punishment.
- This week is about maintainability at a beginner level.

**Transition cue:**

- "Before we clean code, let's look at how last week's debugging work ended."

Visual notes:

- Working code becoming clearer without changing the browser result.

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Assignment 6 success path:

- site runs without console errors
- interaction works
- bug report explains the issue
- fix is connected to evidence
- verification proves the result

Now we ask:
Can another person understand the code?
```

**Instructor notes:**

- Open the Week 6 success solution.
- Show the report before code.
- Connect evidence habits to readable structure.

**Transition cue:**

- "Debugging showed us where code was hard to follow. Refactoring is one response."

Demo connection:

- `Assignments/Success_Solutions/Week_06_Debugging_Problem_Solving/`

### Slide 3 - From Debugging To Refactoring

Student-visible text:

```text
Debugging asks:
Why did this fail?

Refactoring asks:
How can this be clearer while still working?

The rule:
Change structure.
Preserve behavior.
```

**Instructor notes:**

- Give students the language for refactoring before showing code.
- Emphasize that behavior preservation is required.

**Transition cue:**

- "Today's success is not adding a bigger feature. It is making a feature easier to understand."

Visual notes:

- Same browser output with cleaner code behind it.

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you can spot a long event handler
- you can name what each part does
- you can identify 2-3 possible functions
- you can explain why a function name helps
- the original behavior still works
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Keep the target practical and observable.

**Transition cue:**

- "Here are the tools we need for that kind of cleanup."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- working behavior
- function
- responsibility
- event handler
- callback
- scope
- meaningful name
- retest
```

**Instructor notes:**

- Keep the toolbox conceptual and code-adjacent.
- The day is not about memorizing every function syntax variation.

**Transition cue:**

- "And here is what we are deliberately not trying to master today."

Visual notes:

- Toolbox with function, responsibility, callback, scope, name, retest.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- modules
- classes
- complex objects
- advanced scope rules
- build tools
- framework patterns

Today:
clear named functions inside one JavaScript file.
```

**Instructor notes:**

- This protects the scope of Duckett Chapter 3.
- The reading contains more than the assignment requires.

**Transition cue:**

- "Now we can look at code that works, but asks too much of the reader."

Visual notes:

- Shelf of advanced structure topics.

### Slide 7 - Code Can Work And Still Be Hard To Read

Student-visible text:

```text
Working but messy code often has:

- one long event handler
- repeated output text
- several decisions in one place
- vague names
- hidden responsibilities

The browser may be happy.
The next human reader may not be.
```

**Instructor notes:**

- Use this slide to reduce resistance: "it already works" is not the end.
- Tie to professional habits without making it feel advanced.

**Transition cue:**

- "Functions give us a way to name those hidden responsibilities."

Visual notes:

- Tangled event handler being separated into labeled responsibilities.

### Slide 8 - Function As A Named Responsibility

Student-visible text:

```text
A function should answer:

- What job does this code do?
- What information does it need?
- What result does it produce?
- Is the name honest?

Good names make code easier to read aloud.
```

**Instructor notes:**

- Avoid "one function per line" thinking.
- Emphasize responsibility, not just shorter code.

**Transition cue:**

- "One special kind of function use already appears in event code."

Visual notes:

- Code responsibility card becoming a named function.

### Slide 9 - Callback: A Function Used Later

Student-visible text:

```text
In browser code, a callback is often:

- a function
- handed to another piece of code
- used later when something happens

Example:
`button.addEventListener("click", showPlan);`

The click happens later.
The function runs then.
```

**Instructor notes:**

- Keep callback as a timing/use idea, not a deep async topic.
- This prepares Week 8 without teaching Week 8 early.

**Transition cue:**

- "A named callback is easier to recognize than a long anonymous function."

Visual notes:

- Button click leading to a named function.

### Slide 10 - Scope: Where A Name Can Be Seen

Student-visible text:

```text
Scope asks:
Where can this name be used?

Beginner rule:
- keep shared page elements near the top
- keep temporary values inside functions
- avoid depending on names from everywhere

Clear scope makes debugging easier.
```

**Instructor notes:**

- Keep this beginner-level.
- Connect to the reading on scope and global/built-in objects.
- Mention `document` as a built-in/global object only lightly.

**Transition cue:**

- "AI can help explain these structure ideas, but it cannot replace your own refactor."

Visual notes:

- Named areas showing shared page elements versus inside-function values.

### Slide 11 - AI Can Explain Structure, Not Replace Your Refactor

Student-visible text:

```text
AI as Explainer:

Useful:
- explain what a function does
- explain why a name is clearer
- suggest possible responsibilities to look for

Not useful yet:
- "rewrite my whole assignment"
- "make this perfect"
- pasted code you cannot explain
```

**Instructor notes:**

- This follows the Week 6-8 AI as Explainer role.
- Keep students responsible for manual refactoring and final explanation.
- If students use AI, they should still test and explain the result.

**Transition cue:**

- "If students use AI for explanation, the prompt needs boundaries."

Visual notes:

- AI explanation card beside student-owned refactor notes.

### Slide 12 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I manually wrote this JavaScript.
Do not rewrite it for me.
Explain what responsibilities are mixed together,
suggest possible function names,
and ask me one question before suggesting code."
```

**Instructor notes:**

- This gives students a usable pattern before Tuesday lab.
- Emphasize manually wrote, do not rewrite, explain, ask first.
- The prompt is for explanation and reflection, not for outsourcing the
  refactor.

**Transition cue:**

- "Now let's look at working code and identify what responsibilities are hiding inside it."

Visual notes:

- Form-like prompt card with labeled parts: context, constraint, explanation
  request, and question-first behavior.

### Slide 13 - Demo: Messy Working Code

Student-visible text:

```text
Demo: Messy Working Code

Watch for:
- the feature works
- the event handler is long
- decisions are mixed with output
- the code is harder to read aloud

Working is the starting point.
Clarity is the improvement.
```

**Instructor notes:**

- Run the demo first.
- Type or reveal enough of the event handler for students to see the discomfort.
- Do not finish the full refactor Monday.

**Transition cue:**

- "Instead of rewriting everything, we will name the responsibilities."

Demo connection:

- `Demos/Week_07_Structured_JavaScript/01_monday_messy_working_code/`

### Slide 14 - Find The Responsibilities

Student-visible text:

```text
Possible responsibilities:

- read the minutes input
- decide which plan fits
- update the message on the page
- respond to the button click

Possible function names:
- `getMinutesAvailable()`
- `chooseStudyPlan(minutes)`
- `showPlan()`
```

**Instructor notes:**

- These names match the Wednesday reference demo.
- Have students say what each function would own.
- Save the actual extraction for Wednesday.

**Transition cue:**

- "Tuesday lab asks you to do this same thinking with your own JavaScript."

Visual notes:

- Long handler split into named responsibility cards.

### Slide 15 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab: first refactor pass

Your goal:
- choose existing working JavaScript
- identify repeated or mixed logic
- create at least 2-3 functions
- give each function a clear name
- retest the behavior
```

**Instructor notes:**

- Emphasize working code first.
- Refactoring should not break the site.
- Students may feel slower; normalize it.

**Transition cue:**

- "Your evidence this week is not only that it works. It is that the structure is explainable."

Lab connection:

- Assignment 7 - Iteration 1

### Slide 16 - Evidence Expectations

Student-visible text:

```text
Preserve evidence:

- original behavior still works
- JavaScript has named functions
- function names match their jobs
- repeated logic is reduced where possible
- you can explain what changed
```

**Instructor notes:**

- This prepares the final reflection.
- Encourage students to keep a before/after note if helpful.

**Transition cue:**

- "Refactoring is successful when the next reader can follow the code."

### Slide 17 - Closing

Student-visible text:

```text
Today:

- working code became a starting point
- hidden responsibilities became visible
- functions gave responsibilities names
- behavior still had to be verified

Next:
we extract the functions and compare messy vs clean code.
```

**Instructor notes:**

- Close with continuity into Wednesday's recorded refactor.
- Keep the focus on preserving behavior.

**Transition cue:**

- "Code is written for humans first, computers second."

---

# Demo Execution Notes

- Use `Demos/Week_07_Structured_JavaScript/01_monday_messy_working_code/`.
- Run the page before showing code.
- Test several minute values.
- Read the event handler aloud.
- Ask what each part is responsible for.
- Identify possible function names, but save the full extraction for Wednesday.

---

# Lab / Assignment Bridge

Students should use Tuesday to begin Assignment 7:

- select existing working JavaScript
- identify responsibilities
- create at least 2-3 functions
- retest behavior after refactoring
- prepare to explain why the structure is clearer

---

# Evidence / Submission Expectations

For Tuesday, students should have a working refactored draft with:

- at least 2-3 functions
- meaningful names
- behavior still working
- notes on what responsibilities were separated

The final refinement and reflection continue after Wednesday's recorded lesson.

---

# AI-Use Boundary

AI may help explain what a function does, compare possible names, or identify
possible responsibilities in a small code excerpt. Students must still make,
test, and explain their own refactor.

---

# Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | working to clear code | Include in Week 7 prompt packet |
| 2 | Week 6 success path | Include in Week 7 prompt packet |
| 3 | debugging to refactoring | Include in Week 7 prompt packet |
| 4 | success today | Use SmartArt; no image prompt by default |
| 5 | toolbox | Include in Week 7 prompt packet |
| 6 | parked for later | Include in Week 7 prompt packet |
| 7 | working but hard to read | Include in Week 7 prompt packet |
| 8 | named responsibility | Include in Week 7 prompt packet |
| 9 | callback used later | Include in Week 7 prompt packet |
| 10 | scope basics | Include in Week 7 prompt packet |
| 11 | AI as structure explainer | Include in Week 7 prompt packet |
| 12 | useful AI prompt pattern | Include in Week 7 prompt packet |
| 13 | demo messy working code | Include in Week 7 prompt packet |
| 14 | responsibilities to functions | Include in Week 7 prompt packet |

---

# Instructor Timing Notes

- Previous success review: 7-10 minutes
- Refactoring mindset and toolbox: 10-12 minutes
- Functions, callbacks, and scope: 15-18 minutes
- AI-as-explainer boundary and prompt pattern: 4-6 minutes
- Demo and responsibility identification: 15-20 minutes
- Lab bridge and evidence: 5-8 minutes

If delivery time is tight, skim the Week 6 success review or verbally bridge the
AI boundary. Do not skip the demo, responsibility identification, or retest
expectation.

---

# Post-Lecture Notes

- Note whether students resist changing working code.
- Note whether students name functions by responsibility or vague action.
- Use Tuesday lab observations to shape Wednesday's refactor explanation.
