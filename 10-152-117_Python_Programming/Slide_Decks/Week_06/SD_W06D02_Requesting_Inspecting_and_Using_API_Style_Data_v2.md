# Slide Deck Source - Week 6 Day 2

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 6 / Tuesday  
**Date:** September 22, 2026  
**Weekly Theme:** APIs, External Data, and Python App Architecture  
**Lecture Title:** Requesting, Inspecting, and Using API-Style Data  
**Assignments Supported:** A11 - API Data Fetcher  
**Readiness Target:** Students can retrieve or load API-style JSON and select a few useful values.  
**Primary Watch Point:** Do not assume live API access will be stable; fallback path must be named explicitly.

---

# Session Purpose

This session is the main A11 implementation support day.

Students should understand that API-style work is not complete when data is
retrieved. They must inspect the response shape, select useful values, display
those values clearly, and validate the path they used.

The live API path and simulated JSON fallback path are both valid instructional
routes.

---

# Review / Prior Work Bridge

Review from Day 1:

- outside data adds dependency
- a program may need to wait for a response
- response data must be inspected before it is used
- simulated response data can preserve the learning target

Bridge question:

> Once data comes back, how do we avoid dumping everything and hoping it makes
> sense?

Today's answer:

> Inspect first, extract second.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 6
- Textbook area: **Introduction to API Development**

Today's focus:

- what an API is
- the purpose of an API
- response status codes
- API data-exchange formats
- selecting values from returned data

Skim or save for later:

- authentication
- full endpoint implementation
- API documentation tooling
- deployment concerns

---

# What We Will Use Today

Today we will use:

- API vocabulary
- endpoint as a place to ask
- response data
- JSON inspection
- selected values
- error or fallback thinking

Today we will not use yet:

- authentication
- building a full API
- deployment
- complex environment configuration
- raw JSON as the final result

---

# Assignments Supported

Primary assignment:

- A11 - API Data Fetcher

A11 asks students to:

- retrieve or load API-style JSON
- inspect the response
- select meaningful values
- display selected output clearly
- explain the request/response or fallback path

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_06_APIs_External_Data_and_App_Architecture/01_parse_simulated_api_response.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/02_select_values_from_api_data.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/03_handle_api_style_error.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/08_simulated_json_fallback_demo.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/09_environment_based_fallback_preview.py`

Supporting artifacts:

- `Approved_API_Guidance_for_Python.md`
- `Demos/Instructor_Notes-Simulated_JSON_Fallback.md`

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Bridge request/response to A11 |
| Working Set | 4-5 | Define API path and deferred complexity |
| Core Skill | 6-10 | Inspect, select, display, validate |
| Demos | 11-13 | Simulated response, selected values, error/fallback |
| Assignment Bridge | 14-16 | A11 evidence and AI accountability |
| Close | 17 | Define responsible API-style success |

---

## Slide 1 - Python Can Ask For Outside Information

**Delivery Category:** Core

**Student-Visible Text:**

An API gives a program a structured way to ask for information.

The response may come from a live service, a controlled endpoint, or a simulated
JSON file used for practice.

**Instructor Notes:**

Normalize both live and simulated paths immediately. Do not wait until live API
problems appear.

**Transition Cue:**

Before implementation details, return to the simple pattern from Day 1.

---

## Slide 2 - Review: Request, Response, Inspect, Use

**Delivery Category:** Review

**Student-Visible Text:**

The basic API-style pattern is:

- request or load data
- receive or open a response
- inspect the response shape
- select useful values
- display a clear result

**Instructor Notes:**

This repeats the Day 1 pattern and sets the day's implementation target.

**Transition Cue:**

Connect the new API vocabulary to the JSON work students already practiced in
Week 5.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

- identify the data source
- retrieve or load the response
- inspect the JSON shape
- select useful values
- display readable output
- explain the path used

**Instructor Notes:**

This reduces anxiety. APIs are not a total restart; they reuse the Week 5 habit
of inspecting structure before selecting values.

**Transition Cue:**

Now define the working vocabulary students need for that pattern.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- endpoint
- response
- status or error cue
- JSON shape
- selected fields
- fallback data when needed

**Instructor Notes:**

Keep vocabulary lean and connected to the assignment.

**Transition Cue:**

Name the advanced API work that is not part of today's coding target.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- API authentication
- creating endpoints
- API deployment
- full web-framework setup
- complex rate limits and production monitoring

Today we consume or inspect data. We do not build the API.

**Instructor Notes:**

Clear guardrail.

**Transition Cue:**

With the scope bounded, start with the beginner meaning of endpoint.

---

## Slide 6 - An Endpoint Is A Place To Ask

**Delivery Category:** Core

**Student-Visible Text:**

An endpoint is a defined place where a program asks for data.

For beginners, think of it as: "Ask this address for this kind of response."

**Instructor Notes:**

Use simple analogy, but avoid turning endpoint into a vague "website." It is a
defined source of structured response.

**Transition Cue:**

After the program asks the endpoint or data source, it needs a cue about what
happened.

---

## Slide 7 - Status Helps Explain What Happened

**Delivery Category:** Core

**Student-Visible Text:**

A response may include a status cue.

The status helps the program and the developer know whether the request
succeeded, failed, or needs another response.

**Instructor Notes:**

Keep status codes at recognition level. Use examples such as success versus not
found if helpful.

**Transition Cue:**

Even when the response succeeds, students should inspect before extracting.

---

## Slide 8 - Inspect First, Extract Second

**Delivery Category:** Core

**Student-Visible Text:**

Do not guess field names.

First inspect the response shape. Then select the values your program actually
needs.

**Instructor Notes:**

This is the core habit for A11. Repeat it during every demo.

**Transition Cue:**

That habit prevents raw JSON from being mistaken for a finished result.

---

## Slide 9 - Raw JSON Is Not The Finished Result

**Delivery Category:** Core

**Student-Visible Text:**

Printing raw JSON proves that data exists.

It does not prove that the program understood or used the data well.

**Instructor Notes:**

Students need a clear output target: selected values in a readable form.

**Transition Cue:**

Now clarify the two valid paths students may use to practice the same skill.

---

## Slide 10 - Live API And Simulated JSON

**Delivery Category:** Core

**Student-Visible Text:**

Two valid paths can teach the same core skill:

- live API path: request data from an approved source
- simulated path: load instructor-provided JSON with the same response shape

Both require inspection, selection, and explanation.

**Instructor Notes:**

This is the governance slide. It protects the assignment from unstable network
behavior.

**Transition Cue:**

Begin with the stable path so students can focus on response shape instead of
network instability.

---

## Slide 11 - Demo 1: Parse A Simulated Response

**Delivery Category:** Demo

**Student-Visible Text:**

Watch for:

- response structure
- labels
- nested values if present
- selected output

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\01_parse_simulated_api_response.py`

Start with simulated data because it is stable and lets students focus on shape.

**Demo Connection:**

Primary demo file: `01_parse_simulated_api_response.py`

**Transition Cue:**

After parsing the response, move from seeing the shape to choosing the values
that matter.

---

## Slide 12 - Demo 2: Select Values From API Data

**Delivery Category:** Demo

**Student-Visible Text:**

The program should choose useful values and show them clearly.

The selected output should be easier to understand than the original response.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\02_select_values_from_api_data.py`

Ask students what the output gained by being selected and formatted.

**Demo Connection:**

Primary demo file: `02_select_values_from_api_data.py`

**Transition Cue:**

Once selected output works, show how the program can respond when the preferred
path is not available.

---

## Slide 13 - Demo 3: Error And Fallback Path

**Delivery Category:** Demo

**Student-Visible Text:**

Responsible API-style programs plan for problems.

The fallback path keeps the learning target alive when the live path is not
available.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\03_handle_api_style_error.py`

Then use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\08_simulated_json_fallback_demo.py`

Optional extension:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\09_environment_based_fallback_preview.py`

Run or inspect error handling and fallback examples. Emphasize that fallback is
intentional design.

**Demo Connection:**

Primary demo files: `03_handle_api_style_error.py`,
`08_simulated_json_fallback_demo.py`, `09_environment_based_fallback_preview.py`

**Transition Cue:**

Now convert the demos into the exact assignment target for A11.

---

## Slide 14 - Assignment 11 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 11, build a small API-style data fetcher.

Your result should retrieve or load response data, select useful values, display
them clearly, and explain your data path.

**Instructor Notes:**

Give approved paths. Prevent students from wandering into unstable APIs.

**Transition Cue:**

Make the evidence requirements visible so students know what counts as complete.

---

## Slide 15 - Evidence For A11

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should show:

- code file
- data source or simulated JSON path
- selected-value output
- short request/response explanation
- validation or error note
- AI-use note if AI materially helped

**Instructor Notes:**

This is the practical Schoology/GitHub evidence list.

**Transition Cue:**

Because API code is easy for AI to hallucinate, add the verification expectation
before students begin lab work.

---

## Slide 16 - AI-Assisted API Code Must Be Verified

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

AI can suggest API code that looks believable but does not match the actual
response.

You must inspect the response, run the code, and explain what human decision you
made.

**Instructor Notes:**

This is an important conceptual-understanding-over-regurgitation moment.

**Transition Cue:**

Close by returning to the accountable explanation students should be able to
give.

---

## Slide 17 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> I know where the data came from, what shape it had, which values I selected,
> and how I verified the result.

**Instructor Notes:**

Close around accountable API use.

---

# Demo Execution Notes

Recommended order:

1. Show `simulated_weather_response.json`.
2. Run `01_parse_simulated_api_response.py`.
3. Run `02_select_values_from_api_data.py`.
4. Run `03_handle_api_style_error.py`.
5. Show `08_simulated_json_fallback_demo.py`.
6. Mention `09_environment_based_fallback_preview.py` only if the group is ready.

Use `Approved_API_Guidance_for_Python.md` before students choose live sources.

---

# Lab / Assignment Bridge

Students should begin A11 by choosing:

- approved live API path, or
- instructor-provided simulated JSON path

They should then identify:

- the data shape
- the values they want
- the readable output they will produce
- the error or validation check they will include

---

# README / Submission Expectations

Recommended A11 README structure:

```text
# API Data Fetcher

## Data source

## Live or simulated path

## Values selected

## How to run

## What I checked

## AI-use note, if used
```

---

# AI-Use Boundary

Manual first:

- inspect the response structure
- decide which values matter
- run the program
- verify output

AI may help with:

- explaining API vocabulary
- interpreting error messages
- comparing possible parsing approaches

AI must not replace response inspection or student explanation.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | API ask/response | Program asks endpoint or JSON file for structured data | Avoid browser UI |
| 2 | Request/response review | Request/load, response, inspect, select, display pattern | Keep sequence readable |
| 3 | Today's success pattern | Identify source, load response, inspect JSON, select values, explain path | Avoid implying API is a total restart |
| 4 | Working set | Endpoint, response, status, JSON shape, selected fields | Avoid vocabulary overload |
| 5 | Saved for later | Auth, endpoint creation, deployment, rate limits parked | Avoid scary production imagery |
| 6 | Endpoint | Defined place to ask for data | Avoid browser/web page UI |
| 7 | Status cue | Success/failure status as explanation cue | Keep status codes recognition-level |
| 8 | Inspect/extract | Response shape highlighted before selected output | Keep JSON tiny |
| 9 | Raw JSON not enough | Raw JSON contrasted with readable selected output | Avoid terminal dump dominance |
| 10 | Live/fallback paths | Two equal paths leading to same inspect/select skill | Do not rank paths visually |
| 11 | Simulated response demo | Stable JSON response parsed for structure | Avoid fake/lesser framing |
| 12 | Selected values demo | API data transformed into useful output card | Avoid dashboard styling |
| 13 | Error/fallback demo | Problem path leading to fallback response | Avoid alarmist network failure |
| 14 | A11 bridge | Data source to selected output to explanation | Keep assignment scope small |
| 15 | A11 evidence | Checklist with source, output, explanation, validation | Avoid audit/legal look |
| 16 | AI verification | AI suggestion compared against actual response shape | Avoid robot imagery if distracting |

---

# Instructor Timing Notes

Suggested timing:

- Review and API vocabulary: 12 minutes
- Core inspect/extract pattern: 15 minutes
- Demos: 25 minutes
- Assignment bridge: 10 minutes
- Student work: remaining time

If internet or live API setup creates friction, move immediately to simulated
JSON.

---

# Post-Lecture Notes

Use after teaching:

- Did students inspect before extracting?
- Did raw JSON dumping persist?
- Which API/fallback path worked best?
- Did AI-use accountability feel clear?
