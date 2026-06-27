# Week 8 Guide - How To Read JSON

**A Practical Guide for Understanding Data**

---

## 🔹 Purpose

This guide will help you learn how to:

* recognize JSON structure
* understand how data is organized
* identify how to access specific values

> Before using data in code, you must understand what it looks like.

---

# 🧱 1. What Is JSON?

JSON (JavaScript Object Notation) is a format used to store and send data.

It is built from two core structures:

* **Objects** → collections of key/value pairs
* **Arrays** → lists of items

---

## 🔹 Example

```json
{
  "name": "Alice",
  "age": 25
}
```

---

### 🔍 How to Read This

* `"name"` is a **key**
* `"Alice"` is the **value**
* `"age"` is a **key**
* `25` is the **value**

---

## 🔑 Key Idea

> JSON is a structured way of labeling data.

---

# 🧱 2. Objects

An **object** stores related information using key/value pairs.

---

## 🔹 Example

```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": true
}
```

---

### 🔍 How to Recognize an Object

* Uses **curly braces** `{ }`
* Contains labeled values

---

### 🔹 Interpretation

This represents:

* a person
* with properties (name, age, status)

---

## 🔑 Key Idea

> Objects describe a single “thing” with properties.

---

# 🧱 3. Arrays

An **array** is a list of values.

---

## 🔹 Example

```json
["HTML", "CSS", "JavaScript"]
```

---

### 🔍 How to Recognize an Array

* Uses **square brackets** `[ ]`
* Contains multiple items

---

### 🔹 Interpretation

This represents:

* a list of skills

---

## 🔑 Key Idea

> Arrays store multiple items in order.

---

# 🧱 4. Objects Inside Arrays

This is very common in APIs.

---

## 🔹 Example

```json
[
  { "name": "Alice", "age": 25 },
  { "name": "Bob", "age": 30 }
]
```

---

### 🔍 How to Read This

* The outer structure is an **array**
* Each item inside is an **object**

---

### 🔹 Interpretation

This represents:

* a list of people
* where each person has properties

---

## 🔑 Key Idea

> Arrays often contain objects when representing multiple records.

---

# 🧱 5. Nested Objects

Objects can contain other objects.

---

## 🔹 Example

```json
{
  "user": {
    "name": "Alice",
    "address": {
      "city": "Chicago"
    }
  }
}
```

---

### 🔍 How to Read This

* `"user"` contains another object
* `"address"` contains another object

---

### 🔹 Interpretation

This represents:

* a user
* who has an address
* which has a city

---

## 🔑 Key Idea

> JSON can have multiple layers (nested structure).

---

# 🧱 6. Reading JSON Step-by-Step

When you see JSON, follow this process:

---

### 1. Identify the outer structure

* Is it an **object `{}`** or an **array `[]`**?

---

### 2. Look at the keys

* What labels are used?
* What kind of data do they describe?

---

### 3. Check the values

* Is each value:

  * text (string)?
  * number?
  * boolean?
  * object?
  * array?

---

### 4. Follow the structure

* If it’s nested, go layer by layer
* Do not skip levels

---

## 🔑 Rule

> Always understand the structure before trying to use the data.

---

# 🧱 7. From JSON to JavaScript Thinking

When using JSON in JavaScript:

* objects → use **dot notation** (`object.key`)
* arrays → use **indexing** (`array[0]`)

---

## 🔹 Example

```json
[
  { "name": "Alice" },
  { "name": "Bob" }
]
```

---

### 🔹 Access in JavaScript

```javascript
data[0].name   // "Alice"
data[1].name   // "Bob"
```

---

## 🔑 Key Idea

> You must follow the structure exactly to access the correct value.

---

# 🧠 Common Mistakes

---

### ❌ Trying to access data without understanding structure

> Leads to: `undefined`

---

### ❌ Confusing objects and arrays

* using `.name` on an array
* forgetting `[index]`

---

### ❌ Skipping levels in nested data

* trying to jump directly to a value

---

## 🔑 Reminder

> If something is `undefined`, you likely misunderstood the structure.

---

# 🧠 Final Mental Model

When reading JSON, think:

> “What is this?”
> “Where is the value I want?”
> “What path gets me there?”

---

# 🔥 Final Guidance

Before writing code:

1. Look at the data
2. Identify the structure
3. Trace the path to the value
4. Then write your code

---

> “The problem is rarely the code—it’s not understanding the data.”
