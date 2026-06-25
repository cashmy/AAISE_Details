# **PageForge — Initial Milestone Prompt**

---

## **Recommended Use**

Use this prompt only for generating the **first instructional milestone** of `PageForge`.

This prompt is not for:

* generating the canonical final artifact
* copying a previous milestone
* generating later milestone evolutions

This first milestone is a special case.

It should create the true starting instructional version of the project.

This prompt should be used for the first week’s `build` state unless explicitly adapted for another phase.

---

## **Purpose**

The first milestone must represent the smallest truthful beginning of `PageForge` for the opening stage of instruction.

It should:

* reflect the early course constraints
* preserve the core identity of `PageForge`
* avoid prematurely importing later-stage complexity
* create a runnable instructional starting point

The first milestone may be informed by the canonical final artifact, but it must not behave like a copied subset of the final product.

The roadmap must govern this generation.

If the roadmap defines a Monday lecture / Tuesday build / Wednesday concept / Thursday refine rhythm, this prompt must generate only the requested phase, not the completed week-level outcome.

The phase constraints artifact must also govern this generation when it is available.

If the phase constraints artifact is more specific than the roadmap for the target week and phase, the phase constraints artifact wins.

---

## **Scaffolding Principle**

The first milestone is a **foundational scaffold**, not a reduced duplicate of the complete app.

That means:

* include only the layers that truthfully exist at the first milestone
* preserve the identity of the project
* avoid introducing future architecture too early
* keep the structure shallow and understandable

This milestone should feel like a real beginning, not a concealed advanced application.

---

## **Developmental Authenticity Principle**

The first milestone must not only be conceptually early.

It must also **feel developmentally early**.

That means:

* avoid making the first milestone look like a nearly finished app shell
* prefer honest foundational structure over polished product aesthetics
* keep visual styling modest enough that the version still reads as an early manual-stage build
* allow the artifact to look clear and intentional without looking mature or heavily refined

The goal is not to make the first milestone unattractive.

The goal is to make it believable as a true first-stage instructional version.

---

## **Prompt**

```text
MODE: Initial Milestone Generation

You are generating the first instructional milestone of an instructor demonstration project called `PageForge`.

This is NOT the canonical final artifact.
This is NOT an ongoing copy-forward milestone.
Do NOT assume there is a prior milestone to duplicate.

Your task is to create the first runnable milestone as the true starting point of the instructional sequence.

PROJECT IDENTITY
`PageForge` is a browser-based, block-driven webpage composer used as the instructor demonstration project in an HTML/CSS/JavaScript course.

Over time, the full project will allow a user to:
- choose predefined webpage blocks
- add them to a composition
- edit content
- preview the result
- eventually view or export generated code

However, this first milestone must only contain what truthfully exists at the beginning of the course sequence.

SCAFFOLDING DIRECTIVE
This first milestone must behave like a foundational scaffold.
Do NOT create a reduced copy of the final product.
Do NOT include hidden advanced architecture just because it may be useful later.
Do NOT include placeholder complexity for future features unless it is instructionally necessary.

The first milestone should:
- preserve the `PageForge` identity
- establish the starting pages and structure
- remain independently runnable
- stay shallow, legible, and week-appropriate
- remain visually modest and developmentally believable as an early-stage build

INSTRUCTIONAL CONTEXT
This milestone should reflect the opening stage of the course, where structure and simple existence matter more than advanced app behavior.

The student or instructor should be able to look at this version and say:
"This is clearly the beginning of the same project, but it is still only at the foundation stage."

PHASE DIRECTIVE
Unless otherwise specified, this prompt should generate the Week 1 `build` state.

That means:
- model what could exist after Monday lecture and Tuesday lab
- do not include improvements that belong to Wednesday concept reinforcement or Thursday refinement
- do not generate a “best complete Week 1 version”

REQUIRED PAGE STRUCTURE
Use this stable structure:
- `index.html`
- `builder.html`
- `about.html`

At this stage, these pages should be simple and structurally meaningful.

WHAT THIS FIRST MILESTONE SHOULD INCLUDE
- a runnable multi-page site
- working navigation
- meaningful headings, sections, paragraphs, and lists where appropriate
- semantic structure where possible
- a very early and simple version of the builder page layout
- enough content to suggest the future purpose of PageForge without implementing later behavior
- only limited styling appropriate to an early-stage instructional milestone

WHAT THIS FIRST MILESTONE SHOULD NOT INCLUDE
Do NOT include:
- meaningful JavaScript application logic
- block-adding functionality
- live preview behavior
- export functionality
- async behavior
- JSON loading
- state management
- modules
- API/backend integration
- advanced abstraction
- a visually polished app-like shell that feels too complete for the opening stage

You may include:
- static placeholders that suggest future areas of the builder interface
- simple instructional content that explains what the app will eventually become

FOLDER / FILE EXPECTATION
Keep the structure shallow and instructional.
Use something like:
- `/app/index.html`
- `/app/builder.html`
- `/app/about.html`
- `/app/assets/css/styles.css` if needed

Only include JavaScript if it is truly necessary at this stage. Otherwise omit it.

MILESTONE PRESERVATION CONSTRAINT
This milestone must be independently runnable and suitable to freeze as the initial instructional state.
It should not depend on future milestones.
It should not assume shared code from other versions.

PHASE CONSTRAINT GOVERNANCE RULE
If a `PageForge_Phase_Constraints.md` artifact is provided, you must follow it as a controlling source for:

* what must be included
* what may be included
* what must not appear yet
* how visually mature or incomplete the milestone should feel

Do not fall back to generic front-end best practices when the phase constraints artifact is more specific.

OUTPUT REQUIREMENTS
Generate:
1. the milestone file structure
2. the contents of each file
3. a short note explaining why this is the correct initial scaffold
4. a short list of intentionally deferred features
5. a suggested milestone notes file content
6. a short statement confirming which roadmap phase this output represents

QUALITY BAR
This should feel like the honest beginning of a project that will later become `PageForge`, not an artificially stripped-down advanced app.

IMPORTANT FINAL INSTRUCTION
When making tradeoffs, choose:
- truthful beginnings over premature completeness
- instructional clarity over future convenience
- stable identity over hidden complexity
- developmental authenticity over polished presentation

Before producing code, briefly summarize your implementation plan in 6-10 bullets.
Then produce the file tree and code.
```

---

## **Recommended Companion Inputs**

Attach or reference these if possible:

* [PageForge_Phase_Constraints.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Phase_Constraints.md)
* [PageForge_Design_Contract.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Design_Contract.md)
* [PageForge_Week_by_Week_Roadmap.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Week_by_Week_Roadmap.md)
* [PageForge_Milestone_Preservation_Directives.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Milestone_Preservation_Directives.md)

The phase constraints artifact should be treated as the most operationally specific governance source for milestone generation.

The roadmap should be treated as required for stage-authentic milestone generation because it constrains:

* developmental maturity
* concept timing
* the difference between Tuesday `build` and Thursday `refine`

Do not run this prompt without both the roadmap and the phase constraints artifact unless you are intentionally accepting a weaker result.

If token budget is limited, prioritize:

1. `PageForge_Phase_Constraints.md`
2. `PageForge_Week_by_Week_Roadmap.md`
3. `PageForge_Design_Contract.md`
4. `PageForge_Milestone_Preservation_Directives.md`

---
