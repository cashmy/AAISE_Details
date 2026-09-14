# Week 6 Lecture 1 Worked Output - E-commerce Document Boundary

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Selected Access Pattern

```text
Show a product detail page with product name, current price, categories, average rating, review count, and recent reviews.
```

---

# Collection Boundary Decision

```text
Collection: products
```

Why:

```text
The selected access pattern is product-centered. The product detail page needs product facts, category labels, review summary, and recent review snippets together.
```

---

# Embedded vs Referenced Decisions

| Data | Embed or Reference? | Reason | Risk |
| --- | --- | --- | --- |
| Product facts | Embed/top-level | Product is the main document subject | Product document must be maintained carefully |
| Category snapshots | Embed | Product detail needs category labels | Category names can become stale |
| Rating summary | Embed | Product page needs quick summary | Summary duplicates review facts |
| Recent reviews | Embed small array | Product page shows recent feedback | Review changes may need synchronized updates |
| Customer details | Reference by customer_id | Full customer profile does not belong in product document | Extra lookup may be needed for full customer display |
| Order history | Separate boundary | Order history is not product-detail data | Requires another document design later |

---

# First Sample Document

```json
{
  "_id": "prod_1001",
  "name": "Trail Mug",
  "current_price": 14.99,
  "categories": [
    {
      "category_id": "cat_drinkware",
      "name": "Drinkware",
      "is_primary": true
    },
    {
      "category_id": "cat_camping",
      "name": "Camping"
    }
  ],
  "rating_summary": {
    "average_rating": 4.6,
    "review_count": 18
  },
  "recent_reviews": [
    {
      "review_id": "rev_501",
      "customer_id": "cust_77",
      "rating": 5,
      "comment": "Keeps coffee warm during morning hikes.",
      "review_date": "2026-02-04"
    }
  ]
}
```

---

# Tradeoff Note

```text
This document boundary makes product detail display easier, but it introduces update responsibility for category snapshots, rating_summary, and recent_reviews. The design is reasonable only if the product detail access pattern matters enough to justify those duplicated or summarized values.
```

