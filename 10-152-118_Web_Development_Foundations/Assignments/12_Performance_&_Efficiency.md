# 🧭 ASSIGNMENT 12 — PERFORMANCE & EFFICIENCY

**Week 12 — “Making It Efficient”**

---

## 🔹 Context

Your application now:

* responds to user input
* manages data and state
* updates dynamically

This week focuses on improving **how efficiently your application runs**.

Performance is not only about speed. It also includes how much work the browser
has to do, how large files are, and whether the page asks the user or browser to
handle too much at once.

---

## 🔹 Objective

Improve your application by:

* identifying inefficient behavior
* reducing unnecessary work
* making updates more intentional and efficient

---

# 🧱 ITERATION 1 — BUILD (Tuesday Lab)

### 🔹 Task

Identify and improve at least one inefficient part of your application.

---

### 🔹 Requirements

You must:

* Identify at least **1 area of inefficiency**, such as:

  * repeated DOM updates
  * unnecessary function calls
  * redundant calculations
  * images or files that are larger than needed
  * displaying too many items at one time when a smaller set would be clearer
  * repeated input or scroll behavior that could be controlled more carefully

* Implement an improvement that:

  * reduces unnecessary work
  * improves responsiveness or clarity

Possible improvements include:

* simplifying repeated logic
* updating the page fewer times
* using smaller or better-sized images
* showing a smaller group of items instead of everything at once
* applying a basic debounce/throttle pattern if it fits your feature

---

### 🔹 Focus

* observing behavior
* recognizing repetition
* thinking about cost of operations

---

### 🔹 Expectation

Inefficiency may not be obvious at first.

That is normal.

---

# 🧠 CONCEPT FOCUS (Wednesday)

* What “performance” means in a web application
* The idea that some operations cost more than others
* Repetition vs efficiency
* Basic awareness of scaling (doing something once vs many times)
* Thinking about performance without overcomplicating it
* Why file size, repeated events, and too much visible information can affect user experience
* Pagination or chunking as a design choice, not necessarily a programming requirement this week

---

# 🔧 ITERATION 2 — REFINE (Thursday Lab)

### 🔹 Task

Improve your optimization and clarify your changes.

---

### 🔹 Requirements

* Ensure:

  * your optimization works correctly
  * functionality is preserved

* Improve:

  * clarity of your logic
  * structure of your optimized code

* Clearly document:

  * what was inefficient
  * what you changed
  * why it is better

---

### 🔹 Focus

* intentional improvement
* preserving correctness
* clarity of reasoning

---

# 📦 FINAL SUBMISSION

Submit:

* your updated website (HTML, CSS, JS)
* a short performance note

---

### 🔹 Performance Note Requirements

In 2–4 sentences:

* What was inefficient?
* What did you change?
* Why is your solution better?

Your note may refer to repeated work, image/file size, the amount of content
shown at once, debounce/throttle, or another practical improvement discussed in
the Week 12 handout.

---

# 🧠 REFLECTION (Required — Short)

In 2–3 sentences, answer:

> How did thinking about efficiency change the way you approach writing your code?

---

# 📊 EVALUATION

---

### 🔹 Primary Focus

* **T1 - Structured Development**
* **T4 - Debugging & Problem Solving**

---

### 🔹 Secondary Focus

* **T3 - Interactivity (JavaScript)**
* **C1 - Solve Problems**
* **C4 - Value Learning**

---

### 🔹 Emerging

* System thinking (refinement level)

---

# 🔑 SUCCESS CRITERIA (STUDENT-FRIENDLY)

To succeed on this assignment:

* you must identify a real inefficiency
* your improvement must reduce unnecessary work
* your application must still function correctly
* you must clearly explain your change
* your explanation must connect the change to user experience, browser work, or both

---

# 🔥 Instructor Notes (For You)

Students often:

* think optimization = “make it faster” without clarity
* overcomplicate simple improvements
* struggle to identify inefficiency

Your role:

* keep it practical
* emphasize *small, meaningful improvements*
* avoid deep theory

---

# 🧠 Subtle Concept Being Installed

> “Not all solutions are equal—some are more efficient than others.”

---

# 🔑 (Optional Light Tie-In — Big O Awareness)

You may lightly introduce:

> “If something runs once, it’s simple.
> If it runs many times, cost increases.”

No formal notation needed.

---

