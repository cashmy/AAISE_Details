# HTML, CSS, and JavaScript High-Level Course Plan v1

## Course

`10-152-118` - `HTML, CSS, and JavaScript`

Credits: `3`  
Lecture/Lab: `36/36`  
Prerequisite: `n/a`

## Source Description

Learners develop foundational web development skills using HTML, CSS, and
JavaScript to create structured, styled, and interactive web pages. The course
emphasizes multi-page website structure, visual design, responsive layout,
browser-based interactivity, debugging, system behavior, and iterative
refinement. Students learn HTML, CSS, and JavaScript as distinct technologies
while gradually experiencing them as interacting layers within a complete web
system. AI-assisted tools are introduced later in the course as supports for
explanation, debugging, refinement, and capstone acceleration, not as a
replacement for human design judgment or technical understanding.

## Planning Position

This course should function as the bridge sequence's foundational browser-based
web development course. Its primary responsibility is to help students create
visible, usable, interactive software artifacts in the browser while developing
layer awareness:

```text
HTML       -> structure and meaning
CSS        -> appearance, layout, responsiveness, and usability
JavaScript -> logic, behavior, interaction, data, and state
Debugging  -> visual inspection, console tracing, browser tools, AI assistance
AI support -> explanation, comparison, refinement, and accountable acceleration
```

The course should preserve the traditional distinction between HTML, CSS, and
JavaScript, but it should not leave students thinking of them as isolated
checklists. The central movement is:

```text
structure -> style -> behavior -> systems -> integrity -> capstone ownership
```

This makes the course different from `10-152-117 Python Programming`. Python is
where students build general programming confidence and console-based logic.
This course gives them a browser-visible medium where structure, styling,
interaction, and user experience can be inspected directly. JavaScript should be
introduced as a general-purpose programming language that can control web
behavior, not only as a DOM-manipulation trick.

The course should also delay normal AI use until students have enough design,
debugging, and implementation judgment to evaluate AI output. The intended AI
progression is:

```text
manual native work -> assisted explanation/debugging -> strategic capstone use
```

## Delivery Frame

This is a 17-week, 3-credit course with `36` lecture hours and `36` lab hours.
The course uses a layered accumulation model where students continue improving
visible artifacts while adding new technical layers over time.

The weekly learning model combines:

- in-class guided builds, coaching, debugging, and application
- video lecture or asynchronous concept introduction
- homework for reinforcement, extension, and iteration

The course should repeatedly connect concept, visible result, debugging, and
explanation. Students should experience difficulty as a phase transition rather
than as random failure.

## Relationship to Concurrent and Later Courses

This course is part of the first semester bridge foundation alongside:

- `10-152-117 Python Programming`
- `10-152-119 Introduction to Algorithms`

Its role is to make software visible and interactive in the browser while Python
builds general programming confidence and Algorithms later strengthens reasoning
about approaches, structure, and efficiency.

The course should coordinate with `10-152-117` in a staged way:

- Early HTML and CSS give students fast visible wins while Python builds
  console-based programming foundations.
- JavaScript should arrive after students understand page structure and style,
  and after Python has started building basic programming habits.
- JavaScript logic should connect back to programming ideas students encounter
  in Python, including variables, conditionals, functions, debugging, and
  explanation.
- Browser debugging should extend students' general debugging identity: first
  visual inspection, then console logging, then browser developer tools, and
  later AI-assisted debugging.

The course should prepare students for later front-end, full-stack, and
application-development work by establishing:

- semantic structure and multi-page organization
- CSS readability, spacing, layout, visual consistency, and responsiveness
- JavaScript as both programming logic and browser behavior
- events, DOM interaction, async behavior, data, state, and modular thinking
- UX refinement, performance awareness, security awareness, and explanation
- accountable AI use during refinement and capstone work

## High-Level Time Allocation

Suggested emphasis:

```text
15% HTML structure, semantic organization, multi-page sites, and file workflow
20% CSS styling, layout, responsiveness, visual hierarchy, and usability
25% JavaScript language foundations, browser interaction, DOM, events, and
    structured behavior
15% system thinking: async behavior, modules, APIs/data, state, and integration
10% debugging, browser tools, evaluation, testing, and explanation
10% system integrity: performance, security awareness, UX refinement, and polish
5% AI-assisted refinement, capstone acceleration, and use justification
```

## 17-Week Draft Structure

The course is organized into five phases:

```text
Weeks 1-3   -> Foundations
Weeks 4-7   -> Behavior
Weeks 8-11  -> System Thinking
Weeks 12-15 -> System Integrity
Weeks 16-17 -> Capstone
```

### Week 1 - HTML: Something Exists

Purpose: establish that a web page is a structured document that can be created,
organized, linked, and viewed in a browser.

Topics:

- HTML document structure
- Headings, paragraphs, lists, links, and basic semantic elements
- File-to-browser workflow
- Multi-page site organization
- Folder and file naming habits

Lab direction:

- Build a simple two- or three-page site
- Focus on structure rather than appearance
- Explain what each page contains and how pages connect
- Establish the first visible win: something exists in the browser

### Week 2 - CSS: I Can Control Appearance

Purpose: separate structure from presentation and give students control over
readability, spacing, color, and basic visual consistency.

Topics:

- CSS as a separate layer from HTML
- Selectors, classes, IDs, and basic specificity
- Typography, color, spacing, and visual clarity
- Consistent styling across pages
- Design intention as readability and usability, not decoration alone

Lab direction:

- Style the Week 1 site
- Improve spacing, typography, colors, and consistency
- Identify common CSS mistakes and overwritten styles
- Explain how styling changes affect readability

### Week 3 - Layout: Control Space

Purpose: move from page styling into intentional layout and responsive thinking.

Topics:

- Box model
- Flexbox and layout structure
- Spacing, alignment, and section organization
- Media queries and basic responsiveness
- Iteration mindset

Lab direction:

- Redesign page layout using Flexbox
- Improve a site across multiple screen sizes
- Diagnose layout problems visually
- Explain how layout decisions affect user experience

### Week 4 - JavaScript: This Is Programming

Purpose: introduce JavaScript as a programming language before connecting it to
the page.

Topics:

- JavaScript as a separate system
- Variables, values, expressions, conditionals, and functions
- Predict-run-observe workflow
- Console-based logic exercises
- Common logic mistakes

Lab direction:

- Solve small JavaScript logic exercises outside the DOM
- Use console output to observe behavior
- Predict results before running code
- Connect the experience back to Python programming habits where useful

### Week 5 - DOM: Now It Connects

Purpose: connect JavaScript logic to visible browser behavior.

Topics:

- DOM as the bridge between HTML and JavaScript
- Events and event-driven thinking
- Query selectors, IDs, classes, and element references
- Button clicks, input responses, and dynamic updates
- Common null-reference and selector mistakes

Lab direction:

- Add button interactions to an existing page
- Change text, styles, or visibility dynamically
- Respond to user input
- Explain how the HTML, CSS, and JavaScript layers interact

### Week 6 - Debugging: Things Break, and I Can Fix Them

Purpose: make debugging a visible, structured process across HTML, CSS, and
JavaScript.

Topics:

- Debugging as process rather than panic
- Visual debugging for layout and styling
- Console logging for behavior tracing
- Browser developer tools for inspecting elements and styles
- Cause versus symptom

Lab direction:

- Fix intentionally broken multi-layer examples
- Diagnose whether issues originate in structure, style, or behavior
- Use console output and browser inspection tools
- Explain what was wrong and why the fix works

### Week 7 - Structured Behavior

Purpose: improve JavaScript organization so interactive behavior remains
readable and maintainable.

Topics:

- Functions, callbacks, and event-handling structure
- Cleaner versus messier interaction code
- Reuse and responsibility
- Basic code organization patterns
- Structured interaction features

Lab direction:

- Refactor messy interaction code into functions
- Add a multi-step interactive feature
- Compare working code with better-structured code
- Explain how organization affects maintainability

### Week 8 - Async: Time Matters

Purpose: introduce the idea that browser applications often wait, delay, load,
or respond over time.

Topics:

- Asynchronous behavior at an introductory level
- Delayed actions and time-based behavior
- Loading states and user feedback
- Sequential versus delayed execution
- API calls as a future-facing reason async matters

Lab direction:

- Simulate delayed actions with beginner-friendly patterns
- Add loading or delayed feedback behavior
- Explain what happens immediately and what happens later
- Keep the focus conceptual and applied rather than deep JavaScript theory

### Week 9 - Modular Thinking

Purpose: help students move from individual features toward organized systems.

Topics:

- Separation of concerns
- Modules or module-shaped organization
- Splitting code into logical parts
- Responsibility boundaries
- Scaling beyond one script file

Lab direction:

- Refactor prior work into a more modular structure
- Separate responsibilities across files or logical sections
- Explain why a system is easier to maintain after refactoring
- Prepare students for larger integrated work

### Week 10 - Data: Beyond the Page

Purpose: connect browser applications to data beyond static page content.

Topics:

- Data flow from source to UI
- APIs or simulated external data
- `fetch` at an introductory level where appropriate
- JSON-shaped data
- Local storage as a simple browser persistence option

Lab direction:

- Fetch or simulate external data
- Display selected data dynamically
- Explain request, response, data selection, and UI update flow
- Use approved, low-complexity data sources or controlled examples

### Week 11 - State: Things Persist

Purpose: show how applications remember, update, and reflect information over
time.

Topics:

- State as remembered application information
- UI reflecting current data
- Local variables, local storage, or simple persistence
- Consistent updates
- Light recognition of SPA-style thinking

Lab direction:

- Build a stateful feature such as a cart, form flow, toggle system, tracker, or
  saved preference
- Ensure the UI reflects state changes consistently
- Explain where the information lives and how it changes
- Connect persistence to user expectations

### Week 12 - Performance

Purpose: introduce the idea that working software can still be improved for
speed, responsiveness, and efficiency.

Topics:

- Performance as user experience
- Inefficient interactions
- Debounce and throttle at an introductory level
- Avoiding unnecessary work
- Measuring or observing sluggish behavior

Lab direction:

- Improve an inefficient interaction
- Compare before and after behavior
- Explain why the optimized version is better
- Keep performance practical and visible

### Week 13 - Security Awareness

Purpose: develop basic trust-boundary awareness without turning the course into
a security course.

Topics:

- Unsafe input and output patterns
- XSS, CSRF, and CORS at a conceptual level
- Trust boundaries
- Safe handling of user input
- Security as part of reliability and professionalism

Lab direction:

- Identify unsafe patterns in sample code
- Apply simple fixes or safer practices
- Explain the risk in plain language
- Coordinate conceptually with broader security coursework where useful

### Week 14 - UX and Styling Refinement

Purpose: refine working pages into clearer, more usable, more polished web
solutions.

Topics:

- Usability and visual feedback
- Animation and transitions
- Form clarity and interaction feedback
- Accessibility-minded readability and affordances
- Good versus distracting refinement

Lab direction:

- Improve a working project for usability and polish
- Add appropriate transitions, feedback, or layout improvements
- Test whether users can understand and use the interface
- Explain design choices using usability language

### Week 15 - Pre-Capstone Integration

Purpose: move students from guided work toward independent project planning and
initial execution.

Topics:

- Forms and integrated interaction
- Capstone expectations
- Project planning and scope
- Feasibility and early prototype decisions
- AI-use boundaries for final work

Lab direction:

- Build or extend a form-based interaction
- Submit a capstone proposal
- Begin an initial prototype
- Explain structure, styling, behavior, risks, and planned AI use

### Week 16 - Capstone Build

Purpose: give students supported independent build time for an approved complete
web solution.

Topics:

- Independent implementation
- Debugging and troubleshooting without full scaffolding
- Integration of HTML, CSS, JavaScript, data, state, and refinement
- Strategic AI use with student control
- Final readiness checks

Lab direction:

- Build the approved capstone project
- Use instructor coaching and peer feedback
- Apply debugging and browser tools
- Use AI strategically for explanation, debugging, refinement, or acceleration
  while preserving authorship

### Week 17 - Capstone Presentation

Purpose: evaluate understanding through demonstration, explanation, and
communication.

Topics:

- Final project demonstration
- Explanation of structure, styling, behavior, data/state, and debugging
- Design choices and tradeoffs
- Challenges and revisions
- AI-use explanation where applicable

Lab direction:

- Present the final project
- Demonstrate working functionality
- Explain how the system works across layers
- Account for major decisions, problems, fixes, and AI assistance

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Create structured multi-page websites using semantic HTML.
- Apply CSS to control typography, color, spacing, layout, visual consistency,
  and basic responsiveness.
- Write basic JavaScript using variables, conditionals, functions, events, and
  DOM interaction.
- Connect HTML, CSS, and JavaScript so browser-based systems respond visibly to
  user input.
- Debug web applications using visual inspection, console logging, browser tools,
  and structured explanation.
- Organize interactive behavior into clearer, more maintainable code.
- Use introductory async, data, API, local storage, and state patterns to build
  richer browser-based features.
- Apply basic performance, security-awareness, and UX-refinement thinking to
  improve working solutions.
- Use AI-assisted tools appropriately for explanation, debugging, refinement, or
  capstone acceleration after foundational understanding is established.
- Present and explain a complete web solution, including structure, styling,
  behavior, debugging, design choices, and AI use where applicable.

## Notes for Future Detailed Design

- Preserve the five-phase structure. It is central to the course's student
  experience: foundations, behavior, system thinking, system integrity, and
  capstone ownership.
- Keep Week 4 JavaScript logic-first before DOM integration. This avoids
  trapping students into thinking JavaScript only exists to manipulate page
  elements.
- Maintain the debugging progression: visual debugging, console logging, browser
  developer tools, then AI-assisted debugging.
- Treat UX as a practical web-development concern, not as a full design course.
  The goal is readable, usable, coherent interfaces.
- Keep security and performance introductory and applied. Students should build
  awareness and safer habits without being overwhelmed by specialist depth.
- Delay normal AI use until students have enough implementation and debugging
  judgment to inspect and revise AI output.
- Coordinate with `10-152-117` so JavaScript benefits from students' growing
  programming foundation, while still being taught in its own browser-based
  context.
- Coordinate with later application-development courses so this course provides
  durable browser, interface, debugging, and interaction foundations without
  becoming a framework course.
