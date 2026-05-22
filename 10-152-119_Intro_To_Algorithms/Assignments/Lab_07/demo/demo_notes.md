# LAB 07 DEMO NOTES - SIMILARITY, RANKING, AND HASHING

**Demo Title:** Tiny Music Recommendation by Tag Similarity
**Related Lab:** Lab 07 - Similarity, Ranking, and Hashing
**Concept Transfer Target:** Make a small AI/data ranking visible and explain the assumptions behind it
**Estimated Time:** 12-15 minutes

---

# Assumptions

- creating a fresh `Assignments/Lab_07/` package
- treating the student-facing Lab 07 file as authoritative
- using a generic starter rather than a scenario-specific starter
- using a tiny music recommendation example for the demo and a different option
  for the plain success version
- using an item-feature table and ranking table as the visible evidence
- using light ANSI color in the demo because it clarifies the top-ranked item
  and the section boundaries, with a `NO_COLOR` fallback
- creating an optional colorized success version because the user explicitly
  requested it and the selected success option supports meaningful visual
  distinctions

---

# Opening Frame

Today we are moving from classic algorithms to a small AI/data bridge activity.
The goal is to show that a recommendation or ranking can look persuasive, but it
still depends on how the data is represented and how similarity is defined.

---

# Demo Problem

Create a tiny music recommendation example.

Represent songs with simple tags such as genre, mood, tempo, and instrument.
Compare one reference song to several candidate songs using a basic similarity
score based on shared tags.

---

# What Students Should Notice

- representation choices shape the result
- similarity is a design choice, not an objective truth
- a ranking can look authoritative even when the data is limited
- a useful algorithm can still leave out important context
- a top recommendation is only as good as the chosen features and scoring rule

---

# Demo Evidence

Run `demo_code.py` to produce:

- a feature table showing how each song is represented
- a ranking table of candidate songs by similarity score
- a short assumption and limitation summary

The demo uses light ANSI color to highlight section headers and the strongest
match in the ranking output. The color is a presentation aid only and not part
of the assessed student requirement.

Optional Rich demo:

`optional_rich_demo_code.py` presents the same demo logic using Rich tables and
panels. Use it when you want to explicitly compare lightweight ANSI output with
a third-party formatted console presentation.

---

# Transfer Bridge

> In the demo, we ranked songs by similarity using simple tags. In the lab,
> students will use a different data set or another approved AI/data option and
> explain what their result can and cannot claim.

---

# Stop Point

Stop after ranking a few candidate songs and discussing the assumptions behind
the score. Do not turn the demo into a full student solution for the same data
set.

---

# Likely Misconceptions

- students may assume a similarity score is objective rather than designed
- students may ignore that missing features change the ranking
- students may overstate what a small ranking proves
- students may focus on the top item without explaining the representation
  choice that produced it

---

# Instructor Notes

- Keep the number of songs small so students can inspect the ranking manually.
- Emphasize that the tags are a simplified representation, not the songs
  themselves.
- Use the limitation note to show that recommendation logic can still be useful
  without being complete.
- Ask students what feature they would add or remove and how that would change
  the ranking.
- Future lecture development may add optional `numpy`, `pandas`, or related
  package demos after the conceptual similarity/ranking foundation is clear.
