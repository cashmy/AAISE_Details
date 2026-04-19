# **PageForge — Week-by-Week Instructor Roadmap**

---

## **Purpose**

This roadmap defines how the instructor demo project, `PageForge`, can develop across the course in alignment with the existing assignment structure.

Students will still choose their own project track.

This roadmap exists so the instructor can:

* build alongside the class
* model iterative development clearly
* connect each week's topic to a consistent example
* avoid improvising the demo project week-to-week

---

## **How to Use This Roadmap**

Each week should include:

* a **starting version** of `PageForge`
* one **build-focused iteration**
* one **refinement-focused iteration**
* a visible connection to that week's assignment emphasis

The goal is not to make `PageForge` advanced as quickly as possible.

The goal is to make the growth of the project visible, understandable, and instructional.

---

# **Core Project Definition**

`PageForge` is a simple block-based webpage composer.

A user can:

* choose predefined webpage blocks
* edit block content
* preview the page composition
* gradually customize and improve the result

It should remain constrained enough that students can understand how each layer of the system is being built.

---

# **Recommended Baseline Pages**

The application itself should begin with a small site structure such as:

* `index.html` — Home / overview
* `builder.html` — Main composition interface
* `about.html` or `help.html` — Explanation / usage notes

This gives the project enough structure to support the early HTML assignments while leaving room for later interactivity on the builder page.

---

# **Week-by-Week Development Plan**

---

## **Week 1 — HTML Structure**

### **Assignment Alignment**

Create a multi-page HTML site with working navigation and meaningful structure.

### **PageForge Goal**

Create the initial shell of the `PageForge` site.

### **Build Iteration**

Create:

* `index.html`
* `builder.html`
* `about.html` or `help.html`

Include:

* headings
* paragraphs
* lists
* navigation links between all pages

### **Refine Iteration**

Improve:

* heading hierarchy
* semantic sectioning
* link accuracy
* content clarity

### **Visible Outcome**

Students should see that `PageForge` exists as a real, navigable website even before it looks polished or behaves like an app.

### **Instructor Emphasis**

> Structure first. The project should exist before it becomes impressive.

---

## **Week 2 — CSS Foundations**

### **Assignment Alignment**

Apply styling to improve readability, consistency, and visual clarity.

### **PageForge Goal**

Introduce a visual identity and readable layout foundation.

### **Build Iteration**

Add:

* global stylesheet
* typography styles
* color palette
* spacing rules
* nav styling
* section/card styling

### **Refine Iteration**

Improve:

* visual consistency
* contrast
* grouping of related content
* readability of the builder page mock interface

### **Visible Outcome**

The project should now look intentionally designed, even if it is still mostly static.

### **Instructor Emphasis**

> CSS improves communication by making structure easier to read and understand.

---

## **Week 3 — Layout and Responsive Design**

### **Assignment Alignment**

Use layout techniques to organize content and improve presentation across screen sizes.

### **PageForge Goal**

Turn the builder page into a believable application layout.

### **Build Iteration**

Create a layout with:

* block library/sidebar area
* editor/settings area
* live preview area

Use:

* Flexbox and/or Grid
* spacing systems
* section alignment

### **Refine Iteration**

Improve:

* responsive behavior
* stacking on smaller screens
* preview readability
* layout balance

### **Visible Outcome**

`builder.html` should now resemble a real web app interface.

### **Instructor Emphasis**

> Layout is not decoration. It controls how people understand and use the page.

---

## **Week 4 — JavaScript Foundations**

### **Assignment Alignment**

Practice JavaScript logic, variables, conditionals, arrays, objects, and functions.

### **PageForge Goal**

Define the data and logic behind webpage blocks before fully connecting everything to the interface.

### **Build Iteration**

Create JavaScript that defines:

* available block types
* block data objects
* a simple array of placed blocks
* starter functions for rendering or logging output

Possible early block structure:

```js
const availableBlocks = [
  { type: "hero", label: "Hero Section" },
  { type: "text", label: "Text Section" },
  { type: "cta", label: "Call to Action" }
];
```

### **Refine Iteration**

Improve:

* naming
* organization
* clarity of data structure
* use of small functions

### **Visible Outcome**

Even if the UI is not fully interactive yet, students should see that the app now has an underlying system and data model.

### **Instructor Emphasis**

> Before an interface reacts well, the logic behind it needs to make sense.

---

## **Week 5 — DOM Interaction and Events**

### **Assignment Alignment**

Connect JavaScript to the web page and respond to user actions.

### **PageForge Goal**

Make the builder actually respond to clicks or selections.

### **Build Iteration**

Implement at least one clear interaction such as:

* clicking a button to add a block
* selecting a block type from a list
* rendering a block in the preview area

### **Refine Iteration**

Add or improve:

* block removal
* clearer user feedback
* more reliable event handling
* better organization of DOM updates

### **Visible Outcome**

This should be the first moment where `PageForge` truly feels like an application rather than a styled site.

### **Instructor Emphasis**

> Interaction turns structure into behavior.

---

## **Week 6 — Debugging and Problem Solving**

### **Assignment Alignment**

Identify, investigate, and fix issues systematically.

### **PageForge Goal**

Use the existing project to model realistic debugging.

### **Build Iteration**

Prepare or expose a few controlled problems such as:

* broken selector
* event listener attached to the wrong element
* preview not updating as expected
* incorrect block data being displayed

### **Refine Iteration**

Walk through:

* identifying the issue
* checking the console
* isolating the cause
* confirming the fix

### **Visible Outcome**

Students should see that debugging is not separate from development. It is part of building real systems.

### **Instructor Emphasis**

> Problems are not interruptions to programming. They are part of programming.

---

## **Week 7 — Structured JavaScript**

### **Assignment Alignment**

Refactor for readability, maintainability, and clearer structure.

### **PageForge Goal**

Organize the growing JavaScript codebase into understandable parts.

### **Build Iteration**

Refactor into separate functions such as:

* `renderPreview()`
* `createBlockMarkup()`
* `addBlock()`
* `removeBlock()`
* `attachEventListeners()`

### **Refine Iteration**

Improve:

* naming
* repeated logic
* function responsibility
* code layout and readability

### **Visible Outcome**

Students should be able to compare messy code and clearer code inside the same project context.

### **Instructor Emphasis**

> Working code matters. Understandable code matters more as systems grow.

---

## **Week 8 — Data Structures**

### **Assignment Alignment**

Use arrays and objects to organize and display information.

### **PageForge Goal**

Make block rendering clearly data-driven.

### **Build Iteration**

Represent placed blocks with structured objects, for example:

```js
const placedBlocks = [
  {
    id: 1,
    type: "hero",
    title: "Welcome",
    text: "Build your site one block at a time."
  }
];
```

Use this data to generate preview content dynamically.

### **Refine Iteration**

Improve:

* consistency of object structure
* use of loops
* data-to-UI mapping
* clarity between available blocks and placed blocks

### **Visible Outcome**

Students should see that the UI is now driven by organized data, not hard-coded content.

### **Instructor Emphasis**

> Structured data gives the application something real to work with.

---

## **Week 9 — Forms and User Input**

### **Assignment Alignment**

Capture user input and use it to change application behavior.

### **PageForge Goal**

Allow a user to edit the content of placed blocks through form inputs.

### **Build Iteration**

Implement inputs for things like:

* heading text
* body text
* button label
* simple color or alignment option

### **Refine Iteration**

Improve:

* labeling
* form clarity
* how input updates the block data
* how changes appear in the preview

### **Visible Outcome**

The builder now becomes a true content-editing interface rather than just a block adder.

### **Instructor Emphasis**

> Input becomes useful when it meaningfully changes what the system does.

---

## **Week 10 — JSON and External Data**

### **Assignment Alignment**

Retrieve and use external or structured data.

### **PageForge Goal**

Load block presets, themes, or starter content from JSON.

### **Build Iteration**

Use one of the following:

* local JSON file with block presets
* local JSON file with starter templates
* approved simple public data source if useful

Possible example:

* preset landing page blocks
* theme definitions
* starter content packs

### **Refine Iteration**

Improve:

* JSON reading clarity
* display of loaded content
* handling of delayed or missing data
* UI messaging while content loads

### **Visible Outcome**

Students should see the project move from only using hard-coded data to receiving structured data from outside the main script.

### **Instructor Emphasis**

> Real applications often receive data rather than defining everything directly in one file.

---

## **Week 11 — State Management / Integration**

### **Assignment Alignment**

Manage changing values over time and connect multiple parts of the system.

### **PageForge Goal**

Make application state explicit and show the full system flow.

### **Build Iteration**

Track state such as:

* currently selected block
* list of placed blocks
* active style settings
* current template/theme

Use state to drive:

* editor panel content
* preview rendering
* UI highlights or selection feedback

### **Refine Iteration**

Improve:

* consistency of updates
* relationship between state and UI
* flow from input -> state -> display

### **Visible Outcome**

The project should now feel like a connected system rather than a collection of isolated features.

### **Instructor Emphasis**

> Applications do not just display information. They manage and update it over time.

---

## **Week 12 — Performance and Efficiency**

### **Assignment Alignment**

Identify inefficiencies and improve behavior without breaking functionality.

### **PageForge Goal**

Make updates more intentional and reduce unnecessary work.

### **Build Iteration**

Identify inefficiencies such as:

* rerendering the entire preview too often
* repeated DOM queries
* duplicate logic for updates

### **Refine Iteration**

Implement one or more improvements such as:

* caching selectors
* separating full render vs partial update logic
* reducing repeated calculations

### **Visible Outcome**

Students should see that efficiency is often about thoughtful structure, not advanced tricks.

### **Instructor Emphasis**

> Better systems do not just work. They work more intentionally.

---

## **Week 13 — Security and Reliability**

### **Assignment Alignment**

Handle bad input, missing values, and edge cases more safely.

### **PageForge Goal**

Make the builder more reliable and resistant to common failure points.

### **Build Iteration**

Add safeguards for cases like:

* empty text fields
* missing image URLs
* invalid selections
* blocks with incomplete data

### **Refine Iteration**

Improve:

* validation messages
* fallback values
* conditional checks
* graceful handling of unexpected states

### **Visible Outcome**

Students should see that reliability is about anticipating what can go wrong before it breaks the app.

### **Instructor Emphasis**

> Safer systems are built by planning for imperfect input and imperfect conditions.

---

## **Week 14 — UX and Refinement**

### **Assignment Alignment**

Improve usability, feedback, and interface clarity.

### **PageForge Goal**

Polish the builder so it is easier to understand and use.

### **Build Iteration**

Improve:

* labels
* section headings
* preview clarity
* editing workflow
* feedback after actions

Examples:

* selected block highlight
* empty-state message
* clearer action buttons
* improved spacing and visual grouping

### **Refine Iteration**

Test and improve:

* consistency
* ease of use
* clarity for a first-time user

### **Visible Outcome**

Students should see the difference between “it works” and “it feels usable.”

### **Instructor Emphasis**

> A user experiences the interface, not the code behind it.

---

## **Week 15 — Final Integration and Presentation**

### **Assignment Alignment**

Prepare the project as a coherent final demonstration of course growth.

### **PageForge Goal**

Show the completed instructional arc of the demo project.

### **Build Iteration**

Finalize features such as:

* polished preview
* exportable HTML/CSS output
* starter layout preset
* improved overall visual consistency

### **Refine Iteration**

Emphasize:

* readability of code
* stability of the app
* visible progression from Week 1
* explanation of how each major course concept contributed

### **Visible Outcome**

`PageForge` should now serve as evidence of the course philosophy:

* start simple
* build iteratively
* refine intentionally
* connect concepts over time

### **Instructor Emphasis**

> The final project is not just what exists at the end. It is the result of steady, structured growth.

---

# **Recommended Weekly Demo Pattern**

To keep the instructor use of `PageForge` consistent, follow a repeatable rhythm:

1. Show the current version at the start of the week.
2. Point out what is incomplete or limited.
3. Add one meaningful layer during the build phase.
4. Revisit and improve it during the refinement phase.
5. Briefly name what changed and why.

This reinforces the course philosophy of iteration instead of one-pass production.

---

# **Recommended Scope Guardrails**

To keep `PageForge` useful as an instructional companion, avoid:

* full drag-and-drop positioning too early
* too many block types
* advanced frameworks or build tools
* unnecessary abstraction
* trying to solve every possible design need

Prefer:

* simple block templates
* visible state changes
* clear code organization
* limited but meaningful user controls
* consistent improvement over feature sprawl

---

# **Final Teaching Reminder**

`PageForge` should model the learning process, not compete with it.

If students can look at the project each week and clearly answer:

* what was added
* what was improved
* what concept made that possible

then the demo project is doing its job.

---
