# Week 3 Lecture 2 Worked Output - E-commerce ERD Review

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Completed ERD Packet Contents

```text
erd_diagram.drawio
erd_diagram.png
erd_notation_readability_checklist.md
ai_assistance_notes.md, if used
```

---

# Final ERD Assumptions

```text
1. Guest checkout is outside the current model, so each order belongs to one customer.
2. Products have one category in this version.
3. OrderItem is required because orders can contain multiple products and each line needs quantity and purchase-time price.
4. A review must connect one customer and one product.
5. Payment, shipment, and inventory are outside the Week 3 boundary.
```

---

# Notation and Readability Review

| Check | Status | Note |
| --- | --- | --- |
| Entity names are singular and clear | Complete | Customer, Product, Order, OrderItem, Review, Category |
| Key attributes are visible | Complete | Each entity includes an ID field |
| Important non-key attributes are visible | Complete | Only key model-relevant attributes are shown |
| Relationship cardinality is visible | Complete | Labels or crow's-foot notation should be used consistently |
| Many-to-many relationship is resolved | Complete | Order/Product is resolved through OrderItem |
| Important assumptions are documented | Complete | Category/Product and guest checkout assumptions are written |
| Layout supports reading | Complete | OrderItem is placed between Order and Product |
| Scope is controlled | Complete | Payment, shipment, and inventory are not added |

---

# Design Rationale

```text
The most important relationship in this model is the connection between Order, OrderItem, and Product. OrderItem is needed because a single order can include multiple products, and each product can appear in many different orders. OrderItem also stores quantity and item_price, which belong to the purchase event rather than only to Product.
```

---

# Instructor Debrief

```text
The ERD is successful if a reviewer can see what the system remembers, how the major entities connect, and where the current assumptions are. It does not need to include every possible real-world e-commerce feature.
```

