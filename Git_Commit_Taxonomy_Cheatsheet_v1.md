# Git Commit Taxonomy Cheatsheet

## Format

```text
type(scope): summary
```

Example:

```text
frame(program): redefine current problem state for AI-era redesign
```

---

## Types

### `frame`

Use when the governing understanding changes.

Examples:

- problem reframing
- scope clarification
- correcting a higher-order assumption

### `build`

Use when creating substantial new work.

Examples:

- new artifacts
- new sections
- new matrices
- new program or course content

### `refactor`

Use when structure improves without major change to core intent.

Examples:

- reorganizing documents
- tightening structure
- improving sequence or alignment

### `synth`

Use when combining multiple artifacts into one higher-order output.

Examples:

- merging sections into a full draft
- combining several artifacts into one summary

### `review`

Use when a change is driven mainly by feedback or inspection.

Examples:

- supervisor revisions
- advisory revisions
- review-response changes

### `meta`

Use for process or repo guidance.

Examples:

- workflow notes
- commit taxonomy
- README/process guidance

### `chore`

Use for light maintenance only.

Examples:

- renaming
- moving files
- formatting cleanup

---

## Default Scopes

- `program`
- `course`
- `whitepaper`
- `case-study`
- `workflow`
- `repo`

Use the smallest clear scope. If unsure, choose the broader one.

---

## Quick Rule

Choose the commit by the **dominant action**:

- changed the governing meaning -> `frame`
- created substantial new material -> `build`
- reorganized existing structure -> `refactor`
- combined multiple strands -> `synth`
- revised from feedback -> `review`
- updated process/repo guidance -> `meta`
- minor maintenance only -> `chore`

---

## Sample Commits

```text
frame(program): redefine bridge and successor relationship
build(course): add Python bridge implementation patterns
refactor(program): tighten semester-by-semester bridge structure
synth(whitepaper): merge sections and appendices into full draft
review(whitepaper): revise framing for supervisor readability
meta(workflow): simplify commit taxonomy for artifact ecosystems
chore(repo): rename and reorganize support files
```

---

## Keep It Simple

- prefer consistency over perfect precision
- use broad scopes, not overly specific ones
- avoid inventing new types unless needed repeatedly
- if a commit spans multiple artifacts, classify by the main move
