# **PageForge — Ongoing Milestone Generation Prompt**

---

## **Recommended Use**

Use this prompt for generating all `PageForge` milestones **after the first one**.

This includes:

* normal week-to-week progression
* build to refine progression
* contrastive progression such as debug-seeded to debug-fixed

This prompt is not for:

* generating the canonical final artifact
* generating the first milestone from scratch

---

## **Purpose**

This prompt governs how Codex should create a new frozen milestone by duplicating the most instructionally relevant source milestone and then iterating upon the copied version.

The new milestone must remain:

* self-contained
* runnable
* comparable to prior versions
* aligned to the target week and phase

The roadmap is a governing artifact for this generation, not optional supporting context.

The phase constraints artifact is also a governing artifact for this generation and should be treated as the most operationally specific source when available.

---

## **Scaffolding Principle**

Every ongoing milestone is a **copied-forward instructional scaffold**.

That means:

* begin with the most instructionally relevant source milestone
* duplicate that milestone into a new target milestone
* preserve the source untouched
* apply only the changes appropriate for the target milestone
* keep the target milestone independently runnable

Do not collapse milestones into one evolving codebase.

Do not normalize away duplication between milestone folders.

---

## **Developmental Authenticity Principle**

Each milestone must reflect not only the correct concepts for its stage, but also the believable maturity level of that stage.

This means:

* do not make early milestones feel visually or structurally too complete
* do not allow later polish levels to leak backward into earlier stages
* preserve the sense that the project is truly growing over time

The milestone archive should show authentic development, not just filtered feature subsets of a mature app.

---

## **Prompt**

```text
MODE: Ongoing Milestone Generation

You are generating a new frozen instructional milestone for an instructor demonstration project called `PageForge`.

This is NOT the canonical final artifact.
This is NOT the first milestone.

You must follow milestone-preservation logic rather than standard software-archive normalization logic.

PRIMARY DIRECTIVE
Treat milestones as frozen runnable teaching states.

Your job is to:
1. identify the source milestone
2. duplicate the source milestone into the new target milestone
3. modify only the target milestone
4. preserve the source milestone unchanged
5. ensure the target milestone is independently runnable
6. follow the roadmap’s specified phase exactly

PROJECT IDENTITY
`PageForge` is a browser-based, block-driven webpage composer used as the instructor demonstration project in an HTML/CSS/JavaScript course.

SCAFFOLDING DIRECTIVE
Each milestone is a self-contained instructional scaffold.
Do NOT create shared dependencies across milestones.
Do NOT centralize repeated code between milestone folders.
Do NOT replace milestone preservation with Git-style assumptions.

The archive is intentionally duplicated because side-by-side instructional comparison matters more than archive minimization.

SOURCE MILESTONE
You will be given or shown the source milestone.
Treat it as frozen.
Do not modify it.

TARGET MILESTONE
Create the new milestone by copying the source milestone first, then applying only the changes required for the target week/phase/state.

SOURCE SELECTION RULE
Do not assume the source milestone is always the most recent chronological milestone.
Use the most instructionally relevant source milestone.

Examples:
- `week05-refine-...` -> `week06-build-debug-seeded`
- `week06-build-debug-seeded` -> `week06-refine-debug-fixed`

VALID PROGRESSION TYPES
1. Linear progression:
   one milestone evolves normally into the next

2. Contrastive progression:
   a milestone is intentionally altered into a flawed or incomplete instructional state, then a second milestone improves it

If the target milestone is contrastive, preserve the flawed or incomplete state as a valid runnable milestone.

ROADMAP GOVERNANCE RULE
You must follow the roadmap as a controlling source.

If the roadmap defines a week as two instructional states:
- Tuesday `build`
- Thursday `refine`

you must generate only the requested state.

Do not collapse the week into one “finished weekly milestone.”

PHASE CONSTRAINT GOVERNANCE RULE
If a `PageForge_Phase_Constraints.md` artifact is provided, you must follow it as a controlling source for the target week and phase.

Use it to determine:
- what must be included
- what may be included
- what must not appear yet
- how visually mature or incomplete the output should feel

If the phase constraints artifact is more specific than the roadmap, the phase constraints artifact wins.

WHAT YOU MUST PRESERVE
Preserve as much continuity as possible in:
- project identity
- page names
- basic folder structure
- app continuity
- comparability across milestones

WHAT YOU MUST NOT DO
Do NOT:
- rewrite older milestones
- retroactively clean earlier code
- centralize milestone code into shared folders
- introduce abstractions purely to reduce duplication
- remove intentional flaws if they are part of the target milestone

TRUTHFUL SNAPSHOT RULE
The target milestone must contain the smallest truthful runnable version of the app at that point.

Include only the layers that genuinely exist at the target milestone.

Examples:
- early milestone: frontend app only
- later milestone: frontend app + sample output
- later still: frontend app + output + API/backend layer, if truly present

STAGE AUTHENTICITY RULE
The target milestone must feel appropriate to its instructional stage.

Do not introduce:
- visual polish levels that belong to later milestones
- structural maturity that has not yet been taught
- “semi-finished app” aesthetics in early or middle milestones unless explicitly requested

PHASE-SPECIFIC RULE
If target phase is `build`:
- generate the Tuesday-lab-appropriate state
- keep the milestone intentionally incomplete
- do not include cleanup, explanatory maturity, or polish that belongs to the refine state

If target phase is `refine`:
- copy from the same week’s `build` milestone unless explicitly instructed otherwise
- incorporate improvements justified by Wednesday concept reinforcement
- do not leak next-week capabilities into the refine state

MILESTONE NOTES
Include milestone notes content that states:
- source milestone
- target milestone purpose
- what changed
- what this milestone demonstrates
- what remains intentionally incomplete or flawed

OUTPUT REQUIREMENTS
Generate:
1. the target milestone file tree
2. the contents of each created/updated file in the target milestone
3. a short summary of what changed from the source milestone
4. a list of intentionally preserved flaws or intentionally deferred features
5. suggested `notes.md` content
6. a short statement confirming the exact roadmap week and phase represented by the output

QUALITY BAR
The target milestone should feel like a real next stage of the same project, not a newly invented variant.

IMPORTANT FINAL INSTRUCTION
When making tradeoffs, choose:
- side-by-side comparability over DRY structure
- instructional clarity over archive optimization
- truthful evolution over aggressive refactoring

Before producing code, briefly summarize your milestone-generation plan in 6-10 bullets.
Then produce the target milestone file tree and code.
```

---

## **Recommended Companion Inputs**

Attach or reference:

* [PageForge_Phase_Constraints.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Phase_Constraints.md)
* [PageForge_Milestone_Preservation_Directives.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Milestone_Preservation_Directives.md)
* [PageForge_Design_Contract.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Design_Contract.md)
* [PageForge_Week_by_Week_Roadmap.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Week_by_Week_Roadmap.md)
* the actual source milestone folder/content

The phase constraints artifact should be treated as the most operationally specific governance source for milestone generation.

The roadmap should be treated as required because it constrains:

* developmental maturity
* concept timing
* what belongs to `build` versus `refine`

Do not run this prompt without both the roadmap and the phase constraints artifact unless you are intentionally accepting a weaker result.

If token budget is limited, prioritize:

1. source milestone content
2. `PageForge_Phase_Constraints.md`
3. `PageForge_Week_by_Week_Roadmap.md`
4. `PageForge_Milestone_Preservation_Directives.md`
5. `PageForge_Design_Contract.md`

---
