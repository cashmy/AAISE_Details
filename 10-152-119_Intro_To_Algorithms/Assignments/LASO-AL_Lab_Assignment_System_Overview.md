# LAB ASSIGNMENT SYSTEM OVERVIEW - ALGORITHMIC PROBLEM SOLVING

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This artifact defines the lab assignment system for `10-152-119 Algorithmic
Problem Solving`.

The course uses a lecture-demo-lab pattern designed for adult learners:

1. The instructor presents the concept.
2. The instructor demonstrates a related example.
3. Students complete a lab that maps to the demo conceptually but is not the
   same task.
4. Students produce evidence that their algorithm works, can be explained, and
   can be evaluated.
5. A successful version may be released after the assignment is completed for
   review, comparison, and correction.

The intent is to support transfer rather than copying. Demos should make the
thinking visible; labs should require students to apply that thinking to a new
but approachable problem.

---

# Pedagogical Model

The standard instructional movement is:

```text
Lecture concept -> instructor demo -> guided lab start -> student lab work
-> evidence and explanation -> post-lab success version
```

This pattern supports:

- concept introduction before task demand
- modeled expert thinking before independent work
- near transfer from demo to lab
- active student reasoning rather than transcription
- visible evidence of correctness and behavior
- delayed access to complete solutions

The demo and lab should be similar enough that students can see the mapping,
but different enough that they must make decisions.

---

# Demo-to-Lab Transfer Rule

Each lab should have a corresponding instructor demo, but the demo must not be
the lab.

The demo may share:

- the same algorithm family
- the same data structure pattern
- the same evidence type
- the same tool or file structure
- the same kind of reasoning question

The lab should change at least two of the following:

- the problem scenario
- the data set
- the input shape
- the edge cases
- the success criteria
- the explanation prompt
- the comparison target

This keeps the work accessible without turning the lab into a typing exercise.

---

# Standard Lab Package

Each fully authored lab should eventually include:

- **Student assignment sheet**
  - problem statement
  - required tasks
  - constraints and assumptions
  - evidence requirements
  - AI-use boundary
  - submission expectations

- **Instructor demo**
  - related but non-identical example
  - small enough to complete in class
  - demonstrates the core pattern students will transfer
  - includes the reasoning the instructor wants students to imitate

- **Starter files, if appropriate**
  - empty or partially structured Python file
  - sample data
  - testing scaffold
  - optional trace or table template

- **Successful version**
  - completed reference implementation or model response
  - released after the assignment closes or after the key attempt window
  - used for feedback, correction, and study

- **Instructor notes**
  - expected student difficulties
  - likely misconceptions
  - pacing notes
  - grading emphasis

---

# Lab Assignment Template

Each student-facing lab should use a consistent structure.

## 1. Lab Identity

- **Lab Number:**
- **Week:**
- **Unit:**
- **Lab Title:**
- **Primary Competency:**
- **AI Involvement Level:**

## 2. Purpose

Explain what the lab helps students practice in plain language.

## 3. Scenario / Problem

Describe the problem students must solve.

The scenario should be concrete enough to guide work but small enough for the
compressed course format.

## 4. Concepts Practiced

List `3-5` concepts maximum.

Examples:

- correctness
- edge cases
- Big-O growth
- list vs dictionary representation
- binary search preconditions
- BFS traversal
- similarity scoring

## 5. Student Tasks

List the required work in sequence.

Typical sequence:

1. Frame the problem.
2. Identify inputs, outputs, assumptions, and constraints.
3. Write pseudocode or a manual trace.
4. Implement or simulate the algorithm.
5. Test normal and edge cases.
6. Produce visible evidence.
7. Explain the approach and tradeoffs.
8. Use AI only within the stated boundary, if allowed.

## 6. Evidence Requirements

Specify what students must submit beyond code.

Possible evidence forms:

- trace table
- timing table
- growth chart
- comparison table
- graph or grid diagram
- sorted/unsorted example
- similarity matrix
- explanation of assumptions
- AI-use reflection

## 7. AI Boundary

State the approved AI role.

Possible patterns:

- **Manual First:** AI may not be used until after the student completes the
  initial framing, pseudocode, or trace.
- **AI-Assisted:** AI may explain, critique, compare, or suggest questions, but
  students must verify and adapt.
- **AI-Injected:** AI may generate or revise code only after the student has an
  initial attempt, and students must test, justify, and explain the result.
- **AI-Integrated:** Used only when the assignment has enough structure to
  preserve student authorship.

## 8. Submission Checklist

Include a concise checklist such as:

- problem framing completed
- code or simulation completed
- required tests included
- evidence artifact included
- explanation completed
- AI-use statement included, if applicable

## 9. Success Criteria

Summarize what successful work demonstrates.

This should align with the MRS technical competencies and core abilities.

---

# Instructor Demo Template

Each demo should be planned as a companion artifact to the lab.

## 1. Demo Identity

- **Demo Title:**
- **Related Lab:**
- **Concept Transfer Target:**
- **Estimated Time:**

## 2. Demo Problem

State the demo problem.

The demo should be smaller than the lab and should avoid using the same data or
scenario.

## 3. What Students Should Notice

List the key observations students should take from the demo.

Examples:

- the algorithm depends on an assumption
- the data structure changes what is easy or expensive
- the trace shows why the result is correct
- timing evidence does not always match intuition on small inputs
- AI output still needs validation

## 4. Transfer Bridge

Make the mapping explicit:

> "In the demo, we used ______. In the lab, you will use the same idea to ______."

## 5. Demo Evidence

Name the visible artifact produced during the demo.

Examples:

- trace table
- timing table
- chart
- graph traversal order
- comparison table

## 6. Stop Point

Identify where the demo should stop so students still have meaningful work to
do in the lab.

---

# Successful Version Policy

Successful versions are instructional tools, not substitutes for the assignment.

They should normally be withheld until:

- the assignment deadline has passed, or
- the primary attempt window has closed, or
- the instructor intentionally releases a partial model for correction

Successful versions should be used to help students:

- compare their approach to a working model
- identify errors or incomplete reasoning
- improve explanation quality
- study for later work
- see what professional clarity looks like

Successful versions should not be written as the only possible solution when
multiple valid approaches exist.

---

# Weekly Lab and Final System Map

| Week | Lab Focus | Instructor Demo Pattern | Student Lab Transfer |
| --- | --- | --- | --- |
| 1 | Precision and Correctness | Demo a small instruction-following or pseudocode task with ambiguity and edge cases | Students solve a different small task and revise for precision, assumptions, and tests |
| 2 | Growth and Big-O Intuition | Demo timing behavior for a small pair of growth patterns | Students collect and explain timing evidence for a related but different comparison |
| 3 | Data Structure Choice | Demo one problem solved with two structures | Students solve a different problem using two structures and justify the fit |
| 4 | Search and Sort Behavior | Demo search preconditions or a small sort trace | Students compare search/sort behavior with new data and explain assumptions |
| 5 | Strategy Comparison | Demo two strategies for a small problem | Students solve a related problem with two strategies and compare correctness, readability, and growth |
| 6 | Graph Traversal and Real-System Modeling | Demo BFS/DFS on a small relationship or grid model | Students model a different network, workflow, or grid and produce traversal evidence |
| 7 | Similarity, Clustering, Recommendation, or Hashing | Demo a small similarity, ranking, clustering, or hashing example | Students apply the same family of idea to a different data set and explain limits |
| 8 | Final Synthesis Demo and Practice | Demo a compact tradeoff comparison between two approaches | Students complete formative explanation practice, then use the last two class days for the two-part final |

---

# Relationship to Other Artifacts

This LASO should guide the creation of:

- individual lab assignment sheets
- instructor demo files
- starter files
- successful versions
- instructor notes
- lecture outline refinements

It should remain aligned with:

- `Lab_Progression_Ladder_v2.md`
- `../v2/IIM_Matrix_v2.md`
- `../Lecture_Outlines/LOT-AL_Alignment-Based_Lecture_Outline_Template.md`
- `../v2/MRS-AL_Master_Rubric_System.md`
- `../v2/Textbook_Coverage_and_Reference_Map_v2.md`
