# FUTURE DESIGN NOTE - THIRD-PARTY DATA PACKAGES

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This note preserves a possible future enhancement for the algorithm lab system:
introducing selected third-party Python packages after the lecture materials
are more fully developed.

This is not part of the current required lab scope.

---

# Current Decision

The current lab progression should remain focused on:

- algorithmic reasoning
- visible evidence
- comparison of approaches
- explanation of assumptions and limitations
- standard-library Python first

Third-party numeric or data packages should not be added simply to make the
labs look more advanced.

The tool should enter only when the lecture context explains why it matters.

---

# Possible Later Packages

Potential future additions include:

- `numpy` for arrays, vector-like representations, and numerical similarity
- `pandas` for tabular data inspection and lightweight data analysis
- `scipy` for distance metrics or more formal numerical comparison
- `matplotlib` for optional visualization of timing, ranking, or clustering
- `networkx` for graph modeling or traversal visualization

These should be introduced only when they support the course outcome and do not
replace the student's responsibility to explain the algorithmic idea.

---

# Possible Placement

The most natural placement is likely after or during:

- Lab 06 graph modeling, if graph visualization becomes useful
- Lab 07 similarity, ranking, hashing, or AI/data bridge work
- optional instructor demos or enrichment tracks
- later lecture material on vectors, features, tabular data, similarity, or
  data modeling

---

# Instructional Boundary

The package should not become the lesson.

Students should first understand:

```text
problem -> representation -> algorithm -> evidence -> explanation
```

Then a package can be shown as a tool that makes part of the work easier,
clearer, faster, or more scalable.

---

# Dependency Convention

If a future lab or demo uses a third-party package:

1. Add the package to `Assignments/requirements.txt`.
2. Document the dependency in the lab's instructor notes.
3. Explain what the package contributes.
4. Preserve a clear conceptual explanation that does not depend on the package.
5. Avoid requiring students to use the package unless the assignment explicitly
   teaches that tool.

---

# Current Status

Deferred until lecture materials are fleshed out.

The current third-party dependency is `rich`, used only for optional instructor
presentation/refinement examples in Lab 07.
