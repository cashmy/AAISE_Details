# **PageForge — Milestone Preservation Directives**

---

## **Purpose**

This document defines how Codex-style LLMs must generate and preserve `PageForge` milestone artifacts.

These directives exist because standard software-development instincts are not sufficient for this project.

Normal development workflows usually optimize for:

* reduced duplication
* centralization of shared logic
* single-source-of-truth code organization
* long-term maintainability of one evolving codebase

`PageForge` milestone generation must optimize for something different:

* instructional comparability
* frozen runnable states
* side-by-side version demonstration
* visible preservation of change over time

These directives intentionally prioritize teaching value over conventional codebase normalization.

---

## **Primary Instructional Principle**

Milestones are not patches.

Milestones are not abstract diffs.

Milestones are not just points in Git history.

Milestones are **frozen, runnable teaching states**.

Each milestone must remain independently usable for demonstration, comparison, and discussion.

---

## **Core Directive**

When generating a new milestone, Codex must:

1. identify the correct instructional source milestone
2. duplicate that source milestone into a new target milestone folder
3. modify only the new target milestone
4. preserve the source milestone unchanged
5. ensure the new target milestone remains independently runnable

Codex must not treat milestone generation as a request to refactor the archive into a cleaner single codebase.

Codex must also not treat a week as a single completed milestone when the roadmap defines separate `build` and `refine` states.

---

## **Important Exception to Standard Practice**

This project intentionally violates normal DRY and archive-minimization practices for instructional reasons.

Codex must not attempt to “improve” the milestone archive by:

* centralizing shared code across milestones
* replacing milestone snapshots with shared dependencies
* collapsing preserved versions into one evolving implementation
* removing duplication that supports side-by-side instruction

Duplication across milestone folders is intentional and desirable when it preserves runnable instructional states.

---

## **What a Milestone Must Be**

Every preserved milestone must be:

* self-contained
* independently runnable
* clearly named
* instructionally legible
* frozen once created

A milestone should allow the instructor to:

* open it separately
* run it in a browser or development environment
* compare it directly against another milestone
* answer questions about what changed and why

---

## **Runnable Snapshot Requirement**

Each milestone must contain a complete runnable version of the `PageForge` app as it truthfully existed at that point in the course.

This means:

* if the app existed only as frontend pages at that stage, preserve the full runnable frontend
* if output generation existed at that stage, preserve the relevant output support
* if API or backend pieces existed at that stage, preserve those pieces too

Codex must preserve the smallest truthful runnable snapshot for the milestone.

This does **not** mean every milestone must contain every future subsystem.

It means each milestone must fully preserve whatever layers genuinely existed at that point.

---

## **Instructional Comparability Rule**

Codex must optimize milestone generation for side-by-side instructional comparison.

This means milestones should:

* preserve stable naming where possible
* preserve recognizable structure from one version to the next
* make changes visible and attributable
* avoid unnecessary reorganization that makes comparison harder

If a tradeoff exists between:

* cleaner engineering normalization
* and clearer milestone comparison

clearer milestone comparison must win.

---

# **Milestone Progression Patterns**

There are two valid milestone progression patterns.

---

## **Pattern 1 — Linear Progression**

This is the default pattern.

In linear progression:

* a new milestone is copied from the most recent instructionally complete prior milestone
* the copied milestone is updated to reflect the next intended stage

Example:

* `week04-refine` -> `week05-build`
* `week05-build` -> `week05-refine`
* `week05-refine` -> `week06-build`

Use this pattern when the week advances the project normally without needing a deliberate contrast state.

This is also the default weekly cadence:

* prior week `refine` -> current week `build`
* current week `build` -> current week `refine`

---

## **Pattern 2 — Contrastive Progression**

This pattern is used when the instructional goal depends on comparing:

* flawed vs corrected
* messy vs structured
* unsafe vs safe
* incomplete vs improved

In contrastive progression:

* the source milestone is copied into a deliberately altered instructional state
* that altered state is preserved as its own milestone
* a second copied-and-improved version is then created from the altered state

Example:

* `week05-refine` -> `week06-build-debug-seeded`
* `week06-build-debug-seeded` -> `week06-refine-debug-fixed`

This pattern is especially appropriate for:

* debugging
* refactoring
* reliability
* security
* UX comparison
* performance comparison

---

## **Source Selection Rule**

Codex must not assume that the source for a new milestone is always the immediately previous chronological milestone.

Instead, Codex must select the **most instructionally relevant source milestone**.

Usually this will be:

* the prior week’s refined version
* or the current week’s build version when creating the current week’s refined version

In special cases, the correct source may be an intentionally flawed or seeded milestone.

For ordinary weekly progression, Codex should follow this chain:

* `weekNN-build-*` is typically copied from `week(NN-1)-refine-*`
* `weekNN-refine-*` is typically copied from `weekNN-build-*`

Codex must not skip directly from a prior week into a same-week refined state unless explicitly instructed.

---

# **Naming Directives**

Milestone names must be explicit and readable.

Use the pattern:

`week##-phase-instructional-state`

Examples:

* `week01-build-foundation`
* `week01-refine-structured-pages`
* `week05-build-dom-interaction`
* `week06-build-debug-seeded`
* `week06-refine-debug-fixed`
* `week07-build-messy-logic`
* `week07-refine-structured-functions`

Shorter names may be acceptable if they preserve clarity, but Codex should prefer readable instructional naming over abbreviated labels like `a` and `b`.

---

# **What Must Remain Frozen**

Once a milestone is created, Codex must treat it as frozen unless explicitly instructed to repair or regenerate it.

This means:

* do not retroactively update older milestones to match newer ones
* do not rewrite earlier code for consistency
* do not clean up old versions unless the user explicitly requests it
* do not propagate later improvements backward into preserved milestones

Older milestones are records of earlier instructional truth, not drafts waiting to be improved.

---

# **What Codex Must Preserve Across Milestones**

Across milestone generations, Codex should preserve as much consistency as possible in:

* project name
* page names
* basic folder structure
* core block naming
* app identity
* instructional continuity

However, Codex should not preserve poor structure merely for consistency if the instructional goal of the milestone is to improve that structure.

Preservation should support comparison, not block legitimate instructional evolution.

---

# **What Codex Must Not Normalize Away**

Codex must not normalize away intentionally instructional states such as:

* seeded bugs
* weak UX
* messy code
* missing validation
* inefficient behavior
* incomplete handling of state or data

If these states are created intentionally for teaching, they are not quality failures in the archive.

They are valid milestones and must be preserved.

---

# **Notes Requirement**

Each milestone should include a short notes file such as `notes.md`.

This file should briefly state:

* the milestone source
* the purpose of this milestone
* what changed
* what this version is meant to demonstrate
* what remains intentionally incomplete or flawed

This improves archive clarity and supports later instructional reuse.

---

# **Recommended Folder Pattern**

Each milestone folder should preserve a shallow structure.

Example:

```text
milestones/
  week06-build-debug-seeded/
    app/
    notes.md
  week06-refine-debug-fixed/
    app/
    notes.md
```

Later milestones may truthfully include other layers:

```text
milestones/
  week10-build-data-driven/
    app/
    output/
    notes.md
```

If backend/API layers become part of the truthful state later:

```text
milestones/
  week14-refine-api-assisted/
    app/
    api/
    output/
    notes.md
```

Only include layers that genuinely exist at that milestone.

---

# **Milestone Generation Sequence Rule**

When asked to generate a new milestone, Codex should follow this sequence:

1. Confirm the target milestone name.
2. Confirm the target week and target phase (`build` or `refine`).
3. Identify the correct source milestone.
4. Duplicate the source milestone into the new milestone folder.
5. Apply only the changes required for the target milestone phase.
6. Preserve prior milestones unchanged.
7. Verify the new milestone is runnable.
8. Add or update the milestone notes file.

This should be treated as the default workflow unless the user explicitly requests a different generation method.

If the target is a `build` milestone, Codex must not include improvements that belong to the same week’s `refine` state.

If the target is a `refine` milestone, Codex must begin from the same week’s `build` milestone unless explicitly instructed otherwise.

---

# **Directive for Debugging Weeks**

For debugging-focused milestones, Codex must preserve both:

* the intentionally flawed starting version
* the corrected and improved ending version

The flawed milestone must remain runnable enough to demonstrate the problem clearly.

The corrected milestone must remain clearly comparable to the flawed version.

Codex must not skip directly to the fixed version if the flawed state is part of the instruction.

---

# **Directive for Refactoring Weeks**

For refactoring-focused milestones, Codex must preserve both:

* the pre-refactor working version
* the post-refactor clarified version

The pre-refactor version should remain understandable as a real intermediate state, not a caricature.

The post-refactor version should visibly improve organization without becoming overly abstract.

---

# **Directive for Security / Reliability Weeks**

For security or reliability milestones, Codex must preserve both:

* the unsafe or incomplete version
* the improved version with validation, checks, or safer behavior

This allows side-by-side teaching of risk and mitigation.

---

# **Directive for Performance Weeks**

For performance milestones, Codex should preserve:

* the less efficient but understandable version
* the improved version with clearer efficiency gains

Codex should avoid over-optimizing the refined version into something less teachable.

---

# **Role of Git**

Git may be used by the instructor as a supporting preservation mechanism.

However, Codex must not assume Git history replaces milestone folders.

For this project:

* Git is the instructor support layer
* milestone folders are the primary instructional archive

The visible, runnable milestone archive must exist independently of Git concepts such as branches or tags.

---

# **Final Directive**

When in doubt, Codex must ask:

> “Will this make the milestone archive easier or harder to teach from side-by-side?”

If the answer is “harder,” Codex should not make that structural optimization.

The archive exists first to support instruction.

That is the governing principle.

---
