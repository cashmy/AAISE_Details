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

## Slide 2 - Review: Local Data Was Available Immediately

Create a simple review visual titled "Local Data Was In A Known Place".

Show a Python program connected to a local file labeled `data.json`.

Add two small notes:

- "known location"
- "available without asking another system"

Add one small caption:

- "Local files can still fail, but the program knows where to look."

Avoid:

- cloud storage
- server diagrams
- scary file error visuals
- complex folder trees

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for beginner
request/response thinking.

Show a five-step path:

1. "ask for outside data"
2. "notice the waiting point"
3. "inspect the response"
4. "select useful values"
5. "explain the dependency"

Include a small program box, an outside data source, and a calm waiting marker.
Use arrows to show request and response, but keep the success pattern as the
main visual.

Avoid:

- server rack imagery
- complex network maps
- cybersecurity visuals

## Slide 4 - What We Will Use Today

Create a working-set visual titled "Today's External Data Ideas".

Show six simple cards:

- sequential flow
- request
- response
- waiting point
- simulated response
- async recognition

Use a clean classroom style with readable labels.

Avoid:

- dense vocabulary wall
- async code
- cloud architecture

## Slide 5 - What We Will Save For Later

Create a calm "save for later" shelf titled "Later, Not Today's Target".

Place these items on the shelf:

- `async` / `await`
- concurrency
- authentication
- deployment
- full API implementation

Add caption:

- "Useful later, not required today."

Avoid:

- warning symbols
- red X marks
- making advanced topics look scary

## Slide 6 - Sequential Flow Happens In Order

Create a minimal process diagram titled "Sequential Flow".

Show three numbered steps in a straight line:

1. "Run step 1"
2. "Run step 2"
3. "Run step 3"

Add caption:

- "Python usually completes one instruction, then moves to the next."

Avoid:

- async terminology
- branching flowcharts
- complex code blocks

## Slide 7 - Requests Interrupt The Simple Story

Create a simple diagram titled "A Request Creates a Wait Point".

Show:

- program step: "ask for data"
- pause marker labeled "wait"
- response card labeled "data returns"
- final step: "use response"

Use one clear arrow path.

Avoid:

- complex network engineering
- server racks
- loading spinner as the entire image
- error screens

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

## Slide 9 - Waiting Does Not Always Mean Broken

Create a calm educational visual titled "Waiting Is Sometimes Normal".

Show a program waiting for an outside response.

Include two question cards:

- "What is the program waiting for?"
- "What should happen if no response arrives?"

Use calm colors and a neutral tone.

Avoid:

- red alerts
- broken computer imagery
- panic visuals
- cybersecurity imagery

## Slide 10 - Demo 1: Request / Response Flow

Create a demo support visual titled "Request / Response Demo".

Show four simple steps:

1. "request happens"
2. "response returns"
3. "values are selected"
4. "output proves the flow"

Use small cards and arrows.

Avoid:

- API documentation screenshots
- browser UI
- dense code
- complex JSON

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

## Slide 12 - Common Failure: Vocabulary Before Meaning

Create a de-escalation visual titled "Meaning Before Vocabulary".

Left side:

- a small cluster of terms: "sync", "async", "endpoint", "response"

Right side:

- one clear question card: "What is the program waiting for?"

Show the terms simplifying into the question.

Avoid:

- overwhelming word cloud
- academic theory diagram
- code-heavy layout

## Slide 13 - Assignment 11 Preview

Create a simple assignment preview visual titled "A11 First Job".

Show three steps:

1. "inspect response"
2. "choose useful values"
3. "explain the data path"

Add caption:

- "Do not just dump raw JSON."

Avoid:

- internet-globe imagery
- impressive but vague API visuals
- dashboard styling

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

## Slide 2 - Review: Request, Response, Inspect, Use

Create a five-step review flow titled "API-Style Pattern".

Steps:

1. request or load data
2. receive response
3. inspect shape
4. select values
5. display result

Keep all labels large and readable.

Avoid:

- web browser UI
- dense code
- cloud architecture

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for API-style JSON work.

Show a six-step path:

1. "identify data source"
2. "retrieve or load response"
3. "inspect JSON shape"
4. "select useful values"
5. "display readable output"
6. "explain the path used"

Include two small source cards that feed into the same path:

- "approved live API"
- "simulated JSON file"

Add a small note:

- "Week 5 JSON skills still apply."

Avoid:

- implying APIs are a total restart
- deeply nested JSON
- server diagrams

## Slide 4 - What We Will Use Today

Create a working-set visual titled "Today's API Data Tools".

Show six cards:

- endpoint
- response
- status cue
- JSON shape
- selected fields
- fallback data

Avoid:

- vocabulary overload
- raw documentation screenshots
- network infrastructure

## Slide 5 - What We Will Save For Later

Create a calm "save for later" visual titled "Not Today's Build Target".

Put these on a shelf:

- authentication
- creating endpoints
- deployment
- rate limits
- full web-framework setup

Add caption:

- "Today we consume or inspect data. We do not build the API."

Avoid:

- warning tone
- red X marks
- production monitoring dashboards

## Slide 6 - An Endpoint Is A Place To Ask

Create a simple diagram titled "Endpoint: A Defined Place To Ask".

Show a Python program sending a request to one labeled endpoint box:

- `/weather`

Show a response arrow coming back.

Add caption:

- "Ask this place for this kind of response."

Avoid:

- browser address bar
- full website mockup
- server rack imagery

## Slide 7 - Status Helps Explain What Happened

Create a simple status-cue visual titled "Status Helps Explain The Response".

Show three response cards:

- "Success"
- "Not found"
- "Needs checking"

Keep it recognition-level and beginner-friendly.

Avoid:

- long status-code table
- scary error screens
- cybersecurity styling

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

## Slide 9 - Raw JSON Is Not The Finished Result

Create a before/after comparison titled "Raw JSON vs Useful Output".

Left side:

- small raw JSON card labeled "raw response"

Right side:

- clean output card labeled "selected result"
- show two lines:
  - "City: Madison"
  - "Temp: 72"

Add caption:

- "Useful output shows that the program understood the response."

Avoid:

- huge JSON blocks
- terminal dump dominance
- dashboard styling

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

## Slide 11 - Demo 1: Parse A Simulated Response

Create a simple demo visual titled "Parse A Simulated Response".

Show a stable JSON file on the left labeled `simulated_weather_response.json`.

Show an arrow labeled "inspect structure".

On the right, show a small card:

- "labels found"
- "values ready to select"

Avoid:

- fake/lesser framing
- deep nesting
- full code block

## Slide 12 - Demo 2: Select Values From API Data

Create a transformation visual titled "Select Values From API Data".

Left:

- response data card with labels: city, temperature, condition

Right:

- readable output card:
  - "Madison"
  - "72"
  - "Clear"

Use arrows from labels to output.

Avoid:

- dashboard charts
- huge JSON
- raw terminal screenshots

## Slide 13 - Demo 3: Error And Fallback Path

Create a two-path visual titled "Error And Fallback Path".

Top path:

- "live path unavailable"
- "use fallback JSON"

Bottom shared result:

- "inspect, select, explain"

Make the fallback look intentional and valid.

Avoid:

- red alert screens
- making fallback look inferior
- broken internet imagery

## Slide 14 - Assignment 11 Bridge

Create a simple assignment flow titled "A11 API Data Fetcher".

Show four steps:

1. choose data source
2. inspect response
3. select useful values
4. explain data path

Avoid:

- complex API platform UI
- full app mockup
- large data pipeline

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

## Slide 2 - Review: API Output Still Needs Explanation

Create a compact review visual titled "A11 Closeout".

Show three evidence cards:

- data source
- selected values
- explanation

Add caption:

- "Retrieving data is not enough; explain the path."

Avoid:

- raw JSON dump
- dashboard styling
- legal checklist look

## Slide 3 - Today's Success Pattern

Create a clean instructional success-pattern visual for recognizing larger app
architecture.

Show a five-step recognition path:

- input
- validation
- logic
- output/display
- separated responsibilities

Include a small caption:

- "Recognition first. No Django build today."

Show a simple console script on one side and a larger-app flow on the other, but
keep the focus on naming where responsibilities live.

Avoid:

- red warning marks
- messy code imagery
- "bad code" labels

## Slide 4 - What We Will Use Today

Create a working-set visual titled "Today's Architecture Vocabulary".

Show seven cards:

- input
- validation
- logic
- display
- template
- view
- model

Keep the visual calm and recognition-level.

Avoid:

- framework diagrams
- dense architecture maps
- Django logo focus

## Slide 5 - What We Will Save For Later

Create a "save for later" visual titled "Not Today's Build".

Put these items on a shelf:

- installing Django
- full web app
- databases
- authentication
- deployment

Add caption:

- "Today we inspect the shape of a larger app."

Avoid:

- warning signs
- red X marks
- making frameworks look scary

## Slide 6 - Larger Apps Separate Responsibilities

Create a simple separation visual titled "Larger Apps Separate Responsibilities".

Show four connected boxes:

- input
- validation
- logic
- display

Add caption:

- "Each part has a clearer job."

Avoid:

- complex architecture
- web dashboard mockup
- server/cloud visuals

## Slide 7 - Input Enters Through A Controlled Place

Create a comparison visual titled "Where Input Enters".

Left:

- console script using `input()`

Right:

- larger app using "form or request"

Keep both paths simple and equal.

Avoid:

- detailed UI mockup
- full web form design
- framework setup imagery

## Slide 8 - Validation Protects The Flow

Create a simple flow visual titled "Validation Protects The Flow".

Show:

- input
- validation check
- accepted value
- program logic

Add a small side note:

- "Check before depending on the data."

Avoid:

- security-heavy imagery
- lock icons as main metaphor
- scary warning visuals

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

## Slide 9.5 - Full Stack as A Preview

Revise the full-stack preview visual.

Important correction:
Integration is NOT a fourth layer. Do not show Integration as a separate box or layer under the Data Layer.

Create a clean beginner-friendly educational visual titled "Full Stack As A Preview".

Show three main stacked layers only:

Layer 1:
- Label: "Front End"
- Meaning: "what the user sees"
- Simple icon: screen or page

Layer 2:
- Label: "Back End"
- Meaning: "request handling and logic"
- Simple icon: gear or flow arrows

Layer 3:
- Label: "Data Layer"
- Meaning: "files, databases, or API data"
- Simple icon: file/table/database symbol

Show "Integration" as the arrows between the layers, not as a separate layer.

Add double-headed arrows:
- between Front End and Back End
- between Back End and Data Layer

Label the arrows:
- "Integration: communication between parts"

If needed, place this label beside the arrows or as a small side callout pointing to the arrows.

Add a small side note:
"Recognition preview only: you are not building a full-stack app in this course."

Optional footer:
"Today we focus on understanding the shape, not building the stack."

Style:
- clean classroom slide visual
- light background
- large readable labels
- calm colors
- simple icons
- professional but not corporate

Avoid:
- showing Integration as a fourth layer
- complex cloud architecture
- server rack imagery
- detailed deployment diagrams
- code screenshots
- framework logos
- making it look like a required project
- dense text

## Slide 10 - Console Flow Versus App Flow

Create a two-lane comparison titled "Console Flow vs App Flow".

Lane 1:

- "Console script"
- top-to-bottom steps

Lane 2:

- "Larger app"
- request -> validation -> logic -> display

Keep it recognition-level.

Avoid:

- web dashboard
- full framework diagram
- complex branching

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

## Slide 12 - Demo 2: Django MVT Recognition

Create a recognition visual titled "MVT Recognition Preview".

Show three labeled areas:

- model: data shape
- view: request handling
- template: display

Add caption:

- "Recognize the flow; do not build Django today."

Avoid:

- Django logo as main visual
- installation/setup screens
- full web app UI

## Slide 13 - Common Failure: Preview Becomes Panic

Create a supportive visual titled "Preview Is Not Panic".

Show two cards:

- "Recognition today"
- "Implementation later"

Add caption:

- "Naming the parts is the success target."

Avoid:

- anxiety imagery
- warning symbols
- red X marks

## Slide 14 - Assignment 12 Bridge

Create a simple assignment visual titled "A12 Architecture Preview".

Show four question cards:

- Where does input enter?
- Where does validation happen?
- Where does logic live?
- Where is output displayed?

Avoid:

- complex framework diagrams
- database schema
- full web interface

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
