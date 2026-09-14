# Relational Structure and Process Mapping Worksheet

Course: `10-152-123 Modern Data Modeling for Systems`  
Week: `02`  
Assignment: `A2 Relational Structure and Process Mapping`

---

# Instructions

Complete this file in two passes:

1. **Tuesday checkpoint:** Complete Sections 1-4 after Lecture 1 and Lab 1.
2. **Friday final submission:** Complete Sections 5-8 after Lecture 2 and Lab 2.

Do not use AI until after you complete your manual attempt.

Do not write SQL for this assignment. Stay at the structure and reasoning level.

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

# AI Prompt Input Block

After completing Sections 1-4 manually, you may copy the block below into the approved AI critique prompt if AI use is allowed.

Do not ask AI to complete the assignment. Ask AI to critique your manual attempt.

```text
Here is my draft relational structure for this scenario:

[Paste your scenario summary here]

System intent:
[Paste your system intent here]

Entities, attributes, and key candidates:
[Paste your entity/attribute/key table here]

Relationship links:
[Paste your relationship link table here]

Plain-language integrity constraints:
[Paste your constraints here]

Critique this as a reviewer. Do not rewrite the whole model.

Look for:
1. weak or unclear primary key choices,
2. missing relationship links,
3. attributes that may belong on a different entity,
4. relationship types that need clarification,
5. integrity constraints I should write in plain language.

Keep feedback introductory and explain why each issue matters.
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

---

# 8. Final Check

- [ ] My first relational structure version was completed manually.
- [ ] My final version includes a process-to-data map.
- [ ] I identified at least one constraint or rule.
- [ ] I made or explained one process-driven revision.
- [ ] I avoided SQL and formal ERD work for this assignment.
- [ ] I can explain how at least one system action uses my model.
