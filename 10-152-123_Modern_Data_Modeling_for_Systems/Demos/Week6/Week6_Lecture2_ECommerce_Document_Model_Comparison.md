# Week 6 Lecture 2 Demo - E-commerce Document Model Comparison

Course: `10-152-123 Modern Data Modeling for Systems`  
Lecture focus: Document data modeling  
Demo scenario: E-commerce with reviews/ratings  
Primary tangible: Embedded/reference comparison and relational vs document tradeoff table

---

# Demo Purpose

This demo shows that MongoDB document design is a modeling choice, not a conversion trick.

The movement is:

```text
access pattern -> document option -> embedding/reference tradeoff -> representation decision
```

Students should compare what each representation makes easier and harder.

---

# Step 1 - Two Document Options

## Option A - Product-Centered Document with Recent Review Snapshots

```json
{
  "_id": "prod_1001",
  "name": "Trail Mug",
  "current_price": 14.99,
  "rating_summary": {
    "average_rating": 4.6,
    "review_count": 18
  },
  "recent_reviews": [
    {
      "review_id": "rev_501",
      "customer_id": "cust_77",
      "rating": 5,
      "comment": "Keeps coffee warm during morning hikes."
    }
  ]
}
```

## Option B - Product Document with Review References

```json
{
  "_id": "prod_1001",
  "name": "Trail Mug",
  "current_price": 14.99,
  "category_ids": ["cat_drinkware", "cat_camping"],
  "rating_summary": {
    "average_rating": 4.6,
    "review_count": 18
  },
  "recent_review_ids": ["rev_501", "rev_498", "rev_492"]
}
```

Possible separate review document:

```json
{
  "_id": "rev_501",
  "product_id": "prod_1001",
  "customer_id": "cust_77",
  "rating": 5,
  "comment": "Keeps coffee warm during morning hikes.",
  "review_date": "2026-02-04"
}
```

---

# Step 2 - Embedded vs Referenced Comparison

| Design Choice | Makes Easier | Makes Harder | Duplication / Update Concern |
| --- | --- | --- | --- |
| Embed recent review snapshots | Product detail display | Updating review text in all places | Review data may duplicate full review records |
| Reference review IDs | Review updates and full review records | Product detail may need additional retrieval | Product page depends on another collection |
| Embed category snapshots | Product browsing display | Category rename updates | Category labels may become stale |
| Reference category IDs | Category maintenance | Display needs lookup or stored label elsewhere | Less duplication, more retrieval work |

---

# Step 3 - Relational vs Document Tradeoff Table

| Question | Relational/Table-Shaped Representation | Document-Shaped Representation |
| --- | --- | --- |
| Where are product facts? | Product table/entity | Product document |
| Where are review facts? | Review table/entity linked to Product and Customer | Embedded review snapshots or separate review documents |
| What is easy? | Keeping facts in stable homes | Reading product-centered data together |
| What is harder? | Product detail may require assembling related records | Avoiding stale duplicated/summarized data |
| Main risk | Too many joins/lookups later, depending on implementation | Over-embedding or duplicating changing data |
| Best fit when | Consistency and independent updates matter most | Product-centered retrieval is frequent and bounded |

---

# Step 4 - AI Critique Prompt

```text
I have two possible MongoDB document designs for an e-commerce product detail use case.

Access pattern:
Show product name, price, categories, average rating, review count, and recent reviews.

Option A:
Product document embeds recent review snapshots.

Option B:
Product document stores recent_review_ids and keeps reviews in separate review documents.

Critique the tradeoffs.

Do not compare SQL syntax to MongoDB syntax.
Do not choose only based on which document looks simpler.

Compare:
1. what each design makes easier to read,
2. what each design makes harder to update,
3. where duplication may appear,
4. which design better fits the stated access pattern,
5. what human design question should be answered before choosing.
```

---

# Step 5 - Prepared AI Output Excerpt

```text
Option A:
- Easier for product detail display because recent review text is already in the product document.
- Harder if reviews can be edited or need to appear consistently in many places.

Option B:
- Easier to maintain review records independently.
- Harder for product detail display because review details must be retrieved separately.

Duplication:
- Option A duplicates review data.
- Both options may duplicate rating_summary if it is stored instead of calculated.

Fit:
- Option A fits a bounded "recent reviews" display if only a few review snapshots are embedded.

Human question:
- How many reviews are shown on the product page, and how often are reviews edited after posting?
```

---

# Step 6 - Instructor Review Labels

| AI Suggestion | Review Label | Reason |
| --- | --- | --- |
| Option A helps product detail | Accept | Tied to access pattern. |
| Option A creates update concern | Accept | Embedded snapshots need maintenance. |
| Option B helps independent review maintenance | Accept | Good referencing rationale. |
| Both may duplicate rating summary | Accept | Connects to Week 5 tradeoff. |
| Choose based only on simpler-looking JSON | Reject | Simplicity must be tied to system need. |

---

# Step 7 - Final Representation Decision

```text
For the product detail access pattern, Option A is acceptable if recent_reviews is a small bounded snapshot and Review remains the source of truth elsewhere. The model must document the update responsibility for rating_summary and recent review snippets.
```

---

# Student Transfer

Students should create at least two sample documents or document variants and compare them to their relational/table-shaped model.

Transfer bridge:

```text
In the demo, we compared two document shapes against one access pattern.
In your assignment, you will compare representation choices against your scenario's access patterns.
```

