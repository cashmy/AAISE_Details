# 🧭 WEEK 10 — JSON WORKSHEET ANSWER KEY

**Instructor Version (Annotated)**

---

## 🧱 PART 1 — Basic Object

### Answers

1. `"Alice"`
2. Number
3. 3
4. `"CSS"`

---

### 🧠 Instructor Notes

* Watch for:

  * students saying `"age"` is a string → confusion about types
  * indexing mistakes (`skills[2]` instead of `[1]`)

* This section checks:

  > Do they understand **key/value + arrays basics**?

---

## 🧱 PART 2 — Objects vs Arrays

### Answers

1. Array
2. 2
3. `"Alice"`
4. `30`

---

### 🧠 Instructor Notes

* Most common error:

  * treating `"users"` like an object instead of an array

* Diagnostic signal:

  * If they miss this → they will struggle heavily with APIs

---

## 🧱 PART 3 — Nested Data

### Answers

1. `"Alice"`
2. `"Chicago"`
3. `"address"` is an object inside another object (nested object)

---

### 🧠 Instructor Notes

* Watch for:

  * skipping levels (trying to jump directly to `city`)

* This is the **first real friction point**
  → Good students slow down here

---

## 🧱 PART 4 — JSON → JavaScript

### Answers

1. `data[0].name`
2. `data[1].email`

---

### 🧠 Instructor Notes

* Common errors:

  * `data.name` (ignores array)
  * `data[1][email]` (syntax confusion)

* This section tests:

  > Can they **translate structure into access paths**?

---

## 🧱 PART 5 — Real API Observation

### Answers

1. Array
2. 10 (typical response from JSONPlaceholder)
3. Examples of keys:

   * `name`
   * `email`
   * `address`
   * `company`

---

### Step 3 Answers (Example)

* Name → `"Leanne Graham"`
* Email → `"Sincere@april.biz"`
* Company → `"Romaguera-Crona"`

---

### 🧠 Instructor Notes

* This is the **most important section**

Watch for:

* students overwhelmed by structure
* students scanning instead of reading

---

## 🧱 PART 6 — Thinking Before Coding

### Expected Responses (Conceptual)

1. Description of structure (array of objects)
2. Identification of where value exists
3. Correct identification (array vs object)
4. Step-by-step access path

---

### 🧠 Instructor Notes

This section is **not about correctness—it’s about thinking clarity**.

Strong responses:

* explicit
* step-by-step
* structured

Weak responses:

* vague
* “I just get it”
* skipping reasoning

---

# 🔥 Instructor Meta-Signal

You can group students immediately:

---

## 🟢 Strong

* correct structure identification
* correct access patterns
* clear reasoning

---

## 🟡 Developing

* mostly correct but inconsistent
* occasional confusion

---

## 🔴 At Risk

* cannot distinguish object vs array
* cannot form access path
* guessing

---

# 🧠 Critical Decision Rule

> Students in 🔴 group should NOT proceed to full API work without support.

---

# 🔑 Final Reminder

> If they cannot read JSON, they cannot use APIs.

This worksheet is your **early warning system**.
