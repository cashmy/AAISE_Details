# ASSIGNMENT A7 - MONGODB SETUP AND DOCUMENT BOUNDARY DRAFT

**Week 6 - Document Modeling Begins**

---

# Context

MongoDB modeling begins with deciding what data should be stored together.

In this assignment, you will begin document modeling by choosing one part of your current relational/table-shaped model and drafting one MongoDB collection/document boundary. MongoDB setup or guided environment evidence may be required, but setup is not the whole assignment.

The main evidence is your reasoning about access patterns, document boundaries, embedding, referencing, and tradeoffs.

Do not compare SQL syntax to MongoDB syntax.

---

# Objective

Draft one MongoDB document boundary from a modeling decision.

Your work should demonstrate:

- setup or guided environment evidence
- a selected model area
- at least two access patterns
- a collection boundary decision
- embed/reference reasoning
- one sample JSON document
- a tradeoff note

---

# Task

Use your current relational/table-shaped model as the starting point.

Use the assignment template files in:

```text
Student_Submission_Templates/week_06/A7_mongodb_setup_and_document_boundary/
```

The main files for this assignment are:

```text
document_boundary_worksheet.md
mongodb_setup_evidence.md
sample_document.json
```

---

# Requirements

Your submission must include:

1. A completed `document_boundary_worksheet.md`.
2. A completed `mongodb_setup_evidence.md`, unless your instructor provides an alternative.
3. A completed `sample_document.json`.
4. One selected model area to convert first.
5. At least two access patterns.
6. One proposed collection name.
7. One main document subject.
8. Embed, reference, or keep separate reasoning.
9. A tradeoff note.
10. A short README reflection.
11. AI assistance notes, if AI was used.

---

# Evidence Requirements

Required evidence files:

```text
README.md
document_boundary_worksheet.md
mongodb_setup_evidence.md
sample_document.json
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Your README should answer:

- What access pattern did you design for first?
- Why did you choose this document boundary?
- What tradeoff did your document shape create?
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

Do not use AI until after you define your access patterns and draft a boundary decision.

Allowed AI uses:

- ask AI to critique your collection boundary
- ask AI to identify what the document shape makes easier or harder
- ask AI to flag possible stale or duplicated data
- ask AI to question embed/reference decisions
- ask AI to help generate or clean up a small sample JSON document after your boundary is defined

Not allowed:

- asking AI to generate a full database
- asking AI to choose the boundary before your manual attempt
- comparing SQL syntax to MongoDB syntax
- submitting AI output without review

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
week_06/A7_mongodb_setup_and_document_boundary/
```

Your folder should include:

- `README.md`
- `document_boundary_worksheet.md`
- `mongodb_setup_evidence.md`
- `sample_document.json`
- `ai_assistance_notes.md`, if AI was used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, screenshot, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> Why does your selected access pattern support this document boundary?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T4 - Document Modeling and Representation Choice**
- **C3 - Work Productively**

## Secondary Rubric Focus

- **C4 - Value Learning**
- **C6 - Act Professionally**

## Optional / Light Focus

- **T1 - Data Modeling Foundations**
- **T3 - Relational Modeling and Data Integrity**
- **T6 - Modeling Defense and AI-Assisted Design Practice**
- **C1 - Solve Problems**
- **C2 - Communicate Clearly**

## Not Evaluated

- **T2 - ERD Design and Model Communication**, unless a model visual is included
- **T5 - MongoDB Operations as Model Evidence**
- **C5 - Work Cooperatively**, unless a peer activity is assigned

---

# Success Criteria

Successful work:

- documents the setup or guided environment path
- selects one reasonable model area
- starts from access patterns
- explains the collection/document boundary
- explains embed/reference decisions
- includes a readable sample JSON document
- identifies what the document shape makes easier and harder
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should introduce MongoDB as a modeling choice, not as a syntax comparison.

The key teaching target is:

```text
current model area -> access patterns -> collection boundary -> embed/reference choice -> sample document -> tradeoff
```

Do not let students jump to:

- SQL versus MongoDB syntax comparisons
- full database implementation
- large multi-collection designs
- setup evidence replacing modeling evidence

Useful feedback patterns:

- Good: boundary is tied to an access pattern, sample document is inspectable, embed/reference reasoning includes risk.
- Improvements: collection boundary is arbitrary, sample document does not match the reasoning, setup evidence dominates the submission, tradeoff is missing.
- Suggestions: choose one access pattern to prioritize, simplify the sample document, explain what stays outside the document, identify possible stale data.


