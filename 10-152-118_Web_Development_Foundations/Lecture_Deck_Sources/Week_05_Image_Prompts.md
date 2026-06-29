# Week 5 Image Generation Prompts

**10-152-118 Web Development Foundations**

---

# Purpose

This companion artifact expands the image notes from the Week 5 deck sources
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
- Reject any image that turns Week 5 into an exhaustive DOM, jQuery, or app
  development lesson. Week 5 is about the first visible connection between
  JavaScript, the page, events, and user feedback.

Source decks:

- `W05A_DOM_Connection_Live.md`
- `W05B_DOM_Input_Feedback_Recorded.md`

Global style guidance:

- clean instructional PowerPoint visual
- white or very light background
- modern, flat, classroom-friendly style
- large readable labels
- minimal decorative detail
- restrained SWTC-friendly colors: navy, teal, warm gold, white, soft gray
- no dense code walls
- no dark hacker/cyber imagery
- no complex DOM tree diagrams
- no polished app dashboard or framework imagery

---

# Week 5 Monday Live Prompts

## W05A Slide 1 - Now It Connects

```text
Create a clean instructional PowerPoint visual showing JavaScript connecting to an HTML page through the DOM.

Use a white or very light background. Show three simple labeled parts:

- HTML page
- DOM bridge
- JavaScript behavior

Show an arrow or bridge from JavaScript to a visible page message changing.

Add a small note:
"Now code reaches the page."

Use large readable labels and a modern flat classroom-friendly style with restrained navy, teal, warm gold, white, and soft gray.

Avoid complex DOM trees, dense code, jQuery, frameworks, dark terminal imagery, or polished app dashboards.
```

## W05A Slide 2 - Week 4 Console Success Path

```text
Create a clean instructional PowerPoint visual showing one successful Week 4 console-only JavaScript path.

Use a white or very light background. Show a simple JavaScript file connected to a console output panel. Include labels:

- variables
- condition
- function
- console output

Add a small note:
"Logic ran first. Page behavior comes next."

The tone should support revision and recovery.

Avoid DOM interaction, buttons, page updates, advanced JavaScript, dark terminal imagery, or dense code.
```

## W05A Slide 3 - From Console Logic To Page Behavior

```text
Create a clean instructional PowerPoint visual showing console output moving toward visible page behavior.

Use a white or very light background. On the left, show a simple console output panel. On the right, show a simple web page with a visible message area. Between them, show three connection steps:

- find element
- wait for event
- update page

Add a small note:
"Find. Wait. Change."

Use large readable labels and a classroom-friendly flat style.

Avoid dense code, full app interfaces, complex DOM diagrams, jQuery, or framework imagery.
```

## W05A Slide 5 - DOM Connection Toolbox

```text
Create a clean instructional PowerPoint visual showing today's beginner DOM connection toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with today's active tools:

- DOM
- element
- id
- querySelector()
- #message
- textContent
- addEventListener()
- click

Make the tools approachable and clearly labeled.

Use restrained SWTC-friendly colors and large readable labels.

Avoid jQuery, many selector patterns, every event type, form validation, localStorage, dark terminal imagery, or a parked-for-later shelf.
```

## W05A Slide 6 - Parked For Later

```text
Create a clean instructional PowerPoint visual showing DOM and event topics parked for later in Week 5.

Use a white or very light background. Show a calm bookshelf or shelf with separate cards labeled:

- many selectors
- every event type
- full validation
- jQuery implementation
- saving data
- complex UI state

Add a small note:
"Not today. First, one click changes one visible result."

The tone should reduce overload.

Avoid clutter, advanced code, professional app dashboards, dark cyber imagery, or mixing these parked topics into the active toolbox.
```

## W05A Slide 7 - DOM Bridge

```text
Create a clean instructional PowerPoint visual explaining the DOM as the browser's page model.

Use a white or very light background. Show a simple HTML document on the left, a browser DOM model in the middle, and JavaScript on the right. Keep the DOM model simple: a few labeled page elements, not a complex tree.

Use labels:

- HTML source
- DOM page model
- JavaScript can work here

Add a small note:
"The DOM is the bridge JavaScript uses."

Use large readable labels and a modern flat classroom-friendly style.

Avoid detailed tree diagrams, dense code, jQuery, framework imagery, or advanced browser internals.
```

## W05A Slide 8 - Select Listen Change Chain

```text
Create a clean instructional PowerPoint visual showing a beginner DOM interaction chain.

Use a white or very light background. Show four connected steps:

1. select element
2. listen for event
3. run function
4. change visible result

Add a small note:
"Read DOM code as a connection chain."

Use a modern flat classroom-friendly style with large readable labels.

Avoid dense code, complex flowcharts, jQuery, or full application screens.
```

## W05A Slide 10 - Click Event Waiting

```text
Create a clean instructional PowerPoint visual showing a click event waiting for user action.

Use a white or very light background. Show a button labeled "Update message." Show a paused/waiting indicator before the click, then an arrow to a message area changing after the click.

Use labels:

- waits for click
- function runs
- message changes

Add a small note:
"The function waits until the event happens."

Use large readable labels and a calm classroom-friendly style.

Avoid animation effects, dense code, complex event diagrams, dark terminal imagery, or app dashboards.
```

## W05A Slide 11 - Demo Button Text Change

```text
Create a clean instructional PowerPoint visual for a live demo named "Button Text Change."

Use a white or very light background. Show a simple page card with:

- message area: "The page is waiting."
- button: "Update message"
- changed message: "The button changed the page."

Show a small JavaScript connection label:
"querySelector + addEventListener + textContent"

Add a small note:
"One click changes one visible result."

Use a classroom-friendly flat style with large readable labels.

Avoid dense code, complex DOM trees, jQuery, frameworks, or professional app UI.
```

## W05A Slide 12 - Trace HTML To JavaScript Connection

```text
Create a clean instructional PowerPoint visual tracing the connection between HTML ids and JavaScript selectors.

Use a white or very light background. Show two side-by-side panels:

Left panel: HTML
- id="message"
- id="updateButton"

Right panel: JavaScript
- querySelector("#message")
- querySelector("#updateButton")

Draw simple matching lines between each HTML id and its JavaScript selector.

Add a small note:
"The selector must match something real."

Use large readable labels and a modern flat classroom-friendly style.

Avoid dense code, complex DOM trees, jQuery, or intimidating error visuals.
```

---

# Week 5 Wednesday Recorded Prompts

## W05B Slide 1 - From Button To Input Feedback

```text
Create a clean instructional PowerPoint visual showing Monday's button interaction becoming Wednesday's input-feedback interaction.

Use a white or very light background. Show a simple sequence:

1. button changes fixed text
2. user types input
3. JavaScript checks value
4. page shows feedback

Add a small note:
"Same connection. More useful feedback."

Use large readable labels and a modern flat classroom-friendly style.

Avoid full form systems, complex validation, app dashboards, jQuery, or dense code.
```

## W05B Slide 2 - Fixed Text Is Limited

```text
Create a clean instructional PowerPoint visual showing why fixed button text is limited.

Use a white or very light background. On the left, show a button producing the same message every time. On the right, show an input field producing a message based on what the user typed.

Use labels:

- same response
- user-specific feedback

Add a small note:
"Feedback should respond to the user."

Use a supportive classroom-friendly style and large readable labels.

Avoid complex forms, validation dashboards, app interfaces, or dense code.
```

## W05B Slide 4 - Input Response Concept

```text
Create a clean instructional PowerPoint visual showing how input lets a page respond to the user.

Use a white or very light background. Show a user typing into a simple input field, JavaScript reading the value, and a message area updating.

Use labels:

- user provides value
- JavaScript reads value
- page updates feedback

Add a small note:
"The page responds with information from the user."

Use restrained SWTC-friendly colors and large readable labels.

Avoid full form workflows, login screens, validation complexity, jQuery, or advanced app UI.
```

## W05B Slide 5 - Input Feedback Toolbox

```text
Create a clean instructional PowerPoint visual showing today's input-feedback toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with today's active tools:

- input
- label
- .value
- .trim()
- empty string
- return
- feedback message
- selector check

Make the tools approachable and clearly labeled.

Use a modern flat classroom-friendly style with restrained navy, teal, warm gold, white, and soft gray.

Avoid full validation, submit events, localStorage, jQuery, saving data, dark terminal imagery, or a parked-for-later shelf.
```

## W05B Slide 6 - Selector Must Match HTML

```text
Create a clean instructional PowerPoint visual showing that a JavaScript selector must match the HTML.

Use a white or very light background. Show an HTML input with:
id="nameInput"

Show a JavaScript selector:
document.querySelector("#nameInput")

Draw a clear matching line between them. Include a small warning-style note, but keep it calm:
"No match can mean null."

Use large readable labels and a classroom-friendly style.

Avoid scary error imagery, dense code, full DOM trees, jQuery, or advanced debugging screens.
```

## W05B Slide 7 - Reading Input Values

```text
Create a clean instructional PowerPoint visual explaining that selecting an input is different from reading its value.

Use a white or very light background. Show two steps:

1. select input element
2. read current text with .value

Show a simple input field containing the word "Alex" and an arrow to:
nameInput.value = "Alex"

Add a small note:
"Select the element first. Read its value next."

Use large readable labels and a modern flat classroom-friendly style.

Avoid dense code, complex form validation, jQuery, or app dashboards.
```

## W05B Slide 8 - Feedback Decision Branch

```text
Create a clean instructional PowerPoint visual showing feedback as a simple decision branch.

Use a white or very light background. Show a decision point:
"Is the input empty?"

Show two paths:

- yes -> "Please enter a name first."
- no -> "Hello, [name]. Welcome to the page."

Add a small note:
"Good feedback often starts with one condition."

Use large readable labels and a classroom-friendly flat style.

Avoid complex validation rules, warning-heavy visuals, dense code, or full form systems.
```

## W05B Slide 9 - Demo Input Feedback

```text
Create a clean instructional PowerPoint visual for a recorded demo named "Input Feedback."

Use a white or very light background. Show a simple page card with:

- label: Name
- input field
- button: Create greeting
- message area

Show two possible message states:

- "Please enter a name first."
- "Hello, Alex. Welcome to the page."

Add a small note:
"Click reads the current input value."

Use a modern classroom-friendly flat style with large readable labels.

Avoid full forms, login screens, complex validation, jQuery, frameworks, or dense code.
```

## W05B Slide 10 - Common DOM Connection Mistakes

```text
Create a clean instructional PowerPoint visual showing common beginner DOM connection mistakes as a friendly checklist.

Use a white or very light background. Show five checklist items:

- selector does not match HTML
- script file is not linked
- function is not connected to an event
- input selected but .value not read
- console error ignored

Add a small note:
"Connection problems leave clues."

Use a supportive classroom-friendly style.

Avoid red error storms, failure imagery, dark terminal screens, dense stack traces, or complex DevTools screenshots.
```

## W05B Slide 14 - Reactive Page To Debugging Bridge

```text
Create a clean instructional PowerPoint visual showing the transition from reactive pages to debugging.

Use a white or very light background. Show a simple progression:

1. page responds
2. behavior breaks
3. browser gives clues
4. debugging process begins

Add a small note:
"When behavior breaks, evidence matters."

Use modern flat classroom-friendly styling with restrained navy, teal, warm gold, white, and soft gray.

Avoid scary error imagery, hacker/cyber visuals, dense stack traces, or advanced DevTools screens.
```

---

# Suggested Filename Map

Use these filenames when saving generated images:

| Deck | Slide | Suggested filename |
|---|---:|---|
| W05A | 1 | `w05_img_01_now_it_connects.png` |
| W05A | 2 | `w05_img_02_week4_console_success.png` |
| W05A | 3 | `w05_img_03_console_to_page_behavior.png` |
| W05A | 5 | `w05_img_04_dom_connection_toolbox.png` |
| W05A | 6 | `w05_img_05_parked_for_later_dom.png` |
| W05A | 7 | `w05_img_06_dom_bridge.png` |
| W05A | 8 | `w05_img_07_select_listen_change.png` |
| W05A | 10 | `w05_img_08_click_event_waiting.png` |
| W05A | 11 | `w05_img_09_demo_button_text_change.png` |
| W05A | 12 | `w05_img_10_trace_html_js_connection.png` |
| W05B | 1 | `w05_img_11_button_to_input_feedback.png` |
| W05B | 2 | `w05_img_12_fixed_text_limited.png` |
| W05B | 4 | `w05_img_13_input_response_concept.png` |
| W05B | 5 | `w05_img_14_input_feedback_toolbox.png` |
| W05B | 6 | `w05_img_15_selector_match_html.png` |
| W05B | 7 | `w05_img_16_reading_input_values.png` |
| W05B | 8 | `w05_img_17_feedback_decision_branch.png` |
| W05B | 9 | `w05_img_18_demo_input_feedback.png` |
| W05B | 10 | `w05_img_19_common_dom_mistakes.png` |
| W05B | 14 | `w05_img_20_reactive_to_debugging.png` |

---

# Alt Text Drafts

- `w05_img_01_now_it_connects.png`: JavaScript connecting to an HTML page through a DOM bridge.
- `w05_img_02_week4_console_success.png`: Console-only JavaScript success path with variables, condition, function, and output.
- `w05_img_03_console_to_page_behavior.png`: Console output moving toward visible page behavior through find, wait, and change steps.
- `w05_img_04_dom_connection_toolbox.png`: Beginner DOM toolbox with querySelector, textContent, addEventListener, and click.
- `w05_img_05_parked_for_later_dom.png`: Shelf of advanced DOM, event, jQuery, saving, and UI state topics reserved for later.
- `w05_img_06_dom_bridge.png`: HTML source connected to a browser DOM model that JavaScript can work with.
- `w05_img_07_select_listen_change.png`: Four-step chain showing select element, listen for event, run function, and change visible result.
- `w05_img_08_click_event_waiting.png`: Button click triggering a function and message change after waiting.
- `w05_img_09_demo_button_text_change.png`: Simple page where a button changes a waiting message.
- `w05_img_10_trace_html_js_connection.png`: HTML ids matched to JavaScript querySelector calls.
- `w05_img_11_button_to_input_feedback.png`: Sequence from fixed button text to user input and feedback.
- `w05_img_12_fixed_text_limited.png`: Comparison between same response and user-specific feedback.
- `w05_img_13_input_response_concept.png`: User input read by JavaScript and used to update page feedback.
- `w05_img_14_input_feedback_toolbox.png`: Toolbox for input, value reading, trimming, return, and feedback messages.
- `w05_img_15_selector_match_html.png`: HTML id matched to JavaScript selector with a null warning.
- `w05_img_16_reading_input_values.png`: Two steps showing input element selection and reading current text with value.
- `w05_img_17_feedback_decision_branch.png`: Empty-input decision branch leading to reminder or greeting message.
- `w05_img_18_demo_input_feedback.png`: Greeting builder page with input, button, and two possible feedback messages.
- `w05_img_19_common_dom_mistakes.png`: Checklist of common beginner DOM connection mistakes.
- `w05_img_20_reactive_to_debugging.png`: Progression from page response to broken behavior to browser clues and debugging.

---

# Generation Priority

If time is tight, generate these first:

1. `w05_img_01_now_it_connects.png`
2. `w05_img_04_dom_connection_toolbox.png`
3. `w05_img_06_dom_bridge.png`
4. `w05_img_07_select_listen_change.png`
5. `w05_img_10_trace_html_js_connection.png`
6. `w05_img_15_selector_match_html.png`
7. `w05_img_20_reactive_to_debugging.png`
