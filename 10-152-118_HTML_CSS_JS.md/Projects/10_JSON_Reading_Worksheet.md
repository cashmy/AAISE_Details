# 🧭 WEEK 10 — JSON READING WORKSHEET

**Learning to Understand Data Before Using It**

---

## 🔹 Purpose

This worksheet will help you learn how to:

* read JSON data
* understand its structure
* extract specific values

> Before you can use data, you must understand what it looks like.

---

# 🧱 PART 1 — What Is JSON?

JSON (JavaScript Object Notation) is a way of organizing data.

It is built from:

* **objects** → collections of key/value pairs
* **arrays** → lists of items

---

## 🔹 Example JSON

```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": true,
  "skills": ["HTML", "CSS", "JavaScript"]
}
```

---

## 🔍 Your Task

Answer the following:

1. What is the value of `"name"`?
2. What type of data is `"age"`?
3. How many items are in `"skills"`?
4. What is the second skill?

---

# 🧱 PART 2 — Objects vs Arrays

---

## 🔹 Example

```json
{
  "users": [
    { "name": "Alice", "age": 25 },
    { "name": "Bob", "age": 30 }
  ]
}
```

---

## 🔍 Your Task

1. Is `"users"` an object or an array?
2. How many users are there?
3. What is the name of the first user?
4. What is the age of the second user?

---

# 🧱 PART 3 — Nested Data

---

## 🔹 Example

```json
{
  "user": {
    "name": "Alice",
    "address": {
      "city": "Chicago",
      "zip": "60601"
    }
  }
}
```

---

## 🔍 Your Task

1. What is the user’s name?
2. What city does the user live in?
3. How would you describe the structure of `"address"`?

---

# 🧱 PART 4 — From JSON to JavaScript

---

## 🔹 Example Data (from an API)

```json
[
  {
    "name": "Leanne Graham",
    "email": "leanne@example.com"
  },
  {
    "name": "Ervin Howell",
    "email": "ervin@example.com"
  }
]
```

---

## 🔍 Your Task

Write the JavaScript expression to access:

1. The name of the first user
2. The email of the second user

---

# 🧱 PART 5 — Real API Observation

---

## 🔹 Step 1

Open this URL in your browser:

[https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)

---

## 🔹 Step 2

Look at the data and answer:

1. Is the top-level structure an object or an array?
2. How many users are returned?
3. What keys exist for each user? (list at least 3)

---

## 🔹 Step 3

Find:

* one user’s name
* their email
* their company name

---

# 🧱 PART 6 — Think Before You Code

Before writing any JavaScript, answer:

1. What does the data look like?
2. Where is the value you want located?
3. Is it inside an array or an object?
4. What steps are needed to reach it?

---

## 🔑 Rule

> If you cannot answer these questions, you are not ready to write code yet.

---

# 🧠 Reflection (Short)

In 2–3 sentences:

> How did understanding the structure of JSON help you think differently about using data?

---

# 🔥 Final Reminder

When working with APIs:

1. **Look at the data first**
2. **Understand the structure**
3. **Then write code**

---

> “The problem is rarely the code—it’s not understanding the data.”

---

## 🧠 Why This Is So Effective (Instructor Lens)

This worksheet quietly installs:

* **data-first thinking**
* **structure before syntax**
* **intentional access vs guessing**

It also directly combats:

* random console logging without purpose
* trial-and-error property access
* “why is this undefined” confusion

---

## 🧭 If You Want to Push This Further

Two powerful extensions:

### 1. “Break It” Version (Advanced)

Give them incorrect access patterns and ask:

> “Why does this return undefined?”

### 2. Pair Programming Mode

* Driver = writes answers
* Navigator = explains structure out loud

---

If you want, I can also generate:

* an **answer key (clean + instructor annotated)**
* or a **graded rubric tie-in for this worksheet**

Both would integrate cleanly into your MRS-02 system.
