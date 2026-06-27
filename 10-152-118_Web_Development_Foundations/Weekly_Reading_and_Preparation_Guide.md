# Weekly Reading and Preparation Guide

**Course:** 10-152-118 Web Development Foundations  
**Alternate Title:** HTML, CSS, and JavaScript

**Primary readings are from:**

- **HTML/CSS:** HTML & CSS: Design and Build Websites, 1st Edition, Jon Duckett, ISBN: 978-1-118-00818-8
- **JS/JQ:** JavaScript & jQuery: Interactive Front-End Web Development, 1st Edition, Jon Duckett, ISBN: 978-1-118-53164-8

**Reading load principle:** Assigned reading should prepare students to understand lecture and lab, not replace instruction. Most weeks use a small required reading plus optional skim/reference items. This protects beginner cognitive load, especially because students are also beginning Python, Introduction to Security, and English Composition.

**jQuery curation note:** jQuery is used as an example of a third-party helper library, similar to adding a package to a Python program. Students are not learning jQuery as the main way to write JavaScript. Vanilla JavaScript remains the foundation; jQuery examples should be read for library leverage, comparison, and selected convenience patterns.

**Reading Labels:**

- **Required:** Read before lecture. Short, targeted, and directly connected to the week.
- **Skim:** Preview for vocabulary or context. Do not memorize.
- **Reference:** Use during lab/project work when needed.

---

## Unit (Phase 1) - Foundations

**Unit 1 intent:** Build safety and visible success. Students should understand structure, appearance, and space as separate layers without trying to master every HTML/CSS feature.

### Week 1 - HTML: "Something Exists"

- **Preparation Focus:** A web page is a structured document. HTML gives content meaning and connects pages together.
- **Key Terms to Notice:** HTML, element, tag, attribute, heading, paragraph, link, href, relative path, structure.
- **What Students Should Bring into Lecture:** A basic idea that HTML creates meaningful document structure; CSS and JavaScript come later.
- **Connection to Lab/Assignment:** Build a simple multi-page site that exists, opens in the browser, and has working navigation.
- **Assigned Reading:**
  * **Required - HTML/CSS:** Chap 1 - Structure: pp 8-28
  * **Required - HTML/CSS:** Chap 2 - Text: selected pages on headings and paragraphs: pp 40-60
  * **Required - HTML/CSS:** Chap 4 - Links: selected pages on basic links and relative paths: pp 74-92
  * **Reference - HTML/CSS:** Chap 3 - Lists: pp 62-72, use only if needed for the list requirement

### Week 2 - CSS: "I Can Control Appearance"

- **Preparation Focus:** CSS is a separate layer that changes how existing HTML looks.
- **Key Terms to Notice:** CSS rule, selector, property, value, stylesheet, color, font, class, id.
- **What Students Should Bring into Lecture:** A basic understanding that CSS styles HTML; it does not replace HTML structure.
- **Connection to Lab/Assignment:** Add an external CSS file and improve readability, color, typography, and consistency.
- **Assigned Reading:**
  * **Required - HTML/CSS:** Chap 10 - Introducing CSS: pp 226-244
  * **Required - HTML/CSS:** Chap 11 - Color: pp 246-262
  * **Skim - HTML/CSS:** Chap 12 - Text: selected pages on font size and readability: pp 264-286
  * **Reference - HTML/CSS:** Chap 12 - Text: selected pages on font size and readability: pp 287-298

### Week 3 - Layout: "Control Space"

- **Preparation Focus:** Elements occupy space. CSS controls spacing, sizing, and relationships between parts of the page.
- **Key Terms to Notice:** box model, width, height, margin, padding, border, layout, alignment.
- **What Students Should Bring into Lecture:** A styled site and a beginner-level idea that layout problems often come from boxes and spacing.
- **Connection to Lab/Assignment:** Move from "styled page" to "intentional layout" with guided Flexbox and a light responsive introduction.
- **Assigned Reading:**
  * **Required - HTML/CSS:** Chap 13 - Boxes: pp 300-328
  * **Skim - HTML/CSS:** Chap 15 - Layout: pp 358-404
  * **Reference - Supplemental:** Flexbox/media query guides:
    * MDN Flexbox: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox
    * MDN Media Queries: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Media_queries

---

## Unit (Phase 2) - Behavior

**Unit 2 intent:** Introduce JavaScript separately, then connect it to the page. Students should learn behavior through small visible wins, not exhaustive API coverage.

### Week 4 - JavaScript: "This is Programming"

- **Preparation Focus:** JavaScript is a programming language. Start with values, variables, expressions, simple decisions, and mental execution.
- **Key Terms to Notice:** script, statement, variable, value, expression, operator, Boolean, condition, function.
- **What Students Should Bring into Lecture:** A willingness to predict what code will do before running it.
- **Connection to Lab/Assignment:** Console-based logic exercises and predict-run-observe practice.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 1 - The ABC of Programming: selected pages on scripts, variables, and basic program thinking: pp 36-52
  * **Required - JS/JQ:** Chap 2 - Basic JavaScript Instructions: pp 53-84
  * **Skim - JS/JQ:** Chap 1 - The ABC of Programming: pp 11-35
  * **Skim - JS/JQ:** Chap 4 - Decisions & Loops: selected pages on `if` statements only: pp 145-163
  * **Reference - JS/JQ:** Chap 3 - Functions, Methods & Objects: pp 85-144, use later as needed
  * **Reference - JS/JQ:** Chap 4 - Decisions & Loops: selected pages on `switch`, `while`, and `for` loops: pp 164-182

### Week 5 - DOM: "Now It Connects"

- **Preparation Focus:** The DOM is the bridge between page structure and JavaScript behavior.
- **Key Terms to Notice:** DOM, element, selector, query, event, click, input, null.
- **What Students Should Bring into Lecture:** A basic idea that JavaScript can find page elements and respond to user actions.
- **Connection to Lab/Assignment:** Add simple button/input interactions to an existing HTML/CSS page.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 5 - Document Object Model: selected pages on what the DOM is and selecting one element: pp 183-187, 228-231
  * **Required - JS/JQ:** Chap 6 - Events: selected pages on basic event-driven thinking and click events: pp 243-251
  * **Required - JS/JQ:** Chap 7 - jQuery: selected pages for library recognition, script loading, and safety awareness: pp 293-304, 358-361
  * **Skim - JS/JQ:** Chap 5 - Document Object Model: element manipulation: pp 187-227, 232-242
  * **Skim - JS/JQ:** Chap 6 - Events: Handlers, Listeners and other events: pp 252-292
  * **Reference - JS/JQ:** Chap 7 - jQuery: selected pages showing how a helper library shortens common DOM/event tasks: pp 304-357, 362-366


### Week 6 - Debugging: "Things Break - And I Can Fix Them"

- **Preparation Focus:** Debugging is a process for gathering evidence, not a panic response.
- **Key Terms to Notice:** error, console, log, breakpoint, stack, cause, symptom.
- **What Students Should Bring into Lecture:** A working idea that error messages and console output are clues.
- **Connection to Lab/Assignment:** Fix intentionally broken HTML/CSS/JS examples and explain the cause.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 10 - Error Handling & Debugging: selected pages on console, common errors, and tracing: pp 449-465, 480-486
  * **Reference - JS/JQ:** Chap 10 - Error Handling & Debugging: browser specifics, console editing, and advanced debugging techniques: pp 466-479

### Week 7 - Structured Behavior: "From Working to Clean"

- **Preparation Focus:** Working code becomes easier to maintain when behavior is organized into clear functions.
- **Key Terms to Notice:** function, parameter, argument, return value, scope, callback, event handler.
- **What Students Should Bring into Lecture:** Prior interaction code that can be made cleaner.
- **Connection to Lab/Assignment:** Refactor messy interaction code into named functions with clear responsibilities.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected pages on functions, scope, dot notation, and the document object as a built-in/global object: pp 85-103, 120-130
  * **Reference - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected pages on objects and built-in methods: pp 104-119, 131-144

---

## Unit (Phase 3) - System Thinking

**Unit 3 intent:** Students begin thinking beyond individual pages and isolated features. Readings should support vocabulary and mental models; lecture/lab should carry implementation.

### Week 8 - Async: "Time Matters"

- **Preparation Focus:** Some browser behavior happens later: waiting, loading, delaying, or responding after a request.
- **Key Terms to Notice:** asynchronous, delay, callback, request, response, loading, JSON.
- **What Students Should Bring into Lecture:** A basic ability to separate "what happens now" from "what happens later."
- **Connection to Lab/Assignment:** Build visible delayed or sequential behavior.
- **Assigned Reading:**
  * **Required - Course Materials:** `Course_Materials/Week_08_Async_Time_Matters_Handout.md`
  * **Skim - JS/JQ:** Chap 8 - Ajax & JSON: selected pages on the idea of requests/responses and JSON: pp 367-383, 396-397
  * **Skim - Course Materials:** `Course_Materials/Week_08_How_To_Read_JSON_Student_Guide.md`, focus on objects, arrays, nested structure, and the final mental model
  * **Reference - Supplemental:** MDN `setTimeout()`: https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout
  * **Reference - Supplemental:** MDN `fetch()`: https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch
  * **Reference - Supplemental:** MDN `Promise`: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

### Week 9 - Modular Thinking: "Breaking Systems into Parts"

- **Preparation Focus:** Larger programs need smaller purposeful parts.
- **Key Terms to Notice:** function, responsibility, separation of concerns, module, reuse.
- **What Students Should Bring into Lecture:** Existing code that can be separated into clearer pieces.
- **Connection to Lab/Assignment:** Split code into logical parts and explain why the structure is easier to manage.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected review on functions as building blocks: pp 88-99
  * **Required - Course Materials:** `Course_Materials/Week_09_Modular_Thinking_Multi_File_Organization_Handout.md`
  * **Reference - Supplemental:** MDN JavaScript Modules: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
  * **Reference - JS/JQ:** Chap 11 - Content Panels: pp 487-526 ('NOTE: If you wish to "jazz" up your projects, Chap 11 is a good resource. However, submit these addtions as a "***version 2***" of your solution!')

### Week 10 - Data: "Beyond the Page"

- **Preparation Focus:** Web pages can use structured data from outside the page or from stored browser information.
- **Key Terms to Notice:** data, JSON, object, array, API, request, response, fetch.
- **What Students Should Bring into Lecture:** A beginner-level idea that structured data can be displayed in the UI.
- **Connection to Lab/Assignment:** Fetch or simulate external data and display selected results.
- **Assigned Reading:**
  * **Review - JS/JQ:** Chap 8 - Ajax & JSON: selected pages on JSON structure: pp 376-377, 382-383, 396-397
  * **Required - JS/JQ:** Chap 9 - APIs: selected pages on what APIs are: pp 409-413
  * **Reference - Shared Course Materials:** `../Approved_API_List.md`, canonical approved API list shared across AAISE courses
  * **Reference - Course Materials:** `Course_Materials/Week_10_API_Guidance_For_Web_Projects.md`, Web Development Foundations guidance for using the shared API list with browser-based `fetch()` work
  * **Reference - JS/JQ:** Chap 12 - Filtering, Searching & Sorting: pp 527-566, use only if the assignment needs it
  * **Reference - JS/JQ:** Chap 9 - APIs: selected pages 3rd party API's: pp 440-448
  * **Required - Course Activity:** JSON Reading Worksheet Quiz in Schoology (Accomplished in class)

### Week 11 - State: "Things Persist"

- **Preparation Focus:** State is information the application remembers and uses to keep the interface consistent.
- **Key Terms to Notice:** state, current value, update, persistence, local storage, saved preference.
- **What Students Should Bring into Lecture:** A sense that interactive apps need to remember information over time.
- **Connection to Lab/Assignment:** Build a small stateful feature such as a saved preference, tracker, or form progress.
- **Assigned Reading:**
  * **Required - JS/JQ:** Chap 9 - APIs: selected pages on Web Storage/local storage/session storage & history: pp 420-427
  * **Required - Course Materials:** `Course_Materials/Week_11_State_LocalStorage_Example.md`
  * **Reference - JS/JQ:** Chap 12 - Data structures or filtering sections as needed for specific projects: pp 525-531, 533, 540-541

---

## Unit (Phase 4) - System Integrity

**Unit 4 intent:** Improve working systems. Readings should support practical judgment, not specialist depth.

### Week 12 - Performance: "Making it Efficient"

- **Preparation Focus:** Working software can still be improved for responsiveness and efficiency.
- **Key Terms to Notice:** performance, efficiency, loading, repeated work, responsiveness, image size.
- **What Students Should Bring into Lecture:** A working page or feature that can be compared before and after refinement.
- **Connection to Lab/Assignment:** Improve sluggish behavior and explain why the revision is better.
- **Assigned Reading:**
  * **Required - Course Materials:** `Course_Materials/Week_12_Performance_Avoiding_Unnecessary_Work.md`
  * **Skim - HTML/CSS:** Chap 16 - Images: selected pages on image sizing/optimization: pp 409-410
  * **Reference - Supplemental:** MDN Throttle Glossary: https://developer.mozilla.org/en-US/docs/Glossary/Throttle
  * **Reference - Supplemental:** MDN Lazy Loading: https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading
  * **Reference - Supplemental:** MDN Responsive Images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images

### Week 13 - Security Awareness: "Building Safely"

- **Preparation Focus:** Build basic trust-boundary awareness without turning this into a security course.
- **Key Terms to Notice:** input, output, validation, XSS, CSRF, CORS, trust boundary, token, safe handling.
- **What Students Should Bring into Lecture:** A recognition that "it works" is not the same as "it is safe."
- **Connection to Lab/Assignment:** Identify unsafe patterns in sample code and apply simple safer practices.
- **Assigned Reading:**
  * **Required - Course Materials:** `Course_Materials/Week_13_Browser_Security_Awareness_For_Web_Projects.md`
  * **Skim - JS/JQ:** Chap 5 - selected pages on XSS only: pp 228-231
  * **Skim - JS/JQ:** Chap 13 - selected pages on submit/password & validation only: pp 576-579, 598-603
  * **Reference - Supplemental:** MDN Cross-site scripting (XSS): https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting
  * **Reference - Supplemental:** MDN CORS Guide: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS

### Week 14 - UX & Styling Refinement: "Make it Better to Use"

- **Preparation Focus:** Improve a working page/app so it is clearer, easier to use, and more polished.
- **Key Terms to Notice:** UX, feedback, affordance, visual hierarchy, transition, animation, accessibility, error state, success state.
- **What Students Should Bring into Lecture:** A working project that can be improved for usability.
- **Connection to Lab/Assignment:** Improve interaction feedback, layout, styling, and user comprehension.
- **Assigned Reading:**
  * **Required - Course Materials:** `Course_Materials/Week_14_UX_Responsive_Refinement_Checklist.md`
  * **Required - HTML/CSS:** Chap 18 - Process & Design: selected pages on audience, goals, and design planning: pp 452-476
  * **Skim - HTML/CSS:** Chap 17 - HTML5 Layout: selected pages on layout/structure review: pp 428-450
  * **Reference - JS/JQ:** Chap 11/12 UI examples only if useful for a student project

### Week 15 - Forms & Input Systems / Capstone Submissions

- **Preparation Focus:** Connect forms, input handling, validation, and capstone planning.
- **Key Terms to Notice:** form, input, label, submit, validation, simulated login, UI state, proposal, scope, prototype.
- **What Students Should Bring into Lecture:** A project idea or interaction idea that could use structured user input.
- **Connection to Lab/Assignment:** Build or extend a form-based interaction and submit a capstone proposal.
- **Assigned Reading:**
  * **Required - HTML/CSS:** Chap 7 - Forms: pp 144-174
  * **Required - JS/JQ:** Chap 13 - Form Enhancement & Validation: selected pages on basic validation concepts: pp 576-579, 598-603 
  * **Required - Course Materials:** `Course_Materials/Week_15_Basic_Simulated_Login_Form_Handout.md`
  * **Required - Course Materials:** `Course_Materials/Week_15_Capstone_Proposal_and_Scope_Guide.md`
  * **Reference - HTML/CSS:** Chap 14 - Lists, Tables & Forms: pp 330-356, use only for styling/reference

---

## Unit (Phase 5) - Capstone

**Unit 5 intent:** Move from guided work to independent build, explanation, and presentation.

### Week 16 - Capstone Build

- **Preparation Focus:** Apply the course layers independently with instructor coaching and peer feedback.
- **Key Terms to Notice:** integration, debugging, revision, explanation, AI-use boundary, final readiness.
- **What Students Should Bring into Lecture:** An approved project plan and a current build.
- **Connection to Lab/Assignment:** Supports independent capstone build time.
- **Assigned Reading:**
  * **Optional - HTML/CSS:** Chap 18 - Process & Design: optional project review: pp 452-476

### Week 17 - Capstone Wrap-Up & Presentations

- **Preparation Focus:** Prepare to demonstrate, explain, and reflect on the final project.
- **Key Terms to Notice:** demonstration, explanation, tradeoff, revision, debugging evidence, AI-use explanation.
- **What Students Should Bring into Lecture:** A completed or nearly completed project and notes on major design/build decisions.
- **Connection to Lab/Assignment:** Supports final presentations and explanation of how the system works across HTML, CSS, JavaScript, data/state, debugging, and refinement.
- **Assigned Reading:**
  * **Required - Course Materials:** `Course_Materials/Week_17_Capstone_Presentation_and_Readiness_Checklist.md`
  * **Required - Course Materials:** `Course_Materials/Week_17_AI_Use_Explanation_Guide.md`
