# ASSIGNMENT A8 - RELATIONAL VS DOCUMENT MODEL COMPARISON

**Week 6 - Representation Choice and Tradeoffs**

---

# Context

Relational/table-shaped models and document-shaped models organize data differently.

In this assignment, you will compare representation choices. You will use your A7 document boundary, create two document options or variants, and compare them against your relational/table-shaped model.

You are not comparing SQL syntax to MongoDB syntax. You are comparing representation, retrieval, update responsibility, duplication, and tradeoffs.

---

# Objective

Compare relational and document-shaped representations for one access pattern.

Your work should demonstrate:

- one selected access pattern
- two document options or variants
- embedding and referencing comparison
- relational/table-shaped comparison
- document-shaped comparison
- duplication or update concerns
- a recommendation with a tradeoff

---

# Task

Use your A7 document boundary as the starting point.

Use the assignment template files in:

```text
Student_Submission_Templates/week_06/A8_relational_vs_document_model_comparison/
```

The main files for this assignment are:

```text
representation_comparison_worksheet.md
sample_document_option_a.json
sample_document_option_b.json
```

---

# Requirements

Your submission must include:

1. A completed `representation_comparison_worksheet.md`.
2. A completed `sample_document_option_a.json`.
3. A completed `sample_document_option_b.json`.
4. One access pattern being tested.
5. An embedded vs referenced comparison.
6. A relational vs document tradeoff table.
7. A current representation recommendation.
8. One remaining boundary question.
9. A short README reflection.
10. AI assistance notes, if AI was used.

---

# Evidence Requirements

Required evidence files:

```text
README.md
representation_comparison_worksheet.md
sample_document_option_a.json
sample_document_option_b.json
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Your README should answer:

- Which representation currently fits your selected access pattern better?
- What does the document model make easier?
- What does the document model make harder?
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

Complete your two document options and comparison notes before using AI.

Allowed AI uses:

- ask AI to critique tradeoffs between the two document options
- ask AI to identify update or duplication concerns
- ask AI to evaluate whether the option fits the stated access pattern
- ask AI to suggest one human design question
- ask AI to help clean up JSON formatting after your design decision is made

Not allowed:

- asking AI to choose only based on which option looks simpler
- comparing SQL syntax to MongoDB syntax
- submitting AI output without explaining your decision
- replacing your comparison with AI output

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
week_06/A8_relational_vs_document_model_comparison/
```

Your folder should include:

- `README.md`
- `representation_comparison_worksheet.md`
- `sample_document_option_a.json`
- `sample_document_option_b.json`
- `ai_assistance_notes.md`, if AI was used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, screenshot, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> Which representation best fits the selected access pattern right now, and what tradeoff comes with that choice?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T4 - Document Modeling and Representation Choice**
- **C2 - Communicate Clearly**

## Secondary Rubric Focus

- **C1 - Solve Problems**
- **C6 - Act Professionally**

## Optional / Light Focus

- **T1 - Data Modeling Foundations**
- **T3 - Relational Modeling and Data Integrity**
- **T6 - Modeling Defense and AI-Assisted Design Practice**
- **C3 - Work Productively**
- **C4 - Value Learning**

## Not Evaluated

- **T2 - ERD Design and Model Communication**, unless a visual model is included
- **T5 - MongoDB Operations as Model Evidence**
- **C5 - Work Cooperatively**, unless a peer activity is assigned

---

# Success Criteria

Successful work:

- compares two document options or variants
- connects the comparison to an access pattern
- explains embedding and referencing decisions
- compares representation choices rather than syntax
- identifies duplication or update concerns
- recommends a representation with a named tradeoff
- includes a remaining boundary question
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should teach representation choice as contextual, not as a universal ranking of database types.

The key teaching target is:

```text
access pattern -> document option A -> document option B -> table-shaped comparison -> tradeoff -> recommendation
```

Do not let students jump to:

- SQL syntax comparisons
- "MongoDB is better" or "relational is better" claims
- choosing the simpler-looking document without update reasoning
- full implementation

Useful feedback patterns:

- Good: comparison is tied to access pattern, duplication risk is named, recommendation includes a tradeoff, both document options are inspectable.
- Improvements: options are nearly identical, relational comparison is superficial, update responsibility is ignored, recommendation is unsupported.
- Suggestions: make Option B meaningfully different, identify stale data risk, explain when the table-shaped model would still fit, add a boundary question.


