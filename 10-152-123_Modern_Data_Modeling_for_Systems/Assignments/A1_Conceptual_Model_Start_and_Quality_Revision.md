# ASSIGNMENT A1 - CONCEPTUAL MODEL START AND QUALITY REVISION

**Week 1 - Data Modeling Foundations**

---

# Context

A database design should begin with understanding what the system needs to remember, relate, and question.

In this assignment, you will create an early conceptual model for one approved scenario. This is not a final database design. You are not creating an ERD, writing SQL, or building a MongoDB document model yet.

The goal is to make your first modeling ideas visible, then improve them after reviewing model quality.

---

# Objective

Create and revise an early conceptual model.

Your work should demonstrate:

- a clear system intent
- candidate entities with a purpose
- plain-English relationship statements
- open modeling questions
- a quality review and revision note

---

# Task

Choose one approved database scenario and begin modeling it conceptually.

Approved student scenarios:

- Student/Course/Schedule Tracker
- Customer/Orders/Invoicing
- Books/Library
- Music Collection

Use the assignment template files in:

```text
Student_Submission_Templates/week_01/A1_conceptual_model_start_and_quality_revision/
```

The main file for this assignment is:

```text
conceptual_model_worksheet.md
```

---

# Tuesday Checkpoint - Manual First Model

Complete Sections 1-5 of `conceptual_model_worksheet.md`.

Your Tuesday checkpoint should include:

1. Selected scenario.
2. Brief scenario summary.
3. System intent.
4. Candidate entities.
5. Plain-English relationship statements.
6. At least three open modeling questions.

This checkpoint should be completed manually before AI is used.

---

# Friday Final Submission - Quality Review and Revision

Complete Sections 6-10 of `conceptual_model_worksheet.md`.

Your Friday final submission should add:

1. A quality review using clarity, usefulness, flexibility, missing information, and ambiguity.
2. A revision note explaining what changed and why.
3. A statement of what the model currently makes easier.
4. A statement of what the model does not yet answer.
5. A final conceptual model summary.

---

# Requirements

Your submission must include:

1. A completed `conceptual_model_worksheet.md`.
2. A selected approved scenario.
3. A system intent statement.
4. Candidate entities with purpose notes.
5. Plain-English relationship statements.
6. Open modeling questions.
7. A model quality review.
8. A revision note.
9. A short README reflection.
10. AI assistance notes, if AI was used.

Optional:

- `optional_conceptual_sketch.md`

The optional sketch may be a rough text or Mermaid sketch. It is not a formal ERD.

---

# Evidence Requirements

Your evidence should show both the first attempt and the revision.

Required evidence files:

```text
README.md
conceptual_model_worksheet.md
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Optional:

```text
optional_conceptual_sketch.md
```

Your README should answer:

- What was the clearest part of your first conceptual model?
- What was the most uncertain part?
- What changed after the quality review?
- What do you want feedback on?

---

# AI Use

Use the course prompting pattern when AI is allowed:

```text
Context -> Attempt -> Allowed Help -> Constraints -> Questions -> Output
```

In your AI notes or disclosure, identify the closest AI use classification:

- **AI Assistance**: AI supported critique, explanation, review, or thinking.
- **AI Enabled / Collaboration**: AI helped create, revise, compare, or complete a targeted part after your manual framing.
- **AI Embedded**: AI was used inside a tool or system that directly supported the workflow.

Start manually.

Do not use AI until after you complete Sections 1-5 of `conceptual_model_worksheet.md`.

Allowed AI uses:

- ask AI to critique your manual entity list
- ask AI to identify ambiguous relationships
- ask AI to suggest missing questions
- ask AI to point out assumptions

Not allowed:

- asking AI to complete the assignment for you
- submitting AI output without review
- treating AI suggestions as automatically correct

If you use AI, complete:

```text
ai_assistance_notes.md
```

Your notes should explain:

- the AI use classification
- what you completed manually first
- the context, attempt, allowed help, constraints, questions, and output format in your prompt
- the exact prompt you used
- what AI suggested or produced
- what you accepted, rejected, or changed
- what you verified yourself
- why the final decision remained yours

---

# Submission Requirements

Submit your assignment as instructed by your instructor.

If using the course GitHub repo structure, place your work in:

```text
week_01/A1_conceptual_model_start_and_quality_revision/
```

Your folder should include:

- `README.md`
- `conceptual_model_worksheet.md`
- `ai_assistance_notes.md`, if AI was used
- `optional_conceptual_sketch.md`, if used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> What changed after your quality review, and why did that change improve the model?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T1 - Data Modeling Foundations**
- **C2 - Communicate Clearly**

## Secondary Rubric Focus

- **C1 - Solve Problems**
- **C4 - Value Learning**

## Optional / Light Focus

- **T3 - Relational Modeling and Data Integrity**
- **T6 - Modeling Defense and AI-Assisted Design Practice**
- **C3 - Work Productively**
- **C6 - Act Professionally**

## Not Evaluated

- **T2 - ERD Design and Model Communication**
- **T4 - Document Modeling and Representation Choice**
- **T5 - MongoDB Operations as Model Evidence**
- **C5 - Work Cooperatively**, unless a peer activity is assigned

---

# Success Criteria

Successful work:

- identifies a clear system intent
- lists reasonable candidate entities
- explains why the entities matter
- states relationships in plain English
- includes meaningful open questions
- uses model quality criteria to revise the first attempt
- explains what changed and what remains uncertain
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should remain concept-first and confidence-building.

The key teaching target is:

```text
scenario -> system intent -> entities -> relationships -> open questions -> quality revision
```

Do not let students jump to:

- formal ERD notation
- SQL
- MongoDB document design
- implementation details

Useful feedback patterns:

- Good: clear entity purpose statements, honest uncertainty, meaningful relationships.
- Improvements: vague entities, missing system intent, relationships that are really attributes, AI suggestions accepted without judgment.
- Suggestions: ask sharper modeling questions, reduce scope, explain why an entity should be kept, identify one relationship to revisit in Week 2.



