# W05A DOM Connection Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 5
- Session: Monday live
- Deck title: DOM Connection: Now It Connects
- Phase: Behavior
- Target duration: 55-70 minutes
- Recording expected: no

## Session Type

Monday live lecture.

## Lesson Purpose

Students should leave Monday understanding that the DOM is the bridge between
HTML structure and JavaScript behavior.

The practical target is intentionally small: select one existing page element,
wait for one click, and change visible text on the page.

## IIM Alignment

Week 5 Monday:

- DOM = bridge between HTML and JavaScript.
- Event-driven thinking.
- Add button interaction to an existing page.

## Reading Alignment

Week 5 assigned reading:

- Required - JS/JQ: Duckett Chap 5 - Document Object Model, selected pages on what the DOM is and selecting one element, pp. 183-187, 228-231
- Required - JS/JQ: Duckett Chap 6 - Events, selected pages on basic event-driven thinking and click events, pp. 243-251
- Required - JS/JQ: Duckett Chap 7 - jQuery, selected pages for library recognition, script loading, and safety awareness, pp. 293-304, 358-361
- Skim - JS/JQ: Duckett Chap 5 - Document Object Model, element manipulation, pp. 187-227, 232-242
- Skim - JS/JQ: Duckett Chap 6 - Events, handlers, listeners, and other events, pp. 252-292
- Reference - JS/JQ: Duckett Chap 7 - jQuery, selected pages showing how a helper library shortens common DOM/event tasks, pp. 304-357, 362-366

Reading-to-lab bridge:

- Reading gives vocabulary: DOM, element, selector, query, event, click, input, null.
- Lecture shows the smallest useful DOM connection.
- Tuesday lab adds one visible interaction to an existing HTML/CSS page.

What students should not try to master yet:

- every DOM method
- every event type
- jQuery fluency
- complex validation
- state persistence
- multi-feature app behavior

## Review / Prior Work Bridge

Previous lab:

- Assignment 4 - Introduction to JavaScript

Success solution:

```text
Assignments/Success_Solutions/Week_04_Introduction_to_JavaScript/
```

Review focus:

- show one successful console-only path, not the only correct answer
- identify variables, functions, conditions, and console output
- emphasize that Week 4 proved logic can run
- connect to today's question: how does running logic reach the visible page?

## What Counts As Success Today

By the end of the session, students should be able to:

- link a JavaScript file to a page
- select one existing HTML element
- select one button
- attach one click event listener
- change visible page text after the click

Success is one clear page response, not a full interactive app.

## Today's Toolbox

Today we will use:

- DOM
- element
- `id`
- `document.querySelector()`
- `#message`
- `textContent`
- `addEventListener()`
- click event

## Parked For Later

Parked for later:

- many selectors
- every event type
- form validation depth
- jQuery as implementation model
- saving data
- complex UI state

Today: select one thing, wait for one click, update one visible result.

## Assignment Supported

Assignment 5 - DOM Interaction & Events

Monday supports Iteration 1:

- link a JavaScript file to at least one page
- implement one event-driven interaction
- update content or change a visible element
- keep the behavior small and explainable

## Readiness Target

By the end of the session, students should be ready to:

- choose one page element to update
- create or identify a button
- write one selector for each element
- connect a click to a function
- test whether the page visibly changes

## Primary Watch Point

Students may think selecting an element changes it.

Reframe:

```text
Selecting finds the element.
An event triggers the function.
The function changes the page.
```

## Demo Set

Demo folder:

```text
Demos/Week_05_DOM_Interaction/01_monday_button_text_change/
```

Demo files:

- `index.html`
- `styles.css`
- `script.js`
- `demo_notes.md`

Delivery:

- Show the page before JavaScript changes anything.
- Type selectors first.
- Type the function next.
- Add the event listener last.
- Click the button and inspect the visible change.

## Slide Sequence Overview

1. Now It Connects
2. Previous Lab Review / Success Path
3. From Console Logic To Page Behavior
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. The DOM Is The Bridge
8. Select, Listen, Change
9. Selectors Find Existing Elements
10. Events Wait For User Action
11. Demo: Button Text Change
12. Trace The Connection
13. Tuesday Lab Bridge
14. Evidence Expectations
15. Closing

## Slide-By-Slide Source

### Slide 1 - Now It Connects

Student-visible text:

```text
Last week:
- JavaScript ran in the console
- variables stored values
- functions organized logic

This week:
- JavaScript finds page elements
- user actions trigger code
- the page visibly changes
```

**Instructor notes:**

- Name this as the first full connection between layers.
- Keep excitement balanced with calm scope control.

**Transition cue:**

- "Before we connect code to the page, let's briefly prove the logic layer from last week."

Visual notes:

- JavaScript logic connecting to an HTML page through a bridge.

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Assignment 4 success path:

- variables stored values
- conditions chose paths
- functions organized logic
- console output showed the result
- no page update was required yet

Today the result moves onto the page.
```

**Instructor notes:**

- Open the Week 4 success solution.
- Show variables, function, condition, and console output.
- Emphasize that console-only was intentional.

**Transition cue:**

- "The logic worked. Now we need a bridge from that logic to the HTML."

Demo connection:

- `Assignments/Success_Solutions/Week_04_Introduction_to_JavaScript/`

### Slide 3 - From Console Logic To Page Behavior

Student-visible text:

```text
Console output is useful for learning.

Page behavior is useful for users.

The browser needs three pieces:
- an element to find
- an event to wait for
- code that changes something visible
```

**Instructor notes:**

- This slide gives students the whole Week 5 pattern.
- Keep the phrase "find, wait, change" available for repetition.

**Transition cue:**

- "So today's success target is one visible response."

Visual notes:

- Console output arrow moving toward a visible page message.

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- JavaScript is linked correctly
- one page element is selected
- one click event is connected
- one function runs after the click
- visible page text changes
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Keep the target narrow.

**Transition cue:**

- "Here are the only tools we need in our hands today."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- DOM
- element
- `id`
- `document.querySelector()`
- `#message`
- `textContent`
- `addEventListener()`
- click event
```

**Instructor notes:**

- The toolbox is intentionally small.
- jQuery appears in reading for recognition, not today's implementation.

**Transition cue:**

- "And here is what we are not turning this into yet."

Visual notes:

- DOM connection toolbox.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- many selector patterns
- every event type
- deep form validation
- jQuery as implementation model
- saving data
- complex UI state

Today: find one element, respond to one click.
```

**Instructor notes:**

- This slide guards against Duckett breadth overload.
- Mention jQuery as helper-library recognition, not the core path.

**Transition cue:**

- "The reason this works is that the browser builds a bridge we can use."

Visual notes:

- Shelf of advanced DOM/event topics.

### Slide 7 - The DOM Is The Bridge

Student-visible text:

```text
The DOM is the browser's page model.

It lets JavaScript:
- find HTML elements
- read current page values
- change text or styles
- respond when users act

The HTML is the source.
The DOM is what JavaScript can work with.
```

**Instructor notes:**

- Keep DOM explanation conceptual and visual.
- Do not go into tree traversal depth.

**Transition cue:**

- "For today, we use the smallest possible path through that bridge."

Visual notes:

- HTML document becoming browser DOM model that JavaScript can access.

### Slide 8 - Select, Listen, Change

Student-visible text:

```text
Beginner DOM pattern:

1. select the element
2. listen for an event
3. run a function
4. change something visible

Read DOM code as a connection chain.
```

**Instructor notes:**

- This is the core procedural mental model.
- Repeat it during the demo.

**Transition cue:**

- "The first link in the chain is selecting something that already exists."

Visual notes:

- Four-step DOM connection chain.

### Slide 9 - Selectors Find Existing Elements

Student-visible text:

```text
`querySelector()` finds an element.

Example:

`const message = document.querySelector("#message");`

Read it as:
"Find the element with id message and remember it."

Selecting does not change the page yet.
```

**Instructor notes:**

- Stress the `#` for id selector.
- Point at the matching HTML `id`.
- Name `null` lightly as "nothing found," but do not turn this into debugging week.

**Transition cue:**

- "After we find the button, we can tell JavaScript what action to wait for."

### Slide 10 - Events Wait For User Action

Student-visible text:

```text
An event is something that happens.

For today:
- user clicks the button
- browser notices the click
- JavaScript runs the function
- the function updates the page

The function waits until the event happens.
```

**Instructor notes:**

- Students may expect the function to run immediately.
- Make the waiting behavior explicit.

**Transition cue:**

- "Let's build it in that order: select, function, event."

Visual notes:

- Button click triggering a function and visible message update.

### Slide 11 - Demo: Button Text Change

Student-visible text:

```text
Demo: Button Text Change

Watch for:
- the page before interaction
- `#message` selected
- `#updateButton` selected
- function changes `textContent`
- click event runs the function
```

**Instructor notes:**

- Type the selector, function, and event listener live.
- Show that nothing changes until the click occurs.
- If timing requires, paste the HTML/CSS shell but type `script.js`.

**Transition cue:**

- "The moment to watch is when the listener gets added and the button starts to matter."

Demo connection:

- `Demos/Week_05_DOM_Interaction/01_monday_button_text_change/`

### Slide 12 - Trace The Connection

Student-visible text:

```text
Trace the interaction:

HTML:
- `id="message"`
- `id="updateButton"`

JavaScript:
- select both elements
- define the update function
- listen for a click
- change `textContent`
```

**Instructor notes:**

- Use this after the demo to make the path explicit.
- This supports students who saw the result but did not yet understand the connection.

**Transition cue:**

- "Tuesday's lab asks for this same pattern on your own page."

Visual notes:

- Side-by-side HTML ids and JavaScript selectors.

### Slide 13 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab: one visible interaction

Use your existing site.

Your goal:
- link a separate JavaScript file
- choose one button, link, or input
- update text or change a visible element
- keep the behavior small enough to explain
```

**Instructor notes:**

- Monday supports the first iteration only.
- Do not require multiple interactions yet.

**Transition cue:**

- "The evidence should prove the connection works."

Lab connection:

- Assignment 5 - Iteration 1

### Slide 14 - Evidence Expectations

Student-visible text:

```text
Preserve evidence:

- HTML, CSS, and JS files render together
- JavaScript is in a separate file
- one user action changes the page
- the console has no errors
- you can explain select, event, update
```

**Instructor notes:**

- The console-error point prepares Week 6 without turning this into debugging yet.
- Ask students to save a screenshot if useful.

**Transition cue:**

- "Wednesday adds input and clearer feedback."

### Slide 15 - Closing

Student-visible text:

```text
Today:

- JavaScript found HTML elements
- a click triggered code
- a function changed visible text
- the page became reactive

Next:
the page responds to user-provided input.
```

**Instructor notes:**

- Close with the "page is not static" idea.
- Keep it anchored in the small interaction.

**Transition cue:**

- "One working connection is enough for today. Make it clear before making it bigger."

## Demo Execution Notes

- Use `Demos/Week_05_DOM_Interaction/01_monday_button_text_change/`.
- Type all of `script.js` live.
- Pause after selectors to say nothing has changed yet.
- Pause after the function to say it is defined but not triggered yet.
- Add the event listener last, then click the button.

## Lab / Assignment Bridge

Students should use Tuesday to add one small interaction to their existing site:

- separate JS file
- one selected element
- one event
- one visible update
- no console errors

## Evidence / Submission Expectations

For Tuesday, students should have a first working DOM interaction. The full
Assignment 5 endpoint, including additional interaction or improved logic,
belongs after Wednesday's recorded lesson and Thursday refinement.

## AI-Use Boundary

AI can help explain a selector or event listener, but students must be able to
trace the connection:

- which HTML element is selected
- which event is being listened for
- which function runs
- what visible result changes

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | JS connecting to page | Include in Week 5 prompt packet |
| 2 | Week 4 console success path | Include in Week 5 prompt packet |
| 3 | console to page behavior | Include in Week 5 prompt packet |
| 4 | success today | Use SmartArt; no image prompt by default |
| 5 | toolbox | Include in Week 5 prompt packet |
| 6 | parked for later | Include in Week 5 prompt packet |
| 7 | DOM bridge | Include in Week 5 prompt packet |
| 8 | select-listen-change chain | Include in Week 5 prompt packet |
| 10 | click event waiting | Include in Week 5 prompt packet |
| 11 | demo button text change | Include in Week 5 prompt packet |
| 12 | trace HTML to JS connection | Include in Week 5 prompt packet |

## Instructor Timing Notes

- Previous success review: 7-10 minutes
- DOM bridge and pattern: 12-15 minutes
- Selectors and events: 12-15 minutes
- Demo: 10-15 minutes
- Lab bridge and evidence: 5-8 minutes

Compress by shortening the previous success review, not by rushing the demo
trace.

## Post-Lecture Notes

- Note whether students forget `#` in id selectors.
- Note whether students expect selecting an element to change it.
- Note whether script placement or file linking causes confusion.
