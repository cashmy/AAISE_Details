# Design Decision Log v2

## Purpose

This document records what was retained, revised, or set aside from the original
`10-152-119 Introduction to Algorithms` design-history files:

- `Course_Architecture.md`
- `Lab_Architecture.md`
- `WIDS_CCF_Reflection.md`

Those files helped establish the original intent, but the v2 course has moved
toward a textbook-guided, algorithmic-judgment model.

## Retained Design Intent

The v1 artifacts correctly identified that this course should not be a
traditional algorithm-name survey. The strongest retained ideas are:

- students must analyze problems before coding
- students must compare approaches rather than accept first answers
- correctness, efficiency, readability, and tradeoffs must be evaluated
- AI-generated output must be inspected and justified
- students need both manual capability and tool-aware adaptability
- communication and explanation are evidence of understanding

These ideas remain central to v2.

## Revised Design Direction

The v1 version leaned heavily toward an AI-native, dual-mode lab system where
each lab contained a manual solution, AI-assisted solution, comparison, and
adaptation layer.

The v2 course keeps the accountability structure but changes the emphasis:

```text
v1 emphasis: manual solution vs AI solution every week
v2 emphasis: algorithmic judgment first, AI used when it improves critique,
comparison, explanation, code revision, or assumption testing
```

This better matches the course description and the selected textbook:

- algorithms as structured problem-solving approaches
- common data structures
- Big-O and performance comparison
- debugging and refinement
- selected bridges to AI, analytics, and data modeling

## AI Progression Decision

The v2 course uses the bridge-program AI involvement model:

```text
Manual First -> AI-Assisted -> AI-Injected -> AI-Integrated
```

For `10-152-119`:

- Manual First is routine and expected.
- AI-Assisted is used for explanation, research, critique, and comparison.
- AI-Injected is selective and requires justification, testing, and explanation.
- AI-Integrated is optional or preview-level, not a course-wide requirement.

This preserves AI accountability without allowing AI use to dominate the
algorithmic learning target.

## Textbook Decision

The selected textbook, `50 Algorithms Every Programmer Should Know`, is broader
than the course.

v2 treats the book as:

- a required spine for Section 1 foundations
- a guided reference for selected strategy, graph, AI/data, and practical
  consideration topics
- an optional future-reference source for advanced AI, cryptography, data
  systems, and scale topics

The course does not attempt to cover all 50 algorithms.

## Lab Design Decision

The older lab architecture had a strong and useful repeated submission pattern:

```text
problem framing -> manual solution -> AI-assisted solution -> evaluation ->
adaptation
```

v2 generalizes this into:

```text
problem framing -> manual reasoning -> Python implementation/simulation ->
testing/evidence -> comparison/tradeoff explanation -> AI use when appropriate
```

This keeps consistency while allowing some labs to be primarily visual,
comparative, structural, or evidence-based rather than always dual-implementation
tasks.

## Visual/Tangible Learning Decision

The course should not become web-based by default, but it must make abstract
algorithm behavior visible.

Approved visible evidence forms include:

- console traces
- timing tables
- simple charts
- notebooks, if useful
- grid simulations
- graph diagrams
- traversal orders
- search/sort step tables
- similarity matrices
- clustering plots
- ranking tables

The test is whether the evidence helps students explain algorithm behavior.

## Artifact Disposition

The v1 design-history files have been accounted for as follows:

- `Course_Architecture.md`: superseded by
  `WIDS_Course_Competency_Framework_v2.md`,
  `Introduction_to_Algorithms_High_Level_Course_Plan_v2.md`, and this decision
  log.
- `Lab_Architecture.md`: superseded by `Lab_Progression_Ladder_v2.md`,
  `Rubric_Evaluation_v2.md`, and the AI progression notes in the v2 high-level
  plan.
- `WIDS_CCF_Reflection.md`: retained as historical rationale but superseded by
  this decision log and the v2 curation map.

The original files should be moved to `legacy/` after this log is created.
