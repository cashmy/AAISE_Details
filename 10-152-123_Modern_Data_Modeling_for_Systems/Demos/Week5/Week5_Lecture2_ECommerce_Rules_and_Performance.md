# Week 5 Lecture 2 Demo - E-commerce Business Rules and Performance Tradeoffs

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Denormalization and business rules  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Rule placement table and access-pattern tradeoff note

---

# Demo Purpose

This demo shows that model quality also depends on rule placement and performance pressure.

The movement is:

```text
business rule -> possible enforcement location -> risk -> access pattern -> tradeoff
```

Students should see that not every rule belongs in the same place and not every performance improvement is automatically worth the complexity.

---

# Step 1 - Business Rule List

Start with plain-language rules.

```text
1. A review must connect one customer to one product.
2. A rating must be within the allowed range.
3. A customer may have only one active review per product.
4. An order item must preserve the purchase-time item price.
5. A product may appear in multiple categories.
```

---

# Step 2 - Rule Placement Table

| Business Rule | Possible Enforcement Location | Why | Risk or Limitation |
| --- | --- | --- | --- |
| Review connects one customer and one product | Database/model structure + application/backend | The model requires both relationships; app guides valid creation | If only handled by user process, invalid reviews may appear |
| Rating stays in allowed range | Database constraint or application/backend | Simple validation rule | If only in UI, bad data may enter through other paths |
| One active review per customer/product | Mixed: model rule + application/backend | Needs relationship awareness and workflow handling | Rule may change if edits or review history are allowed |
| OrderItem preserves item_price | Model structure | Purchase-time price is part of the order event | If only product price is stored, historical orders become inaccurate |
| Product may appear in multiple categories | Model structure | ProductCategory supports the rule | Adds complexity if the scenario only needs one category |

Instructor note:

```text
Students are not implementing constraints yet. They are deciding where responsibility seems to belong.
```

---

# Step 3 - Access Pattern Pressure

Access pattern:

```text
Show a product listing page with product name, current price, primary category, average rating, and review count.
```

Possible pressure:

```text
The system may need to repeatedly summarize review ratings for many products.
```

Possible tradeoff:

```text
Store an average_rating and review_count summary on Product or in a product summary area.
```

Risk:

```text
Stored summaries can become stale if review data changes and the summary is not updated responsibly.
```

---

# Step 4 - AI Critique Prompt

```text
I am deciding where to enforce business rules and whether to consider a performance tradeoff in an e-commerce model.

Rules:
1. A review must connect one customer to one product.
2. A rating must be within the allowed range.
3. A customer may have only one active review per product.
4. OrderItem must preserve purchase-time item_price.
5. A product may appear in multiple categories.

Access pattern:
The product listing page may need product name, current price, primary category, average rating, and review count.

Possible tradeoff:
Store average_rating and review_count as summary values for faster product listing.

Critique this reasoning.

Do not write SQL.
Do not design implementation code.

Identify:
1. which rule placement choices seem reasonable,
2. which rule needs mixed enforcement,
3. what could go wrong with stored summary values,
4. whether the performance tradeoff is appropriate at a beginner modeling level,
5. one question a human designer should answer before accepting the tradeoff.
```

---

# Step 5 - Prepared AI Output Excerpt

```text
Reasonable placement:
- Rating range can be enforced through validation and possibly a database-level rule later.
- OrderItem item_price belongs in the model because it preserves historical purchase facts.

Mixed enforcement:
- One active review per customer/product may need both model support and application workflow rules.

Stored summary risk:
- average_rating and review_count can become stale if reviews are added, edited, or removed without updating the summary.

Appropriate tradeoff:
- It is reasonable to discuss as a performance tradeoff, but students should not implement it yet.

Human question:
- How often are product listings viewed compared with how often reviews change?
```

---

# Step 6 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Rating range validation | Accept | Simple rule placement example. |
| OrderItem item_price belongs in model | Accept | This protects historical meaning. |
| Review uniqueness needs mixed enforcement | Accept | Good example of model plus workflow. |
| Stored summary may become stale | Accept | This is the core denormalization risk. |
| Implement stored summary now | Reject | Week 5 asks for reasoning, not implementation. |

---

# Step 7 - Final Tradeoff Explanation

```text
Storing average_rating and review_count could make product listing faster or simpler to display, but it duplicates information that can be calculated from Review records. The tradeoff may be worth considering if product listings are frequent and review changes are less frequent. A human designer must decide how the summary will stay accurate.
```

---

# Student Transfer

Students should identify rules in their own scenario and explain one access pattern that could create performance pressure.

Transfer bridge:

```text
In the demo, we separated rule placement from performance tradeoff.
In your assignment, you will decide where rules belong and explain one tradeoff without jumping into implementation.
```

