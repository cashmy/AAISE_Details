# RBA-APPLIED PROCESS FOR AI-ASSISTED COURSE DESIGN

---

# Purpose

This artifact documents a repeatable RBA-applied process for AI-assisted course design.

It is based on the observed workflow used in the development of:

* `10-152-117 Python Programming`

but is intentionally written in a reusable way so it can support:

* future iterations of the Python course
* other courses in the program
* cross-domain instructional design work

This is **not** a claim that there is only one valid workflow.

It is a practical process model that appears to:

* increase throughput
* reduce mechanical drafting burden
* preserve instructional governance
* improve cross-artifact alignment
* make AI-assisted design more repeatable and less ad hoc

---

# Core Principle

The process is RBA-applied in the sense that:

* intent is clarified before large-scale generation
* constraints are made explicit early
* artifact relationships are governed, not assumed
* revision and refactoring are expected
* alignment is treated as first-class work

In practical terms:

**the goal is not merely to generate many course artifacts**

The goal is to generate a **governed instructional ecosystem**.

---

# Phase 1 - Course Framing Inputs

## Step 1 - Define the Course Frame

Craft or submit:

* course description
* course length
* day / week structure
* total hours
* lecture vs lab division

Why it matters:

* this defines the delivery container and prevents later pacing distortion

---

## Step 2 - Define or Import the Competency Framework

Craft or submit:

* WIDS competency framework

if already defined, use it as a governing source

Why it matters:

* competencies define what the course must ultimately support

---

## Step 3 - Identify Additional Foundational Inputs

Craft or identify as needed:

* learner profile
* lab system
* outcome identity statement
* course architecture

These may not always all exist in finished form at the beginning.

Why it matters:

* these artifacts help shape tone, pacing, support assumptions, and student-facing framing

---

# Phase 2 - Progression Design from Source Material

This phase often uses ECL-Bounce or similar iterative shaping against the selected textbook or source material.

## Step 4 - Craft Phase / Week Descriptions

Develop:

* phase descriptions
* week descriptions

Why it matters:

* this creates the conceptual arc before individual sessions are over-specified

---

## Step 5 - Craft the APL Progression Ladder

Develop:

* assignment progression ladder

Why it matters:

* this creates the student task arc and reveals where scaffolding must occur

---

## Governance Checkpoint A

Before moving on, verify:

* the week progression is realistic for the course length
* the assignment ladder matches the phase logic
* no major concept is floating without a later performance use
* no assignment path outruns the course arc

---

# Phase 3 - Intent Mapping

## Step 6 - Craft the IIM

Develop:

* `IIM_Instructional_Intent_Map`

using AI assistance and iterative refinement

Why it matters:

* the IIM becomes a central instructor-facing design map

---

## Step 7 - Create the IIM Spreadsheet

Develop manually:

* `IIM_(nnn) - Spreadsheet`

with added detail, refinements, and operational clarity

Why it matters:

* the spreadsheet often becomes the most detailed practical pacing map
* it allows human refinement beyond the first AI-assisted narrative artifact

---

## Canonical Source Note

At this stage, explicitly declare what is canonical.

Typical pattern:

* the narrative IIM explains the intent
* the spreadsheet carries the session-level operational detail

This distinction should be named, not assumed.

---

# Phase 4 - Evaluation and Pacing System

## Step 8 - Craft the Assignment Week / Day Matrix

Develop:

* `Assignment_Week_Day_Matrix`

Why it matters:

* this translates the assignment ladder into an actual teaching rhythm

---

## Step 9 - Craft the Master Rubric System

Develop:

* Master Rubric System

including:

* technical skill criteria
* core skill criteria
* weighting matrix
* assignment mapping matrix

Why it matters:

* this becomes the canonical evaluation layer

---

## Governance Checkpoint B

Before artifact-detail work begins, verify:

* the assignment matrix matches the course rhythm
* the rubric system matches the assignment arc
* the weighting logic is sustainable for actual grading
* canonical evaluation mappings are named explicitly

---

# Phase 5 - Assignment and Demo Ecosystem

## Step 10 - Craft Assignment Details

Develop:

* individual assignment artifacts

Why it matters:

* these become the core student-task layer

Critical path note:

assignments should be crafted **after** the initial content arc is mapped, but **before** the full lecture-content system is built.

That ordering matters because it changes the instructional design logic from:

* "cover content, then later invent student work"

to:

* "define what students must do, then shape lectures to support that doing"

That is a much stronger applied-learning posture.

Why this matters pedagogically:

* it reduces content-front-loading
* it forces earlier performance thinking
* it creates better integration between demos, lectures, and assignments
* it makes the later lecture system more accountable to student action
* it mirrors ECL logic more closely, even if the course is not purely experiential

ECL-Bounce note:

the bounce is not just between concepts and assignments, but between:

* topic mapping
* assignment design
* intent mapping
* lecture support
* later refinement

That creates a more integrated final system than a linear "content first, activities later" model.

---

## Step 11 - Craft Demo Examples

Develop:

* instructor demos
* support files such as JSON, CSV, or sample data

Important note:

the true load here is often not code complexity.

The true load is selecting examples that:

* teach the right concept
* stay bounded
* prevent misconception
* align to readiness targets

---

## Step 12 - Craft Successful Assignment Examples

Develop:

* success examples distinct from demos

Why it matters:

* demos illustrate concepts
* success examples illustrate acceptable outcome shape

Those are not the same instructional role.

---

## Step 13 - Identify an Optional Iterative Instructor Example

If useful, identify:

* a continuity example or instructor-only iterative project

Why it matters:

* this can provide longitudinal pedagogy without forcing students into one cumulative project structure

---

## Step 14 - Craft Optional Context Prompts for the Instructor Example

If the iterative instructor example will be built using AI-assisted tooling in another environment, prepare:

* project brief
* curriculum alignment document
* context prompts

Why it matters:

* this preserves context and reduces prompt drift in downstream build sessions

---

# Phase 6 - Alignment and Support Layer

## Step 15 - Craft the Lecture Content and Demo Alignment Artifact

Develop:

* `Lecture_Content_and_Demo_Alignment_Matrix`

Why it matters:

* this is one of the highest-value governance artifacts in the system
* it reveals hidden assumptions
* it validates that assignments are actually teachable within the planned sequence

---

## Step 16 - Craft Policy Wrappers and Related Support Artifacts

Develop or adapt:

* AI use policy wrappers
* approved API wrappers
* student-facing guidance documents
* instructor notes
* readmes and usage guidance

Why it matters:

* support artifacts reduce ambiguity and preserve consistent implementation

---

## Step 17 - Reconcile Previously Created Artifacts

Update prior artifacts as needed so they remain aligned.

This may include:

* assignment wording
* MRS mappings
* unit/week descriptions
* policy references
* support documents

Why it matters:

* new artifact families often reveal misalignments in earlier documents

This step should be expected, not treated as rework failure.

---

## Governance Checkpoint C

Before lecture-system drafting begins, verify:

* every assignment is supported by prior instruction
* demos support readiness rather than merely existing
* no hidden concept assumptions remain
* policy and wrapper artifacts agree with the course design

---

# Phase 7 - Lecture System

## Step 18 - Draft Initial Lecture Outlines

Develop:

* first `1-2` or `2-3` lecture outlines as samples

Why it matters:

* this tests the lecture-outline process before scaling it

---

## Step 19 - Update the Lecture Outline Template

Refine or replace the template based on the sampled outlines.

Why it matters:

* the correct template should emerge from the actual alignment process, not be assumed in advance

---

## Step 20 - Draft Initial Slide Deck Samples

Develop:

* first `1-2` or `2-3` slide decks

Why it matters:

* this tests whether the outline-to-deck flow actually works

---

## Step 21 - Update the Slide Deck Template / Design System

Refine:

* slide deck template
* slide README usage guidance

Why it matters:

* slide decks should remain anchor artifacts, not turn into full speaking scripts

---

## Step 22 - Complete Remaining Lecture Outlines in Blocks

Develop the remaining lecture outlines in:

* week blocks
* phase blocks
* or other sensible grouped units

Why it matters:

* block production allows consistency without allowing small drifts to multiply across the entire course

---

# Phase 8 - Slide System

## Step 23 - Complete Remaining Slide Decks in Blocks

Develop the remaining slide decks in:

* week blocks
* phase blocks
* or other sensible grouped units

Why it matters:

* this preserves consistency while still allowing review checkpoints

---

## Step 24 - Create Meta-Reviews for the Lecture and Slide Systems

Develop:

* lecture outline system meta-review
* slide deck system meta-review

Why it matters:

* these artifacts preserve system-level judgment
* they record strengths, watch points, and future guidance

---

## Step 25 - Update System Readmes / Indexes

Develop or revise:

* README files
* indexes
* navigation guides

Why it matters:

* large artifact ecosystems need navigational support
* otherwise value is lost through retrieval friction

---

# Phase 9 - Publication and Student-Facing Layer

## Step 26 - Create Student-Facing Publication Artifacts

Develop as needed:

* LMS-ready week descriptions
* student AI-use policy documents
* assignment instructions
* final presentation or justification guides

Why it matters:

* the course needs a student-consumable layer, not only an instructor-design layer

---

# Phase 10 - Reflection and Reusability

## Step 27 - Create Reflective / Comparison Artifacts

Develop as useful:

* AI-assisted vs solo comparison
* case reflection
* process reflection
* cross-domain reuse notes

Why it matters:

* these artifacts help future design efforts learn from the present one

---

## Step 28 - Capture the Reusable Process Itself

Develop:

* the process artifact you are reading now

Why it matters:

* if the workflow is not captured, future projects may repeat the output but lose the method

---

# Required Governance Concepts Across All Phases

These are not separate optional ideas.

They should be active throughout the process.

## 1. Canonical Source Declaration

For each stage, explicitly name what artifact is authoritative.

Examples:

* MRS mapping is canonical for evaluation
* spreadsheet may be canonical for session detail
* alignment matrix may be canonical for lecture support

Why it matters:

* contradictions are easier to resolve when authority is named clearly

---

## 2. Readiness Validation

Continuously ask:

* what should students be able to do after this artifact?
* what prior artifact supports that?

Why it matters:

* it prevents performance expectations from drifting ahead of instruction

Related critical-path reminder:

this is one reason assignments should be defined before the lecture system is fully expanded.

When assignments are designed early enough, the later lecture and demo layers can be shaped to support actual student performance rather than drifting toward content coverage for its own sake.

---

## 3. Drift Detection

Regularly test for:

* hidden assumptions
* concept overload
* contradictory evaluation language
* premature tool depth
* unsupported assignment expectations

Why it matters:

* AI-assisted throughput increases the need for active drift control

---

## 4. Revision as Normal Work

Expect upstream and downstream revision.

Why it matters:

* in a governed system, revision is not failure
* revision is how coherence is preserved

---

## 5. Human Judgment as the Governing Layer

AI may accelerate:

* drafting
* comparison
* restructuring
* expansion

But the human must remain decisive in:

* pacing
* scope
* pedagogical fit
* cognitive load judgment
* policy boundaries
* realism
* final alignment

This is non-negotiable.

---

# Practical Compression of the Full Process

This full workflow can be remembered more simply as:

1. Frame the course
2. Define competencies and constraints
3. Build the progression
4. Map instructional intent
5. Build evaluation and pacing systems
6. Build assignments, demos, and success layers
7. Build the alignment and policy layer
8. Build the lecture system
9. Build the slide system
10. Review, reconcile, and capture the method

---

# Final Conclusion

The value of this process is not only that it helps produce many artifacts quickly.

Its value is that it helps produce:

* aligned artifacts
* reviewable artifacts
* reusable artifacts
* governed artifacts

That makes the process suitable not only for one course, but for an expanding instructional design practice.

The most important practical lesson is:

**AI-assisted course design works best when generation is treated as only one part of the system.**

The stronger model is:

* frame
* generate
* compare
* align
* revise
* govern

That is the repeatable pattern worth carrying forward.
