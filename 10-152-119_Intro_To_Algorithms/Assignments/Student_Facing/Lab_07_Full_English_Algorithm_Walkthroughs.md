# LAB 7 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 7 - Similarity, Clustering, Recommendation, and Hashing**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 7 option choices before writing code or creating visible evidence.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how small data choices can support similarity, ranking,
grouping, recommendation, or hashing behavior.

---

# How To Use This Artifact

For your chosen option:

1. Read the matching walkthrough.
2. Create a small data set with at least six items.
3. Describe how the data is represented.
4. Choose the algorithm idea you will demonstrate.
5. Create visible evidence such as a table, matrix, grouping, or hash
   comparison.
6. Explain at least two assumptions.
7. Explain at least one limitation or risk.

Do not copy the wording directly as your final answer. Your submitted work must
include your own data set, representation explanation, implementation or
simulation, visible evidence, assumptions, limitation, AI/data connection, and
AI-use note if applicable.

---

# What Makes This A Data/AI Bridge Lab?

Many AI and analytics systems begin with ordinary algorithmic choices.

Before a system can rank, recommend, group, or verify something, the data has
to be represented in a usable form. The algorithm then uses that representation
to produce a result.

The result is not magic. It depends on the data, the representation, the
comparison method, and the assumptions.

---

# Option 1 - Similarity Ranking

First, create a small set of items. Each item should have features that can be
compared. Features may be tags, categories, skills, genres, ingredients, or
numeric values.

Then choose one target item or profile to compare against the others.

For each candidate item, compare its features to the target. If using tags, you
might count shared tags. If using numeric features, you might calculate a
simple distance or difference.

Record a score for each candidate item.

Sort or list the candidates by score so the most similar items appear first.

Questions to guide your evidence:

- What features are used for comparison?
- Are all features equally important?
- What does a high score mean?
- What important information is missing from the representation?

---

# Option 2 - Simple Clustering

First, create a small set of items that can be grouped. The items may be points,
products, learners, tasks, or resources.

Then choose the features that will determine closeness. For points, closeness
may be based on x/y position. For tagged items, closeness may be based on
shared tags.

Compare items and decide which ones belong together.

Create a visible grouping table or simple diagram showing which items are in
each group.

Explain why those groups make sense according to your chosen features.

Questions to guide your evidence:

- What features define closeness?
- How many groups did you create?
- Could a different feature choice change the groups?
- What does the grouping not prove?

---

# Option 3 - Tiny Recommendation

First, define a user profile. The profile should include preferences, needs, or
features the user cares about.

Then create a small set of possible recommendations. Each item should have
features that can be compared to the user profile.

For each item, compare its features to the profile. Give points for matches or
calculate a simple score.

Rank the items from strongest match to weakest match.

Return the top recommendation and show the evidence for why it ranked highest.

Questions to guide your evidence:

- What does the user profile include?
- Which features count most?
- What score does each item receive?
- What could make the recommendation misleading?

---

# Option 4 - Hashing Demonstration

First, create a small set of text records, file names, messages, or identifiers.

Then choose what hashing will demonstrate. It may show lookup, identity, or
integrity checking.

For an integrity check, store an expected hash for each original record. Then
compare it to the hash of a later version. If the hash matches, the content is
probably unchanged. If the hash does not match, the content has changed.

For lookup, hash keys can help map a value to a storage location or dictionary
entry. For this beginner lab, keep the explanation conceptual and visible.

Questions to guide your evidence:

- What value is being hashed?
- What does a matching hash suggest?
- What does a changed hash suggest?
- What does hashing not explain about the meaning of the data?

---

# Choosing Your Evidence Format

Choose the evidence that fits your option.

Useful formats include:

- ranking table
- similarity score table
- similarity matrix
- cluster grouping table
- simple scatter plot
- hash comparison table
- before/after representation table

The evidence should make the algorithm visible. A reader should be able to see
how the result was produced.

---

# Assumptions And Limits

Every option needs assumptions and limitations.

Assumptions may include:

- the selected features are meaningful
- shared tags indicate similarity
- the user profile is accurate
- the data set is large enough to demonstrate the idea
- the chosen score represents the intended concept

Limitations may include:

- the data set is too small for strong conclusions
- important features are missing
- all features are weighted equally
- similarity does not prove quality
- a hash match checks identity, not usefulness or truth

---

# Your Turn

After reading the walkthrough for your option, build your own small data set and
make the result visible.

Your next step is not to build a full AI system. Your next step is to show how
one small algorithmic idea can support AI, analytics, or data modeling.
