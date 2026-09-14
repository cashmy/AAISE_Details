# Week 2 Lecture 1 Worked Output - E-commerce Relational Structure

Course: `10-152-123 Modern Data Modeling for Systems`  
Demo scenario: E-commerce with reviews/ratings  
Status: Instructor worked example

---

# 1. Starting Point

System intent:

```text
The system supports customers browsing products, purchasing products, and leaving feedback that helps other customers evaluate products.
```

Entities carried forward:

```text
Customer
Product
Order
OrderItem
Review
Category
```

Boundary entities:

```text
Payment
Shipment
Inventory
StaffUser
```

---

# 2. Entity / Attribute / Key Table

| Entity | Purpose | Important Attributes | Primary Key Candidate | Notes or Questions |
| --- | --- | --- | --- | --- |
| Customer | Person who buys products and writes reviews | name, email | customer_id | Email should probably be unique |
| Product | Item available for purchase | name, description, current_price | product_id | Category relationship needs clarification |
| Order | Purchase event made by a customer | order_date, status | order_id | Total may be calculated from order items |
| OrderItem | Product line inside an order | quantity, item_price | order_item_id | item_price preserves purchase-time price |
| Review | Customer feedback about a product | rating, comment, review_date | review_id | Rating needs allowed range |
| Category | Product grouping | category_name | category_id | One-to-many or many-to-many is still a question |

---

# 3. Relationship Link Table

| From Entity | Relationship Phrase | To Entity | Relationship Type | Foreign Key or Link Candidate | Notes or Questions |
| --- | --- | --- | --- | --- | --- |
| Customer | places | Order | one-to-many | Order.customer_id | One customer can place many orders |
| Order | contains | OrderItem | one-to-many | OrderItem.order_id | One order can have many order items |
| Product | appears in | OrderItem | one-to-many | OrderItem.product_id | One product can appear in many order items |
| Customer | writes | Review | one-to-many | Review.customer_id | One customer can write many reviews |
| Product | receives | Review | one-to-many | Review.product_id | One product can receive many reviews |
| Category | groups | Product | one-to-many for now | Product.category_id | Revisit if products can have multiple categories |

---

# 4. Plain-Language Integrity Constraints

```text
1. An order must belong to one customer.
2. An order item must belong to one order.
3. An order item must refer to one product.
4. A review must connect to one customer and one product.
5. A rating should be within the allowed range, such as 1-5.
6. Customer email should be unique if it identifies a customer account.
7. Order item price should preserve the purchase-time price, even if current product price changes later.
```

---

# 5. AI Assistance Notes

## Manual Work Completed Before AI

```text
I created the entity/attribute/key table, relationship link table, and first integrity constraints before asking AI for critique.
```

## Prompt Used

```text
Here is my draft relational structure for an e-commerce model.

Entities and key candidates:
- Customer(customer_id): name, email
- Product(product_id): name, description, price
- Order(order_id): order_date, status
- OrderItem(order_item_id): quantity, item_price
- Review(review_id): rating, comment, review_date
- Category(category_id): category_name

Relationship links:
- Order.customer_id links Order to Customer
- OrderItem.order_id links OrderItem to Order
- OrderItem.product_id links OrderItem to Product
- Review.customer_id links Review to Customer
- Review.product_id links Review to Product
- Product.category_id may link Product to Category

Critique this as a reviewer. Do not rewrite the whole model.

Look for:
1. weak or unclear primary key choices,
2. missing foreign key relationships,
3. attributes that may belong on a different entity,
4. relationship types that need clarification,
5. integrity constraints I should write in plain language.

Keep feedback introductory and explain why each issue matters.
```

## Most Useful AI Suggestion

```text
AI suggested preserving item_price on OrderItem so historical orders do not change when current product prices change.
```

## Suggestion I Rejected

```text
AI suggested adding Payment, Shipment, and Inventory immediately.
```

## Change I Made After Reviewing AI

```text
I kept Payment, Shipment, and Inventory as boundary questions, added item_price to OrderItem, and added constraints for rating range and email uniqueness.
```

## What I Verified Myself

```text
I verified that each relationship supports the current scope: browsing, ordering, and reviewing.
```

