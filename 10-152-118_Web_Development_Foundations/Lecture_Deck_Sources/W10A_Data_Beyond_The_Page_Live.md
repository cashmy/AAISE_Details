# W10A Data Beyond The Page Live

**10-152-118 Web Development Foundations**  
**Week 10 Monday Live Lecture**  
**Topic:** Data Beyond The Page - Reading Structure Before Fetching

---

# Session Purpose

Week 10 connects browser applications to structured data beyond the values
students typed directly into their own scripts.

Monday begins with the Schoology JSON Reading Worksheet quiz, then uses the
results to reinforce object, array, key, value, and access-path thinking. The
live demo deliberately uses a local JavaScript object before adding `fetch()`.
Students should learn to read the shape before timing and networking make the
task more difficult.

The practical target is intentionally focused:

- distinguish objects from arrays
- trace a path to one selected value
- explain the difference between JSON text and a JavaScript value
- display selected fields instead of dumping raw data
- connect a data source to the request, response, select, and display path

---

# IIM Alignment

Week 10 Monday:

- APIs and `fetch()` at an introductory level
- JSON-shaped data
- data from outside the page
- local or simulated data as a stable fallback

Tuesday lab:

- fetch approved public data or provided JSON
- inspect the structure before selecting values
- display meaningful values in the page

AI role:

- AI as Assistant
- students must inspect the data and attempt an access path manually first
- AI may compare the student's proposed path with the visible structure
- AI may not choose the project, build the complete fetch solution, or replace
  the student's testing and explanation

Scope correction:

- Local storage appears in some older planning material for Week 10.
- Current canonical pacing assigns persistence and local storage to Week 11.
- Do not add local storage to this deck.

---

# Reading Alignment

Assigned reading and activity:

- **Review - JS/JQ:** Chap 8 - Ajax & JSON: selected pages on JSON structure:
  pp 376-377, 382-383, 396-397
- **Required - JS/JQ:** Chap 9 - APIs: selected pages on what APIs are:
  pp 409-413
- **Reference - Shared Course Materials:** `../Approved_API_List.md`
- **Reference - Course Materials:**
  `Course_Materials/Week_10_API_Guidance_For_Web_Projects.md`
- **Reference - JS/JQ:** Chap 12 - Filtering, Searching & Sorting: pp 527-566,
  only if the assignment needs it
- **Reference - JS/JQ:** Chap 9 - selected pages on third-party APIs:
  pp 440-448
- **Required - Course Activity:** JSON Reading Worksheet Quiz in Schoology,
  accomplished in class

Reading-to-lab bridge:

- The quiz checks whether students can distinguish objects, arrays, and nested
  values before API implementation begins.
- Monday models selected-value access from a known local structure.
- Tuesday adds retrieval with `fetch()` using approved or simulated data.

What students should not try to master yet:

- large or deeply nested responses
- API keys, authentication, or OAuth
- CORS troubleshooting
- pagination implementation
- filtering and sorting unless their chosen data requires it
- displaying every value returned by an API

---

# Prior Lab Review

Use the Week 9 success solution:

```text
Assignments/Success_Solutions/Week_09_Modular_Thinking/
```

Review rhythm:

1. Run the Study Sprint planner and delayed reminder.
2. Open `script.js`.
3. Identify the responsibility groups: input, validation, planning, display,
   async reminder, and event wiring.
4. Emphasize that the solution stays in one JavaScript file because its
   responsibilities remain easy to locate.
5. Ask where a future data-loading responsibility could fit.

Bridge:

```text
Week 9 gave each job a clear home.
Week 10 sends structured data through those jobs.
```

---

# Course Activity

Use the Schoology quiz configured from:

```text
Course_Materials/Week_10_JSON_Reading_Quiz_Setup.md
```

Instructor reference:

```text
Course_Materials/Week_10_JSON_Reading_Quiz_Key_Instructor.md
```

Purpose:

- diagnose object versus array understanding
- reveal indexing and nested-path confusion early
- identify students who need guided support before full API work
- establish that structure comes before syntax

Do not turn the quiz into a punitive gate. Use it to decide where students need
additional modeling during the lecture and Tuesday lab.

---

# Demo Set

Demo folder:

```text
Demos/Week_10_Data_APIs/01_monday_json_shape/
```

Demo role:

- type the `studyResource` object live
- identify property names and value types
- access `name` and `category` with dot notation
- access the first tag with bracket notation
- display only selected fields in the page
- change or mistype one property name to expose `undefined`
- return to the data shape to repair the path

---

# Slide Sequence Overview

1. Data Beyond The Page
2. Previous Lab Review / Success Path
3. Organized Code Gives Data A Path
4. Course Activity: JSON Reading Worksheet Quiz
5. Quiz Debrief: Structure Before Syntax
6. What Counts As Success Today
7. Today's Toolbox
8. Parked For Later
9. Data, JSON, And JavaScript Values
10. Objects Use Named Properties
11. Arrays Use Ordered Positions
12. Arrays Often Contain Objects
13. Access Paths Follow The Shape
14. `undefined` Is A Structural Clue
15. Select Useful Values
16. Demo: Read The Shape First
17. Inspect The Access Path
18. What An API Provides
19. The Week 10 Data Path
20. Approved Sources And Local Fallbacks
21. AI Assistant: Verify A Data Path
22. Useful AI Prompt Pattern
23. Tuesday Lab Bridge
24. Evidence Expectations
25. Closing

---

# Slide-By-Slide Source

### Slide 1 - Data Beyond The Page

Student-visible text:

```text
Until now, most data came from values you created.

This week, your page will work with structured data from another source.

The challenge has three parts:

- understand the shape
- wait for the data
- display useful values

Start with one value you can explain.
```

**Instructor notes:**

- Frame Week 10 as combining prior skills, not starting over.
- Students already know objects, arrays, timing, DOM updates, and functions in
  partial forms.

**Transition cue:**

- "First, let's look at how last week's organization prepares a place for data work."

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Previous lab review:

- functions have clear jobs
- event handlers stay focused
- input, decisions, timing, and display are separated
- the application still works after refactoring

One successful path kept one well-organized JavaScript file.
```

**Instructor notes:**

- Open the Week 9 success solution.
- Frame it as one successful path.
- Identify where data retrieval and data display could become new
  responsibilities.

**Transition cue:**

- "Clear responsibilities give incoming data a route through the program."

### Slide 3 - Organized Code Gives Data A Path

Student-visible text:

```text
New data will move through responsibilities:

1. request or load the data
2. receive and interpret the structure
3. select useful values
4. update the page

Week 9 organization makes this flow easier to trace.
```

**Instructor notes:**

- Keep this as the Week 9 to Week 10 bridge.
- Do not introduce full implementation yet.

**Transition cue:**

- "Before we request anything, the JSON quiz checks whether we can read the structure."

### Slide 4 - Course Activity: JSON Reading Worksheet Quiz

Student-visible text:

```text
JSON Reading Worksheet Quiz

This activity checks whether you can:

- identify an object or array
- recognize keys and values
- follow nested structure
- write a path to one value

Read the data before choosing an answer.
```

**Instructor notes:**

- Direct students to the Schoology quiz.
- Use the configured quiz rather than reproducing all questions in the deck.
- Allow the planned course time for completion.

**Transition cue:**

- "The quiz results tell us which structural ideas need another example before coding."

### Slide 5 - Quiz Debrief: Structure Before Syntax

Student-visible text:

```text
Use the quiz as a diagnostic:

- Curly braces contain an object.
- Square brackets contain an array.
- Array positions begin at index 0.
- Nested values require every level in the path.

If the path is unclear, return to the shape before guessing.
```

**Instructor notes:**

- Use the instructor key to choose the most useful debrief examples.
- Pay special attention to arrays of objects and nested properties.
- Do not publicly label students by performance group.

**Transition cue:**

- "Today's success is careful reading before code."

### Slide 6 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- identify the outer structure
- trace a path to a selected value
- distinguish an object property from an array index
- display useful fields instead of raw data
- explain where `fetch()` will join the data path
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate image for this slide.

**Transition cue:**

- "The working vocabulary is small, but every term has a different job."

### Slide 7 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- data
- JSON
- object
- property
- array
- index
- access path
- selected display
- API
- `fetch()`
```

**Instructor notes:**

- Keep `fetch()` present as the Week 8 connection, though Monday's demo does
  not retrieve data yet.

**Transition cue:**

- "Several nearby API topics remain outside this beginner path."

### Slide 8 - Parked For Later

Student-visible text:

```text
Parked for later:

- API keys and authentication
- CORS troubleshooting
- pagination code
- large nested responses
- advanced filtering and sorting
- displaying every returned field

For now:

Read one structure. Retrieve one source. Display selected values.
```

**Instructor notes:**

- Keep the scope narrow because Week 10 already combines several concepts.
- Pagination returns conceptually in Week 12 performance work.

**Transition cue:**

- "Before reading the shape, we need to separate three terms students often blend together."

### Slide 9 - Data, JSON, And JavaScript Values

Student-visible text:

```text
Data is the information we want to use.

JSON is a text format used to store or send structured data.

After JavaScript parses JSON, the program works with JavaScript values such as:

- objects
- arrays
- strings
- numbers
- booleans

Similar shape does not mean identical form.
```

**Instructor notes:**

- This corrects the common shortcut that every object is JSON.
- Keep parsing conceptual until Wednesday's `response.json()` slide.

**Transition cue:**

- "The first structure stores values under names."

### Slide 10 - Objects Use Named Properties

Student-visible text:

```text
An object groups related values under property names.

Example questions:

- What thing does this object describe?
- Which properties are available?
- What type of value belongs to each property?

Use a property name exactly as the data provides it.
```

**Instructor notes:**

- Connect to the quiz's key/value language.
- Use `name`, `category`, `available`, and `tags` from the Monday demo.

**Transition cue:**

- "The second structure stores items by position."

### Slide 11 - Arrays Use Ordered Positions

Student-visible text:

```text
An array stores an ordered list of items.

Indexes begin at 0:

- first item: `[0]`
- second item: `[1]`
- third item: `[2]`

The index identifies a position, not a property name.
```

**Instructor notes:**

- Keep the example small.
- Link directly to the quiz question about the second skill.

**Transition cue:**

- "API responses often combine these two structures."

### Slide 12 - Arrays Often Contain Objects

Student-visible text:

```text
A common data shape is an array of objects.

Read it in layers:

1. choose an item from the array
2. choose a property from that object

Example path:

`data[0].name`

First item, then its name.
```

**Instructor notes:**

- This is the most important quiz-to-API bridge.
- Have students say the access path in plain language.

**Transition cue:**

- "Every value has an address created by the structure around it."

### Slide 13 - Access Paths Follow The Shape

Student-visible text:

```text
Build an access path one level at a time.

Ask:

- What is the outer structure?
- Which item or property comes next?
- Is the next level an object or array?
- What exact path reaches the value?

Do not skip a level that exists in the data.
```

**Instructor notes:**

- Use a nested example only if quiz results show students are ready.
- Trace visually from outside to inside.

**Transition cue:**

- "When the path and shape disagree, JavaScript often gives us a useful clue."

### Slide 14 - `undefined` Is A Structural Clue

Student-visible text:

```text
`undefined` often means the requested path did not match the data.

Check:

- spelling and capitalization
- object property name
- array index
- missing nested level
- whether the data has arrived yet

Inspect the structure before changing random code.
```

**Instructor notes:**

- Connect structure errors to Week 8 timing errors without blending them.
- `undefined` may have other causes, but these checks fit the beginner task.

**Transition cue:**

- "Finding the value is only half the task. We also decide whether users need to see it."

### Slide 15 - Select Useful Values

Student-visible text:

```text
An API may return more data than the page needs.

Choose fields that support the page's purpose.

Good first step:

- select one or two values
- label them clearly
- display them in the existing UI
- expand only after the path works

Raw JSON is inspection evidence, not the finished interface.
```

**Instructor notes:**

- Connect to the API guidance artifact.
- Avoid rewarding a raw JSON dump as the assignment outcome.

**Transition cue:**

- "The live demo models that small selected-value path."

### Slide 16 - Demo: Read The Shape First

Student-visible text:

```text
Demo: JSON-shaped data before `fetch()`

Watch for:

- identify the object and its properties
- recognize `tags` as an array
- access `name` and `category`
- access the first tag with `[0]`
- display selected values in the page

The data shape determines the code path.
```

**Instructor notes:**

- Use `Demos/Week_10_Data_APIs/01_monday_json_shape/`.
- Type the object and selected accesses live.
- Do not begin by dumping the complete object.
- Ask students to predict each result before clicking the button.

**Transition cue:**

- "Now we test whether the path still works when the shape changes."

### Slide 17 - Inspect The Access Path

Student-visible text:

```text
Inspection questions:

- Which property produces the resource name?
- Why does `tags[0]` produce one tag?
- What happens if `category` becomes `type`?
- Which part of the access path must change?

When the source shape changes, dependent code may need to change.
```

**Instructor notes:**

- Make one controlled property-name mismatch and observe `undefined`.
- Repair the path by returning to the source structure.

**Transition cue:**

- "An API gives the program a source beyond its own file."

### Slide 18 - What An API Provides

Student-visible text:

```text
An API gives one program a defined way to request information or behavior from another system.

For Week 10, focus on:

- a URL or endpoint
- a request from `fetch()`
- a response that arrives later
- structured data in the response

We use public, approved, beginner-friendly sources.
```

**Instructor notes:**

- Keep the definition practical.
- Do not imply all APIs are public or return JSON.
- State that this course selects APIs where JSON is the intended learning path.

**Transition cue:**

- "The complete path connects Week 8 timing, Week 9 organization, and today's data shape."

### Slide 19 - The Week 10 Data Path

Student-visible text:

```text
Week 10 data path:

1. request data with `fetch()`
2. wait for the response
3. parse the JSON text
4. inspect the JavaScript value
5. select useful fields
6. update the page

Each step answers a different question.
```

**Instructor notes:**

- Use this as the week's recurring mental model.
- Wednesday will implement the complete path.

**Transition cue:**

- "Students need a data source that keeps the technical surface manageable."

### Slide 20 - Approved Sources And Local Fallbacks

Student-visible text:

```text
Choose a source from the approved API list.

Recommended default:

- JSONPlaceholder for predictable list data

Other approved choices offer smaller or more specialized responses.

A provided local JSON file is the stable fallback when networking is not the lesson.
```

**Instructor notes:**

- Point students to the shared `Approved_API_List.md` and the Week 10 Web
  guidance.
- Mention JSONPlaceholder, Agify, Advice Slip, REST Countries, and Open-Meteo
  only as choices, not as simultaneous examples.
- Avoid live demonstrations that depend on an unstable API.

**Transition cue:**

- "AI may help verify a student's proposed path after the student has inspected the data manually."

### Slide 21 - AI Assistant: Verify A Data Path

Student-visible text:

```text
AI as Assistant may help after your manual attempt.

You must first provide:

- the small data sample you inspected
- the value you want
- the access path you attempted
- the result or error you observed

Ask AI to compare your path with the structure.
Do not ask it to build the whole feature.
```

**Instructor notes:**

- Keep the Weeks 9-12 manual-first constraint visible.
- Students should paste only the relevant data and code excerpt.

**Transition cue:**

- "A strong prompt shows the reasoning already attempted."

### Slide 22 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I inspected this JSON sample manually.
I want to access [specific value].
I tried [access path], and I observed [result].

Do not write the complete fetch feature.
Compare my path with the data structure and explain the first mismatch.
Ask me one clarifying question before suggesting code."
```

**Instructor notes:**

- Model a path-check request rather than open-ended generation.
- The student still repairs, runs, and explains the code.

**Transition cue:**

- "Tuesday adds retrieval to the structure-reading skill."

Visual notes:

- Use a document-style prompt form with fields for inspected data, target
  value, attempted path, observed result, constraint, and clarifying question.

### Slide 23 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab:

Fetch and display approved or provided data.

First iteration:

- choose one approved source or local JSON file
- inspect the outer structure
- retrieve the data with `fetch()`
- access one meaningful value
- display that value in the page

Build outward only after one path works.
```

**Instructor notes:**

- Connect directly to Assignment 10 Iteration 1.
- A local JSON fallback is acceptable and often preferable for the first path.
- Run local JSON projects through a local server.

**Transition cue:**

- "The evidence must show meaningful use, not merely a successful request."

### Slide 24 - Evidence Expectations

Student-visible text:

```text
Evidence this week:

- data is retrieved successfully
- the structure is interpreted correctly
- selected values appear in the UI
- raw JSON is not the final display
- loading and timing remain understandable
- your reflection describes one challenge and its resolution

Show what the data means in your application.
```

**Instructor notes:**

- Tie evidence to Assignment 10 success criteria.
- Normalize `undefined` and timing problems as debugging evidence.

**Transition cue:**

- "The short version is structure first, one working path, then expansion."

### Slide 25 - Closing

Student-visible text:

```text
Before using external data:

1. inspect the shape
2. identify the value you need
3. trace the access path
4. retrieve the source
5. display the selected result

Understanding the data comes before expanding the feature.
```

**Instructor notes:**

- Close on the same thinking pattern used in the quiz and demo.
- Preview Wednesday's complete data-to-UI flow.

**Transition cue:**

- "Wednesday, we retrieve an array of objects and turn selected fields into visible page content."

---

# AI Use Notes

AI remains an Assistant. Students must inspect the source data, identify a
target value, and attempt an access path before requesting help. AI may compare
the proposed path with the supplied structure. Students still choose the data,
write the feature, test the result, and explain the flow.

---

# Image Prompt Notes

Use the Week 10 prompt packet for the following:

| Slide | Image Concept | Prompt Packet Note |
| --- | --- | --- |
| 1 | data arriving from beyond the page | Include in Week 10 prompt packet |
| 2 | modular responsibilities ready for data | Include in Week 10 prompt packet |
| 3 | organized data path | Include in Week 10 prompt packet |
| 4 | JSON quiz activity | Include in Week 10 prompt packet |
| 5 | structure before syntax | Include in Week 10 prompt packet |
| 7 | today's data toolbox | Include in Week 10 prompt packet |
| 8 | parked advanced API topics | Include in Week 10 prompt packet |
| 9 | data, JSON text, and JavaScript value | Include in Week 10 prompt packet |
| 10 | object properties | Include in Week 10 prompt packet |
| 11 | array indexes | Include in Week 10 prompt packet |
| 12 | array of objects | Include in Week 10 prompt packet |
| 13 | access path through structure | Include in Week 10 prompt packet |
| 14 | undefined as structural clue | Include in Week 10 prompt packet |
| 15 | selected values instead of raw dump | Include in Week 10 prompt packet |
| 16 | JSON shape demo | Include in Week 10 prompt packet |
| 17 | changed property path | Include in Week 10 prompt packet |
| 18 | API endpoint and response | Include in Week 10 prompt packet |
| 19 | complete Week 10 data path | Include in Week 10 prompt packet |
| 20 | approved API and local fallback | Include in Week 10 prompt packet |
| 21 | AI verifies attempted data path | Include in Week 10 prompt packet |
| 22 | useful AI data-path prompt | Include in Week 10 prompt packet |
| 25 | structure-first summary | Include in Week 10 prompt packet |

No separate image prompt is needed for Slide 6 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- prior lab review and Week 9 bridge: 8-10 minutes
- Schoology JSON Reading Worksheet quiz: use planned course activity time
- quiz debrief and JSON structure: 12-18 minutes
- selected-value demo and inspection: 12-18 minutes
- API/data-path framing: 10-12 minutes
- AI Assistant prompt, lab bridge, and evidence: 6-10 minutes

