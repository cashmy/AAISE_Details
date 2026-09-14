# Week 4 Lecture 2 Worked Output - E-commerce Refined Model

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Selected Conceptual Pattern

```text
Associative entity
```

Reason:

```text
The first ERD treated Category-to-Product as one-to-many. That is simple, but it may not fit product browsing if one product can appear in multiple categories. ProductCategory resolves the many-to-many relationship without duplicating products or categories.
```

---

# Revised Entity List

```text
Customer
Order
OrderItem
Product
Review
Category
ProductCategory
```

---

# Revised Relationship Statements

```text
Customer places Order.
Order contains OrderItem.
OrderItem refers to Product.
Customer writes Review.
Review is about Product.
Product connects to Category through ProductCategory.
ProductCategory connects one Product to one Category.
```

---

# ProductCategory Notes

| Attribute | Keep, Change, or Defer | Reason |
| --- | --- | --- |
| product_category_id | Keep | Simple identifier for the associative entity |
| product_id | Keep | Links to Product |
| category_id | Keep | Links to Category |
| is_primary_category | Optional | Useful if a product needs one default category |
| display_order | Defer | Only needed if category browsing order matters |

---

# Change Log

| Change | Reason | Benefit | Tradeoff |
| --- | --- | --- | --- |
| Added ProductCategory | Product/Category may be many-to-many | More flexible category browsing | More complex ERD |
| Added review duplicate rule note | Customer/Product/Review rule was unclear | Cleaner review interpretation | Rule may require enforcement later |
| Deferred Payment/Shipment/Inventory | Keeps scope focused | Avoids model sprawl | Real system would need these later |

---

# Model Quality Self-Assessment

| Quality Lens | Rating | Explanation |
| --- | --- | --- |
| Clarity | Developing/Meets | The ERD has one more entity, but the Product/Category relationship is now more honest. |
| Usefulness | Meets | The model better supports browsing products by category. |
| Flexibility | Meets | Products can now appear in more than one category. |
| Scope control | Meets | Payment, shipment, and inventory remain boundary notes. |
| Remaining questions | Developing | Need to decide whether `is_primary_category` belongs now or later. |

---

# Final Revision Claim

```text
The revised model is better because it handles product categorization more flexibly while keeping the course-stage boundary under control. The main tradeoff is that the ERD is slightly more complex, so the ProductCategory purpose must be explained clearly.
```

