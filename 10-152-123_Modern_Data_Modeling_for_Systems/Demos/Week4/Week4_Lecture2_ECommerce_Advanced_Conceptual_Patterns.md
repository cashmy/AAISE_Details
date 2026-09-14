# Week 4 Lecture 2 Demo - E-commerce Advanced Conceptual Patterns

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Advanced conceptual patterns  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Revised model, conceptual pattern note, quality self-assessment

---

# Demo Purpose

This demo shows how advanced conceptual patterns can improve a model when they solve a real problem.

The movement is:

```text
revision plan -> pattern choice -> focused model change -> change log -> quality self-assessment
```

Students should see that patterns are options, not decorations.

---

# Step 1 - Pattern Review

Review the Week 4 revision plan against common conceptual patterns.

| Pattern | Does It Fit? | Reason |
| --- | --- | --- |
| Role clarification | Maybe later | Customer roles could split later, but not needed now |
| Subtype | Not now | Product subtypes are possible but not required |
| Category/hierarchy | Maybe | Categories may need organization later |
| Associative entity | Yes | Product and Category may be many-to-many |
| Event entity | Already present | Order and Review behave like event/interaction records |
| Boundary clarification | Yes | Payment, shipment, and inventory remain outside current scope |

---

# Step 2 - Manual Revision

Apply one focused pattern:

```text
Add ProductCategory as an associative entity between Product and Category.
```

Revised relationship statements:

```text
Product can appear in many ProductCategory records.
Category can appear in many ProductCategory records.
ProductCategory connects one Product to one Category.
```

Revised entity list:

```text
Customer
Order
OrderItem
Product
Review
Category
ProductCategory
```

ProductCategory possible attributes:

```text
product_category_id
product_id
category_id
is_primary_category
display_order
```

Instructor note:

```text
Do not turn every relationship into an associative entity. We are using this pattern because it solves a specific relationship problem.
```

---

# Step 3 - AI Critique Prompt

```text
I revised an e-commerce ERD by adding ProductCategory as an associative entity between Product and Category.

Original issue:
The first ERD assumed each product has one category, but product browsing may require products to appear in multiple categories.

Revised entities:
Customer, Order, OrderItem, Product, Review, Category, ProductCategory

ProductCategory attributes:
product_category_id, product_id, category_id, is_primary_category, display_order

Boundary:
Payment, shipment, and inventory remain out of scope.

Critique this focused revision.

Do not redesign the whole model.

Identify:
1. whether the associative entity is justified,
2. whether any ProductCategory attributes seem unnecessary,
3. what assumption should be documented,
4. one risk of adding this complexity,
5. one reason this revision improves the model.
```

---

# Step 4 - Prepared AI Output Excerpt

```text
Justification:
- ProductCategory is justified if products can belong to multiple categories.

Attribute caution:
- is_primary_category and display_order are useful only if the system needs primary category or category display behavior.

Assumption:
- A product can belong to more than one category.

Risk:
- The model is more flexible but also more complex for students and users to understand.

Improvement:
- The model no longer forces duplicate products or an artificially simple category structure.
```

---

# Step 5 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| ProductCategory is justified | Accept | It directly solves the selected issue. |
| Question extra attributes | Modify | Keep `is_primary_category` as optional; defer `display_order` unless browsing order matters. |
| Document assumption | Accept | This is required for the revised ERD. |
| Complexity risk | Accept | Students should name the tradeoff. |
| Avoid duplicate products | Accept | This is the clearest model-quality improvement. |

---

# Step 6 - Final Revision Note

```text
The revised model adds ProductCategory to support products appearing in multiple categories. This improves flexibility and avoids duplicating product records. The tradeoff is that the model now has one more entity and relationship path for readers to understand.
```

---

# Step 7 - Model Quality Self-Assessment

| Quality Lens | Assessment |
| --- | --- |
| Clarity | Slightly more complex, but clearer about Product/Category structure |
| Usefulness | Better supports product browsing |
| Flexibility | More flexible than one-category-only Product |
| Scope control | Payment, shipment, and inventory remain out of scope |
| Remaining ambiguity | Need to decide whether primary category matters |

---

# Student Transfer

Students should choose one meaningful refinement, explain one pattern considered or applied, and document what they deliberately did not change.

Transfer bridge:

```text
In the demo, we used an associative entity only because a real relationship problem required it.
In your lab, use a pattern only if it improves your model's purpose, clarity, or flexibility.
```

