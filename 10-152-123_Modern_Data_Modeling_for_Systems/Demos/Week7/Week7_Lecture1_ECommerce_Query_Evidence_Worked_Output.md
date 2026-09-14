# Week 7 Lecture 1 Worked Output - E-commerce Query Evidence

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# System Question

```text
Which camping products have an average rating above 4?
```

---

# Expected Result

```text
A list of product documents or projected fields showing product name, category information, and average rating.
```

---

# Query Evidence

```javascript
db.products.find(
  {
    "categories.category_id": "cat_camping",
    "rating_summary.average_rating": { $gt: 4 }
  },
  {
    name: 1,
    categories: 1,
    "rating_summary.average_rating": 1
  }
)
```

---

# Result Evidence

```json
{
  "_id": "prod_1001",
  "name": "Trail Mug",
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
    "average_rating": 4.6
  }
}
```

---

# Retrieval Explanation

```text
This query is supported by the product document shape because category snapshots and rating_summary are stored with the product. The benefit is simple product-listing retrieval. The risk is that category labels and rating summaries must be kept accurate when category or review information changes.
```

---

# Model Evidence Claim

```text
The product document supports product-centered retrieval well, especially when the system needs category and rating information together. It does not eliminate update responsibility for duplicated or summarized data.
```

