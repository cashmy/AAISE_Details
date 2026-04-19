# UNIT / WEEK DESCRIPTIONS — Python Programming

---

# Purpose

This artifact translates the Instructional Intent Map into a more readable week-by-week teaching narrative.

It is intended to help with:

* instructor planning
* week-level course communication
* alignment between lecture framing, lab design, and assignments
* future assignment and slide development

This document preserves the current course structure:

* high-level phases
* weekly themes
* session-level pacing
* delayed and bounded AI use
* a compressed RBA mini-unit before final capstone work

---

# Phase 1 — Foundations + Manual Habits

## Week 1 — First Programs and Basic Values

Week 1 is designed to reduce fear, establish course expectations, and create the first feeling of success. Students should leave this week believing that Python is learnable and that they can make a program do something visible. The focus is intentionally narrow. Instead of treating "data types" as an encyclopedic category, the instruction emphasizes only the smallest useful subset needed to produce first working programs: strings, numbers, booleans, variables, input, output, and simple expressions.

The week should remain strongly manual-first. Students should spend more time writing, running, fixing, and explaining tiny programs than hearing about Python in the abstract. Setup and syntax friction should be normalized rather than dramatized. The instructional goal is not coverage of the textbook's full built-in type system. The goal is to help students understand that values move through a program and produce output.

By the end of the week, students should be able to write and explain very small programs that accept input, store values, and produce useful output. They should also understand that the course will build outward from this foundation gradually rather than all at once.

---

## Week 2 — Decision Logic and Repetition

Week 2 introduces the first real sense that programs can make choices and repeat behavior. This is where students begin moving from static scripts toward actual program logic. Conditionals and loops should be taught through small, concrete use cases rather than through abstract rule memorization. Students should repeatedly predict what code will do before running it, so that execution becomes something they can reason about rather than merely observe.

This week is also important for maintaining manual habits. Students should be tracing branches and loops directly, identifying why a condition passes or fails, and noticing how state changes affect repetition. The instruction should keep examples small enough that students can still explain them line by line. Confusion around loop stopping conditions, infinite loops, and misplaced condition checks should be treated as normal developmental milestones.

By the end of the week, students should be able to build small decision-driven and repetition-driven programs and explain why the logic behaves the way it does.

---

# Phase 2 — Structure + Code Literacy

## Week 3 — Organizing Code and Data

Week 3 shifts students from isolated logic into more intentional program structure. Functions, lists, and dictionaries are introduced not as abstract language features, but as tools that make programs easier to manage, extend, and understand. This is also the first week where limited AI comparison can appear, but only after students have created a manual baseline. That order matters because students need to see organization as something they can do, not something AI simply provides.

The week should emphasize naming logic, reducing repetition, and storing related data in practical forms. Functions should feel like containers for responsibility. Lists and dictionaries should feel like tools for managing information that a program needs to keep track of. The goal is not to maximize topic breadth. The goal is to help students feel that a program can be shaped and organized deliberately.

By the end of the week, students should be able to refactor small programs into functions, use simple collections to hold data, and compare a rougher version of code to a cleaner, better-organized version.

---

## Week 4 — Debugging, Testing, and Reading Structured Code

Week 4 develops code literacy. Students should learn that ownership of code includes the ability to inspect it, trace it, test it, and repair it. Debugging should be presented as normal engineering behavior rather than as evidence of failure. This is also the right point to give stronger treatment to class-based methodology, not because students need deep OOP mastery, but because they increasingly need to read, modify, and judge class-based code that AI often produces.

The week should compare different organizational styles in plain language: procedural, function-based, and simple class-based code. Students do not need formal OOP theory. They do need to recognize a class, understand what an object stores, understand what a method does, and modify a small example without freezing. AI support can appear here in a bounded way for debugging and explanation, but only after manual diagnosis is attempted first.

By the end of the week, students should be more comfortable reading unfamiliar code, identifying bug sources, testing expected vs actual behavior, and explaining the parts of a simple class-based example.

---

# Phase 3 — Data, Files, and Bounded AI Support

## Week 5 — Files, Errors, and Data Persistence

Week 5 connects programming to persistence and structured data. This is where students begin to see that programs are not limited to immediate input and output; they can store, retrieve, and work with information over time. File handling, basic CSV/JSON use, and beginner-friendly error handling make the course feel more practical and more real. Students should begin to feel that they are building tools rather than isolated exercises.

This week should also reinforce that real-world programming often includes messy inputs, missing files, bad data, and failure conditions. Error handling is not a side topic here. It is part of building programs that behave responsibly. AI use can be introduced in a more purposeful but still bounded way by comparing parsing strategies, revising error messages, or exploring alternate implementations after manual work has already begun.

By the end of the week, students should be able to build a small utility that saves and reloads information, explain how file and data handling work, and describe how their program behaves when something goes wrong.

---

## Week 6 — APIs, External Data, and Responsible AI Use

Week 6 expands the course outward again by introducing APIs and external data. This week is less about teaching networking in depth and more about giving students a practical sense that Python can connect to information beyond the local program. Endpoints, requests, responses, and JSON should be taught in a concrete, usable way. Students should see external data as structured, inspectable, and transformable rather than mysterious.

This is also the point where responsible AI use becomes more explicit. Tasks are complex enough now that AI can genuinely improve productivity, but the course still needs to preserve accountability. Students should compare manual API code with AI-assisted code, inspect response structures carefully, and explain what required human decisions. Tokens and authentication can be introduced at a recognition level, especially to help students recognize ideas they may see in examples or generated code, but without turning the week into an authentication unit.

By the end of the week, students should be able to retrieve and use simple external data, validate AI-assisted code rather than trusting it blindly, and explain the difference between help with implementation and responsibility for correctness.

---

# Phase 4 — RBA Mini-Unit + Capstone Application

## Week 7 — RBA and Project Framing

Week 7 introduces Refraction-Based Architecture as a distinct, bounded development paradigm rather than as the hidden method of the entire course. This matters because RBA is emerging, not yet a universal industry norm, and may differ from the expectations of more traditional shops. Students should understand that this week is about learning a real project-development framework used by the instructor, not about replacing Python fundamentals or claiming that all software teams work this way.

The instructional emphasis should be on intent-first and structure-first development. Students should see clearly how a weakly framed project start differs from a stronger one. They should practice defining purpose, inputs, outputs, constraints, success criteria, and likely structure before using AI for assistance. This is the bridge between earlier bounded AI use and final capstone application. It should feel practical, not overly theoretical.

By the end of the week, students should be able to frame a project more deliberately, justify an initial structural choice, and explain how clearer framing can improve project quality, features, and coherence.

---

## Week 8 — Capstone Build, Justification, and Presentation

Week 8 is where the course comes together. Students should use what they have learned about Python, debugging, structured development, bounded AI use, and RBA-informed project framing to complete and present a capstone. The goal is not merely to show a working artifact. The goal is to show a working artifact that the student can explain, justify, and defend.

The AI use justification process is especially important here. Students should not only demonstrate their code, but also articulate how AI was used, what was accepted, what was changed, what was rejected, how correctness was tested, and what decisions remained theirs. This supports authorship, anti-vibe-coding expectations, and a stronger evaluation of understanding.

By the end of the week, students should be able to present a coherent project, explain their logic and design choices, account for their AI use responsibly, and describe at least one revision that came from testing, friction, or reality contact.

---

# Final Throughline

Taken together, these weeks move students through a deliberate progression:

* first make Python feel approachable
* then build logic and structure
* then work with persistent and external data
* then introduce a bounded new project-development paradigm
* finally apply everything in a capstone that values both functionality and explainability

The most important outcome is not just that students can produce code.

It is that they can understand what they build, improve it, explain it, and use AI support without surrendering judgment.

