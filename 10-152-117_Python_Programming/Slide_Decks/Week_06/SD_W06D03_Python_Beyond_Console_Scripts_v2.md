# Slide Deck Source - Week 6 Day 3

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 6 / Thursday  
**Date:** September 24, 2026  
**Weekly Theme:** APIs, External Data, and Python App Architecture  
**Lecture Title:** Python Beyond Console Scripts  
**Assignments Supported:** A11 - API Data Fetcher; A12 - Python App Architecture Preview  
**Readiness Target:** Students can explain where input, validation, logic, and display live in a larger app flow.  
**Primary Watch Point:** Do not let the Django/MVT preview become a hidden framework requirement.

---

# Session Purpose

This session closes A11 and introduces A12 as a recognition-level architecture
preview.

Students should understand that Python is not limited to console scripts. The
same ideas they have used so far can appear inside larger application flows
where input, validation, logic, data, and display are separated.

This is not a Django build day.

---

# Review / Prior Work Bridge

Review from Day 2:

- API-style data must be inspected before values are selected.
- Live API and simulated JSON are both valid learning paths.
- AI-assisted code must be validated against the actual response structure.

Bridge question:

> If Python is part of a larger application, where do input, logic, data, and
> display live?

Today's answer:

> Larger apps separate responsibilities so each part has a clearer job.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 6
- Textbook area: **Introduction to API Development**

Today's focus:

- endpoints as recognition
- reading, creating, updating, and deleting data as concepts
- documenting an API as recognition
- project setup and configuration as recognition only
- larger app flow

Skim or save for later:

- database modeling
- authentication
- full endpoint implementation
- framework setup
- deployment

---

# What We Will Use Today

Today we will use:

- console script comparison
- input
- validation
- logic
- display
- MVT vocabulary as recognition
- template/form/view concepts

Today we will not use yet:

- installing Django
- building a web app
- implementing authentication
- database modeling
- deploying an application

---

# Assignments Supported

Assignments supported:

- A11 - API Data Fetcher
- A12 - Python App Architecture Preview

A11 closes around selected API-style output and explanation.

A12 asks students to inspect a guided architecture example and explain the flow
in plain language.

---

# Demo Set For The Session

Primary demos:

- `Demos/Week_06_APIs_External_Data_and_App_Architecture/06_architecture_preview_console_mvt.py`
- `Demos/Week_06_APIs_External_Data_and_App_Architecture/07_django_mvt_recognition.md`

Optional review:

- A11 success example
- `02_select_values_from_api_data.py`

Keep architecture recognition bounded.

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Move from API output to larger app flow |
| Working Set | 4-5 | Set framework-preview boundary |
| Core Architecture | 6-10 | Explain input, validation, logic, display, MVT |
| Demos | 11-12 | Show console-to-MVT and Django recognition |
| Assignment Bridge | 13-15 | Close A11 and launch A12 |
| Close | 16 | Define success as architecture explanation |

---

## Slide 1 - Python Can Live Beyond One Script

**Delivery Category:** Core

**Student-Visible Text:**

Python can run as a console script, but it can also be part of a larger
application.

The ideas are familiar. The responsibilities are separated more clearly.

**Instructor Notes:**

Frame this as expansion, not a sudden framework pivot.

**Transition Cue:**

Before looking beyond scripts, close the loop on what A11 required students to
explain.

---

## Slide 2 - Review: API Output Still Needs Explanation

**Delivery Category:** Review

**Student-Visible Text:**

For A11, the goal is not just to retrieve data.

The goal is to explain where the data came from, what shape it had, and which
values your program selected.

**Instructor Notes:**

Use this as an A11 closeout checkpoint before moving into A12.

**Transition Cue:**

Now shift from data path explanation to responsibility separation.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

- identify where input enters
- identify where validation or request handling happens
- identify where logic lives
- identify where output/display happens
- explain how a larger app separates responsibility

This is recognition first. You are not building a Django app today.

**Instructor Notes:**

Avoid shaming single-file programs. They are appropriate at this stage. The
success target is noticing how responsibilities separate as programs grow.

**Transition Cue:**

Now name the vocabulary students will use to describe that separation.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- input
- validation
- logic
- display
- template
- view
- model as recognition vocabulary

**Instructor Notes:**

This sets up MVT without requiring framework work.

**Transition Cue:**

Protect the scope before the framework vocabulary makes the lesson feel bigger
than it is.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- installing Django
- building a full web app
- databases
- authentication
- deployment

Today we inspect the shape of a larger app, not build one.

**Instructor Notes:**

Critical boundary slide.

**Transition Cue:**

With the boundary set, return to the main architecture idea: separating
responsibilities.

---

## Slide 6 - Larger Apps Separate Responsibilities

**Delivery Category:** Core

**Student-Visible Text:**

As programs grow, it becomes useful to separate responsibilities.

Different parts of the application can handle input, validation, data logic, and
display.

**Instructor Notes:**

This is the central architecture concept.

**Transition Cue:**

Start tracing the flow at the point where information enters the program.

---

## Slide 7 - Input Enters Through A Controlled Place

**Delivery Category:** Core

**Student-Visible Text:**

In a console script, input may come from `input()`.

In a larger app, input may come through a form, request, or controlled interface.

**Instructor Notes:**

Connect to forms without teaching form implementation.

**Transition Cue:**

After input enters, the program needs to check whether it can safely depend on
that input.

---

## Slide 8 - Validation Protects The Flow

**Delivery Category:** Core

**Student-Visible Text:**

Validation checks whether input is acceptable before the program depends on it.

This is the same idea as checking file data or API response data before using
it.

**Instructor Notes:**

This ties Week 4/5/6 together: evidence, checking, validation.

**Transition Cue:**

Now introduce MVT as one vocabulary system for talking about separated
responsibilities.

---

## Slide 9 - MVT As Recognition Vocabulary

**Delivery Category:** Core

**Student-Visible Text:**

MVT is one way to talk about separated responsibilities:

- Model: data shape and rules
- View: request handling and decisions
- Template: displayed result

Today you only need to recognize the flow.

**Instructor Notes:**

Keep it simple and accept imperfect beginner wording.

**Transition Cue:**

Compare that larger-app flow to the top-to-bottom console flow students already
know.

---

## Slide 10 - Console Flow Versus App Flow

**Delivery Category:** Core

**Student-Visible Text:**

A console script may run from top to bottom.

A larger app often responds to a request, validates input, runs logic, and then
returns a display.

**Instructor Notes:**

This prepares the architecture preview demo.

**Transition Cue:**

Now use the demo to label responsibilities instead of trying to build a
framework.

---

## Slide 11 - Demo 1: Console-To-MVT Preview

**Delivery Category:** Demo

**Student-Visible Text:**

Watch where each responsibility lives:

- input
- validation
- logic
- display

The code is a teaching model, not a framework requirement.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\06_architecture_preview_console_mvt.py`

Ask students to label responsibilities as you walk through the demo.

**Demo Connection:**

Primary demo file: `06_architecture_preview_console_mvt.py`

**Transition Cue:**

The console preview gives us a bridge. Now inspect the Django/MVT recognition
artifact without turning it into a build requirement.

---

## Slide 12 - Demo 2: Django MVT Recognition

**Delivery Category:** Demo

**Student-Visible Text:**

This is a recognition preview.

You should be able to point to the pieces and explain the flow, but you are not
expected to build a Django app in this course.

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_06_APIs_External_Data_and_App_Architecture\07_django_mvt_recognition.md`

Use `07_django_mvt_recognition.md` as an annotated reading/demo artifact.

**Demo Connection:**

Primary demo artifact: `07_django_mvt_recognition.md`

**Transition Cue:**

After seeing the larger structure, explicitly protect students from thinking
they are expected to implement all of it now.

---

## Slide 13 - Common Failure: Preview Becomes Panic

**Delivery Category:** Core

**Student-Visible Text:**

Seeing a larger structure does not mean you are behind.

Recognition comes before implementation. Today, naming the parts and explaining
the flow is the success target.

**Instructor Notes:**

Important confidence-preserving slide.

**Transition Cue:**

That recognition-level target becomes Assignment 12.

---

## Slide 14 - Assignment 12 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 12, inspect a guided Python app-architecture example.

Identify where input enters, where validation happens, where logic lives, and
where output is displayed.

**Instructor Notes:**

Keep A12 interpretive. If there is a guided edit, keep it small.

**Transition Cue:**

Close the week by separating A11 evidence from A12 evidence.

---

## Slide 15 - Evidence For A11 And A12

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

For A11, show selected API-style output and explain your data path.

For A12, explain the larger app flow in plain language and identify the main
parts.

Include an AI-use note if AI helped explain code or vocabulary.

**Instructor Notes:**

This closes Week 6 evidence expectations cleanly.

**Transition Cue:**

End with the sentence students should be able to say about any larger app flow.

---

## Slide 16 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> This part receives input, this part checks or handles it, this part runs the
> logic, and this part displays the result.

**Instructor Notes:**

Close on explanation. That is the architecture readiness target.

---

# Demo Execution Notes

Recommended order:

1. Review A11 output expectations.
2. Run or walk through `06_architecture_preview_console_mvt.py`.
3. Ask students to label input, validation, logic, and display.
4. Inspect `07_django_mvt_recognition.md`.
5. Emphasize recognition, not implementation.

---

# Lab / Assignment Bridge

A11 closeout:

- selected values
- readable output
- source/path explanation
- validation or fallback note

A12 launch:

- identify parts of guided example
- explain flow in plain language
- compare to console-only script

---

# README / Submission Expectations

For A12, a short markdown response may use:

```text
# Python App Architecture Preview

## Where input enters

## Where validation or request handling happens

## Where logic lives

## Where output/display happens

## How this differs from a console script

## AI-use note, if used
```

---

# AI-Use Boundary

AI may help explain unfamiliar architecture vocabulary.

Students must verify that the explanation matches the actual guided example and
must restate the flow in their own words.

AI should not turn A12 into a generic Django research report.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Beyond one script | Console script expands into larger app flow | Avoid web-dashboard look |
| 2 | A11 closeout | Data source, shape, selected values, explanation | Keep API review compact |
| 3 | Today's success pattern | Identify input, validation, logic, display, and separated responsibilities | Keep positive, not "bad code" |
| 4 | Working set | Input, validation, logic, display, template, view, model | Avoid framework overload |
| 5 | Saved for later | Django install, databases, auth, deployment parked | Avoid warning tone |
| 6 | Separated responsibilities | Larger app divides input, validation, logic, display | Avoid complex architecture |
| 7 | Controlled input | Console input compared with form/request input | Do not build UI mockup |
| 8 | Validation protects flow | Input checked before logic depends on it | Avoid security-heavy imagery |
| 9 | MVT recognition | Three labeled boxes: Model, View, Template | Avoid framework logo dependence |
| 10 | Console vs app flow | Top-to-bottom script compared with request-driven flow | Avoid full web app UI |
| 11 | Responsibility trace | Input, validation, logic, display highlighted in flow | No dense code |
| 12 | Django recognition | Point to parts, explain flow, no build requirement | Avoid Django branding dependence |
| 13 | Preview not panic | Recognition before implementation | Keep tone supportive |
| 14 | A12 bridge | Identify input, validation, logic, display in example | Keep response-focused |
| 15 | Evidence closeout | Two-column evidence: A11 data path, A12 app flow | Avoid compliance styling |

---

# Instructor Timing Notes

Suggested timing:

- A11 review and closeout: 10 minutes
- Architecture concept: 20 minutes
- Demos: 20 minutes
- A12 bridge: 10 minutes
- Student work / questions: remaining time

If students need A11 support, reduce Django recognition time and keep A12 as a
short guided response.

---

# Post-Lecture Notes

Use after teaching:

- Did MVT recognition remain bounded?
- Did students confuse view/template roles?
- Did A12 need more concrete examples?
- Was A11 complete enough before the architecture preview?
