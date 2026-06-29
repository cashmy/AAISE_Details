# W04A JavaScript Foundations Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 4
- Session: Monday live
- Deck title: JavaScript Foundations: This Is Programming
- Phase: Behavior
- Target duration: 55-70 minutes
- Recording expected: no

## Session Type

Monday live lecture.

## Lesson Purpose

Students should leave Monday understanding that JavaScript is a programming
language with instructions that execute step by step.

The practical target is intentionally small: create a JavaScript file, run it
through a browser page, inspect console output, and predict one simple decision.

## IIM Alignment

Week 4 Monday:

- JavaScript as a separate system.
- Variables, functions, and logic at a first-contact level.
- No DOM yet; this boundary is important.

## Reading Alignment

Week 4 assigned reading:

- Required - JS/JQ: Duckett Chap 1 - The ABC of Programming, selected pages on scripts, variables, and basic program thinking, pp. 36-52
- Required - JS/JQ: Duckett Chap 2 - Basic JavaScript Instructions, pp. 53-84
- Skim - JS/JQ: Duckett Chap 1 - The ABC of Programming, pp. 11-35
- Skim - JS/JQ: Duckett Chap 4 - Decisions & Loops, selected pages on `if` statements only, pp. 145-163
- Reference - JS/JQ: Duckett Chap 3 - Functions, Methods & Objects, pp. 85-144, use later as needed
- Reference - JS/JQ: Duckett Chap 4 - Decisions & Loops, selected pages on `switch`, `while`, and `for` loops, pp. 164-182

Reading-to-lab bridge:

- Reading gives vocabulary: script, statement, variable, value, expression, operator, Boolean, condition, function.
- Lecture isolates programming before connecting JavaScript to the page.
- Tuesday lab uses console-based practice: predict, run, observe.

What students should not try to master yet:

- DOM interaction
- button clicks and events
- loops
- full function design
- JavaScript libraries
- changing page content with JavaScript

## Review / Prior Work Bridge

Previous lab:

- Assignment 3 - Layout & Responsive Design

Success solution:

```text
Assignments/Success_Solutions/Week_03_Layout_Responsive_Design/
```

Review focus:

- show one successful path, not the only correct answer
- resize the page to show the media query
- identify Flexbox and responsive rules in `styles.css`
- connect the end of Unit 1 to the start of Unit 2
- make the phase shift explicit: pages are built and styled; now code will execute

## What Counts As Success Today

By the end of the session, students should be able to:

- create or identify a `.js` file
- connect it to a simple HTML page
- open the browser console
- use `console.log()` to see output
- predict one `if / else` result before running it

Success is not page interaction today.

## Today's Toolbox

Today we will use:

- `script.js`
- `<script src="script.js"></script>`
- variable
- value
- Boolean
- `console.log()`
- `if / else`
- browser console

## Parked For Later

Parked for later:

- DOM selection
- button click events
- changing page text
- loops
- jQuery
- full app behavior

Today, JavaScript runs as instructions we can read, predict, and inspect.

## Assignment Supported

Assignment 4 - Introduction to JavaScript

Monday supports Iteration 1:

- create a JavaScript file
- use at least two variables
- use at least one condition
- output results with `console.log()`
- follow the logic step by step

Functions are introduced lightly on Monday and deepened in the Wednesday
recording.

## Readiness Target

By the end of the session, students should be ready to:

- write a small console-based JavaScript program
- change a value and predict the output
- identify whether a result came from a variable or a condition
- avoid expecting visible page behavior yet

## Primary Watch Point

Students may expect JavaScript to immediately change the web page.

Reframe:

```text
Before JavaScript changes the page, JavaScript has to execute correctly.
```

## Demo Set

Demo folder:

```text
Demos/Week_04_JavaScript_Logic/01_monday_values_conditions/
```

Demo files:

- `index.html`
- `script.js`
- `demo_notes.md`

Delivery:

- Type the JavaScript live.
- Open the browser console early.
- Add variables first, then `console.log()`, then the `if / else`.
- Change one value and ask students to predict before refreshing.

## Slide Sequence Overview

1. Phase Shift: The Page Starts To Execute
2. Previous Lab Review / Success Path
3. HTML And CSS Describe; JavaScript Executes
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. What A Program Does
8. Variables Store Values
9. Console Output Makes Thinking Visible
10. Conditions Choose A Path
11. Demo: Values And Conditions
12. Predict, Run, Observe
13. Tuesday Lab Bridge
14. Evidence Expectations
15. Closing

## Slide-By-Slide Source

### Slide 1 - Phase Shift: The Page Starts To Execute

Student-visible text:

```text
Weeks 1-3:
- HTML gave the page structure
- CSS controlled appearance
- layout organized space

Week 4:
- JavaScript introduces instructions
- instructions execute step by step
- behavior begins with logic
```

**Instructor notes:**

- Make the phase shift explicit.
- Students are moving from describing a page to running instructions.
- Keep the tone steady; this is the biggest cognitive jump so far.

**Transition cue:**

- "Before we add behavior, let's close the loop on the layout work."

Visual notes:

- Progression from HTML/CSS/layout into JavaScript execution.

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Assignment 3 success path:

- Flexbox used intentionally
- spacing and alignment improved
- at least one media query
- layout adapts on smaller screens
- navigation remains usable

This completes the first foundation layer.
```

**Instructor notes:**

- Open the Week 3 success solution.
- Resize the browser to show responsiveness.
- Briefly identify Flexbox and media query rules.

**Transition cue:**

- "Now we shift from what the page is and how it looks to what code does."

Demo connection:

- `Assignments/Success_Solutions/Week_03_Layout_Responsive_Design/`

### Slide 3 - HTML And CSS Describe; JavaScript Executes

Student-visible text:

```text
HTML says:
"Here is the content and meaning."

CSS says:
"Here is how it should look and fit."

JavaScript says:
"Run these instructions in this order."

That order matters.
```

**Instructor notes:**

- This is the central mental model.
- Avoid saying HTML/CSS are not code; they are different kinds of code.
- Emphasize execution order.

**Transition cue:**

- "So today's target is not a fancy interactive page. It is seeing code run."

Visual notes:

- Three labeled layers: describe structure, describe appearance, execute instructions.

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- a `.js` file runs
- output appears in the console
- variables hold values
- an `if / else` chooses a path
- you predict before you run
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Keep the success target smaller than the full assignment endpoint.

**Transition cue:**

- "Here is the small set of tools we need for that."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- `script.js`
- script link
- variable
- value
- Boolean
- `console.log()`
- `if / else`
- browser console
```

**Instructor notes:**

- This is a new kind of toolbox: more logic than visual output.
- Mention that the console is the visible place today.

**Transition cue:**

- "And here is what we are deliberately not doing yet."

Visual notes:

- JavaScript beginner toolbox.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- finding page elements
- button clicks
- changing visible page text
- loops
- jQuery
- full app behavior

Today: run small logic and read the result.
```

**Instructor notes:**

- This slide is important because students may expect DOM work.
- Say directly that Week 5 connects JavaScript to the page.

**Transition cue:**

- "A program is smaller and more concrete than it may sound."

Visual notes:

- Shelf with DOM/events/loops parked for later.

### Slide 7 - What A Program Does

Student-visible text:

```text
A program is a set of instructions.

The browser runs those instructions:
- from top to bottom
- using stored values
- making decisions when conditions appear
- producing output we can inspect

Programming begins with mental execution.
```

**Instructor notes:**

- Tie to the reading's "scripts" and "instructions" language.
- This supports students taking Python at the same time without merging the courses.

**Transition cue:**

- "The first thing a program needs is a way to remember a value."

Visual notes:

- Step-by-step instruction path.

### Slide 8 - Variables Store Values

Student-visible text:

```text
A variable gives a name to a value.

Example:

`const assignmentScore = 84;`
`const submittedOnTime = true;`

Read it as:
"remember this value using this name."
```

**Instructor notes:**

- Avoid a deep `var` / `let` / `const` comparison.
- Use `const` as today's stable default.
- Explain Boolean as true/false.

**Transition cue:**

- "A stored value is only useful if we can inspect what the program sees."

### Slide 9 - Console Output Makes Thinking Visible

Student-visible text:

```text
The console is our first output space.

`console.log()` helps us see:
- what value is stored
- which line ran
- what decision happened
- whether our prediction was right

Today, console output is the visible result.
```

**Instructor notes:**

- Open the browser console before students need it.
- Normalize console output as a learning tool, not an error-only place.

**Transition cue:**

- "Once we can see values, we can ask the program to choose a path."

Visual notes:

- Browser console with simple beginner output.

### Slide 10 - Conditions Choose A Path

Student-visible text:

```text
A condition creates a branch.

`if` means:
"when this is true, run this block."

`else` means:
"otherwise, run this other block."

Do not guess.
Trace the values.
```

**Instructor notes:**

- Use the assignment score and on-time submission example.
- Point out that the condition evaluates to true or false.

**Transition cue:**

- "Let's build one small program and read it like a path."

Visual notes:

- Simple branch diagram: true path / otherwise path.

### Slide 11 - Demo: Values And Conditions

Student-visible text:

```text
Demo: Values And Conditions

Watch for:
- `script.js` linked to the page
- variables created first
- `console.log()` output
- one `if / else` decision
- changing a value and predicting the result
```

**Instructor notes:**

- Type the JavaScript live.
- Paste the HTML shell if timing requires it.
- Keep the focus on prediction and console evidence.

**Transition cue:**

- "The page may look boring. The program is still running."

Demo connection:

- `Demos/Week_04_JavaScript_Logic/01_monday_values_conditions/`

### Slide 12 - Predict, Run, Observe

Student-visible text:

```text
Use this rhythm:

1. predict what should happen
2. run or refresh the page
3. observe the console output
4. compare prediction to result
5. change one value and repeat

This is how logic becomes less mysterious.
```

**Instructor notes:**

- This is the Week 4 learning habit.
- It will also help in Python and later debugging.

**Transition cue:**

- "Tuesday's lab uses this rhythm before we add visible page interaction."

Visual notes:

- Predict-run-observe cycle.

### Slide 13 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab: first JavaScript program

Create a `.js` file with:
- at least 2 variables
- at least 1 `if / else`
- console output
- a simple calculation or decision

Functions are coming next; start with values and decisions.
```

**Instructor notes:**

- Protect the assignment timing: Monday prepares the first working version.
- If students are ready, a tiny function can be previewed, but do not make it the center.

**Transition cue:**

- "The first evidence is not a pretty page. It is output you can explain."

Lab connection:

- Assignment 4 - Iteration 1

### Slide 14 - Evidence Expectations

Student-visible text:

```text
Preserve evidence:

- your `.js` file runs
- console output is visible
- variable names are meaningful
- the condition makes sense
- you can explain what changed when a value changed
```

**Instructor notes:**

- Mention screenshots of console output if useful for lab support.
- Emphasize explanation over syntax perfection.

**Transition cue:**

- "Wednesday will help organize this logic so it can be reused."

### Slide 15 - Closing

Student-visible text:

```text
Today:

- JavaScript ran as instructions
- variables stored values
- console output made logic visible
- a condition chose a path

Next:
we organize logic into functions.
```

**Instructor notes:**

- Close with calm confidence.
- Acknowledge that this may feel different from HTML/CSS.

**Transition cue:**

- "You do not have to memorize everything. You do need to slow down and trace the steps."

## Demo Execution Notes

- Use `Demos/Week_04_JavaScript_Logic/01_monday_values_conditions/`.
- Type `const assignmentScore = 84;` and `const submittedOnTime = true;` live.
- Open the browser console before writing the condition.
- Change one value after the first run and ask students to predict the next output.

## Lab / Assignment Bridge

Students should use Tuesday to build the first console-based program:

- create a JavaScript file
- use values and variables
- write one condition
- output with `console.log()`
- explain the result

## Evidence / Submission Expectations

For Tuesday, students should have a JavaScript file that runs and produces
understandable console output. The full Assignment 4 endpoint, including
functions and improved logic organization, belongs after Wednesday's recorded
lesson and Thursday refinement.

## AI-Use Boundary

AI can explain unfamiliar syntax, but students should not use AI to generate a
complete program they cannot trace. For Week 4, the minimum student control is:

- name each variable
- explain each output line
- trace why the condition chose a path

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | foundation to JavaScript phase shift | Include in Week 4 prompt packet |
| 2 | Week 3 responsive success path | Include in Week 4 prompt packet |
| 3 | describe vs execute | Include in Week 4 prompt packet |
| 4 | success today | Use SmartArt; no image prompt by default |
| 5 | toolbox | Include in Week 4 prompt packet |
| 6 | parked for later | Include in Week 4 prompt packet |
| 7 | program as instructions | Include in Week 4 prompt packet |
| 9 | console output | Include in Week 4 prompt packet |
| 10 | condition branch | Include in Week 4 prompt packet |
| 11 | demo values and conditions | Include in Week 4 prompt packet |
| 12 | predict-run-observe | Include in Week 4 prompt packet |

## Instructor Timing Notes

- Previous success review: 7-10 minutes
- Phase shift and mental model: 10-12 minutes
- Variables, console, conditions: 15-20 minutes
- Demo: 10-15 minutes
- Lab bridge and evidence: 5-8 minutes

Compress by shortening the review, not by skipping prediction before running.

## Post-Lecture Notes

- Note whether students can open the console.
- Note whether they expect visible page changes.
- Note which syntax errors or prediction mistakes should be addressed in the Wednesday recording.
