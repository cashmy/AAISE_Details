# W09B Multi-File Organization Recorded

**10-152-118 Web Development Foundations**  
**Week 9 Wednesday Recorded Lecture**  
**Topic:** Modular Thinking - From Clear Functions To Clear Files

---

# Session Purpose

Wednesday deepens Monday's one-file refactoring by moving selected
responsibilities into multiple JavaScript files.

Students should see multi-file organization as a purposeful next step, not a
requirement to split every project. The same responsibility map remains in
place. The improvement is that related jobs become easier to locate as the
project grows.

The practical target is intentionally controlled:

- decide when a separate file improves navigation
- group related responsibilities instead of splitting randomly
- explain why script loading order matters in the demonstrated approach
- preserve the same visible behavior across the reorganization
- recognize modern JavaScript module syntax without needing to master it

---

# IIM Alignment

Week 9 Wednesday:

- deepen code organization
- connect modular thinking to a practical multi-file structure
- recognize ES modules as a modern file-connection tool

Thursday lab:

- refine function boundaries and names
- simplify the flow between responsibilities
- use multiple files only when they make the student's project clearer

AI role:

- AI as Assistant
- manually written or revised code must come first
- AI may compare organization choices or point out dependencies
- AI may not split the entire project automatically or replace testing and
  explanation

---

# Reading Alignment

Assigned reading:

- **Required - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected review
  on functions as building blocks: pp 88-99
- **Required - Course Materials:**
  `Course_Materials/Week_09_Modular_Thinking_Multi_File_Organization_Handout.md`
- **Reference - Supplemental:** MDN JavaScript Modules
- **Reference - JS/JQ:** Chap 11 - Content Panels: pp 487-526, only for an
  optional version 2 enhancement

Reading-to-lab bridge:

- Monday organized responsibilities inside one JavaScript file.
- Wednesday keeps those responsibilities but gives selected groups their own
  files.
- Thursday asks students to improve clarity based on their own project's size
  and needs.

What students should not try to master yet:

- advanced module graphs
- bundlers or build pipelines
- npm dependency management
- framework architecture
- dynamic imports
- creating a file for every function

---

# Demo Set

Demo folder:

```text
Demos/Week_09_Modular_Thinking/02_wednesday_multi_file_organization/
```

Demo role:

- start from Monday's one-file responsibility map
- move decision logic into `planLogic.js`
- move display logic into `display.js`
- keep input reading, coordination, and event wiring in `app.js`
- load dependency files before `app.js`
- refresh and retest after each move
- compare navigation before and after the split

---

# Slide Sequence Overview

1. Reconnect To Monday
2. The Working Problem: Finding The Right Place
3. What Counts As Success Today
4. Modularity Still Comes First
5. Today's Toolbox
6. One File Can Be Modular
7. When Another File Helps
8. Choose File Boundaries By Responsibility
9. Script Loading Order Matters
10. Dependencies Create An Order
11. Demo: Multi-File Organization
12. Inspect The Three-File Structure
13. Same Behavior, Clearer Navigation
14. Modern JavaScript Modules: Recognition
15. A Larger Project Shape
16. Avoid Over-Splitting
17. AI Assistant: Compare Boundaries
18. Thursday Lab Refinement
19. Evidence And Submission
20. How To Read Next Week's Material
21. Closing

---

# Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday organized one JavaScript file by responsibility:

- read input
- choose a plan
- update the page
- coordinate the feature
- connect the event

Today we keep the same jobs and consider where they should live.
```

**Instructor notes:**

- Reuse Monday's responsibility language exactly.
- Wednesday extends the same model rather than introducing a disconnected
  architecture topic.

**Transition cue:**

- "The reason to consider another file is practical: finding the right place becomes harder as a project grows."

### Slide 2 - The Working Problem: Finding The Right Place

Student-visible text:

```text
A growing project should help us answer:

- Where is the decision logic?
- Where does the page get updated?
- Where are events connected?
- Which file should change for this feature?
- What else could this change affect?

Organization should make those answers easier to find.
```

**Instructor notes:**

- Frame files as navigation aids and responsibility boundaries.
- A multi-file project is only better when the names and boundaries help.

**Transition cue:**

- "Today's success is purposeful organization, not a high file count."

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- explain why a responsibility belongs in a file
- follow the dependency order between files
- preserve the same behavior after moving code
- recognize `type="module"`, `import`, and `export`
- decide when one file is still the clearer choice
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate image for this slide.
- Include the final bullet to prevent multi-file work from becoming dogma.

**Transition cue:**

- "The distinction from Monday still controls every decision."

### Slide 4 - Modularity Still Comes First

Student-visible text:

```text
Modularity is the design habit.

A module or separate file is an implementation choice.

Good question:

"Will this boundary make the responsibility easier to find, understand, or reuse?"

If the answer is no, the split may not help.
```

**Instructor notes:**

- Reinforce the handout's opening distinction.
- Use this as the decision rule throughout the recording.

**Transition cue:**

- "The tools today add files and dependency order to Monday's responsibility map."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- responsibility boundaries
- purposeful file names
- `planLogic.js`
- `display.js`
- `app.js`
- script loading order
- dependency
- retesting after each move
```

**Instructor notes:**

- Keep `import` and `export` out of the primary toolbox because the actual demo
  uses ordered script tags.
- Formal modules appear later as recognition.

**Transition cue:**

- "Before splitting anything, remember that Monday's one-file version was already modular."

### Slide 6 - One File Can Be Modular

Student-visible text:

```text
One JavaScript file can be well organized when:

- responsibilities are clear
- functions have purposeful names
- event handlers stay focused
- related code remains easy to find
- the file is still comfortable to navigate

Multiple files are an option, not a badge of quality.
```

**Instructor notes:**

- Protect Assignment 9's actual requirement: clear functions and
  responsibilities.
- Students do not need multiple files to succeed.

**Transition cue:**

- "A separate file becomes useful when it gives a related responsibility a clearer home."

### Slide 7 - When Another File Helps

Student-visible text:

```text
Consider another file when a responsibility:

- has a clear name and purpose
- contains related behavior
- may grow independently
- may be reused on another page
- is difficult to locate in the current file

The boundary should reduce searching and confusion.
```

**Instructor notes:**

- Use decision logic and display logic as the immediate examples.
- Do not turn each bullet into a mandatory rule.

**Transition cue:**

- "The file name should describe the responsibility it contains."

### Slide 8 - Choose File Boundaries By Responsibility

Student-visible text:

```text
Example responsibility groups:

`planLogic.js`
- chooses a study plan
- does not update the page

`display.js`
- updates the visible result

`app.js`
- reads input
- coordinates the feature
- connects the click event
```

**Instructor notes:**

- Explain why these boundaries make sense for this small demo.
- A different project may need different groups.
- `app.js` acts as the assembly point for the feature.

**Transition cue:**

- "Because one file uses work defined in another, the browser must receive them in a usable order."

### Slide 9 - Script Loading Order Matters

Student-visible text:

```text
In today's demo, HTML loads three scripts:

1. `planLogic.js`
2. `display.js`
3. `app.js`

`app.js` calls functions defined by the first two files.

The needed functions must exist before `app.js` uses them.
```

**Instructor notes:**

- Show the bottom of `index.html` beside this slide.
- This explains the demonstrated approach, not every possible JavaScript
  loading strategy.

**Transition cue:**

- "That order reveals a dependency."

### Slide 10 - Dependencies Create An Order

Student-visible text:

```text
A dependency exists when one part needs another part.

Here:

- `app.js` needs `choosePlan()`
- `app.js` needs `updateResult()`
- those functions must be available first

Dependencies should be visible enough to explain and test.
```

**Instructor notes:**

- Define dependency in plain language.
- Avoid package-management or dependency-injection tangents.
- Ask what error students might expect if `app.js` loads first.

**Transition cue:**

- "Now we will move one responsibility at a time and test the dependency order."

### Slide 11 - Demo: Multi-File Organization

Student-visible text:

```text
Demo: one working feature, three JavaScript files

Watch for:

- decision logic moves to `planLogic.js`
- display logic moves to `display.js`
- coordination stays in `app.js`
- HTML loads dependencies before `app.js`
- the page is refreshed after each move

The visible behavior should stay the same.
```

**Instructor notes:**

- Use `Demos/Week_09_Modular_Thinking/02_wednesday_multi_file_organization/`.
- Begin from Monday's one-file version.
- Type the new file names and moved function blocks.
- Retest after each extraction and deliberately inspect script order.

**Transition cue:**

- "The browser result did not change, so the value appears in how quickly we can navigate the code."

### Slide 12 - Inspect The Three-File Structure

Student-visible text:

```text
Finished structure:

`planLogic.js` owns the decision.

`display.js` owns the page update.

`app.js` connects input, decision, display, and event.

Each file name answers a navigation question.
```

**Instructor notes:**

- Open the three files in tabs or the file explorer.
- Ask where a change to the study-plan rule belongs.
- Ask where a change to the visible result belongs.

**Transition cue:**

- "The feature has the same output, but the path to a change is clearer."

### Slide 13 - Same Behavior, Clearer Navigation

Student-visible text:

```text
Before and after should produce the same result.

The improvement is structural:

- decision code has a clear home
- display code has a clear home
- coordination remains easy to trace
- a future change has a likely destination

Refactoring succeeds only when the behavior still works.
```

**Instructor notes:**

- Compare behavior first, then navigation.
- Reinforce that no new feature was needed to make a meaningful improvement.

**Transition cue:**

- "Modern JavaScript also has formal syntax for connecting files."

### Slide 14 - Modern JavaScript Modules: Recognition

Student-visible text:

```text
Modern JavaScript may connect files with:

`<script type="module" src="js/app.js"></script>`

`export` makes a named value available.

`import` uses that named value in another file.

For now, recognize the pattern and the purpose.
```

**Instructor notes:**

- Keep this at recognition level, aligned with the handout and reading guide.
- Explain that the demo used a simpler ordered-script approach to expose the
  dependency clearly.
- Do not convert the demo unless time and student readiness support it.

**Transition cue:**

- "The same responsibility thinking scales into a larger capstone folder."

### Slide 15 - A Larger Project Shape

Student-visible text:

```text
A larger project may grow into:

project/
  index.html
  about.html
  css/style.css
  js/navigation.js
  js/validation.js
  js/data.js
  js/app.js
  images/

Names should help a future reader find the responsibility.
```

**Instructor notes:**

- Present this as a next-step model for capstone planning.
- It is not a required folder checklist.
- Connect shared CSS and JavaScript to multi-page projects.

**Transition cue:**

- "Growth needs boundaries, but too many boundaries can create a different kind of confusion."

### Slide 16 - Avoid Over-Splitting

Student-visible text:

```text
Too much splitting can make code harder to follow.

Warning signs:

- one tiny function per file
- vague names such as `helpers.js`
- constant jumping between files
- dependencies that are difficult to trace
- more structure than the project needs

Use the simplest organization that stays clear.
```

**Instructor notes:**

- Normalize keeping small projects in one file.
- The goal is reduced cognitive load, not architecture for its own sake.

**Transition cue:**

- "AI can help compare possible boundaries after the student has created and understood the first structure."

### Slide 17 - AI Assistant: Compare Boundaries

Student-visible text:

```text
AI as Assistant can compare organization choices.

Before asking, provide:

- the code you manually wrote or revised
- what already works
- the responsibilities you identified
- the boundary you are considering

Ask for tradeoffs, not a complete rewrite.
You still choose, move, test, and explain the code.
```

**Instructor notes:**

- Reinforce the Week 9-12 manual-first constraint.
- Refer students back to Monday's prompt pattern.
- AI advice does not prove that a boundary fits the student's project.

**Transition cue:**

- "Thursday applies the same judgment to each student's current project."

### Slide 18 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab:

Improve the structure you created Tuesday.

Check:

- Does each function have one explainable job?
- Do names communicate purpose?
- Is the flow between functions easy to trace?
- Would another file genuinely make navigation easier?
- Does the application still work after every change?
```

**Instructor notes:**

- Connect directly to Assignment 9 Iteration 2.
- One improvement that simplifies or clarifies the system is enough.
- Multiple files remain optional.

**Transition cue:**

- "The final evidence should explain the design decision, not merely list the files."

### Slide 19 - Evidence And Submission

Student-visible text:

```text
Final submission evidence:

- working HTML, CSS, and JavaScript
- purposeful functions
- clear responsibility boundaries
- readable flow between parts
- no unnecessary duplicated logic
- a short reflection on what became easier to understand

Explain the organization you chose and why it fits your project.
```

**Instructor notes:**

- Align with Assignment 9 and the success criteria.
- Students may submit one or multiple JavaScript files based on the approved
  submission workflow; clarity remains the criterion.

**Transition cue:**

- "Next week, the organized system will receive structured data from beyond the page."

### Slide 20 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- understand what an API provides
- notice request, response, object, array, and JSON

Review:
- revisit the JSON shape examples from Week 8

Reference:
- use the approved API list and Web project guidance during lab

Read for the data path: request, response, structure, display.
```

**Instructor notes:**

- Point students to the exact Week 10 entries in the reading guide.
- Emphasize selected pages and course guidance rather than the full API
  chapter.
- Students should bring recognition, not API mastery.

**Transition cue:**

- "Organization gives incoming data a clear path through the program."

### Slide 21 - Closing

Student-visible text:

```text
Modular thinking scales in stages:

1. identify responsibilities
2. name them with clear functions
3. group related work
4. create another file only when it helps
5. preserve behavior after every change

The best structure is one you can navigate, test, and explain.
```

**Instructor notes:**

- Close the Monday-Wednesday progression explicitly.
- Preview Week 10 without beginning API implementation.

**Transition cue:**

- "Next week, we follow structured data through the parts you now know how to organize."

---

# AI Use Notes

AI remains an Assistant in Week 9. Students must supply manually written or
revised code, current working behavior, identified responsibilities, and a
focused organization question. AI may compare boundaries or name tradeoffs.
Students still choose the structure, make the changes, retest the application,
and explain the result.

---

# Image Prompt Notes

Use the Week 9 prompt packet for the following:

| Slide | Image Concept | Prompt Packet Note |
| --- | --- | --- |
| 1 | Monday responsibility map reconnect | Include in Week 9 prompt packet |
| 2 | finding the right place in growing code | Include in Week 9 prompt packet |
| 4 | modularity before file choice | Include in Week 9 prompt packet |
| 5 | multi-file toolbox | Include in Week 9 prompt packet |
| 6 | one organized file | Include in Week 9 prompt packet |
| 7 | decision point for another file | Include in Week 9 prompt packet |
| 8 | three responsibility-based files | Include in Week 9 prompt packet |
| 9 | script loading order | Include in Week 9 prompt packet |
| 10 | visible dependency direction | Include in Week 9 prompt packet |
| 11 | multi-file organization demo | Include in Week 9 prompt packet |
| 12 | three-file structure inspection | Include in Week 9 prompt packet |
| 13 | same behavior, clearer navigation | Include in Week 9 prompt packet |
| 14 | import/export recognition | Include in Week 9 prompt packet |
| 15 | larger capstone project shape | Include in Week 9 prompt packet |
| 16 | over-splitting warning | Include in Week 9 prompt packet |
| 17 | AI comparing boundaries after manual work | Include in Week 9 prompt packet |
| 21 | modular thinking progression | Include in Week 9 prompt packet |

No separate image prompt is needed for Slide 3 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- Monday reconnect and problem framing: 5-8 minutes
- one-file versus multi-file decision: 8-12 minutes
- file boundaries, loading order, and dependencies: 12-15 minutes
- multi-file demo and inspection: 15-20 minutes
- modern modules and capstone-scale organization: 8-12 minutes
- AI Assistant reminder, lab refinement, and next reading: 6-10 minutes

