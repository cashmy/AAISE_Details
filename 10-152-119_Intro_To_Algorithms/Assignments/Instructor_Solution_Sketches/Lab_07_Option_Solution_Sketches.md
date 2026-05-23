# LAB 07 OPTION SOLUTION SKETCHES

**Lab:** Similarity, Ranking, and Hashing  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches support evaluation of the Lab 07 option paths. They are not
student-facing walkthroughs and are not full runnable solution packages.

For Lab 07, a strong submission makes a small AI/data idea visible without
overclaiming what the result proves. Representation, assumptions, and
limitations matter as much as the output.

---

# Common Required Evidence

Every option should include:

- selected option
- data set with at least six items
- representation explanation
- implementation or clear simulation
- visible evidence
- at least two assumptions
- at least one limitation or risk
- AI/data/analytics connection
- AI-use note if applicable

Acceptable evidence formats:

- similarity matrix
- ranking table
- cluster grouping table
- scatter plot
- hash value comparison
- before/after representation table

---

# Option 1 - Similarity Ranking

## Viable Framing

Compare items using shared tags or numeric features and rank them by similarity
to a target.

## Expected Representation

Items may be represented as sets of tags, dictionaries of numeric features, or
small vectors.

## Expected Evidence

Ranking table with item, score, shared features or distance, and rank.

## Expected Assumptions

- selected features represent meaningful similarity
- score treats features consistently
- higher score or lower distance means closer match

## Expected Limitation

Similarity score does not prove quality, usefulness, or user preference.

## Grading Watch-Fors

- Student ranks items but does not explain representation.
- Student changes scoring rules midstream.
- Student overstates the ranking as objectively correct.

## Runnable Expansion Note

The secondary Lab 07 success package may cover a similarity/resource option.
Use it as a model if a full runnable version is needed.

---

# Option 2 - Simple Clustering

## Viable Framing

Group items or points based on closeness.

## Expected Representation

Use numeric points, simple feature pairs, or tag sets. Keep the representation
small enough to explain.

## Expected Evidence

Cluster grouping table, scatter plot, or distance table.

## Expected Assumptions

- chosen features define closeness
- selected number of groups is reasonable for the example
- distance or shared-feature rule matches the stated goal

## Expected Limitation

Different features or a different number of groups could change the clusters.

## Grading Watch-Fors

- Student groups by intuition only and does not show evidence.
- Student calls clusters "true categories" instead of algorithmic groupings.
- Student uses more complexity than they can explain.

## Runnable Expansion Note

Use six to eight two-dimensional points. Group manually by distance to simple
centers or by visible closeness. Avoid introducing advanced library dependency
unless intentionally chosen.

---

# Option 3 - Tiny Recommendation

## Viable Framing

Rank possible recommendations based on a user profile.

## Expected Representation

User profile as tags, preferences, or weighted features. Candidate items use
the same feature language.

## Expected Evidence

Recommendation table with item, matching features, score, and rank.

## Expected Assumptions

- profile accurately represents user needs
- feature matches are meaningful
- weights or points are justified

## Expected Limitation

Recommendation may ignore context, quality, novelty, or factors not included
in the profile.

## Grading Watch-Fors

- Student creates recommendations without showing scoring.
- Student does not explain why the top item ranked highest.
- Student treats the result as personalized truth rather than a simple model.

## Runnable Expansion Note

Use six candidate resources, tools, songs, meals, or study supports. Score each
candidate by shared features with the user profile.

---

# Option 4 - Hashing Demonstration

## Viable Framing

Use hashing to show identity, lookup, or integrity checking.

## Expected Representation

Small set of text records, file names, messages, or identifiers. For integrity,
store original and current values.

## Expected Evidence

Hash comparison table with item, expected hash, current hash, and match status.

## Expected Assumptions

- same hash function is applied consistently
- exact content equality is the intended signal
- a hash mismatch means the content changed

## Expected Limitation

Hashing can show that content changed, but it does not explain whether the
change is meaningful, harmful, or correct.

## Grading Watch-Fors

- Student thinks hashing encrypts the content.
- Student does not explain what a mismatch means.
- Student uses hash values without any visible comparison table.

## Runnable Expansion Note

The existing Lab 07 success package implements a hashing integrity-checking
version.

---

# Cross-Option Grading Calibration

Strong work should:

- make representation explicit
- provide visible evidence
- include assumptions and limitations
- connect the small activity to AI, analytics, or data modeling
- avoid overstating what a small data set proves
