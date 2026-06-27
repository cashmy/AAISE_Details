# 🧭 ASSIGNMENT 13 — SECURITY & RELIABILITY

**Week 13 — “Building Safely”**

---

## 🔹 Context

Your application now:

* responds to user input
* manages data and state
* performs efficiently

This week focuses on making your application **safe, predictable, and reliable**.

This is security awareness for a front-end web project. You are not expected to
build real authentication, server security, or a complete secure system. The goal
is to recognize risky patterns and use safer beginner-level habits.

---

## 🔹 Objective

Improve your application by:

* handling input more carefully
* preventing unexpected or incorrect behavior
* making your system more reliable

---

# 🧱 ITERATION 1 — BUILD (Tuesday Lab)

### 🔹 Task

Identify and address potential risks in your application.

---

### 🔹 Requirements

You must:

* Identify at least **2 potential issues**, such as:

  * invalid or unexpected user input
  * missing or undefined data
  * actions that break your application
  * user input being displayed in an unsafe way
  * assuming browser storage is private or secure
  * confusing a simulated login with real authentication
  * API or cross-origin behavior that may fail or be blocked

* Implement protections, such as:

  * input validation
  * conditional checks
  * default/fallback values
  * safer output techniques, such as using text content instead of injecting raw HTML
  * clear messages when input cannot be used
  * comments or notes that identify what is simulated or not secure

---

### 🔹 Focus

* anticipating problems
* controlling input
* preventing failure

---

### 🔹 Expectation

You may not catch every issue immediately.

That is expected.

---

# 🧠 CONCEPT FOCUS (Wednesday)

* Why user input cannot always be trusted
* The importance of validation and checking data
* Common failure points in applications
* Defensive programming (planning for what might go wrong)
* Building systems that fail gracefully instead of breaking
* XSS, CSRF, and CORS as awareness terms for browser-based projects
* Why simulated login is useful for practice but is not real account security
* Why "it works" is not the same as "it is safe"

---

# 🔧 ITERATION 2 — REFINE (Thursday Lab)

### 🔹 Task

Improve your safeguards and reliability.

---

### 🔹 Requirements

* Ensure:

  * your protections work consistently
  * your application does not break with unexpected input

* Improve:

  * clarity of validation logic
  * user feedback when something is incorrect

* Add at least:

  * one improvement that makes your system more robust

---

### 🔹 Focus

* predictability
* resilience
* clear behavior under edge cases

---

# 📦 FINAL SUBMISSION

Submit:

* your updated website (HTML, CSS, JS)
* a short reliability note

---

### 🔹 Reliability Note Requirements

In 2–4 sentences:

* What issue did you identify?
* What could go wrong?
* What did you add to prevent it?

At least one note should connect your improvement to the Week 13 browser
security handout, such as safer input/output handling, trust boundaries, XSS
awareness, CORS/API awareness, or simulated login limitations.

---

# 🧠 REFLECTION (Required — Short)

In 2–3 sentences, answer:

> How did thinking about “what could go wrong” change how you approached your code?

---

# 📊 EVALUATION (MRS-02 ALIGNED)

---

### 🔹 Primary Focus

* **T4 - Debugging & Problem Solving**
* **T5 - Structured Development**

---

### 🔹 Secondary Focus

* **T3 - Interactivity (JavaScript)**
* **C1 - Solve Problems**
* **C4 - Value Learning**

---

### 🔹 Emerging

* System thinking (risk awareness)

---

# 🔑 SUCCESS CRITERIA (STUDENT-FRIENDLY)

To succeed on this assignment:

* you must identify real risks in your application
* your application must handle unexpected input safely
* your system must remain stable under different conditions
* you must clearly explain your improvements
* you must avoid claiming that a front-end-only login is secure authentication

---

# 🔥 Instructor Notes (For You)

Students often:

* assume input will always be correct
* overlook edge cases
* struggle to think about failure conditions

Your role:

* encourage “what if?” thinking
* reward prevention, not just fixes
* keep it practical (not theoretical security)

---

# 🧠 Subtle Concept Being Installed

> “Good systems don’t just work—they handle problems gracefully.”

---

