# Week 8 Worked Output - E-commerce Capstone Defense

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Capstone Pathway

```text
Pathway 1: Continue and finalize the database concept used during Weeks 1-7.
```

---

# Evidence Index Summary

| Evidence | What It Supports |
| --- | --- |
| ERD | Shows main entities and relationships |
| Business rules | Shows constraints and responsibility decisions |
| Relational model evidence | Shows table-shaped structure and key relationships |
| Product document sample | Shows document-shaped representation |
| Query evidence | Shows product retrieval works for category/rating question |
| Aggregation evidence | Shows category rating summary is possible |

---

# Final Design Defense

```text
The e-commerce design fits product browsing and review display because the model identifies the core entities, shows their relationships in an ERD, and then narrows the MongoDB document design around product-centered questions.

The relational/table-shaped model is useful because it shows the full structure: Customer, Order, OrderItem, Product, Review, Category, and ProductCategory. It makes the separate facts easier to inspect.

The document-shaped product model is useful because product facts, category snapshots, rating summary, and recent review snippets can be read together for product browsing. The query and aggregation evidence show that the document shape can answer product-centered questions.

This design does not handle everything yet. Payment, shipment, inventory, and complete review-history rules are outside the current scope. The model also needs a responsible update plan for rating_summary and review snapshots.

My final recommendation is to keep the relational/table-shaped model as the clearest full design reference and use the product-centered document model when the system needs product browsing and review display evidence.
```

---

# Limitation Statement

```text
The design is conceptual. It supports the course-level modeling question, but it is not a complete production database.
```

