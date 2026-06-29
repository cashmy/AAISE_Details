# W05B DOM Input Feedback Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 5
- Session: Wednesday recorded
- Deck title: DOM Input Feedback: The Page Responds
- Phase: Behavior
- Target duration: 25-35 minutes
- Recording expected: yes

## Session Type

Wednesday recorded lecture.

## Lesson Purpose

Students should see Monday's fixed button interaction grow into an interaction
that reads user input and gives clearer feedback.

The instructional move is:

```text
button changes fixed text -> input provides value -> function checks value -> page gives feedback
```

## IIM Alignment

Week 5 Wednesday:

- Query selectors vs IDs/classes.
- Debugging null errors at a recognition level.
- Prepare Thursday lab: add multiple interactions or improve existing interaction.

## Reading Alignment

Week 5 assigned reading:

- Required - JS/JQ: Duckett Chap 5 - Document Object Model, selected pages on what the DOM is and selecting one element, pp. 183-187, 228-231
- Required - JS/JQ: Duckett Chap 6 - Events, selected pages on basic event-driven thinking and click events, pp. 243-251
- Required - JS/JQ: Duckett Chap 7 - jQuery, selected pages for library recognition, script loading, and safety awareness, pp. 293-304, 358-361
- Skim - JS/JQ: Duckett Chap 5 - Document Object Model, element manipulation, pp. 187-227, 232-242
- Skim - JS/JQ: Duckett Chap 6 - Events, handlers, listeners, and other events, pp. 252-292
- Reference - JS/JQ: Duckett Chap 7 - jQuery, selected pages showing how a helper library shortens common DOM/event tasks, pp. 304-357, 362-366

What this recording reinforces:

- selectors must match existing HTML
- events wait for user action
- input values must be read with `.value`
- visible feedback should help the user
- a console error is a clue, not a dead end

What students should not try to master yet:

- full form validation
- every input event
- jQuery implementation
- saving data
- large UI state
- advanced debugging tools

## Review / Prior Work Bridge

Monday introduced:

```text
select element -> listen for click -> run function -> update text
```

Wednesday grows that into:

```text
select input -> read value -> check condition -> update feedback
```

## What Counts As Success Today

By the end of the recording, students should be able to:

- select an input element
- read an input's `.value`
- use a condition to check empty input
- update a message based on user input
- recognize a selector mismatch as a likely cause of `null`

Success is clearer feedback, not a complete form system.

## Today's Toolbox

Today we will use:

- input element
- label
- `.value`
- `.trim()`
- empty string
- `return`
- feedback message
- selector check

## Parked For Later

Parked for later:

- full validation rules
- submit events
- saving input
- localStorage
- accessibility depth
- complex form workflows

Today: read one input and respond clearly.

## Assignment Supported

Assignment 5 - DOM Interaction & Events

Wednesday supports concept focus and Thursday refinement:

- improve reliability and clarity
- add one additional interaction, or improve one existing interaction
- improve user feedback
- keep JavaScript organized and readable
- remove console errors

## Readiness Target

By the end of the recording, students should be ready to:

- revise their first interaction
- add input-based feedback if appropriate
- test empty and filled input
- explain how the event triggers the function
- use the console as a clue when the connection breaks

## Primary Watch Point

Students may forget that an input's text is not the input element itself.

Reframe:

```text
Select the input element first.
Read its current text with `.value`.
```

## Demo Set

Demo folder:

```text
Demos/Week_05_DOM_Interaction/02_wednesday_input_feedback/
```

Demo files:

- `index.html`
- `styles.css`
- `script.js`
- `demo_notes.md`

Delivery:

- Start from Monday's button idea.
- Type selectors for input, button, and message.
- Read `.value`, trim it, and check for empty input.
- Click with empty input and then with a name.
- Emphasize that the event waits until the click.

## Slide Sequence Overview

1. Reconnect To Monday
2. The Working Problem: Fixed Text Is Limited
3. What Counts As Success Today
4. Inputs Make The Page Respond To The User
5. Today's Toolbox
6. Selectors Must Match The HTML
7. Reading Input Values
8. Feedback Needs A Decision
9. Demo: Input Feedback
10. Common DOM Connection Mistakes
11. Thursday Lab Refinement
12. Evidence And Reflection
13. How To Read Next Week's Material
14. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- selected page elements
- waited for a click
- ran a function
- changed visible text

Today:
- read user input
- check the value
- give clearer feedback
```

**Instructor notes:**

- Keep the recording tied to Monday.
- This is a deeper version of the same connection pattern.

**Transition cue:**

- "A button changing fixed text is useful, but user input makes the page feel more alive."

Visual notes:

- Monday button interaction expanding into input feedback.

### Slide 2 - The Working Problem: Fixed Text Is Limited

Student-visible text:

```text
A fixed message proves the connection works.

But users often need feedback based on what they do.

Examples:
- empty input needs a reminder
- typed input can personalize a message
- unclear feedback leaves users guessing
```

**Instructor notes:**

- This motivates input without jumping to full forms.
- Keep "feedback" as the user-facing goal.

**Transition cue:**

- "So today's success is reading one input and responding clearly."

Visual notes:

- Static message changing into user-specific feedback.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- an input is selected
- the current `.value` is read
- empty input is handled
- feedback appears on the page
- selector mistakes are easier to spot
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Keep the scope smaller than full form validation.

**Transition cue:**

- "The key shift is that the page uses what the user typed."

### Slide 4 - Inputs Make The Page Respond To The User

Student-visible text:

```text
Input changes the interaction.

Without input:
- the page gives the same response every time

With input:
- the user provides a value
- JavaScript reads that value
- the page responds with feedback
```

**Instructor notes:**

- Keep this conceptual before syntax.
- This is still DOM interaction, not forms week.

**Transition cue:**

- "Here are the tools we need for that one input path."

Visual notes:

- User typing input, JavaScript reading it, message updating.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- input element
- label
- `.value`
- `.trim()`
- empty string
- `return`
- feedback message
- selector check
```

**Instructor notes:**

- Explain `.trim()` as removing extra spaces, not a deep string-method lesson.
- Explain `return` as stopping the function after the reminder.

**Transition cue:**

- "Before we read a value, the selector has to find the right element."

Visual notes:

- Input-feedback toolbox.

### Slide 6 - Selectors Must Match The HTML

Student-visible text:

```text
The selector must match the page.

HTML:
`<input id="nameInput">`

JavaScript:
`document.querySelector("#nameInput")`

If the selector does not match,
JavaScript may find `null`.
```

**Instructor notes:**

- This introduces null as a likely mismatch without making Week 5 a debugging lecture.
- Point out `#` for id.

**Transition cue:**

- "Once we have the input element, we still need the text inside it."

Visual notes:

- Matching HTML id and JavaScript selector.

### Slide 7 - Reading Input Values

Student-visible text:

```text
Selecting the input finds the element.

`.value` reads what the user typed.

Example:

`const name = nameInput.value.trim();`

Read it as:
"Get the current input text and remove extra spaces."
```

**Instructor notes:**

- This is the central new syntax for Wednesday.
- Show empty input first, then typed input.

**Transition cue:**

- "Once the program has the value, it can make a decision."

### Slide 8 - Feedback Needs A Decision

Student-visible text:

```text
Good feedback often needs a condition.

If the input is empty:
- ask the user to enter something
- stop the function

Otherwise:
- use the input
- update the message
```

**Instructor notes:**

- Connect back to Week 4 conditions.
- This is a nice moment to show prior logic now helping the page.

**Transition cue:**

- "Let's build the smallest version of that feedback path."

Visual notes:

- Empty input branch and filled input branch.

### Slide 9 - Demo: Input Feedback

Student-visible text:

```text
Demo: Input Feedback

Watch for:
- input, button, and message selected
- `.value` read after the click
- empty input checked
- feedback message updated
- click event still controls timing
```

**Instructor notes:**

- Type selectors and function live.
- Test empty input first.
- Then type a name and test again.

**Transition cue:**

- "The event still waits. The difference is that the function reads the current input."

Demo connection:

- `Demos/Week_05_DOM_Interaction/02_wednesday_input_feedback/`

### Slide 10 - Common DOM Connection Mistakes

Student-visible text:

```text
Common connection mistakes:

- selector does not match the HTML
- script file is not linked
- function is defined but not connected to an event
- input element is selected but `.value` is not read
- console error is ignored
```

**Instructor notes:**

- Keep this as recognition and preparation for Week 6.
- Mention that errors are clues.

**Transition cue:**

- "Thursday's lab is about making the interaction clearer and more reliable."

Visual notes:

- Friendly checklist of DOM connection mistakes.

### Slide 11 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab: refine interaction

Your goal:
- keep the JavaScript in a separate file
- make one interaction reliable
- add a second interaction or improve the first
- improve user feedback
- remove console errors
```

**Instructor notes:**

- Now it is safe to name the full weekly endpoint.
- Emphasize reliability over adding features.

**Transition cue:**

- "The final evidence should show that the page responds on purpose."

Lab connection:

- Assignment 5 - Iteration 2

### Slide 12 - Evidence And Reflection

Student-visible text:

```text
Final Assignment 5 evidence:

- updated HTML files
- CSS file
- separate JavaScript file
- at least one visible interaction
- no console errors
- short reflection on how page behavior changed your understanding
```

**Instructor notes:**

- Encourage students to test from a fresh refresh.
- The reflection should name the connection between layers.

**Transition cue:**

- "Next week focuses on what happens when these connections break."

### Slide 13 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- read for debugging as a process
- notice console messages and common errors
- look for cause versus symptom

Reference:
- browser-specific tools are there when you need them
- do not memorize every DevTools feature

Before next time:
bring one broken or confusing behavior you would like to understand.
```

**Instructor notes:**

- Week 6 is debugging and problem solving.
- Use this to normalize errors before students arrive frustrated.

**Transition cue:**

- "A page that reacts can also break. Next week, that becomes the lesson."

### Slide 14 - Closing

Student-visible text:

```text
This week:

- JavaScript connected to HTML
- events triggered functions
- input values affected output
- the page responded to the user

Next:
debugging turns broken behavior into evidence.
```

**Instructor notes:**

- End by reinforcing the "web page as reactive system" idea.
- Keep the bridge to Week 6 practical.

**Transition cue:**

- "When something does not work, the browser usually leaves clues."

## Demo Execution Notes

- Use `Demos/Week_05_DOM_Interaction/02_wednesday_input_feedback/`.
- Type selectors for `#nameInput`, `#greetButton`, and `#message`.
- Type `const name = nameInput.value.trim();` live.
- Test empty input before filled input.
- Emphasize that the click event controls when the function reads the current value.

## Lab / Assignment Bridge

Students should use Thursday to finish Assignment 5:

- reliable event-driven interaction
- visible feedback
- separate JavaScript file
- no console errors
- reflection on how JavaScript changed the page

## Evidence / Submission Expectations

Assignment 5 final evidence should show:

- HTML, CSS, and JS files
- one or more working interactions
- visible page update or visible element change
- readable JavaScript
- no console errors
- short reflection

## AI-Use Boundary

AI can help compare selector syntax or explain an error message. Students must
still be able to identify:

- which element is selected
- which event triggers the function
- where `.value` is read
- what feedback is shown

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | Monday connection to input feedback | Include in Week 5 prompt packet |
| 2 | fixed text limitation | Include in Week 5 prompt packet |
| 3 | success today | Use SmartArt; no image prompt by default |
| 4 | input response concept | Include in Week 5 prompt packet |
| 5 | toolbox | Include in Week 5 prompt packet |
| 6 | selector must match HTML | Include in Week 5 prompt packet |
| 7 | reading input values | Include in Week 5 prompt packet |
| 8 | feedback decision branch | Include in Week 5 prompt packet |
| 9 | demo input feedback | Include in Week 5 prompt packet |
| 10 | common DOM mistakes | Include in Week 5 prompt packet |
| 14 | reactive page to debugging bridge | Include in Week 5 prompt packet |

## Instructor Timing Notes

- Reconnect and problem framing: 5-7 minutes
- Input value and feedback concepts: 8-10 minutes
- Demo: 12-18 minutes
- Mistakes and lab bridge: 7-10 minutes
- Next-reading guidance and close: 3-5 minutes

Compress by shortening common mistakes, not by skipping empty-input testing.

## Post-Lecture Notes

- Note whether students confuse the input element with its `.value`.
- Note whether students understand that event timing controls when the value is read.
- Use Week 6 to revisit any repeated selector or script-linking errors.
