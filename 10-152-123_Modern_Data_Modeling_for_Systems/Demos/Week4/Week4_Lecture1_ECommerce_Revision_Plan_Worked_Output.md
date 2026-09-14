# Week 4 Lecture 1 Worked Output - E-commerce Revision Plan

Course: `10-152-123 Modern Data Modeling for Systems`  
Scenario: E-commerce with reviews/ratings

---

# Evidence Review

| Evidence Source | Finding | Revision Implication |
| --- | --- | --- |
| Week 1 questions | Product categories may not be simple | Revisit Category/Product relationship |
| Week 2 process map | Product browsing depends on category organization | Category design affects user behavior |
| Week 3 ERD | Product has one Category | Current model may be too restrictive |
| Week 3 assumptions | Payment/shipment/inventory excluded | Keep boundary visible |

---

# Model Issue List

| Issue | Why It Matters | Planned Response |
| --- | --- | --- |
| Product-to-category may need many-to-many support | Products often appear in multiple browsing categories | Add ProductCategory as associative entity |
| Duplicate reviews need a rule | Review data may become messy without a rule | Add rule note for one active review per customer/product |
| Review eligibility is unclear | Purchase verification may matter later | Document as boundary question |
| Payment/shipment/inventory pressure exists | Real system needs them eventually | Defer from Week 4 scope |

---

# Revision Plan

```text
Revision 1:
Replace the direct Category-to-Product assumption with a ProductCategory associative entity.

Intended improvement:
This supports products appearing in multiple categories without duplicating product records.

Revision 2:
Add a plain-language rule that a customer may have one active review per product.

Intended improvement:
This clarifies the Customer/Product/Review relationship without adding unnecessary entities.

Deferred issue:
Do not add Payment, Shipment, or Inventory yet.

Reason:
Those areas are important, but adding all of them now would distract from the Week 4 goal of deliberate model refinement.
```

---

# Change Log Draft

| Change | Reason | Expected Benefit |
| --- | --- | --- |
| Add ProductCategory | Product/Category may be many-to-many | More flexible product browsing model |
| Add review duplicate rule | Review relationship needs clearer constraint | Cleaner review data |
| Keep payment/shipment/inventory out | Scope control | Model remains focused |

