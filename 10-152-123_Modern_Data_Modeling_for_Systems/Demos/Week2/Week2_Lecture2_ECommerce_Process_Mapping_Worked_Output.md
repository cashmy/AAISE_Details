# Week 2 Lecture 2 Worked Output - E-commerce Process Mapping

Course: `10-152-123 Modern Data Modeling for Systems`  
Demo scenario: E-commerce with reviews/ratings  
Status: Instructor worked example

---

# 1. Process-to-Data Map

| System Action or Process | Data Needed | Entities Involved | Relationship or Constraint Tested | Gap or Revision Found |
| --- | --- | --- | --- | --- |
| Customer views product detail | product name, description, current price, category, rating, review comments | Product, Category, Review, Customer | Product-Category, Product-Review, Review-Customer | Need review rating/date; inventory status is boundary question |
| Customer places order | customer, order date, order status, selected products, quantities, purchase-time prices | Customer, Order, OrderItem, Product | Customer-Order, Order-OrderItem, OrderItem-Product | OrderItem is necessary |
| Customer writes review | customer, product, rating, comment, review date | Customer, Product, Review | Customer-Review, Product-Review | Need duplicate-review rule |

---

# 2. Process-Driven Revision Note

What changed after mapping system actions to data?

```text
OrderItem moved from a likely entity to a required entity because the "Customer places order" process needs to support multiple products, quantities, and purchase-time prices inside one order.
```

Why did that change improve the model?

```text
It prevents the model from pretending an order directly contains only one product. It also gives the model a place to store quantity and item_price for each product in the order.
```

---

# 3. Added Plain-Language Constraints

```text
1. An order must belong to one customer.
2. An order item must belong to one order.
3. An order item must refer to one product.
4. A review must connect one customer to one product.
5. A review rating must be within the allowed range.
6. The duplicate-review rule must be decided before the model becomes formal.
```

---

# 4. Remaining Modeling Question

```text
Should products be limited to one category, or should products support multiple categories?
```

---

# 5. Boundary Questions

```text
Payment, shipment, and inventory are real e-commerce concerns, but they remain outside the current Week 2 model unless the course scope expands.
```

---

# 6. AI Assistance Notes

## Manual Work Completed Before AI

```text
I created the process-to-data map for viewing product details, placing an order, and writing a review before asking AI for critique.
```

## Prompt Used

```text
Here is a process-to-data map for an e-commerce model.

Current entities:
Customer, Product, Order, OrderItem, Review, Category

Mapped processes:
1. Customer views product detail.
2. Customer places order.
3. Customer writes review.

For each process, I listed data needed, entities involved, and relationships tested.

Critique the process-to-data map.

Do not rewrite the full model.

Identify:
1. system actions that may require missing data,
2. relationships that are being tested by the process,
3. constraints or rules I should state in plain language,
4. one reasonable revision or boundary question.

Keep feedback introductory and focused on data modeling.
```

## Most Useful AI Suggestion

```text
AI pointed out that the place-order process confirms the need for OrderItem.
```

## Suggestion I Rejected

```text
AI noted that inventory availability may matter for viewing products.
```

Why did you reject it?

```text
I did not reject it as unrealistic. I kept it as a boundary question because inventory is outside the current Week 2 model.
```

## Change I Made After Reviewing AI

```text
I made OrderItem required and added a duplicate-review rule question.
```

## What I Verified Myself

```text
I verified that the revised structure supports the three mapped processes without adding payment, shipment, or inventory prematurely.
```

