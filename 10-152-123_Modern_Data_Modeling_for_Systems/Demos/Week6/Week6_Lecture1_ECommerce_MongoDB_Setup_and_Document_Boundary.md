# Week 6 Lecture 1 Demo - E-commerce MongoDB Setup and Document Boundary

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: MongoDB architecture, setup, and first document boundary  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Access pattern notes, collection boundary decision, first sample document

---

# Demo Purpose

This demo shows how to begin MongoDB thinking from access patterns.

The movement is:

```text
system question -> information retrieved together -> collection boundary -> sample document
```

Setup matters, but setup is not the model. The model begins when students decide what information belongs together and why.

---

# Starting Point from Prior Weeks

Current E-commerce model includes:

```text
Customer
Order
OrderItem
Product
Review
Category
ProductCategory
```

Relevant Week 5 access pattern:

```text
Show a product listing or product detail page with product name, price, categories, average rating, review count, and recent reviews.
```

---

# Step 1 - MongoDB Setup Evidence

Show minimal setup evidence, such as:

```text
MongoDB environment available
Database name: ecommerce_demo
Planned collection: products
```

Instructor note:

```text
If the local install process consumes too much time, use a guided environment or instructor-provided setup. The modeling target is document-boundary reasoning.
```

---

# Step 2 - Access Pattern Notes

| Access Pattern | Data Needed Together | Frequency Guess | Modeling Pressure |
| --- | --- | --- | --- |
| View product detail page | product name, price, categories, rating summary, recent reviews | frequent | Product-centered document may help |
| Show customer order history | customer, orders, order items, product names, purchase-time prices | frequent for account pages | Customer/order boundary may differ |
| Add a new review | customer, product, rating, comment, date | less frequent than viewing | Embedded reviews may create update concerns |

---

# Step 3 - Collection Boundary Decision

First boundary to draft:

```text
products collection
```

Reason:

```text
The product detail page retrieves product facts, categories, rating summary, and recent review information together.
```

Decision:

```text
Embed categories as simple category snapshots for product browsing.
Embed a small recent_reviews array for display.
Reference full customer information by customer_id inside each review snapshot.
Keep order history outside the product document.
```

Tradeoff:

```text
This makes product-detail retrieval easier, but review snapshots and rating summaries may duplicate facts that need responsible updates later.
```

---

# Step 4 - First Sample Document

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

Instructor note:

```text
This is a document draft, not a claim that every review must always be embedded this way.
```

---

# Step 5 - AI Critique Prompt

```text
I am converting part of an e-commerce relational model into MongoDB documents.

Main access pattern:
Show a product detail page with product name, current price, categories, average rating, review count, and recent reviews.

Proposed collection boundary:
products collection

Proposed document shape:
- product fields at the top level
- categories embedded as small snapshots
- rating_summary embedded
- recent_reviews embedded as a small array
- customer_id referenced inside each review snapshot
- order history stays outside the product document

Critique this collection boundary.

Do not generate a full database.
Do not compare this to SQL syntax.

Identify:
1. what this document shape makes easier,
2. what it may make harder,
3. where duplication or stale data could appear,
4. whether embedding or referencing seems appropriate,
5. one boundary question I should answer before finalizing.
```

---

# Step 6 - Prepared AI Output Excerpt

```text
Easier:
- Product detail retrieval is simpler because product facts, category labels, rating summary, and recent reviews are together.

Harder:
- Updating review information may be harder if the same review is also stored elsewhere.

Duplication risk:
- rating_summary duplicates information that can be calculated from reviews.
- category names may become stale if category labels change.

Embedding/reference:
- Embedding category snapshots and recent reviews can fit product display.
- Referencing customer_id is reasonable because full customer data does not belong inside every product.

Boundary question:
- How many reviews should be embedded before the document becomes too large or awkward?
```

---

# Step 7 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Product detail becomes easier | Accept | This matches the access pattern. |
| Review updates may become harder | Accept | Embedded snapshots create update responsibility. |
| Rating summary can become stale | Accept | This echoes Week 5 denormalization reasoning. |
| Reference customer_id | Accept | Avoids embedding full customer records. |
| Embed every review forever | Reject | Unbounded arrays can become a design concern. |

---

# Student Transfer

Students should choose one part of their model and draft one document boundary.

Transfer bridge:

```text
In the demo, we did not convert the whole model. We picked one access pattern and drafted one collection boundary.
In your assignment, you will do the same for your scenario.
```

