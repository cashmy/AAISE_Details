# INSTRUCTIONAL INTENT MAP (IIM) — Python Programming

---

# COURSE DESIGN POSITION

This course teaches Python first.

AI-assisted development is introduced deliberately and bounded by student understanding.

Refraction-Based Architecture (RBA) is included as a compressed mini-unit later in the course, not as the invisible default operating system of the entire class.

This design preserves:

* manual-first foundational learning
* stronger anti-cheating habits in the early weeks
* a clearer distinction between Python fundamentals and an emerging development framework
* a bounded but meaningful use of RBA to improve capstone quality, productivity, and feature depth

---

# STRUCTURAL MODEL

This course uses a three-layer instructional structure:

* **Phases** provide the high-level map of the course
* **Weekly Themes** give each week a clear, student-friendly focus
* **Session Micro-Arcs** keep each class cognitively manageable

This structure supports consistency, pacing, and UDL-friendly instructional design.

---

# SESSION MICRO-ARC

Each class meeting should contain a smaller instructional cycle rather than placing all lecture on one day and all application on another.

Recommended pattern within each session:

* **Concept Frame** = short lecture, framing, vocabulary, mental model
* **Demo / Guided Example** = instructor-led modeling or code walkthrough
* **Hands-On Practice** = immediate student use, guided build, or lab activity
* **Explain / Checkpoint** = short reflection, debugging check, explanation, or compare-and-revise moment

This preserves a consistent learner experience across the course while reducing cognitive overload.

---

# TREATMENT LEVELS

* **Core Manual** = students should write, trace, debug, and explain this largely on their own
* **Guided AI-Supported** = students may use AI support in a bounded way, but must validate, adapt, and explain the result
* **Recognition / Interpretation** = students should recognize the construct, read simple examples, and understand why AI or other developers may use it

---

# PHASE 1 — FOUNDATIONS + MANUAL HABITS (Weeks 1-2)

**Purpose:** establish confidence, reduce fear, create manual-first habits, and focus only on the smallest useful subset of Python needed to build first programs

---

## Week 1 Theme — First Programs and Basic Values

### Monday

**Concept Frame**

* What programming is
* How this course works
* What a Python program does

**Demo / Guided Example**

* `print()`
* simple strings
* simple variables

**Hands-On Practice**

* first tiny programs
* greeting output
* simple variable substitution

**Explain / Checkpoint**

* students describe what each line does
* normalize setup and syntax mistakes

### Tuesday

**Concept Frame**

* numbers as values
* simple expressions
* input and output

**Demo / Guided Example**

* numeric calculations
* user input
* converting values where needed

**Hands-On Practice**

* simple calculator-style scripts
* unit converter or total-cost examples

**Explain / Checkpoint**

* trace values from input to output
* identify simple errors

### Thursday

**Concept Frame**

* basic type awareness through use, not encyclopedic coverage
* strings vs numbers vs booleans in real code

**Demo / Guided Example**

* combining strings, numbers, and input in one small program

**Hands-On Practice**

* build 2-3 very small practical programs

**Explain / Checkpoint**

* explain inputs, outputs, and value changes step by step

### Topic Treatment

* **Core Manual:** setup, script execution, strings, integers, floats, booleans, variables, input/output, simple expressions
* **Guided AI-Supported:** instructor demonstration only if needed, not normal student lab use
* **Recognition / Interpretation:** textbook coverage includes many more built-in types than students need in Week 1; those broader types will be introduced later as instructionally useful

---

## Week 2 Theme — Decision Logic and Repetition

### Monday

**Concept Frame**

* booleans and comparisons
* how programs make decisions

**Demo / Guided Example**

* `if`, `elif`, `else`
* simple branching examples

**Hands-On Practice**

* decision-based programs such as grading checks or eligibility checks

**Explain / Checkpoint**

* predict which path the code will take before running it

### Tuesday

**Concept Frame**

* repetition as a programming tool
* `for` and `while` at a beginner-friendly level

**Demo / Guided Example**

* counting loops
* repeating prompts
* input loops with stopping conditions

**Hands-On Practice**

* simple number sequences
* repeated input programs

**Explain / Checkpoint**

* identify where loops begin, stop, or go wrong

### Thursday

**Concept Frame**

* conditionals and loops working together

**Demo / Guided Example**

* menu or simple validation examples

**Hands-On Practice**

* small logic-and-repetition mini-programs

**Explain / Checkpoint**

* debug missing updates, incorrect conditions, and infinite-loop behavior

### Topic Treatment

* **Core Manual:** booleans, comparisons, conditionals, `for`, `while`, range, loop control through state change
* **Guided AI-Supported:** none as normal workflow yet
* **Recognition / Interpretation:** students begin to see that clear logic must come before tooling support

---

# PHASE 2 — STRUCTURE + CODE LITERACY (Weeks 3-4)

**Purpose:** help students move from isolated code fragments toward readable, organized programs and begin controlled comparison with AI-supported code

---

## Week 3 Theme — Organizing Code and Data

### Monday

**Concept Frame**

* functions as reusable named logic
* why repeated code becomes a problem

**Demo / Guided Example**

* turning repeated steps into functions
* parameters and return values

**Hands-On Practice**

* refactor earlier programs into functions

**Explain / Checkpoint**

* explain what each function is responsible for

### Tuesday

**Concept Frame**

* lists and dictionaries as practical storage tools

**Demo / Guided Example**

* storing and retrieving values
* iterating through collections

**Hands-On Practice**

* trackers, menus, or lookup tools using lists and dictionaries

**Explain / Checkpoint**

* explain how data moves through the program

### Thursday

**Concept Frame**

* organization choices affect readability and maintainability

**Demo / Guided Example**

* compare a rough manual solution with a cleaner organized version

**Hands-On Practice**

* build a small multi-function mini-app
* compare one manual baseline with one limited AI-generated variation

**Explain / Checkpoint**

* identify what improved and what still needs revision

### Topic Treatment

* **Core Manual:** functions, parameters, return values, lists, dictionaries, indexing, collection iteration
* **Guided AI-Supported:** controlled comparison of a student solution with an AI-generated variation after a manual baseline exists
* **Recognition / Interpretation:** tuples and additional built-in collection types may be recognized by contrast, but are not all performance-level targets here

---

## Week 4 Theme — Debugging, Testing, and Reading Structured Code

### Monday

**Concept Frame**

* debugging as a normal engineering practice
* testing through sample inputs and edge cases

**Demo / Guided Example**

* tracing values
* print-based debugging
* checking expected vs actual output

**Hands-On Practice**

* debug intentionally broken examples

**Explain / Checkpoint**

* identify bug source rather than only the symptom

### Tuesday

**Concept Frame**

* reading code written in different organizational styles
* why AI often returns class-based structures

**Demo / Guided Example**

* procedural version
* function-based version
* simple class-based version of the same problem

**Hands-On Practice**

* inspect and modify a simple class-based example

**Explain / Checkpoint**

* explain `class`, `__init__`, attributes, and methods in plain language

### Thursday

**Concept Frame**

* debugging and explanation are part of code ownership

**Demo / Guided Example**

* compare multiple fixes for the same problem

**Hands-On Practice**

* diagnose, repair, and explain broken code
* use tightly bounded AI support for debugging or explanation only after manual diagnosis is attempted

**Explain / Checkpoint**

* justify why a fix works

### Topic Treatment

* **Core Manual:** tracing, debugging workflow, testing basics, code explanation
* **Guided AI-Supported:** bounded debugging help, code explanation, alternate-fix comparison
* **Recognition / Interpretation:** classes, objects, attributes, methods, `__init__`, class-based code as a common AI default

---

# PHASE 3 — DATA, FILES, AND BOUNDED AI SUPPORT (Weeks 5-6)

**Purpose:** connect Python to data formats, files, and external information while introducing more intentional but still governed AI-assisted development

---

## Week 5 Theme — Files, Errors, and Data Persistence

### Monday

**Concept Frame**

* persistence: programs can remember information
* file work as a practical programming skill

**Demo / Guided Example**

* reading and writing text files

**Hands-On Practice**

* small save/load examples

**Explain / Checkpoint**

* explain what data is stored and where it goes

### Tuesday

**Concept Frame**

* errors as expected events that require handling
* structured data formats at a beginner-friendly level

**Demo / Guided Example**

* `try` / `except`
* CSV and JSON basics

**Hands-On Practice**

* load and use simple CSV or JSON data

**Explain / Checkpoint**

* explain how the program handles success vs failure

### Thursday

**Concept Frame**

* practical data handling often involves revision and cleanup

**Demo / Guided Example**

* compare alternate parsing or error-handling approaches

**Hands-On Practice**

* build a small data-driven utility that saves and reloads information
* use AI in a bounded way only after manual work is underway

**Explain / Checkpoint**

* identify what was improved and how correctness was checked

### Topic Treatment

* **Core Manual:** file I/O basics, text files, CSV/JSON reading and writing, simple exception handling
* **Guided AI-Supported:** parsing helpers, error-message revision, comparison of alternate data-handling solutions
* **Recognition / Interpretation:** config-style data, context managers, more advanced exception patterns if surfaced by AI

---

## Week 6 Theme — APIs, External Data, and Responsible AI Use

### Monday

**Concept Frame**

* APIs as structured ways programs retrieve or send information
* endpoints, requests, responses, and JSON as practical terms

**Demo / Guided Example**

* read a simple endpoint example
* inspect a structured response

**Hands-On Practice**

* retrieve and inspect small pieces of external data

**Explain / Checkpoint**

* explain how request and response fit together

### Tuesday

**Concept Frame**

* responsible AI use in more complex programming tasks
* tokens/authentication as recognition-level ideas tied to access and permissions

**Demo / Guided Example**

* compare manual API code with AI-assisted code generation for the same task

**Hands-On Practice**

* adapt request code, parse useful values, and revise structure

**Explain / Checkpoint**

* explain what AI helped with and what still required human decisions

### Thursday

**Concept Frame**

* bounded AI support requires validation, not trust

**Demo / Guided Example**

* show how a plausible AI-generated example can still need correction

**Hands-On Practice**

* build a small external-data feature into an existing mini-app

**Explain / Checkpoint**

* justify what was accepted, changed, or rejected

### Topic Treatment

* **Core Manual:** API basics, requests/responses at an introductory level, reading structured JSON responses
* **Guided AI-Supported:** request scaffolding, endpoint adaptation, response formatting, bounded code generation
* **Recognition / Interpretation:** tokens, auth headers, rate limits, decorators/iterators or wrappers if encountered in library examples

---

# PHASE 4 — RBA MINI-UNIT + CAPSTONE APPLICATION (Weeks 7-8)

**Purpose:** give students a bounded introduction to RBA as an emerging development paradigm, then apply it to capstone framing, productivity, coherence, and explanation

---

## Week 7 Theme — RBA and Project Framing

### Monday

**Concept Frame**

* RBA as an emerging AI-era development framework
* the instructor's real project-development process
* why RBA differs from ad hoc prompting-first behavior and may differ from traditional shop norms

**Demo / Guided Example**

* compare a weakly framed project start with an intent-first, structure-first project start

**Hands-On Practice**

* analyze small project starts and identify which one has stronger framing

**Explain / Checkpoint**

* describe the difference between asking for code first and defining intent first

### Tuesday

**Concept Frame**

* purpose, boundaries, constraints, and structure before AI participation

**Demo / Guided Example**

* show a simplified RBA flow for a small Python project

**Hands-On Practice**

* frame a project idea before code generation

**Explain / Checkpoint**

* explain inputs, outputs, constraints, success criteria, and likely structure

### Thursday

**Concept Frame**

* capstone quality improves when development starts with clearer framing

**Demo / Guided Example**

* compare procedural, function-based, and light class-based structure choices for a project

**Hands-On Practice**

* begin capstone framing using simplified RBA ideas

**Explain / Checkpoint**

* justify the chosen project structure and what AI should or should not help with

### Topic Treatment

* **Core Manual:** project framing, decomposition, intent definition, success criteria, structure choice
* **Guided AI-Supported:** bounded project ideation and refinement after framing is complete
* **Recognition / Interpretation:** RBA as a distinct paradigm, top-down governance, reality contact, bounded upward revision when friction appears

---

## Week 8 Theme — Capstone Build, Justification, and Presentation

### Monday

**Concept Frame**

* project expectations: working program, understandable logic, accountable AI use, explainable decisions

**Demo / Guided Example**

* introduce or reinforce the AI use justification/explanation process

**Hands-On Practice**

* begin or continue capstone build under student-defined structure

**Explain / Checkpoint**

* identify what the student is trying to build and what AI is allowed to assist with

### Tuesday

**Concept Frame**

* AI can improve productivity and feature depth only if coherence is preserved

**Demo / Guided Example**

* show revision and refactoring as part of project strengthening

**Hands-On Practice**

* continue capstone implementation
* refactor for readability, coherence, and correctness

**Explain / Checkpoint**

* identify what was accepted, changed, rejected, and why

### Thursday

**Concept Frame**

* presentation is explanation, not just demonstration

**Demo / Guided Example**

* model how to explain code, choices, testing, and AI use clearly

**Hands-On Practice**

* present final project

**Explain / Checkpoint**

* explain core logic, design choices, debugging/testing process, AI use, and at least one revision caused by friction, testing, or reality contact

### Topic Treatment

* **Core Manual:** final code explanation, testing, debugging, user-facing demonstration, decision explanation
* **Guided AI-Supported:** polishing, refactoring, feature extension, structure cleanup, documentation support
* **Recognition / Interpretation:** more advanced patterns may appear if students can explain and justify them responsibly

---

# CLASS-BASED METHODOLOGY THREAD

This course remains procedural-first, but class-based methodology receives stronger treatment than a typical beginner Python course because students must increasingly interpret and govern AI-generated code that defaults to class-based organization.

### Students should be able to:

* recognize a simple class definition
* explain objects, attributes, and methods in plain language
* instantiate a simple class and call methods
* modify a small AI-generated class-based example
* compare a procedural approach with a class-based approach at a beginner level

### Students are not expected to master:

* deep inheritance hierarchies
* polymorphism as formal theory
* advanced magic methods
* framework-scale OOP design

---

# AI + RBA PROGRESSION

| Weeks | AI Role | RBA Role |
| ----- | ------- | -------- |
| 1-2 | AI is not a normal student lab tool | RBA not yet taught as a course method |
| 3-4 | limited comparison, explanation, and debugging support after manual work | indirect preparation through stronger framing and code explanation habits |
| 5-6 | bounded implementation support for files, data, and API work | bridge toward later RBA mini-unit through responsible AI use and validation |
| 7 | AI used only after explicit project framing | distinct compressed introduction to RBA as an emerging paradigm |
| 8 | strategic capstone acceleration under student control | bounded application of RBA to capstone framing, revision, and explanation |

---

# AI ACCOUNTABILITY EXPECTATION

Students should not merely use AI.

Students should be able to account for how they used AI.

This course should therefore support a brief justification/explanation artifact for projects or capstone work that captures:

* what the student was trying to build
* what AI was used for
* what the student accepted from AI output
* what the student changed or rejected
* how the student validated correctness
* what decisions remained human decisions

This artifact reinforces:

* authorship
* code comprehension
* anti-vibe-coding expectations
* explainability during capstone review

---

# WHY THIS DESIGN FITS THE COURSE

* It preserves the higher-level phase model for course consistency
* It gives each week a clear theme students can recognize
* It replaces lecture-heavy overload with repeatable session-level learning cycles
* It reduces early cognitive load by teaching only the smallest useful subset first
* It delays normal AI use long enough to build stronger manual habits
* It preserves RBA as a distinct, explicitly framed paradigm rather than a hidden assumption
* It uses RBA where it is most valuable in this course: improving project framing, capstone coherence, productivity, and feature quality

---

# MOST IMPORTANT OUTCOME

Students leave this course able to build and explain basic Python programs, use AI assistance with accountability rather than dependence, and apply a bounded introduction to RBA in order to frame, refine, and justify a stronger capstone project.

