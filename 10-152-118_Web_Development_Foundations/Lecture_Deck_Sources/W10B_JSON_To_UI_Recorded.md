# W10B JSON To UI Recorded

**10-152-118 Web Development Foundations**  
**Week 10 Wednesday Recorded Lecture**  
**Topic:** Data Flow - Request, Parse, Select, Display

---

# Session Purpose

Wednesday deepens Monday's structure-reading work by retrieving a local JSON
file and turning selected fields into visible page content.

The recording keeps the source stable so students can focus on the complete
data path. It reconnects `fetch()` and waiting from Week 8, responsibility
boundaries from Week 9, and object/array access from Monday. Public APIs remain
available for student projects, but the core demo should not depend on network
availability or a changing external response.

The practical target is intentionally controlled:

- trace a request from source to UI
- explain what `response.json()` contributes
- wait for parsed data before using it
- loop through an array of objects
- create readable page content from selected fields
- show loading feedback while the work happens

---

# IIM Alignment

Week 10 Wednesday:

- data flow from request to response to UI
- asynchronous arrival of external or simulated data
- structured data displayed dynamically

Thursday lab:

- improve timing reliability
- improve display clarity
- add one focused selection, formatting, or organization improvement

AI role:

- AI as Assistant
- manually written code and a specific observed problem must come first
- AI may help trace one step of the data path or compare an access path
- AI may not replace the student's complete implementation, testing, or
  reflection

---

# Reading Alignment

Assigned reading and activity:

- **Review - JS/JQ:** Chap 8 - Ajax & JSON: selected JSON pages
- **Required - JS/JQ:** Chap 9 - selected introduction to APIs
- **Reference - Shared Course Materials:** `../Approved_API_List.md`
- **Reference - Course Materials:**
  `Course_Materials/Week_10_API_Guidance_For_Web_Projects.md`
- **Reference - JS/JQ:** filtering, searching, sorting, and third-party API
  selections only when needed
- **Required - Course Activity:** JSON Reading Worksheet Quiz completed in
  class

Reading-to-lab bridge:

- Monday identified objects, arrays, and access paths.
- Wednesday retrieves an array of objects and uses the same path reasoning.
- Thursday improves how the result is selected, formatted, or displayed.

What students should not try to master yet:

- production API clients
- authentication and API keys
- full error-classification systems
- CORS configuration
- pagination implementation
- complex data transformation pipelines

---

# Demo Set

Demo folder:

```text
Demos/Week_10_Data_APIs/02_wednesday_json_to_page/
```

Demo role:

- open `data.json` before opening the JavaScript
- identify the outer array and the properties in each object
- run the page through a local server
- show the immediate loading message
- trace `fetch()`, `await response`, and `await response.json()`
- loop through the parsed array
- create page elements with `textContent`
- append one resource card per object

Important delivery note:

```text
Run this demo through a local server so `fetch("data.json")` works reliably.
```

---

# Slide Sequence Overview

1. Reconnect To Monday
2. The Tuesday Friction Points
3. What Counts As Success Today
4. The Data Path
5. Today's Toolbox
6. Local JSON And Public APIs
7. `fetch()` Starts The Request
8. A Response Is Not Yet The Data
9. `response.json()` Parses The Body
10. Use Data Only After It Arrives
11. Loading, Success, And Failure States
12. Arrays Of Objects Need Repetition
13. Selected Fields Become Page Content
14. `textContent` Keeps The Output Direct
15. Demo: JSON File To Page
16. Trace The Complete Flow
17. Why The Local Server Matters
18. Stable Fallback And Live Extension
19. AI Assistant: Trace One Broken Step
20. Thursday Lab Refinement
21. Evidence And Submission
22. How To Read Next Week's Material
23. Closing

---

# Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday practiced the first half of data work:

- inspect the outer structure
- identify objects and arrays
- trace a path to one value
- display selected fields

Today we add retrieval and timing to the same structure-reading skill.
```

**Instructor notes:**

- Reconnect to the JSON quiz and Monday demo.
- Avoid reteaching every quiz item.

**Transition cue:**

- "Tuesday likely exposed where structure, timing, and display collide."

### Slide 2 - The Tuesday Friction Points

Student-visible text:

```text
Common first-attempt problems:

- the path produces `undefined`
- `fetch()` appears to return the wrong thing
- data is used before it arrives
- raw JSON reaches the page
- the page gives no loading feedback
- local JSON fails when the file is opened directly

Each problem points to a specific step in the flow.
```

**Instructor notes:**

- Normalize these as expected Week 10 friction.
- The recording gives students a diagnostic sequence rather than random fixes.

**Transition cue:**

- "Today's success is locating the step that needs attention."

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- trace request, response, parse, select, and display
- explain why data must be awaited
- loop through an array of objects
- create readable UI from selected properties
- identify which step failed when the page stays empty
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate image for this slide.

**Transition cue:**

- "The same five-step path will organize the whole recording."

### Slide 4 - The Data Path

Student-visible text:

```text
Follow the data through five questions:

1. Request: where did we ask for it?
2. Response: what came back?
3. Parse: how did JSON text become usable values?
4. Select: which properties support the page?
5. Display: where did the UI change?

Debug one step at a time.
```

**Instructor notes:**

- Keep this visible as the diagnostic spine.
- Timing sits between request and usable data.

**Transition cue:**

- "Today's toolbox gives each step a concrete JavaScript form."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- local JSON file
- local server
- `async` / `await`
- `fetch()`
- response
- `response.json()`
- array loop
- `createElement()`
- `textContent`
- loading feedback
```

**Instructor notes:**

- Most items are familiar from Weeks 5, 8, and 10 Monday.
- The novelty lies in connecting them.

**Transition cue:**

- "The source can be local or public while the data path stays similar."

### Slide 6 - Local JSON And Public APIs

Student-visible text:

```text
Local JSON file:

- stable classroom source
- known structure
- no external network dependency

Public API:

- data comes from another service
- structure may be larger or change
- network and service availability matter

Both let us practice request, parse, select, and display.
```

**Instructor notes:**

- Present local JSON as a legitimate simulated external source.
- Do not imply it is identical to a remote API in every technical detail.

**Transition cue:**

- "In either case, `fetch()` begins the request."

### Slide 7 - `fetch()` Starts The Request

Student-visible text:

```text
`fetch(source)` starts a request.

It does not immediately produce the final data.

The browser must:

- contact or locate the source
- wait for a response
- make the response available to the program

This is the Week 8 timing model in real use.
```

**Instructor notes:**

- Reuse the exact Week 8 mental model.
- Avoid Promise chaining; the demo uses `async` / `await`.

**Transition cue:**

- "The response represents what came back, but one more step remains."

### Slide 8 - A Response Is Not Yet The Data

Student-visible text:

```text
The `Response` object describes the result of the request.

It can tell the program about:

- the returned body
- status information
- headers and other response details

The JSON body still needs to be read and parsed.
```

**Instructor notes:**

- Keep headers and status at recognition level.
- The main correction is that `fetch()` does not directly return the array of
  resources.

**Transition cue:**

- "`response.json()` performs the parsing step for this JSON response."

### Slide 9 - `response.json()` Parses The Body

Student-visible text:

```text
`response.json()` reads the response body and parses JSON.

After awaiting it, JavaScript can work with:

- an object
- an array
- values nested inside them

The parsed value must still be inspected before properties are selected.
```

**Instructor notes:**

- Connect back to Monday's JSON versus JavaScript-value distinction.
- Avoid describing parsing as validation or automatic correctness.

**Transition cue:**

- "Because parsing also takes time, the code waits before using the result."

### Slide 10 - Use Data Only After It Arrives

Student-visible text:

```text
Inside the async function:

1. await the response
2. await the parsed JSON value
3. use the data

Code that needs the data belongs after the awaited result.

Moving display code too early creates timing problems.
```

**Instructor notes:**

- Keep the sequence concrete.
- Relate this to Week 8's now-versus-later timeline.

**Transition cue:**

- "While that work happens, the page should tell the user what state it is in."

### Slide 11 - Loading, Success, And Failure States

Student-visible text:

```text
Data work creates visible states:

Loading:
- the request has started

Success:
- selected data appears

Failure:
- the page explains that the data could not be loaded

An empty page does not explain any state.
```

**Instructor notes:**

- The demo visibly implements loading and success.
- Use failure as a required mental model and refinement target, without turning
  this into a full error-handling lecture.

**Transition cue:**

- "When the parsed value is an array, the page usually repeats a display pattern."

### Slide 12 - Arrays Of Objects Need Repetition

Student-visible text:

```text
The demo data is an array of resource objects.

For each resource:

- select the current object
- read its `name`, `category`, and `use`
- create one visible resource card
- append that card to the page

One data item produces one repeated UI item.
```

**Instructor notes:**

- Use the `for...of` loop from the demo.
- Keep repetition tied to the data shape.

**Transition cue:**

- "Each card uses selected properties rather than displaying the complete object."

### Slide 13 - Selected Fields Become Page Content

Student-visible text:

```text
For each object, the page chooses fields with a purpose:

- `name` becomes the heading
- `category` becomes a labeled detail
- `use` becomes a short explanation

The UI translates data structure into information a user can read.
```

**Instructor notes:**

- Connect technical selection to the page's purpose.
- This is the Assignment 10 standard beyond raw JSON dumping.

**Transition cue:**

- "The demo uses DOM methods that keep text output direct and visible."

### Slide 14 - `textContent` Keeps The Output Direct

Student-visible text:

```text
The demo creates elements and assigns text with `textContent`.

This approach:

- makes each field's destination visible
- avoids building one large HTML string
- keeps data selection easy to inspect
- prepares for later security discussion

Use the clearest method you can explain.
```

**Instructor notes:**

- Mention the Week 13 safety connection briefly.
- Do not turn this into the security lecture yet.

**Transition cue:**

- "Now we connect every step in one working example."

### Slide 15 - Demo: JSON File To Page

Student-visible text:

```text
Demo: local JSON file to visible resource cards

Watch for:

- inspect `data.json` first
- start the request with `fetch()`
- await the response and parsed value
- loop through the array
- create elements from selected properties
- replace the loading message with results

Run the project through a local server.
```

**Instructor notes:**

- Use `Demos/Week_10_Data_APIs/02_wednesday_json_to_page/`.
- Open `data.json` before writing JavaScript.
- Type the fetch, parse, loop, and DOM creation blocks in understandable
  sections.
- Retest after each meaningful block when practical.

**Transition cue:**

- "The finished page is useful only if we can trace how each value arrived."

### Slide 16 - Trace The Complete Flow

Student-visible text:

```text
Trace one resource name:

1. `fetch("data.json")` requests the file
2. the response arrives
3. `response.json()` parses the body
4. the loop selects one resource object
5. `resource.name` selects the value
6. `textContent` places it in the heading

Every visible value has a traceable path.
```

**Instructor notes:**

- Use one value rather than tracing every card property.
- This slide is the conceptual payoff for the demo.

**Transition cue:**

- "One environmental detail can stop the path before the request succeeds."

### Slide 17 - Why The Local Server Matters

Student-visible text:

```text
Opening `index.html` directly uses a `file:` address.

Fetching `data.json` works more reliably through a local web server.

The local server gives the project an `http:` address and serves both files in a browser-friendly context.

If local JSON does not load, check how the page was opened.
```

**Instructor notes:**

- Show the browser address bar if useful.
- Avoid a deep origin-policy or CORS explanation.
- This is an operational check students can perform immediately.

**Transition cue:**

- "Once the stable local path works, a live approved API can become an extension."

### Slide 18 - Stable Fallback And Live Extension

Student-visible text:

```text
Stable first path:

- local JSON file
- known data shape
- repeatable classroom result

Possible extension:

- approved public API
- live response
- selected fields matched to the project purpose

Keep the local version when it protects a working submission.
```

**Instructor notes:**

- Encourage a stable fallback for students choosing a live API.
- Public API use should remain within the approved list or instructor approval.

**Transition cue:**

- "When one step breaks, AI can assist with a focused trace after the student has run and observed the code."

### Slide 19 - AI Assistant: Trace One Broken Step

Student-visible text:

```text
Before asking AI, provide:

- the code you manually wrote
- the small JSON sample
- the step you expected to work
- the actual console or page result
- the test you already performed

Ask for help locating one failed step.
Do not request a complete replacement solution.
```

**Instructor notes:**

- Refer students back to Monday's data-path prompt pattern.
- Useful AI verbs: compare, trace, explain, suggest one test.
- The student must implement and verify the repair.

**Transition cue:**

- "Thursday improves the working path without expanding beyond what students can explain."

### Slide 20 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab:

Improve one working data path.

Choose at least one:

- select or filter specific data
- improve labels or layout
- simplify data-handling functions
- improve loading or failure feedback
- preserve a local JSON fallback

Retest the complete path after the change.
```

**Instructor notes:**

- Connect directly to Assignment 10 Iteration 2.
- Keep filtering modest; Chapter 12 remains reference only.

**Transition cue:**

- "Submission evidence should show that the data is both correct and meaningful."

### Slide 21 - Evidence And Submission

Student-visible text:

```text
Final submission evidence:

- approved or provided data source
- successful retrieval
- correct object and array access
- selected values displayed in the UI
- understandable loading behavior
- no raw JSON as the finished result
- reflection on one challenge and resolution

Explain the path from source to page.
```

**Instructor notes:**

- Align with Assignment 10 final submission and success criteria.
- A stable local JSON solution fully supports the learning target.

**Transition cue:**

- "Next week asks what the application remembers after data or user actions change the interface."

### Slide 22 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required - JS/JQ:
- pp 420-427 on Web Storage, local storage, session storage, and history

Required - Course Materials:
- `Week_11_State_LocalStorage_Example.md`

Reference - JS/JQ:
- selected Chapter 12 data sections only when your project needs them

Notice:
- current value
- update
- state
- persistence
- saved preference

Ask: "What information should the application remember?"
```

**Instructor notes:**

- Preserve the exact Required and Reference distinction from the Week 11
  reading guide.
- Emphasize that state and persistence are related but different.

**Transition cue:**

- "Week 10 brings data into the application. Week 11 examines what the application keeps."

### Slide 23 - Closing

Student-visible text:

```text
Complete Week 10 mental model:

- inspect the source
- request the data
- wait for the response
- parse the JSON
- select meaningful values
- display them clearly
- trace problems to one step

Applications receive and respond to data over time.
```

**Instructor notes:**

- Close by connecting Week 8 timing, Week 9 organization, and Week 10 data.
- Keep the final emphasis on an explainable data path.

**Transition cue:**

- "A working data path gives next week's state a clear source and destination."

---

# AI Use Notes

AI remains an Assistant. Students must provide manually written code, a small
data sample, an expected step, the observed result, and a test already
performed. AI may help trace one failed step. Students still implement, retest,
and explain the repair.

---

# Image Prompt Notes

Use the Week 10 prompt packet for the following:

| Slide | Image Concept | Prompt Packet Note |
| --- | --- | --- |
| 1 | structure reading to retrieval | Include in Week 10 prompt packet |
| 2 | common data-flow friction points | Include in Week 10 prompt packet |
| 4 | five-step data path | Include in Week 10 prompt packet |
| 5 | today's fetch-to-UI toolbox | Include in Week 10 prompt packet |
| 6 | local JSON versus public API | Include in Week 10 prompt packet |
| 7 | fetch starts request | Include in Week 10 prompt packet |
| 8 | response before parsed data | Include in Week 10 prompt packet |
| 9 | response.json parsing | Include in Week 10 prompt packet |
| 10 | await before use | Include in Week 10 prompt packet |
| 11 | loading, success, and failure states | Include in Week 10 prompt packet |
| 12 | array items to repeated UI | Include in Week 10 prompt packet |
| 13 | selected properties to page fields | Include in Week 10 prompt packet |
| 14 | textContent output path | Include in Week 10 prompt packet |
| 15 | JSON file to page demo | Include in Week 10 prompt packet |
| 16 | trace one value end to end | Include in Week 10 prompt packet |
| 17 | file address versus local server | Include in Week 10 prompt packet |
| 18 | stable fallback and live extension | Include in Week 10 prompt packet |
| 19 | AI traces one attempted step | Include in Week 10 prompt packet |
| 23 | complete Week 10 mental model | Include in Week 10 prompt packet |

No separate image prompt is needed for Slide 3 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- Monday and Tuesday reconnect: 5-8 minutes
- data-path and toolbox framing: 8-10 minutes
- fetch, response, parse, and timing: 12-18 minutes
- arrays, selected fields, and DOM output: 10-15 minutes
- demo and full-flow trace: 18-25 minutes
- local-server check, AI boundary, lab refinement, and next reading: 8-12 minutes
