# ASSIGNMENT A2 - RELATIONAL STRUCTURE AND PROCESS MAPPING

**Week 2 - Relational Structure Before SQL**

---

# Context

Relational modeling is not the same as writing SQL.

In this assignment, you will take the conceptual model you started in Week 1 and reshape it into a clearer relational structure. You will identify entities, attributes, key candidates, relationship links, and plain-language integrity constraints.

Then you will test that structure against system actions to see whether the model supports what the system needs to do.

You are not writing SQL and you are not creating a formal ERD yet.

---

# Objective

Create an early relational structure and revise it using process evidence.

Your work should demonstrate:

- entities with attributes and purpose
- reasonable primary key candidates
- relationship links between entities
- plain-language integrity constraints
- a process-to-data map
- one revision based on how the system would use the data

---

# Task

Continue with your approved Week 1 scenario unless your instructor approves a change.

Use the assignment template files in:

```text
Student_Submission_Templates/week_02/A2_relational_structure_and_process_mapping/
```

The main file for this assignment is:

```text
relational_structure_worksheet.md
```

---

# Tuesday Checkpoint - Manual Relational Structure

Complete Sections 1-4 of `relational_structure_worksheet.md`.

Your Tuesday checkpoint should include:

1. Your selected scenario.
2. A brief reminder of system intent.
3. Week 1 entities and open questions you are carrying forward.
4. An entity / attribute / key table.
5. A relationship link table.
6. Plain-language integrity constraints.

This checkpoint should be completed manually before AI is used.

---

# Friday Final Submission - Process-to-Data Revision

Complete Sections 5-8 of `relational_structure_worksheet.md`.

Your Friday final submission should add:

1. A process-to-data map.
2. At least one process-driven revision note.
3. One remaining modeling question.
4. A final check confirming that you stayed at the structure and reasoning level.

---

# Requirements

Your submission must include:

1. A completed `relational_structure_worksheet.md`.
2. A clear connection to your Week 1 conceptual model.
3. An entity / attribute / key table.
4. A relationship link table.
5. Plain-language integrity constraints.
6. A process-to-data map.
7. A process-driven revision note.
8. A short README reflection.
9. AI assistance notes, if AI was used.

Optional:

- `optional_relational_sketch.md`

The optional sketch may be a rough text or Mermaid sketch. It is not a formal ERD.

---

# Evidence Requirements

Your evidence should show your first relational structure and your process-driven revision.

Required evidence files:

```text
README.md
relational_structure_worksheet.md
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Optional:

```text
optional_relational_sketch.md
```

Your README should answer:

- What changed from your Week 1 conceptual model?
- Which entity or relationship was hardest to clarify?
- What did the process-to-data map reveal?
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

Do not use AI until after you complete Sections 1-4 of `relational_structure_worksheet.md`.

Allowed AI uses:

- ask AI to critique your key choices
- ask AI to identify missing relationship links
- ask AI to look for misplaced attributes
- ask AI to question unclear relationship types
- ask AI to suggest plain-language constraints

Not allowed:

- asking AI to complete the assignment for you
- asking AI to write SQL
- submitting AI output without review
- accepting AI relationship changes without explaining your decision

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
week_02/A2_relational_structure_and_process_mapping/
```

Your folder should include:

- `README.md`
- `relational_structure_worksheet.md`
- `ai_assistance_notes.md`, if AI was used
- `optional_relational_sketch.md`, if used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> What did the process-to-data map reveal about your relational structure?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T3 - Relational Modeling and Data Integrity**
- **C1 - Solve Problems**

## Secondary Rubric Focus

- **T1 - Data Modeling Foundations**
- **C2 - Communicate Clearly**

## Optional / Light Focus

- **T2 - ERD Design and Model Communication**
- **T6 - Modeling Defense and AI-Assisted Design Practice**
- **C3 - Work Productively**
- **C4 - Value Learning**
- **C6 - Act Professionally**

## Not Evaluated

- **T4 - Document Modeling and Representation Choice**
- **T5 - MongoDB Operations as Model Evidence**
- **C5 - Work Cooperatively**, unless a peer activity is assigned

---

# Success Criteria

Successful work:

- carries forward the Week 1 model without simply replacing it
- separates entities from attributes
- identifies reasonable key candidates
- describes relationship links in clear language
- states integrity constraints without SQL
- maps system actions to the data they require
- revises the model based on process evidence
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should help students move from concept-first modeling into relational structure without turning the work into SQL.

The key teaching target is:

```text
conceptual model -> attributes and keys -> relationship links -> constraints -> process-to-data map -> focused revision
```

Do not let students jump to:

- SQL syntax
- formal ERD notation as the primary deliverable
- fully normalized schema design
- implementation details

Useful feedback patterns:

- Good: clear relationship links, purposeful key candidates, process map reveals data needs, constraints written plainly.
- Improvements: attributes treated as entities, vague key candidates, process map not connected to revision, SQL syntax appearing in the model.
- Suggestions: test one system action more carefully, clarify one relationship type, add one missing constraint, preserve boundary questions for later weeks.


