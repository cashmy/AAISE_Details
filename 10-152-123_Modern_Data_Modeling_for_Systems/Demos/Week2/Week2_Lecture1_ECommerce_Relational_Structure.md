# Week 2 Lecture 1 Demo - E-commerce Relational Structure

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Core relational concepts  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Entity/attribute/key/relationship table

---

# Demo Purpose

This demo shows how to sharpen a conceptual model into relational structure.

The movement is:

```text
conceptual entities -> attributes -> key candidates -> relationship links -> integrity constraints
```

Do not write SQL. Do not create a formal ERD yet.

---

# Starting Point from Week 1

Current E-commerce entities:

```text
Customer
Product
Order
OrderItem
Review
Category
```

Boundary questions:

```text
Payment
Shipment
Inventory
StaffUser
```

Relationship statements:

```text
Customer places Order.
Order contains OrderItem.
OrderItem refers to Product.
Customer writes Review.
Review is about Product.
Product belongs to Category.
```

---

# Step 1 - Manual Attempt

Create a first relational structure table in front of students.

Keep it reasonable but not perfect.

## Manual Entity / Attribute / Key Table

| Entity | Purpose | Important Attributes | Primary Key Candidate | Notes or Questions |
| --- | --- | --- | --- | --- |
| Customer | Person who buys products and writes reviews | name, email | customer_id | Should email be unique? |
| Product | Item available for purchase | name, description, price | product_id | Category relationship still unclear |
| Order | Purchase event | order_date, status | order_id | Total may be calculated later |
| OrderItem | Line item inside an order | quantity, item_price | order_item_id | Connects Order and Product |
| Review | Customer feedback about product | rating, comment, review_date | review_id | Should one customer review product once? |
| Category | Product grouping | category_name | category_id | Can product have multiple categories? |

## Manual Relationship Link Table

| From Entity | Relationship Phrase | To Entity | Relationship Type | Foreign Key or Link Candidate | Notes or Questions |
| --- | --- | --- | --- | --- | --- |
| Customer | places | Order | one-to-many | Order.customer_id | One customer can place many orders |
| Order | contains | OrderItem | one-to-many | OrderItem.order_id | One order can have many line items |
| Product | appears in | OrderItem | one-to-many | OrderItem.product_id | One product can appear in many order items |
| Customer | writes | Review | one-to-many | Review.customer_id | Customer may write many reviews |
| Product | receives | Review | one-to-many | Review.product_id | Product may receive many reviews |
| Category | groups | Product | one-to-many? | Product.category_id? | May become many-to-many later |

## Manual Integrity Constraints

```text
1. An order must belong to one customer.
2. An order item must belong to one order.
3. An order item must refer to one product.
4. A review must connect to one customer and one product.
5. A rating should stay within the allowed rating range.
```

---

# Step 2 - AI Critique Prompt

Show a prompt that asks AI to critique the structure, not write the model.

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

---

# Step 3 - Prepared AI Output Excerpt

```text
Useful suggestion:
- Email may need a uniqueness rule if it identifies customer accounts.

Relationship clarification:
- Category to Product may be one-to-many if each product has one category, but many-to-many if products can appear in multiple categories.

Possible missing attribute:
- OrderItem may need item_price to preserve the price at the time of purchase, even if Product.price later changes.

Integrity constraint:
- Review.rating should have an allowed range such as 1-5.

Possible overreach:
- Adding Payment, Shipment, and Inventory now may expand the model beyond the current assignment scope.
```

---

# Step 4 - Instructor Review Labels

| AI Suggestion | Review Label | Instructor Reasoning |
| --- | --- | --- |
| Email uniqueness rule | Accept | This is a clear integrity constraint. |
| Clarify Product-Category | Accept | The relationship type affects structure later. |
| Add item_price to OrderItem | Accept | This preserves historical purchase information. |
| Rating range constraint | Accept | This is a simple plain-language constraint. |
| Add Payment/Shipment/Inventory | Out of Scope | These remain boundary questions for now. |

---

# Step 5 - Finalized Lecture 1 Tangible

The finalized tangible is the revised relational structure table and relationship notes.

Instructor note:

```text
The important move is not "AI found the answer." The important move is that AI helped us notice questions and constraints we still had to judge.
```

Student transfer:

```text
Students now create the same kind of table for their selected scenario.
```

