# Week 5 Lecture 2 Worked Output - E-commerce Rules and Performance

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Rule Placement Table

| Business Rule | Recommended Placement | Reason | Risk or Limitation |
| --- | --- | --- | --- |
| Review must connect one customer and one product | Model structure + application/backend | The relationship belongs in the model, but workflow creates the review | If handled only by user process, invalid reviews may exist |
| Rating must stay within allowed range | Validation rule, possibly database-backed later | Simple rule with clear allowed values | If only checked by the screen, other entry paths may bypass it |
| Customer may have one active review per product | Mixed | Requires relationship awareness and workflow decisions | History, edits, and duplicate handling may complicate it |
| OrderItem preserves purchase-time item_price | Model structure | The price at purchase is part of the order line event | If omitted, historical order meaning can change when product price changes |
| Product may appear in multiple categories | Model structure | ProductCategory supports this relationship | Adds complexity if one-category products are enough |

---

# Access Pattern Pressure

```text
Product listing page:
Show product name, current price, primary category, average rating, and review count.
```

Why it may create pressure:

```text
The listing page may be viewed frequently and may need rating summaries for many products at once.
```

---

# Performance Tradeoff Note

Possible tradeoff:

```text
Store average_rating and review_count as summary values.
```

Benefit:

```text
The listing page can display rating summaries without recalculating them from every review each time.
```

Risk:

```text
The stored summary duplicates information from Review records and can become stale if review changes do not update the summary.
```

Human governor question:

```text
Are product listings viewed often enough, and reviews changed rarely enough, to justify the added responsibility of keeping summary values accurate?
```

---

# Final Claim

```text
The model should keep Review records as the source of truth. A stored average_rating and review_count may be reasonable later if product listing performance becomes important, but it should be treated as a deliberate denormalization tradeoff, not as the default design.
```

