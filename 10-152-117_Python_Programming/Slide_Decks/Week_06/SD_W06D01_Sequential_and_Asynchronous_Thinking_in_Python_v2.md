# Slide Deck Source - Week 6 Day 1

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 6 / Monday  
**Date:** September 21, 2026  
**Weekly Theme:** APIs, External Data, and Python App Architecture  
**Lecture Title:** Sequential and Asynchronous Thinking in Python  
**Assignments Supported:** A10 - Data Representation and App-Structure Preview; A11 - API Data Fetcher  
**Readiness Target:** Students can explain sequential versus asynchronous thinking at a beginner level.  
**Primary Watch Point:** Async is recognition-level only; do not let terminology outpace practical understanding.

---

# Session Purpose

This session bridges from local files and data representation into external data
and request/response thinking.

Students do not need to write asynchronous Python. They need to recognize that
some programs depend on outside responses, and that waiting can affect the flow
of a program.

This prepares A11 without creating a hidden async requirement.

---

# Review / Prior Work Bridge

Review from Week 5:

- Data can live outside the running program.
- Programs can read structured information from files.
- Representation changes how data is used.

Bridge question:

> What changes when the information is not already on your computer?

Today's answer:

> The program may need to request it and wait for a response.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 6
- Textbook areas: **Files and Data Persistence** and **Introduction to API Development**

Today's focus:

- I/O, streams, and requests
- making HTTP requests
- Hypertext Transfer Protocol as recognition
- request/response thinking
- sequential versus asynchronous recognition

Skim or save for later:

- asynchronous programming syntax
- framework setup
- deployment
- authentication
- full API implementation

---

# What We Will Use Today

Today we will use:

- sequential flow
- request/response vocabulary
- waiting as a program behavior
- simple external-data mental models
- simulated examples

Today we will not use yet:

- `async` / `await` as required syntax
- concurrent program design
- live API dependence as the only path
- framework setup

---

# Assignments Supported

Assignments supported:

- A10 - Data Representation and App-Structure Preview
- A11 - API Data Fetcher

A10 closes around representation comparison.

A11 begins with the idea that outside data is requested, received, inspected,
and selected.

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_06_APIs_External_Data_and_App_Architecture/04_request_response_flow.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/05_async_recognition_preview.py`

Supporting preview if time permits:

- `Demos/Week_06_APIs_External_Data_and_App_Architecture/08_simulated_json_fallback_demo.py`

Keep async recognition conceptual. Do not turn this into syntax mastery.

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Bridge local data to outside responses |
| Working Set | 4-5 | Set async as recognition-level |
| Core Flow | 6-9 | Explain sequential flow, waiting, and request/response |
| Demos | 10-11 | Show request/response and async recognition |
| Assignment Bridge | 12-14 | Transition from A10 to A11 |
| Close | 15 | Define success as explanation |

---

## Slide 1 - Sometimes Programs Have To Wait

**Delivery Category:** Core

**Student-Visible Text:**

Some programs can do everything with local values and files.

Other programs ask for information from somewhere else, and that outside
response may take time.

**Instructor Notes:**

Frame this as normal program behavior. Avoid making async sound exotic.

**Visual Notes:**

Program step, waiting marker, response step.

---

## Slide 2 - Review: Local Data Was Available Immediately

**Delivery Category:** Review

**Student-Visible Text:**

Last week, our data was stored locally.

The file might be missing or invalid, but the program was still looking for
information in a known place.

**Instructor Notes:**

Bridge from file errors to external dependency. Local files can fail; outside
responses add timing and access issues.

---

## Slide 3 - Outside Data Adds A Dependency

**Delivery Category:** Core

**Student-Visible Text:**

When a program asks an outside source for data, it depends on something beyond
itself.

That dependency can affect timing, reliability, and how we test the program.

**Instructor Notes:**

This prepares students to accept fallback JSON as legitimate rather than fake.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- sequential flow
- request
- response
- waiting point
- simulated response
- beginner-level async recognition

**Instructor Notes:**

This is a vocabulary and mental-model day.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- writing asynchronous programs
- `async` / `await` mastery
- concurrent design
- API authentication
- deployment

Today we recognize the idea without making it a required coding target.

**Instructor Notes:**

Important anxiety reducer and scope guard.

---

## Slide 6 - Sequential Flow Happens In Order

**Delivery Category:** Core

**Student-Visible Text:**

Sequential code runs step by step.

Python completes one instruction, then moves to the next instruction.

**Instructor Notes:**

Students have been using sequential thinking all along. Name it explicitly.

---

## Slide 7 - Requests Interrupt The Simple Story

**Delivery Category:** Core

**Student-Visible Text:**

A request asks another system for information.

The program may need to wait before it can use the response.

**Instructor Notes:**

Keep this practical: "Ask, wait, receive, inspect, use."

---

## Slide 8 - Request / Response Thinking

**Delivery Category:** Core

**Student-Visible Text:**

API-style work often follows this pattern:

- request data
- receive a response
- inspect the response shape
- select useful values
- display or use the result

**Instructor Notes:**

This is the A11 thinking pattern. It echoes Week 5's structured data work.

---

## Slide 9 - Waiting Does Not Always Mean Broken

**Delivery Category:** Core

**Student-Visible Text:**

When outside data is involved, delay can be normal.

The real questions are: what is the program waiting for, and what should happen
if the response does not arrive as expected?

**Instructor Notes:**

This connects to error handling without diving into network exception details.

---

## Slide 10 - Demo 1: Request / Response Flow

**Delivery Category:** Demo

**Student-Visible Text:**

Watch for:

- where the request happens
- what response returns
- which values are selected
- what output proves the flow worked

**Instructor Notes:**

Run the demo slowly. Ask students to narrate the flow before discussing code
details.

**Demo Connection:**

Primary demo file: `04_request_response_flow.py`

---

## Slide 11 - Demo 2: Async Recognition Preview

**Delivery Category:** Demo

**Student-Visible Text:**

This demo is for recognition.

You do not need to write async code today. You only need to recognize why
waiting can change how a program is organized.

**Instructor Notes:**

Do not make students copy async syntax. The point is the idea.

**Demo Connection:**

Primary demo file: `05_async_recognition_preview.py`

---

## Slide 12 - Common Failure: Vocabulary Before Meaning

**Delivery Category:** Core

**Student-Visible Text:**

Words like synchronous, asynchronous, endpoint, and response can sound bigger
than the idea.

Start with the plain question: what is the program waiting for?

**Instructor Notes:**

Use this slide to de-escalate terminology.

---

## Slide 13 - Assignment 11 Preview

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Assignment 11 will ask you to work with API-style data.

Your first job is not to impress the internet. Your first job is to inspect the
response and choose useful values.

**Instructor Notes:**

This is a gentle but firm guardrail against raw JSON dumping or live-API drama.

---

## Slide 14 - Live API And Fallback Are Both Legitimate

**Delivery Category:** Core

**Student-Visible Text:**

A live API can be useful, but it can also fail for reasons outside your code.

Simulated JSON can still teach the core skill: inspect the response, select
values, and explain the flow.

**Instructor Notes:**

This anticipates Tuesday. Say explicitly that fallback is not lesser learning.

---

## Slide 15 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> This program asks for data, waits for a response, inspects what came back, and
> then uses selected values.

**Instructor Notes:**

Close with explanation, not syntax.

---

# Demo Execution Notes

Recommended order:

1. Review A10 representation comparison if needed.
2. Run `04_request_response_flow.py`.
3. Ask students to identify request, response, and selected values.
4. Run or inspect `05_async_recognition_preview.py`.
5. Explain why async remains recognition-level.

Optional:

6. Preview `08_simulated_json_fallback_demo.py` as a bridge to Tuesday.

---

# Lab / Assignment Bridge

Use remaining time to:

- close or review A10
- introduce A11 expectations
- help students choose between live API and simulated data paths

Do not require students to finish A11 today.

---

# README / Submission Expectations

For A11, students will later need to explain:

```text
## Data source

## Request or simulated response path

## Values selected from the response

## Validation or error check

## AI-use note, if used
```

---

# AI-Use Boundary

AI can help explain terms such as:

- request
- response
- endpoint
- synchronous
- asynchronous

AI should not generate code that students cannot inspect, run, and explain.

For A11, students must validate any AI-assisted API code against the actual or
simulated response structure.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Waiting point | Program step pauses before response returns | Avoid spinning-loader UI only |
| 3 | Outside dependency | Program connected to outside data source | Avoid cloud infrastructure complexity |
| 8 | Request/response | Ask, receive, inspect, select, display flow | Keep labels large |
| 11 | Async recognition | Two lanes: sequential and waiting-aware | No code-heavy async syntax |
| 14 | Live/fallback | Two legitimate paths to same JSON skill | Do not imply fallback is inferior |

---

# Instructor Timing Notes

Suggested timing:

- Review and concept framing: 12 minutes
- Sequential/request-response explanation: 18 minutes
- Demos: 20 minutes
- A11 preview and lab transition: 10 minutes
- Student work / questions: remaining time

If students are uneasy, skip async demo execution and use a visual explanation
only.

---

# Post-Lecture Notes

Use after teaching:

- Did async recognition confuse or clarify?
- Did students accept simulated JSON as legitimate?
- Did A10 close cleanly?
- What API path should be emphasized on Day 2?
