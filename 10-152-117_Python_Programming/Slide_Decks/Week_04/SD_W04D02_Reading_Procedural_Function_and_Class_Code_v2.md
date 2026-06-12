# SLIDE DECK SOURCE - WEEK 4 DAY 2

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 4 / Tuesday |
| Date | September 8, 2026 |
| Weekly Theme | Debugging, Testing, and Reading Structured Code |
| Lecture Title | Reading Procedural, Function-Based, and Class-Based Code |
| Assignments Supported | Assignment 7 - Reading Structured Code |
| Readiness Target | Students can read and lightly modify a small class-based example |
| Primary Watch Point | Do not let this turn into full OOP theory; this is recognition and interpretation |
| Source Version | v2 refactor |

---

# Session Purpose

This session helps students read the same basic task written in different code
shapes.

Students do not need to master object-oriented design in this course. They do
need to recognize simple class-based code, especially because AI-generated
examples and professional documentation may use classes.

The target pattern is:

```text
read the structure -> identify the parts -> explain in plain language -> modify one small thing
```

---

# Review / Prior Work Bridge

Review from Monday:

- debugging begins with evidence
- expected versus actual helps locate problems
- labeled print-debugging can reveal the first useful signal
- A6 requires repair plus explanation

Quick review questions:

- What evidence did you use before changing code?
- What part of the code was easiest to read?
- What part was harder because of structure?
- How does organization affect debugging?

Bridge into Day 2:

Today students practice reading unfamiliar structure without freezing or
assuming that "more advanced-looking" means "better."

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 4
- textbook chapter area: **OOP, Decorators, and Iterators** for recognition

Day 2 reading focus:

- OOP overview
- the simplest Python class
- class and object namespaces
- the `self` argument
- initializing an instance

Use this reading to support:

- reading procedural code
- reading function-based code
- recognizing class-based structure
- making light modifications without deep OOP theory

Today's reading boundary:

Students should not worry yet about inheritance, composition, multiple
inheritance, polymorphism, operator overloading, decorators, or custom
iterators.

---

# What We Will Use Today

Today we will use:

- procedural code recognition
- function-based code recognition
- class-based code recognition
- class names
- attributes
- methods
- `__init__`
- `self`
- object creation
- one small modification

Today we will skip for now and revisit later:

- full OOP design
- inheritance
- polymorphism
- decorators
- advanced class patterns
- large class hierarchies

---

# Assignments Supported

Primary support:

- Assignment 7 - Reading Structured Code

A7 asks students to inspect a simple class-based example and compare it with a
procedural or function-based version of the same task.

Minimum assignment direction:

- identify the class
- identify attributes
- identify methods
- instantiate an object
- call a method
- make a small working modification
- explain the difference between organization styles

---

# Readiness Target

By the end of the session, students should be able to:

- identify procedural code
- identify function-based code
- identify a class definition
- describe what an object stores
- describe what a method does
- explain `__init__` as setup
- explain `self` as the current object at a beginner level
- make one small modification to a class-based example

---

# Primary Watch Point

The main risk is turning this into a full OOP lecture.

Keep the language plain:

```text
class -> a template for an object
attribute -> data the object stores
method -> action the object can do
__init__ -> setup step
self -> this object
```

The goal is recognition and interpretation, not design mastery.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/06_procedural_task_tracker.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/07_function_based_task_tracker.py`
- `Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/08_class_based_task_tracker.py`

Recommended use:

1. Show the procedural version first.
2. Show the function-based version as named responsibility.
3. Show the class-based version as data and actions grouped together.
4. Ask students to identify the class, attributes, methods, object, and calls.

---

# Student Hands-On Bridge

Students should begin A7 by reading before editing.

Suggested start:

```text
1. Identify the class name.
2. Identify what the object stores.
3. Identify what actions the object can do.
4. Find where the object is created.
5. Find where a method is called.
6. Make one small modification.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Normalize different code shapes |
| Today's Working Set | 4-5 | Core | Bound OOP to recognition and defer advanced theory |
| Three Code Shapes | 6-9 | Core / Demo | Compare procedural, function-based, and class-based versions |
| Class Recognition | 10-13 | Core / Demo | Teach class, object, attributes, methods, `__init__`, and `self` |
| Common Failures | 14 | Core | Prevent prestige bias toward class-based code |
| Assignment 7 Bridge | 15-17 | Lab Bridge / Evidence | Start A7 with identification, modification, and explanation |
| Closing Check | 18 | Assessment / Evidence | Define successful structured-code reading |

---

# Slide-by-Slide Source

## Slide 1 - Different Code Shapes Can Do The Same Job

**Delivery Category:** Review

**Student-Visible Text:**

The same task can be written in different shapes.

Today, compare:

- procedural code
- function-based code
- class-based code

The goal is not to decide that one shape is always best. The goal is to read
the structure and explain how it works.

**Instructor Notes:**

Reduce fear around unfamiliar structure. Students may see class-based code and
assume it is beyond them. Reframe it as a different organization shape.

**Transition Cue:**

You already know why structure matters from Week 3.

**Visual Notes:**

Use three side-by-side panels labeled procedural, function-based, class-based.

---

## Slide 2 - Build Structure, Then Read Structure

**Delivery Category:** Review

**Student-Visible Text:**

Week 3 focused on building structure.

Week 4 adds code literacy: reading structure someone else wrote.

Code reading matters because:

- examples may use unfamiliar organization
- AI may generate class-based code
- documentation may assume structure vocabulary
- debugging depends on knowing where to look

**Instructor Notes:**

Tie this to both AI realities and professional documentation. Students do not
need mastery, but they need enough literacy not to freeze.

**Transition Cue:**

The success pattern is read, identify, explain, and modify.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Read the structure -> identify the parts -> explain in plain language -> modify
one small thing.

For structured code, ask:

- What stores data?
- What performs actions?
- Where does the program start?
- What line changes behavior?

**Instructor Notes:**

This gives students an action path for A7. Keep "plain language" central.

**Transition Cue:**

Now name today's working set.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- procedural code
- functions
- classes
- attributes
- methods
- `__init__`
- `self`
- object creation

These are recognition tools for reading small structured examples.

**Instructor Notes:**

Do not let the list become an OOP vocabulary dump. Each term must attach to a
visible line in the demo.

**Transition Cue:**

Several OOP topics are intentionally out of scope.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip inheritance, polymorphism, decorators, and large class hierarchies
for now.

Today's goal is smaller:

- identify the class
- identify what it stores
- identify what it does
- make one small change

**Instructor Notes:**

This reduces anxiety. Students may skim textbook OOP sections and see far more
than today's assignment requires.

**Transition Cue:**

Start with the simplest shape: procedural code.

---

## Slide 6 - Procedural Code: Steps In Order

**Delivery Category:** Core

**Student-Visible Text:**

Procedural code is organized as steps in order.

It often reads like:

- create values
- change values
- loop or branch
- print output

This can be clear for small programs, but it may become harder to manage as the
program grows.

**Instructor Notes:**

Use this to connect to earlier weeks. Students have written mostly procedural
code already.

**Transition Cue:**

Watch a small procedural task tracker.

---

## Slide 7 - Demo 1: Procedural Task Tracker

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the code run as ordered steps.

Identify:

- where the list is created
- where tasks are added
- where tasks are displayed
- what would be repeated if the program grew

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/06_procedural_task_tracker.py`

Keep this as the baseline shape.

**Transition Cue:**

Functions name some of those steps.

**Demo Connection:**

Primary demo file: `06_procedural_task_tracker.py`

---

## Slide 8 - Demo 2: Function-Based Task Tracker

**Delivery Category:** Demo

**Student-Visible Text:**

Function-based code names responsibilities.

In the demo, identify:

- the function that adds a task
- the function that shows tasks
- where each function is called
- what data is passed in

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/07_function_based_task_tracker.py`

Connect back to Week 3 A4.

**Transition Cue:**

Classes group stored data and actions together.

**Demo Connection:**

Primary demo file: `07_function_based_task_tracker.py`

---

## Slide 9 - A Class Stores Data And Actions Together

**Delivery Category:** Core

**Student-Visible Text:**

A class can group data and actions that belong together.

Beginner wording:

- attribute: data the object stores
- method: action the object can do
- object: one usable instance of the class

This is organization, not magic.

**Instructor Notes:**

Keep vocabulary simple. Use "stores" and "does" more than abstract OOP
language.

**Transition Cue:**

The setup step is usually named `__init__`.

---

## Slide 10 - `__init__` Sets The Starting State

**Delivery Category:** Core

**Student-Visible Text:**

`__init__` is the setup step for a new object.

It often creates starting attributes.

Example idea:

```text
new tracker -> setup -> tracker has an empty task list
```

Say "setup step" before worrying about the word constructor.

**Instructor Notes:**

Demystify the double underscores. Students only need recognition and purpose.

**Transition Cue:**

Now watch the class-based task tracker.

---

## Slide 11 - Demo 3: Class-Based Task Tracker

**Delivery Category:** Demo

**Student-Visible Text:**

Watch what the object stores and what it does.

Identify:

- class name
- stored task list
- method that adds a task
- method that shows tasks
- object creation line
- method call lines

**Instructor Notes:**

Use:

`Demos/Week_04_Debugging_Testing_and_Reading_Structured_Code/08_class_based_task_tracker.py`

Do not teach inheritance or design theory. Keep it line-by-line and concrete.

**Transition Cue:**

`self` points to the current object.

**Demo Connection:**

Primary demo file: `08_class_based_task_tracker.py`

---

## Slide 12 - What Does `self` Mean?

**Delivery Category:** Core

**Student-Visible Text:**

At a beginner level, `self` means "this object."

`self.tasks` means this object has a `tasks` attribute.

When a method runs, it uses `self` to access the object's stored data.

Do not overthink it today. Recognize the pattern.

**Instructor Notes:**

Students may find `self` odd. Keep the explanation stable and short.

**Transition Cue:**

Now compare the three shapes by purpose, not prestige.

---

## Slide 13 - Same Task, Several Valid Shapes

**Delivery Category:** Core

**Student-Visible Text:**

Procedural, function-based, and class-based code can all solve the same small
task.

Compare by asking:

- Where is the data stored?
- Where are actions named?
- Which version is easiest to read?
- Which version is easiest to change?

**Instructor Notes:**

This prepares the comparison requirement in A7.

**Transition Cue:**

Do not assume class-based automatically means better.

---

## Slide 14 - Common Failure: Prestige Bias

**Delivery Category:** Core

**Student-Visible Text:**

Class-based code is not automatically better.

Choose or evaluate structure by fit:

- Does the structure match the problem?
- Can you explain it?
- Can you modify it safely?
- Is it small enough for this course target?

Advanced-looking code is not useful if you cannot understand it.

**Instructor Notes:**

This is especially important with AI-generated code. AI may return class-based
solutions that look polished but exceed the student's current explanation.

**Transition Cue:**

Now connect the reading process to Assignment 7.

---

## Slide 15 - Assignment 7 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 7, read and lightly modify a structured example.

Your work should show that you can:

- identify the class
- identify attributes
- identify methods
- create or use an object
- call a method
- make one small working change

**Instructor Notes:**

Keep the task modest. A7 is code literacy, not a full OOP build assignment.

**Transition Cue:**

Use a short reading checklist before editing.

**Lab Connection:**

Supports Assignment 7 - Reading Structured Code.

---

## Slide 16 - Structured Code Reading Checklist

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Before editing class-based code, answer:

- What is the class name?
- What does the object store?
- What actions can it do?
- Where is the object created?
- Where are methods called?
- What one change am I making?

**Instructor Notes:**

This reduces blank-page anxiety. It also keeps modifications intentional.

**Transition Cue:**

The explanation matters as much as the modification.

---

## Slide 17 - Evidence For A7

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Useful evidence includes:

- modified `.py` file
- short explanation of the class
- attributes identified
- methods identified
- one working modification
- comparison to procedural or function-based structure

Explain the code in your own words.

**Instructor Notes:**

If AI explanation support is permitted, students must verify the explanation
against the code and restate it.

**Transition Cue:**

Close by removing the mystery from class-based code.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can explain it plainly, it is no longer mysterious.

Before submitting A7, ask:

- What did the class store?
- What did its methods do?
- What did I modify?
- How is this different from the function-based version?

**Instructor Notes:**

Close on plain-language explanation. Thursday will connect debugging, testing,
and justification across A6 and A7.

**Transition Cue:**

Next session, we show validation evidence and justify fixes.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one debugging evidence question from Day 1.
2. Run `06_procedural_task_tracker.py`.
3. Run `07_function_based_task_tracker.py`.
4. Run `08_class_based_task_tracker.py`.
5. Compare where data is stored and where actions live.
6. Identify class, attributes, methods, object creation, and method calls.
7. Move students into A7 reading checklist and small modification.

Instructor pacing note:

If OOP vocabulary starts overwhelming students, return to "stores" and "does."

---

# Lab / Assignment Bridge

By the end of Day 2, students should have started A7 or have completed the
structured-code reading checklist.

Minimum A7 start target:

- class identified
- attributes identified
- methods identified
- modification target selected
- comparison note started

---

# README / Submission Expectations

Suggested student evidence:

- modified `.py` file
- short explanation or worksheet responses
- class/attribute/method identification
- plain-language comparison to another structure
- AI-use note if AI explanation support was permitted and used

---

# AI-Use Boundary

Bounded AI explanation support may be allowed.

Students may use AI to help explain unfamiliar structure only if they:

- verify the explanation against the code
- restate the explanation in their own words
- identify which lines support the explanation
- avoid submitting an explanation they cannot defend

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Three code shapes | Three panels: procedural, function-based, class-based | Do not rank them |
| 3 | Read-identify-explain-modify | Four-step reading path | Keep simple |
| 4 | Today's tools | Toolbox with class, attribute, method, init, self, object | Avoid advanced OOP |
| 5 | Deferred OOP topics | Parked shelf: inheritance, polymorphism, decorators | Reassuring tone |
| 6 | Procedural steps | Ordered step list with values and output | Keep beginner-level |
| 8 | Function-based task tracker | Two function cards: add task, show tasks | Avoid full code wall |
| 9 | Class stores data/actions | Container with data area and methods area | Keep plain |
| 10 | Init setup | New object -> setup -> starting data | Demystify `__init__` |
| 11 | Class demo labels | Annotated class snippet with class, attribute, methods | Minimal code |
| 12 | Self | Object card pointing to its own data | Avoid abstract theory |
| 14 | Prestige bias | Advanced-looking vs fit-for-purpose comparison | Do not mock class code |
| 16 | Reading checklist | Checklist for class name, stores, actions, object, method calls | Large readable text |
| 17 | Evidence | Modified file plus class/method explanation note | Keep documentation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Opening/review | 8 min | Use Slides 1 and 3 only | Ask where structure affected debugging |
| Working set | 6 min | Combine Slides 4 and 5 verbally | Define each OOP term on one line |
| Procedural/function demos | 15 min | Show only output | Compare responsibilities |
| Class demo | 18 min | Identify only class/methods | Annotate `self` and `__init__` |
| Common failure | 5 min | Mention verbally | Discuss AI-generated class code |
| Assignment bridge | 25+ min | Use checklist only | Confer on modifications |
| Closing check | 4 min | Ask two questions verbally | Have students explain class in pairs |

---

# Post-Lecture Notes

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
