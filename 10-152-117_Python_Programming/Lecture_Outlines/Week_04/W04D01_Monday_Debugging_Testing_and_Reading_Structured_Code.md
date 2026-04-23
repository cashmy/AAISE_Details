# WEEK 4 DAY 1 LECTURE OUTLINE

**10-152-117 Python Programming**

---

# 1. Session Identity

* **Week / Day:** Week 4 / Monday
* **Date:** September 7, 2026
* **Weekly Theme:** Debugging, Testing, and Reading Structured Code
* **Lecture Title:** Debugging as Evidence Gathering

---

# 2. Alignment Anchor

* **Assignments Supported:** A6 - Debug and Explain
* **Readiness Target:** students can identify bug source evidence rather than only symptoms
* **Primary Watch Point:** print-debugging must be taught as intentional evidence, not random `print("here")` behavior

---

# 3. Opening Frame (2-4 minutes)

Today reframes debugging as normal engineering work.

Key message:

* bugs are not proof that a student is bad at programming
* debugging is a process of gathering signal from the code
* changing random lines is not the same as diagnosing a problem

Suggested wording:

> "A bug is not a verdict. A bug is information. The real skill is learning how to read that information before changing the code."

---

# 4. Course Positioning (2-4 minutes)

Students now know:

* how to write small structured programs
* how to use functions and collections

Today adds:

* print-debugging
* expected vs actual reasoning
* syntax bug versus logic bug thinking

Suggested wording:

> "So far, we have been focused on building. Today we begin strengthening code ownership by learning how to inspect, trace, and fix what goes wrong."

---

# 5. Core Concepts (10-20 minutes)

## Concept 1 - A bug has a source and a symptom

Plain-language explanation:

* the visible wrong behavior is often not the exact place where the problem started

Why it matters:

* students must learn to search for source, not only react to symptoms

## Concept 2 - Expected vs actual is a debugging tool

Plain-language explanation:

* students should compare what should happen to what did happen

Why it matters:

* this creates evidence instead of guesswork

## Concept 3 - Print-debugging can reveal value flow

Plain-language explanation:

* labeled print statements help locate where a value becomes wrong

Why it matters:

* Assignment 6 now explicitly allows debugging evidence such as labeled print output

## Concept 4 - Syntax and logic bugs are different

Plain-language explanation:

* syntax bugs stop the program
* logic bugs let the program run but produce the wrong result

Why it matters:

* students need to learn different debugging postures for different bug types

---

# 6. Demo Plan (10-20 minutes)

## Demo 1

* **Artifact:** broken syntax example
* **Focus:** read the error and identify the location
* **Students should notice:** Python gives useful clues when syntax breaks

## Demo 2

* **Artifact:** logic bug expected-vs-actual example
* **Focus:** wrong output even though the code runs
* **Students should notice:** running code can still be incorrect

## Demo 3

* **Artifact:** print-debugging discovery demos
* **Focus:** add evidence to locate where values drift
* **Students should notice:** labeled print statements expose the first meaningful signal

Instructional note:

* use [Instructor Notes - The Debugging Process](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Debugging_Process.md) as framing support

---

# 7. Hands-On / Lab Bridge (10-20 minutes)

Students should try:

* tracing a broken example
* comparing expected vs actual output
* adding one or two intentional labeled debug prints

Suggested wording:

> "Your goal today is not to fix bugs by luck. Your goal is to gather enough evidence that the fix becomes justified."

Do not require yet:

* elaborate testing frameworks
* large codebases
* advanced debugger tooling

---

# 8. Common Mistakes / Watch-Fors (5-8 minutes)

## Mistake 1 - changing code before understanding the failure

Why it happens:

* students feel pressure to fix things quickly

Correction:

* slow them down and require expected-vs-actual language first

## Mistake 2 - print statements without purpose

Why it happens:

* students may treat print-debugging as noise rather than evidence

Correction:

* require labeled prints that answer a specific question

## Mistake 3 - students only notice the symptom

Why it happens:

* the visible wrong answer is easier to see than the place where the value drift began

Correction:

* ask: where is the first place the value becomes wrong?

---

# 9. Explain / Checkpoint Questions (3-8 minutes)

Ask:

* What did you expect to happen?
* What actually happened?
* What evidence helped you narrow the problem?
* Where did the value first become wrong?

---

# 10. End-of-Class Success Check

> By the end of this session, students should be able to compare expected vs actual behavior, use simple print-debugging evidence, and identify where a bug is likely coming from.

---

# 11. Materials / Artifacts Used

* Week 4 debugging and print-debugging demos
* [Instructor Notes - The Debugging Process](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Demos/Instructor_Notes-Debugging_Process.md)
* A6 - Debug and Explain
* [Lecture Content and Demo Alignment Matrix](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md)

