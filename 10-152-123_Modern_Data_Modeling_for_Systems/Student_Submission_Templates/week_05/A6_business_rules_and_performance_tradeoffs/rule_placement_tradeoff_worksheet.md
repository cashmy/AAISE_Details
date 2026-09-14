# Rule Placement and Performance Tradeoff Worksheet

Course: `10-152-123 Modern Data Modeling for Systems`  
Week: `05`  
Assignment: `A6 Business Rules and Performance Tradeoffs`

---

# Instructions

Use your current model and scenario.

Do not use AI until after you complete your manual rule placement table and access pattern note.

Do not write SQL for this assignment.

---

# 1. Scenario Reminder

Briefly restate your system purpose.

```text

```

Which part of the model are you focusing on?

```text

```

---

# 2. Business Rule List

Write at least three business rules in plain English.

```text
1.
2.
3.
4.
5.
```

---

# 3. Rule Placement Table

Possible enforcement locations:

```text
database/model structure
application/backend
user process
mixed
unclear
```

| Business Rule | Possible Enforcement Location | Why | Risk or Limitation |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# 4. Access Pattern Pressure

Identify one system action, screen, report, lookup, or repeated question that could create performance pressure.

```text

```

What data would this access pattern need?

```text

```

Why might this become expensive, repeated, or awkward?

```text

```

---

# AI Prompt Input Block

After completing Sections 1-4 manually, you may copy the block below into the approved AI critique prompt if AI use is allowed.

Do not ask AI to implement the rules.

```text
I am deciding where to place business rules and whether to consider a performance tradeoff for this scenario:

[Paste scenario summary here]

Current model summary:
[Paste relevant entities and relationships here]

Business rules and placement table:
[Paste rule placement table here]

Access pattern pressure:
[Paste access pattern note here]

Critique my reasoning.

Do not write SQL.
Do not design implementation code.

Identify:
1. which rule placement choices seem reasonable,
2. which rule may need mixed enforcement,
3. what could go wrong with my placement decisions,
4. whether a performance or denormalization tradeoff should be considered,
5. one human design question I should answer before accepting the tradeoff.
```

---

# 5. Performance or Denormalization Tradeoff

Possible tradeoff:

```text

```

Possible benefit:

```text

```

Possible risk:

```text

```

Would you recommend this tradeoff now?

```text

```

Why or why not?

```text

```

---

# 6. Human Governor Question

What question should a human designer answer before accepting this tradeoff?

```text

```

---

# 7. Final Claim

Complete this statement:

```text
The most important rule placement decision in my model is...
```

Complete this statement:

```text
The performance tradeoff I considered is or is not worth it because...
```

---

# Final Check

- [ ] I separated rule placement from implementation.
- [ ] I explained why each rule belongs where I placed it.
- [ ] I identified one access pattern that could create pressure.
- [ ] I explained one tradeoff and its risk.
- [ ] I avoided SQL for this assignment.

