# RBA Case Observation - Batching and Compression Bias

**Workspace:** 10-152-117 Python Programming  
**Context:** Slide deck source generation and refactoring  
**Observation Type:** Process / quality-control heuristic  
**Status:** Captured for future course-design sessions

---

# Core Observation

During the Python 117 slide deck refactor, Weeks 1-4 were generated and reviewed
one deck at a time. Each day-level deck received its own focused generation
cycle, human inspection point, and opportunity for corrective steering.

Weeks 5 and 6 were then generated through a broader request that covered both
weeks at once. The resulting artifacts preserved the major topic coverage, but
showed a noticeable loss of instructional scaffolding:

- missing or weakened `Today's Success Pattern` slides
- absent or sparse `Transition Cue` sections
- thinner instructor handoff notes
- incomplete demo-file path guidance
- slimmer image-prompt support
- reduced preservation of the lecture-flow architecture established in prior
  weeks

The issue was not that the generated material was globally wrong. The issue was
that the supporting instructional architecture compressed.

---

# Interpretation

The broader generation request appears to have introduced a form of compression
bias. The model optimized for completing a larger content span, which preserved
obvious topical coverage but weakened less-visible structural elements.

Those less-visible elements are pedagogically important. They preserve:

- instructor flow
- memory jogging for future delivery
- transitions between concepts
- demo-to-lab alignment
- cognitive load management
- handoff quality for other instructors

In other words, the content survived more strongly than the scaffolding.

---

# RBA Significance

This is a useful RBA pattern because it shows that artifact quality is affected
by the unit size of generation.

When an artifact contains dense human judgment, instructional sequencing, and
multiple layers of purpose, batching can increase speed while decreasing
structural fidelity.

The correct unit of generation should therefore be based not only on topic
quantity, but on the amount of design structure that must be preserved.

For Python 117 slide deck source artifacts, the reliable unit appears to be:

> one day-level deck at a time

At most, a full week may be generated together only after a strong continuity
brief exists and the output is explicitly checked against it.

---

# Practical Rule

Generate dense instructional artifacts at the smallest unit where quality
structure must be preserved.

For future slide deck work:

1. Generate one day-level deck at a time when the deck includes demos,
   transitions, assignment alignment, or instructor handoff notes.
2. Use the continuity brief as an explicit governance artifact.
3. Validate each deck for:
   - `Today's Success Pattern`
   - review bridge
   - working set / skipped-for-now framing
   - transition cues
   - demo paths and instructor-use notes
   - assignment bridge
   - evidence expectations
   - image prompt coverage
4. Only batch multiple decks when the goal is rough discovery rather than
   production-ready instructional scaffolding.

---

# Course Impact

The Week 5 artifacts were repaired by restoring the missing scaffolding while
preserving the already-useful content. This reinforced a key course-production
lesson:

> Faster generation is only an advantage when the artifact preserves the layers
> that make it teachable.

This observation should be carried forward into remaining Python 117 deck work
and into future course artifact generation.

