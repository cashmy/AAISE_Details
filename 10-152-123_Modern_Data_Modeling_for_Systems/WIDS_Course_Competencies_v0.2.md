# WIDS Course Competencies
## Course 123 - Modern Data Modeling for Systems

Status: Refactored Draft  
Version: `0.2`  
Purpose: Align WIDS competency language to the actual scaffolded course artifacts, demos, and assignments  
Framework: SWTC Core Abilities integration

---

# Alignment Position

This course teaches students how to model database-backed systems before they learn SQL in `10-152-120 Database Query and Design`.

Course 123 may use relational vocabulary such as tables, rows, columns, keys, relationships, constraints, and normalization concepts. It does not require SQL syntax, SQL scripts, SQL joins, or SQL implementation.

MongoDB concepts are introduced in Weeks 6-7 because students already have background with JSON, dictionaries, lists, and arrays from Python and Web Development Foundations.

The course arc is:

```text
conceptual model -> relational/table-shaped structure -> ERD -> refinement
-> integrity/rules -> document model -> MongoDB evidence -> design defense
```

---

# Technical Competencies (T1-T6)

## T1. Data Modeling Foundations

Bloom's Level: Apply  
Bloom's Domain: Cognitive

Competency:

Apply foundational data modeling concepts to identify system intent, candidate entities, relationships, attributes, constraints, and model-quality questions.

Learning Objectives:

- State the purpose and boundary of a database-backed system.
- Identify candidate entities and explain their purpose.
- Describe relationships in clear plain language.
- Identify attributes, key candidates, and basic constraints.
- Use model-quality criteria to revise an early model.
- Explain what a model currently answers and what remains unclear.

Primary course evidence:

- A1 conceptual model worksheet
- A2 relational structure worksheet
- A4 model revision worksheet
- Week 8 system scope and final design defense

---

## T2. ERD Design and Model Communication

Bloom's Level: Create  
Bloom's Domain: Cognitive

Competency:

Create and explain ERDs or equivalent visual models that communicate entities, relationships, cardinality, assumptions, and model boundaries.

Learning Objectives:

- Translate entity and relationship notes into an ERD.
- Use appropriate introductory ERD notation for entities, keys, relationships, and cardinality.
- Create a readable diagram using draw.io or an approved equivalent.
- Document assumptions and unclear relationships.
- Use a visual model as a communication and review artifact.
- Revise a model based on feedback, assumptions, or pattern awareness.

Primary course evidence:

- A3 ERD and readability checklist
- A4 revised model evidence
- Week 8 ERD or visual model evidence

---

## T3. Relational Modeling and Data Integrity

Bloom's Level: Analyze  
Bloom's Domain: Cognitive

Competency:

Analyze relational/table-shaped model structures for keys, relationships, constraints, anomalies, business rules, and maintenance risks without requiring SQL implementation.

Learning Objectives:

- Identify key candidates and relationship links.
- Explain relationship types and integrity constraints.
- Connect system actions to relational/table-shaped structure.
- Identify possible update, insert, or delete anomaly risks.
- Explain whether normalization would improve a model.
- Place business rules responsibly across model structure, application/backend, user process, or mixed responsibility.

Primary course evidence:

- A2 entity/attribute/key/relationship table
- A5 anomaly analysis worksheet
- A6 rule placement tradeoff worksheet
- Week 8 relational model evidence and business rules

---

## T4. Document Modeling and Representation Choice

Bloom's Level: Evaluate  
Bloom's Domain: Cognitive

Competency:

Evaluate relational/table-shaped and document-shaped representations by designing MongoDB document boundaries, embedding/reference choices, sample documents, and representation explanations.

Learning Objectives:

- Identify system questions that a document model should help answer.
- Choose a collection/document boundary based on data that is used together.
- Decide what should be embedded, referenced, or kept separate.
- Create limited JSON/BSON-style sample documents.
- Compare relational/table-shaped and document-shaped representations.
- Explain what a document model makes easier and what it does not handle yet.

Primary course evidence:

- A7 document boundary worksheet and sample document
- A8 representation comparison worksheet
- Week 8 NoSQL/document model evidence, when used
- Week 8 relational vs document consideration

---

## T5. MongoDB Operations as Model Evidence

Bloom's Level: Apply  
Bloom's Domain: Cognitive

Competency:

Apply introductory MongoDB CRUD, query, and aggregation operations as evidence that a document model can support stated system questions.

Learning Objectives:

- Use basic MongoDB operations or guided equivalents as model evidence.
- State an expected result before running or checking an operation.
- Connect a query or CRUD operation to a system question.
- Build or interpret an introductory aggregation pipeline or guided aggregation result.
- Explain how document shape helps or complicates retrieval or summary evidence.
- Identify a simple performance consideration such as query shape, repeated retrieval, document size, summary values, or index awareness.

Primary course evidence:

- A9 query/access-pattern map and operation evidence
- A10 aggregation and performance awareness evidence
- Week 8 final defense evidence, when operations support the claim

---

## T6. Modeling Defense and AI-Assisted Design Practice

Bloom's Level: Evaluate  
Bloom's Domain: Cognitive / Affective

Competency:

Evaluate and defend database design choices using evidence, limitations, and transparent AI-assisted design practices.

Learning Objectives:

- Select evidence that supports a final database design claim.
- Explain why a design fits a system idea.
- Identify what the design does not handle yet.
- Compare representation choices at an introductory level.
- Disclose AI assistance clearly and responsibly.
- Accept, reject, modify, and verify AI suggestions.
- Defend final design decisions as the student's own work.

Primary course evidence:

- AI assistance notes across assignments
- A10 capstone evidence selection
- Week 8 capstone evidence index
- Week 8 AI assistance disclosure
- Week 8 final design defense

---

# Core Abilities (C1-C6)

The Core Ability names are institution/program-wide and should remain unchanged. Course 123 defines how each Core Ability is evaluated through data modeling evidence.

---

## C1. Solve Problems

Course 123 evidence lens:

Students solve data modeling problems by identifying unclear entities, relationship issues, integrity risks, representation mismatches, document-boundary problems, and evidence gaps.

Observable evidence:

- model issue lists
- revision plans
- anomaly/risk analysis
- rule placement decisions
- troubleshooting operation results
- capstone limitation statements

---

## C2. Communicate Clearly

Course 123 evidence lens:

Students communicate data modeling decisions through diagrams, worksheets, rationale statements, assumptions, evidence indexes, and final design defenses.

Observable evidence:

- ERD explanation
- relationship and assumption notes
- design rationale
- representation comparison
- final design defense
- README reflections

---

## C3. Work Productively

Course 123 evidence lens:

Students work productively by completing scaffolded modeling artifacts, organizing files in the expected repo structure, meeting checkpoint expectations, and using lab time to produce visible progress.

Observable evidence:

- required files submitted in the correct week/assignment folder
- completed worksheets
- diagram source/export files
- setup evidence
- timely checkpoint/final submissions

---

## C4. Value Learning

Course 123 evidence lens:

Students value learning by using feedback, instructor demos, readings, templates, peer review, and AI critique to revise and improve modeling decisions.

Observable evidence:

- revision notes
- change logs
- self-assessments
- accepted/rejected AI suggestions
- improved artifacts after feedback
- questions and limitations documented honestly

---

## C5. Work Cooperatively

Course 123 evidence lens:

Students work cooperatively when they participate in peer review, shared diagram review, model critique, paired lab checks, or constructive discussion of design decisions.

Observable evidence:

- peer review notes
- collaborative diagram feedback
- partner check-off notes
- constructive critique of another model
- respectful lab participation

Note:

C5 should be assessed only when a specific assignment, lab, or class activity produces observable cooperative evidence.

---

## C6. Act Professionally

Course 123 evidence lens:

Students act professionally by preparing and submitting organized work, respecting scope and academic integrity, disclosing tool/AI use, and taking responsibility for design choices.

Observable evidence:

- complete README reflection
- organized evidence files
- AI assistance disclosure
- responsible use of tools
- honest limitation statements
- professional final defense

---

# WIDS Entry Notes

The revised T1-T6 competencies are intentionally aligned to the assignment ladder and course sequence. This avoids assessing NoSQL/document modeling before it is taught and prevents MongoDB operations from replacing the central data modeling scaffold.

Core abilities retain the institution/program-wide names. The Course 123 evidence lens describes how those abilities become observable in this course.

