# Week 4 Lecture 1 Demo - E-commerce Model Revision Process

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Modeling process and revision planning  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Model issue list and revision plan

---

# Demo Purpose

This demo shows that model revision should be deliberate.

The movement is:

```text
prior artifact evidence -> model issue -> revision intention -> planned change
```

The teaching point is that students should not revise a model simply because they can add more detail. They revise because the current model has a clarity, scope, relationship, or usefulness problem.

---

# Starting Point from Week 3

The Week 3 E-commerce ERD included:

```text
Customer
Order
OrderItem
Product
Review
Category
```

Known assumptions:

```text
1. Guest checkout is out of scope.
2. Product-to-category is one-to-many for the first ERD.
3. OrderItem resolves the Order/Product relationship.
4. Review connects Customer and Product.
5. Payment, shipment, and inventory are outside the Week 3 boundary.
```

---

# Step 1 - Manual Evidence Review

Review artifacts from prior weeks.

| Evidence Source       | What It Shows                                         | Possible Model Issue                        |
| --------------------- | ----------------------------------------------------- | ------------------------------------------- |
| Week 1 open questions | Can customers review products more than once?         | Missing business rule                       |
| Week 2 process map    | Customer writes review after interacting with product | Review may need rule tied to purchases      |
| Week 3 ERD            | Product belongs to Category                           | Category relationship may be oversimplified |
| Week 3 assumptions    | Payment/shipment/inventory excluded                   | Boundary should remain explicit             |
| Diagram review        | OrderItem is central                                  | Keep OrderItem, do not flatten it           |

---

# Step 2 - Manual Issue List

Create a model issue list.

| Issue                                 | Evidence                | Why It Matters                                                   | Severity       | Revision Direction                                         |
| ------------------------------------- | ----------------------- | ---------------------------------------------------------------- | -------------- | ---------------------------------------------------------- |
| Product-to-category may be too simple | Week 3 assumption       | Products may need multiple categories for browsing               | Medium         | Decide whether to keep one category or add ProductCategory |
| Review duplicate rule unresolved      | Week 1 and Week 2 notes | A customer could accidentally review the same product repeatedly | Medium         | Add plain-language business rule                           |
| Review eligibility unclear            | Process map             | Does a customer need to buy a product before reviewing?          | Low/Medium     | Record as boundary question, not immediate model change    |
| Payment/shipment/inventory pressure   | Boundary notes          | Real e-commerce has these, but adding all now would expand scope | Low for Week 4 | Keep as out-of-scope note                                  |

Instructor note:

```text
Severity is about learning priority and model risk, not how "real-world" the feature is.
```

---

# Step 3 - Revision Plan

| Planned Revision                                              | Intended Improvement                               | Artifact to Update             | Keep / Change / Defer |
| ------------------------------------------------------------- | -------------------------------------------------- | ------------------------------ | --------------------- |
| Add ProductCategory as an associative entity                  | Supports products appearing in multiple categories | ERD/model notes                | Change                |
| Add rule: one customer may have one active review per product | Clarifies Review relationship                      | Assumption/business rule notes | Change                |
| Do not add Payment, Shipment, Inventory yet                   | Preserves Week 4 scope                             | Boundary notes                 | Defer                 |
| Keep OrderItem unchanged                                      | It already solves a real relationship problem      | ERD/model notes                | Keep                  |

---

# Step 4 - AI Critique Prompt

```text
I am revising an introductory ERD for an e-commerce model.

Current entities:
Customer, Order, OrderItem, Product, Review, Category

Current assumptions:
- Guest checkout is out of scope.
- Product-to-category is one-to-many.
- OrderItem resolves the Order/Product relationship.
- Review connects Customer and Product.
- Payment, shipment, and inventory are out of scope.

My possible revision issues:
1. Product-to-category may need many-to-many support.
2. Review duplicate rules are unclear.
3. Review eligibility may depend on purchase history.
4. Payment, shipment, and inventory are real but may be too much for this course stage.

Critique my revision plan.

Do not redesign the whole model.

Identify:
1. which issue is most worth revising now,
2. which issue should be documented as a boundary question,
3. which possible change may add unnecessary complexity,
4. what evidence from the current model supports the revision.
```

---

# Step 5 - Prepared AI Output Excerpt

```text
Most worth revising:
- Product-to-category may be worth revising if product browsing is important. A ProductCategory associative entity would support products belonging to multiple categories.

Boundary question:
- Review eligibility is important but may require purchase verification logic, so it can be documented as a rule question rather than fully modeled now.

Possible overcomplexity:
- Adding Payment, Shipment, and Inventory all at once would expand the model significantly.

Evidence:
- The prior ERD already uses OrderItem to resolve a many-to-many relationship, so ProductCategory can be introduced using a similar pattern.
```

---

# Step 6 - Instructor Review Labels

| AI Suggestion                                 | Review Label | Instructor Reasoning                                                |
| --------------------------------------------- | ------------ | ------------------------------------------------------------------- |
| Revise Product/Category                       | Accept       | It connects to a known assumption and teaches associative entities. |
| Treat review eligibility as boundary question | Accept       | It matters, but may require process/rule detail beyond Week 4.      |
| Avoid adding Payment/Shipment/Inventory       | Accept       | Scope discipline is a modeling skill.                               |
| Use OrderItem as analogy                      | Accept       | This helps students transfer a pattern.                             |

---

# Step 7 - Student Transfer

Students should review their own A1-A3 artifacts and create a revision plan.

Transfer bridge:

```text
In the demo, we did not revise everything. We selected one useful revision, one rule clarification, and one boundary decision.
In your lab, you will do the same for your selected scenario.
```
