# Lecture Deck Source Design Guide

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This artifact defines the approach for creating lecture deck source materials
for `10-152-119 Algorithmic Problem Solving`.

The goal is not to generate finished PowerPoint files directly.

The goal is to create high-quality deck source artifacts that can be converted
into instructor-designed slide decks with strong instructional sequence,
accurate content coverage, and clear links to demos, labs, readings, and
assessment expectations.

---

# Rationale

Finished AI-generated slide decks are often visually generic, shallow, or hard
to revise into an instructor's preferred teaching style.

For this course, the higher-value artifact is a structured slide source file
that includes:

- slide titles
- slide body text
- instructor notes
- optional visual or image notes
- demo cues
- lab bridge cues
- textbook review material
- misconception warnings
- timing and pacing guidance
- core, optional, and reserve teaching sections

This preserves the intellectual and pedagogical design while allowing the final
PowerPoint deck to be crafted visually by the instructor.

---

# Student-Facing Reading Framing

The lecture should not include language such as:

```text
If students did not complete the reading
```

That phrasing can unintentionally communicate that the reading is optional.

Instead, assigned readings should be handled through a student-facing section
such as:

```text
Textbook Review
Reading Review
Key Ideas from the Reading
```

This section should briefly summarize the assigned reading, reinforce key
terms, and identify the concepts that will be used in the live lecture.

The lecture may then teach those concepts in greater depth without announcing
that it is compensating for unread material.

---

# Math-Heavy Textbook Treatment

The textbook may present some algorithm topics with more mathematical notation
or theoretical depth than beginning developers need on first exposure.

Decks should not dismiss the math or imply that it is unimportant. Instead,
they should help students adopt the correct reading posture:

- skim first for the idea
- notice key terms
- mark unfamiliar formulas without panicking
- connect the topic back to code, functions, inputs, outputs, and evidence
- expect some concepts to become clearer after lecture, demo, and lab work

The course should repeatedly emphasize:

```text
When you write a function that takes input, follows steps, and returns a
result, you are already participating in algorithmic thinking.
```

Some topics may be included in the textbook because the author is giving a
fuller computer-science treatment. Examples such as P, NP, NP-Complete, and
NP-Hard have real relevance, but beginning developers do not need full mastery
of those topics to become competent at introductory algorithmic problem
solving.

When needed, decks should include a brief student-facing "How to use the
textbook" slide near the beginning of the lesson.

---

# Reading Reality

The course design should assume that some students may:

- complete the reading carefully
- skim the reading
- read but not fully understand the reading
- delay textbook purchase due to cost
- avoid mentioning that they do not have the textbook

The lecture should therefore preserve the textbook as an important resource
while still making the live instruction sufficient for core concept access.

The reading becomes:

- preparation for students who read ahead
- reinforcement for students who read after class
- an alternate explanation for students who need another pass
- a future reference source after the course

---

# Slide Count and Pacing

The course has a guided standard of approximately `50%` lecture time, which can
allow up to about `3` hours of lecture per week in an 8-week course.

In practice, long contiguous lecture blocks are cognitively difficult for many
adult learners.

The deck source should therefore support flexible delivery:

- enough content to cover the required concepts
- enough structure to pause, skip, or reserve sections
- enough repetition to support beginners
- enough examples to avoid abstraction overload
- enough breaks and checks for understanding to preserve attention

The goal is not to minimize slide count.

The goal is to ensure that each slide has one clear instructional job.

---

# Section Types

Each deck source may divide content into the following delivery categories.

## Core

Core slides should be taught live unless time or class conditions require a
major adjustment.

Core material includes:

- course-critical concepts
- required vocabulary
- examples needed for the demo
- concepts needed for the lab
- common misconceptions that must be corrected

## Optional Deepening

Optional deepening slides expand or reinforce the core material.

Use these when:

- students are ready for more detail
- questions reveal that the class needs more explanation
- the topic is especially dense
- time allows deeper treatment

## Instructor Reserve

Instructor reserve slides are available for reteaching, enrichment, or future
reuse.

These slides may not be shown every time the course runs.

They can support:

- stronger student groups
- additional examples
- alternate explanations
- extra visual models
- questions that arise during class

---

# Multiple Topic Blocks

Most lectures in this course will cover multiple related topics.

Examples:

- Big-O includes growth intuition, notation, common classes, input size,
  constants, nested loops, and comparison limits.
- Data structures include lists, dictionaries, sets, stacks, queues, trees,
  graphs, and selection tradeoffs.
- Search and sort include direct search, binary search, comparison sorting,
  correctness, stability, and tradeoff reasoning.

Deck source artifacts should therefore avoid treating the lecture as one flat
topic.

Instead, each lecture should contain multiple topic blocks.

Each topic block should include:

- topic purpose
- key terms
- student-facing explanation
- instructor notes
- example or visual cue
- connection to demo, lab, or assessment
- misconception warning when appropriate

---

# Recommended Deck Flow

Most lectures should follow this general pattern, adapted as needed:

1. Opening review and bridge from the previous week
2. Textbook Review
3. Lesson outcomes
4. Topic Block 1
5. Check for understanding
6. Topic Block 2
7. Worked example or representation bridge
8. Topic Block 3, if needed
9. Demo setup
10. Demo walkthrough
11. Lab bridge
12. Wrap-up and next-step cue

The exact number of topic blocks should follow the content, not an artificial
template requirement.

---

# Representation Bridge

Algorithms should be shown in multiple forms whenever useful:

- plain English
- formal or semi-formal algorithm description
- pseudocode
- Python code
- table or trace
- visual diagram

This is especially important for beginners who may believe that an algorithm is
only a mathematical formula or only Python code.

The lecture should repeatedly show that an algorithm is a structured procedure
for solving a problem, and that the same idea can be represented in different
forms.

---

# Demo and Lab Bridge

Each deck source should identify how lecture content maps into the instructor
demo and student lab.

The demo should not be identical to the lab.

The demo should be close enough that students can transfer the concept, but
different enough that they must think rather than copy.

Recommended pattern:

```text
lecture concept
-> instructor demo with near-transfer scenario
-> student lab with related but different scenario
-> README evidence and explanation
```

---

# Optional Visual or Image Notes

Deck source artifacts may include optional visual notes rather than finished
images.

Useful visual notes include:

- diagram concept
- table concept
- comparison layout
- suggested icon or metaphor
- image-generation prompt draft
- warning that a visual should be instructor-created rather than AI-generated

Visual notes should support learning, not decorate the deck.

---

# Tone and Student Experience

Slides should be clear, direct, and student-facing.

Avoid:

- scolding language
- dense textbook-style paragraphs
- unnecessary formalism before students understand the purpose
- unsupported abstraction
- implying that reading is optional

Prefer:

- concrete examples
- visible reasoning
- short definitions followed by use
- repeated translation between representations
- questions that invite explanation
- bridges from prior knowledge to new concepts

---

# Instructor Notes Standard

Instructor notes and transition cues should be readable after time has passed.

Avoid notes that only function as memory hooks while the design session is
fresh. A future instructor, or the same instructor after a weekend away, should
be able to understand the intended teaching move without reconstructing hidden
context.

Instructor notes should usually include:

- what to say or demonstrate
- why the teaching move matters
- what student misconception or confusion it addresses
- what example should be used, when an example is mentioned
- what "it," "this," or "that" refers to when ambiguity is possible

Compressed note:

```text
Use a bad example. Ask why it is hard to follow.
```

Preferred note:

```text
Use the weak instruction "Pick the best option." Ask students why that
instruction is hard for another person to follow. The issue is that "best" is
undefined; it could mean cheapest, fastest, healthiest, or most convenient.
Connect this back to precision and testability.
```

Transition cues should also be explicit enough to preserve the instructional
logic between slides.

---

# Relationship to Existing Lecture Outlines

The existing lecture outlines remain the instructional planning layer.

The deck source artifacts are a second layer:

```text
Lecture Outline
-> Lecture Deck Source
-> Instructor-Crafted PowerPoint
-> Live Lecture / Demo / Lab Bridge
```

This separation prevents the lecture outline from becoming overcrowded while
still preserving a PowerPoint-ready instructional sequence.

---

# Future Use

This guide may also be adapted for other courses in the Bridge pathway.

The specific content belongs to `10-152-119`, but the deck-source approach can
generalize to:

- Python Programming
- HTML/CSS/JavaScript
- Advanced Python
- AI or data-focused future courses

The reusable idea is that slide construction should be artifact-driven, not
tool-driven.
