# W07B Function Refactor Iteration Recorded

**10-152-118 Web Development Foundations**  
**Week 7 Wednesday Recorded Lecture**  
**Topic:** Structured Behavior - Refactoring Working Code

---

# Session Purpose

Wednesday deepens Monday's structured-behavior lesson by performing the actual
refactor. The recording should feel like an iteration from Monday's working
but messy code into clearer named functions.

Students should see that refactoring is controlled change:

- record expected behavior
- extract one responsibility at a time
- reconnect the event listener
- retest the same values
- explain why the code is clearer

---

# IIM Alignment

Week 7 Wednesday:

- arrow functions
- clean vs messy code comparison

Thursday lab:

- add structured interactivity to project

AI role:

- AI as Explainer
- AI may help explain the difference between function styles or function names
- AI should not replace the student's own refactor or explanation

---

# Reading Alignment

Assigned reading:

- **Required - JS/JQ:** Chap 3 - Functions, Methods & Objects: selected pages
  on functions, scope, dot notation, and the document object as a
  built-in/global object: pp 85-103, 120-130
- **Reference - JS/JQ:** selected pages on objects and built-in methods:
  pp 104-119, 131-144

Reading-to-lab bridge:

- Functions are the main required reading target.
- Scope and dot notation support understanding, not memorization.
- Objects and built-in methods are reference material.

---

# Demo Set

Demo folder:

```text
Demos/Week_07_Structured_JavaScript/02_wednesday_refactored_code/
```

Demo role:

- start from Monday's messy working version
- extract `getMinutesAvailable()`
- extract `chooseStudyPlan(minutes)`
- extract `showPlan()`
- reconnect `addEventListener("click", showPlan)`
- retest the same behavior

---

# Slide Sequence Overview

1. Reconnect To Monday
2. The Same Feature, Clearer Code
3. What Counts As Success Today
4. Refactor In Small Steps
5. Today's Toolbox
6. Before You Change Structure, Record Behavior
7. Extract One Responsibility
8. Return Values Carry Results Back
9. Demo: Refactor Into Named Functions
10. Named Function Callback
11. Arrow Functions Are Alternate Syntax
12. Clean Versus Messy Comparison
13. AI Can Explain Choices, Not Decide For You
14. Useful AI Prompt Pattern
15. Thursday Lab Refinement
16. Evidence And Submission
17. How To Read Next Week's Material
18. Closing

---

# Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- working code can still be hard to read
- long event handlers hide responsibilities
- functions name responsibilities
- refactoring must preserve behavior

Today:
we perform the refactor one step at a time.
```

**Instructor notes:**

- Make the continuity explicit.
- This is not a new feature; it is a controlled iteration.

**Transition cue:**

- "The browser result should stay familiar while the code becomes clearer."

Visual notes:

- Monday messy handler moving into a cleaner Wednesday structure.

### Slide 2 - The Same Feature, Clearer Code

Student-visible text:

```text
The feature:
enter minutes and receive a study plan.

The improvement:
separate the jobs.

Before:
one event handler does everything.

After:
named functions each do one clear job.
```

**Instructor notes:**

- Run the page or show the feature before code.
- Emphasize that behavior is preserved.

**Transition cue:**

- "Today's success depends on structure and verification."

Visual notes:

- Same page output with before/after code organization behind it.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you identify one responsibility
- you extract it into a function
- you reconnect the behavior
- you retest the same input values
- you can explain why the structure is clearer
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- This should feel manageable, not like a rewrite.

**Transition cue:**

- "Small steps protect working behavior."

### Slide 4 - Refactor In Small Steps

Student-visible text:

```text
Do not refactor everything at once.

Use this rhythm:

1. choose one responsibility
2. move that code into a function
3. reconnect the call
4. retest
5. then choose the next responsibility
```

**Instructor notes:**

- Echo Week 6's one-fix-at-a-time habit.
- The debugging process becomes a refactoring process.

**Transition cue:**

- "Here are the tools for that controlled change."

Visual notes:

- One responsibility extracted at a time.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- expected behavior
- named function
- return value
- parameter
- event listener
- callback
- arrow function awareness
- retest
```

**Instructor notes:**

- Arrow functions are awareness, not mastery.
- Keep named functions as the main beginner path.

**Transition cue:**

- "Before changing code, we need to know what behavior must stay the same."

Visual notes:

- Refactoring toolbox.

### Slide 6 - Before You Change Structure, Record Behavior

Student-visible text:

```text
Before refactoring, record expected behavior.

Example test values:
- 0 minutes
- 10 minutes
- 30 minutes
- 60 minutes

After refactoring, run the same checks.
```

**Instructor notes:**

- This is the refactoring version of evidence.
- It prevents accidental behavior changes.

**Transition cue:**

- "Now we can safely extract one responsibility."

Visual notes:

- Before/after test checklist.

### Slide 7 - Extract One Responsibility

Student-visible text:

```text
Look for one job:

- read input
- validate input
- choose a plan
- update the page
- handle the click

Each function should have a name that says its job.
```

**Instructor notes:**

- Encourage responsibility language.
- Avoid every-line-as-function thinking.

**Transition cue:**

- "Some functions do work and return a result."

Visual notes:

- Responsibilities becoming function names.

### Slide 8 - Return Values Carry Results Back

Student-visible text:

```text
A return value sends a result back.

Example:
`chooseStudyPlan(minutes)`
returns the message to show.

Then another function can use that result.

Returning a value keeps jobs separate.
```

**Instructor notes:**

- Keep this concrete with the demo function.
- Distinguish deciding the plan from updating the page.

**Transition cue:**

- "Now we will refactor the demo using those responsibilities."

Visual notes:

- Function returning a message to another step.

### Slide 9 - Demo: Refactor Into Named Functions

Student-visible text:

```text
Demo: Refactor Into Named Functions

Watch for:
- record expected behavior
- extract `getMinutesAvailable()`
- extract `chooseStudyPlan(minutes)`
- extract `showPlan()`
- reconnect the click listener
- retest the same values
```

**Instructor notes:**

- Start from the Monday version.
- Type the function extraction live or reveal in controlled steps.
- Do not turn this into a speed-coding performance.

**Transition cue:**

- "The event listener becomes easier to read when it names the callback."

Demo connection:

- `Demos/Week_07_Structured_JavaScript/02_wednesday_refactored_code/`

### Slide 10 - Named Function Callback

Student-visible text:

```text
Before:
`button.addEventListener("click", function () { ... });`

After:
`button.addEventListener("click", showPlan);`

The named function makes the event's purpose visible.
```

**Instructor notes:**

- This is the callback concept in practical form.
- Keep the focus on readability.

**Transition cue:**

- "There is another function syntax students will see in examples."

Visual notes:

- Anonymous function contrasted with named callback.

### Slide 11 - Arrow Functions Are Alternate Syntax

Student-visible text:

```text
Arrow functions are another way to write functions.

Traditional:
`function showPlan() { ... }`

Arrow style:
`const showPlan = () => { ... };`

For this course:
recognize arrow functions.
Use clear names first.
```

**Instructor notes:**

- The IIM calls for arrow functions, but this should be awareness-level.
- Avoid converting the whole course style to arrow functions.

**Transition cue:**

- "Syntax matters less than whether the code is easier to understand."

Visual notes:

- Two equivalent-looking function style cards.

### Slide 12 - Clean Versus Messy Comparison

Student-visible text:

```text
Messy code hides:
- purpose
- responsibilities
- testing points

Cleaner code reveals:
- what each function does
- where values come from
- where the page updates
- what to retest
```

**Instructor notes:**

- Compare the Monday and Wednesday scripts side by side.
- Ask what became easier to explain.

**Transition cue:**

- "AI can help explain these differences, but the student still owns the choice."

Visual notes:

- Messy handler beside clean named functions.

### Slide 13 - AI Can Explain Choices, Not Decide For You

Student-visible text:

```text
AI as Explainer:

Useful for:

- comparing two function names
- explaining a return value
- explaining why a callback works
- identifying what a function is responsible for

You still choose, test, and explain.
```

**Instructor notes:**

- Reinforce Week 6-8 role: Explainer.
- Avoid moving into Week 9-12 Assistant language too early.
- Students should not ask AI to rewrite the assignment.

**Transition cue:**

- "A useful AI prompt needs context, limits, and a learning goal."

Visual notes:

- Student code with AI explanation notes, not replacement code.

### Slide 14 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I manually refactored this JavaScript into functions.
Do not rewrite it for me.
Explain what each function is responsible for,
where the callback happens,
and one name that could be clearer.
Ask me a question before suggesting code."
```

**Instructor notes:**

- This is prompt engineering by example, not a separate prompt-engineering unit.
- Emphasize manually refactored, do not rewrite, explain, ask first.
- Students need a pattern because vague prompts invite vague or replacement
  answers.

**Transition cue:**

- "Now the Thursday lab uses that same boundary: improve your own structure."

Visual notes:

- Form-like prompt card with labeled parts: context, constraint, explanation
  request, question-first behavior.

### Slide 15 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab: refine structure

Your goal:
- improve function names
- organize logic clearly
- reduce repetition where possible
- keep the feature working
- add one clarity improvement
```

**Instructor notes:**

- Now name the full weekly endpoint.
- Tie to Assignment 7 Iteration 2.

**Transition cue:**

- "The final submission should show both working behavior and readable structure."

Lab connection:

- Assignment 7 - Iteration 2

### Slide 16 - Evidence And Submission

Student-visible text:

```text
Final Assignment 7 evidence:

- updated HTML, CSS, and JS
- JavaScript uses functions effectively
- function names are meaningful
- behavior still works
- short reflection explains what changed
```

**Instructor notes:**

- Mention that code must run without errors.
- The reflection is not optional.

**Transition cue:**

- "Next week, behavior gets a new challenge: time."

### Slide 17 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- read the async handout for the big idea
- focus on what happens now vs what happens later

Skim:
- Ajax and JSON as background
- JSON structure guide for objects and arrays

Reference:
- MDN links are there when you need exact syntax
```

**Instructor notes:**

- Week 8 uses course-authored async handout as the required anchor.
- Do not let students believe they must master Promises before lecture.

**Transition cue:**

- "You can now structure behavior. Next, we explore how behavior happens over time."

### Slide 18 - Closing

Student-visible text:

```text
This week:

- working code became clearer
- responsibilities became functions
- callbacks became easier to read
- behavior stayed verified

Next:
systems respond over time.
```

**Instructor notes:**

- Close the unit transition.
- Prepare students for async without teaching it early.

**Transition cue:**

- "Clear structure makes next week's timing problems easier to follow."

---

# Demo Execution Notes

- Use `Demos/Week_07_Structured_JavaScript/02_wednesday_refactored_code/`.
- Start from Monday's messy working version.
- Test the original values before refactoring.
- Extract `getMinutesAvailable()`.
- Extract `chooseStudyPlan(minutes)`.
- Extract `showPlan()`.
- Reconnect `planButton.addEventListener("click", showPlan);`.
- Retest the same values after each meaningful step.

---

# Lab / Assignment Bridge

Students should use Thursday to finish Assignment 7:

- refine function names
- improve readability
- keep behavior working
- add at least one clarity improvement
- complete the short reflection

---

# Evidence / Submission Expectations

Assignment 7 final evidence should show:

- working page behavior
- JavaScript organized into functions
- meaningful names
- reduced repeated logic where appropriate
- reflection explaining how restructuring changed understanding

---

# AI-Use Boundary

AI may explain function responsibilities, return values, callbacks, or naming
tradeoffs. Students still need to make their own structure choices, test the
behavior, and explain what changed.

---

# Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | Monday to Wednesday refactor | Include in Week 7 prompt packet |
| 2 | same feature clearer code | Include in Week 7 prompt packet |
| 3 | success today | Use SmartArt; no image prompt by default |
| 4 | small-step refactor | Include in Week 7 prompt packet |
| 5 | toolbox | Include in Week 7 prompt packet |
| 6 | record behavior first | Include in Week 7 prompt packet |
| 7 | extract responsibility | Include in Week 7 prompt packet |
| 8 | return value | Include in Week 7 prompt packet |
| 9 | demo refactor | Include in Week 7 prompt packet |
| 10 | named callback | Include in Week 7 prompt packet |
| 11 | arrow function awareness | Include in Week 7 prompt packet |
| 12 | clean vs messy comparison | Include in Week 7 prompt packet |
| 13 | AI explains choices | Include in Week 7 prompt packet |
| 14 | useful AI prompt pattern | Include in Week 7 prompt packet |
| 18 | structure to async bridge | Include in Week 7 prompt packet |

---

# Instructor Timing Notes

- Reconnect and framing: 5-7 minutes
- Small-step refactor setup: 8-10 minutes
- Demo: 18-25 minutes
- Callback/arrow/comparison discussion: 12-15 minutes
- AI-as-explainer boundary and prompt pattern: 4-6 minutes
- Lab bridge, reading guidance, and close: 6-8 minutes

If recording time is tight, skim the arrow-function comparison or verbally
bridge the AI boundary. Do not skip behavior recording, refactor demo, retest,
or final evidence expectations.

---

# Post-Lecture Notes

- Note whether students preserve behavior while refactoring.
- Note whether function names become clearer or just shorter.
- Use Week 8 to connect structured functions to async timing examples.
