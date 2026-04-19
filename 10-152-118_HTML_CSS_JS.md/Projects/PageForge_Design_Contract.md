# **PageForge — Design Contract**

---

## **Purpose**

This document defines the core design boundaries for `PageForge`.

Its purpose is to stabilize the project before code generation begins so that:

* the canonical final artifact remains focused
* weekly milestone versions remain aligned
* Codex generations do not drift in structure, scope, or identity

This is not a week-by-week roadmap.

It is not a detailed engineering specification.

It is a **constraint document** that defines what `PageForge` must remain.

---

## **Project Identity**

`PageForge` is a browser-based, block-driven webpage composer used as the instructor demonstration project for the HTML, CSS, and JavaScript course.

It exists to model how a web application can grow iteratively from simple structure into a more complete interactive system over time.

It should always feel like:

* a web-based tool
* a structured, teachable application
* a project that clearly reflects course concepts

It should never drift into feeling like:

* a professional-grade commercial site builder
* a general-purpose design platform
* a framework-heavy engineering exercise

---

## **Instructional Role**

`PageForge` is:

* the instructor demo project
* a reference implementation for iterative growth
* a model of how concepts are added, connected, and refined

`PageForge` is not:

* the required student project
* the standard all students must copy
* a production product being optimized for maximum feature breadth

The value of `PageForge` comes from its clarity as a learning model, not its complexity.

---

## **Primary User**

The immediate user of `PageForge` is the instructor.

The secondary audience is the student, who uses it as:

* a visible example
* a motivational reference
* a model of iterative development

The simulated end-user inside the app is someone assembling a simple webpage from predefined building blocks.

This simulated end-user should remain generic and approachable.

---

## **Core Purpose of the App**

The core purpose of `PageForge` is:

> to let a user assemble a simple webpage from predefined content blocks, edit the content of those blocks, preview the resulting composition, and eventually export or view the generated structure.

Everything in the design should support this purpose.

If a feature does not support this purpose clearly, it should be considered optional or excluded.

---

## **Required End-State Pages**

`PageForge` should retain a small, stable site structure.

Required pages:

* `index.html` — project overview or landing page
* `builder.html` — main composition workspace
* `about.html` or `help.html` — explanation, usage notes, or project context

These page names should remain stable unless there is a compelling instructional reason to change them.

---

## **Core UI Regions**

The `builder.html` page should preserve the same core zones throughout the project lifecycle.

Required UI regions:

* block library or block selector area
* editing or controls panel
* live preview area
* primary action area for operations such as add, remove, update, or export

These regions may evolve visually over time, but their functional identity should remain stable.

---

## **Required Core Block Types**

The project should use a limited, reusable set of predefined block types.

Required baseline block types:

* Hero section
* Text section
* Image section
* Card or feature grid
* Call-to-action section
* Footer

Additional block types may be added only if they clearly support instruction and do not increase complexity unnecessarily.

---

## **Required End-State Features**

By the completed version of `PageForge`, the project should support the following core capabilities:

* display a set of predefined block types
* add blocks to a page composition
* remove blocks from a page composition
* reorder or reorganize placed blocks in a simple way
* edit core block content through form inputs
* reflect changes in a live preview
* apply limited style or theme controls
* show or export generated structure at a simple instructional level

These end-state features define the target boundaries for the canonical version.

---

## **Optional Features**

The following may be included only if they remain aligned with the roadmap and do not compromise clarity:

* local save/load behavior
* starter templates loaded from JSON
* theme presets
* simple preview modes
* limited transition or animation polish

Optional features should never become the center of the project.

---

## **Explicitly Out of Scope**

The following are outside the design contract and should not be treated as required goals:

* freeform drag-anywhere design canvas
* pixel-perfect visual editor behavior
* account systems or authentication
* cloud storage or remote persistence
* multi-user collaboration
* full CMS behavior
* full website hosting workflow
* arbitrary custom component authoring
* advanced framework migration as part of the core build
* professional-grade site builder parity with tools like Webflow, Wix, or Framer

These features create complexity that is not necessary for the instructional purpose of `PageForge`.

---

## **Technical Constraints**

`PageForge` should remain primarily grounded in:

* HTML
* CSS
* JavaScript

The architecture should stay understandable for students in an introductory HTML/CSS/JS sequence.

Preferred characteristics:

* readable file organization
* direct logic before abstraction
* progressively improved code structure
* limited tooling complexity
* minimal dependency burden

Avoid:

* unnecessary build tooling
* excessive abstraction layers
* architecture that obscures the connection between HTML, CSS, JS, and browser behavior

---

## **Instructional Constraints**

The project must remain teachable at every stage.

That means milestone generations should:

* show only week-appropriate concepts
* avoid leaking future concepts too early
* prioritize readability over cleverness
* preserve direct relationships between concept and implementation

The canonical final version may be more complete, but it must still remain instructional rather than over-engineered.

---

## **AI Alignment Constraint**

`PageForge` must support the staged AI philosophy defined in the IIM.

This means the artifact family should allow the instructor to demonstrate:

* manual foundations first
* AI as explainer later
* AI as assistant during system-building stages
* AI as collaborator during refinement and capstone-like work

The project should not require AI to make sense.

Rather, it should create opportunities to show where AI support is and is not appropriate.

---

## **Consistency Requirements**

The following should remain consistent across canonical and milestone versions unless intentionally revised:

* project name: `PageForge`
* required page names
* core block type naming
* UI region naming
* basic feature direction
* overall identity as a block-based webpage composer

Consistency matters because the project is intended to evolve visibly over time, not reset its identity each week.

---

## **Milestone Preservation Rules**

When generating week-specific versions from the canonical final artifact:

* preserve project identity
* preserve naming consistency
* preserve overall file structure where possible
* remove or simplify features not yet appropriate for the target week
* keep early versions visibly connected to the final destination
* prefer omission over premature abstraction

The weekly versions should feel like earlier stages of the same project, not different projects that happen to share a name.

---

## **Visual Direction**

The visual style of `PageForge` should feel:

* modern
* clear
* structured
* approachable

It should support instructional clarity more than aesthetic experimentation.

The interface should look intentionally designed, but not so stylized that design becomes the main lesson.

Preferred visual qualities:

* clear separation of regions
* readable typography
* consistent spacing
* obvious interaction points
* strong preview visibility

---

## **Export Expectation**

The export functionality should remain simple and instructional.

It may take the form of:

* displayed generated HTML
* displayed generated CSS
* downloadable code snippets
* simple preview-to-code representation

It does not need to become a full production export pipeline.

The purpose of export is to reinforce the relationship between the UI builder and the underlying webpage structure.

---

## **Definition of Success**

`PageForge` succeeds if:

* students can recognize it as the same project growing over time
* each milestone clearly demonstrates the intended weekly concept
* the final artifact feels coherent and stable
* Codex-generated versions remain aligned instead of drifting
* the project supports both manual and AI-mediated instructional moments

---

## **Final Constraint**

If a design or generation decision creates a conflict between:

* greater feature complexity
* and clearer instructional value

the clearer instructional value should win.

`PageForge` is not meant to demonstrate everything that can be built.

It is meant to demonstrate how a meaningful application can be built, step by step, with clarity.

---
