# Week 5 Lecture 1 Worked Output - E-commerce Anomaly Analysis

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Risky Excerpt Reviewed

```text
OrderItemDetail(order_id, order_date, customer_email, customer_name,
product_id, product_name, category_name, quantity, item_price)
```

---

# Anomaly/Risk Table

| Risk Type | Where It Appears | What Could Go Wrong | Cause | Recommended Improvement |
| --- | --- | --- | --- | --- |
| Update anomaly | `customer_name` repeated across order-item rows | Customer name may be changed in one row but not another | Customer facts are stored with order-line facts | Store customer facts with Customer |
| Update anomaly | `product_name` and `category_name` repeated | Product/category wording may become inconsistent | Product facts are repeated in transaction rows | Store product facts with Product and category facts with Category |
| Insert anomaly | New product has no natural place unless ordered | Catalog cannot represent products before purchase | Product facts depend on order rows | Product should exist independently |
| Delete anomaly | Deleting last row for a product removes product/category meaning | Transaction cleanup could erase catalog facts | Catalog facts are trapped in order-item rows | Keep product/category facts separate from order history |

---

# Normalization Awareness Explanation

```text
Normalization would help because the excerpt repeats customer, product, and category facts inside order-item rows. Separating these facts reduces inconsistency and makes each entity responsible for one kind of information.
```

---

# Structural Recommendation

```text
Use separate structures for Customer, Order, OrderItem, Product, Category, and ProductCategory.

OrderItem should keep order-specific line facts such as quantity and item_price.

OrderItem should not store customer_name, customer_email, product_name, or category_name as its main source of truth.
```

---

# Tradeoff Note

```text
The more normalized version is cleaner for maintenance, but it requires readers to understand more relationships. That is acceptable here because the repeated facts create clear update, insert, and delete risks.
```

