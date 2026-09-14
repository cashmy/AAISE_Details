# Assignment Progression Overview - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `1.3`  
Purpose: Scaffolded 8-week, 10-assignment progression aligned to the spring delivery rhythm

---

# Delivery Constraint

Spring semester courses run for eight weeks, four class meetings per week:

```text
Monday, Tuesday, Thursday, Friday
9:30-11:23
```

Course 123 should use:

- 2 lectures per week
- 2 labs per week
- a strong lecture-to-lab relationship
- assignment work that aligns to the weekly lecture sequence

Preferred weekly rhythm:

| Day | Primary Use | Assignment Role |
| --- | --- | --- |
| Monday | Lecture 1 | Introduce first modeling move |
| Tuesday | Lab 1 | Start or complete Assignment A / checkpoint |
| Thursday | Lecture 2 | Introduce second modeling move or refinement lens |
| Friday | Lab 2 | Complete Assignment B or revise/finalize iterative assignment |

Most weeks should have two assignment targets, one aligned to each lecture/lab pair.

Some weeks are intentionally single-assignment weeks. In Weeks 1, 2, and 4, the assignment must be iterative: students create a first checkpoint after Lecture/Lab 1, then revise or extend the same assignment after Lecture/Lab 2. Week 3 is also a single-assignment week, but its second lab is primarily tool training, diagram completion, and review rather than a separate iteration cycle.

---

# Design Position

The assignments should not behave like unrelated weekly database tasks. They should form one evolving modeling thread while still respecting the two-lecture, two-lab weekly cadence.

Course 123 may introduce relational modeling concepts such as tables, rows, columns, keys, relationships, and constraints. It should not require SQL syntax, SQL queries, SQL DDL, or SQL scripts. SQL belongs in the following `10-152-120 Database Query and Design` course.

MongoDB concepts such as collections, documents, fields, arrays, embedded documents, references, BSON, CRUD, and introductory aggregation are allowed because they build on prior Python and Web Foundations work with JSON, dictionaries, lists, and arrays.

The repeated evidence pattern is:

```text
system intent -> model artifact -> decision rationale -> evidence of fit -> tradeoff or limitation
```

The course uses three instructional layers:

| Layer | Role in Assignments |
| --- | --- |
| SKY | Students frame system intent, audience, success, and modeling questions |
| CORE | Students create model artifacts, comparisons, maps, and rationales |
| BASE | Students use tools, diagrams, documents, queries, or MongoDB operations to produce evidence |

CORE is the hinge. No assignment should be only broad explanation or only tool mechanics.

---

# Assignment System Summary

| Week | Lecture/Lab Pair | Assignment | Assignment Mode | Primary CORE Artifact |
| --- | --- | --- | --- | --- |
| 1 | L1/Lab1 + L2/Lab2 | A1 Conceptual Model Start and Quality Revision | Iterative single assignment | Conceptual model, entity purposes, open questions, revision note |
| 2 | L1/Lab1 + L2/Lab2 | A2 Relational Structure and Process Mapping | Iterative single assignment | Entity/attribute/key/relationship table, process map, constraints |
| 3 | L1/Lab1 + L2/Lab2 | A3 ERD Creation and Diagramming Practice | Single assignment with tool-training lab | ERD, notation checklist, assumptions, tool-use notes |
| 4 | L1/Lab1 + L2/Lab2 | A4 Conceptual Modeling Refinement | Iterative single assignment | Revised model, change log, model quality self-assessment |
| 5 | L1/Lab1 | A5 Normalization and Anomaly Analysis | Separate assignment | Anomaly/risk notes and normalization recommendation |
| 5 | L2/Lab2 | A6 Business Rules and Performance Tradeoffs | Separate assignment | Rule placement table and access-pattern tradeoff |
| 6 | L1/Lab1 | A7 MongoDB Setup and Document Boundary Draft | Separate assignment | Document boundary decision and sample collection/document |
| 6 | L2/Lab2 | A8 Relational vs Document Model Comparison | Separate assignment | Embedded/reference comparison and relational/document tradeoff |
| 7 | L1/Lab1 | A9 MongoDB CRUD and Query Evidence | Separate assignment | Query/access-pattern map and CRUD/query evidence |
| 7 | L2/Lab2 | A10 Aggregation, Performance, and Final Modeling Defense Prep | Separate assignment | Aggregation evidence, performance note, capstone prep |

Week 8 should be reserved primarily for capstone completion, explanation defense, revision, and presentation/check-off using the evidence from A1-A10. It may have capstone due dates, but it does not need a new numbered assignment unless the LMS requires it.

---

# Scenario Strategy

Students should select one primary scenario in Week 1 and keep working with that scenario unless the instructor approves a change.

Recommended student scenario options:

1. Student/Course/Schedule Tracker
2. Customer/Orders/Invoicing
3. Books/Library
4. Music Collection

Instructor demo scenarios should remain separate from student scenarios to reduce copying.

Recommended instructor demo scenario:

- E-commerce with reviews/ratings

Optional larger instructor reference scenario:

- Project management system

---

# Week 1 - Data Modeling Foundations

## A1 Conceptual Model Start and Quality Revision

Assignment mode: Iterative single assignment  
Aligned lectures: Lecture 1 Data-Centric Design Principles; Lecture 2 Model Quality and Evaluation  
AI involvement level: Manual First

### Purpose

Students experience a data model as a thinking artifact. The goal is not a final schema. The goal is to identify what the system needs to remember, relate, and question, then revise the model using quality criteria.

### Tuesday Checkpoint - After Lecture 1

Students submit or save an initial checkpoint with:

1. Scenario selected.
2. System intent statement.
3. Candidate entity list.
4. Purpose statement for each entity.
5. Plain-English relationship statements.
6. At least three open modeling questions.

### Friday Final Submission - After Lecture 2

Students revise the checkpoint by adding:

1. A model quality review using simple criteria: clarity, usefulness, flexibility, missing information, and ambiguity.
2. One entity or relationship revision based on the quality review.
3. One explanation of what the model currently makes easier.
4. One explanation of what the model does not yet answer.
5. AI-use statement, if applicable.

### Required CORE Artifact

- Initial conceptual model
- Entity purpose list
- Relationship statement list
- Open modeling questions
- Quality revision note

### BASE Evidence

- Optional rough sketch or simple diagram
- No formal ERD required
- No SQL, MongoDB, or implementation detail

### Success Criteria

Successful work shows that the student can extract an initial information structure from a scenario and improve it using basic model quality criteria.

---

# Week 2 - Relational Model Components and Data-Process Connection

## A2 Relational Structure and Process Mapping

Assignment mode: Iterative single assignment  
Aligned lectures: Lecture 1 Core Relational Concepts; Lecture 2 Data-Process Connection  
AI involvement level: AI-Assisted after manual attempt

### Purpose

Students convert conceptual thinking into relational structure while preserving the link between data and system behavior.

### Tuesday Checkpoint - After Lecture 1

Students extend A1 by creating:

1. Entity/attribute table.
2. Primary key candidates.
3. Foreign key candidates or relationship links.
4. Relationship type labels.
5. Plain-language integrity constraint notes.

### Friday Final Submission - After Lecture 2

Students revise the checkpoint by adding:

1. Two or three system actions or processes.
2. A process-to-data map showing which entities/attributes each action needs.
3. One revision to the relational structure based on the process map.
4. One remaining modeling question about process support.

### Required CORE Artifact

- Entity/attribute/key/relationship table
- Process-to-data map
- Integrity constraint notes
- Process-driven revision note

### BASE Evidence

- Optional relational sketch
- No SQL required

### Success Criteria

Successful work shows that the student can connect system behavior to relational structure without reducing the assignment to syntax.

---

# Week 3 - ERD Design and Visualization

## A3 ERD Creation and Diagramming Practice

Assignment mode: Single assignment with tool-training lab  
Aligned lectures: Lecture 1 ERD Fundamentals and Notation; Lecture 2 draw.io Training and Practice  
AI involvement level: AI-Assisted critique only

### Purpose

Students learn to turn relational structure into a visual model using basic ERD notation and a diagramming tool. The goal is not artistic polish. The goal is a readable model another person can inspect.

### Tuesday Lab - Diagram Planning and Tool Orientation

Students should:

1. Review their A2 entity/attribute/key/relationship table.
2. Identify which entities and relationships belong in the first ERD.
3. Practice creating entities, attributes, connectors, and relationship labels in draw.io.
4. Save a small practice file or screenshot as tool-training evidence when required.

### Friday Lab - ERD Completion and Review

Students should complete one ERD assignment by:

1. Converting the A2 structure into an ERD.
2. Including entities, key attributes, important non-key attributes, relationships, and cardinality.
3. Using consistent notation.
4. Writing assumptions for unclear relationships or scope decisions.
5. Completing a notation and readability checklist.
6. Explaining the most important relationship in the model.
7. Documenting AI assistance if used.

### Required CORE Artifact

- ERD
- Notation and readability checklist
- Assumption list
- Design rationale
- AI review notes, if used

### BASE Evidence

- draw.io source file or exported diagram
- accepted alternatives: Lucidchart, Miro/FigJam, ERDPlus, Visual Paradigm, Creately, Mermaid, or another instructor-approved ERD-capable tool
- optional tool-practice screenshot or export

### Success Criteria

Successful work shows that the student can make model structure visible using standard notation at an introductory level and can use the diagram as a communication artifact.

---

# Week 4 - Conceptual Modeling Process

## A4 Conceptual Modeling Refinement

Assignment mode: Iterative single assignment  
Aligned lectures: Lecture 1 Modeling Process; Lecture 2 Advanced Conceptual Patterns  
AI involvement level: AI-Assisted critique

### Purpose

Students practice systematic model refinement. They should improve a model because the system understanding changed, not because they are adding complexity for its own sake.

### Tuesday Checkpoint - After Lecture 1

Students should:

1. Review feedback, assumptions, and open questions from A1-A3.
2. Identify at least two model issues.
3. Create a revision plan.
4. Explain what each planned revision is intended to clarify or fix.

### Friday Final Submission - After Lecture 2

Students revise the model using advanced conceptual pattern awareness.

They should consider whether the model needs:

1. Role clarification.
2. Subtype or category clarification.
3. Hierarchy or grouping structure.
4. Associative entity.
5. Event entity.
6. Boundary clarification.

Final submission includes:

1. Revised model.
2. Change log.
3. Explanation of which conceptual pattern was considered or applied.
4. Model quality self-assessment.
5. Remaining open questions.

### Required CORE Artifact

- Revision plan
- Revised model
- Change log
- Conceptual pattern note
- Model quality self-assessment

### BASE Evidence

- Revised ERD or marked-up model notes

### Success Criteria

Successful work shows that the student can revise a model through a deliberate process and explain why the revision improves the model.

---

# Week 5 - Normalization and Business Rules

## A5 Normalization and Anomaly Analysis

Assignment mode: Separate assignment  
Aligned lecture: Lecture 1 Normalization Awareness  
AI involvement level: AI-Assisted critique

### Purpose

Students learn that a model can appear reasonable but still create data maintenance problems.

### Student Task

Students should:

1. Identify one possible insert, update, or delete anomaly risk in their model or in an instructor-provided sample.
2. Explain what causes the risk.
3. Identify whether normalization would help.
4. Recommend one structural improvement or explain why the current model is acceptable.

### Required CORE Artifact

- Anomaly/risk notes
- Normalization awareness explanation
- Structural recommendation

### BASE Evidence

- Optional schema excerpt or ERD annotation

### Success Criteria

Successful work shows introductory reasoning about normalization as a model-quality tool, not a memorized ritual.

## A6 Business Rules and Performance Tradeoffs

Assignment mode: Separate assignment  
Aligned lecture: Lecture 2 Denormalization and Business Rules  
AI involvement level: AI-Assisted critique

### Purpose

Students learn that business rules and performance needs affect where responsibility belongs in a system.

### Student Task

Students should:

1. Identify at least three business rules in the scenario.
2. Decide where each rule might be enforced: database, application/backend, user process, or mixed.
3. Identify one access pattern that could create performance pressure.
4. Explain one possible denormalization or performance tradeoff.
5. Explain why that tradeoff may or may not be worth it.

### Required CORE Artifact

- Rule placement table
- Access pattern note
- Performance or denormalization tradeoff explanation

### BASE Evidence

- Optional model annotation

### Success Criteria

Successful work shows that the student can reason about model responsibility, business rules, and performance at an appropriate introductory level.

---

# Week 6 - MongoDB Fundamentals

## A7 MongoDB Setup and Document Boundary Draft

Assignment mode: Separate assignment  
Aligned lecture: Lecture 1 MongoDB Architecture and Setup  
AI involvement level: AI-Assisted or limited AI-Injected after student framing

### Purpose

Students learn MongoDB setup and basic document thinking without reducing the week to installation mechanics.

### Student Task

Students should:

1. Complete the required MongoDB setup or guided environment access.
2. Identify the part of their relational model they will convert first.
3. Identify two access patterns the document model should support.
4. Draft one collection boundary.
5. Create one simple sample document.

### Required CORE Artifact

- Access pattern notes
- Collection/document boundary decision
- First document draft

### BASE Evidence

- Setup evidence when required
- First database/collection or guided equivalent
- Sample document

### Success Criteria

Successful work shows that the student can connect setup and document creation to an intended access pattern.

## A8 Relational vs Document Model Comparison

Assignment mode: Separate assignment  
Aligned lecture: Lecture 2 Document Data Modeling  
AI involvement level: AI-Assisted or limited AI-Injected after document boundaries are defined

### Purpose

Students compare relational and document representations as modeling choices.

### Student Task

Students should:

1. Create at least two sample documents.
2. Decide what information should be embedded.
3. Decide what information should be referenced.
4. Compare the document model to the relational model.
5. Explain what the document model makes easier and what it makes harder.

### Required CORE Artifact

- Embedded vs referenced comparison
- Relational vs document tradeoff table
- Representation decision explanation

### BASE Evidence

- JSON/BSON-style sample documents
- MongoDB collection evidence when required

### Success Criteria

Successful work shows that the student can make representation choices based on retrieval and update needs.

---

# Week 7 - MongoDB Operations

## A9 MongoDB CRUD and Query Evidence

Assignment mode: Separate assignment  
Aligned lecture: Lecture 1 CRUD Operations  
AI involvement level: AI-Injected allowed for query help after expected results are stated

### Purpose

Students use MongoDB operations as evidence that the document model can support system behavior.

### Student Task

Students should:

1. Perform basic CRUD operations or document the guided equivalent.
2. Write at least one query connected to a real system question.
3. State the expected result before running or checking the query.
4. Explain how the document shape helped or complicated the operation.

### Required CORE Artifact

- Query/access-pattern map
- Expected-result notes
- Retrieval explanation

### BASE Evidence

- CRUD examples
- Query examples
- Result evidence

### Success Criteria

Successful work shows that the student can connect operations to model behavior rather than treating operations as disconnected syntax practice.

## A10 Aggregation, Performance, and Final Modeling Defense Prep

Assignment mode: Separate assignment  
Aligned lecture: Lecture 2 Aggregation and Performance  
AI involvement level: AI-Injected allowed for aggregation help after expected results are stated

### Purpose

Students connect aggregation, performance awareness, and final modeling defense preparation.

### Student Task

Students should:

1. Build at least one aggregation pipeline or guided aggregation exercise.
2. Explain the system question the aggregation answers.
3. Identify one simple performance consideration such as index awareness, query shape, explain output, or repeated access pattern.
4. Select the evidence they will use in the Week 8 capstone defense.
5. Draft a short claim about which representation currently fits their scenario better and why.

### Required CORE Artifact

- Aggregation-to-system-question map
- Performance awareness note
- Capstone evidence selection
- Draft modeling claim

### BASE Evidence

- Aggregation example and result
- Optional explain/index observation

### Success Criteria

Successful work shows that the student can connect transformation and performance evidence to a broader modeling defense.

---

# Week 8 - Capstone Modeling Defense

Week 8 should focus on synthesis, completion, and explanation. It may use capstone due dates, but the numbered assignment evidence should already exist through A1-A10.

Week 8 is not a new numbered assignment. It is a capstone project and defense using one approved pathway:

1. Continue and finalize the database concept used during Weeks 1-7.
2. Choose a remaining unused option from `Database_Concept_Options_v1.md` and complete a compressed conceptual design.
3. Design a database layer for a project from `10-152-117 Python Programming` or `10-152-118 Web Development Foundations`.
4. Use a new instructor-approved concept.

Option 2 is expected to use substantial AI assistance because the design is compressed into the capstone week. Students choosing this pathway must provide a stronger AI assistance disclosure.

Recommended Week 8 evidence packet:

1. README with Capstone Evidence Index.
2. System scope statement.
3. ERD or equivalent visual model.
4. Business rules and constraints.
5. Relational model evidence.
6. NoSQL/document model evidence, if used or selected.
7. Relational vs document consideration.
8. Final design defense.
9. AI assistance disclosure.

## AI-Ready Retrieval Boundary Notes

AI-ready retrieval boundary notes may be included when they fit the chosen project. Students should identify:

1. What should be searchable.
2. What should be summarizable.
3. What should be filtered.
4. What should be excluded or protected.
5. What metadata, provenance, or source tracking would matter.

## Final Defense Question

Students should be able to answer:

```text
Given this system idea, why does this database design fit, and what does it not handle yet?
```

---

# Suggested Rubric Emphasis

Most assignments should use three to five rubric rows. Avoid scoring every technical and core ability category every week.

| Assignment | Suggested Technical Emphasis | Suggested Core Ability Emphasis |
| --- | --- | --- |
| A1 | T1 Data Modeling Fundamentals | C1 Solve Problems, C2 Communicate Clearly |
| A2 | T1 Data Modeling Fundamentals | C1 Solve Problems, C2 Communicate Clearly |
| A3 | T2 ERD Design and Visualization | C2 Communicate Clearly, C3 Work Productively |
| A4 | T1 Data Modeling Fundamentals, T2 ERD Design and Visualization | C1 Solve Problems, C4 Value Learning |
| A5 | T5 Performance and Scalability Reasoning | C1 Solve Problems, C2 Communicate Clearly |
| A6 | T5 Performance and Scalability Reasoning | C1 Solve Problems, C2 Communicate Clearly |
| A7 | T3 Relational vs Non-Relational Data Structures | C3 Work Productively, C4 Value Learning |
| A8 | T3 Relational vs Non-Relational Data Structures | C1 Solve Problems, C2 Communicate Clearly |
| A9 | T4 Data Transformation and Integration | C1 Solve Problems, C2 Communicate Clearly |
| A10 | T4 Data Transformation and Integration, T5 Performance and Scalability Reasoning | C1 Solve Problems, C2 Communicate Clearly |
| Week 8 Defense | T3, T5, T6 AI-Ready Data Concepts | C2 Communicate Clearly, C6 Act Professionally |

Rubric note: the existing MRS should be revised so its technical rows match the WIDS T1-T6 language more closely.

---

# Instructor Production Notes

Next artifacts should be produced in this order:

1. Full student-facing A1 sheet.
2. Refactored Week 1 instructor discovery demo.
3. A1 checkpoint/final submission worksheet.
4. A1 success example, held for release after submission.
5. Full student-facing A2 sheet.
6. MRS-DM v2 aligned to the revised 10-assignment progression.

Do not generate all full assignment sheets at once until A1 and A2 have been tested for tone, scaffold level, and weekly pacing.
