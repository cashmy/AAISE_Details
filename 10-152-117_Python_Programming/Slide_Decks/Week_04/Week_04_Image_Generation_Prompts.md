# Week 4 Image Generation Prompts

**10-152-117 Python Programming**

---

# Purpose

This companion artifact expands the Week 4 v2 deck source image notes into
explicit image-generation prompts.

Use these prompts when PowerPoint Designer does not provide a useful visual or
when a slide needs a precise instructional diagram.

---

# Style Guidance For All Week 4 Images

Use a clean educational diagram style for beginner programming students.

Preferred visual qualities:

- light background
- readable labels
- calm instructional tone
- simple vector-style diagrams
- one main idea per image
- minimal code
- evidence-focused visuals
- no dense screenshots

Avoid:

- scary error screens
- red alarm-heavy designs
- complex debugger UI
- professional test dashboards
- pytest appearing as a required mastery target
- robot/AI imagery unless explicitly requested
- cluttered flowcharts

---

# Week 4 Day 1 - Debugging As Evidence Gathering

Source deck:

`SD_W04D01_Debugging_as_Evidence_Gathering_v2.md`

## Slide 1 - A Bug Is Information

Create a calm instructional visual showing a bug or error symbol transforming
into an evidence clue, such as a magnifying glass over a signal marker. Add
the phrase "bug -> information". Use a reassuring style.

Avoid panic imagery, warning sirens, or frightening red screens.

## Slide 3 - Symptoms Show Up, Sources Hide

Create a split visual. Left side: "symptom" with wrong output visible. Right
side: "source" with an earlier code step highlighted. Show that the visible
problem may start earlier in the program.

Avoid dense code or full stack traces.

## Slide 4 - What We Will Use Today

Create a toolbox visual with cards labeled expected vs actual, traceback clue,
labeled print, one-change repair, and evidence notes. Use calm colors and
readable text.

Avoid advanced debugger or profiling tools.

## Slide 5 - What We Will Skip For Now

Create a calm "parked for later" shelf with four labeled cards: full debugger workflows, logging architecture, pytest mastery, and profiling. Add a small bookmark or clock icon
to show these are useful later but not today's focus.

Avoid warning signs or making the deferred topics look wrong.

## Slide 6 - Expected Versus Actual

Create two large comparison cards. One card labeled "Expected" and one labeled
"Actual". Include a small difference marker between them and a caption:
"compare before changing code."

Avoid tiny text or spreadsheet-style detail.

## Slide 7 - Demo 1: Syntax Error Signal

Create a simplified Python error-message visual with three highlighted clues:
file name, line number, and error type. The error should look readable and
instructional, not alarming.

Avoid full terminal walls or dramatic red error styling.

## Slide 8 - Demo 2: Logic Bug Expected vs Actual

Create a simple discount-calculation visual showing expected 80 and actual 120.
Highlight a suspicious calculation step where a discount is added instead of
subtracted. Use a clear "investigate here" marker.

Avoid complex math layout.

## Slide 9 - Ask One Question, Print One Clue

Create a side-by-side visual. Left side: weak print debugging with
`print("here")`. Right side: stronger labeled output such as
`print("subtotal before tax:", subtotal)`. Label the right side "answers a
question."

Avoid shaming language.

## Slide 10 - Demo 3: Grade Summary Debugging

Create a trace visual for student grade records moving through checkpoints:
student, running total, added score, average. Highlight the first wrong average
or first suspicious value.

Avoid too many records or dense tables.

## Slide 11 - Demo 4: Order Total Debugging

Create a staged calculation visual with checkpoints: line total, subtotal,
discount, tax, final total. Highlight the stage where the wrong value is first
used.

Avoid receipt or shopping-cart realism unless very simple.

## Slide 13 - Common Failure: Changing Code First

Create an ordered process visual: observe, inspect one clue, change one thing,
run again. Use a calm checklist or step cards.

Avoid chaotic "random edits" imagery.

## Slide 16 - Debugging Notes Template

Create a large readable notes card with five labeled fields: Expected, Actual,
Evidence, Fix, Check after fix. Use a clean worksheet style.

Avoid tiny handwriting or clutter.

## Slide 17 - Evidence For A Debugging Submission

Create an evidence layout showing a corrected `.py` file, expected-vs-actual
card, labeled debug output, traceback clue, and short explanation note. Keep it
light and organized.

Avoid professional QA dashboard imagery.

---

# Week 4 Day 2 - Reading Procedural, Function-Based, And Class-Based Code

Source deck:

`SD_W04D02_Reading_Procedural_Function_and_Class_Code_v2.md`

## Slide 1 - Different Code Shapes Can Do The Same Job

Create three equal side-by-side panels labeled procedural, function-based, and
class-based. Each panel should show the same simple task, such as tracking
tasks, represented in a different shape. Keep all three visually equal.

Avoid ranking one style above the others.

## Slide 3 - Today's Success Pattern

Create a four-step reading path: read the structure, identify the parts,
explain in plain language, modify one small thing. Use arrows and simple cards.

Avoid complex process diagrams.

## Slide 4 - What We Will Use Today

Create a toolbox visual with cards labeled class, attribute, method,
`__init__`, `self`, object, and method call. Use readable text and a beginner
friendly style.

Avoid inheritance, polymorphism, or advanced OOP terms.

## Slide 5 - What We Will Skip For Now

Create a calm "parked for later" shelf with cards labeled inheritance,
polymorphism, decorators, and large class hierarchies. Add a caption: "Useful
later, not today's focus."

Avoid warning signs or making OOP look dangerous.

## Slide 6 - Procedural Code: Steps In Order

Create a simple ordered-step visual showing create list, add tasks, loop over
tasks, print output. Label it "procedural steps".

Avoid dense code.

## Slide 8 - Demo 2: Function-Based Task Tracker

Create two function cards labeled `add_task` and `show_tasks`. Show a task list
being passed into each function and output appearing from `show_tasks`.

Avoid full code walls.

## Slide 9 - A Class Stores Data And Actions Together

Create a container diagram labeled `TaskTracker`. Inside the container, show a
data section labeled `tasks` and an actions section labeled `add_task()` and
`show_tasks()`.

Avoid advanced class diagrams or UML notation.

## Slide 10 - `__init__` Sets The Starting State

Create a simple flow: create new tracker -> `__init__` setup -> empty task list
stored. Label `__init__` as "setup step".

Avoid deep constructor terminology.

## Slide 11 - Demo 3: Class-Based Task Tracker

Create a small annotated class visual with labels pointing to class name,
attribute, methods, object creation, and method call. Use minimal code-like
text and spacious labels.

Avoid full file screenshots.

## Slide 12 - What Does `self` Mean?

Create an object card labeled "this tracker" with an arrow to its own `tasks`
data. Add the phrase "`self` means this object" in readable text.

Avoid abstract theory or memory diagrams.

## Slide 14 - Common Failure: Prestige Bias

Create a balanced comparison between "advanced-looking" and "fits the problem".
Show that the fit-for-purpose option is selected because it is explainable and
modifiable.

Avoid mocking class-based code.

## Slide 16 - Structured Code Reading Checklist

Create a checklist visual with six items: class name, stored data, actions,
object creation, method calls, one change. Keep text large.

Avoid too much decorative detail.

## Slide 17 - Evidence For A7

Create an evidence layout showing a modified `.py` file, class explanation
note, attribute/method labels, and a small output sample. Keep it
student-friendly.

Avoid professional code-review dashboard imagery.

---

# Week 4 Day 3 - Validation, Testing, And Justifying A Fix

Source deck:

`SD_W04D03_Validation_Testing_and_Justifying_a_Fix_v2.md`

## Slide 1 - A Fix Is Stronger When It Is Checked

Create a simple progression: bug -> fix -> check. Use three large cards with
arrows. The check card should include a small evidence checkmark.

Avoid complex testing-tool imagery.

## Slide 2 - Evidence, Repair, Validation

Create an arc diagram (Week 4): evidence, repair, validation, explanation. Use
four connected cards and keep the final explanation card visible.

Avoid making validation look separate from debugging.

## Slide 3 - One Run Is Not Enough

Create a contrast visual. Left side: one successful run. Right side: several
small checked cases including normal, boundary, and alternate values. Make the
right side feel stronger.

Avoid formal coverage dashboards.

## Slide 4 - What We Will Use Today

Create a toolbox visual with expected/actual checks, simple test cases,
multiple values, optional assert, pytest recognition, and repair justification.
Make pytest a small card, not the dominant card.

Avoid making pytest look required.

## Slide 5 - What We Will Skip For Now

Create a "parked for later" shelf with cards labeled pytest mastery, mocking,
full test suites, profiling, and TDD workflow. Add a caption: "Useful later,
not today's required target."

Avoid warning visuals.

## Slide 6 - Expected Behavior Can Be Checked

Create a check card with fields: input, expected, actual, result. Use example
values such as input 69, expected False, actual False, result matches.

Keep text readable.

## Slide 7 - Demo 1: Simple Test Cases

Create three simple test cards checking one function. Use values 90, 70, and
69 with expected boolean results. Highlight that more than one value is being
checked.

Avoid dense code.

## Slide 8 - Boundaries Matter

Create a cutoff visual for passing score 70. Show 69 below the line and 70 on
the line. Label 70 as the boundary value.

Avoid math-heavy graphics.

## Slide 10 - Testing Tool Progression

Create a simple ladder: expected-vs-actual print checks, assert checks, pytest
recognition, future full test suites. Label the ladder "validation grows over
time."

Avoid implying all steps are required today.

## Slide 11 - Demo 2: Pytest Recognition

Create a small test-file card with one test function and a pass/fail output
indicator. Add a visible label: "recognition only unless assigned."

Avoid making pytest visually dominant or intimidating.

## Slide 13 - Explain Why The Fix Works

Create a five-step explanation chain: bug, evidence, change, check, result.
Use simple cards connected with arrows.

Avoid long paragraphs.

## Slide 15 - Finish A6: Debug And Explain

Create an Assignment #6 closeout visual with corrected file, debugging clue, check output,
and explanation note. Keep it clean and practical.

Avoid large report imagery.

## Slide 16 - Finish A7: Reading Structured Code

Create an Assignment #7 closeout visual with modified class file, class/attribute/method
labels, and an output sample proving the modification works.

Avoid full OOP diagrams.

## Slide 17 - Evidence For Week 4

Create an organized evidence board with corrected or modified files,
expected-vs-actual examples, debug output, simple checks, explanation note, and
optional AI-use note.

Avoid professional QA or project-management dashboard visuals.

---

# Revision Notes

Use this section after slide production to record which prompts worked well and
which need revision.

## Worked Well

-

## Needs Revision

-

## Reused Visual Style Notes

-
