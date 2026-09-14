# Week 5 Lecture 1 Demo - E-commerce Normalization and Anomalies

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Normalization awareness  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Anomaly/risk table and normalization recommendation

---

# Demo Purpose

This demo shows that a model can look understandable but still create maintenance risks.

The movement is:

```text
risky model excerpt -> anomaly risk -> cause -> possible improvement -> tradeoff
```

Students should understand normalization as a model-quality lens, not a memorized ritual.

---

# Starting Point from Week 4

The refined E-commerce model includes:

```text
Customer
Order
OrderItem
Product
Review
Category
ProductCategory
```

Week 5 starts by intentionally showing a simplified risky version of part of the model.

---

# Step 1 - Risky Model Excerpt

Show this as a deliberately flawed table-shaped excerpt.

```text
OrderItemDetail
--------------------------------------------------------------
order_id
order_date
customer_email
customer_name
product_id
product_name
category_name
quantity
item_price
```

Sample records:

| order_id | order_date | customer_email | customer_name | product_id | product_name | category_name | quantity | item_price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1001 | 2026-02-03 | alex@example.com | Alex Rivera | P10 | Trail Mug | Drinkware | 2 | 14.99 |
| 1001 | 2026-02-03 | alex@example.com | Alex Rivera | P22 | Camp Spoon | Kitchen | 1 | 5.99 |
| 1002 | 2026-02-04 | alex@example.com | Alex Rivera | P10 | Trail Mug | Drinkware | 1 | 14.99 |

Instructor note:

```text
This is not a recommended final model. It is a teaching excerpt designed to make anomaly risks visible.
```

---

# Step 2 - Manual Anomaly/Risk Table

| Risk Type | Where It Appears | What Could Go Wrong | Cause |
| --- | --- | --- | --- |
| Update anomaly | Customer name appears on multiple order-item rows | If Alex changes their name, several rows must be updated consistently | Customer data is repeated with order item data |
| Update anomaly | Product name/category appears on repeated product rows | Product details could become inconsistent across past orders | Product data is repeated in transactional rows |
| Insert anomaly | Cannot record a new product until it appears in an order | Product catalog depends on order activity | Product and order-item information are mixed |
| Delete anomaly | Deleting the only order row for a product could remove product/category information | Losing order history could erase catalog facts | Product facts are not stored separately |

---

# Step 3 - Normalization Recommendation

Recommended improvement:

```text
Separate repeated facts into their own entities:

Customer
Order
OrderItem
Product
Category
ProductCategory
```

Keep on `OrderItem`:

```text
order_item_id
order_id
product_id
quantity
item_price
```

Do not keep on `OrderItem`:

```text
customer_name
customer_email
product_name
category_name
```

Instructor note:

```text
The point is not to chant normal forms. The point is to ask: What fact is being repeated, and what could break because of that repetition?
```

---

# Step 4 - AI Critique Prompt

```text
Here is a simplified table-shaped excerpt from an e-commerce model:

OrderItemDetail:
- order_id
- order_date
- customer_email
- customer_name
- product_id
- product_name
- category_name
- quantity
- item_price

I think this design may create update, insert, and delete anomalies because customer and product facts are repeated inside order-item rows.

Critique my anomaly analysis.

Do not write SQL.
Do not redesign the whole database.

Identify:
1. one likely update anomaly,
2. one likely insert anomaly,
3. one likely delete anomaly,
4. whether normalization would help,
5. one risk of over-normalizing or making the model too complex for this course stage.
```

---

# Step 5 - Prepared AI Output Excerpt

```text
Update anomaly:
- If customer_name changes, it must be updated in every order-item row for that customer.

Insert anomaly:
- You may not be able to add a product to the catalog unless there is already an order row for it.

Delete anomaly:
- If the only row mentioning a product is deleted, product information may be lost.

Normalization:
- Separating Customer, Product, Order, and OrderItem would reduce repeated facts.

Over-normalization risk:
- Splitting every small descriptive value into its own entity can make the model harder to understand without solving a real maintenance problem.
```

---

# Step 6 - Instructor Review Labels

| AI Suggestion | Review Label | Instructor Reasoning |
| --- | --- | --- |
| Customer update anomaly | Accept | Repeated customer facts are a clear maintenance risk. |
| Product insert anomaly | Accept | Catalog data should not depend on order activity. |
| Product delete anomaly | Accept | Deleting a transaction should not erase catalog meaning. |
| Separate Customer/Product/Order/OrderItem | Accept | This matches prior model structure. |
| Avoid splitting every value | Accept | Scope discipline still matters. |

---

# Step 7 - Final Demo Claim

```text
The risky excerpt mixes customer facts, product facts, category facts, and order-line facts into one structure. Normalization helps because each kind of fact should have a stable home. The tradeoff is that a more normalized model has more entities and relationships to understand.
```

---

# Student Transfer

Students should now inspect either their own model or an instructor-approved excerpt and identify one meaningful anomaly risk.

Transfer bridge:

```text
In the demo, we looked for repeated facts and asked what could break.
In your assignment, you will use the same reasoning to identify one maintenance risk and recommend a focused improvement.
```

