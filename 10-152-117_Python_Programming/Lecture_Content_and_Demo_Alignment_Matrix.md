# LECTURE CONTENT AND DEMO ALIGNMENT MATRIX

**10-152-117 Python Programming**

---

# Purpose

This artifact maps the day-by-day lecture content and demo set against the assignments they are intended to support.

It exists to help answer:

* what students must be taught before an assignment is launched
* which demos support that content
* what readiness target should be achieved by the end of the session
* where hidden assumptions or misalignments may exist

This is a planning and alignment tool that sits between:

* the IIM
* the assignment week-day matrix
* the demo folders
* the success examples
* future lecture outlines and slides

---

# How to Read This Matrix

Each session includes:

* **Core Lecture Content** - the main concepts that need direct instruction
* **Recommended Demos** - the demos that most directly support those concepts
* **Assignments Supported** - the assignment(s) whose success depends on the session
* **Readiness Target** - what students should be able to do by the end of class
* **Assumptions / Watch Points** - likely places for hidden mismatch or overload

---

# Phase 1 - Foundations + Manual Habits

| Week | Day | Date | Core Lecture Content | Recommended Demos | Assignments Supported | Readiness Target | Assumptions / Watch Points |
| ---- | --- | ---- | -------------------- | ----------------- | --------------------- | ---------------- | -------------------------- |
| 1 | Monday | 2026-08-17 | what a program is, running Python, `print()`, strings, variables, visible output | `Week_01/01-03` first output and variable demos | A1 | students can run a tiny program and explain what a variable stores | do not assume `input()` yet; keep setup friction from consuming the session |
| 1 | Tuesday | 2026-08-18 | numbers, simple expressions, value changes, optional `input()` introduction, input-to-output flow | `Week_01/04-05` numeric and expression demos; use input demo only if introduced | A1 | students can trace values from numeric expression to printed result | if `input()` is introduced, keep it shallow; if not, A1 must allow assigned variables only |
| 1 | Thursday | 2026-08-20 | strings vs numbers vs booleans in actual code, combining values, simple type awareness through use | `Week_01/06` combined practical examples; [Instructor Notes - Typing vs Copy/Paste](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Typing_vs_CopyPaste.md) as framing | A1 | students can complete 2-3 tiny programs and explain inputs, outputs, and value changes | avoid encyclopedic built-in types coverage; success depends on confidence, not breadth |

---

# Phase 2 - Logic, Structure, and Code Literacy

| Week | Day | Date | Core Lecture Content | Recommended Demos | Assignments Supported | Readiness Target | Assumptions / Watch Points |
| ---- | --- | ---- | -------------------- | ----------------- | --------------------- | ---------------- | -------------------------- |
| 2 | Monday | 2026-08-24 | booleans, comparisons, `if` / `elif` / `else`, branch prediction | `Week_02/01-03` decision demos | A2 | students can predict which branch runs and explain why | keep examples small; do not yet mix in too much loop complexity |
| 2 | Tuesday | 2026-08-25 | `for`, `while`, repeated behavior, stopping conditions, infinite-loop risk | `Week_02/04-06` loop demos | A3 | students can explain what repeats and what stops repetition | if repeated input is shown, make sure students understand state change clearly |
| 2 | Thursday | 2026-08-27 | conditionals plus loops together, validation patterns, small menu logic | `Week_02/07-08` combined logic/repetition demos | A2, A3 | students can build or fix a small logic-and-repetition program | do not let combined examples become too large for line-by-line reasoning |
| 3 | Monday | 2026-08-31 | functions, named responsibility, parameters, return values, repeated code as a smell | `Week_03/01-03` repeated-code and function demos | A4 | students can explain what each function is responsible for | do not assume deep return-value fluency too fast; keep function count small and intentional |
| 3 | Tuesday | 2026-09-01 | lists, dictionaries, storing related data, iterating through collections | `Week_03/04-06` list/dictionary demos | A5 | students can store, retrieve, and loop through structured data | ensure dictionary access is explicitly taught before lookup-style tasks are assigned |
| 3 | Thursday | 2026-09-03 | organization choices, compare rough vs cleaner version, limited AI comparison after manual baseline | `Week_03/07` structure comparison demo | A4, A5 | students can compare a rough solution to a cleaner organized one | bounded AI use depends on manual baseline existing first; do not invert that sequence |
| 4 | Monday | 2026-09-07 | debugging as evidence gathering, print-debugging, expected vs actual, syntax vs logic bugs | `Week_04/01-03`, `Week_04/09-10`; [Instructor Notes - The Debugging Process](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Debugging_Process.md) | A6 | students can identify bug source evidence rather than only symptoms | print-debugging must be taught as intentional evidence, not random `print("here")` behavior |
| 4 | Tuesday | 2026-09-08 | reading procedural, function-based, and class-based code; plain-language explanation of classes, attributes, methods | `Week_04/06-08` organizational comparison demos | A7 | students can read and lightly modify a small class-based example | do not let this turn into full OOP theory; this is recognition and interpretation |
| 4 | Thursday | 2026-09-10 | testing basics, expected vs actual checks, pytest recognition, bounded AI debugging help after manual diagnosis | `Week_04/04-05`, `Week_04/11` pytest demo | A6, A7 | students can show simple validation evidence and explain why a fix works | pytest is recognition-plus-light-practice only; do not accidentally make it a hidden required syntax target |

---

# Phase 3 - Data, Files, and Bounded AI Support

| Week | Day | Date | Core Lecture Content | Recommended Demos | Assignments Supported | Readiness Target | Assumptions / Watch Points |
| ---- | --- | ---- | -------------------- | ----------------- | --------------------- | ---------------- | -------------------------- |
| 5 | Monday | 2026-09-14 | persistence, file paths, writing text, reading text, why programs remember data | `Week_05/01-02` text file demos | A8 | students can explain what a program writes, where it goes, and how it is loaded back | avoid jumping to JSON too early if plain file mental model is not clear first |
| 5 | Tuesday | 2026-09-15 | `try` / `except`, JSON and CSV basics, success vs failure handling | `Week_05/03-07` JSON, CSV, and file-error demos | A8, A9 | students can save/load simple structured data and explain at least one likely error path | assignment success assumes students can distinguish file-not-found from bad-data problems |
| 5 | Thursday | 2026-09-17 | data representation choices, files vs structured data vs model-like structures, ORM as recognition only | `Week_05/08` data representation preview | A9, A10 | students can compare multiple representations of the same information | this is a recognition bridge; do not accidentally drift into database implementation |
| 6 | Monday | 2026-09-21 | synchronous vs asynchronous recognition, request/response thinking, waiting and sequencing | `Week_06/04-05` request-response and async recognition demos | A10, A11 | students can explain sequential vs asynchronous thinking at a beginner level | async is recognition-level only; do not let terminology outpace practical understanding |
| 6 | Tuesday | 2026-09-22 | APIs, endpoints, requests, responses, JSON selection, approved API list, simulated fallback concept, validating AI-assisted code | `Week_06/01-04`, `Week_06/08-09`; [Approved API Guidance for Python](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Approved_API_Guidance_for_Python.md); [Instructor Notes - Simulated JSON Fallback](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Simulated_JSON_Fallback.md) | A11 | students can retrieve or load API-style JSON and select a few useful values | do not assume live API access will be stable; fallback path must be named explicitly, not implied |
| 6 | Thursday | 2026-09-24 | Python beyond console scripts, MVT, templates, forms, views, architecture recognition | `Week_06/06-07` architecture preview demos | A11, A12 | students can explain where input, validation, logic, and display live in a larger app flow | do not let Django preview become a hidden framework requirement |

---

# Phase 4 - RBA Mini-Unit + Capstone Application

| Week | Day | Date | Core Lecture Content | Recommended Demos | Assignments Supported | Readiness Target | Assumptions / Watch Points |
| ---- | --- | ---- | -------------------- | ----------------- | --------------------- | ---------------- | -------------------------- |
| 7 | Monday | 2026-09-28 | RBA as a distinct paradigm, prompt-first vs intent-first, purpose before generation | `Week_07/01-02` framing and comparison demos | A13 | students can describe why framing before generation improves project quality | do not let RBA become abstract philosophy; keep it tied to concrete project framing |
| 7 | Tuesday | 2026-09-29 | constraints, structure choice, risks, AI boundaries, bounded upward revision | `Week_07/03-04`, `Week_07/06` scope and structure demos | A13, A14 | students can revise a project idea into a realistic structured proposal | proposal success depends on scope control being taught directly, not assumed |
| 7 | Thursday | 2026-10-01 | project-path comparison, capstone proposal quality, approval criteria, explainable scope | `Week_07/05-06` capstone proposal and structure comparison demos | A14 | students can justify project type, scope, and AI-use boundaries for approval | students may overreach; approval day must actively cut feature bloat rather than merely receive proposals |
| 8 | Monday | 2026-10-05 | capstone expectations, what counts as validation, AI-use accountability expectations | `Week_08/01-03` validation and AI justification demos | A15 | students can identify what part of their project matters most and how they will verify it | do not assume students know what “validation evidence” looks like unless modeled explicitly |
| 8 | Tuesday | 2026-10-06 | revision, refactoring, reality contact, coherence over feature sprawl | `Week_08/02`, `Week_08/05` validation notes and revision-after-reality-contact demos | A15 | students can describe what they changed, cut, or revised and why | this day must normalize scope reduction and revision as strength, not failure |
| 8 | Thursday | 2026-10-08 | presentation as explanation, run instructions, AI-use justification, professional defense of work | `Week_08/03-06` AI justification, presentation outline, and run instructions demos | A16 | students can explain project purpose, logic, testing, AI use, and one meaningful revision | final success depends on explanation quality; students should not be evaluated on a demo they cannot run clearly |

---

# Cross-Course Readiness Checks

## Assignment 1 Readiness Check

Before A1 is fully in motion, students should have seen:

* `print()`
* strings
* variables
* simple numeric expressions
* optional `input()` only if intentionally introduced

## Assignment 6 Readiness Check

Before A6 is launched, students should have seen:

* syntax error examples
* logic bug examples
* expected vs actual comparisons
* print-debugging as evidence

## Assignment 11 Readiness Check

Before A11 is launched, students should have seen:

* API terminology
* response structure inspection
* one selected-value example
* simulated fallback concept
* approved API list guidance

## Assignment 14 Readiness Check

Before A14 is submitted, students should have practiced:

* project purpose statements
* scope reduction
* structure choice
* AI boundary definition

---

# Most Likely Misalignment Risks

## Risk 1 - `input()` appears before it is stable

If Week 1 overloads students with `input()` too early, Assignment 1 may become harder than intended.

Response:

* keep assigned variables as an allowed path
* treat `input()` as optional until students can trace it comfortably

## Risk 2 - Pytest drifts from recognition into hidden requirement

Week 4 now includes pytest exposure, but Assignment 6 should still center on debugging evidence and validation reasoning rather than pytest syntax mastery.

Response:

* keep pytest optional or instructor-directed
* grade diagnosis and explanation more than framework syntax

## Risk 3 - API work depends too heavily on live internet behavior

If the live endpoint becomes the main challenge, Assignment 11 drifts away from JSON structure and validation.

Response:

* keep simulated JSON fallback explicit
* use approved APIs
* preserve the fallback path as legitimate instructional practice

## Risk 4 - Architecture preview becomes accidental framework instruction

Week 6 app-architecture recognition should help students see where Python can go next without making them think Django fluency is required.

Response:

* keep the preview bounded
* use plain-language flow explanation
* avoid full framework setup demands

## Risk 5 - RBA becomes too abstract or too universal

If Week 7 is taught as a generalized philosophy rather than a bounded project-framing process, students may lose the practical connection.

Response:

* keep RBA tied to capstone framing
* emphasize that it is emerging, not universal
* teach it through project choices, not theoretical excess

---

# Use for Lecture Outline Drafting

This matrix should be used before writing detailed lecture outlines.

For each lecture outline, confirm:

1. Which readiness target is the lecture responsible for?
2. Which demo(s) directly support that target?
3. Which assignment depends on this content later?
4. What assumption must be made explicit so students are not surprised later?

