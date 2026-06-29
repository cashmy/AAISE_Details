# W04B JavaScript Logic Iteration Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 4
- Session: Wednesday recorded
- Deck title: JavaScript Logic Iteration: Functions And Decisions
- Phase: Behavior
- Target duration: 25-35 minutes
- Recording expected: yes

## Session Type

Wednesday recorded lecture.

## Lesson Purpose

Students should see Monday's values-and-condition program become clearer and
more reusable by moving logic into a function.

The instructional move is:

```text
one decision written once -> named function -> call with values -> read result
```

## IIM Alignment

Week 4 Wednesday:

- Address common logic mistakes.
- Reinforce mental execution of code.
- Prepare Thursday lab: small logic challenges and confidence in JS thinking.

## Reading Alignment

Week 4 assigned reading:

- Required - JS/JQ: Duckett Chap 1 - The ABC of Programming, selected pages on scripts, variables, and basic program thinking, pp. 36-52
- Required - JS/JQ: Duckett Chap 2 - Basic JavaScript Instructions, pp. 53-84
- Skim - JS/JQ: Duckett Chap 1 - The ABC of Programming, pp. 11-35
- Skim - JS/JQ: Duckett Chap 4 - Decisions & Loops, selected pages on `if` statements only, pp. 145-163
- Reference - JS/JQ: Duckett Chap 3 - Functions, Methods & Objects, pp. 85-144, use later as needed
- Reference - JS/JQ: Duckett Chap 4 - Decisions & Loops, selected pages on `switch`, `while`, and `for` loops, pp. 164-182

What this recording reinforces:

- programs execute step by step
- variables store values
- conditions choose paths
- functions package reusable logic
- `return` sends a value back

What students should not try to master yet:

- DOM selection
- event listeners
- complex function architecture
- loops
- objects
- jQuery

## Review / Prior Work Bridge

Monday introduced:

```text
variables -> console output -> if / else decision
```

Wednesday grows that into:

```text
decision logic -> function -> function call -> returned message
```

## What Counts As Success Today

By the end of the recording, students should be able to:

- distinguish defining a function from calling a function
- recognize a parameter as input to a function
- explain that `return` sends a result back
- change one input value and predict the output
- improve code clarity without adding page interaction

Success is clearer logic, not DOM behavior.

## Today's Toolbox

Today we will use:

- function
- parameter
- argument
- `return`
- function call
- meaningful names
- console output
- predict, run, observe

## Parked For Later

Parked for later:

- DOM and page elements
- button events
- loops
- objects
- jQuery
- larger app organization

Today, functions help us organize logic before the page becomes interactive.

## Assignment Supported

Assignment 4 - Introduction to JavaScript

Wednesday supports the concept focus and Thursday refinement:

- organize code so it is easier to follow
- use meaningful variable names
- add at least one function
- improve or expand a condition
- produce understandable console output
- reflect on what feels different from HTML/CSS

## Readiness Target

By the end of the recording, students should be ready to:

- revise their first JavaScript program
- move a decision into a named function
- call the function with stored values
- test at least two input changes
- explain the result in plain language

## Primary Watch Point

Students may confuse a function definition with a function call.

Reframe:

```text
Defining a function teaches JavaScript the steps.
Calling a function asks JavaScript to run those steps now.
```

## Demo Set

Demo folder:

```text
Demos/Week_04_JavaScript_Logic/02_wednesday_function_decision/
```

Demo files:

- `index.html`
- `script.js`
- `demo_notes.md`

Delivery:

- Start from Monday's decision idea.
- Type the function definition and function call live.
- Change values and predict the console output.
- Emphasize `return` as the value sent back.

## Slide Sequence Overview

1. Reconnect To Monday
2. The Working Problem: Logic Gets Repeated Or Messy
3. What Counts As Success Today
4. Functions Package A Small Job
5. Today's Toolbox
6. Define Versus Call
7. Return Sends A Value Back
8. Demo: Function Decision
9. Common Logic Mistakes
10. Thursday Lab Refinement
11. Evidence And Reflection
12. How To Read Next Week's Material
13. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- variables stored values
- console output made values visible
- `if / else` chose a path

Today:
- the same decision becomes reusable
- functions help organize logic
```

**Instructor notes:**

- Keep the recording tightly connected to Monday.
- Students should feel this is an iteration of the same idea.

**Transition cue:**

- "Once code starts working, the next question is whether we can read and reuse it."

Visual notes:

- Monday decision code moving into a named function.

### Slide 2 - The Working Problem: Logic Gets Repeated Or Messy

Student-visible text:

```text
Working code can still be hard to follow.

Common signs:
- names are vague
- output is unclear
- the same decision appears more than once
- changing one value is confusing
- the result is hard to explain
```

**Instructor notes:**

- This sets up refinement without shaming first attempts.
- Connect to Thursday's task: improve and organize.

**Transition cue:**

- "Today's success is making a small program easier to reason about."

Visual notes:

- Small messy logic block becoming a named reusable block.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- a function has one clear job
- inputs are named clearly
- the function is called
- `return` sends a result back
- console output is explainable
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Make clear that the page still does not need to change visibly.

**Transition cue:**

- "A function is just a way to name a small job."

### Slide 4 - Functions Package A Small Job

Student-visible text:

```text
A function packages steps under a name.

Use a function when:
- a task has a clear purpose
- the logic may be reused
- you want code to read like an idea

Good function names explain the job.
```

**Instructor notes:**

- Avoid deep abstraction. Keep it practical.
- Use `getProgressMessage` as a readable name.

**Transition cue:**

- "But there are two moments students often mix up: defining and calling."

Visual notes:

- Function as labeled recipe card or small machine with input/output.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- function
- parameter
- argument
- `return`
- function call
- meaningful names
- console output
- predict, run, observe
```

**Instructor notes:**

- This is enough vocabulary for the function demo.
- Do not expand into methods and objects today.

**Transition cue:**

- "The most important distinction is define versus call."

Visual notes:

- Function-focused JavaScript toolbox.

### Slide 6 - Define Versus Call

Student-visible text:

```text
Define:
"Here are the steps."

Call:
"Run those steps now."

Example:

`function getProgressMessage(...) { ... }`
`const message = getProgressMessage(score, lateSubmissions);`
```

**Instructor notes:**

- Point to the function name appearing in both places.
- Explain that nothing useful comes back until the function is called.

**Transition cue:**

- "When the function runs, it needs a way to send the answer back."

Visual notes:

- Two panels: define the recipe, then use the recipe.

### Slide 7 - Return Sends A Value Back

Student-visible text:

```text
`return` sends a result back to the caller.

The function can decide:
- "On track"
- "Needs attention"
- "Schedule support"

Then another line can store or print that result.
```

**Instructor notes:**

- Use the demo messages.
- Keep `return` separate from `console.log()`: return gives a value; log shows output.

**Transition cue:**

- "Now let's turn Monday's decision into a function."

Visual notes:

- Input values entering a function and message coming back.

### Slide 8 - Demo: Function Decision

Student-visible text:

```text
Demo: Function Decision

Watch for:
- function definition
- parameters as inputs
- `if` decisions inside the function
- `return` message
- function call
- console output after the call
```

**Instructor notes:**

- Type the function definition and call live.
- Change `score` and `lateSubmissions` and predict the result.
- Pause to distinguish definition from call.

**Transition cue:**

- "The code becomes easier when each part has a job we can name."

Demo connection:

- `Demos/Week_04_JavaScript_Logic/02_wednesday_function_decision/`

### Slide 9 - Common Logic Mistakes

Student-visible text:

```text
Watch for these beginner mistakes:

- using a name before it exists
- forgetting parentheses in a function call
- expecting `return` to print by itself
- changing a value but not refreshing
- reading syntax without tracing values
```

**Instructor notes:**

- Use one or two of these as live verbal examples.
- Avoid overwhelming students with every possible error.

**Transition cue:**

- "Thursday's work is to improve the program, not make it larger for its own sake."

Visual notes:

- Friendly checklist of common beginner logic issues.

### Slide 10 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab: improve the program

Your goal:
- use meaningful names
- add or improve one function
- improve or expand one condition
- keep console output understandable
- make the logic easier to explain
```

**Instructor notes:**

- Now it is safe to present the full weekly endpoint.
- Emphasize clarity over cleverness.

**Transition cue:**

- "Your final submission should make the logic visible to someone else."

Lab connection:

- Assignment 4 - Iteration 2

### Slide 11 - Evidence And Reflection

Student-visible text:

```text
Final Assignment 4 evidence:

- `.js` file only
- code runs without errors
- output appears in the console
- variables, condition, and function are present
- reflection explains what felt different from HTML/CSS
```

**Instructor notes:**

- Reinforce that visible page changes are not required.
- The reflection is useful because this is the first programming week.

**Transition cue:**

- "Next week we connect this logic to the page."

### Slide 12 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- read for the big idea of the DOM as a bridge
- notice how JavaScript can find one page element
- notice basic click-event thinking

Skim:
- do not memorize every DOM method or event type
- look for examples that feel close to buttons and page text

Reference:
- jQuery is recognition and helper-library awareness, not the main model

Before next time:
bring one question about how code connects to visible page behavior.
```

**Instructor notes:**

- Week 5 is DOM and basic events.
- Keep the warning against exhaustive DOM/event memorization.

**Transition cue:**

- "This week, code ran in the console. Next week, code reaches into the page."

### Slide 13 - Closing

Student-visible text:

```text
This week:

- JavaScript became a programming language
- values changed program behavior
- conditions chose paths
- functions organized logic

Next:
JavaScript connects to HTML through the DOM.
```

**Instructor notes:**

- End with the bridge to Week 5.
- Keep the distinction clear: no DOM yet, DOM next.

**Transition cue:**

- "The page is ready. The program is ready. Next, they meet."

## Demo Execution Notes

- Use `Demos/Week_04_JavaScript_Logic/02_wednesday_function_decision/`.
- Type `function getProgressMessage(currentScore, lateCount)` live.
- Explain parameters as names for incoming values.
- Pause after the function definition and ask whether anything has run yet.
- Type the function call and console output, then change values and retest.

## Lab / Assignment Bridge

Students should use Thursday to finish Assignment 4:

- revise their first program
- add or improve a function
- expand one condition
- make output clearer
- submit the `.js` file and reflection

## Evidence / Submission Expectations

Assignment 4 final evidence should show:

- a runnable `.js` file
- at least two variables
- at least one conditional statement
- at least one function
- understandable console output
- a short reflection on how programming differs from HTML/CSS

## AI-Use Boundary

AI can explain a confusing line or compare two possible function names.
Students should not submit AI-generated code they cannot trace. They must be
able to explain:

- what each variable stores
- when the function runs
- why the condition chooses a path
- what value is returned or printed

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | Monday logic into function iteration | Include in Week 4 prompt packet |
| 2 | messy to clearer logic | Include in Week 4 prompt packet |
| 3 | success today | Use SmartArt; no image prompt by default |
| 4 | function packages small job | Include in Week 4 prompt packet |
| 5 | toolbox | Include in Week 4 prompt packet |
| 6 | define versus call | Include in Week 4 prompt packet |
| 7 | return sends value back | Include in Week 4 prompt packet |
| 8 | demo function decision | Include in Week 4 prompt packet |
| 9 | common logic mistakes | Include in Week 4 prompt packet |
| 13 | JS to DOM bridge | Include in Week 4 prompt packet |

## Instructor Timing Notes

- Reconnect and problem framing: 5-7 minutes
- Function concept: 8-10 minutes
- Demo: 10-15 minutes
- Common mistakes and lab bridge: 7-10 minutes
- Next-reading guidance and close: 3-5 minutes

Compress by shortening common mistakes, not by skipping the define-versus-call
distinction.

## Post-Lecture Notes

- Note whether students distinguish `return` from `console.log()`.
- Note whether students confuse defining a function with calling it.
- Use Week 5 to remind students that working console logic comes before visible page behavior.
