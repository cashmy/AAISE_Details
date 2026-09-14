# Week 3 Lecture 2 Demo - E-commerce draw.io Practice and ERD Review

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: draw.io training and ERD review  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Completed ERD packet

---

# Demo Purpose

This demo supports the practical side of Week 3.

The movement is:

```text
ERD plan -> draw.io shapes and connectors -> exportable diagram -> notation/readability review
```

This is still a modeling lesson. draw.io is the tool, not the learning target.

---

# Step 1 - draw.io Setup and File Expectations

Show students how to:

1. Open draw.io / diagrams.net.
2. Create a blank diagram.
3. Save the source file.
4. Use rectangles or ERD shapes for entities.
5. Add attributes inside or below the entity shape.
6. Use connectors for relationships.
7. Add relationship labels and cardinality notation.
8. Export as PNG or PDF if required.

Recommended file names:

```text
erd_diagram.drawio
erd_diagram.png
```

---

# Step 2 - Manual Diagram Build Order

Build the diagram in this order:

```text
1. Add entity boxes first.
2. Add key attributes.
3. Add important non-key attributes.
4. Add relationship lines.
5. Add cardinality markers or cardinality labels.
6. Add relationship names only where they improve readability.
7. Add a small assumptions note.
8. Review layout before exporting.
```

Instructor note:

```text
If students start with line styling and colors, pull them back to structure. Readability matters, but decoration is not the assignment.
```

---

# Step 3 - E-commerce ERD Review Checklist

| Review Item | Demo Finding | Action |
| --- | --- | --- |
| Every entity has a clear name | Yes | Keep singular names |
| Key attributes are visible | Mostly | Mark key attributes consistently |
| OrderItem is positioned between Order and Product | Yes | Keep placement |
| Review connects to both Customer and Product | Yes | Keep both relationships visible |
| Category/Product assumption is documented | Missing at first | Add assumption note |
| Lines cross unnecessarily | Some crossing | Move Review lower or to the side |
| Cardinality is visible | Incomplete | Add labels or crow's-foot markers |

---

# Step 4 - AI Critique Prompt After Draft

Students may use AI only after they have a manual draft or a written description of the draft.

```text
I created an ERD draft for an e-commerce model.

Entities:
Customer, Product, Order, OrderItem, Review, Category

Layout description:
- Customer is on the left.
- Order is near Customer.
- OrderItem is between Order and Product.
- Product is near Category.
- Review is below Product and also connects to Customer.

Relationships:
- Customer 1-to-many Order
- Order 1-to-many OrderItem
- Product 1-to-many OrderItem
- Customer 1-to-many Review
- Product 1-to-many Review
- Category 1-to-many Product

Assumptions:
- Guest checkout is out of scope.
- Product has one category in this version.
- Review must connect one customer and one product.

Critique my ERD as a communication artifact.

Do not redesign the whole model.

Identify:
1. one notation issue to check,
2. one readability issue to check,
3. one assumption that should be visible,
4. one relationship that is especially important to explain,
5. one thing I should not overcomplicate yet.
```

---

# Step 5 - Prepared AI Output Excerpt

```text
Notation issue:
- Make sure optionality is visible. For example, a customer may have zero orders, but an order should have exactly one customer.

Readability issue:
- If Review connects to both Customer and Product, place it where both lines can be seen without crossing other major lines.

Visible assumption:
- Product has one category in this version.

Important relationship:
- OrderItem is central because it explains how an order can contain multiple products and store quantity.

Do not overcomplicate:
- Avoid adding Payment, Shipment, and Inventory unless the assignment scope requires them.
```

---

# Step 6 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Add optionality | Accept if notation supports it | Good modeling precision for Week 3. |
| Move Review for readability | Accept | Layout should reduce line crossing. |
| Show Category assumption | Accept | Prevents later confusion. |
| Explain OrderItem | Accept | This is the central relationship resolution. |
| Add Payment/Shipment/Inventory | Reject for now | Scope discipline matters. |

---

# Step 7 - Final Student Transfer

Students should submit one ERD packet:

```text
1. ERD source/export
2. notation and readability checklist
3. assumptions
4. short design rationale
5. AI assistance notes, if AI was used
```

The final reminder:

```text
The diagram should be clear enough that another person can ask useful questions about your model.
```

