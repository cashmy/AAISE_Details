# SLIDE DECK - WEEK 6 DAY 2

* Course: 10-152-117 Python Programming
* Week / Day: Week 6 / Tuesday
* Date: September 22, 2026
* Weekly Theme: APIs, External Data, and Python App Architecture
* Lecture Title: Requesting, Inspecting, and Using API-Style Data
* Assignments Supported: A11 - API Data Fetcher
* Readiness Target: students can retrieve or load API-style JSON and select a few useful values
* Primary Watch Point: do not assume live API access will be stable; fallback path must be named explicitly, not implied

---

### SLIDE 1 - OPENING FRAME

Python can ask
for outside information.

---
Cue:
- Frame APIs as structured outside information, not magical internet behavior.
- Keep the first success target small and believable.

Visual:
- Layout: Simple flow
- Content:
  - program
  - endpoint or file
  - returned data
- Purpose:
  - introduce API-style interaction as request and response

### SLIDE 2 - COURSE POSITIONING

Last week: stored data.
Today: requested data.

---
Cue:
- Tie APIs directly to the JSON work students already know.
- Emphasize continuity between local structured data and external structured data.

Visual:
- Layout: Compare
- Content:
  - local JSON file
  - API response JSON
- Purpose:
  - show that the structure-reading skill transfers cleanly

### SLIDE 3 - CORE IDEA

An endpoint
is a defined place to ask.

---
Cue:
- Keep the endpoint model simple and concrete.
- Avoid overloading with protocol detail.

Visual:
- Layout: Isolated focus
- Content:
  - one endpoint label
  - one request arrow
  - one response arrow
- Purpose:
  - install a clean mental model of API access

### SLIDE 4 - CORE IDEA

Inspect first.
Extract second.

---
Cue:
- Make this the day’s main thinking tool.
- Push structure inspection before field guessing every time.

Visual:
- Layout: Two-step sequence
- Content:
  - response shape
  - selected values
- Purpose:
  - anchor responsible JSON use

### SLIDE 5 - DEMO ANCHOR

Watch the shape.
Then choose the value.

---
Cue:
- Use before the parsing and selected-values demos.
- Focus students on meaningful extraction, not raw dumping.

Visual:
- Layout: Annotated response
- Content:
  - response sample
  - chosen fields highlighted
- Purpose:
  - direct demo attention to inspection and selection

### SLIDE 6 - SYSTEM

Live API
and fallback JSON
are both valid paths.

---
Cue:
- Be explicit that fallback is part of the design, not an afterthought.
- This is one of the most important governance points for Week 6.

Visual:
- Layout: Two-path flow
- Content:
  - live endpoint path
  - simulated JSON fallback path
- Purpose:
  - legitimize both instructional routes clearly

### SLIDE 7 - COMMON FAILURE

Raw JSON
is not the finished result.

---
Cue:
- Push students beyond retrieval-only behavior.
- Require one or two meaningful values and a useful summary.

Visual:
- Layout: Contrast
- Content:
  - full raw payload
  - cleaned selected summary
- Purpose:
  - reinforce output selection as the real success target

### SLIDE 8 - BRIDGE

Choose a source.
Choose useful values.

---
Cue:
- Bridge directly to Assignment 11.
- Keep the assignment target bounded: inspect, extract, explain.

Visual:
- Layout: Decision panel
- Content:
  - live approved API
  - fallback JSON
  - selected fields output
- Purpose:
  - connect the lecture to the approved-path assignment design

### SLIDE 9 - CLOSING

If you can inspect the response
and justify the path,
you are using the API responsibly.

---
Cue:
- End with judgment and explanation, not just connectivity.
- Tie in the accountability layer if AI helped scaffold anything.

Visual:
- Layout: Isolated focus
- Content:
  - response sample
  - chosen values
  - live/fallback note
- Purpose:
  - close around the readiness target and watch point together
