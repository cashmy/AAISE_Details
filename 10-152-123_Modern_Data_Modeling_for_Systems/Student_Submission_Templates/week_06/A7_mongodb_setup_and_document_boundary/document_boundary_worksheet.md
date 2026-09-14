# Document Boundary Worksheet

Course: `10-152-123 Modern Data Modeling for Systems`  
Week: `06`  
Assignment: `A7 MongoDB Setup and Document Boundary Draft`

---

# Instructions

Use your current relational/table-shaped model as the starting point.

Choose one part of the model to represent as a MongoDB document.

Do not use AI until after you define your access patterns and draft a boundary decision.

Do not compare SQL syntax to MongoDB syntax.

---

# 1. Starting Model Area

Which part of your current model are you converting first?

```text

```

Relevant entities or structures:

```text

```

Why this area is a reasonable first MongoDB boundary:

```text

```

---

# 2. Access Pattern Notes

Identify at least two access patterns.

| Access Pattern | Data Needed Together | Frequency Guess | Modeling Pressure |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Frequency examples:

```text
frequent
occasional
rare
unknown
```

---

# 3. Collection Boundary Decision

Proposed collection name:

```text

```

Main document subject:

```text

```

Why this boundary fits the access pattern:

```text

```

What stays outside this document boundary?

```text

```

---

# 4. Embed / Reference Draft

| Data or Related Concept | Embed, Reference, or Keep Separate? | Reason | Risk |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# AI Prompt Input Block

After completing Sections 1-4 manually, you may copy the block below into the approved AI critique prompt if AI use is allowed.

AI may help critique or generate a small sample JSON document only after you define the boundary yourself.

```text
I am converting part of my relational/table-shaped model into a MongoDB document.

Scenario:
[Paste your scenario summary here]

Access patterns:
[Paste your access pattern table here]

Proposed collection boundary:
[Paste your collection boundary decision here]

Embed/reference draft:
[Paste your embed/reference table here]

Critique this collection boundary.

Do not generate a full database.
Do not compare SQL syntax to MongoDB syntax.

Identify:
1. what this document shape makes easier,
2. what it may make harder,
3. where duplication or stale data could appear,
4. whether embedding or referencing seems appropriate,
5. one boundary question I should answer before finalizing.
```

---

# 5. First Sample Document Summary

Filename:

```text
sample_document.json
```

What does this document represent?

```text

```

What access pattern does it support?

```text

```

---

# 6. Tradeoff Note

What does this document shape make easier?

```text

```

What does it make harder?

```text

```

What duplicated or summarized data may need responsible updates?

```text

```

---

# Final Check

- [ ] My boundary starts from an access pattern.
- [ ] My sample document is valid JSON or close enough to inspect clearly.
- [ ] I explained what is embedded.
- [ ] I explained what is referenced or kept separate.
- [ ] I documented at least one tradeoff.
- [ ] I avoided SQL syntax comparison.

