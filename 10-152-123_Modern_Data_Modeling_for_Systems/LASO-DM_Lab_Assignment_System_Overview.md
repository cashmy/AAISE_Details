# Lab Assignment System Overview - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.1`  
Purpose: Define the demo-to-lab and assignment system for the course

---

# Delivery Constraint

Course 123 runs for eight weeks, four class meetings per week:

```text
Monday, Tuesday, Thursday, Friday
9:30-11:23
```

The lab and assignment system should assume:

- 2 lectures per week
- 2 labs per week
- Monday lecture followed by Tuesday lab
- Thursday lecture followed by Friday lab
- assignment work aligned to those two lecture/lab cycles

The preferred pattern is two assignment targets per week. When there is only one assignment in a week, it should still contain two visible instructional moves:

1. a first checkpoint after Lecture/Lab 1
2. a revised or extended final submission after Lecture/Lab 2

Weeks 1, 2, and 4 are intended to use this iterative single-assignment structure. Week 3 is also a single-assignment week, but its second lab is primarily diagramming-tool training, practice, completion, and review rather than a separate iterative assignment.

---

# Purpose

This artifact defines how labs, demos, and assignments should be created for Course 123.

Course 123 may use relational modeling concepts such as tables, rows, columns, keys, relationships, and constraints, but student labs should not require SQL syntax, SQL queries, SQL DDL, or SQL scripts. SQL belongs in the following `10-152-120 Database Query and Design` course.

MongoDB collections, documents, fields, arrays, embedded documents, references, BSON, CRUD, and introductory aggregation are acceptable because they build from prior JSON, dictionary, list, and array work in Python and Web Development Foundations.

The course should not ask students to complete isolated database tasks. Each lab should help students practice one movement in the larger modeling process:

```text
understand the system need -> shape the information -> choose a representation -> test the fit -> explain the tradeoff
```

The course is compressed into eight weeks, so each assignment should reuse and deepen prior work whenever possible. Students should feel that their model is evolving rather than being replaced every week.

---

# Standard Instructional Pattern

The standard weekly movement is:

```text
lecture concept -> instructor discovery demo -> guided model start -> student transfer task -> evidence and explanation -> revision or comparison
```

The instructor demo should make expert reasoning visible. The student lab should require transfer to a related but non-identical scenario or decision.

The course should preserve three separate but connected layers:

| Layer | Demo Role | Lab Role |
| --- | --- | --- |
| SKY | Show how to frame the system need | Students state intent, audience, questions, and success criteria |
| CORE | Show how to convert need into model decisions | Students create entities, relationships, comparisons, diagrams, and rationale |
| BASE | Show only enough tool detail to produce evidence | Students use tools to express, test, or communicate the model |

If a lab only produces BASE evidence, it is probably too mechanical.  
If a lab only produces SKY explanation, it is probably too vague.  
Each lab needs a CORE artifact.

---

# Demo-to-Lab Transfer Rule

Each student lab should have a corresponding instructor demo, but the demo must not become the student assignment.

The demo and lab may share:

- the same modeling move
- the same artifact type
- the same kind of relationship problem
- the same tool
- the same evidence pattern

The lab should change at least two of the following:

- scenario
- entity set
- access pattern
- business rule
- relationship ambiguity
- audience
- evidence requirement
- tradeoff question

This keeps the task accessible without letting students copy the demo structure blindly.

---

# Standard Lab Package

Each fully developed lab should eventually include:

- Student assignment sheet
- Instructor demo file
- Starter model or worksheet, when useful
- Evidence checklist
- AI-use boundary
- Rubric row mapping
- Instructor notes
- Optional success example released after the attempt window

Not every week needs a large assignment. Some weeks may use one primary assignment plus a lab checkpoint or revision artifact.

---

# Student Assignment Template

Each assignment should use a consistent structure.

## 1. Assignment Identity

- Assignment number:
- Week:
- Title:
- Course phase:
- Primary competency:
- Secondary competency:
- AI involvement level:

## 2. Purpose

State what modeling capability the assignment builds.

Use capability language, not only topic language.

Weak:

```text
This assignment covers ERDs.
```

Better:

```text
This assignment helps you make a data model visible so another person can inspect relationships, assumptions, and missing information.
```

## 3. Scenario

Provide a bounded system scenario.

The scenario should be concrete enough to support modeling decisions but incomplete enough that students must identify questions and assumptions.

## 4. Modeling Task

Describe the main student task in sequence.

Typical sequence:

1. State the system intent.
2. Identify information the system must remember.
3. Create or revise the model artifact.
4. Test the model against specific system actions or questions.
5. Explain one tradeoff, limitation, or open issue.
6. Document AI use if applicable.

## 5. Required CORE Artifact

Each assignment must name the CORE artifact students will submit.

Examples:

- conceptual model
- entity/attribute/relationship table
- ERD
- model revision log
- rule placement table
- relational vs document comparison table
- document boundary decision
- query-to-access-pattern map
- AI-ready retrieval boundary map

## 6. BASE Evidence

Name the tool-produced or implementation-level evidence, if any.

Examples:

- draw.io export
- MongoDB collection screenshot or command transcript
- JSON sample document
- CRUD/query examples
- aggregation result

## 7. Explanation Requirement

Every assignment should require a short explanation.

The explanation should answer:

- What did you choose?
- Why does it fit the system need?
- What does it make easier?
- What does it make harder?
- What question remains?

## 8. AI Boundary

Use one of the standard levels:

- Manual First
- AI-Assisted
- AI-Injected
- AI-Integrated

The assignment should state exactly when AI may enter the work.

## 9. Submission Checklist

Use a short checklist so students can self-audit before submitting.

## 10. Success Criteria

Describe what successful work demonstrates.

Success criteria should align to the selected MRS rows and should avoid grading every course competency every week.

---

# Instructor Demo Template

Each demo should be planned as a companion to the student task.

## 1. Demo Identity

- Demo title:
- Related assignment:
- Concept transfer target:
- Estimated time:

## 2. Demo Scenario

State the demo scenario.

The demo should be smaller than the student assignment or use a different domain.

## 3. What Students Should Notice

List the main observations.

Examples:

- The first entity list is usually incomplete.
- A relationship may hide an event entity.
- A model can be logically clean but poor for a common access pattern.
- Embedding makes one read easy but can make updates harder.
- AI suggestions may add plausible but out-of-scope complexity.

## 4. Transfer Bridge

Make the transfer explicit:

```text
In the demo, we used ______ to decide ______.
In your lab, you will use the same kind of reasoning to decide ______.
```

## 5. Demo Evidence

Name the artifact produced during the demo.

## 6. Stop Point

Identify where the demo should stop so students still have meaningful modeling work to do.

---

# AI Involvement Progression

AI should support critique, comparison, and explanation more often than direct production.

| Level | Course Meaning | Appropriate Weeks |
| --- | --- | --- |
| Manual First | Students produce initial framing or model before AI enters | Weeks 1-3 |
| AI-Assisted | AI may explain, critique, question, or compare | Weeks 2-8 |
| AI-Injected | AI may generate code, query, JSON, or alternate model after student framing | Weeks 6-8 |
| AI-Integrated | AI acts as a structured collaborator inside a larger modeling process | Optional capstone only |

AI should not be used to skip the CORE artifact. If AI generates BASE evidence, students still need to explain the modeling decision.

---

# Recommended Assignment System

The strongest structure is a 10-assignment ladder across Weeks 1-7, followed by a Week 8 capstone defense that synthesizes evidence from the prior assignments.

Weeks 1, 2, and 4 should use iterative single assignments. Each one still follows the two-lecture rhythm by requiring a first checkpoint after Lecture/Lab 1 and a revised final submission after Lecture/Lab 2. Week 3 should remain one assignment because part of the lab time is needed for draw.io training and supported tool use.

| Week | Assignment Target | CORE Artifact | BASE Evidence | Primary Purpose |
| --- | --- | --- | --- | --- |
| 1 | A1 Conceptual Model Start and Quality Revision | Conceptual model, entity purposes, open questions, quality revision | Optional rough sketch | Move from scenario to information shape |
| 2 | A2 Relational Structure and Process Mapping | Entity/attribute/key/relationship table, process map, constraints | Optional relational sketch | Connect data to process |
| 3 | A3 ERD Creation and Diagramming Practice | ERD, notation checklist, assumptions, rationale | draw.io source/export or approved equivalent | Make the model visible and reviewable |
| 4 | A4 Conceptual Modeling Refinement | Revision plan, revised model, change log, quality assessment | Revised ERD or model notes | Improve the model systematically |
| 5 | A5 Normalization and Anomaly Analysis | Anomaly/risk notes and normalization recommendation | Optional schema excerpt | Test model correctness and maintenance risk |
| 5 | A6 Business Rules and Performance Tradeoffs | Rule placement table and access-pattern tradeoff | Optional model annotation | Test model responsibility and performance judgment |
| 6 | A7 MongoDB Setup and Document Boundary Draft | Access pattern notes, document boundary decision, first document draft | Setup evidence and sample document | Begin document representation from access patterns |
| 6 | A8 Relational vs Document Model Comparison | Embedded/reference comparison and relational/document tradeoff | Sample documents | Compare representation strategies |
| 7 | A9 MongoDB CRUD and Query Evidence | Query/access-pattern map and expected-result notes | CRUD/query evidence | Show the model supports behavior |
| 7 | A10 Aggregation, Performance, and Final Modeling Defense Prep | Aggregation map, performance note, capstone evidence selection | Aggregation result and optional performance observation | Connect transformation evidence to defense |
| 8 | Capstone Modeling Defense | Final comparison, AI-ready boundaries, decision defense | Final model packet | Defend representation choices |

This gives students one evolving modeling thread while still respecting the two-lecture, two-lab weekly cadence.

---

# Week-by-Week Lab Design Notes

## Week 1 - Conceptual Model Start

The first assignment should be small and intentionally unfinished.

Avoid requiring:

- complete attributes
- perfect cardinality
- formal ERD notation
- implementation detail

Require:

- intent
- entities with purpose
- relationships in plain English
- open questions
- one explanation of uncertainty

## Week 2 - Relational Structure Analysis

This should extend Week 1 rather than replace it.

Require:

- entities
- attributes
- key candidates
- relationship types
- process-to-data mapping

Avoid making this a SQL assignment.

## Week 3 - ERD Creation and Review

This is a natural major checkpoint.

Require:

- clear ERD
- assumptions
- notation effort
- peer or self-review
- draw.io practice or approved equivalent tool evidence

The grade should emphasize communication and structure, not artistic polish.

Acceptable alternative tools may include Lucidchart, Miro, FigJam, ERDPlus, Visual Paradigm, Creately, Mermaid, or another instructor-approved ERD-capable tool. Some tools can generate database scripts; that feature should not be used in Course 123.

## Week 4 - Model Refinement

This should not be a new unrelated complex scenario unless students are ready.

Preferred structure:

- revise the Week 3 ERD
- add or correct hierarchy, role, event, or associative entity issues
- explain changes

This week teaches modeling process, not model size.

## Week 5 - Rules, Normalization, and Performance Stress Test

This can be one assignment with two parts rather than two separate assignments.

Part A:

- identify anomaly or normalization concerns

Part B:

- place business rules and explain one performance exception

The target is judgment, not deep normalization theory.

## Week 6 - Document Model Conversion

This should focus on representation choice before MongoDB mechanics.

Require:

- document boundary decision
- embedded vs referenced comparison
- sample documents
- relational vs document tradeoff

Tool setup should be supported, but setup should not dominate the assignment.

## Week 7 - Operations and Retrieval Evidence

This week should prove that the document model supports behavior.

Require:

- CRUD examples
- one query connected to a system question
- one aggregation or guided transformation
- note on how document shape affected the query

## Week 8 - Capstone Modeling Defense

The capstone should be a defense, not a surprise new build.

Require:

- final model packet
- relational/document comparison
- access pattern and performance reasoning
- AI-ready retrieval boundary notes
- final explanation

---

# Rubric Use Guidance

Most weekly assignments should use three to five rubric rows:

- one or two technical rows
- one or two core ability rows
- one communication or explanation row when the assignment requires rationale

Avoid scoring all T1-T6 and C1-C6 every week.

Suggested major checkpoints:

| Week | Strong Evaluation Focus |
| --- | --- |
| 3 | ERD design and communication |
| 5 | rules, normalization, performance reasoning |
| 7 | document model operation and retrieval |
| 8 | synthesis and modeling defense |

---

# Success Example Policy

Success examples are useful, but they should normally be released after the primary attempt window.

They should show:

- one reasonable model, not the only model
- clear assumptions
- explanation of tradeoffs
- professional formatting
- appropriate scope

They should not erase the ambiguity that makes modeling educational.

---

# Instructor Quality Check

Before approving a lab or assignment, check:

- Does it identify the required CORE artifact?
- Does it avoid premature BASE detail?
- Does it require evidence beyond explanation?
- Does it require explanation beyond artifact production?
- Does the demo support transfer without becoming the answer?
- Does AI support reasoning rather than replacing it?
- Does this assignment build from the previous week?
