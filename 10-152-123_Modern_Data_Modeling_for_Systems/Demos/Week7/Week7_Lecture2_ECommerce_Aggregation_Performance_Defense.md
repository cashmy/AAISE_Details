# Week 7 Lecture 2 Demo - E-commerce Aggregation, Performance, and Defense Prep

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Aggregation and performance awareness  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Aggregation evidence, performance note, capstone evidence selection, draft modeling claim

---

# Demo Purpose

This demo shows how aggregation and performance awareness become evidence for a modeling defense.

The movement is:

```text
system question -> aggregation goal -> result evidence -> performance note -> defense claim
```

Students should not just paste a pipeline. They should explain what the pipeline proves about their document model.

---

# Step 1 - Aggregation Goal

System question:

```text
Which categories have the strongest product ratings?
```

Aggregation goal:

```text
Group products by embedded category snapshot and calculate average product rating by category.
```

Expected result:

```text
A list of category names with average product rating and product count.
```

---

# Step 2 - Example Aggregation Pipeline

```javascript
db.products.aggregate([
  { $unwind: "$categories" },
  {
    $group: {
      _id: "$categories.name",
      average_category_rating: { $avg: "$rating_summary.average_rating" },
      product_count: { $sum: 1 }
    }
  },
  { $sort: { average_category_rating: -1 } }
])
```

---

# Step 3 - Result Evidence

```json
[
  {
    "_id": "Camping",
    "average_category_rating": 4.6,
    "product_count": 12
  },
  {
    "_id": "Drinkware",
    "average_category_rating": 4.4,
    "product_count": 8
  }
]
```

---

# Step 4 - Performance Awareness Note

```text
This aggregation depends on category snapshots and rating_summary being stored in each product document. That makes category-level rating summaries possible from the products collection, but it also means rating_summary accuracy matters. If product listing and category summaries are frequent, indexes on category identifiers and rating fields may matter later.
```

Optional performance observation:

```text
Possible index awareness: categories.category_id and rating_summary.average_rating may be relevant for frequent product-listing queries.
```

Instructor note:

```text
Students do not need to become performance engineers. They need to notice that document shape affects query and aggregation behavior.
```

---

# Step 5 - Capstone Evidence Selection

| Evidence | Why It Matters for Defense |
| --- | --- |
| Week 3 ERD | Shows original relational/table-shaped structure |
| Week 6 document boundary decision | Shows access-pattern-based document modeling |
| Week 6 relational vs document comparison | Shows representation tradeoff reasoning |
| Week 7 query evidence | Shows the document model supports product listing retrieval |
| Week 7 aggregation evidence | Shows the document model can support category rating summaries |

---

# Step 6 - Draft Modeling Claim

```text
For product-centered browsing and review display, the document-shaped product model is a responsible choice because it keeps product facts, category snapshots, rating summaries, and recent review snippets together. The main tradeoff is update responsibility for duplicated or summarized values.
```

---

# Step 7 - AI Critique Prompt

```text
I am preparing a final modeling defense for an e-commerce data model.

Aggregation goal:
Group products by category and calculate average product rating by category.

Evidence:
- Product documents include embedded category snapshots.
- Product documents include rating_summary.average_rating.
- A query can retrieve camping products with average rating above 4.
- An aggregation can summarize average rating by category.

Draft claim:
For product-centered browsing and review display, the document-shaped product model is a responsible choice because it keeps product facts, category snapshots, rating summaries, and recent review snippets together. The main tradeoff is update responsibility for duplicated or summarized values.

Critique this defense preparation.

Do not rewrite the defense for me.

Identify:
1. whether the aggregation evidence supports the system question,
2. whether my performance note is specific enough,
3. whether my claim fairly compares relational/table-shaped and document-shaped representations,
4. what evidence I should bring into the final defense,
5. one limitation I should acknowledge.
```

---

# Step 8 - Prepared AI Output Excerpt

```text
Evidence support:
- The aggregation supports category rating summaries if rating_summary is accurate.

Performance note:
- Mention which access pattern is frequent and which fields may need index awareness.

Fairness:
- Acknowledge that the relational model is stronger for maintaining separate facts consistently.

Evidence to bring:
- ERD, document boundary worksheet, comparison table, query result, aggregation result.

Limitation:
- Stored rating_summary and category snapshots can become stale.
```

---

# Step 9 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Aggregation depends on rating_summary accuracy | Accept | Important limitation. |
| Name frequent access pattern | Accept | Makes performance note less vague. |
| Relational model has consistency strengths | Accept | Defense should be fair. |
| Bring full evidence chain | Accept | Supports Week 8 readiness. |
| Claim document model is always better | Reject | Representation choice depends on need. |

---

# Student Transfer

Students should create one aggregation or guided aggregation exercise and connect it to their final modeling defense.

Transfer bridge:

```text
In the demo, aggregation evidence became part of a defensible claim.
In your assignment, your aggregation should help you explain why a representation fits your scenario, not just show that a command ran.
```

