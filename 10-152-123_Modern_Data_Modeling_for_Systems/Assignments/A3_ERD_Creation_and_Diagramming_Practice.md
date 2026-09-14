# ASSIGNMENT A3 - ERD CREATION AND DIAGRAMMING PRACTICE

**Week 3 - Visual Model Communication**

---

# Context

A relational structure becomes easier to inspect when it is shown visually.

In this assignment, you will convert your Week 2 relational structure into an ERD that another person can read, question, and discuss. The purpose is not to make a decorative diagram. The purpose is to show entities, key attributes, relationships, cardinality, and assumptions clearly.

You will practice draw.io / diagrams.net during lab. Your instructor may allow another ERD-capable tool.

You are not writing SQL for this assignment.

---

# Objective

Create a readable ERD from your Week 2 relational structure.

Your work should demonstrate:

- entities with clear names
- key attributes
- important non-key attributes
- relationship lines
- cardinality decisions
- documented assumptions
- a readable exported diagram

---

# Task

Use your Week 2 relational structure as the starting point.

Use the assignment template files in:

```text
Student_Submission_Templates/week_03/A3_erd_creation_and_diagramming_practice/
```

The main files for this assignment are:

```text
erd_diagramming_worksheet.md
erd_notation_readability_checklist.md
tool_alternatives_notes.md
```

You must also submit an ERD source file or exported diagram.

Recommended diagram filenames:

```text
erd_diagram.drawio
erd_diagram.png
```

---

# Assignment Workflow

Complete the assignment in one main pass during Week 3.

Your work should include:

1. A manual ERD planning table.
2. Cardinality and relationship decisions.
3. A layout plan before finalizing the diagram.
4. A completed ERD in draw.io or another approved tool.
5. A notation and readability checklist.
6. Tool notes explaining what you used.
7. A short README reflection.
8. AI assistance notes, if AI was used.

---

# Requirements

Your submission must include:

1. A completed `erd_diagramming_worksheet.md`.
2. A completed `erd_notation_readability_checklist.md`.
3. A completed `tool_alternatives_notes.md`.
4. An ERD source file or exported diagram.
5. Entities, key attributes, relationships, and cardinality.
6. At least three assumptions or scope decisions.
7. A short design rationale.
8. A short README reflection.
9. AI assistance notes, if AI was used.

Your ERD should be readable when opened outside the diagramming tool.

---

# Evidence Requirements

Required evidence files:

```text
README.md
erd_diagramming_worksheet.md
erd_notation_readability_checklist.md
tool_alternatives_notes.md
```

Required diagram evidence:

```text
erd_diagram.drawio
erd_diagram.png
```

or another approved source/export format.

Required if AI was used:

```text
ai_assistance_notes.md
```

Your README should answer:

- What relationship was hardest to show visually?
- What assumption did you need to write down so the ERD made sense?
- What did the diagram reveal that was less obvious in your Week 2 tables?
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

Do not use AI until after you complete a manual ERD plan or draft.

Allowed AI uses:

- ask AI to critique your ERD plan
- ask AI to identify cardinality decisions to double-check
- ask AI to flag possible many-to-many relationships
- ask AI to suggest where an associative entity may be needed
- ask AI for readability feedback on your layout plan

Not allowed:

- asking AI to create the diagram for you
- submitting AI-generated ERD content without review
- using AI to bypass your own relationship decisions
- writing SQL

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
week_03/A3_erd_creation_and_diagramming_practice/
```

Your folder should include:

- `README.md`
- `erd_diagramming_worksheet.md`
- `erd_notation_readability_checklist.md`
- `tool_alternatives_notes.md`
- an ERD source/export file
- `ai_assistance_notes.md`, if AI was used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, image file, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> What did the ERD make clearer than your Week 2 tables?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T2 - ERD Design and Model Communication**
- **C2 - Communicate Clearly**

## Secondary Rubric Focus

- **C3 - Work Productively**
- **T1 - Data Modeling Foundations**

## Optional / Light Focus

- **T3 - Relational Modeling and Data Integrity**
- **T6 - Modeling Defense and AI-Assisted Design Practice**
- **C1 - Solve Problems**
- **C4 - Value Learning**
- **C6 - Act Professionally**

## Not Evaluated

- **T4 - Document Modeling and Representation Choice**
- **T5 - MongoDB Operations as Model Evidence**
- **C5 - Work Cooperatively**, unless a peer activity is assigned

---

# Success Criteria

Successful work:

- starts from the Week 2 relational structure
- shows entities and key attributes clearly
- connects relationships to the correct entities
- shows or labels cardinality
- documents assumptions and unclear decisions
- uses a tool export that another person can inspect
- improves the diagram after a notation/readability check
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should treat diagramming as model communication, not tool decoration.

The key teaching target is:

```text
relational structure -> ERD plan -> cardinality decisions -> visual layout -> readability review -> diagram evidence
```

Do not let students jump to:

- SQL
- tool features that hide the modeling decisions
- over-decorated diagrams
- unexamined many-to-many relationships

Useful feedback patterns:

- Good: readable diagram layout, clear cardinality labels, key assumptions documented, relationship lines match Week 2 reasoning.
- Improvements: missing key attributes, unclear cardinality, crossed lines that obscure meaning, diagram does not match the worksheet.
- Suggestions: simplify the layout, move related entities closer together, explain one assumption near the diagram, revisit one many-to-many relationship.


