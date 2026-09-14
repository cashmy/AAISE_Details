# ASSIGNMENT A6 - BUSINESS RULES AND PERFORMANCE TRADEOFFS

**Week 5 - Rule Placement and Modeling Consequences**

---

# Context

Data models do not only store information. They also influence where rules can be enforced and where tradeoffs appear.

In this assignment, you will identify business rules in your scenario, decide where those rules might belong, and consider one performance or denormalization tradeoff.

You are not implementing the rules. You are reasoning about responsibility and consequences.

You are not writing SQL for this assignment.

---

# Objective

Explain rule placement decisions and one responsible performance tradeoff.

Your work should demonstrate:

- plain-English business rules
- rule placement reasoning
- risks or limitations of placement decisions
- one access pattern that could create pressure
- one performance or denormalization tradeoff
- a human design question before accepting the tradeoff

---

# Task

Use your current model and scenario.

Use the assignment template files in:

```text
Student_Submission_Templates/week_05/A6_business_rules_and_performance_tradeoffs/
```

The main file for this assignment is:

```text
rule_placement_tradeoff_worksheet.md
```

---

# Requirements

Your submission must include:

1. A completed `rule_placement_tradeoff_worksheet.md`.
2. A short scenario reminder.
3. At least three business rules in plain English.
4. A completed rule placement table.
5. One access pattern that could create performance pressure.
6. One performance or denormalization tradeoff.
7. A recommendation to accept, reject, or defer the tradeoff.
8. One human governor question.
9. A short README reflection.
10. AI assistance notes, if AI was used.

Optional:

- marked-up ERD, model annotation, note, or screenshot

---

# Evidence Requirements

Required evidence files:

```text
README.md
rule_placement_tradeoff_worksheet.md
```

Required if AI was used:

```text
ai_assistance_notes.md
```

Optional:

```text
model_annotation
```

Your README should answer:

- Which business rule was hardest to place?
- What performance pressure did you identify?
- What tradeoff are you recommending or rejecting?
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

Do not use AI until after you complete your manual rule placement table and access pattern note.

Allowed AI uses:

- ask AI to critique your rule placement choices
- ask AI to identify a rule that may need mixed enforcement
- ask AI to point out what could go wrong with a placement decision
- ask AI to question whether a tradeoff is worth considering
- ask AI to suggest a human design question

Not allowed:

- asking AI to implement the rules
- asking AI to write SQL
- asking AI to create backend code
- replacing your rule placement decisions with AI output

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
week_05/A6_business_rules_and_performance_tradeoffs/
```

Your folder should include:

- `README.md`
- `rule_placement_tradeoff_worksheet.md`
- `ai_assistance_notes.md`, if AI was used
- optional model annotation, if used

Schoology may be used to submit a GitHub link, confirmation message, exported PDF, image file, or other item requested by your instructor.

---

# Reflection / Explanation

Answer briefly in your `README.md`:

> Which rule placement or tradeoff decision required the most judgment?

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

- states business rules in plain English
- separates rule placement from implementation
- explains why each rule belongs where it was placed
- identifies one access pattern that could create pressure
- explains one tradeoff and its risk
- recommends accepting, rejecting, or deferring the tradeoff
- includes a human design question
- discloses AI use if AI was used

---

# Instructor Notes

This assignment should help students see that model design includes responsibility decisions, not just entity lists.

The key teaching target is:

```text
business rule -> placement choice -> placement risk -> access pressure -> tradeoff -> human governor question
```

Do not let students jump to:

- SQL
- backend implementation
- advanced performance tuning
- treating denormalization as automatically good or bad

Useful feedback patterns:

- Good: rules are plain-English and specific, placement reasoning is defensible, tradeoff includes both benefit and risk.
- Improvements: rules are too vague, placement is asserted without reason, access pattern is not connected to the model, recommendation ignores consequences.
- Suggestions: choose one rule to analyze more deeply, name what could go wrong, defer a tradeoff if evidence is weak, add a human policy question.


