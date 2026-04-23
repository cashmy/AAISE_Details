# WEEK 6 DAY 2 LECTURE OUTLINE

**10-152-117 Python Programming**

---

# 1. Session Identity

* **Week / Day:** Week 6 / Tuesday
* **Date:** September 22, 2026
* **Weekly Theme:** APIs, External Data, and Python App Architecture
* **Lecture Title:** Requesting, Inspecting, and Using API-Style Data

---

# 2. Alignment Anchor

* **Assignments Supported:** A11 - API Data Fetcher
* **Readiness Target:** students can retrieve or load API-style JSON and select a few useful values
* **Primary Watch Point:** do not assume live API access will be stable; fallback path must be named explicitly, not implied

---

# 3. Opening Frame (2-4 minutes)

Today makes Python feel connected to the outside world.

Key message:

* APIs are structured sources of external information
* useful API work begins with reading the response shape carefully
* the first success is one useful selected value, not a full application

Suggested wording:

> "The goal today is not to consume an entire API. The goal is to request or load API-style data, inspect its structure, and use one or two values correctly."

---

# 4. Course Positioning (2-4 minutes)

Students now know:

* what structured data looks like
* how waiting can affect program flow

Today adds:

* endpoints
* requests and responses
* selected-value extraction from API-style JSON
* explicit live-versus-fallback thinking

Suggested wording:

> "This session connects your JSON skills to real or simulated external data. The key skill is not 'use the internet.' The key skill is 'read the response and choose useful values responsibly.'"

---

# 5. Core Concepts (10-20 minutes)

## Concept 1 - APIs expose structured endpoints

Plain-language explanation:

* an API gives a program a defined place to request information

Why it matters:

* students need a clean mental model for what an endpoint is

## Concept 2 - A response must be inspected before it is used

Plain-language explanation:

* JSON should be read carefully before values are selected

Why it matters:

* Assignment 11 depends on structure inspection and extraction, not blind guessing

## Concept 3 - Live API and simulated fallback are both legitimate instructional paths

Plain-language explanation:

* sometimes the live API works
* sometimes a saved JSON response is the better path for the lesson

Why it matters:

* the fallback is part of the design, not an emergency afterthought

## Concept 4 - AI can help scaffold, but humans must validate

Plain-language explanation:

* AI may help generate a first request pattern or response-handling draft
* the student must still inspect, test, and explain the result

Why it matters:

* this is a key Week 6 accountability bridge

---

# 6. Demo Plan (10-20 minutes)

## Demo 1

* **Artifact:** simulated API response parsing demo
* **Focus:** inspect and extract selected values from JSON
* **Students should notice:** the structure determines how the values are accessed

## Demo 2

* **Artifact:** selected-values API summary demo
* **Focus:** print meaningful information instead of raw JSON
* **Students should notice:** useful output is chosen, not dumped

## Demo 3

* **Artifact:** simulated JSON fallback demo and environment-based fallback preview
* **Focus:** why fallback exists and how development conditions may justify it
* **Students should notice:** fallback is a legitimate design and teaching strategy

Instructional note:

* use [Approved API Guidance for Python](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Approved_API_Guidance_for_Python.md) and [Instructor Notes - Simulated JSON Fallback](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Simulated_JSON_Fallback.md) explicitly

---

# 7. Hands-On / Lab Bridge (10-20 minutes)

Students should try:

* loading or requesting API-style data
* selecting one or two useful fields
* displaying a meaningful summary
* using fallback JSON when appropriate

Suggested wording:

> "Your goal today is not to use every field in the response. Your goal is to inspect the structure, choose a few meaningful values, and explain why those are the values your program is showing."

Do not require:

* large API coverage
* authentication systems
* rate-limit management
* advanced network tooling

---

# 8. Common Mistakes / Watch-Fors (5-8 minutes)

## Mistake 1 - printing raw JSON and stopping there

Why it happens:

* students may think retrieval alone is the goal

Correction:

* require selected values and meaningful output

## Mistake 2 - guessing the structure without inspecting it

Why it happens:

* students may assume field names or nesting

Correction:

* model inspection before extraction every time

## Mistake 3 - fallback is seen as a shortcut instead of a design decision

Why it happens:

* students may assume local JSON is "less real"

Correction:

* frame fallback as controlled development and instructional practice

---

# 9. Explain / Checkpoint Questions (3-8 minutes)

Ask:

* What endpoint or file did your program use?
* What did the response look like?
* Which values did you choose to display?
* Why is a simulated fallback legitimate in some situations?
* What still required human judgment if AI helped scaffold the code?

---

# 10. End-of-Class Success Check

> By the end of this session, students should be able to retrieve or load API-style JSON, inspect its structure, choose a few meaningful values, and explain why a live or fallback path was used.

---

# 11. Materials / Artifacts Used

* Week 6 API response, selection, fallback, and environment preview demos
* [Approved API Guidance for Python](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Approved_API_Guidance_for_Python.md)
* [Instructor Notes - Simulated JSON Fallback](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Simulated_JSON_Fallback.md)
* A11 - API Data Fetcher
* [Lecture Content and Demo Alignment Matrix](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md)

