# W09A Modular Thinking Live

**10-152-118 Web Development Foundations**  
**Week 9 Monday Live Lecture**  
**Topic:** Modular Thinking - Breaking Systems Into Parts

---

# Session Purpose

Week 9 helps students manage growing JavaScript by separating behavior into
clear responsibilities.

Students should first understand that modularity is a design habit and a module
is one possible implementation tool. Monday keeps the work in one JavaScript
file so students can see that good organization begins before files are split.

The practical target is intentionally focused:

- identify the responsibilities inside working code
- extract those responsibilities into clearly named functions
- use one coordinating function to connect the parts
- preserve behavior while reorganizing code
- explain why the new structure is easier to follow

---

# IIM Alignment

Week 9 Monday:

- code organization
- ES modules concept
- larger programs need smaller purposeful parts

Tuesday lab:

- split code into logical responsibilities
- preserve existing behavior
- explain how the revised organization reduces confusion

AI role:

- AI as Assistant begins in Week 9
- students must manually write or revise relevant code before requesting help
- AI may suggest possible responsibility boundaries or clearer names
- AI may not start the assignment, rewrite the whole project, or replace the
  student's explanation

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

- The textbook review reinforces functions as named building blocks.
- The course handout distinguishes modularity from modules and shows how
  responsibility can guide file and function organization.
- Monday applies modularity inside one JavaScript file.
- Tuesday asks students to reorganize their own existing behavior.

What students should not try to master yet:

- build tools or bundlers
- npm package workflows
- framework folder structures
- advanced `import` and `export` patterns
- one function per file
- a perfect or professional-scale architecture

---

# Prior Lab Review

Use the Week 8 success solution:

```text
Assignments/Success_Solutions/Week_08_Asynchronous_Behavior/
```

Review rhythm:

1. Run the Study Sprint planner normally.
2. Click the delayed reminder button.
3. Identify the immediate waiting message and the later result.
4. Show the functions that support the working behavior.
5. Ask where each responsibility would be easiest to find as the project grows.

Bridge:

```text
Last week we made timing visible.
This week we make growing behavior easier to find and change.
```

---

# Demo Set

Demo folder:

```text
Demos/Week_09_Modular_Thinking/01_monday_one_file_responsibilities/
```

Demo role:

- start from one working event handler
- identify reading, decision, display, and event responsibilities
- extract `readMinutes()`, `choosePlan(minutes)`, and `updateResult(message)`
- keep `handlePlanClick()` as the coordinator
- retest after each small extraction
- show that the behavior stays the same while the structure improves

---

# Slide Sequence Overview

1. Breaking Systems Into Parts
2. Previous Lab Review / Success Path
3. From Timing To Organization
4. Modularity And Modules
5. What Counts As Success Today
6. Today's Toolbox
7. Parked For Later
8. Complexity Grows Quietly
9. Separation Of Concerns
10. Responsibilities Come Before Files
11. Functions Give Responsibilities Names
12. A Coordinator Connects The Parts
13. Refactoring Preserves Behavior
14. Demo: One File, Clear Responsibilities
15. Inspect The Responsibility Map
16. AI Role: Assistant
17. Useful AI Prompt Pattern
18. Tuesday Lab Bridge
19. Evidence Expectations
20. Closing

---

# Slide-By-Slide Source

### Slide 1 - Breaking Systems Into Parts

Student-visible text:

```text
Working code can still become difficult code.

As a program grows, we need to know:

- where each job belongs
- which part should change
- what must stay working
- how the parts connect

Modular thinking makes a larger system understandable.
```

**Instructor notes:**

- Frame the week as managing growth, not adding a flashy new feature.
- Students already have enough behavior for organization to matter.
- Keep the focus on clarity and changeability.

**Transition cue:**

- "First, let's revisit the timed behavior that gave our program one more responsibility."

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Previous lab review:

- an action starts now
- waiting is visible
- a result appears later
- the existing planner still works

One successful path used small functions to keep the timing explainable.
```

**Instructor notes:**

- Open the Week 8 success solution and run the delayed reminder.
- Present it as one successful path, not the only answer.
- Point out that each added feature increases the number of jobs the script has.

**Transition cue:**

- "The behavior works. Our next question is whether we can still find and explain each job."

### Slide 3 - From Timing To Organization

Student-visible text:

```text
Week 8 asked:

- What happens now?
- What happens later?

Week 9 adds:

- Which part owns this job?
- Where should a future change happen?
- Can I explain the structure without tracing every line?
```

**Instructor notes:**

- Preserve the progression from behavior over time to system organization.
- Organization should answer practical questions, not merely look tidy.

**Transition cue:**

- "Two closely related words will guide this week, and they do not mean exactly the same thing."

### Slide 4 - Modularity And Modules

Student-visible text:

```text
Modularity is the habit:

Break a larger system into understandable parts with clear jobs.

A module is one possible tool:

Place a related piece of code in a file or code unit that another part can use.

You can practice modularity before using multiple files.
```

**Instructor notes:**

- Make this distinction explicit before any file organization appears.
- Repeat that modularity describes the design idea.
- A module is one way to express that idea in code.

**Transition cue:**

- "Today succeeds when students can find the jobs before they think about extra files."

### Slide 5 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- identify separate responsibilities in working code
- give each responsibility a clear function name
- connect the functions through a simple coordinator
- reorganize without changing the result
- explain why the new structure is easier to follow
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate image for this slide.
- Emphasize that file count is not a success measure.

**Transition cue:**

- "The toolbox is mostly made from ideas students have already used."

### Slide 6 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- responsibility
- separation of concerns
- clear function names
- parameters and return values
- coordinator function
- event handler
- small-step refactoring
- retesting
```

**Instructor notes:**

- Connect parameters and return values back to Week 7.
- Name refactoring as changing structure while preserving behavior.

**Transition cue:**

- "Several professional tools sit nearby, but they are not needed for today's goal."

### Slide 7 - Parked For Later

Student-visible text:

```text
Parked for later:

- bundlers and build tools
- npm package workflows
- framework architectures
- advanced `import` / `export`
- dependency injection
- the "perfect" folder structure

For now:

Find the responsibilities. Name them clearly. Keep the program working.
```

**Instructor notes:**

- Protect students from interpreting modularity as professional tooling.
- Native modules receive recognition-level coverage on Wednesday.

**Transition cue:**

- "The need for organization often appears before a program looks large."

### Slide 8 - Complexity Grows Quietly

Student-visible text:

```text
A script becomes harder to manage when one place must:

- read user input
- validate or decide
- calculate a result
- update the page
- handle timing
- respond to events

Each job may be small. Together they create cognitive load.
```

**Instructor notes:**

- Use the current Study Sprint progression as the familiar example.
- Avoid suggesting that line count alone determines complexity.
- The problem is mixed responsibility and difficult navigation.

**Transition cue:**

- "Separation of concerns gives us a way to name those jobs."

### Slide 9 - Separation Of Concerns

Student-visible text:

```text
Separation of concerns means giving different jobs clear homes.

In a beginner web project:

- HTML provides structure and content
- CSS controls appearance and layout
- JavaScript controls behavior

Inside JavaScript, responsibilities can also be separated.
```

**Instructor notes:**

- Connect to the course's structure, style, behavior progression.
- Explain that concerns still cooperate; separation does not mean isolation.

**Transition cue:**

- "The same idea applies inside a single JavaScript file."

### Slide 10 - Responsibilities Come Before Files

Student-visible text:

```text
Before creating more files, identify the jobs:

- read input
- make a decision
- prepare a result
- display the result
- respond to the user's action

Split by purpose, not by random line count.
```

**Instructor notes:**

- This is the main guardrail for the week.
- Students should not create one file or one function for every tiny action.
- Ask, "Can I describe this job in one sentence?"

**Transition cue:**

- "Functions let us give each useful job a name."

### Slide 11 - Functions Give Responsibilities Names

Student-visible text:

```text
A clear function name answers:

"What job does this part perform?"

Examples:

- `readMinutes()` gets input
- `choosePlan(minutes)` makes a decision
- `updateResult(message)` changes the page

Names reduce the amount of code we must hold in memory at once.
```

**Instructor notes:**

- Read each name aloud as a plain-language job.
- Point out how parameters and return values move information between parts.

**Transition cue:**

- "Once the jobs have names, one function can coordinate their order."

### Slide 12 - A Coordinator Connects The Parts

Student-visible text:

```text
A coordinator function tells the story of the feature:

1. read the minutes
2. choose a plan
3. update the result

`handlePlanClick()` connects the parts.

It coordinates the work instead of containing every detail.
```

**Instructor notes:**

- Use the demo's `handlePlanClick()` as the concrete example.
- Distinguish coordinating from doing every job directly.
- Keep the term beginner-friendly; this is not an architecture-pattern lecture.

**Transition cue:**

- "Reorganization only helps if the feature still behaves correctly."

### Slide 13 - Refactoring Preserves Behavior

Student-visible text:

```text
Refactoring changes the structure of working code.

The visible behavior should stay the same.

Safe rhythm:

1. make one small structural change
2. run the page
3. verify the same result
4. continue only after it works
```

**Instructor notes:**

- Connect directly to the Week 6 debugging discipline.
- Warn against rewriting everything and testing only at the end.

**Transition cue:**

- "Now we will apply that rhythm to one working event handler."

### Slide 14 - Demo: One File, Clear Responsibilities

Student-visible text:

```text
Demo: one file, clear responsibilities

Watch for:

- the original behavior works first
- one responsibility moves at a time
- each function receives a purposeful name
- `handlePlanClick()` coordinates the feature
- the browser is retested after each change

The result should behave exactly as it did before.
```

**Instructor notes:**

- Use `Demos/Week_09_Modular_Thinking/01_monday_one_file_responsibilities/`.
- Start from a working event handler and extract the named functions live.
- Type the key function boundaries manually.
- Paste only larger unchanged sections if time compression is needed.

**Transition cue:**

- "The page looks the same, so we inspect the structure to see the improvement."

### Slide 15 - Inspect The Responsibility Map

Student-visible text:

```text
The finished script now has a responsibility map:

- input: `readMinutes()`
- decision: `choosePlan(minutes)`
- display: `updateResult(message)`
- coordination: `handlePlanClick()`
- event connection: `addEventListener(...)`

Each part has a reason to exist.
```

**Instructor notes:**

- Keep the finished script open while using this slide.
- Ask where students would change the decision rule or display behavior.
- The ability to locate a change is evidence of useful organization.

**Transition cue:**

- "Week 9 also changes the allowed AI role, but only after students have written code themselves."

### Slide 16 - AI Role: Assistant

Student-visible text:

```text
AI as Assistant begins this week.

You must manually write or revise relevant code first.

AI may help you:

- identify possible responsibility groups
- compare two organization choices
- suggest clearer function names
- explain a small structural tradeoff

AI may not start the assignment or rewrite the whole project.
```

**Instructor notes:**

- Explicitly mark the role change from Explainer to Assistant.
- Manual-first work is a hard constraint for Weeks 9-12.
- Students remain responsible for testing and explaining every accepted change.

**Transition cue:**

- "A useful prompt proves that the student already has code and asks for focused help."

### Slide 17 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I manually wrote this JavaScript first.
It currently [describe what works].
The code feels difficult to follow because [specific concern].

Do not rewrite the project.
Identify the responsibilities you see and suggest two possible function
boundaries. Explain why each boundary may help.
Ask any clarifying questions before suggesting code."
```

**Instructor notes:**

- Model pasting only the small relevant section, not an entire repository.
- The student asks for analysis and alternatives before code generation.
- Require the student to decide which suggestion fits their own project.

**Transition cue:**

- "Tuesday begins with the same manual responsibility check."

Visual notes:

- Use a document-style prompt form with fields for manual work, current
  behavior, specific concern, constraint, requested help, and clarifying
  question.

### Slide 18 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab:

Restructure existing JavaScript into clearer parts.

Your first iteration should include:

- at least 3-4 purposeful functions
- separate event, data or decision, and display responsibilities
- less complexity inside event listeners
- the same working behavior after reorganization

Multiple JavaScript files are optional, not required.
```

**Instructor notes:**

- Connect directly to Assignment 9 Iteration 1.
- Students should begin from their existing project, not invent a new feature.
- Clarify that one well-organized file fully meets the conceptual target.

**Transition cue:**

- "The submission must show both working behavior and understandable structure."

### Slide 19 - Evidence Expectations

Student-visible text:

```text
Evidence this week:

- the application still works
- function names describe real jobs
- responsibilities are separated intentionally
- event handlers remain focused
- repeated logic is reduced where reasonable
- your reflection explains what became clearer

More functions alone do not prove modularity.
```

**Instructor notes:**

- Tie evidence to structure, interactivity, debugging, and communication.
- Encourage screenshots or code references only when required by the current
  submission workflow.

**Transition cue:**

- "The goal is a program that a future version of you can still understand."

### Slide 20 - Closing

Student-visible text:

```text
Modular thinking begins with responsibility.

Ask:

- What jobs exist?
- Which jobs belong together?
- What name explains each job?
- Did the behavior stay correct?

Clear parts make growing systems manageable.
```

**Instructor notes:**

- Close on the design habit rather than file count.
- Preview that Wednesday uses the same responsibility map to make a deliberate
  multi-file version.

**Transition cue:**

- "Wednesday, we keep the same behavior and give selected responsibilities their own files."

---

# AI Use Notes

Week 9 begins the AI Assistant phase. Students must manually write or revise
the relevant code before requesting help. AI may suggest responsibility groups,
function boundaries, or clearer names. Students must choose, implement, test,
and explain any accepted suggestion.

---

# Image Prompt Notes

Use the Week 9 prompt packet for the following:

| Slide | Image Concept                                  | Prompt Packet Note              |
| ----- | ---------------------------------------------- | ------------------------------- |
| 1     | larger system broken into understandable parts | Include in Week 9 prompt packet |
| 2     | async feature adding another responsibility    | Include in Week 9 prompt packet |
| 3     | timing questions to organization questions     | Include in Week 9 prompt packet |
| 4     | modularity versus module                       | Include in Week 9 prompt packet |
| 6     | today's modularity toolbox                     | Include in Week 9 prompt packet |
| 7     | parked professional tooling                    | Include in Week 9 prompt packet |
| 8     | quiet growth of mixed responsibilities         | Include in Week 9 prompt packet |
| 9     | separation of concerns                         | Include in Week 9 prompt packet |
| 10    | responsibilities before files                  | Include in Week 9 prompt packet |
| 11    | functions as named jobs                        | Include in Week 9 prompt packet |
| 12    | coordinator connecting parts                   | Include in Week 9 prompt packet |
| 13    | small-step refactoring loop                    | Include in Week 9 prompt packet |
| 14    | one-file responsibilities demo                 | Include in Week 9 prompt packet |
| 15    | responsibility map                             | Include in Week 9 prompt packet |
| 16    | AI as manual-first assistant                   | Include in Week 9 prompt packet |
| 17    | useful AI prompt pattern                       | Include in Week 9 prompt packet |
| 20    | modular thinking summary                       | Include in Week 9 prompt packet |

No separate image prompt is needed for Slide 5 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- prior lab review: 8-10 minutes
- modularity versus modules and scope framing: 8-12 minutes
- responsibilities, functions, and coordination: 15-20 minutes
- live refactoring demo and inspection: 15-20 minutes
- AI Assistant role and prompt pattern: 6-8 minutes
- lab bridge and evidence: 5-8 minutes
