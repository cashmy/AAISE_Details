# WEEK 5 DAY 2 LECTURE OUTLINE

**10-152-117 Python Programming**

---

# 1. Session Identity

* **Week / Day:** Week 5 / Tuesday
* **Date:** September 15, 2026
* **Weekly Theme:** Files, Errors, and Data Persistence
* **Lecture Title:** Structured Data and Basic Error Handling

---

# 2. Alignment Anchor

* **Assignments Supported:** A8 - Save and Load Utility; A9 - Structured Data Reader
* **Readiness Target:** students can save/load simple structured data and explain at least one likely error path
* **Primary Watch Point:** assignment success assumes students can distinguish file-not-found from bad-data problems

---

# 3. Opening Frame (2-4 minutes)

Today moves from simple stored text into structured data and failure handling.

Key message:

* files can hold more than plain notes
* structured data has a shape
* programs should respond reasonably when something goes wrong

Suggested wording:

> "Real programs do not only work with perfect input and perfect files. Today we begin dealing with structured data and the fact that file work can fail in more than one way."

---

# 4. Course Positioning (2-4 minutes)

Students now know:

* what persistence is
* how a program can write and read basic file content

Today adds:

* CSV and JSON as structured formats
* `try` / `except`
* distinction between missing files and bad data

Suggested wording:

> "Yesterday we focused on memory. Today we add structure and responsibility so the program can handle saved data more intelligently."

---

# 5. Core Concepts (10-20 minutes)

## Concept 1 - Structured data has a shape

Plain-language explanation:

* CSV and JSON are not random text
* the program needs to understand the structure to use the data well

Why it matters:

* Assignment 9 depends on students selecting values, not just printing everything

## Concept 2 - JSON and CSV serve different kinds of structure

Plain-language explanation:

* CSV is row-and-column oriented
* JSON can represent labeled and nested data

Why it matters:

* this helps students choose and interpret the format they are given

## Concept 3 - Errors are expected events, not disasters

Plain-language explanation:

* a file may be missing
* a file may exist but contain invalid or broken data

Why it matters:

* error handling is part of responsible program behavior

## Concept 4 - `try` / `except` protects the program path

Plain-language explanation:

* the program can respond to a problem instead of simply crashing

Why it matters:

* students should see error handling as part of program design

---

# 6. Demo Plan (10-20 minutes)

## Demo 1

* **Artifact:** save JSON demo
* **Focus:** write structured labeled data to a file
* **Students should notice:** program data can be saved in a reusable structure

## Demo 2

* **Artifact:** CSV summary demo
* **Focus:** read structured rows and summarize useful values
* **Students should notice:** the program is selecting fields, not dumping raw file content

## Demo 3

* **Artifact:** missing-file and invalid-JSON demos
* **Focus:** distinguish file-not-found from bad-data errors
* **Students should notice:** different failures require different explanations

Instructional note:

* explicitly compare the two failure modes in plain language

---

# 7. Hands-On / Lab Bridge (10-20 minutes)

Students should try:

* saving structured task data
* loading structured task data
* reading a provided CSV or JSON file
* handling one likely file or data error

Suggested wording:

> "Your goal today is not to become a data engineer. Your goal is to read structured data carefully, use a few meaningful values, and show that your program can respond to a likely failure case."

Do not require yet:

* deep nested data design
* large datasets
* advanced parsing edge cases

---

# 8. Common Mistakes / Watch-Fors (5-8 minutes)

## Mistake 1 - raw data is printed without interpretation

Why it happens:

* students may stop after successfully loading the file

Correction:

* require one useful selected value, summary, or filtered result

## Mistake 2 - all errors are treated as the same

Why it happens:

* students may only notice that "something failed"

Correction:

* distinguish clearly between missing-file and invalid-data cases

## Mistake 3 - JSON structure is assumed instead of inspected

Why it happens:

* students may guess at keys or fields without reading the structure carefully

Correction:

* model inspection before extraction

---

# 9. Explain / Checkpoint Questions (3-8 minutes)

Ask:

* What kind of structured data is this?
* Which value or field did your program choose to use?
* What happens if the file is missing?
* What happens if the file exists but the data is malformed?

---

# 10. End-of-Class Success Check

> By the end of this session, students should be able to load simple CSV or JSON data, use selected fields meaningfully, and explain at least one likely file-related failure path.

---

# 11. Materials / Artifacts Used

* Week 5 JSON, CSV, and error-handling demos
* A8 - Save and Load Utility
* A9 - Structured Data Reader
* [Lecture Content and Demo Alignment Matrix](D:/@Artifact_Generation/108_AAISE_Details/10-152-117_Python_Programming/Lecture_Content_and_Demo_Alignment_Matrix.md)

