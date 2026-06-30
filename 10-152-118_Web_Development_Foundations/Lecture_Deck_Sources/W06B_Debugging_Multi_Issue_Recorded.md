# W06B Debugging Multi-Issue Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 6
- Session: Wednesday recorded
- Deck title: Debugging Multi-Issue: Cause, Fix, Verify
- Phase: Behavior
- Target duration: 25-35 minutes
- Recording expected: yes

## Session Type

Wednesday recorded lecture.

## Lesson Purpose

Students should see Monday's single-bug debugging process scale to a small
multi-issue example without losing the evidence-first habit.

The instructional move is:

```text
one obvious failure -> first cause fixed -> retest -> next issue appears -> document verified fixes
```

## IIM Alignment

Week 6 Wednesday:

- Read errors.
- Trace cause versus symptom.
- Prepare Thursday lab: mixed HTML/CSS/JS bugs and explanation of fixes.

## Reading Alignment

Week 6 assigned reading:

- Required - JS/JQ: Duckett Chap 10 - Error Handling & Debugging, selected pages on console, common errors, and tracing, pp. 449-465, 480-486
- Reference - JS/JQ: Duckett Chap 10 - Error Handling & Debugging, browser specifics, console editing, and advanced debugging techniques, pp. 466-479

What this recording reinforces:

- fix one issue at a time
- retest after each change
- JavaScript, HTML, and CSS issues can overlap
- not every visible problem is the current cause
- debugging reports should explain evidence and verification

What students should not try to master yet:

- every DevTools feature
- advanced breakpoint workflow
- automated testing
- performance diagnosis
- complete code refactoring

## Review / Prior Work Bridge

Monday introduced:

```text
reproduce -> read clue -> compare source -> fix one cause -> retest
```

Wednesday grows that into:

```text
prioritize issue -> fix -> retest -> find next issue -> document the process
```

## What Counts As Success Today

By the end of the recording, students should be able to:

- separate symptom from likely cause
- fix one issue before chasing the next
- use `console.log()` as evidence
- verify that a fix actually worked
- write a short debugging report entry

Success is process clarity, not fixing the most bugs fastest.

## Today's Toolbox

Today we will use:

- issue list
- priority
- console error
- `console.log()`
- selector check
- condition check
- CSS mismatch check
- verification note

## Parked For Later

Parked for later:

- advanced breakpoint sessions
- automated test suites
- linting tools
- performance debugging
- network debugging
- refactoring large codebases

Today: choose one issue, fix one cause, verify before moving on.

## Assignment Supported

Assignment 6 - Debugging & Problem Solving

Wednesday supports Iteration 2 and final submission:

- fix at least two confirmed issues completely
- use console output, element checks, and layout verification
- document the issue, investigation, fix, and verification
- submit updated website and debugging report

## Readiness Target

By the end of the recording, students should be ready to:

- prioritize a mixed set of bugs
- fix JavaScript connection issues before cosmetic issues when appropriate
- retest after each fix
- write a report that makes the investigation visible

## Primary Watch Point

Students may try to fix every file at once.

Reframe:

```text
Change one likely cause.
Retest.
Then decide what the next issue is.
```

## Demo Set

Demo folder:

```text
Demos/Week_06_Debugging_Process/02_wednesday_multi_issue_debugging/
```

Demo files:

- `index.html`
- `styles.css`
- `script.js`
- `fixed_script.js`
- `demo_notes.md`

Known issues:

- JavaScript selects `#addTaskButton`, but the HTML id is `addButton`.
- Empty-input condition uses assignment `=` instead of comparison `===`.
- CSS has `.status`, but the HTML uses `id="status"`.

Delivery:

- Start with the broken version.
- Fix the selector first.
- Retest before addressing the condition.
- Fix `=` to `===`.
- Address the CSS mismatch only after interaction works.
- Compare to `fixed_script.js` at the end.

## Slide Sequence Overview

1. Reconnect To Monday
2. The Working Problem: More Than One Thing Can Be Wrong
3. What Counts As Success Today
4. Prioritize The First Cause
5. Today's Toolbox
6. Do Not Fix Everything At Once
7. Console Logs As Evidence
8. Proper `console.log()` Format
9. Demo: Multi-Issue Debugging
10. Retest After Each Fix
11. A Good AI Debugging Prompt
12. Debugging Report Pattern
13. Thursday Lab Refinement
14. Evidence And Submission
15. How To Read Next Week's Material
16. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- reproduced one problem
- read one console clue
- compared HTML and JavaScript
- fixed one selector
- verified the result

Today:
we keep that process when more than one issue appears.
```

**Instructor notes:**

- Make the continuity explicit.
- Students should see the same loop, not a new debugging theory.

**Transition cue:**

- "The hard part is not that there are many bugs. The hard part is deciding what to test first."

Visual notes:

- One-bug loop expanding to a small issue list.

### Slide 2 - The Working Problem: More Than One Thing Can Be Wrong

Student-visible text:

```text
A page can have multiple issues:

- JavaScript selector mismatch
- condition logic error
- CSS selector mismatch
- confusing user feedback

Fixing one issue may reveal the next.
That is normal.
```

**Instructor notes:**

- Normalize layered issues.
- Emphasize that debugging is sequential.

**Transition cue:**

- "So today's success is not speed. It is order."

Visual notes:

- Small stack of issue cards, one being selected first.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you choose one likely cause first
- you make one focused change
- you retest before moving on
- you document what happened
- at least two fixes are verified
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Tie directly to Assignment 6 final report.

**Transition cue:**

- "The first decision is priority: what blocks the rest of the behavior?"

### Slide 4 - Prioritize The First Cause

Student-visible text:

```text
Start with the issue that blocks testing.

Good first checks:
- script file linked?
- console error present?
- selector matches HTML?
- event listener connected?

Cosmetic issues can wait until behavior works.
```

**Instructor notes:**

- This prepares the CSS mismatch in the demo.
- Make clear that CSS matters, but priority matters too.

**Transition cue:**

- "Here are today's tools for that ordered investigation."

Visual notes:

- Debugging priority ladder: blocking behavior before styling.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- issue list
- priority
- console error
- `console.log()`
- selector check
- condition check
- CSS mismatch check
- verification note
```

**Instructor notes:**

- Keep `console.log()` as an evidence tool, not a permanent final-code feature.

**Transition cue:**

- "The biggest danger is changing several things before knowing what worked."

Visual notes:

- Multi-issue debugging toolbox.

### Slide 6 - Do Not Fix Everything At Once

Student-visible text:

```text
Avoid this:
- change selector
- change condition
- change CSS
- refresh once
- hope it works

Use this:
- change one likely cause
- retest
- record result
- then choose the next issue
```

**Instructor notes:**

- This is the anti-random-editing slide.
- Pair it with a calm tone; students often do this under stress.

**Transition cue:**

- "When the behavior is confusing, logs can make the path visible."

Visual notes:

- Chaotic multi-edit path contrasted with orderly one-change loop.

### Slide 7 - Console Logs As Evidence

Student-visible text:

```text
`console.log()` can answer:

- did this function run?
- what value did the input contain?
- which branch did the condition choose?
- did the code reach this line?

Use logs to test a question.
Then remove or clean them later.
```

**Instructor notes:**

- Connect to Week 4 console work.
- Keep this practical and focused.

**Transition cue:**

- "Before the demo, let's make the log messages readable enough to be useful."

Visual notes:

- Console log checkpoints along a code path.

### Slide 8 - Proper `console.log()` Format

Student-visible text:

```text
Use logs that explain what you are checking.

Less useful:
`console.log(taskText);`

More useful:
`console.log("Task text:", taskText);`

Best habit:
- label the value
- log one question at a time
- remove extra logs after debugging
```

**Instructor notes:**

- Bridge from Python's print-debugging habit to JavaScript's console output.
- Emphasize labels: unlabeled values become confusing once there are several logs.
- Keep this as a refresher, not a logging deep dive.

**Transition cue:**

- "Now the demo logs can tell us what question each checkpoint is answering."

Visual notes:

- Side-by-side less useful versus more useful console log example.

### Slide 9 - Demo: Multi-Issue Debugging

Student-visible text:

```text
Demo: Multi-Issue Debugging

Watch for:
- first visible symptom
- first console clue
- selector mismatch
- retest after selector fix
- condition error
- CSS issue handled after behavior works
```

**Instructor notes:**

- Start with broken `script.js`.
- Do not show `fixed_script.js` first.
- Work through the issues in order.

**Transition cue:**

- "The order matters because each retest tells us what to investigate next."

Demo connection:

- `Demos/Week_06_Debugging_Process/02_wednesday_multi_issue_debugging/`

### Slide 10 - Retest After Each Fix

Student-visible text:

```text
After each change, ask:

- Did the original symptom change?
- Did the console error change?
- Did a new issue appear?
- Is the current fix verified?
- What is the next smallest check?

Retesting turns edits into evidence.
```

**Instructor notes:**

- This is the key transfer from demo to lab.
- Encourage students to write these observations down.

**Transition cue:**

- "If you ask AI for help, these observations are what make the prompt useful."

Visual notes:

- Fix/retest/evidence cards.

### Slide 11 - A Good AI Debugging Prompt

Student-visible text:

```text
A useful AI debugging prompt includes:

- observed symptom
- exact console error
- small relevant code section
- what you already checked
- what kind of help you want

Ask for explanation and possible causes.
Do not ask for a replacement project.
```

**Instructor notes:**

- This models the IIM Week 6 boundary: AI as explainer only.
- Encourage students to ask for understanding, not pasted fixes.
- Reinforce that the report still needs their evidence, chosen fix, and verification.

**Transition cue:**

- "Whether AI helped explain the clue or not, the final report still needs your evidence."

Visual notes:

- Prompt card with fields feeding into an AI explainer, then returning possible causes for the student to test.

### Slide 12 - Debugging Report Pattern

Student-visible text:

```text
Debugging report pattern:

Issue:
- what was wrong?

Evidence:
- how did you identify it?

Fix:
- what did you change?

Verification:
- how do you know it works now?
```

**Instructor notes:**

- This is the assignment report structure.
- Make it clear that fixed code alone is not enough this week.

**Transition cue:**

- "Thursday's lab is where the report and final fixes come together."

Visual notes:

- Four-part report template.

### Slide 13 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab: verified fixes

Your goal:
- fix at least 2 confirmed issues completely
- use console output or inspection as evidence
- verify the behavior after each fix
- document issue, evidence, fix, and verification
```

**Instructor notes:**

- Now it is safe to name the full weekly endpoint.
- Stress confirmed and verified.

**Transition cue:**

- "Your final submission should show both the repaired site and your thinking."

Lab connection:

- Assignment 6 - Iteration 2

### Slide 14 - Evidence And Submission

Student-visible text:

```text
Final Assignment 6 evidence:

- updated HTML, CSS, and JS
- site runs with fixes applied
- at least two issues fixed correctly
- debugging report included
- reflection explains how your problem-solving changed
```

**Instructor notes:**

- Mention that screenshots may support the report but are not a substitute for explanation.

**Transition cue:**

- "Next week, we use what we learned from debugging to write cleaner behavior."

### Slide 15 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- read functions as a way to organize behavior
- notice scope, dot notation, and document as a built-in object

Reference:
- objects and built-in methods are there when you need them
- do not memorize every method

Before next time:
bring one piece of interaction code that could be made clearer.
```

**Instructor notes:**

- Week 7 moves from working/fixed behavior to cleaner structured behavior.
- Keep function reading purposeful.

**Transition cue:**

- "Debugging tells us where code is hard to understand. Next week, we make code easier to maintain."

### Slide 16 - Closing

Student-visible text:

```text
This week:

- problems became evidence
- console messages became clues
- fixes were verified
- reports explained the process

Next:
working code becomes cleaner code.
```

**Instructor notes:**

- Close by stabilizing confidence.
- Connect debugging to maintainability.

**Transition cue:**

- "The best debugging lesson is often the code structure you improve afterward."

## Demo Execution Notes

- Use `Demos/Week_06_Debugging_Process/02_wednesday_multi_issue_debugging/`.
- Start with broken `script.js`.
- Fix `#addTaskButton` to `#addButton` first.
- Retest before fixing the condition.
- Fix `taskText = ""` to `taskText === ""`.
- Address `.status` versus `id="status"` only after the interaction works.

## Lab / Assignment Bridge

Students should use Thursday to finish Assignment 6:

- verify at least two fixes
- document issue/evidence/fix/verification
- submit repaired site and report
- reflect on changed problem-solving process

## Evidence / Submission Expectations

Assignment 6 final evidence should show:

- repaired HTML/CSS/JS
- no unresolved console errors for the fixed behavior
- debugging report with at least two issues
- explanation of how each issue was identified and fixed

## AI-Use Boundary

AI can help interpret error messages or suggest possible causes. Students still
need to provide their own observed symptom, evidence, chosen fix, and
verification result.

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | one bug to issue list | Include in Week 6 prompt packet |
| 2 | multiple issue stack | Include in Week 6 prompt packet |
| 3 | success today | Use SmartArt; no image prompt by default |
| 4 | priority ladder | Include in Week 6 prompt packet |
| 5 | toolbox | Include in Week 6 prompt packet |
| 6 | one fix at a time | Include in Week 6 prompt packet |
| 7 | console logs as evidence | Include in Week 6 prompt packet |
| 8 | proper console.log format | Include in Week 6 prompt packet |
| 9 | demo multi-issue debugging | Include in Week 6 prompt packet |
| 10 | retest after each fix | Include in Week 6 prompt packet |
| 11 | good AI debugging prompt | Include in Week 6 prompt packet |
| 12 | report pattern | Include in Week 6 prompt packet |
| 16 | cleaner code bridge | Include in Week 6 prompt packet |

## Instructor Timing Notes

- Reconnect and problem framing: 5-7 minutes
- Prioritization and process: 8-10 minutes
- Console log format refresher: 3-5 minutes
- Demo: 15-20 minutes
- AI prompt pattern: 3-5 minutes
- Report pattern and lab bridge: 7-10 minutes
- Next-reading guidance and close: 3-5 minutes

If recording time is tight, skim the issue-list discussion or verbally bridge
the AI prompt pattern. Do not skip retesting, the report pattern, or final
evidence expectations.

## Post-Lecture Notes

- Note whether students document evidence or only final changes.
- Note whether students chase CSS before JavaScript blockers.
- Use Week 7 to turn repeated debugging pain points into code-organization examples.
