# Weekly Reading and Preparation Guide

**Course:** 10-152-118 HTML, CSS, and JavaScript

**Primary readings are from:**

- **HTML/CSS:** HTML & CSS: Design and Build Websites, 1st Edition, Jon Duckett, ISBN: 978-1-118-00818-8
- **JS/JQ:** JavaScript & jQuery: Interactive Front-End Web Development, 1st Edition, Jon Duckett, ISBN: 978-1-118-53164-8

**jQuery curation note:** jQuery is used as an example of a third-party helper library, similar to adding a package to a Python program. Students are not learning jQuery as the main way to write JavaScript. Vanilla JavaScript remains the foundation; jQuery examples should be read for library leverage, comparison, and selected convenience patterns.

---

## Unit (Phase 1) - Foundations

**Unit 1 reading note:** These first three weeks use Duckett to establish HTML structure, basic CSS control, and box/space fundamentals. Flexbox and media queries should be scaffolded carefully in lecture/lab and revisited later, not overloaded into the first CSS exposure.

### Week 1 - HTML: "Something Exists"

- **Preparation Focus:** Understand that a web page is a structured document made from elements. Focus on creating meaningful content, clear hierarchy, and working links before worrying about appearance.
- **Key Terms to Notice:** HTML, element, tag, attribute, heading, paragraph, link, href, relative path, page structure.
- **What Students Should Bring into Lecture:** A basic sense that HTML gives content structure and that links connect separate pages into a small site. Students do not need to know CSS yet.
- **Connection to Lab/Assignment:** Prepares students to build a simple multi-page HTML site with headings, paragraphs, basic lists if needed, and navigation links. The success target is "something exists and works."
- **Assigned Reading:**
  * **HTML/CSS:** Chap 1 - Structure: pp 8-28
  * **HTML/CSS:** Chap 2 - Text: pp 33-60
  * **HTML/CSS:** Chap 4 - Links: pp 74-92
  * **HTML/CSS:** Chap 3 - Lists: selected pages only if needed for the Week 1 list requirement: pp __-__

### Week 2 - CSS: "I Can Control Appearance"

- **Preparation Focus:** See CSS as a separate layer that changes how existing HTML looks. Focus on rules, selectors, color, typography, readability, and visual consistency.
- **Key Terms to Notice:** CSS rule, selector, declaration, property, value, stylesheet, color, contrast, font family, font size, class, id, specificity.
- **What Students Should Bring into Lecture:** A recognition that CSS does not replace HTML structure; it applies presentation choices to structured content.
- **Connection to Lab/Assignment:** Prepares students to add an external CSS file to the Week 1 site, apply readable colors and text styling, and make styling consistent across pages.
- **Assigned Reading:**
  * **HTML/CSS:** Chap 10 - Introducing CSS: pp 226-244
  * **HTML/CSS:** Chap 11 - Color: pp 246-282, 290-298
  * **HTML/CSS:** Chap 12 - Text: selected pages on typefaces, size, and readability: pp __-__

### Week 3 - Layout: "Control Space"

- **Preparation Focus:** Understand that every element occupies space and that CSS can control spacing, sizing, and the visual relationship between parts of a page. Keep the focus on box/space thinking before heavier responsive-layout mechanics.
- **Key Terms to Notice:** box model, width, height, margin, padding, border, display, block, inline, whitespace, layout.
- **What Students Should Bring into Lecture:** A working styled site from Week 2 and a beginner-level understanding that layout problems often come from how boxes, spacing, and selectors interact.
- **Connection to Lab/Assignment:** Supports the move from "the page has styling" to "the page has intentional space." Flexbox and media queries should be scaffolded carefully in lecture/lab and revisited later when students have more CSS confidence.
- **Assigned Reading:**
  * **HTML/CSS:** Chap 13 - Boxes: pp 300-328
  * **HTML/CSS:** Chap 15 - Layout: selected pages for layout vocabulary and context only: pp __-__
  * **Supplemental:** Flexbox/media-query prep to be placed after the course-wide reading pass: URL/page range __

---

## Unit (Phase 2) - Behavior

### Week 4 - JavaScript: "This is Programming"

- **Preparation Focus:** Begin JavaScript as programming before attaching it to the page. Focus on values, variables, expressions, decisions, and the habit of predicting behavior before running code.
- **Key Terms to Notice:** script, statement, variable, value, data type, expression, operator, condition, Boolean, if statement, loop.
- **What Students Should Bring into Lecture:** A willingness to treat JavaScript as a separate logic layer, not merely a way to make buttons do things.
- **Connection to Lab/Assignment:** Prepares students for console-based JavaScript logic exercises and reinforces programming habits from Python.
- **Assigned Reading:**
  * **JS/JQ:** Introduction: pp 1-10
  * **JS/JQ:** Chap 1 - The ABC of Programming: pp 11-52
  * **JS/JQ:** Chap 2 - Basic JavaScript Instructions: pp 53-84
  * **JS/JQ:** Chap 4 - Decisions & Loops: selected pages on conditionals and basic loops: pp 145-182

### Week 5 - DOM: "Now It Connects"

- **Preparation Focus:** Connect JavaScript logic to visible browser behavior through the DOM and events.
- **Key Terms to Notice:** DOM, DOM tree, element node, query, selector, textContent, attribute, event, event listener, click, input.
- **What Students Should Bring into Lecture:** A basic understanding that JavaScript can locate page elements, respond to user actions, and update what the user sees.
- **Connection to Lab/Assignment:** Prepares students to add button/input interactions to an existing HTML/CSS page.
- **Assigned Reading:**
  * **JS/JQ:** Chap 5 - Document Object Model: pp 183-242
  * **JS/JQ:** Chap 6 - Events: selected pages on event listeners, event objects, and user events: pp 243-292
  * **JS/JQ:** Chap 7 - jQuery: optional comparison only; read for "library leverage," not memorization: pp 293-366 selected pages __-__

### Week 6 - Debugging: "Things Break - And I Can Fix Them"

- **Preparation Focus:** Treat debugging as a visible, repeatable process instead of a panic response. Use browser tools, console output, and careful observation to locate causes.
- **Key Terms to Notice:** error, console, stack, breakpoint, scope, execution order, log, exception, debugging workflow.
- **What Students Should Bring into Lecture:** A working idea that errors are information and that debugging means gathering evidence.
- **Connection to Lab/Assignment:** Prepares students to fix intentionally broken HTML/CSS/JS examples and explain what was wrong.
- **Assigned Reading:**
  * **JS/JQ:** Chap 10 - Error Handling & Debugging: pp 449-486
  * **HTML/CSS:** Chap 10 - Introducing CSS: optional review on selectors/cascade if CSS bugs are included: pp 226-244

### Week 7 - Structured Behavior: "From Working to Clean"

- **Preparation Focus:** Move from code that merely works to code that is easier to read, explain, reuse, and revise.
- **Key Terms to Notice:** function, parameter, argument, return value, scope, object, method, event handler, separation of concerns.
- **What Students Should Bring into Lecture:** A sense that organization is part of correctness because unclear code becomes harder to debug and extend.
- **Connection to Lab/Assignment:** Prepares students to refactor messy interaction code into named functions with clearer responsibilities.
- **Assigned Reading:**
  * **JS/JQ:** Chap 3 - Functions, Methods & Objects: pp 85-144
  * **JS/JQ:** Chap 6 - Events: selected review on event handlers/listeners: pp __-__
  * **JS/JQ:** Chap 11 - Content Panels: selected pages on separation of concerns only: pp 487-526 selected pages __-__

---

## Unit (Phase 3) - System Thinking

### Week 8 - Async: "Time Matters"

- **Preparation Focus:** Understand that browser behavior does not always happen immediately. Some actions wait, load, delay, or complete later.
- **Key Terms to Notice:** asynchronous, request, response, callback, loading, timing, Ajax, JSON.
- **What Students Should Bring into Lecture:** A beginner-level ability to distinguish "what happens now" from "what happens later."
- **Connection to Lab/Assignment:** Prepares students to build visible delayed/timed behavior and observe asynchronous flow.
- **Assigned Reading:**
  * **JS/JQ:** Chap 8 - Ajax & JSON: selected pages on what Ajax is, how requests/responses work, and JSON: pp 367-408 selected pages __-__
  * **JS/JQ:** Chap 11 - Content Panels: selected asynchronous loading/caching examples: pp __-__
  * **Supplemental:** Modern `fetch`/Promise intro if used in lecture: URL/page range __

### Week 9 - Modular Thinking: "Breaking Systems into Parts"

- **Preparation Focus:** Organize growing code into smaller, purposeful pieces. Focus on responsibility boundaries before professional module systems.
- **Key Terms to Notice:** function, object, responsibility, separation of concerns, reusable code, dependency, module-shaped organization.
- **What Students Should Bring into Lecture:** Prior JavaScript interaction code that can be reorganized and explained in smaller pieces.
- **Connection to Lab/Assignment:** Prepares students to refactor behavior into clearer functions and responsibility groups.
- **Assigned Reading:**
  * **JS/JQ:** Chap 3 - Functions, Methods & Objects: review selected sections on functions/objects: pp 85-144 selected pages __-__
  * **JS/JQ:** Chap 11 - Content Panels: selected pages on separation of concerns/plugin structure as concept only: pp 487-526 selected pages __-__
  * **Supplemental:** Modern ES module or multi-file organization prep if used: URL/page range __

### Week 10 - Data: "Beyond the Page"

- **Preparation Focus:** Work with data that is not hard-coded into the page. Focus on request, response, JSON structure, selection, and display.
- **Key Terms to Notice:** data, JSON, object, array, API, request, response, fetch, filter, sort.
- **What Students Should Bring into Lecture:** A basic understanding that page content can be generated from structured data.
- **Connection to Lab/Assignment:** Prepares students to fetch or simulate external data and display selected results dynamically.
- **Assigned Reading:**
  * **JS/JQ:** Chap 8 - Ajax & JSON: pp 367-408
  * **JS/JQ:** Chap 9 - APIs: selected pages on APIs and web storage/API concepts: pp 409-448 selected pages __-__
  * **JS/JQ:** Chap 12 - Filtering, Searching & Sorting: selected pages on arrays/filtering/sorting: pp 527-566 selected pages __-__
  * **Supplemental:** Modern `fetch` and JSON examples if used instead of jQuery Ajax: URL/page range __

### Week 11 - State: "Things Persist"

- **Preparation Focus:** Understand state as remembered application information and connect that idea to UI updates and browser storage.
- **Key Terms to Notice:** state, persistence, local storage, session storage, current value, update, saved preference.
- **What Students Should Bring into Lecture:** A sense that interactive applications need to remember information and keep the interface consistent with that information.
- **Connection to Lab/Assignment:** Prepares students to build a feature that remembers a choice, setting, cart item, tracker value, or form progress.
- **Assigned Reading:**
  * **JS/JQ:** Chap 9 - APIs: selected pages on Web Storage, local storage, and session storage: pp 409-448 selected pages __-__
  * **JS/JQ:** Chap 12 - Filtering, Searching & Sorting: selected pages on data structures if the state feature uses arrays/objects: pp __-__
  * **Supplemental:** Instructor-provided state/localStorage example if needed: URL/page range __

---

## Unit (Phase 4) - System Integrity

### Week 12 - Performance: "Making it Efficient"

- **Preparation Focus:** Notice that working code can still be improved. Focus on visible responsiveness, avoiding unnecessary work, and making media or repeated operations more efficient.
- **Key Terms to Notice:** performance, efficiency, loading, caching, repeated work, responsiveness, image size.
- **What Students Should Bring into Lecture:** A working feature or page that can be compared before and after refinement.
- **Connection to Lab/Assignment:** Prepares students to improve sluggish or inefficient behavior and explain why the revised version is better.
- **Assigned Reading:**
  * **JS/JQ:** Chap 11 - Content Panels: selected pages on asynchronous loading and caching images: pp 487-526 selected pages __-__
  * **JS/JQ:** Chap 12 - Filtering, Searching & Sorting: selected pages on filtering/sorting work: pp 527-566 selected pages __-__
  * **HTML/CSS:** Chap 16 - Images: selected pages on image sizing/optimization context: pp 406-426 selected pages __-__
  * **Supplemental:** Modern web performance prep if needed: URL/page range __

### Week 13 - Security Awareness: "Building Safely"

- **Preparation Focus:** Build basic trust-boundary awareness. Focus on unsafe input/output patterns, validation, and why user-provided content requires care.
- **Key Terms to Notice:** input, output, validation, escaping, XSS, trust boundary, safe handling, error message.
- **What Students Should Bring into Lecture:** A recognition that "it works" is not the same as "it is safe."
- **Connection to Lab/Assignment:** Prepares students to identify unsafe patterns in sample code and apply simple safer practices.
- **Assigned Reading:**
  * **JS/JQ:** Chap 5 - Document Object Model: selected pages on XSS attacks and defending against XSS: pp 183-242 selected pages __-__
  * **JS/JQ:** Chap 13 - Form Enhancement & Validation: selected validation pages: pp 567-622 selected pages __-__
  * **Supplemental:** Intro browser/web security prep if needed: URL/page range __

### Week 14 - UX & Styling Refinement: "Make it Better to Use"

- **Preparation Focus:** Refine a working page or app so it is clearer, more usable, and easier to understand. Focus on feedback, visual hierarchy, affordances, and appropriate interactive polish.
- **Key Terms to Notice:** UX, feedback, affordance, accessibility, content panel, modal, accordion, filtering, sorting, responsive design.
- **What Students Should Bring into Lecture:** A working project that can be improved for usability, clarity, and presentation.
- **Connection to Lab/Assignment:** Prepares students to improve interaction feedback, layout, styling, and user comprehension.
- **Assigned Reading:**
  * **HTML/CSS:** Chap 17 - HTML5 Layout: pp 428-450 selected pages __-__
  * **HTML/CSS:** Chap 18 - Process & Design: pp 452-474 selected pages __-__
  * **JS/JQ:** Chap 11 - Content Panels: pp 487-526 selected pages __-__
  * **JS/JQ:** Chap 12 - Filtering, Searching & Sorting: pp 527-566 selected pages __-__
  * **Supplemental:** Modern Flexbox/media-query refinement prep if placed here: URL/page range __

## Week 15 - Forms & Input Systems / Capstone Submissions

- **Preparation Focus:** Connect forms, input handling, validation, and capstone planning. Focus on collecting information, responding to it, and scoping a feasible final project.
- **Key Terms to Notice:** form, input, label, submit, validation, required field, form event, proposal, scope, prototype.
- **What Students Should Bring into Lecture:** A project idea or interaction idea that could use structured user input.
- **Connection to Lab/Assignment:** Prepares students to build or extend a form-based interaction and submit a capstone proposal.
- **Assigned Reading:**
  * **HTML/CSS:** Chap 7 - Forms: pp 144-174
  * **HTML/CSS:** Chap 14 - Lists, Tables & Forms: pp 330-356 selected pages __-__
  * **JS/JQ:** Chap 13 - Form Enhancement & Validation: pp 567-622
  * **HTML/CSS:** Chap 18 - Process & Design: selected capstone-planning support: pp 452-474 selected pages __-__

---

## Unit (Phase 5) - Capstone

### Week 16 - Capstone Build

- **Preparation Focus:** Apply the course layers independently with instructor coaching and peer feedback.
- **Key Terms to Notice:** integration, debugging, revision, explanation, AI-use boundary, final readiness.
- **What Students Should Bring into Lecture:** An approved project plan and a current build they can continue developing.
- **Connection to Lab/Assignment:** Supports independent capstone build time.
- **Assigned Reading:**
  * **HTML/CSS:** Chap 18 - Process & Design: optional review: pp 452-474
  * **HTML/CSS:** Chap 19 - Practical Information: optional deployment/SEO/analytics context if relevant: pp 476-490
  * **Course Materials:** Capstone rubric, proposal feedback, and final readiness checklist: file/page range __

### Week 17 - Capstone Wrap-Up & Presentations

- **Preparation Focus:** Prepare to demonstrate, explain, and reflect on the final project.
- **Key Terms to Notice:** demonstration, explanation, tradeoff, revision, debugging evidence, AI-use explanation.
- **What Students Should Bring into Lecture:** A completed or nearly completed project and notes on major design/build decisions.
- **Connection to Lab/Assignment:** Supports final presentations and explanation of how the system works across HTML, CSS, JavaScript, data/state, debugging, and refinement.
- **Assigned Reading:**
  * **Course Materials:** Presentation checklist, final rubric, and AI-use explanation guide: file/page range __
