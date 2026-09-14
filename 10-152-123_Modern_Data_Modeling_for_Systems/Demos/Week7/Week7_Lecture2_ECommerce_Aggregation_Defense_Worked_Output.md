# Week 7 Lecture 2 Worked Output - E-commerce Aggregation and Defense Prep

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Aggregation Goal

```text
Group products by category and calculate average product rating by category.
```

---

# Aggregation Evidence

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

# Result Evidence

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

# Performance Awareness Note

```text
This aggregation is useful because category snapshots and rating_summary are stored in the product document. If product-listing and category-summary views are frequent, fields such as categories.category_id and rating_summary.average_rating may deserve index awareness later. The main risk is that stored summaries must remain accurate when reviews change.
```

---

# Capstone Evidence Selection

| Evidence | Defense Use |
| --- | --- |
| Week 3 ERD | Shows original relational/table-shaped model |
| Week 6 document boundary | Shows access-pattern-based document design |
| Week 6 comparison table | Shows tradeoff reasoning |
| Week 7 query result | Shows retrieval evidence |
| Week 7 aggregation result | Shows summary/reporting evidence |

---

# Draft Modeling Claim

```text
The product-centered document model is a responsible choice for product browsing because it supports product detail, category filtering, rating display, and category-level summaries from a product-shaped document. The tradeoff is that embedded snapshots and stored rating summaries require update responsibility, while the relational/table-shaped model remains stronger for keeping separate facts independently consistent.
```

