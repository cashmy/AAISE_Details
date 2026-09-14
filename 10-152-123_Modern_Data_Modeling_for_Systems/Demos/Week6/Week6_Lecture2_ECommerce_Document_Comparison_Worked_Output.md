# Week 6 Lecture 2 Worked Output - E-commerce Document Comparison

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Access Pattern

```text
Show product name, current price, categories, average rating, review count, and recent reviews on a product detail page.
```

---

# Embedded vs Referenced Comparison

| Choice | Benefit | Risk | Decision |
| --- | --- | --- | --- |
| Embed category snapshots | Fast product display | Category labels can become stale | Accept for display labels |
| Reference customer_id in reviews | Avoids full customer duplication | Needs lookup for full profile | Accept |
| Embed recent review snapshots | Product page can display recent feedback quickly | Review edits may require synchronization | Accept only as bounded snapshot |
| Store rating_summary | Product listing/detail display is easier | Summary can become stale | Accept as deliberate summary with update responsibility |
| Keep order history separate | Product documents remain focused | Separate design needed for account pages | Accept |

---

# Relational vs Document Tradeoff

| Modeling Question | Relational/Table-Shaped Model | Product Document Model |
| --- | --- | --- |
| Product facts | Stable Product structure | Top-level product document fields |
| Categories | ProductCategory relationship | Embedded category snapshots or category IDs |
| Reviews | Review linked to Product and Customer | Embedded recent snapshots plus possible full Review collection |
| Easier | Maintenance of separate facts | Product-centered reading |
| Harder | Assembling product display | Keeping duplicated summaries/snapshots accurate |
| Best fit | Consistency across many independent updates | Frequent bounded product-detail retrieval |

---

# Representation Decision Explanation

```text
The product document model is reasonable for product-detail display because it groups the data most often read together. It should not become the only source of truth for every review. Recent review snapshots and rating_summary are useful, but they create update responsibility that must be documented.
```

---

# Remaining Boundary Question

```text
How many recent reviews should be embedded before the product document becomes too large or too hard to keep accurate?
```

