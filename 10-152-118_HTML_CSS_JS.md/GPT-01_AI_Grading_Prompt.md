Excellent—this is where your system becomes *AI-augmented without losing integrity*.

What I’m giving you here is a **production-ready grading prompt template (GPT-01)** designed specifically for:

* your **MRS-02**
* your **Instructor Scoring Guide (ISG-01)**
* **Schoology workflow**
* **low hallucination risk**
* **defensible outputs**

---

# 🧭 AI GRADING PROMPT TEMPLATE (GPT-01)

---

## 🔹 PURPOSE

Use AI to:

* generate **first-pass rubric scores**
* produce **evidence-based rationale**
* draft **student feedback**
* flag **uncertainty**

---

# 🧱 CORE PRINCIPLE (Embed This Always)

> **Score only what is directly observable. Do NOT infer intent, effort, or understanding unless explicitly evidenced.**

---

# 🧾 TEMPLATE (COPY / PASTE READY)

---

## 🔹 SYSTEM / ROLE INSTRUCTION

```
You are an instructional assistant grading student work using a structured rubric.

You must:
- Score strictly based on observable evidence
- Follow the rubric definitions exactly
- Avoid assumptions or inference
- Flag uncertainty when evidence is missing
- Be consistent and conservative in scoring

You are NOT the final grader. You are providing a first-pass evaluation for instructor review.
```

---

## 🔹 INPUT SECTION

### 1. Assignment Description

```
[PASTE ASSIGNMENT INSTRUCTIONS HERE]
```

---

### 2. Rubric (MRS-02)

```
[PASTE RELEVANT RUBRIC SECTIONS OR FULL RUBRIC]
```

---

### 3. Student Submission

```
[PASTE CODE / LINK / DESCRIPTION OF SUBMISSION]
```

---

### 4. Instructor Observation Notes (OPTIONAL BUT IMPORTANT)

```
[PAIR PROGRAMMING NOTES, PARTICIPATION, PROFESSIONALISM, ETC.]

If not provided, DO NOT score those categories.
```

---

# 🧠 EVALUATION RULES

Include this every time:

```
Evaluation Rules:

1. Only score what is directly observable in the submission or notes.
2. If evidence is missing, mark the category as "Insufficient Evidence".
3. Do NOT assume correctness based on partial output.
4. If functionality is broken, score accordingly even if intent is clear.
5. Use the rubric language exactly when justifying scores.
6. Be consistent across all categories.
```

---

# 🧾 OUTPUT FORMAT (STRICT)

---

## 🔹 PART 1 — TECHNICAL SCORES

```
Structure (HTML): [0–4]
Reason:

Styling & Layout (CSS): [0–4]
Reason:

Interactivity (JavaScript): [0–4]
Reason:

Debugging & Problem Solving: [0–4]
Reason:

Structured Development: [0–4]
Reason:
```

---

## 🔹 PART 2 — CORE ABILITIES

```
Solve Problems: [0–4 or Insufficient Evidence]
Reason:

Communicate Clearly: [0–4 or Insufficient Evidence]
Reason:

Work Productively: [0–4 or Insufficient Evidence]
Reason:

Value Learning: [0–4 or Insufficient Evidence]
Reason:

Work Cooperatively: [0–4 or Insufficient Evidence]
Reason:

Act Professionally: [0–4 or Insufficient Evidence]
Reason:
```

---

## 🔹 PART 3 — UNCERTAINTY FLAGS

```
List any categories where:
- evidence was weak
- interpretation was uncertain
- assumptions might affect scoring
```

---

## 🔹 PART 4 — SUGGESTED STUDENT FEEDBACK

```
Write a concise feedback summary:

- 2–3 strengths
- 2–3 improvement areas
- Tie feedback to rubric categories
- Keep tone constructive and clear
```

---

## 🔹 PART 5 — INSTRUCTOR REVIEW NOTE

```
Provide 1–2 sentences indicating:
- where instructor attention is most needed
- any areas that should be manually verified
```

---

# 🔥 EXAMPLE (SHORT SNIPPET OUTPUT)

```
Interactivity (JavaScript): 3
Reason:
Basic interactivity works as expected. Event handling is functional, though logic is not fully optimized.

Debugging & Problem Solving: 2
Reason:
Student attempted fixes but did not fully resolve console errors. Limited evidence of systematic debugging.

Work Cooperatively: Insufficient Evidence
Reason:
No observation notes provided regarding pair programming participation.
```

---

# 🧭 HOW YOU WILL USE THIS (REAL WORKFLOW)

---

## 🔹 Step 1 — Run AI Evaluation

* Paste prompt
* Get structured output

---

## 🔹 Step 2 — Instructor Review (FAST)

* Scan scores
* Adjust if needed
* Focus on flagged areas

---

## 🔹 Step 3 — Enter in Schoology

* Use rubric clicks
* Copy feedback if useful

---

# ⚠️ IMPORTANT GUARDRAILS

---

## ❌ Do NOT:

* blindly accept AI scores
* let AI score professionalism without notes
* allow AI to infer understanding

---

## ✅ DO:

* treat AI as **assistant, not authority**
* use it to **accelerate, not replace judgment**
* rely on your **live observations for Core Abilities**

---

# 🧠 WHY THIS WORKS (WITH YOUR SYSTEM)

Because you already built:

* structured rubric (MRS-02)
* observable criteria
* assignment progression
* behavioral anchors

👉 AI now has **clear rails to operate within**

---

# 🔑 ONE-LINE SUMMARY

> **AI handles structure and consistency.
> You handle judgment and context.**

---

# 🚧 If You Want Next-Level

I can also create:

### 🔹 Batch grading workflow

* process multiple students efficiently

### 🔹 VS Code / local tool integration

* paste repo + auto-evaluate

### 🔹 Feedback-only version (no scoring)

### 🔹 “Strict mode” vs “lenient mode” prompts

---

But as it stands:

> You now have a **complete AI-assisted grading system layered on top of a fully defensible course architecture**

And that’s rare.
