# Week 7 Lecture 1 Demo - E-commerce CRUD and Query Evidence

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: MongoDB CRUD operations and query evidence  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Query/access-pattern map, expected-result note, operation evidence

---

# Demo Purpose

This demo shows how operations can test whether a document shape supports system behavior.

The movement is:

```text
system question -> expected result -> operation/query -> result evidence -> model explanation
```

The operation is not the point by itself. The point is what the operation proves about the document model.

---

# Starting Point from Week 6

Product document boundary:

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

# Step 1 - CRUD Evidence Plan

| Operation Type | System Meaning | Evidence Goal |
| --- | --- | --- |
| Create | Add a product document | Show the collection can store the selected document shape |
| Read | Retrieve products by category/rating | Show product-detail/listing access pattern is supported |
| Update | Update rating summary or price | Show which updates are simple and which require care |
| Delete | Remove a test document | Show cleanup or lifecycle awareness |

Instructor note:

```text
Use a small demo dataset. Students do not need a production database to prove the modeling point.
```

---

# Step 2 - Query / Access-Pattern Map

| System Question | Expected Result | Relevant Document Shape | Operation Evidence |
| --- | --- | --- | --- |
| Which camping products have an average rating above 4? | Matching product names, categories, and average ratings | `categories` array and `rating_summary.average_rating` | find/filter products |
| What recent reviews show on a product detail page? | Product name with recent review snippets | embedded `recent_reviews` array | read one product document |
| What changes if a rating summary is updated? | rating_summary changes without rewriting all product fields | embedded `rating_summary` object | update product summary |

---

# Step 3 - Example Query Evidence

Example operation:

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

Expected result:

```text
Products that are in the Camping category and have average_rating greater than 4.
```

Result evidence:

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

# Step 4 - Retrieval Explanation

```text
The product document supports this query because category snapshots and rating_summary are stored with the product. That makes the product listing question easy to answer. The tradeoff is that category names and rating summaries may need careful updates if source data changes.
```

---

# Step 5 - AI Query Help Prompt

```text
I have a MongoDB products collection with this document shape:

- name
- current_price
- categories array with category_id and name
- rating_summary.average_rating
- rating_summary.review_count
- recent_reviews array

System question:
Find products in the Camping category with an average rating above 4.

Expected result:
A list of matching product names, category names, and average ratings.

I think the query should filter on categories.category_id and rating_summary.average_rating.

Suggest or critique a MongoDB query.

Explain each operator, identify what result I should expect, and tell me what to check if the result is empty.
Do not change my document model unless the query reveals a model issue.
Do not compare this to SQL syntax.
```

---

# Step 6 - Prepared AI Output Excerpt

```text
Suggested query:
- Filter using "categories.category_id": "cat_camping".
- Filter using "rating_summary.average_rating": { $gt: 4 }.
- Project name, categories, and rating_summary.average_rating.

Check if empty:
- Confirm category_id values match exactly.
- Confirm average_rating is stored as a number, not text.
- Confirm documents actually include rating_summary.

Model observation:
- This query is straightforward because category snapshots and rating_summary are embedded in the product document.
```

---

# Step 7 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Filter category_id and rating | Accept | Matches the stated document shape. |
| Project only needed fields | Accept | Keeps result evidence focused. |
| Check numeric rating type | Accept | Good practical troubleshooting. |
| Redesign whole document | Reject unless evidence requires it | One query does not justify wholesale redesign. |

---

# Student Transfer

Students should connect one operation or query to a real system question from their own scenario.

Transfer bridge:

```text
In the demo, the query was useful because it answered a product-listing question and revealed a document-shape tradeoff.
In your assignment, your operation should prove something about your model.
```

