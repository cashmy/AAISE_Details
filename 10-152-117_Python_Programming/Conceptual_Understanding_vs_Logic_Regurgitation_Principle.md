# Conceptual Understanding vs Logic Regurgitation Principle

**Course:** `10-152-117 Python Programming`

---

# Purpose

This artifact preserves a course-level instructional principle for future AI
sessions, assignment refinement, demo generation, rubric updates, and slide-deck
development.

It clarifies that this course prioritizes accurate conceptual understanding,
code ownership, and explanation over memorized reproduction of precise logic.

This does not remove the need for students to write, trace, test, or debug code.
It reframes what durable competence means in an AI-assisted development
environment.

---

# Core Principle

The course should concentrate more on whether students understand the concepts
than on whether they can independently regurgitate precise implementation logic
from memory.

AI-assisted development drastically changes the instructional target:

```text
old center of gravity:
manual recall of exact syntax and logic patterns

new center of gravity:
accurate concept awareness, explanation, validation, and judgment
```

Students still need enough manual ability to reason about code, but the deeper
goal is not instinctive memorization of every implementation pattern.

The deeper goal is that students can understand what kind of problem they are
solving, recognize the relevant programming concept, inspect a proposed
solution, and determine whether it fits.

---

# Why This Matters

In a non-AI programming course, students often had to internalize exact logic
patterns because they had no practical support system available during
development.

In an AI-assisted development environment, that changes.

AI can often help correct poor syntax or weak implementation logic if the
student understands the underlying concept well enough to:

- describe the intended behavior
- identify relevant inputs and outputs
- recognize which concept applies
- inspect whether the code matches the intent
- test expected and actual behavior
- ask a useful follow-up question
- reject or revise an unsuitable suggestion

If the concept is sound, AI debugging can help repair the implementation.

If the concept is unsound, AI may simply produce a more polished version of the
wrong idea.

---

# What Students Still Need to Know Manually

This principle does not mean students can skip basic programming practice.

Students still need enough manual fluency to:

- write small programs
- trace values through code
- recognize variables, conditionals, loops, functions, lists, dictionaries,
  files, and JSON structures
- identify where a program makes a decision or repeats behavior
- read error messages at a beginner level
- run simple tests
- explain what a block of code is trying to do

Manual ability remains necessary because students cannot govern AI output they
cannot read.

---

# What Should Not Be Overemphasized

The course should avoid overvaluing:

- memorized syntax recall as the main evidence of learning
- exact reproduction of a previously shown algorithm
- hidden-test style trick logic
- speed of manual coding as proof of understanding
- punishment for needing support on syntax details
- assessment that rewards only students who can already think like experienced
  programmers

These can create false signals. A student may memorize a pattern without
understanding it, or may struggle to recall exact syntax while still having a
sound conceptual model.

---

# Better Evidence of Learning

Stronger evidence includes whether a student can:

- explain what problem the code solves
- identify the inputs, outputs, and constraints
- choose the relevant concept family
- predict what the code should do
- trace key values or decisions
- explain why a loop stops
- explain why a condition passes or fails
- describe what a function is responsible for
- identify where data is stored or retrieved
- test the program with meaningful examples
- compare expected and actual behavior
- describe what AI helped with
- identify what they accepted, changed, or rejected
- explain why the final result fits the requirement

---

# Assessment Implication

Assignments, demos, rubrics, and capstone questioning should prioritize:

- concept identification
- explanation
- testing and validation
- debugging process
- accountable AI use
- fit between problem, structure, and implementation

They should still require working code when code is the expected deliverable,
but working code alone is not the whole target.

The best assessment question is often not:

> Can you write this exact logic from memory?

but:

> Can you explain what this logic is supposed to do, verify that it does it, and
> make a responsible change when the requirement shifts?

---

# AI-Assisted Development Implication

AI should be treated as a correction, comparison, explanation, and acceleration
tool after the student has enough conceptual footing to govern it.

Appropriate AI use may include:

- explaining unfamiliar syntax
- suggesting a corrected loop
- comparing two versions of a function
- helping interpret an error message
- producing a first draft after the student has framed the problem
- suggesting test cases
- refactoring for readability

AI use becomes problematic when it replaces:

- problem framing
- concept identification
- reading the code
- testing the result
- explaining the behavior
- making human decisions

---

# Instructor Guidance

When a student struggles, the most important first question is often:

> Do they misunderstand the concept, or are they struggling with implementation
> mechanics?

If the concept is weak:

- return to examples
- ask for inputs and outputs
- ask what should happen step by step
- ask what concept applies
- use smaller code
- delay AI until the frame is clearer

If the concept is sound but implementation is weak:

- allow targeted debugging help
- use AI as an explainer or repair assistant when allowed
- ask the student to test and explain the revised version
- focus on ownership of the corrected result

---

# Future AI Session Guidance

When future AI sessions generate Python materials for this course, they should
preserve this principle.

Do:

- design assignments around concept ownership and explanation
- include demo/lab transfer rather than identical copying
- ask students to explain behavior and validate results
- allow AI support only at the appropriate course stage
- distinguish concept misunderstanding from implementation weakness
- preserve beginner confidence while maintaining accountability

Do not:

- turn assignments into memorization tests
- overemphasize exact syntax recall
- generate unnecessarily tricky programming challenges
- assume that manual coding speed equals understanding
- remove working-code expectations entirely
- allow AI to replace student explanation or validation

---

# Relationship to Existing Course Artifacts

This principle supports and sharpens:

- `TD_Teaching_Doctring.md`
- `Python_AI_Use_Addendum.md`
- `AI_Use_Justification_Guide.md`
- `LS_Lab_System.md`
- `MRS-Py_Master_Rubric_System.md`
- `Assignments/LDP-Py_Lab_Demo_Prompt_Pack.md`

It should be referenced when refining:

- assignments
- demos
- starter files
- successful versions
- lecture outlines
- slide decks
- rubric language
- capstone questioning

---

# Final Statement

For this course, the student target is not:

> I can reproduce every Python logic pattern from memory.

The student target is:

> I understand the concept well enough to build with support, inspect the code,
> debug the result, explain the behavior, and remain responsible for the final
> program.
