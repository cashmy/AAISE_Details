# Python Programming High-Level Course Plan v1

## Course

`10-152-117` - `Python Programming`

Credits: `2`  
Lecture/Lab: `18/36`  
Prerequisite: `n/a`

## Source Description

Learners explore Python programming by designing and implementing solutions to
small, practical problems. Students develop foundational programming skills using
variables, data types, conditionals, loops, functions, lists, dictionaries, file
input/output, structured data, and introductory API work. The course emphasizes
problem-solving, debugging, code comprehension, and clear explanation while
introducing AI-assisted development in a bounded, accountable way. By the end of
the course, students are able to create, understand, debug, refine, and explain
basic Python programs both independently and with appropriate AI assistance.

## Planning Position

This course should function as the bridge sequence's first programming
foundation. It is where students begin moving from uncertain beginners toward
capable novice programmers who can make code run, reason about what it does,
repair it when it fails, and explain their work clearly.

The course should prioritize confidence, manual capability, and code ownership
over broad language coverage. Students do not need an encyclopedic introduction
to every Python feature. They need repeated practice with the core structures
that let them solve small problems:

```text
values       -> variables, types, expressions, input, and output
choices      -> comparisons, booleans, conditionals
repetition   -> loops, stopping conditions, repeated input
organization -> functions, responsibility, readable structure
data         -> lists, dictionaries, files, CSV/JSON, API responses
ownership    -> tracing, testing, debugging, explanation
AI support   -> prompting, inspection, adaptation, validation, disclosure
```

The course should remain Python-first. AI-assisted development is important, but
it should be introduced as a support for learning and production, not as a
replacement for basic program understanding. The strongest course identity is:

```text
manual habits first -> bounded AI comparison and debugging -> accountable
AI-assisted project work
```

Refraction-Based Architecture should appear as a compact late-course mini-unit
to improve capstone framing, scope control, AI-use boundaries, and explanation.
It should not be treated as the hidden operating system of the whole course.

## Delivery Frame

This is an 8-week, 2-credit course with `18` lecture hours and `36` lab hours.
The compressed format requires frequent visible wins, repeated patterns, and
short feedback loops.

The stable weekly rhythm is:

```text
concept frame -> demo / guided example -> hands-on practice -> explain /
checkpoint
```

The plan assumes three course meetings per week:

- concept and framing
- guided build or code walkthrough
- lab, challenge, debugging, explanation, or checkpoint

Individual sessions should still contain a complete learning cycle rather than
separating all lecture from all practice.

## Relationship to Concurrent and Later Courses

This course is part of the first semester bridge foundation alongside:

- `10-152-118 HTML/CSS/JavaScript`
- `10-152-119 Introduction to Algorithms`

Its primary role is to build logic, confidence, and code ownership. The
HTML/CSS/JavaScript course gives students early experience making software
visible and interactive in the browser, while the algorithms course later
refines students' approach selection, reasoning, and efficiency awareness.

This course should prepare students for `10-152-119` by establishing:

- step-by-step problem decomposition
- input, output, and constraint awareness
- branch and loop tracing
- debugging and expected-versus-actual reasoning
- explanation of why a solution works

It should prepare students for `10-152-121 Advanced Python Systems` by
establishing a compressed but meaningful base in:

- variables, expressions, input/output, decisions, loops, functions, lists, and
  dictionaries
- simple debugging, testing, and code explanation
- recognition-level procedural, function-based, and class-based code reading
- file persistence, text files, CSV, JSON, and basic error handling
- introductory API endpoints, requests, responses, and JSON parsing
- recognition-level Python application architecture, including Django MVT,
  templates, and forms
- RBA project framing, AI-use boundaries, capstone build, and final explanation

Later courses should treat these topics as first exposure already completed, but
not yet fully durable. The expectation is transfer and strengthening, not
mastery.

## High-Level Time Allocation

Suggested emphasis:

```text
25% basic Python syntax, values, input/output, decisions, and loops
20% functions, collections, program organization, and code readability
15% debugging, testing, tracing, explanation, and code literacy
15% files, structured data, error handling, APIs, and external data
10% recognition-level architecture, class-based code, Django/MVT, and data
    representation previews
10% bounded AI-assisted development, validation, adaptation, and disclosure
5% RBA project framing and capstone preparation
```

## 8-Week Draft Structure

The course is organized into four two-week phases:

```text
Weeks 1-2 -> Foundations + Manual Habits
Weeks 3-4 -> Structure + Code Literacy
Weeks 5-6 -> Data, Files, and Bounded AI Support
Weeks 7-8 -> RBA Mini-Unit + Capstone Application
```

### Week 1 - First Programs and Basic Values

Purpose: reduce fear, establish course expectations, and create the first
feeling of programming success.

Topics:

- What programming is and what a Python program does
- Running small scripts
- Strings, numbers, booleans, variables, and simple expressions
- `print()`, input, output, and value movement
- Setup and syntax mistakes as normal learning events

Lab direction:

- Build very small greeting, calculator, converter, or message programs
- Trace values from input to output
- Explain what each line does
- Keep AI out of normal student lab work except as instructor demonstration if
  needed

### Week 2 - Decision Logic and Repetition

Purpose: help students understand that programs can choose paths and repeat
behavior.

Topics:

- Booleans, comparisons, and conditions
- `if`, `elif`, and `else`
- `for` and `while` loops
- Stopping conditions and repeated input
- Predicting behavior before running code

Lab direction:

- Build decision-based programs such as grading, eligibility, discount, or
  recommendation tools
- Build repetition-based programs such as counters, input collectors, or
  loop-driven menus
- Debug missing updates, incorrect conditions, and infinite-loop behavior
- Maintain manual-first work habits

### Week 3 - Organizing Code and Data

Purpose: move students from isolated code fragments toward intentional program
structure.

Topics:

- Functions as named responsibility
- Parameters, return values, and repeated logic
- Lists and dictionaries as practical storage tools
- Iteration over collections
- Comparing rough code with cleaner organized code

Lab direction:

- Refactor earlier programs into functions
- Build small trackers, menus, lookup tools, or collection-based mini-apps
- Explain what each function or data structure is responsible for
- Compare a manual baseline with a limited AI-generated variation only after the
  student solution exists

### Week 4 - Debugging, Testing, and Reading Structured Code

Purpose: develop code literacy and reinforce that ownership includes inspection,
repair, testing, and explanation.

Topics:

- Debugging as normal engineering practice
- Tracing values and using simple diagnostic output
- Expected-versus-actual testing
- Reading procedural, function-based, and simple class-based code
- Classes, objects, attributes, methods, and `__init__` at a recognition level

Lab direction:

- Repair intentionally broken examples
- Create or apply simple test cases
- Compare manual and AI-assisted fixes after manual diagnosis
- Inspect and lightly modify a simple class-based example
- Justify why a chosen fix works

### Week 5 - Files, Errors, and Data Persistence

Purpose: show that programs can store, retrieve, and work with information over
time.

Topics:

- File input/output
- Text files, CSV, JSON, and simple structured data
- Basic `try` / `except` error handling
- Success and failure paths
- Recognition-level transition from flat files toward data models and larger
  application data structures

Lab direction:

- Build a small save/load utility
- Read structured data and produce useful filtered or summarized output
- Explain where information is stored and how it returns to the program
- Compare simple data representations such as text, CSV, JSON, and model-shaped
  data
- Use AI in bounded ways for explanation, parsing comparison, or error-message
  revision

### Week 6 - APIs, External Data, and Python App Architecture

Purpose: expand Python from local scripts toward external data and larger
application contexts.

Topics:

- Sequential versus asynchronous thinking at a recognition level
- APIs, endpoints, requests, responses, HTTP/REST vocabulary, and JSON responses
- Inspecting response structures and selecting useful values
- Introductory recognition of tokens, auth headers, and rate limits
- Python web-app architecture preview, including Django MVT, templates, forms,
  and views

Lab direction:

- Retrieve and use simple external data from an approved API or controlled
  endpoint
- Compare manual request code with bounded AI-assisted code
- Parse selected values from JSON
- Inspect a simple web-app flow or complete a guided edit
- Explain what AI helped with and what still required human judgment

### Week 7 - RBA and Project Framing

Purpose: introduce RBA as a bounded development framework for project definition,
scope control, AI-use boundaries, and capstone readiness.

Topics:

- Intent-first and structure-first project framing
- Purpose, inputs, outputs, constraints, success criteria, and risks
- Project structure choices: console, data-driven, API-based, light UI, or
  architecture-preview paths
- AI-use boundaries before implementation
- Bounded upward revision when project structure begins to drift

Lab direction:

- Compare weak prompting-first starts with stronger project framing
- Draft and revise project framing sheets
- Define likely project structure and AI boundaries
- Submit a capstone proposal for approval
- Justify why the chosen scope is realistic and explainable

### Week 8 - Capstone Build, Justification, and Presentation

Purpose: integrate Python fundamentals, debugging, structured development,
bounded AI use, and project explanation.

Topics:

- Capstone implementation under an approved project frame
- Readability, correctness, testing, and revision
- AI-assisted feature extension or refactoring with accountability
- Final demonstration and explanation
- AI-use justification and authorship

Lab direction:

- Build and refine the approved capstone project
- Test the program using sample inputs or scenarios
- Explain core logic and design choices
- Identify what AI output was accepted, changed, or rejected
- Present the final project and account for at least one revision caused by
  testing, friction, or reality contact

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Analyze small programming problems by identifying inputs, outputs,
  constraints, and step-by-step logic.
- Write basic Python programs using variables, expressions, conditionals, loops,
  functions, lists, dictionaries, and file input/output.
- Read and explain program behavior using clear, beginner-appropriate language.
- Debug syntax and logic errors using tracing, testing, and expected-vs-actual
  reasoning.
- Use simple structured data from files or API responses in Python programs.
- Recognize simple class-based code and larger Python application structures
  without needing deep framework mastery.
- Use AI-assisted tools in bounded ways to compare, explain, refine, or extend
  code while retaining responsibility for correctness.
- Frame, build, present, and justify a small capstone project.
- Explain how AI was used, what was changed or rejected, how correctness was
  validated, and which decisions remained human decisions.

## Notes for Future Detailed Design

- Preserve this course as a confidence-building programming foundation. Avoid
  allowing AI, RBA, APIs, Django, or class-based methodology to crowd out core
  Python practice.
- Keep early assignments small, manual, and winnable. The first two weeks should
  build belief, not just coverage.
- Treat the current assignment ladder as the detailed implementation source:
  short targeted builds first, integration primarily in the capstone.
- Maintain the distinction between AI as a tool and AI as a substitute for
  understanding. Students should account for AI use, not merely disclose it.
- Keep RBA late, bounded, and project-facing. It should improve capstone quality
  and scope control without turning the whole course into a theory course.
- Use architecture previews sparingly. Students should recognize class-based
  code, data models, APIs, and Django-style application flow, but Advanced Python
  Systems should be responsible for deeper implementation.
- Coordinate with `10-152-118` and `10-152-119` so students encounter a coherent
  first-semester pattern: build simple things, make them visible, debug them,
  reason about them, and explain them.
- Coordinate with `10-152-121` so that Advanced Python Systems can build forward
  from this course rather than reteach it as first exposure.
