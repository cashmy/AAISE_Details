# **PageForge — Canonical Generation Prompt**

---

## **Recommended Use**

Use this prompt in VS Code with a strong frontier model such as:

* `GPT-5.4`
* `GPT-5.2`

Purpose:

Generate the **canonical final artifact** for `PageForge`, which will later be simplified into weekly milestone versions for instruction.

This prompt is for canonical end-state generation only.

It is not for:

* first milestone generation
* milestone copy-forward generation
* frozen milestone preservation workflow

This prompt is designed to create the full end-state project while keeping it:

* consistent
* instructional
* constrained
* aligned to the course design

---

## **Prompt**

```text
MODE: Canonical Final Artifact Generation

You are helping generate the canonical final version of an instructor demonstration project called `PageForge`.

This is not a production SaaS product.
This is not a commercial no-code builder.
This is an instructional, browser-based, block-driven webpage composer used as the instructor companion project in an HTML/CSS/JavaScript course.

This prompt is for canonical generation only.
Do NOT apply milestone-copying behavior.
Do NOT assume a source milestone exists.
Do NOT optimize for frozen milestone duplication in this run.

Your goal is to generate a complete, coherent, end-state version of `PageForge` that can later be transformed into earlier weekly milestone versions.

The project must remain readable, teachable, and constrained.

SCAFFOLDING CONSISTENCY DIRECTIVE
The canonical artifact must preserve the same project identity that later milestone scaffolds will use.
However, this run should generate the completed end-state application directly.

Do NOT treat this as a copied-forward milestone.
Do NOT artificially strip the architecture down to an early-week state.
Do NOT include milestone archive structures in the canonical output unless explicitly requested.

PROJECT PURPOSE
`PageForge` allows a user to:
- choose from predefined webpage blocks
- add blocks to a page composition
- edit the content of those blocks
- preview the resulting composition
- apply limited styling/theme choices
- view or export the generated HTML/CSS at a simple instructional level

INSTRUCTIONAL CONTEXT
This canonical final artifact will be used as the source for staged course milestones.
That means:
- the code must be understandable
- the app structure must be stable
- naming must be consistent
- the project must not become over-engineered
- it should feel like a polished end-state of an HTML/CSS/JS learning project

IMPORTANT DESIGN CONSTRAINTS
The app must remain:
- browser-based
- built primarily with HTML, CSS, and JavaScript
- understandable to students in an HTML/CSS/JS sequence
- modular enough to be clean, but not abstract to the point of obscuring learning

The app must NOT become:
- a drag-anywhere freeform builder
- a commercial-grade visual design platform
- a framework-heavy application
- an account-based or cloud-based system
- a backend-driven product

REQUIRED PAGES
Use this stable page structure:
- `index.html` = overview / landing page
- `builder.html` = main composition interface
- `about.html` = explanation / help / project context

REQUIRED CORE UI REGIONS ON `builder.html`
Preserve these core zones:
- block library / block selector
- editing or controls panel
- live preview area
- primary action area for operations such as add, remove, reorder, and export/view code

REQUIRED BLOCK TYPES
Include these predefined block types:
- Hero section
- Text section
- Image section
- Card or feature grid
- Call-to-action section
- Footer

REQUIRED END-STATE FEATURES
The canonical final version should support:
- displaying available block types
- adding blocks to the composition
- removing blocks
- simple reordering of blocks
- editing block content through form-based controls
- live preview updates
- limited theme/style controls
- viewing and/or exporting generated HTML/CSS in a simple instructional way

OPTIONAL FEATURES
You may include these only if they remain simple and readable:
- local save/load
- starter templates loaded from JSON
- theme presets
- simple preview modes

Do not include optional features if they complicate the app significantly.

EXPLICITLY OUT OF SCOPE
Do not implement:
- freeform drag-anywhere placement
- authentication
- remote persistence
- multi-user collaboration
- full CMS behavior
- framework migration
- heavy build tooling
- production-grade complexity

VISUAL DIRECTION
The app should feel:
- modern
- clear
- structured
- approachable

It should support instructional clarity more than aesthetic experimentation.
Use a clean layout with readable typography, obvious UI regions, and strong preview visibility.

TECHNICAL DIRECTION
Prefer:
- direct, readable JavaScript
- clear file organization
- functions with obvious responsibilities
- comments only where they help explain non-obvious structure
- light modularity if helpful, but no unnecessary complexity

Avoid:
- clever abstractions
- deeply nested architecture
- excessive indirection
- unnecessary dependencies

EXPORT EXPECTATION
The export/code-view feature should be simple and instructional.
Acceptable forms include:
- showing generated HTML
- showing generated CSS
- downloadable text snippets
- a code preview panel

It does not need to be a professional export pipeline.

OUTPUT REQUIREMENTS
Generate:
1. the full project file structure
2. the contents of each file
3. a short architectural overview
4. a feature inventory
5. a short note describing why this version is suitable as the canonical final artifact for later milestone simplification

IMPLEMENTATION PREFERENCE
Build this as a static frontend project using plain HTML, CSS, and JavaScript unless a very small amount of structure beyond that clearly improves readability.

Prefer a structure such as:
- `/index.html`
- `/builder.html`
- `/about.html`
- `/assets/css/...`
- `/assets/js/...`
- `/assets/data/...` if needed

QUALITY BAR
This should feel like a strong final instructor demo project for a 15-week HTML/CSS/JS course:
- polished enough to be motivating
- constrained enough to be teachable
- coherent enough to remain stable across milestone derivations

IMPORTANT FINAL INSTRUCTION
When making tradeoffs, choose:
- instructional clarity over cleverness
- coherence over feature breadth
- stable structure over flashy complexity

Before writing the final code output, briefly summarize your implementation plan in 8-12 bullets.
Then produce the file tree and the code.
```

---

## **Recommended Companion Inputs**

If the VS Code workflow allows attaching or referencing additional files, provide these alongside the prompt:

* [PageForge_Design_Contract.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Design_Contract.md)
* [PageForge_Week_by_Week_Roadmap.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Week_by_Week_Roadmap.md)
* [PageForge_Instructor_Companion.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Instructor_Companion.md)
* [PageForge_Generation_Workflow.md](D:/@Artifact_Generation/108_AAISE_Details/10-152-118_HTML_CSS_JS.md/Projects/PageForge_Generation_Workflow.md)

If token budget becomes tight, prioritize:

1. `PageForge_Design_Contract.md`
2. `PageForge_Week_by_Week_Roadmap.md`
3. `PageForge_Instructor_Companion.md`

---

## **Recommended Process in VS Code**

1. Start with `GPT-5.4`.
2. Paste the canonical generation prompt.
3. Attach or paste the design contract first.
4. If needed, add the roadmap and instructor companion.
5. Ask the model to generate the full canonical artifact.
6. Review the result against the design contract before accepting it as canonical.

---

## **Review Checklist After Generation**

After generation, confirm that the artifact:

* preserves the required page names
* uses the required core UI regions
* includes the required block types
* stays inside the defined scope
* avoids unnecessary complexity
* feels polished but still teachable
* could plausibly be simplified into Week 1 through Week 15 milestone versions

If the artifact fails two or more of these checks, regenerate with a tighter reminder about instructional clarity and scope.

---
