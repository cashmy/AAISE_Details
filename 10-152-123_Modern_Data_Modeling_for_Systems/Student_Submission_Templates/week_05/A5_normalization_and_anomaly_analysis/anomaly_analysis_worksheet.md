# Anomaly Analysis Worksheet

Course: `10-152-123 Modern Data Modeling for Systems`  
Week: `05`  
Assignment: `A5 Normalization and Anomaly Analysis`

---

# Instructions

Use your current model or an instructor-approved excerpt.

Do not use AI until after you complete your manual anomaly/risk table.

Do not write SQL for this assignment.

---

# 1. Model Excerpt Reviewed

Describe or paste the part of the model you reviewed.

```text

```

Which entities, attributes, or table-shaped structures are involved?

```text

```

---

# 2. Repeated or Mixed Facts

What facts appear repeated, mixed together, or stored in a risky place?

```text
1.
2.
3.
```

---

# 3. Anomaly/Risk Table

| Risk Type | Where It Appears | What Could Go Wrong | Cause | Possible Improvement |
| --- | --- | --- | --- | --- |
| update anomaly |  |  |  |  |
| insert anomaly |  |  |  |  |
| delete anomaly |  |  |  |  |
| other maintenance risk |  |  |  |  |

You do not need to force all three anomaly types if they do not honestly fit. Explain what you found.

---

# 4. Normalization Awareness Explanation

Would normalization help?

```text

```

Why or why not?

```text

```

What fact should have a more stable home?

```text

```

---

# AI Prompt Input Block

After completing Sections 1-4 manually, you may copy the block below into the approved AI critique prompt if AI use is allowed.

Do not ask AI to redesign the whole model.

```text
Here is the model excerpt I reviewed:

[Paste your model excerpt here]

Repeated or mixed facts I noticed:
[Paste your notes here]

My anomaly/risk table:
[Paste your anomaly/risk table here]

My current recommendation:
[Paste your recommendation here]

Critique my anomaly analysis.

Do not write SQL.
Do not redesign the whole model.

Identify:
1. whether my anomaly labels make sense,
2. whether I missed a likely update, insert, or delete risk,
3. whether normalization would help,
4. one risk of over-normalizing,
5. one focused improvement I should consider.
```

---

# 5. Structural Recommendation

What change do you recommend?

```text

```

What problem would that change reduce?

```text

```

What tradeoff would that change create?

```text

```

---

# 6. Final Claim

Complete this statement:

```text
This model excerpt has a maintenance risk because...
```

Complete this statement:

```text
My recommendation is responsible because...
```

---

# Final Check

- [ ] I identified a real maintenance risk.
- [ ] I explained the cause of the risk.
- [ ] I connected normalization to model quality.
- [ ] I avoided deep implementation detail.
- [ ] I avoided SQL for this assignment.

