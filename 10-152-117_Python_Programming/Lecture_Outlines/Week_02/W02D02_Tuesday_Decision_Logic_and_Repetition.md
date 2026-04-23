# WEEK 2 DAY 2 LECTURE OUTLINE

**10-152-117 Python Programming**

---

# 1. Session Identity

* **Week / Day:** Week 2 / Tuesday
* **Date:** August 25, 2026
* **Weekly Theme:** Decision Logic and Repetition
* **Lecture Title:** Repetition with Control

---

# 2. Alignment Anchor

* **Assignments Supported:** A3 - Loops and Repetition
* **Readiness Target:** students can explain what repeats and what stops repetition
* **Primary Watch Point:** if repeated input is shown, make sure students understand state change clearly

---

# 3. Opening Frame (2-4 minutes)

Today adds repetition as a programming tool.

Key message:

* some instructions need to happen more than once
* programs can repeat on purpose
* repetition must still be controlled

Suggested wording:

> "If logic helps a program choose, loops help a program repeat. The real skill is understanding what repeats and what makes it stop."

---

# 4. Course Positioning (2-4 minutes)

Students now know:

* how to use variables
* how to print output
* how to make decisions with conditions

Today adds:

* repeated behavior
* `for` loops
* `while` loops
* stopping conditions

Suggested wording:

> "Yesterday your program learned how to choose. Today it learns how to do something again and again without you rewriting the same line every time."

---

# 5. Core Concepts (10-20 minutes)

## Concept 1 - A loop repeats an action

Plain-language explanation:

* loops let code run more than once
* the repeated behavior should be visible and intentional

Why it matters:

* Assignment 3 depends on students seeing repetition as controlled, not accidental

## Concept 2 - `for` loops repeat over a known range or collection

Plain-language explanation:

* `for` is useful when the number of repeats is already clear

Why it matters:

* this is often the easiest entry point for beginner repetition

## Concept 3 - `while` loops repeat while a condition remains true

Plain-language explanation:

* `while` depends on state changing
* if nothing changes, the loop may not stop

Why it matters:

* students must understand that the stopping condition is part of the design

## Concept 4 - State change controls stopping

Plain-language explanation:

* something must advance, update, or become false

Why it matters:

* this is the most common source of beginner loop confusion

---

# 6. Demo Plan (10-20 minutes)

## Demo 1

* **Artifact:** simple `for` loop counting demo
* **Focus:** visible repetition with a clear stop
* **Students should notice:** the loop runs a fixed number of times

## Demo 2

* **Artifact:** total accumulator or sequence demo
* **Focus:** repeated behavior changes a running value
* **Students should notice:** repetition often changes state each time through the loop

## Demo 3

* **Artifact:** `while` loop with stopping condition
* **Focus:** condition remains true until a value changes
* **Students should notice:** the update is what prevents infinite repetition

Instructional note:

* if repeated input is shown, narrate the update step very explicitly

---

# 7. Hands-On / Lab Bridge (10-20 minutes)

Students should try:

* a counting program
* a number sequence generator
* a repeated-input collector
* a simple total accumulator

Suggested wording:

> "Your goal today is not to write the biggest loop. Your goal is to write a loop where you can point to what repeats, what changes, and what makes it stop."

Do not require:

* heavy nested logic
* large menu systems
* multiple loop types in one assignment unless necessary

---

# 8. Common Mistakes / Watch-Fors (5-8 minutes)

## Mistake 1 - not understanding what repeats

Why it happens:

* students may recognize the loop syntax but not the repeated action

Correction:

* point directly to the repeated block and have students narrate it

## Mistake 2 - missing the update in a `while` loop

Why it happens:

* students focus on the condition and forget the changing value

Correction:

* ask: what becomes different after one loop cycle?

## Mistake 3 - stopping condition is vague or accidental

Why it happens:

* students may not design the stop intentionally

Correction:

* require them to identify the exact reason the loop ends

---

# 9. Explain / Checkpoint Questions (3-8 minutes)

Ask:

* What repeats in this loop?
* How many times will it run?
* What changes each time?
* What makes it stop?
* What would happen if this value never changed?

---

# 10. End-of-Class Success Check

> By the end of this session, students should be able to write a small loop, identify what repeats, explain what changes each time, and show what makes the loop stop.

---

# 11. Materials / Artifacts Used

* Week 2 loop demos
* A3 - Loops and Repetition
* [Lecture Content and Demo Alignment Matrix](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md)

