# **PageForge — Codex Generation Workflow**

---

## **Purpose**

This document defines a repeatable workflow for using a Codex-style LLM to generate the instructor demonstration project, `PageForge`, in a structured and reusable way.

The goal is to reduce manual development time while preserving alignment with:

* the course roadmap
* the phase-constraint artifact
* the instructional intent map (IIM)
* the staged role of AI across the course
* the iterative philosophy of the project system

---

## **Core Idea**

`PageForge` should not be generated as a one-off project.

It should be generated as a **family of aligned artifacts**:

* one canonical final version
* multiple stage-appropriate weekly versions
* supporting notes that explain what changes and why

This allows the instructor to:

* show students a motivating end state
* build progressively during the course
* preserve consistency across weeks
* avoid rebuilding the same project manually from scratch

---

# **The Recommended Model**

Use **Option 1 as the production workflow**:

> Generate the final `PageForge` first, then derive the weekly instructional versions from it.

This is the preferred workflow because it:

* reduces drift
* creates a stable reference point
* improves naming and file consistency
* makes staged simplification easier than staged invention
* supports reuse across multiple semesters

---

# **Generation Architecture**

The system should include four layers.

---

## **Layer 1 — Canonical Final Artifact**

This is the full end-state version of `PageForge`.

It represents what the instructor project should become by the end of the course.

It should include:

* full app structure
* stable file naming
* final information architecture
* final feature boundaries
* polished but still understandable code

This artifact is not the week-by-week teaching version.

It is the canonical source for all staged derivations.

---

## **Layer 2 — Weekly Milestone Artifacts**

These are the week-specific versions of `PageForge`.

Each milestone version should:

* reflect only the concepts available by that point in the course
* preserve the same overall project identity
* omit later-week abstractions and features
* visibly connect to the final destination
* follow the roadmap's intra-week phase exactly

These artifacts are the versions the instructor actually teaches from.

---

## **Layer 3 — Delta / Change Notes**

Each milestone should include short notes explaining:

* what changed from the previous version
* why those changes were made
* what instructional concept they demonstrate
* what remains intentionally incomplete

These notes are useful for:

* lecture planning
* recording demos
* instructor clarity
* explaining iteration to students

---

## **Layer 4 — AI Usage Notes**

Each milestone should also identify the intended role of AI for that stage of the course, based on the IIM.

This creates alignment between:

* how the project is built behind the scenes
* how AI is discussed in instruction
* how students are expected to engage with AI later

---

# **Why Final-First Works Better for Codex**

Generating the final project first is the better RBA workflow because LLMs are generally better at:

* simplifying
* constraining
* decomposing
* refactoring

than they are at maintaining long-horizon consistency across many independent generations.

If the model is asked to invent the project step-by-step across many weeks, the following risks increase:

* UI drift
* naming drift
* feature creep
* inconsistent architecture
* awkward late-stage retrofits

If the final artifact exists first, the model can instead be asked to:

> produce the Week 4 version of this same project while preserving only the concepts appropriate for Week 4

That is a more stable and controllable transformation task.

---

# **Key Guardrail**

Generating the final artifact first does **not** mean teaching the final artifact first.

The final artifact should function as:

* the canonical source
* the planning anchor
* the motivational preview

The weekly milestone artifacts remain the teaching versions.

---

# **Required Supporting Documents**

Before generating the artifact family, the following documents should exist:

* `PageForge_Instructor_Companion.md`
* `PageForge_Week_by_Week_Roadmap.md`
* `PageForge_Phase_Constraints.md`
* a short `PageForge_Design_Contract.md` document

The design contract should define:

* core purpose
* minimum required pages
* final feature boundaries
* prohibited scope
* required naming consistency

Without a design contract, milestone generations are more likely to drift.

Without the phase constraints artifact, milestone generations are more likely to normalize toward generic completeness instead of the intended instructional stage.

---

# **Recommended Workflow**

---

## **Step 1 — Define the Canonical Target**

Use Codex to generate the final `PageForge` artifact first.

This should be done only after the project identity is clearly defined.

Inputs:

* instructor companion document
* week-by-week roadmap
* design contract
* phase constraints, if they clarify current instructional boundaries
* IIM guidance

Output:

* the canonical final codebase for `PageForge`

Important:

This version should still be readable and instructional.
It should not become over-engineered simply because AI can generate more complexity.

---

## **Step 2 — Freeze the Core Identity**

Before generating weekly versions, confirm:

* file names
* page names
* core block types
* feature boundaries
* UI zones
* terminology

These should not change casually across milestone generations.

This is what prevents drift.

---

## **Step 3 — Generate Weekly Milestones**

For each instructional week, use Codex to generate milestone versions of `PageForge` that reflect only that stage of the course.

Each generation should explicitly specify:

* which week is being generated
* which instructional phase is being generated
* what concepts are allowed
* what concepts are not yet allowed
* what visible features should exist
* what should remain incomplete or simplified

The instructional phase is required.

Codex must not generate a generic “Week N completed version.”

Instead, Codex must generate the specific roadmap phase requested, such as:

* `build` = Tuesday lab state
* `refine` = Thursday lab state

---

## **Step 4 — Generate Weekly Change Notes**

For each milestone, also generate:

* short explanation of what changed since the prior milestone
* reasons for those changes
* teaching focus
* suggested demo emphasis

These notes help transform generated code into instruction.

---

## **Step 5 — Generate AI Role Notes**

For each milestone, generate a short note aligned to the IIM that identifies AI's role during that week.

Examples:

* Week 1: no AI involvement in the student-visible foundational build
* Week 6: AI as explainer for debugging logic
* Week 9: AI as assistant for structure suggestions
* Week 13: AI as collaborator for safety review and edge-case analysis

This strengthens the connection between project evolution and AI literacy.

---

# **Recommended Artifact Set**

For practical reuse, each major generation cycle should create:

* the code snapshot
* a short milestone summary
* a list of features present
* a list of intentionally deferred features
* AI usage notes for that stage

Optional:

* screenshots
* before/after comparison notes
* instructor talking points

---

# **Weekly Downgrade Rules**

When generating milestone versions from the canonical final artifact, Codex should follow explicit downgrade rules.

These prevent later-stage complexity from leaking into earlier instructional versions.

---

## **Global Downgrade Rules**

For all early and middle milestones:

* preserve project identity
* preserve naming consistency
* preserve file organization where possible
* remove features not yet supported by the course week
* prefer readability over cleverness
* prefer direct logic over abstraction
* avoid introducing future-week concepts early
* keep comments instructional and time-appropriate
* follow the roadmap phase strictly
* treat the roadmap as a governing artifact, not optional guidance

---

## **Roadmap Governance Rule**

For milestone generation, the roadmap is effectively required.

Codex must treat the roadmap as a governing source for:

* concept timing
* developmental maturity
* phase-specific expectations
* what belongs to Tuesday `build` versus Thursday `refine`

Codex must not infer a completed week-level outcome when the roadmap defines a two-step weekly progression.

If a generation request includes a week and phase, the roadmap phase must control the output.

If the roadmap and a more generalized interpretation conflict, the roadmap wins.

If the phase constraints artifact is more specific than the roadmap for the target week and phase, the phase constraints artifact wins.

---

## **Two-Phase Weekly Cadence Rule**

Each instructional week should be treated as two distinct milestone targets:

* `build`
* `refine`

These are not interchangeable.

### **Build Phase**

Represents the Tuesday lab state.

This version should:

* reflect what could plausibly exist after Monday lecture and Tuesday lab
* remain intentionally incomplete
* avoid cleanup, polish, or interpretive completeness that depends on Wednesday concept reinforcement
* avoid borrowing clarity or refinement from the Thursday state

### **Refine Phase**

Represents the Thursday lab state.

This version should:

* begin from the same week’s `build` milestone
* incorporate improvements informed by Wednesday’s concept reinforcement
* improve clarity, structure, correctness, or presentation within the week’s scope
* remain bounded to that week rather than leaking into next-week capabilities

Codex must not collapse these two states into one weekly artifact.

---

## **Weeks 1–3**

Allowed emphasis:

* HTML structure
* CSS styling
* layout and responsiveness

Do not include:

* meaningful JavaScript logic
* async behavior
* state management
* modular architecture
* API integration

Any UI that suggests future capability should remain mostly static.

---

## **Weeks 4–5**

Allowed emphasis:

* JavaScript basics
* DOM interaction
* simple events

Do not include:

* async patterns
* external data loading
* complex state systems
* advanced abstractions

Use straightforward functions and simple event flows.

---

## **Weeks 6–7**

Allowed emphasis:

* debugging
* refactoring
* structured JavaScript

Do not include:

* modules too early if not yet taught
* complex framework-style architecture
* optimization-first thinking

The project should still feel simple enough to debug visibly.

---

## **Weeks 8–11**

Allowed emphasis:

* async concepts
* modularization
* JSON/data flow
* state

Do not include:

* advanced libraries unless aligned to roadmap timing
* unnecessary toolchain complexity

This is where the project can become more system-like, but it should remain understandable.

---

## **Weeks 12–15**

Allowed emphasis:

* performance
* reliability
* UX refinement
* project integration

This is where the milestone versions can move closer to the canonical final artifact.

Even here, instructional clarity should still outrank maximal polish.

---

# **AI Role Alignment by Phase**

The generated milestone notes should align with the IIM's AI progression.

---

## **Weeks 1–5 — Native / Manual First**

AI role in instructor-facing generation:

* hidden production accelerator

AI role in student-facing instruction:

* minimal or none

Purpose:

* foundational concepts should appear manual and direct
* students must first understand the underlying layers

---

## **Weeks 6–8 — AI as Explainer**

AI role in instruction:

* explanation
* debugging interpretation
* concept clarification

Use examples like:

* asking AI to explain an error
* comparing AI explanation to actual code behavior

---

## **Weeks 9–12 — AI as Assistant**

AI role in instruction:

* refactoring suggestions
* structure suggestions
* support for reasoning through data/state/organization

Use examples like:

* asking AI for cleaner function organization
* asking AI to suggest modular boundaries

---

## **Weeks 13–17 — AI as Collaborator**

AI role in instruction:

* idea partner
* UX refinement partner
* safety reviewer
* implementation collaborator

Use examples like:

* asking AI to identify risky edge cases
* comparing alternate UX refinements
* using AI strategically during capstone work

---

# **Prompting Strategy for Codex**

Do not rely on vague continuity alone.

Each generation prompt should explicitly provide:

* project purpose
* target week
* allowed concepts
* prohibited concepts
* required files/pages
* current milestone or final artifact reference
* desired output format

This greatly improves consistency.

---

## **Prompt Structure Template**

Use a structure like:

1. Project Identity
2. Week Target
3. Allowed Concepts
4. Not Yet Allowed
5. Required Visible Features
6. Required Constraints
7. Output Needed

---

## **Example Prompt Pattern**

> Generate the Week 5 instructional version of `PageForge`, a block-based webpage composer used as an instructor demo project in an HTML/CSS/JS course.
>
> Preserve the established project identity and file naming.
>
> This version should reflect only concepts available by Week 5:
> HTML structure, CSS styling/layout, JavaScript basics, DOM interaction, and event handling.
>
> Do not include:
> async behavior, external data fetching, modules, state management systems, or advanced abstractions.
>
> The visible app should allow a user to add a predefined block and see it appear in a preview area.
>
> Keep the code readable, direct, and beginner-appropriate.
>
> Output:
> 1. the code snapshot
> 2. a short summary of what changed from Week 4
> 3. a list of intentionally deferred features
> 4. a short note on how AI should be framed this week according to the IIM

---

# **Recommended Cadence**

Your intended cadence of generating `PageForge` once or twice per week is reasonable.

A practical rhythm would be:

* one generation for the build iteration
* one generation for the refinement iteration

This mirrors the course structure well.

For example:

* Tuesday version = build milestone
* Thursday version = refined milestone

This approach provides clean instructional checkpoints without requiring you to manually author each version.

---

# **Recommended Naming Convention**

To keep artifact management clear, use milestone labels such as:

* `pageforge-final`
* `pageforge-week01-build`
* `pageforge-week01-refine`
* `pageforge-week02-build`
* `pageforge-week02-refine`

This makes reuse, comparison, and archival easier.

---

# **Practical Warning**

Codex can generate complexity faster than the course can explain it.

So the key discipline is not whether AI can build `PageForge`.

It can.

The key discipline is whether each generated version remains:

* week-appropriate
* instructional
* readable
* aligned to the roadmap

Always constrain for clarity before sophistication.

---

# **Final Recommendation**

Use Codex to generate `PageForge` through a **canonical-target workflow**:

* create the final artifact first
* derive weekly milestone snapshots from it
* generate delta notes and AI-usage notes along the way
* align every version to the IIM and roadmap

This gives you:

* speed
* consistency
* reusability
* instructional control

without requiring you to manually build the instructor project from scratch each week.

---
