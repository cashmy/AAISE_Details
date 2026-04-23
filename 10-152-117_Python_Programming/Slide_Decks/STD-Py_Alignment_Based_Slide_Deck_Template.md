# SLIDE DECK TEMPLATE - PYTHON (ALIGNMENT-BASED)

**10-152-117 Python Programming**

---

# Purpose

This template is the slide-deck generation layer for the Python course.

It is designed to sit after:

* the Instructional Intent Map
* the Assignment Week-Day Matrix
* the Lecture Content and Demo Alignment Matrix
* the day-specific lecture outline

Its job is to turn the lecture outline into a slide-deck `.md` artifact that supports lecture delivery without turning slides into a transcript.

---

# Core Principle

Slides are **visual anchors**, not content containers.

The lecture outline carries the detailed teaching logic.

The slide deck should carry:

* the memorable anchor line
* the instructor cue
* the visual intent

---

# Python Course-Specific Rule

Every slide deck should preserve the session micro-arc in visible form:

1. Opening Frame
2. Core Idea(s)
3. Demo / Guided Example
4. Common Failure or Thinking Tool
5. Hands-On Bridge
6. Closing Success Check

If a deck loses that structure, it is drifting away from the course design.

---

# Required Source Inputs

Before drafting a slide deck, confirm these inputs from the lecture outline:

* session identity
* assignments supported
* readiness target
* primary watch point
* 3-5 core concepts maximum
* selected demos
* hands-on / lab bridge
* common mistakes or confusion patterns
* end-of-class success check

If these are not clear, the deck should not be drafted yet.

---

# Standard Deck Header

Use this header at the top of each slide-deck artifact:

```text
# SLIDE DECK - WEEK X DAY Y

* Course:
* Week / Day:
* Date:
* Weekly Theme:
* Lecture Title:
* Assignments Supported:
* Readiness Target:
* Primary Watch Point:
```

---

# Recommended Deck Size

* Target: `7-9` slides
* Soft maximum: `10` slides

If the deck grows beyond that, reduce content rather than adding more slides.

The lecture outline should hold the detail.

The deck should hold the anchor points.

---

# Recommended Flow

## Slide 1 - Opening Frame

Purpose:

* establish the day's direction
* reduce anxiety
* frame the lesson clearly

## Slide 2 - Course Positioning

Purpose:

* connect today to what students already know
* show what new capability is being added

## Slide 3 - Core Idea 1

Purpose:

* anchor the first major concept

## Slide 4 - Core Idea 2 or System

Purpose:

* add the second essential concept
* show relationship when needed

## Slide 5 - Demo Anchor

Purpose:

* make the concept visible
* direct attention during the demonstration

## Slide 6 - Common Failure or Thinking Tool

Purpose:

* preempt predictable mistakes
* install a reasoning heuristic

## Slide 7 - Hands-On Bridge

Purpose:

* direct student action
* clarify what the assignment/lab goal is today

## Slide 8 - Closing Success Check

Purpose:

* reinforce what success looks like
* connect directly to readiness target

Optional:

* a ninth slide may be used when the lecture has a second essential failure pattern or a needed contrast slide

---

# Slide Spec Format

Use this exact structure for each slide:

```text
### SLIDE X - [TYPE]

[Primary Line]
[Optional second line]

---
Cue:
- (delivery guidance)
- (emphasis, pacing, framing)

Visual:
- Layout:
- Content:
  - (element 1)
  - (element 2)
- Purpose:
  - (what this reveals)
```

---

# Allowed Slide Types

Use a limited slide vocabulary:

* OPENING FRAME
* COURSE POSITIONING
* CORE IDEA
* SYSTEM
* CONTRAST
* DEMO ANCHOR
* COMMON FAILURE
* THINKING TOOL
* BRIDGE
* CLOSING

Do not invent many custom types unless there is a strong reason.

---

# Text Rules

* maximum `2` lines per slide
* target `3-8` words per line
* hard maximum `10` words per line
* simple declarative language
* no paragraphs
* no bullet lists on the student-facing slide text

The detail belongs in:

* Cue
* Visual
* lecture delivery

---

# Alignment Rules for This Course

## 1. Readiness Target Rule

Every deck must visibly support one readiness target.

If a slide cannot be connected to that target, cut it.

## 2. Watch Point Rule

At least one slide should help prevent the day's primary watch point.

Examples:

* `input()` overload
* hidden pytest requirement drift
* live API instability
* accidental Django overreach
* vague RBA abstraction

## 3. Assignment Support Rule

At least one slide must explicitly bridge to what students are expected to do in the assignment or lab.

## 4. Demo Support Rule

If the lecture outline names a demo, the deck should contain a demo anchor slide that tells students what to notice during the demo.

---

# Deck Drafting Workflow

## Step 1

Read the day-specific lecture outline.

## Step 2

Extract:

* opening frame
* course positioning statement
* 2-3 essential concept anchors
* 1 demo emphasis point
* 1 common failure or heuristic
* 1 hands-on bridge
* 1 success definition

## Step 3

Convert each of those into minimal slide language.

## Step 4

Write the cue and visual intent for each slide.

## Step 5

Check the deck against the readiness target and watch point.

---

# Quality Check

Before using a deck, ask:

* Does each slide support the readiness target?
* Is the deck aligned to the lecture outline rather than competing with it?
* Is there a clear demo anchor?
* Is there a clear hands-on bridge?
* Is at least one likely failure pattern addressed?
* Is the closing slide tied to what students should be able to do?

---

# Important Distinction

The lecture outline is the **teaching logic artifact**.

The slide deck is the **delivery support artifact**.

Do not merge them into one thing.

If a deck starts carrying all the explanation, it has drifted.

