Excellent—this is where your system becomes **AI-augmented in a controlled, defensible way**.

What follows is a **production-ready grading prompt framework (GPT-01)** you can reuse for every assignment.

This is designed to:

* reduce grading time
* maintain rubric integrity (MRS-02)
* avoid hallucination
* preserve instructor authority
* work cleanly with Schoology

---

# 🧭 AI GRADING PROMPT TEMPLATE (GPT-01)

---

# 🔹 PURPOSE

Use AI to:

* generate **first-pass scores**
* produce **rubric-aligned rationale**
* draft **student feedback**

NOT to replace instructor judgment.

---

# 🧱 INPUT STRUCTURE (YOU PROVIDE)

You will paste the following sections into the AI:

---

## 1. Assignment Context

```
Assignment Name: [e.g., Assignment 5 – Interactive Page]

Objective:
[Short description of what students were expected to build]

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
```

---

## 2. Student Submission

```
[Paste code, link, or description of submission]

If link:
- summarize what is observable
- include any screenshots if needed
```

---

## 3. Instructor Observation Notes (CRITICAL for Core Abilities)

```
(Optional but recommended)

- Pair programming behavior:
- Participation level:
- Zoom professionalism:
- Use of AI/resources:
- Notable issues or strengths:
```

---

## 4. Rubric (MRS-02 Summary)

```
Technical Categories (score 0–4):
- Structure (HTML)
- Styling & Layout (CSS)
- Interactivity (JavaScript)
- Debugging & Problem Solving
- Structured Development

Core Abilities (score 0–4, only if evidence exists):
- Solve Problems
- Communicate Clearly
- Work Productively
- Value Learning
- Work Cooperatively
- Act Professionally
```

---

# 🧱 AI INSTRUCTION BLOCK (COPY EXACTLY)

This is the *most important part*.

---

```
You are evaluating a student assignment using a structured rubric.

STRICT RULES:
1. Score ONLY based on observable evidence.
2. Do NOT assume intent or understanding.
3. If evidence is missing, state "Insufficient Evidence" instead of guessing.
4. Be consistent and conservative in scoring.
5. Default to score = 3 (Meets) if functional and correct, unless strong evidence supports 4 or lower score is clearly justified.

SCORING SCALE:
4 = Exceeds (correct, intentional, well-structured)
3 = Meets (functional, minor issues)
2 = Developing (partial, inconsistent)
1 = Needs Improvement (broken or unclear)
0 = Missing

TASK:

1. Evaluate each TECHNICAL category:
- Provide score (0–4)
- Provide 1–2 sentence justification based ONLY on observable evidence

2. Evaluate CORE ABILITIES:
- Only score categories supported by observation notes
- If not supported, write "Insufficient Evidence"
- Provide brief justification

3. Identify:
- 2–3 strengths
- 2–3 areas for improvement

4. Generate a short student feedback paragraph:
- Clear, constructive, aligned with rubric

5. Flag uncertainty:
- List any categories where evidence was unclear or incomplete

OUTPUT FORMAT:

TECHNICAL SCORES:
[Category]: Score — Justification

CORE ABILITIES:
[Category]: Score or "Insufficient Evidence" — Justification

STRENGTHS:
- ...
- ...

AREAS FOR IMPROVEMENT:
- ...
- ...

STUDENT FEEDBACK:
[Paragraph]

UNCERTAINTIES:
- ...
```

---

# 🧠 WHY THIS WORKS

This prompt enforces:

### ✔ Evidence-based grading

Prevents hallucination

### ✔ Controlled scoring

Defaults to 3 unless justified

### ✔ Safe Core Ability handling

No guessing without observation

### ✔ Consistency

Same structure every time

---

# 🔥 BEST PRACTICE WORKFLOW

---

## Step 1 — Run AI Evaluation

Paste:

* assignment
* submission
* rubric
* notes

---

## Step 2 — Review (30–60 seconds)

You check:

* Does scoring match reality?
* Any over/under scoring?
* Any missing nuance?

---

## Step 3 — Adjust + Finalize

* Enter into Schoology
* Use AI feedback (edit if needed)

---

# ⚠️ IMPORTANT GUARDRAILS

---

## DO NOT:

* blindly accept AI scores
* allow AI to infer behavior
* skip observation notes for Core Abilities

---

## ALWAYS:

* verify edge cases
* adjust when intuition flags something
* override when needed

---

# 🧭 OPTIONAL ENHANCEMENTS

---

## 🔹 Add Calibration Prompt (Occasionally)

To keep consistency across students:

```
Compare this evaluation to a typical "3-level" assignment.
Is this student above, equal, or below that standard?
Adjust if needed.
```

---

## 🔹 Batch Grading Mode

You can:

* reuse same prompt
* swap only submission + notes
* maintain consistency across class

---

# 🔑 FINAL INSIGHT

You’ve now built something rare:

> A **human-defined grading system** that is **AI-executable but not AI-dependent**

---

# 🧭 ONE-LINE SUMMARY

> “AI proposes. Instructor confirms.”

---

# 🚧 If You Want Next Level

I can also build:

* **Schoology comment auto-format (copy/paste ready)**
* **Batch grading template**
* **Rubric calibration examples (what a 2 vs 3 vs 4 looks like)**

But this GPT-01 is already **fully usable in your workflow today**.
