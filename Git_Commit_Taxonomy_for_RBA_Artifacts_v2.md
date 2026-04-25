# Git Commit Taxonomy for RBA Artifacts v2

## Purpose

This version simplifies the earlier commit taxonomy into a smaller,
operation-centered system that fits RBA-governed artifact ecosystems more
naturally.

The goal is to classify commits by the **kind of change** being made rather
than by the exact artifact type being edited.

This is important because RBA work often produces commits that span multiple
interdependent artifacts at once, such as:

- framing documents
- course or program artifacts
- matrices
- summaries
- white paper sections
- case-study reflections

In those situations, a file-type taxonomy becomes too detailed to be practical.

---

## Recommended Format

Use the same basic structure:

```text
type(scope): summary
```

Examples:

```text
frame(program): redefine bridge and successor relationship under new constraints
build(bridge): add course direction matrix and replacement-course definitions
refactor(whitepaper): tighten structure and align section numbering
synth(whitepaper): merge summary, core sections, and appendices into full draft
review(supervisor): revise framing after management feedback
meta(repo): add commit taxonomy for artifact ecosystem
```

---

## Recommended Commit Types

### `frame`

Use when the governing interpretation of the work changes.

This includes:

- problem reframing
- redefining scope or intent
- clarifying a central distinction
- correcting a higher-order assumption

Use `frame` when the meaning architecture changes.

---

### `build`

Use when substantial new artifact work is created.

This includes:

- drafting new artifacts
- adding new sections
- producing new matrices or summaries
- creating new course, program, or paper content

Use `build` when the dominant action is creating meaningful new material.

---

### `refactor`

Use when structure changes without major change to core intent.

This includes:

- reorganizing documents
- tightening structure
- moving or reshaping content
- improving sequencing or alignment

Use `refactor` when coherence improves but the primary purpose remains stable.

---

### `synth`

Use when multiple existing artifacts are unified into a higher-order output.

This includes:

- merging sections into one paper
- turning several artifacts into a summary document
- integrating multiple strands into one coherent artifact

Use `synth` when the main action is synthesis rather than raw creation.

---

### `review`

Use when a change is driven primarily by feedback, inspection, or response.

This includes:

- supervisor-driven revisions
- advisory-driven revisions
- review-response changes
- refinement after critique or reflection

Use `review` when the change is best understood as a response cycle.

---

### `meta`

Use for repo-level or process-level guidance.

This includes:

- taxonomy files
- process notes
- README guidance
- artifact indexing or workflow explanation

Use `meta` when the change affects how the artifact system is understood or
managed.

---

### `chore`

Use for light maintenance that does not deserve a more meaningful type.

This includes:

- small cleanup
- renaming
- moving files
- formatting-only passes

Use `chore` sparingly.

If the commit has real design meaning, one of the other types is usually better.

---

## Recommended Minimal Set

For most RBA-governed repositories, the following set should be enough:

- `frame`
- `build`
- `refactor`
- `synth`
- `review`
- `meta`
- `chore`

This keeps the system small enough to use consistently while still preserving
meaning in the history.

---

## Recommended Scope Set

To keep scopes just as usable as the commit types, the default shared scope set
should also remain small.

Recommended scopes:

- `program`
- `course`
- `whitepaper`
- `case-study`
- `workflow`
- `repo`

These scopes are intentionally broad enough to stay memorable while still being
specific enough to make commit history easy to scan.

If a more specialized scope is occasionally needed, it can still be used, but
the default shared convention should stay small.

---

## Internal Meanings

To keep history interpretable, the types can be read this way:

- `frame`
  - the governing understanding changed
- `build`
  - new substantive work was created
- `refactor`
  - structure improved without large change to intent
- `synth`
  - multiple artifacts were unified
- `review`
  - feedback or inspection drove the change
- `meta`
  - the repo or process layer changed
- `chore`
  - low-level maintenance only

---

## Example Commits

```text
frame(program): redefine current problem state around mixed workforce realities
build(program): add graduate capability model and workforce definitions
build(program): create course direction matrix and semester progression
refactor(program): revise course-slot logic after deeper bridge analysis
synth(whitepaper): combine summary, core sections, appendices, and contents
review(whitepaper): adjust framing and readability for management audience
meta(workflow): add RBA artifact commit taxonomy guidance
chore(repo): rename and reorganize white paper support files
```

---

## Suggested Use Rule

When a commit spans multiple artifact types, choose the code based on the
**dominant action**:

- if the main change is a new governing understanding, use `frame`
- if the main change is creating new material, use `build`
- if the main change is reworking existing structure, use `refactor`
- if the main change is combining multiple strands, use `synth`

This keeps the taxonomy practical for real multi-artifact work.

---

## Working Summary

This simplified system is better suited to RBA artifact ecosystems because it
tracks the type of architectural work being done rather than trying to label
every commit by the specific artifact class involved.

That makes the taxonomy:

- simpler to remember
- easier to apply consistently
- more useful for mixed commits
- better aligned with how RBA work actually unfolds

The same design principle applies to scopes:

keep them broad enough to remember and stable enough to share.
