# Week 6 Image Generation Prompts

**Course:** 10-152-117 Python Programming  
**Week:** Week 6 - APIs, External Data, and Python App Architecture

---

# Prompt Use Notes

These prompts expand the image prompt notes in the Week 6 v2 deck sources.

Use clean, instructional visuals. The goal is to clarify request/response,
fallback, and architecture recognition without implying that students are
building production systems.

Avoid:

- complex cloud architecture diagrams
- web dashboards
- framework logos as the main visual
- scary network-failure screens
- dense code screenshots

---

# Week 6 Day 1 - Sequential And Asynchronous Thinking In Python

## Slide 1 - Sometimes Programs Have To Wait

Create a simple educational diagram showing a program moving through three
steps:

- "Step 1: ask for data"
- "waiting"
- "Step 2: use response"

Use a small pause icon or hourglass at the waiting point. Keep the tone calm and
beginner-friendly.

Avoid:

- loading spinners as the whole image
- cloud infrastructure
- error screens
- async code

## Slide 3 - Outside Data Adds A Dependency

Create a diagram with a Python program box on the left and an outside data
source on the right.

Labels:

- "Program"
- "Outside data source"
- "request"
- "response"

Show a clear two-way arrow. Add a small note: "depends on response".

Avoid:

- server rack imagery
- complex network maps
- cybersecurity visuals

## Slide 8 - Request / Response Thinking

Create a five-step horizontal flow:

1. Request data
2. Receive response
3. Inspect shape
4. Select values
5. Display result

Use simple icons and large labels. The visual should feel like a process map for
beginners.

Avoid:

- actual API documentation screenshots
- unreadable JSON
- dashboard styling

## Slide 11 - Async Recognition Preview

Create a two-lane comparison visual.

Lane 1 title: "Sequential"

- step 1
- step 2
- step 3

Lane 2 title: "Waiting-aware"

- ask for data
- wait for response
- continue after response

The visual should communicate recognition only, not syntax.

Avoid:

- `async` / `await` code
- performance charts
- complex event loops

## Slide 14 - Live API And Fallback Are Both Legitimate

Create a two-path diagram with both paths leading to the same learning target.

Path 1:

- "Live API"
- "response JSON"

Path 2:

- "Simulated JSON"
- "response JSON"

Shared endpoint:

- "Inspect, select, explain"

Make both paths visually equal.

Avoid:

- making one path look inferior
- warning symbols on the simulated path
- cloud provider imagery

---

# Week 6 Day 2 - Requesting, Inspecting, And Using API-Style Data

## Slide 1 - Python Can Ask For Outside Information

Create a simple diagram showing a Python program asking for structured data from
either an endpoint or a local simulated JSON file.

Labels:

- "Python program"
- "approved API or simulated JSON"
- "structured response"

Use a request arrow and a response arrow.

Avoid:

- browser address bars
- full web page mockups
- complex network architecture

## Slide 8 - Inspect First, Extract Second

Create a two-step visual.

Left side:

- small JSON response with three readable labels
- heading: "Inspect shape"

Right side:

- clean output card with two selected values
- heading: "Extract useful values"

Use arrows from JSON labels to selected output.

Avoid:

- deep nested JSON
- more than three labels
- raw terminal dump style

## Slide 10 - Live API And Simulated JSON

Create a balanced two-column comparison.

Left column:

- "Live API"
- "real response"

Right column:

- "Simulated JSON"
- "stable practice response"

Bottom shared label:

- "Same skill: inspect, select, explain"

Use equal visual weight for both columns.

Avoid:

- ranking icons
- warning colors
- implying simulated data is fake or lesser

## Slide 15 - Evidence For A11

Create a clean checklist titled "A11 Evidence".

Checklist items:

- code file
- data source or simulated path
- selected output
- request/response explanation
- validation note
- AI-use note, if used

Keep it clear and classroom-friendly.

Avoid:

- legal or audit styling
- too many icons
- dense paragraphs

## Slide 16 - AI-Assisted API Code Must Be Verified

Create an instructional comparison visual.

Left:

- "AI suggestion"
- small code card icon

Right:

- "Actual response shape"
- small JSON card icon

Center:

- "human verification"

Bottom caption:

- "Run it, inspect it, explain it."

Avoid:

- robot characters
- scary AI imagery
- implying AI is forbidden

---

# Week 6 Day 3 - Python Beyond Console Scripts

## Slide 1 - Python Can Live Beyond One Script

Create a simple expansion visual.

Left:

- one console script file

Right:

- larger app flow with separated boxes

Labels on right:

- input
- validation
- logic
- display

Show that the right side grows from the left side.

Avoid:

- web dashboard screenshots
- framework logos
- implying console scripts are bad

## Slide 3 - One Script Can Hold Many Responsibilities

Create a single friendly code-file box containing four labeled responsibility
chips:

- input
- validation
- logic
- output

The visual should communicate that small programs may keep these together.

Avoid:

- red warning marks
- messy code imagery
- "bad code" labels

## Slide 9 - MVT As Recognition Vocabulary

Create a three-part MVT recognition diagram.

Boxes:

- Model: data shape and rules
- View: request handling and decisions
- Template: displayed result

Use arrows to show a simple flow among the boxes.

Keep the wording readable and beginner-friendly.

Avoid:

- Django logo as central focus
- full web page UI
- database schema complexity

## Slide 11 - Demo 1: Console-To-MVT Preview

Create a responsibility trace diagram.

Flow:

- user input
- validation
- program logic
- display result

Add small tags showing how these map to larger app thinking:

- form/input
- view/logic
- template/display

Avoid:

- dense source code
- framework setup screens
- complicated branching

## Slide 15 - Evidence For A11 And A12

Create a two-column evidence visual.

Left column title: "A11"

- data path
- selected output
- validation note

Right column title: "A12"

- input location
- logic location
- display location

Bottom:

- "Explain the flow in your own words."

Avoid:

- legal rubric styling
- clutter
- tiny text
