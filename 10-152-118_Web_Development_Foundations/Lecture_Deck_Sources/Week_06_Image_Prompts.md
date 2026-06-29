# Week 6 Image Generation Prompts

**10-152-118 Web Development Foundations**

---

# Purpose

This companion artifact expands the image notes from the Week 6 deck sources
into explicit image-generation prompts for browser-based ChatGPT image
generation.

Primary workflow:

- Copy one prompt block at a time into the browser-based ChatGPT image tool.
- Use Codex image generation only as a fallback if the browser image result is
  significantly unusable.
- Do not generate images for `What Counts As Success Today`; use the standard
  course SmartArt / built-in graphic pattern for that slide.
- Preserve slide numbering as placement guidance for the final PowerPoint
  sequence.
- Reject any image that makes debugging look scary, punitive, or like an
  advanced DevTools certification. Week 6 is calm evidence gathering, focused
  fixes, retesting, and explanation.

Source decks:

- `W06A_Debugging_Process_Live.md`
- `W06B_Debugging_Multi_Issue_Recorded.md`

Global style guidance:

- clean instructional PowerPoint visual
- white or very light background
- modern, flat, classroom-friendly style
- large readable labels
- minimal decorative detail
- restrained SWTC-friendly colors: navy, teal, warm gold, white, soft gray
- no dark hacker/cyber imagery
- no red alarm/error storm imagery
- no dense stack traces or intimidating terminal screens
- no complex DevTools screenshots

---

# Week 6 Monday Live Prompts

## W06A Slide 1 - Debugging As Information

```text
Create a clean instructional PowerPoint visual showing debugging as calm information gathering.

Use a white or very light background. Show a simple broken interaction as an evidence card, not a disaster. Include labeled clues:

- observed behavior
- console clue
- source comparison
- focused fix
- retest

Add a small note:
"Problems are information."

Use a calm classroom-friendly flat style with restrained navy, teal, warm gold, white, and soft gray.

Avoid scary red error imagery, dark hacker/cyber visuals, broken-glass screens, dense stack traces, or panic/failure symbolism.
```

## W06A Slide 2 - Week 5 Success Path

```text
Create a clean instructional PowerPoint visual showing one successful Week 5 DOM interaction path.

Use a white or very light background. Show a simple page interaction chain:

- input value
- button click
- JavaScript function
- visible feedback

Add a small check mark near "no console errors."

Add a small note:
"One successful path. Not the only answer."

The tone should support revision and recovery.

Avoid advanced app UI, complex forms, jQuery, frameworks, or dense code.
```

## W06A Slide 3 - Broken Connection

```text
Create a clean instructional PowerPoint visual showing a previously working DOM connection with one broken link.

Use a white or very light background. Show a chain:

HTML element -> selector -> event -> function -> visible update

Highlight one broken link between selector and HTML element, but keep the tone calm and diagnostic.

Add a small note:
"Find the broken connection before changing everything."

Use large readable labels and a modern flat classroom-friendly style.

Avoid alarm icons, red error storms, dark terminal imagery, or complex DOM trees.
```

## W06A Slide 5 - Debugging Toolbox

```text
Create a clean instructional PowerPoint visual showing today's beginner debugging toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with today's active tools:

- reproduce
- observe
- console
- error message
- HTML id
- JS selector
- one focused change
- retest

Make the tools approachable and clearly labeled.

Use restrained SWTC-friendly colors and large readable labels.

Avoid advanced breakpoints, stack traces, performance tools, automated tests, dark terminal imagery, or a parked-for-later shelf.
```

## W06A Slide 6 - Parked For Later

```text
Create a clean instructional PowerPoint visual showing advanced debugging topics parked for later.

Use a white or very light background. Show a calm bookshelf or shelf with separate cards labeled:

- advanced breakpoints
- full stack traces
- performance tools
- browser compatibility
- automated tests
- large debugging sessions

Add a small note:
"Not today. First, one bug, one clue, one fix."

The tone should reduce overload.

Avoid scary errors, dark cyber imagery, dense code, or mixing these parked topics into the active toolbox.
```

## W06A Slide 7 - Debugging Loop

```text
Create a clean instructional PowerPoint visual showing a beginner debugging loop.

Use a white or very light background. Show a circular loop with six steps:

1. reproduce
2. observe evidence
3. isolate one cause
4. change one thing
5. retest
6. explain

Add a small note:
"Debugging is a process, not a panic response."

Use a modern flat classroom-friendly style with large readable labels.

Avoid complex engineering diagrams, dark terminal imagery, or red emergency visuals.
```

## W06A Slide 8 - Symptom Versus Cause

```text
Create a clean instructional PowerPoint visual distinguishing symptom from cause.

Use a white or very light background. Show one large card labeled:
Symptom: "The button does nothing."

Show smaller possible cause cards:

- script not linked
- selector mismatch
- event not connected
- earlier code error

Add a small note:
"Name the symptom. Gather evidence for the cause."

Use large readable labels and a calm classroom-friendly style.

Avoid alarm imagery, medical imagery, dense code, or complex troubleshooting charts.
```

## W06A Slide 9 - Console Clue

```text
Create a clean instructional PowerPoint visual showing a browser console message as a clue.

Use a white or very light background. Show a simplified console panel with labeled parts:

- file
- line
- message
- clue

Do not use real stack traces. Use a simple beginner-friendly placeholder error.

Add a small note:
"Read the message before changing code."

Use a supportive classroom-friendly style with large readable labels.

Avoid dark terminal screens, scary red errors, dense stack traces, or hacker imagery.
```

## W06A Slide 10 - AI As Debugging Explainer

```text
Create a clean instructional PowerPoint visual showing AI as a bounded debugging explainer.

Use a white or very light background. Show a student evidence packet going into an AI explanation panel. The evidence packet should include labeled cards:

- observed symptom
- exact console error
- small code section
- what I checked

The AI panel should return:

- possible causes
- explanation
- questions to test

Add a small note:
"AI can explain clues. You still verify the fix."

Use a calm classroom-friendly flat style with large readable labels and restrained navy, teal, warm gold, white, and soft gray.

Avoid robot characters, magic imagery, full-code replacement visuals, dark hacker imagery, or anything that suggests AI is doing the assignment for the student.
```

## W06A Slide 11 - Exact Match Comparison

```text
Create a clean instructional PowerPoint visual comparing an HTML id and a JavaScript selector.

Use a white or very light background. Show two side-by-side cards:

HTML:
id="statusButton"

JavaScript:
querySelector("#statusButton")

Draw a matching line between the two exact names.

Add a small note:
"Small spelling differences can break the connection."

Use large readable labels and a modern flat classroom-friendly style.

Avoid dense code, complex DOM trees, jQuery, or intimidating error visuals.
```

## W06A Slide 12 - Demo Broken Selector

```text
Create a clean instructional PowerPoint visual for a live demo named "Broken Selector."

Use a white or very light background. Show a simple page with a "Show status" button and a message area. Beside it, show a small comparison:

HTML id: statusButton
JS selector: statusBtn

Highlight the mismatch calmly.

Add a small note:
"Compare the names before guessing."

Use a classroom-friendly flat style with large readable labels.

Avoid red error storms, dense code, dark terminal imagery, or complex DevTools screens.
```

## W06A Slide 13 - Verify The Fix

```text
Create a clean instructional PowerPoint visual showing verification after a debugging fix.

Use a white or very light background. Show a before/after sequence:

Before: button does nothing
Fix: selector corrected
After: status message changes

Include a small checklist:

- save
- refresh
- repeat original action
- check console
- explain result

Add a small note:
"A fix counts after verification."

Use large readable labels and a calm classroom-friendly style.

Avoid trophy imagery, alarm visuals, dense code, or advanced testing dashboards.
```

---

# Week 6 Wednesday Recorded Prompts

## W06B Slide 1 - One Bug To Issue List

```text
Create a clean instructional PowerPoint visual showing Monday's single-bug debugging loop expanding to a small issue list.

Use a white or very light background. On the left, show one issue card labeled "selector mismatch." On the right, show a short ordered issue list:

1. selector mismatch
2. condition error
3. CSS mismatch

Add a small note:
"Same process. More than one issue."

Use large readable labels and a modern flat classroom-friendly style.

Avoid chaotic bug swarms, scary errors, dark terminals, or dense code.
```

## W06B Slide 2 - Multiple Issue Stack

```text
Create a clean instructional PowerPoint visual showing a page with multiple layered issues.

Use a white or very light background. Show three calm issue cards stacked vertically:

- JavaScript selector mismatch
- condition logic error
- CSS selector mismatch

Add a small note:
"Fixing one issue may reveal the next."

Use a supportive classroom-friendly style with restrained navy, teal, warm gold, white, and soft gray.

Avoid panic imagery, red alert graphics, dark cyber imagery, or complex stack traces.
```

## W06B Slide 4 - Priority Ladder

```text
Create a clean instructional PowerPoint visual showing debugging priority.

Use a white or very light background. Show a simple ladder or ordered stack:

1. script linked?
2. console error?
3. selector matches?
4. event connected?
5. condition logic?
6. styling issue?

Add a small note:
"Start with what blocks testing."

Use large readable labels and a calm classroom-friendly style.

Avoid complex flowcharts, emergency visuals, or dense code.
```

## W06B Slide 5 - Multi-Issue Debugging Toolbox

```text
Create a clean instructional PowerPoint visual showing today's multi-issue debugging toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with today's active tools:

- issue list
- priority
- console error
- console.log()
- selector check
- condition check
- CSS mismatch check
- verification note

Make the tools approachable and clearly labeled.

Use restrained SWTC-friendly colors and large readable labels.

Avoid automated tests, performance tools, network panels, dark terminal imagery, or a parked-for-later shelf.
```

## W06B Slide 6 - One Fix At A Time

```text
Create a clean instructional PowerPoint visual contrasting chaotic multi-edit debugging with a calm one-fix-at-a-time process.

Use a white or very light background. Left side: tangled arrows labeled "change everything." Right side: orderly steps:

1. change one cause
2. retest
3. record result
4. choose next issue

Add a small note:
"Retesting tells you what worked."

Use a classroom-friendly flat style with large readable labels.

Avoid shame/failure imagery, red alarm visuals, or dense code.
```

## W06B Slide 7 - Console Logs As Evidence

```text
Create a clean instructional PowerPoint visual showing console.log as evidence checkpoints.

Use a white or very light background. Show a simple code path with three checkpoint markers:

- function started
- input value read
- condition branch chosen

Beside it, show a simplified console output panel with matching messages.

Add a small note:
"Use logs to test a question."

Use large readable labels and a modern flat classroom-friendly style.

Avoid dark terminal imagery, dense code, stack traces, or advanced debugging tools.
```

## W06B Slide 8 - Demo Multi-Issue Debugging

```text
Create a clean instructional PowerPoint visual for a recorded demo named "Multi-Issue Debugging."

Use a white or very light background. Show a simple task input page with three issue callouts:

- selector mismatch
- condition error
- CSS mismatch

Show a calm ordered path:
1. fix selector
2. retest
3. fix condition
4. retest
5. check styling

Add a small note:
"Order matters."

Use large readable labels and a classroom-friendly flat style.

Avoid red alarm imagery, complex DevTools screens, dark terminal visuals, or dense source code.
```

## W06B Slide 9 - Retest After Each Fix

```text
Create a clean instructional PowerPoint visual showing retesting after each fix.

Use a white or very light background. Show three repeating cards:

Fix 1 -> retest -> evidence
Fix 2 -> retest -> evidence
Fix 3 -> retest -> evidence

Add a small note:
"Retesting turns edits into evidence."

Use a modern flat classroom-friendly style with large readable labels.

Avoid testing-framework dashboards, dense code, or success/failure alarm imagery.
```

## W06B Slide 10 - Good AI Debugging Prompt

```text
Create a clean instructional PowerPoint visual showing the shape of a good AI debugging prompt.

Use a white or very light background. Show a prompt card with five labeled fields:

- observed symptom
- exact console error
- relevant code only
- checks already tried
- ask for explanation

Beside the prompt card, show a small output card labeled "possible causes to test."

Add a small note:
"Ask for explanation, not a replacement project."

Use large readable labels and a calm classroom-friendly flat style with restrained navy, teal, warm gold, white, and soft gray.

Avoid robot characters, chatbot screenshots, pasted full-project code, magic-wand imagery, dark cyber visuals, or anything that implies copying the answer.
```

## W06B Slide 11 - Debugging Report Pattern

```text
Create a clean instructional PowerPoint visual showing a four-part debugging report template.

Use a white or very light background. Show four labeled sections:

- Issue: what was wrong?
- Evidence: how did you identify it?
- Fix: what did you change?
- Verification: how do you know it works?

Add a small note:
"Fixed code alone is not the whole assignment."

Use large readable labels and a classroom-friendly flat style.

Avoid legal/report bureaucracy imagery, dense text, or complex documentation templates.
```

## W06B Slide 15 - Cleaner Code Bridge

```text
Create a clean instructional PowerPoint visual showing the transition from debugging to cleaner structured behavior.

Use a white or very light background. Show a simple progression:

1. bug found
2. cause understood
3. fix verified
4. code made clearer

Add a small note:
"Working code becomes cleaner code next."

Use modern flat classroom-friendly styling with restrained navy, teal, warm gold, white, and soft gray.

Avoid dense refactoring diagrams, advanced architecture, dark terminal imagery, or framework visuals.
```

---

# Suggested Filename Map

Use these filenames when saving generated images:

| Deck | Slide | Suggested filename |
|---|---:|---|
| W06A | 1 | `w06_img_01_debugging_information.png` |
| W06A | 2 | `w06_img_02_week5_success_path.png` |
| W06A | 3 | `w06_img_03_broken_connection.png` |
| W06A | 5 | `w06_img_04_debugging_toolbox.png` |
| W06A | 6 | `w06_img_05_parked_for_later_debugging.png` |
| W06A | 7 | `w06_img_06_debugging_loop.png` |
| W06A | 8 | `w06_img_07_symptom_vs_cause.png` |
| W06A | 9 | `w06_img_08_console_clue.png` |
| W06A | 10 | `w06_img_09_ai_debugging_explainer.png` |
| W06A | 11 | `w06_img_10_exact_match_comparison.png` |
| W06A | 12 | `w06_img_11_demo_broken_selector.png` |
| W06A | 13 | `w06_img_12_verify_fix.png` |
| W06B | 1 | `w06_img_13_one_bug_to_issue_list.png` |
| W06B | 2 | `w06_img_14_multiple_issue_stack.png` |
| W06B | 4 | `w06_img_15_priority_ladder.png` |
| W06B | 5 | `w06_img_16_multi_issue_toolbox.png` |
| W06B | 6 | `w06_img_17_one_fix_at_a_time.png` |
| W06B | 7 | `w06_img_18_console_logs_evidence.png` |
| W06B | 8 | `w06_img_19_demo_multi_issue_debugging.png` |
| W06B | 9 | `w06_img_20_retest_after_fix.png` |
| W06B | 10 | `w06_img_21_good_ai_debugging_prompt.png` |
| W06B | 11 | `w06_img_22_debugging_report_pattern.png` |
| W06B | 15 | `w06_img_23_cleaner_code_bridge.png` |

---

# Alt Text Drafts

- `w06_img_01_debugging_information.png`: Calm debugging evidence cards showing observed behavior, console clue, source comparison, focused fix, and retest.
- `w06_img_02_week5_success_path.png`: Successful DOM interaction path from input and click to JavaScript function and visible feedback.
- `w06_img_03_broken_connection.png`: DOM interaction chain with one broken link highlighted.
- `w06_img_04_debugging_toolbox.png`: Beginner debugging toolbox with reproduce, observe, console, error message, selector, focused change, and retest.
- `w06_img_05_parked_for_later_debugging.png`: Shelf of advanced debugging topics reserved for later.
- `w06_img_06_debugging_loop.png`: Six-step debugging loop from reproduce through explain.
- `w06_img_07_symptom_vs_cause.png`: Symptom card branching into possible causes.
- `w06_img_08_console_clue.png`: Simplified console message with file, line, message, and clue labels.
- `w06_img_09_ai_debugging_explainer.png`: Evidence packet sent to AI for explanation, with student still verifying the fix.
- `w06_img_10_exact_match_comparison.png`: HTML id and JavaScript selector compared side by side.
- `w06_img_11_demo_broken_selector.png`: Broken selector demo with mismatch between statusButton and statusBtn.
- `w06_img_12_verify_fix.png`: Before, fix, and after verification sequence for a button interaction.
- `w06_img_13_one_bug_to_issue_list.png`: Single selector issue expanding into an ordered multi-issue list.
- `w06_img_14_multiple_issue_stack.png`: Stack of three issue cards for selector, condition, and CSS mismatch.
- `w06_img_15_priority_ladder.png`: Debugging priority ladder from script link to styling issue.
- `w06_img_16_multi_issue_toolbox.png`: Toolbox for multi-issue debugging with issue list, priority, logs, checks, and verification note.
- `w06_img_17_one_fix_at_a_time.png`: Chaotic multi-edit path contrasted with orderly one-fix-at-a-time process.
- `w06_img_18_console_logs_evidence.png`: Console log checkpoints along a simple code path.
- `w06_img_19_demo_multi_issue_debugging.png`: Task input demo with ordered fixes for selector mismatch, condition error, and CSS mismatch.
- `w06_img_20_retest_after_fix.png`: Repeating fix, retest, evidence cards.
- `w06_img_21_good_ai_debugging_prompt.png`: Prompt card with symptom, console error, relevant code, checks tried, and explanation request.
- `w06_img_22_debugging_report_pattern.png`: Four-section debugging report template with issue, evidence, fix, and verification.
- `w06_img_23_cleaner_code_bridge.png`: Progression from bug found to fix verified to cleaner code next.

---

# Generation Priority

If time is tight, generate these first:

1. `w06_img_01_debugging_information.png`
2. `w06_img_04_debugging_toolbox.png`
3. `w06_img_06_debugging_loop.png`
4. `w06_img_07_symptom_vs_cause.png`
5. `w06_img_09_ai_debugging_explainer.png`
6. `w06_img_10_exact_match_comparison.png`
7. `w06_img_19_demo_multi_issue_debugging.png`
8. `w06_img_21_good_ai_debugging_prompt.png`
9. `w06_img_22_debugging_report_pattern.png`
