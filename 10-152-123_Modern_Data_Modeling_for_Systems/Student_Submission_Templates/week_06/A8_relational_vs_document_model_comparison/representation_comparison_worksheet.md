# Representation Comparison Worksheet

Course: `10-152-123 Modern Data Modeling for Systems`  
Week: `06`  
Assignment: `A8 Relational vs Document Model Comparison`

---

# Instructions

Use your A7 document boundary as the starting point.

Create two sample document options or variants, then compare them against your relational/table-shaped model.

Do not compare SQL syntax to MongoDB syntax.

---

# 1. Access Pattern Being Tested

Which access pattern are you designing for?

```text

```

What data is needed together?

```text

```

---

# 2. Document Options

Option A filename:

```text
sample_document_option_a.json
```

Option A summary:

```text

```

Option B filename:

```text
sample_document_option_b.json
```

Option B summary:

```text

```

---

# 3. Embedded vs Referenced Comparison

| Design Choice | Makes Easier | Makes Harder | Duplication / Update Concern |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# 4. Relational vs Document Tradeoff Table

| Question | Relational/Table-Shaped Representation | Document-Shaped Representation |
| --- | --- | --- |
| Where is the main subject stored? |  |  |
| Where are related facts stored? |  |  |
| What is easy? |  |  |
| What is harder? |  |  |
| What can become duplicated or stale? |  |  |
| When would this representation fit best? |  |  |

---

# AI Prompt Input Block

After completing Sections 1-4 manually, you may copy the block below into the approved AI critique prompt if AI use is allowed.

```text
I have two possible MongoDB document designs for this scenario:

[Paste scenario summary here]

Access pattern:
[Paste access pattern here]

Option A:
[Paste or summarize document option A]

Option B:
[Paste or summarize document option B]

My relational/table-shaped comparison:
[Paste your comparison notes here]

Critique the tradeoffs.

Do not compare SQL syntax to MongoDB syntax.
Do not choose only based on which document looks simpler.

Compare:
1. what each design makes easier to read,
2. what each design makes harder to update,
3. where duplication may appear,
4. which design better fits the stated access pattern,
5. what human design question should be answered before choosing.
```

---

# 5. Representation Decision

Which option or representation do you currently recommend for the selected access pattern?

```text

```

Why?

```text

```

What is the main tradeoff?

```text

```

---

# 6. Remaining Boundary Question

What question should be answered before this model is treated as final?

```text

```

---

# Final Check

- [ ] I compared at least two document options or variants.
- [ ] I connected my comparison to an access pattern.
- [ ] I explained embedding and referencing decisions.
- [ ] I compared relational/table-shaped and document-shaped representation.
- [ ] I identified a tradeoff or update concern.
- [ ] I avoided SQL syntax comparison.

