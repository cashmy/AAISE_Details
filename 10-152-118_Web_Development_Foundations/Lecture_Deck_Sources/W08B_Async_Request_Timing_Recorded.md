# W08B Async Request Timing Recorded

**10-152-118 Web Development Foundations**  
**Week 8 Wednesday Recorded Lecture**  
**Topic:** Async Timing - Requests, Promises, And Loading

---

# Session Purpose

Wednesday deepens Monday's delayed-behavior idea by connecting timing to
request-shaped web behavior.

Students should leave the recording understanding that `fetch` starts a
request, a Promise represents a future result, and `async`/`await` makes waiting
code easier to read. This is still concept-first. Week 10 will carry the
heavier data/API implementation work.

The practical target is intentionally small:

- explain "now" versus "later" in a timing example
- recognize that `fetch()` does not instantly give final data
- read JSON as structured data before trying to use it
- improve a timed feature with clearer feedback or sequencing

---

# IIM Alignment

Week 8 Wednesday:

- real-world analogy
- API calls
- loading

Thursday lab:

- add delayed or sequential behavior
- improve clarity of timed behavior

AI role:

- AI as Explainer
- AI may explain output order, request/response vocabulary, or JSON shape
- AI should not replace the student's explanation of their own behavior

---

# Reading Alignment

Assigned reading:

- **Required - Course Materials:** `Course_Materials/Week_08_Async_Time_Matters_Handout.md`
- **Skim - JS/JQ:** Chap 8 - Ajax & JSON: selected pages on requests,
  responses, and JSON: pp 367-383, 396-397
- **Skim - Course Materials:** `Course_Materials/Week_08_How_To_Read_JSON_Student_Guide.md`
- **Reference - Supplemental:** MDN `setTimeout()`, `fetch()`, and `Promise`

Reading-to-lab bridge:

- Monday made delay visible with a timer.
- Wednesday connects timing to request-shaped behavior.
- Thursday asks students to refine or extend timed behavior while keeping
  feedback clear.

What students should not try to master yet:

- production API architecture
- authentication
- CORS debugging
- advanced Promise chains
- loading spinners as a design system
- complex JSON transformations

---

# Demo Set

Demo folder:

```text
Demos/Week_08_Async_Time/02_wednesday_fetch_timing_shape/
```

Demo role:

- run a timing order example
- show `setTimeout()` scheduling later work
- show `fetch()` starting a request for `data.json`
- explain that `await` waits inside the async function
- connect JSON to "read the structure before using the data"

Important delivery note:

```text
Run this demo through a local server so the local JSON request works.
```

---

# Slide Sequence Overview

1. Reconnect To Monday
2. Timing Is A User Experience Issue
3. What Counts As Success Today
4. From Delay To Request
5. Today's Toolbox
6. Request And Response
7. `fetch()` Starts A Request
8. Promise Means Future Result
9. `async` / `await` Makes Waiting Readable
10. JSON Has Shape
11. Demo: Timing Order
12. Demo: Fetch Timing Shape
13. Waiting Still Happens
14. AI Can Explain The Timeline
15. Useful AI Prompt Pattern
16. Thursday Lab Refinement
17. Evidence And Submission
18. How To Read Next Week's Material
19. Closing

---

# Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday's key question:

What happens now?
What happens later?

Today we apply that same question to:

- loading
- requests
- future results
- JSON-shaped data
```

**Instructor notes:**

- Start by recalling the delayed-message demo.
- Avoid presenting Wednesday as a separate topic.
- This is the same timing model with a more realistic reason to wait.

**Transition cue:**

- "When a page waits, the user experiences that wait."

### Slide 2 - Timing Is A User Experience Issue

Student-visible text:

```text
Async is not only a code issue.

It affects the user:

- Did my click work?
- Is something loading?
- Did the result arrive?
- Should I wait or try again?

Good pages explain waiting.
```

**Instructor notes:**

- Connect timing to clarity and trust.
- This is a gentle bridge toward UI/UX without jumping ahead to Week 14.

**Transition cue:**

- "Today's success is recognizing the timeline."

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- trace what runs now and later
- explain why data is not instant
- describe `fetch` as starting a request
- describe a Promise as a future result
- read simple JSON structure before using it
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate image for this slide.

**Transition cue:**

- "The first step is moving from a delay to a request."

### Slide 4 - From Delay To Request

Student-visible text:

```text
A delay waits for time.

A request waits for a response.

Both create the same beginner question:

What can happen now?
What has to wait until later?
```

**Instructor notes:**

- Keep this as an analogy, not a complete technical equivalence.
- Make it clear that requests are useful because they ask for data.

**Transition cue:**

- "We only need a small toolbox to read this shape."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- request
- response
- `fetch()`
- Promise
- `async`
- `await`
- JSON
- loading feedback
```

**Instructor notes:**

- These are recognition terms.
- Warn students that mastery comes from repeated exposure, not one recording.

**Transition cue:**

- "Requests and responses are the web conversation."

### Slide 6 - Request And Response

Student-visible text:

```text
Request:

"Please send me something."

Response:

"Here is what you asked for."

The response may take time.
The page should stay understandable while waiting.
```

**Instructor notes:**

- Use a non-code analogy: asking for a file, menu, or weather data.
- Keep the vocabulary plain.

**Transition cue:**

- "In JavaScript, one common way to start that request is `fetch()`."

### Slide 7 - `fetch()` Starts A Request

Student-visible text:

```text
`fetch()` starts a request.

Important:

`fetch()` is not the final data.

It begins the process of asking for something.
The response arrives later.
```

**Instructor notes:**

- Explicitly state the planned handout language.
- This prevents the common misconception that `fetch()` immediately equals the
  usable data.

**Transition cue:**

- "JavaScript needs a way to represent that future result."

### Slide 8 - Promise Means Future Result

Student-visible text:

```text
A Promise represents a future result.

Read it as:

"Something is happening.
The final result is not ready yet."

A Promise is not the final data.
It points to work that may finish later.
```

**Instructor notes:**

- Keep this conceptual; do not teach full `.then()` chains.
- Use "future result" repeatedly.

**Transition cue:**

- "Then `async` and `await` help us write waiting code more clearly."

### Slide 9 - `async` / `await` Makes Waiting Readable

Student-visible text:

```text
`async` marks a function that can wait.

`await` marks a waiting point.

Cleaner syntax does not remove waiting.

It only helps the code read more clearly.
```

**Instructor notes:**

- Reinforce the handout's wording: waiting still happens.
- Keep this recognition-level.

**Transition cue:**

- "After the response arrives, the data often has JSON shape."

### Slide 10 - JSON Has Shape

Student-visible text:

```text
Before using JSON, read its shape:

- Is the outside an object or array?
- What keys are present?
- Are any values nested?
- What path leads to the value?

Understand the structure before using the data.
```

**Instructor notes:**

- This connects to the Week 8 JSON student guide.
- Do not make this a full Week 10 JSON/API lecture.
- Use JSON as preview and preparation.

**Transition cue:**

- "Now let's watch timing before we fetch anything."

### Slide 11 - Demo: Timing Order

Student-visible text:

```text
Demo:

Run timing example.

Expected idea:

- start now
- schedule later work
- finish current work now
- later work appears after the delay

Typed order and finished order are not always the same.
```

**Instructor notes:**

- Use `Demos/Week_08_Async_Time/02_wednesday_fetch_timing_shape/`.
- Click "Run timing example."
- Read the log in order.

**Transition cue:**

- "The fetch example uses the same timing idea with a request."

### Slide 12 - Demo: Fetch Timing Shape

Student-visible text:

```text
Demo:

Load sample data.

Trace the shape:

1. request starts
2. browser waits for response
3. response becomes JSON
4. page uses the future result

The data arrives later.
```

**Instructor notes:**

- Run through a local server.
- Click "Load sample data."
- Connect each log message to `fetch`, `await`, and `response.json()`.

**Transition cue:**

- "The syntax can look neat, but waiting still happened."

### Slide 13 - Waiting Still Happens

Student-visible text:

```text
Do not let clean syntax trick you.

This code may look step-by-step:

- fetch
- await response
- await JSON
- use data

But the request still takes time.
```

**Instructor notes:**

- This is the concept students most need before Week 10.
- Avoid going deeper into event loop internals.

**Transition cue:**

- "AI can help explain the timeline, but it cannot replace your observation."

### Slide 14 - AI Can Explain The Timeline

Student-visible text:

```text
AI as Explainer:

Useful for:

- explaining output order
- identifying what happens now
- identifying what happens later
- explaining what the Promise represents

You still:

- write the code
- run the page
- observe the result
- explain your own timing
```

**Instructor notes:**

- Keep Week 8 in the Explainer role.
- This is a good continuation from Week 6-7 AI slides.
- Do not shift into "Assistant" language yet.

**Transition cue:**

- "A useful async prompt needs context, constraints, and the timeline question."

### Slide 15 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I manually wrote this async JavaScript example.
Do not rewrite it for me.
Explain the order of events:
what happens now, what happens later,
where the request starts,
and what the Promise represents.
Ask me one question before suggesting code."
```

**Instructor notes:**

- This deepens the Monday prompt for request-shaped behavior.
- Keep the role as Explainer.
- Students should use this to understand timing, not to generate a finished
  feature.

**Transition cue:**

- "For Thursday, the goal is to make your own timing clearer."

Visual notes:

- Form-like prompt card with labeled parts: context, constraint, timeline,
  request start, Promise meaning, and ask-first behavior.

### Slide 16 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab:

Improve your async behavior.

Choose at least one:

- add a second timed interaction
- improve the waiting message
- make the sequence clearer
- structure the timed code better

Keep it explainable.
```

**Instructor notes:**

- Connect directly to Assignment 8 Iteration 2.
- Encourage small, clear refinement over feature sprawl.

**Transition cue:**

- "Your evidence should prove that timing was intentional."

### Slide 17 - Evidence And Submission

Student-visible text:

```text
Submission evidence:

- timed behavior is visible
- waiting feedback is clear
- final result appears later
- code runs without errors
- reflection explains how timing changed your thinking

The timing should be intentional, not accidental.
```

**Instructor notes:**

- This slide mirrors the assignment language.
- Emphasize visible behavior and short reflection.

**Transition cue:**

- "Next week, we use structure to keep larger systems manageable."

### Slide 18 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Look for structure, not extra complexity.

Notice:

- responsibility
- separation of concerns
- module vs modularity
- files that work together
- code that is easier to find later

Ask:

"What part of the system does this belong to?"
```

**Instructor notes:**

- Week 9 shifts from timing to modular thinking.
- Tell students not to overbuild. The goal is organization.

**Transition cue:**

- "Week 8 gave us timing. Week 9 gives us places to put things."

### Slide 19 - Closing

Student-visible text:

```text
Async timing mental model:

`fetch` starts a request.

A Promise represents a future result.

`async` / `await` makes waiting easier to read.

Waiting still happens.
Good pages explain the wait.
```

**Instructor notes:**

- Close by repeating the handout summary.
- This is the sentence students should carry into Week 10.

**Transition cue:**

- "When your code waits clearly, your users trust what is happening."

---

# AI Use Notes

AI may explain async timelines, request/response vocabulary, Promise meaning, or
JSON shape. Students still need to manually write, test, observe, and explain
their own timed behavior.

---

# Image Prompt Notes

Use the Week 8 prompt packet for the following:

| Slide | Image Concept | Prompt Packet Note |
| --- | --- | --- |
| 1 | Monday now/later reconnect | Include in Week 8 prompt packet |
| 2 | Timing as user experience | Include in Week 8 prompt packet |
| 4 | Delay to request | Include in Week 8 prompt packet |
| 5 | Today's toolbox | Include in Week 8 prompt packet |
| 6 | Request and response | Include in Week 8 prompt packet |
| 7 | `fetch()` starts request | Include in Week 8 prompt packet |
| 8 | Promise future result | Include in Week 8 prompt packet |
| 9 | `async` / `await` readable waiting | Include in Week 8 prompt packet |
| 10 | JSON shape | Include in Week 8 prompt packet |
| 11 | Timing order demo | Include in Week 8 prompt packet |
| 12 | Fetch timing demo | Include in Week 8 prompt packet |
| 13 | Waiting still happens | Include in Week 8 prompt packet |
| 14 | AI explains timeline | Include in Week 8 prompt packet |
| 15 | useful AI prompt pattern | Include in Week 8 prompt packet |
| 19 | Async mental model | Include in Week 8 prompt packet |

No separate image prompt is needed for Slide 3 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- Monday reconnect: 3-5 minutes
- timing / UX framing: 5-8 minutes
- request / Promise / await concepts: 15-20 minutes
- JSON shape preview: 5-8 minutes
- demo sequence: 15-20 minutes
- AI-as-explainer boundary and prompt pattern: 4-6 minutes
- lab bridge / next reading: 5-8 minutes
