# Week 7 Image Generation Prompts

**10-152-118 Web Development Foundations**

---

# Purpose

This companion artifact expands the image notes from the Week 7 deck sources
into explicit image-generation prompts for browser-based ChatGPT image
generation.

Primary workflow:

- Copy one prompt block at a time into the browser-based ChatGPT image tool.
- Use Codex image generation only as a fallback if the browser image result is
  significantly unusable.
- Do not generate images for `What Counts As Success Today`; use the standard
  course SmartArt / built-in graphic pattern for that slide.
- Preserve slide numbering as placement guidance for the final PowerPoint
  sequence.
- Week 7 visuals should communicate calm refactoring, readability, named
  responsibilities, and behavior preservation.

Global style guidance:

- clean instructional PowerPoint visual
- white or very light background
- modern, flat, classroom-friendly style
- large readable labels
- minimal decorative detail
- restrained SWTC-friendly colors: navy, teal, warm gold, white, soft gray
- no dense code walls
- no dark terminal imagery
- no framework or React imagery
- no magical AI replacement imagery

Source decks:

- `W07A_Structured_Behavior_Live.md`
- `W07B_Function_Refactor_Iteration_Recorded.md`

---

# Week 7 Monday Live Prompts

## W07A Slide 1 - Working To Clear Code

```text
Create a clean instructional PowerPoint visual showing working code becoming clearer without changing the browser result.

Use a white or very light background. Show the same simple web page output on both sides. Behind the first page, show a tangled single code block labeled "works but hard to read." Behind the second page, show three small labeled function cards:

- read input
- choose plan
- update page

Add a small note:
"Same behavior. Clearer structure."

Use restrained navy, teal, warm gold, white, and soft gray.

Avoid dense code, dark terminal imagery, framework logos, or overly technical architecture diagrams.
```

## W07A Slide 2 - Week 6 Success Path

```text
Create a clean instructional PowerPoint visual connecting debugging evidence to clearer code.

Use a white or very light background. Show a simple flow:

debugging report -> verified fix -> working feature -> code ready to improve

Add small labels:

- issue
- evidence
- fix
- verification
- next: readability

Add a small note:
"Last week: make it work. This week: make it clear."

Use a calm classroom-friendly style.

Avoid alarm/error imagery, dark terminal screens, or dense reports.
```

## W07A Slide 3 - Debugging To Refactoring

```text
Create a clean instructional PowerPoint visual contrasting debugging and refactoring.

Use a white or very light background. Show two labeled question cards:

Debugging:
Why did this fail?

Refactoring:
How can this be clearer while still working?

Between them, show a simple bridge labeled "preserve behavior."

Add a small note:
"Change structure. Preserve behavior."

Use large readable labels and restrained SWTC-friendly colors.

Avoid broken-code panic imagery, complex diagrams, or decorative clutter.
```

## W07A Slide 5 - Structured JavaScript Toolbox

```text
Create a clean instructional PowerPoint visual showing today's structured JavaScript toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with labeled tools:

- working behavior
- function
- responsibility
- event handler
- callback
- scope
- meaningful name
- retest

Make the tools approachable and clearly labeled.

Use restrained navy, teal, warm gold, white, and soft gray.

Avoid advanced architecture tools, modules, classes, frameworks, or dense code.
```

## W07A Slide 6 - Parked For Later Structure Topics

```text
Create a clean instructional PowerPoint visual showing advanced JavaScript structure topics parked for later.

Use a white or very light background. Show a simple shelf or parking area with labeled items:

- modules
- classes
- complex objects
- advanced scope
- build tools
- framework patterns

In the foreground, show today's focus:
"Clear named functions in one JavaScript file."

Use a calm classroom-friendly style.

Avoid making the parked topics look scary or overly technical.
```

## W07A Slide 7 - Working But Hard To Read

```text
Create a clean instructional PowerPoint visual showing code that works but is hard to read.

Use a white or very light background. Show a simple event handler represented as one long tangled block. Add callouts:

- mixed decisions
- repeated text
- hidden responsibilities
- hard to read aloud

Beside it, show the browser output working correctly.

Add a small note:
"The browser may be happy. The next reader may not be."

Avoid dense real code, red error imagery, or shame/failure symbolism.
```

## W07A Slide 8 - Function As Named Responsibility

```text
Create a clean instructional PowerPoint visual showing a responsibility becoming a named function.

Use a white or very light background. Show a responsibility card labeled "choose the study plan" transforming into a function card labeled:

chooseStudyPlan(minutes)

Add three small question labels:

- What job?
- What input?
- What result?

Add a small note:
"Good names make code easier to read."

Use large readable labels and a modern flat style.

Avoid complicated syntax, dense code, or advanced design-pattern imagery.
```

## W07A Slide 9 - Callback Used Later

```text
Create a clean instructional PowerPoint visual explaining a callback as a function used later.

Use a white or very light background. Show a button labeled "Plan" with an arrow to a waiting function card labeled "showPlan." Add a small clock or "later" label near the click event.

Include this simple line:
addEventListener("click", showPlan)

Add a small note:
"The click happens later. The function runs then."

Use a calm classroom-friendly style with large readable labels.

Avoid async complexity, promises, timers, or dense event diagrams.
```

## W07A Slide 10 - Scope Basics

```text
Create a clean instructional PowerPoint visual showing beginner scope.

Use a white or very light background. Show two areas:

Shared page elements:
- minutesInput
- planButton
- message

Inside a function:
- minutes
- plan

Add a small note:
"Scope asks: where can this name be used?"

Use simple boxes or zones with large readable labels.

Avoid advanced scope-chain diagrams, closures, nested bubbles, or dense code.
```

## W07A Slide 11 - AI As Structure Explainer

```text
Create a clean instructional PowerPoint visual showing AI as an explainer for code structure.

Use a white or very light background. Show student-owned code on one side and an explanation note on the other. The explanation note should include:

- what this function does
- why this name is clearer
- possible responsibilities to look for

Add a clear boundary label:
"Explain structure. Do not replace the refactor."

Use restrained navy, teal, warm gold, white, and soft gray.

Avoid robot characters, magic imagery, full-code replacement visuals, or anything that suggests AI is doing the assignment.
```

## W07A Slide 12 - Useful AI Prompt Pattern

```text
Create a clean instructional PowerPoint visual showing a useful AI prompt pattern for asking AI to explain JavaScript structure before a refactor.

Use a white or very light background. Make the visual look like a polished worksheet or form card, not a chatbot screenshot. Show four labeled sections:

- Context: I manually wrote this JavaScript.
- Constraint: Do not rewrite it for me.
- Explain: responsibilities mixed together.
- Ask First: ask me one question before suggesting code.

Add a small footer reminder:
"Prompt for explanation, not replacement."

Use restrained navy, teal, warm gold, white, and soft gray. Keep labels large and readable.

Avoid robot characters, full-code generation visuals, magic imagery, dense code, or anything suggesting AI completes the assignment.
```

## W07A Slide 13 - Demo Messy Working Code

```text
Create a clean instructional PowerPoint visual for a live demo named "Messy Working Code."

Use a white or very light background. Show a simple study-planner page that works, plus a single long event-handler block behind it. Add callouts:

- feature works
- handler is long
- decisions mixed with output
- ready for refactor

Add a small note:
"Working is the starting point."

Avoid broken-code imagery, dense readable code, or advanced tooling.
```

## W07A Slide 14 - Responsibilities To Functions

```text
Create a clean instructional PowerPoint visual showing hidden responsibilities becoming function names.

Use a white or very light background. Show four responsibility cards:

- read minutes input
- choose study plan
- update message
- respond to click

Then show three function cards:

- getMinutesAvailable()
- chooseStudyPlan(minutes)
- showPlan()

Add a small note:
"Name the job before moving the code."

Use a classroom-friendly flat style.

Avoid dense code blocks, complex architecture diagrams, or framework imagery.
```

---

# Week 7 Wednesday Recorded Prompts

## W07B Slide 1 - Monday To Wednesday Refactor

```text
Create a clean instructional PowerPoint visual showing Monday's messy working code becoming Wednesday's refactored code.

Use a white or very light background. Show a progression:

working feature -> identify responsibilities -> extract functions -> retest

Add a small note:
"Same feature. Clearer code."

Use large readable labels and restrained SWTC-friendly colors.

Avoid dense source code, terminal imagery, or complex refactoring diagrams.
```

## W07B Slide 2 - Same Feature Clearer Code

```text
Create a clean instructional PowerPoint visual showing the same web feature with clearer code behind it.

Use a white or very light background. Show one simple study-planner page in the center. On the left, show "Before: one handler does everything." On the right, show "After: named functions do clear jobs."

Function cards:

- getMinutesAvailable()
- chooseStudyPlan(minutes)
- showPlan()

Add a small note:
"The page behavior stays familiar."

Avoid dense code walls or framework visuals.
```

## W07B Slide 4 - Small-Step Refactor

```text
Create a clean instructional PowerPoint visual showing a small-step refactoring rhythm.

Use a white or very light background. Show five ordered steps:

1. choose one responsibility
2. move it into a function
3. reconnect the call
4. retest
5. choose the next responsibility

Add a small note:
"Do not refactor everything at once."

Use a calm classroom-friendly style with large readable labels.

Avoid chaotic code imagery or advanced refactoring tool screenshots.
```

## W07B Slide 5 - Refactoring Toolbox

```text
Create a clean instructional PowerPoint visual showing today's refactoring toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with labeled tools:

- expected behavior
- named function
- return value
- parameter
- event listener
- callback
- arrow function awareness
- retest

Use restrained navy, teal, warm gold, white, and soft gray.

Avoid classes, modules, frameworks, build tools, or dense code.
```

## W07B Slide 6 - Record Behavior First

```text
Create a clean instructional PowerPoint visual showing behavior recorded before refactoring.

Use a white or very light background. Show a before/after testing checklist:

Before refactor:
- 0 minutes
- 10 minutes
- 30 minutes
- 60 minutes

After refactor:
- same checks
- same expected behavior

Add a small note:
"Retest the same values."

Use large readable labels and a calm classroom-friendly style.

Avoid test-framework dashboards, dense tables, or alarm imagery.
```

## W07B Slide 7 - Extract Responsibility

```text
Create a clean instructional PowerPoint visual showing one responsibility extracted from a long handler.

Use a white or very light background. Show a long handler block with one highlighted responsibility labeled "choose a plan." Move that responsibility into a function card labeled:

chooseStudyPlan(minutes)

Add a small note:
"Extract one job at a time."

Use large readable labels and restrained colors.

Avoid dense code, complex diagrams, or advanced design patterns.
```

## W07B Slide 8 - Return Value

```text
Create a clean instructional PowerPoint visual showing a return value carrying a result back.

Use a white or very light background. Show:

chooseStudyPlan(minutes)
-> returns message
-> showPlan uses message
-> page updates

Add a small note:
"Returning a value keeps jobs separate."

Use simple arrows and large labels.

Avoid mathematical function graphs, complex code, or advanced programming notation.
```

## W07B Slide 9 - Demo Refactor

```text
Create a clean instructional PowerPoint visual for a recorded demo named "Refactor Into Named Functions."

Use a white or very light background. Show an ordered refactor path:

1. record expected behavior
2. extract getMinutesAvailable()
3. extract chooseStudyPlan(minutes)
4. extract showPlan()
5. reconnect click listener
6. retest

Add a small note:
"Structure changes. Behavior stays verified."

Use a classroom-friendly flat style.

Avoid dense source code, terminal imagery, or complex tooling.
```

## W07B Slide 10 - Named Function Callback

```text
Create a clean instructional PowerPoint visual contrasting an anonymous callback and a named callback.

Use a white or very light background. Show two cards:

Before:
addEventListener("click", function () { ... })

After:
addEventListener("click", showPlan)

Add a small note:
"The named function makes the event's purpose visible."

Use large readable labels and restrained SWTC-friendly colors.

Avoid dense code, async diagrams, or framework visuals.
```

## W07B Slide 11 - Arrow Function Awareness

```text
Create a clean instructional PowerPoint visual showing traditional function syntax and arrow function syntax as two styles students may see.

Use a white or very light background. Show two equivalent style cards:

Traditional:
function showPlan() { ... }

Arrow style:
const showPlan = () => { ... };

Add a small note:
"Recognize arrow functions. Use clear names first."

Use large readable labels and a calm classroom-friendly style.

Avoid implying arrow functions are required, superior, or a new mastery target.
```

## W07B Slide 12 - Why Arrow Functions Became Common

```text
Create a clean instructional PowerPoint visual explaining why arrow functions became common in modern JavaScript.

Use a white or very light background. Create a balanced three-column layout:

- Advantages
- Disadvantages
- Recommendation

Under Advantages, show simple icons for shorter syntax, common examples, callbacks, and advanced this behavior. Under Disadvantages, show readability caution, not always ideal, and avoid clever one-liners. Under Recommendation, show a highlighted card:
"Use for small callbacks. Keep names and readability first."

Use restrained navy, teal, warm gold, white, and soft gray. Keep labels large and readable.

Avoid dense code, implying arrow functions are always superior, advanced lexical-this diagrams, or framework imagery.
```

## W07B Slide 13 - Clean Versus Messy Comparison

```text
Create a clean instructional PowerPoint visual comparing messy code and cleaner code.

Use a white or very light background. On the left, show a tangled block labeled "Messy: purpose hidden." On the right, show three clean function cards:

- getMinutesAvailable()
- chooseStudyPlan(minutes)
- showPlan()

Add labels:

- responsibilities visible
- testing points clearer
- page update easier to find

Add a small note:
"Cleaner code is easier to explain."

Avoid dense code walls, shame imagery, or complicated architecture.
```

## W07B Slide 14 - AI Explains Choices

```text
Create a clean instructional PowerPoint visual showing AI explaining code-structure choices without replacing student work.

Use a white or very light background. Show a student code excerpt card and an AI explanation card. The AI explanation card should say:

- explains each function's responsibility
- compares two function names
- explains a return value

Add a boundary label:
"You still choose, test, and explain."

Use restrained navy, teal, warm gold, white, and soft gray.

Avoid robot characters, full-code generation visuals, magic imagery, or chatbot screenshot styling.
```

## W07B Slide 15 - Useful AI Prompt Pattern

```text
Create a clean instructional PowerPoint visual showing a useful AI prompt pattern for explaining a JavaScript refactor.

Use a white or very light background. Make the visual look like a polished worksheet or form card, not a chatbot screenshot. Show four labeled sections:

- Context: I manually refactored this JavaScript into functions.
- Constraint: Do not rewrite it for me.
- Explain: responsibilities, callback, and naming.
- Ask First: ask me a question before suggesting code.

Add a small footer reminder:
"Prompt for explanation, not replacement."

Use restrained navy, teal, warm gold, white, and soft gray. Keep labels large and readable.

Avoid robot characters, full-code generation visuals, magic imagery, dense code, or anything suggesting AI completes the assignment.
```

## W07B Slide 19 - Structure To Async Bridge

```text
Create a clean instructional PowerPoint visual showing clear structure preparing students for async timing next week.

Use a white or very light background. Show a progression:

clear functions -> verified behavior -> timing question -> async next

Add a small note:
"Clear structure makes timing easier to follow."

Use large readable labels and a modern flat classroom-friendly style.

Avoid promises/fetch syntax, dense async diagrams, or advanced API imagery.
```

---

# Suggested Filename Map

Use these filenames when saving generated images:

| Deck | Slide | Suggested filename |
|---|---:|---|
| W07A | 1 | `w07_img_01_working_to_clear_code.png` |
| W07A | 2 | `w07_img_02_week6_success_path.png` |
| W07A | 3 | `w07_img_03_debugging_to_refactoring.png` |
| W07A | 5 | `w07_img_04_structured_js_toolbox.png` |
| W07A | 6 | `w07_img_05_parked_structure_topics.png` |
| W07A | 7 | `w07_img_06_working_but_hard_to_read.png` |
| W07A | 8 | `w07_img_07_named_responsibility.png` |
| W07A | 9 | `w07_img_08_callback_used_later.png` |
| W07A | 10 | `w07_img_09_scope_basics.png` |
| W07A | 11 | `w07_img_10_ai_structure_explainer.png` |
| W07A | 12 | `w07_img_11_monday_ai_prompt_pattern.png` |
| W07A | 13 | `w07_img_12_demo_messy_working_code.png` |
| W07A | 14 | `w07_img_13_responsibilities_to_functions.png` |
| W07B | 1 | `w07_img_14_monday_to_wednesday_refactor.png` |
| W07B | 2 | `w07_img_15_same_feature_clearer_code.png` |
| W07B | 4 | `w07_img_16_small_step_refactor.png` |
| W07B | 5 | `w07_img_17_refactoring_toolbox.png` |
| W07B | 6 | `w07_img_18_record_behavior_first.png` |
| W07B | 7 | `w07_img_19_extract_responsibility.png` |
| W07B | 8 | `w07_img_20_return_value.png` |
| W07B | 9 | `w07_img_21_demo_refactor_named_functions.png` |
| W07B | 10 | `w07_img_22_named_function_callback.png` |
| W07B | 11 | `w07_img_23_arrow_function_awareness.png` |
| W07B | 12 | `w07_img_24_arrow_function_tradeoffs.png` |
| W07B | 13 | `w07_img_25_clean_vs_messy_comparison.png` |
| W07B | 14 | `w07_img_26_ai_explains_choices.png` |
| W07B | 15 | `w07_img_27_useful_ai_prompt_pattern.png` |
| W07B | 19 | `w07_img_28_structure_to_async_bridge.png` |

---

# Alt Text Drafts

- `w07_img_01_working_to_clear_code.png`: Same browser result shown with tangled code on one side and named function cards on the other.
- `w07_img_02_week6_success_path.png`: Debugging report and verified fix leading to readable code improvement.
- `w07_img_03_debugging_to_refactoring.png`: Debugging question bridged to refactoring question with behavior preservation.
- `w07_img_04_structured_js_toolbox.png`: Toolbox with function, responsibility, event handler, callback, scope, name, and retest.
- `w07_img_05_parked_structure_topics.png`: Advanced structure topics parked while named functions remain in focus.
- `w07_img_06_working_but_hard_to_read.png`: Working browser output beside a long event handler with readability callouts.
- `w07_img_07_named_responsibility.png`: Responsibility card transformed into `chooseStudyPlan(minutes)`.
- `w07_img_08_callback_used_later.png`: Button click leading later to the named function `showPlan`.
- `w07_img_09_scope_basics.png`: Shared page elements separated from temporary values inside a function.
- `w07_img_10_ai_structure_explainer.png`: AI explanation notes beside student-owned code, with a boundary against replacement.
- `w07_img_11_monday_ai_prompt_pattern.png`: Prompt-pattern worksheet showing context, constraint, explanation request, and ask-first behavior before Tuesday lab.
- `w07_img_12_demo_messy_working_code.png`: Study planner feature working while a long event handler is marked ready for refactor.
- `w07_img_13_responsibilities_to_functions.png`: Responsibility cards mapped to `getMinutesAvailable`, `chooseStudyPlan`, and `showPlan`.
- `w07_img_14_monday_to_wednesday_refactor.png`: Progression from working feature to responsibilities to extracted functions and retest.
- `w07_img_15_same_feature_clearer_code.png`: Same study planner feature with before and after code organization.
- `w07_img_16_small_step_refactor.png`: Ordered refactor rhythm from choosing one responsibility through retesting.
- `w07_img_17_refactoring_toolbox.png`: Toolbox with expected behavior, named function, return value, parameter, event listener, callback, arrow awareness, and retest.
- `w07_img_18_record_behavior_first.png`: Before and after checklist using the same minute values.
- `w07_img_19_extract_responsibility.png`: One highlighted responsibility extracted into `chooseStudyPlan(minutes)`.
- `w07_img_20_return_value.png`: `chooseStudyPlan(minutes)` returning a message used by `showPlan`.
- `w07_img_21_demo_refactor_named_functions.png`: Ordered demo path for extracting named functions and retesting.
- `w07_img_22_named_function_callback.png`: Anonymous callback contrasted with named `showPlan` callback.
- `w07_img_23_arrow_function_awareness.png`: Traditional function syntax and arrow style shown as alternate styles.
- `w07_img_24_arrow_function_tradeoffs.png`: Advantages, disadvantages, and recommendation for beginner arrow-function use.
- `w07_img_25_clean_vs_messy_comparison.png`: Messy purpose-hidden code contrasted with named function cards.
- `w07_img_26_ai_explains_choices.png`: AI explains responsibilities and naming while the student still chooses, tests, and explains.
- `w07_img_27_useful_ai_prompt_pattern.png`: Prompt-pattern worksheet showing context, constraint, explanation request, and ask-first behavior.
- `w07_img_28_structure_to_async_bridge.png`: Clear functions and verified behavior leading to async timing next week.

---

# Generation Priority

If time is tight, generate these first:

1. `w07_img_01_working_to_clear_code.png`
2. `w07_img_04_structured_js_toolbox.png`
3. `w07_img_06_working_but_hard_to_read.png`
4. `w07_img_07_named_responsibility.png`
5. `w07_img_11_monday_ai_prompt_pattern.png`
6. `w07_img_12_demo_messy_working_code.png`
7. `w07_img_16_small_step_refactor.png`
8. `w07_img_21_demo_refactor_named_functions.png`
9. `w07_img_24_arrow_function_tradeoffs.png`
10. `w07_img_25_clean_vs_messy_comparison.png`
