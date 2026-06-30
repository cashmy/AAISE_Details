# W06A Debugging Process Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 6
- Session: Monday live
- Deck title: Debugging Process: Things Break And I Can Fix Them
- Phase: Behavior
- Target duration: 55-70 minutes
- Recording expected: no

## Session Type

Monday live lecture.

## Lesson Purpose

Students should leave Monday understanding that debugging is a process for
gathering evidence, not a panic response.

The practical target is intentionally small: reproduce one broken behavior,
read the console clue, compare HTML and JavaScript, make one focused fix, and
verify the result.

## IIM Alignment

Week 6 Monday:

- Debugging as process.
- Print -> Console -> DevTools.
- Prepare Tuesday lab: fix intentionally broken examples.

## Reading Alignment

Week 6 assigned reading:

- Required - JS/JQ: Duckett Chap 10 - Error Handling & Debugging, selected pages on console, common errors, and tracing, pp. 449-465, 480-486
- Reference - JS/JQ: Duckett Chap 10 - Error Handling & Debugging, browser specifics, console editing, and advanced debugging techniques, pp. 466-479

Reading-to-lab bridge:

- Reading gives vocabulary: error, console, log, breakpoint, stack, cause, symptom.
- Lecture demonstrates the simplest useful debugging loop.
- Tuesday lab asks students to identify issues, attempt fixes, and describe what happened.

What students should not try to master yet:

- every DevTools panel
- advanced breakpoints
- stack-trace depth
- performance profiling
- automated testing
- fixing everything at once

## Review / Prior Work Bridge

Previous lab:

- Assignment 5 - DOM Interaction & Events

Success solution:

```text
Assignments/Success_Solutions/Week_05_DOM_Interaction_Events/
```

Review focus:

- show one successful interactive path, not the only correct answer
- test empty input and valid input
- identify selectors, function, event listener, and visible update
- connect to today's question: what do we do when that connection breaks?

## What Counts As Success Today

By the end of the session, students should be able to:

- reproduce one broken behavior
- read one console error as a clue
- compare an HTML id to a JavaScript selector
- make one focused fix
- retest and explain what changed

Success is not fixing every possible bug today.

## Today's Toolbox

Today we will use:

- reproduce
- observe
- console
- error message
- HTML id
- JavaScript selector
- one focused change
- retest

## Parked For Later

Parked for later:

- advanced breakpoints
- full stack traces
- performance tools
- browser compatibility issues
- automated tests
- large debugging sessions

Today: one bug, one clue, one fix, one verification.

## Assignment Supported

Assignment 6 - Debugging & Problem Solving

Monday supports Iteration 1:

- identify at least three issues
- describe what is wrong
- attempt focused fixes
- observe behavior
- isolate problems
- test changes

## Readiness Target

By the end of the session, students should be ready to:

- open the console without fear
- document the symptom before changing code
- compare what the browser reports to the source files
- change one thing at a time
- record whether the fix worked

## Primary Watch Point

Students may jump from symptom directly to random edits.

Reframe:

```text
The symptom tells us what we noticed.
Evidence helps us find the cause.
Fix one likely cause, then retest.
```

## Demo Set

Demo folder:

```text
Demos/Week_06_Debugging_Process/01_monday_broken_selector/
```

Demo files:

- `index.html`
- `styles.css`
- `script.js`
- `fixed_script.js`
- `demo_notes.md`

Delivery:

- Start with the broken version.
- Do not reveal `fixed_script.js` first.
- Click the button and observe failure.
- Read the console error.
- Compare `id="statusButton"` to `#statusBtn`.
- Fix the selector and retest.

## Slide Sequence Overview

1. Things Break - And That Is Information
2. Previous Lab Review / Success Path
3. From Working Interaction To Broken Connection
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. Debugging Is A Loop
8. Symptom Is Not Cause
9. Console Messages Are Clues
10. AI Can Explain Clues, Not Replace Evidence
11. Useful AI Prompt Pattern
12. Compare What Must Match
13. Demo: Broken Selector
14. Verify The Fix
15. Tuesday Lab Bridge
16. Evidence Expectations
17. Closing

## Slide-By-Slide Source

### Slide 1 - Things Break - And That Is Information

Student-visible text:

```text
Debugging is not proof that you failed.

Debugging means:
- something happened
- we can observe it
- the browser may give clues
- one focused change can be tested

Problems are information.
```

**Instructor notes:**

- Start with pressure reduction.
- Week 6 should stabilize confidence after DOM confusion.
- Emphasize process over speed.

**Transition cue:**

- "Before we break something on purpose, let's look at what worked last week."

Visual notes:

- Calm evidence-gathering visual rather than alarm/error imagery.

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Assignment 5 success path:

- JavaScript linked separately
- page elements selected
- click event connected
- input value read
- visible feedback updated
- no console errors

Now we practice recovery when that chain breaks.
```

**Instructor notes:**

- Open the Week 5 success solution.
- Show the planner with empty input and valid input.
- Identify selectors, function, event, and update.

**Transition cue:**

- "The same connection chain also gives us places to investigate when something fails."

Demo connection:

- `Assignments/Success_Solutions/Week_05_DOM_Interaction_Events/`

### Slide 3 - From Working Interaction To Broken Connection

Student-visible text:

```text
A broken interaction may look simple:

- button does nothing
- message does not change
- input is ignored
- layout looks wrong
- console shows an error

Do not guess first.
Observe first.
```

**Instructor notes:**

- Connect directly to Week 5 DOM/event work.
- Keep the message calm: broken behavior is normal.

**Transition cue:**

- "Today's success is one clean debugging loop."

Visual notes:

- Working interaction chain with one broken link highlighted.

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you reproduce the problem
- you read one clue
- you compare the related code
- you make one focused change
- you retest and explain the result
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Do not make this a "fix everything" slide.

**Transition cue:**

- "Here are the debugging tools we actually need today."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- reproduce
- observe
- console
- error message
- HTML id
- JavaScript selector
- one focused change
- retest
```

**Instructor notes:**

- This toolbox is process-oriented.
- Keep DevTools breadth out of the center.

**Transition cue:**

- "And just as important, here is what we are not trying to master today."

Visual notes:

- Debugging toolbox with process tools.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- advanced breakpoints
- full stack traces
- performance tools
- browser compatibility issues
- automated tests
- large debugging sessions

Today: one bug, one clue, one fix.
```

**Instructor notes:**

- The reading includes more than students need for first debugging practice.
- Protect the scope.

**Transition cue:**

- "The basic debugging loop is small enough to practice today."

Visual notes:

- Shelf of advanced debugging tools.

### Slide 7 - Debugging Is A Loop

Student-visible text:

```text
Use the debugging loop:

1. reproduce the problem
2. observe the evidence
3. isolate one likely cause
4. change one thing
5. retest
6. explain what happened
```

**Instructor notes:**

- This is the core Week 6 process.
- Return to it during the demo.

**Transition cue:**

- "The first trap is confusing what we noticed with what caused it."

Visual notes:

- Simple observe-isolate-fix-retest loop.

### Slide 8 - Symptom Is Not Cause

Student-visible text:

```text
Symptom:
"The button does nothing."

Possible causes:
- script file is not linked
- selector does not match
- function is not connected
- code has an earlier error

Name the symptom.
Then gather evidence for the cause.
```

**Instructor notes:**

- This slide should slow students down.
- Use their likely language: "it doesn't work."

**Transition cue:**

- "The console is one place the browser leaves evidence."

Visual notes:

- Symptom card branching into possible causes.

### Slide 9 - Console Messages Are Clues

Student-visible text:

```text
The console may tell you:

- which file had a problem
- which line was involved
- what kind of problem happened
- what value was missing or unexpected

Read the message before changing code.
```

**Instructor notes:**

- Show that console errors are not punishment.
- Avoid deep stack trace explanation.

**Transition cue:**

- "AI can help explain this kind of clue, but only after we give it real evidence."

Visual notes:

- Friendly console clue visual with file, line, and message labels.

### Slide 10 - AI Can Explain Clues, Not Replace Evidence

Student-visible text:

```text
AI can help explain debugging clues.

Useful AI input:
- what you observed
- the exact console error
- the small code section involved
- what you already checked

AI should help you understand possible causes.
It should not replace your evidence or verification.
```

**Instructor notes:**

- This is the formal Week 6 introduction of assisted debugging.
- Tie it to the standard student AI policy: explanation is allowed; unexamined replacement work is not.
- Emphasize that the student still owns the final fix and report.

**Transition cue:**

- "A useful prompt gives AI the same evidence a careful debugger would use."

Visual notes:

- Evidence packet going into an AI explainer, then returning possible causes for the student to test.

### Slide 11 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

I am debugging a beginner web page.

What I observed:
[What I clicked or tried, and what happened]

Console message:
[Paste the exact message]

Relevant code:
[Paste the small HTML/JS section]

What I checked:
[IDs, selectors, script link, spelling]

Please explain what this error means.
Give me possible causes to test.
Do not rewrite the whole project.
```

**Instructor notes:**

- This is a usable prompt pattern for Tuesday's debugging pass.
- Keep the emphasis on explanation and possible causes, not generated fixes.
- Mention that students should paste only the relevant section, not an entire project.

**Transition cue:**

- "For today's bug, the evidence points us toward a mismatch we can verify ourselves."

Visual notes:

- Use the existing `Useful AI Prompt Pattern` slide format if available.

### Slide 12 - Compare What Must Match

Student-visible text:

```text
Some code must match exactly.

HTML:
`id="statusButton"`

JavaScript:
`document.querySelector("#statusButton")`

Small spelling differences can break the connection.
```

**Instructor notes:**

- This prepares the demo bug.
- Emphasize exact comparison, including capitalization and missing letters.

**Transition cue:**

- "Let's debug a selector mismatch without guessing."

Visual notes:

- HTML id and JS selector side by side with matching line.

### Slide 13 - Demo: Broken Selector

Student-visible text:

```text
Demo: Broken Selector

Watch for:
- reproduce the problem
- open the console
- read the error
- compare HTML id to JS selector
- fix one selector
- refresh and retest
```

**Instructor notes:**

- Start with the broken `script.js`.
- Do not show `fixed_script.js` until after the class has reasoned through the bug.
- Type the corrected selector live.

**Transition cue:**

- "The fix only counts after we verify it."

Demo connection:

- `Demos/Week_06_Debugging_Process/01_monday_broken_selector/`

### Slide 14 - Verify The Fix

Student-visible text:

```text
After a fix:

- save the file
- refresh the page
- repeat the original action
- check the console again
- explain what changed

Do not stop at "I changed something."
Stop at "I verified the result."
```

**Instructor notes:**

- Verification is the key habit.
- This supports the debugging report later.

**Transition cue:**

- "Tuesday's lab uses this same loop on more than one issue."

Visual notes:

- Before/after verification check.

### Slide 15 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab: first debugging pass

Your goal:
- identify at least 3 issues
- describe what is wrong
- attempt focused fixes
- test each change
- keep notes on what you observed
```

**Instructor notes:**

- Monday supports the first debugging pass, not the final report yet.
- Tell students they may not fix everything immediately.

**Transition cue:**

- "Your notes matter because debugging is evidence work."

Lab connection:

- Assignment 6 - Iteration 1

### Slide 16 - Evidence Expectations

Student-visible text:

```text
Preserve evidence:

- issue observed
- clue or evidence found
- file or line inspected
- change attempted
- result after retesting

Clear notes are part of the work.
```

**Instructor notes:**

- This prepares the final debugging report.
- Encourage screenshots only when they support explanation.

**Transition cue:**

- "Debugging gets easier when the process is visible."

### Slide 17 - Closing

Student-visible text:

```text
Today:

- broken behavior became evidence
- console messages became clues
- matching code mattered
- one focused fix was verified

Next:
we debug more than one issue without chasing everything at once.
```

**Instructor notes:**

- Close with confidence and process.
- Preview Wednesday's multi-issue debugging without raising anxiety.

**Transition cue:**

- "The goal is not never breaking things. The goal is knowing how to recover."

## Demo Execution Notes

- Use `Demos/Week_06_Debugging_Process/01_monday_broken_selector/`.
- Start with broken `script.js`.
- Click the button before opening code.
- Read the console error.
- Compare `statusButton` and `statusBtn`.
- Fix only the selector, refresh, and retest.

## Lab / Assignment Bridge

Students should use Tuesday to begin Assignment 6:

- identify issues
- describe symptoms
- gather evidence
- attempt focused fixes
- document what happened

## Evidence / Submission Expectations

For Tuesday, students should have notes on at least three identified issues and
attempted fixes. The final required report and verified fixes belong after
Wednesday's recorded lesson and Thursday refinement.

## AI-Use Boundary

AI can help interpret an error message, but students must not skip evidence.
They should provide the error text, describe what they observed, and explain
what they changed.

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | debugging as information | Include in Week 6 prompt packet |
| 2 | Week 5 success path | Include in Week 6 prompt packet |
| 3 | broken connection | Include in Week 6 prompt packet |
| 4 | success today | Use SmartArt; no image prompt by default |
| 5 | toolbox | Include in Week 6 prompt packet |
| 6 | parked for later | Include in Week 6 prompt packet |
| 7 | debugging loop | Include in Week 6 prompt packet |
| 8 | symptom vs cause | Include in Week 6 prompt packet |
| 9 | console clue | Include in Week 6 prompt packet |
| 10 | AI as debugging explainer | Include in Week 6 prompt packet |
| 11 | useful AI prompt pattern | Use existing slide format; optional image prompt |
| 12 | exact match comparison | Include in Week 6 prompt packet |
| 13 | demo broken selector | Include in Week 6 prompt packet |
| 14 | verify the fix | Include in Week 6 prompt packet |

## Instructor Timing Notes

- Previous success review: 7-10 minutes
- Debugging mindset and loop: 12-15 minutes
- Console and symptom/cause: 10-12 minutes
- AI-as-explainer boundary: 2-4 minutes
- Useful AI prompt pattern: 3-5 minutes
- Demo: 12-18 minutes
- Lab bridge and evidence: 5-8 minutes

If delivery time is tight, skim the previous success review or verbally bridge
the AI boundary/prompt-pattern slides. Do not skip retest, verification, or
evidence expectations.

## Post-Lecture Notes

- Note whether students read errors before changing code.
- Note whether students compare exact selector spelling.
- Use those observations to shape the Wednesday multi-issue recording.
