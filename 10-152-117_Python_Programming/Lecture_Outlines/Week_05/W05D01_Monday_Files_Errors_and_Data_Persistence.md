# WEEK 5 DAY 1 LECTURE OUTLINE

**10-152-117 Python Programming**

---

# 1. Session Identity

* **Week / Day:** Week 5 / Monday
* **Date:** September 14, 2026
* **Weekly Theme:** Files, Errors, and Data Persistence
* **Lecture Title:** Programs That Remember

---

# 2. Alignment Anchor

* **Assignments Supported:** A8 - Save and Load Utility
* **Readiness Target:** students can explain what a program writes, where it goes, and how it is loaded back
* **Primary Watch Point:** avoid jumping to JSON too early if plain file mental model is not clear first

---

# 3. Opening Frame (2-4 minutes)

Today changes the feel of programming in an important way.

Key message:

* a program can remember information after it stops running
* stored information makes a program more useful
* persistence is a practical programming skill

Suggested wording:

> "Until now, most of your programs lived only while they were running. Today we begin making programs that can remember something after they close."

---

# 4. Course Positioning (2-4 minutes)

Students now know:

* variables
* control flow
* functions
* collections

Today adds:

* file writing
* file reading
* persistence as a program capability

Suggested wording:

> "So far, your programs could work with data while they were alive. Today we start giving programs memory beyond one run."

---

# 5. Core Concepts (10-20 minutes)

## Concept 1 - Persistence means the program can remember

Plain-language explanation:

* persistence is the idea that data can exist after the script ends

Why it matters:

* this is the conceptual reason file work matters

## Concept 2 - Writing stores information outside the running program

Plain-language explanation:

* writing sends information into a file

Why it matters:

* students need a physical or visible mental model of where the data goes

## Concept 3 - Reading brings stored information back in

Plain-language explanation:

* reading loads the saved content back into the program

Why it matters:

* save and load are one connected cycle, not two unrelated actions

## Concept 4 - A small file utility can still be useful

Plain-language explanation:

* a note keeper or task saver is already a meaningful programming step

Why it matters:

* students should feel the practical value of persistence early

---

# 6. Demo Plan (10-20 minutes)

## Demo 1

* **Artifact:** write text file demo
* **Focus:** create a file and store lines of text
* **Students should notice:** the program writes information into a named location

## Demo 2

* **Artifact:** read text file demo
* **Focus:** load stored text and display it again
* **Students should notice:** the saved content becomes usable program data

## Demo 3

* **Artifact:** one small practical save/load example
* **Focus:** connect persistence to a realistic tool idea
* **Students should notice:** save and load are part of one useful workflow

Instructional note:

* keep Monday on the plain-text mental model first
* do not rush into CSV/JSON vocabulary before students understand simple persistence

---

# 7. Hands-On / Lab Bridge (10-20 minutes)

Students should try:

* saving a note
* loading a note
* saving a simple task list line by line

Suggested wording:

> "Your goal today is not to build a full data system. Your goal is to make a small program save information, then bring it back in a way you can explain."

Do not require yet:

* CSV
* JSON
* complex error handling beyond the basic concept

---

# 8. Common Mistakes / Watch-Fors (5-8 minutes)

## Mistake 1 - file work feels too abstract

Why it happens:

* students may not form a clear mental model of where the data goes

Correction:

* explicitly point to the created file and describe the save/load cycle in plain language

## Mistake 2 - reading and writing are treated as separate unrelated skills

Why it happens:

* students may focus on individual lines of code without seeing the workflow

Correction:

* keep repeating: write stores, read retrieves

## Mistake 3 - persistence gets buried under syntax

Why it happens:

* file syntax can distract from the concept

Correction:

* keep the lecture focused on the purpose of the operation, not only the mechanics

---

# 9. Explain / Checkpoint Questions (3-8 minutes)

Ask:

* What is the program saving?
* Where does that information go?
* How does the program load it again?
* Why is this more useful than a program that forgets everything when it closes?

---

# 10. End-of-Class Success Check

> By the end of this session, students should be able to describe the save/load cycle clearly and build a small program that writes information to a file and reads it back.

---

# 11. Materials / Artifacts Used

* Week 5 text file demos
* A8 - Save and Load Utility
* [Lecture Content and Demo Alignment Matrix](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md)

