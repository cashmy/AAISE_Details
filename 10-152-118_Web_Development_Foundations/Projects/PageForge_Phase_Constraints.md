# **PageForge — Phase Constraints**

---

## **Purpose**

This document defines the fine-grained week-and-phase constraints for generating `PageForge` milestones.

It acts as the operational companion to the higher-level roadmap.

The roadmap defines the overall instructional arc.

This document defines the tighter rules needed for milestone generation, especially when the Codex-LLM would otherwise normalize toward generic front-end completeness.

For milestone generation, this document should be treated as a governing artifact.

If this document is more precise than the roadmap for a given week, this document should control the generation.

---

# **Week 1 — Structure: Something Exists**

## **Week Overview**

### **Primary Instructional Focus**

Week 1 is about creating something that exists in the browser and can be navigated.

The emphasis is on:

* HTML structure
* multi-page thinking
* working links
* headings and paragraphs
* simple content organization

### **Relationship to Prior Weeks**

This is the foundation week.

There is no prior project complexity to preserve beyond the identity of `PageForge` as the instructor project.

### **Relationship to Later Weeks**

Week 1 must remain intentionally limited.

Styling, layout refinement, JavaScript behavior, and more complete interface structure are deferred to later weeks.

---

## **Build Phase**

### **Instructional Purpose**

This phase represents the Tuesday lab state.

It should model what could plausibly exist after the Monday lecture and the first guided build lab.

The artifact should show that the project exists and can be navigated, but it should still feel early, rough, and intentionally incomplete.

### **Must Include**

* exactly 3 HTML pages:
  * `index.html`
  * `builder.html`
  * `about.html`
* working navigation links between all three pages
* page-level headings
* paragraphs of explanatory text
* simple content that establishes the purpose of each page
* a very early placeholder version of the builder page

### **May Include**

* simple grouping using `div` or `section` only if needed for basic readability
* plain placeholder labels for future builder regions
* minimal default browser styling only

### **Must Not Include Yet**

* lists, if they are not introduced until the Wednesday concept focus
* footer structure
* richer semantic element variety beyond what has been explicitly introduced
* meaningful CSS styling or visual polish
* card layouts
* hero sections
* app-shell presentation
* JavaScript of any kind
* interactive behavior
* explanatory maturity that reads like a completed Week 1 reflection

### **Visual / Maturity Guidance**

This version should feel like a true first pass.

It should look plain, browser-default, and minimally organized.

It should not look polished, balanced, or visually composed like a small finished site.

The main success condition is existence and navigability, not presentation quality.

### **LLM Guardrails**

Do not add common front-end “best practice” elements just because they are typical.

Do not introduce lists, footers, polished sections, or app-like content containers unless they are explicitly allowed.

Do not make the builder page feel like a refined wireframe.

Do not make the text sound like it was written after the whole week was completed.

### **Notes for Future Revision**

If the lecture sequence changes and lists or additional semantic elements are introduced earlier, this section should be updated.

---

## **Refine Phase**

### **Instructional Purpose**

This phase represents the Thursday lab state.

It should model what could plausibly exist after the Wednesday concept reinforcement and the Thursday refinement lab.

The refine version should improve structure, clarity, and correctness while still remaining fully inside Week 1.

### **Must Include**

* everything from the build phase
* corrections to navigation, naming, or heading hierarchy if needed
* improved content clarity
* better structural consistency across pages
* lists if they were introduced on Wednesday and are now appropriate
* clearer organization of the placeholder builder content

### **May Include**

* a slightly more consistent use of structure-related elements discussed by Wednesday
* clearer section labeling
* modest organization improvements that still remain visually plain

### **Must Still Avoid**

* meaningful CSS polish
* layout systems that belong to later weeks
* footer if it is not yet introduced
* card-based visual grouping
* hero-style landing sections
* app-shell styling
* JavaScript behavior
* any interactivity
* content that reads like a later-week product explanation

### **Visual / Maturity Guidance**

This version should feel more organized than the build phase, but still clearly plain and structure-first.

A viewer should be able to compare the build and refine versions and say:

* the refined version is clearer
* the refined version is more correct
* but it is still obviously only a Week 1 HTML milestone

### **LLM Guardrails**

Do not treat refinement as permission to add styling, polish, or next-week capabilities.

Do not collapse “better structure” into “better interface.”

Do not make the refine version look like a small finished website.

### **Notes for Future Revision**

If the Wednesday concept lecture expands or contracts the set of allowed HTML elements, this section should be updated to match.

---

## **Optional Comparison Notes**

The key contrast between Week 1 build and Week 1 refine should be:

* Build = something exists
* Refine = the structure is clearer and more correct

The contrast should not be:

* Build = rough HTML
* Refine = mini finished site

If the refined version looks visually or structurally like a polished small site, it has overshot the week.

---
