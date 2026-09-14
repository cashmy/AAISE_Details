# Relational Structure Table Template

Course: `10-152-123 Modern Data Modeling for Systems`  
Assignment: `A2 Relational Structure and Process Mapping`

---

# Purpose

Use this template to sharpen a conceptual model into relational structure.

At this stage, you are not writing SQL and you are not creating a formal ERD. You are identifying entities, attributes, key candidates, relationship links, constraints, and the data needed to support system actions.

---

# 1. Starting Point

Selected scenario:

```text

```

Brief reminder of system intent:

```text

```

Week 1 entities you are carrying forward:

```text

```

Week 1 open questions that still matter:

```text
1.
2.
3.
```

---

# 2. Entity / Attribute / Key Table

| Entity | Purpose | Important Attributes | Primary Key Candidate | Notes or Questions |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

# 3. Relationship Link Table

Describe how entities connect.

Do not worry about perfect notation yet. Use clear language.

| From Entity | Relationship Phrase | To Entity | Relationship Type | Foreign Key or Link Candidate | Notes or Questions |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Relationship type examples:

```text
one-to-one
one-to-many
many-to-many
unclear
```

---

# 4. Plain-Language Integrity Constraints

Write rules the data should obey.

Examples:

```text
An order must belong to one customer.
A review must be connected to a product.
A product name should not be blank.
```

Your constraints:

```text
1.
2.
3.
4.
5.
```

---

# 5. Process-to-Data Map

Complete this after the second Week 2 lecture.

| System Action or Process | Data Needed | Entities Involved | Relationship or Constraint Tested | Gap or Revision Found |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

# 6. Process-Driven Revision Note

What did you change after mapping system actions to data?

```text

```

Why did that change improve the model?

```text

```

---

# 7. Remaining Modeling Question

What is one question about process support that still needs to be answered?

```text

```
