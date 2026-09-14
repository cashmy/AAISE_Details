# Week 8 Demo - E-commerce Capstone Modeling Defense

Course: `10-152-123 Modern Data Modeling for Systems`  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Capstone evidence index and final design defense

---

# Demo Purpose

This demo shows how to turn course evidence into a final defense.

The movement is:

```text
evidence packet -> design claim -> support from artifacts -> limitation -> final defense
```

Students should see that the capstone is not about creating more artifacts. It is about organizing evidence and explaining the design.

---

# Step 1 - Capstone Pathway

Instructor demo pathway:

```text
Pathway 1: Continue and finalize the database concept used during Weeks 1-7.
```

Demo concept:

```text
E-commerce with reviews/ratings
```

---

# Step 2 - Capstone Evidence Index

| Evidence File or Artifact | Source | What It Shows | Use in Defense |
| --- | --- | --- | --- |
| E-commerce conceptual model | Week 1 | System intent, candidate entities, open questions | Shows starting model logic |
| Relational structure and process map | Week 2 | Entities, keys, relationships, system actions | Shows table-shaped structure |
| ERD | Week 3 | Visual model and relationship structure | Shows inspectable model |
| Model revision/change log | Week 4 | ProductCategory refinement and boundary control | Shows model improvement |
| Rules/anomaly/performance notes | Week 5 | Maintenance risk and rule placement | Shows quality reasoning |
| Document boundary worksheet | Week 6 | Product document design from system questions | Shows MongoDB design reasoning |
| Query and aggregation evidence | Week 7 | Product retrieval and category summary evidence | Shows model behavior |

---

# Step 3 - System Questions

Use student-facing phrasing.

```text
1. What products should appear on a product detail page?
2. Which products belong to a category?
3. Which products have strong ratings?
4. What recent reviews should display for a product?
5. What information should remain outside the product document?
```

Instructor note:

```text
These are plain-language questions the database design should help answer.
```

---

# Step 4 - Final Design Claim

```text
For product browsing and review display, the product-centered document model fits well because it keeps product facts, category snapshots, rating summary, and recent review snippets together. The relational/table-shaped model remains useful for understanding the full structure and for keeping separate facts clear.
```

---

# Step 5 - What the Design Does Not Handle Yet

```text
1. It does not fully model payment, shipment, or inventory.
2. It does not solve every review-history rule.
3. It does not prove that stored rating summaries will always stay accurate.
4. It does not replace the need for later query/design work in Course 120.
```

---

# Step 6 - AI Critique Prompt

```text
I am preparing a short final defense of an e-commerce database design for an introductory data modeling course.

Pathway:
Continue and finalize the course demo concept.

Design claim:
For product browsing and review display, the product-centered document model fits well because it keeps product facts, category snapshots, rating summary, and recent review snippets together. The relational/table-shaped model remains useful for understanding the full structure and for keeping separate facts clear.

Evidence I plan to use:
- ERD
- business rules and constraints
- relational model evidence
- document boundary worksheet
- sample product document
- query and aggregation evidence

Known limitations:
- payment, shipment, and inventory are outside scope
- review-history rules are incomplete
- rating summaries need responsible updates

Critique my defense.

Do not rewrite it for me.

Identify:
1. unsupported claims,
2. missing evidence,
3. unclear explanation of what the design does not handle yet,
4. whether the relational/table-shaped and document-shaped representations are treated fairly,
5. one revision priority before presenting.
```

---

# Step 7 - Prepared AI Output Excerpt

```text
Unsupported claim:
- If you say the document model "fits well," connect that claim directly to product browsing and review display evidence.

Missing evidence:
- Include the sample product document and one query or aggregation result.

Limitation:
- Explain that rating_summary is useful but requires update responsibility.

Fairness:
- Acknowledge that the relational/table-shaped model is stronger for showing full structure and separate facts.

Revision priority:
- Make the final claim narrower and evidence-based.
```

---

# Step 8 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Connect claim to evidence | Accept | Defense must be evidence-based. |
| Include sample document and query result | Accept | These show model behavior. |
| Explain rating_summary limitation | Accept | Honest limitation strengthens defense. |
| Treat relational model fairly | Accept | Avoids document-model hype. |
| Rewrite entire defense | Reject | Student must preserve ownership. |

---

# Student Transfer

Students should prepare their own capstone evidence packet using one approved pathway.

Transfer bridge:

```text
In the demo, the final claim was narrow, evidence-based, and honest about limits.
In your capstone, your defense should do the same for your selected concept.
```
