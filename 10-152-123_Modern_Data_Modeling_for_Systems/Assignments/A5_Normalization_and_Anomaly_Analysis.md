# ASSIGNMENT A5 - NORMALIZATION AND ANOMALY ANALYSIS

**Week 5 - Maintenance Risk and Responsible Structure**

---

# Context

A model can look organized and still create maintenance problems.

In this assignment, you will review a focused excerpt from your current model and look for repeated facts, mixed facts, or risky structures. You will explain whether normalization would help and make one focused recommendation.

You are not redesigning the whole model.

You are not writing SQL for this assignment.

---

# Objective

Identify a maintenance risk and explain a responsible structural improvement.

Your work should demonstrate:

- a focused model excerpt
- repeated or mixed facts
- possible update, insert, delete, or other maintenance risks
- normalization awareness
- a structural recommendation
- a tradeoff created by that recommendation

---

# Task

Use your current model or an instructor-approved excerpt.

Use the assignment template files in:

```text
Student_Submission_Templates/week_05/A5_normalization_and_anomaly_analysis/
```

The main file for this assignment is:

```text
anomaly_analysis_worksheet.md
```

---

# Requirements

Your submission must include:

1. A completed `anomaly_analysis_worksheet.md`.
2. A model excerpt or clear description of the structure reviewed.
3. Notes on repeated or mixed facts.
4. At least one possible anomaly or maintenance risk.
5. An explanation of what causes the risk.
6. An explanation of whether normalization would help.
7. One focused structural recommendation.
8. A tradeoff or risk created by the recommendation.
9. A short README reflection.
10. AI assistance notes, if AI was used.

Optional:

- marked-up model evidence, ERD annotation, model excerpt, or screenshot

---

# Evidence Requirements

Required evidence files:

```text
README.md
anomaly_analysis_worksheet.md
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Optional:

```text
marked_up_model_evidence
```

Your README should answer:

- What maintenance risk did you find?
- What caused the risk?
- What recommendation are you making?
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

Do not use AI until after you complete your manual anomaly/risk table.

Allowed AI uses:

- ask AI to critique your anomaly labels
- ask AI to identify a likely missed risk
- ask AI to question whether normalization would help
- ask AI to point out a risk of over-normalizing
- ask AI to critique your recommendation

Not allowed:

- asking AI to redesign the whole model
- asking AI to write SQL
- replacing your analysis with AI output
- forcing anomaly types that do not honestly fit

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
week_05/A5_normalization_and_anomaly_analysis/
```

Your folder should include:

- `README.md`
- `anomaly_analysis_worksheet.md`
- `ai_assistance_notes.md`, if AI was used
- optional marked-up model evidence, if used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, image file, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> What maintenance risk did you find, and why does it matter?

If you used AI:

> What did AI help you notice, and what decision remained yours?

---

# Evaluation Focus

This assignment is aligned to `MRS-DM_Master_Rubric_System_v2.md`.

## Primary Rubric Focus

- **T3 - Relational Modeling and Data Integrity**
- **C1 - Solve Problems**

## Secondary Rubric Focus

- **C2 - Communicate Clearly**

## Optional / Light Focus

- **T1 - Data Modeling Foundations**
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

- reviews a focused model excerpt
- identifies a real maintenance risk
- explains what causes the risk
- connects normalization to model quality
- avoids unnecessary redesign
- recommends one focused improvement
- names a tradeoff or risk
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should make normalization concrete by tying it to maintenance risk.

The key teaching target is:

```text
model excerpt -> repeated or mixed facts -> anomaly risk -> normalization awareness -> focused recommendation
```

Do not let students jump to:

- SQL
- complete schema redesign
- memorized normal-form definitions without model evidence
- forcing all anomaly types when only one risk is visible

Useful feedback patterns:

- Good: risk is specific, cause is explained, recommendation is focused, tradeoff is acknowledged.
- Improvements: anomaly label is vague, model excerpt is too broad, recommendation redesigns too much, normalization claim is unsupported.
- Suggestions: narrow the excerpt, identify the fact being repeated, explain what could go wrong over time, name one risk of over-normalizing.


