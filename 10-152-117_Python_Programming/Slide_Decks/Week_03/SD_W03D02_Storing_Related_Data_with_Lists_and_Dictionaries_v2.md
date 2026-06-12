# SLIDE DECK SOURCE - WEEK 3 DAY 2

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Week / Day | Week 3 / Tuesday |
| Date | September 1, 2026 |
| Weekly Theme | Organizing Code and Data |
| Lecture Title | Storing Related Data with Lists and Dictionaries |
| Assignments Supported | Assignment 5 - List or Dictionary Mini-App |
| Readiness Target | Students can store, retrieve, and loop through structured data |
| Primary Watch Point | Ensure dictionary access is explicitly taught before lookup-style tasks are assigned |
| Source Version | v2 refactor |

---

# Session Purpose

This session introduces lists and dictionaries as beginner-friendly ways to
organize related data.

Students should understand that data structures are not just new syntax. They
allow a program to store multiple related values, retrieve those values, loop
through them, and use them in small practical programs.

The target pattern is:

```text
store related data -> retrieve useful values -> loop or look up -> show behavior
```

---

# Review / Prior Work Bridge

Review from Monday:

- functions organize logic into named responsibilities
- meaningful names help code become easier to explain
- A4 asks students to use functions to improve code structure

Quick review questions:

- What job does a function own?
- What information goes into a function?
- What result or behavior comes out?
- How can a function use stored data?

Bridge into Day 2:

Yesterday organized logic. Today organizes information so a program can do more
useful work with related values.

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 3
- textbook chapter areas: **Built-In Data Types** and **Functions, the
  Building Blocks of Code**

Day 2 reading focus:

- mutable sequences
- lists
- mapping types
- dictionaries
- how to choose data structures

Use this reading to support:

- storing related data
- retrieving values
- iterating through a list
- looking up information in a dictionary

Today's reading boundary:

Students should not worry yet about comprehensions, generators, advanced
built-in functions, full namespace theory, or deep data-structure taxonomy.

---

# What We Will Use Today

Today we will use:

- lists
- list indexes
- `append()`
- `for` loops over lists
- dictionaries
- keys and values
- dictionary lookup
- a list of dictionaries

Today we will skip for now and revisit later:

- comprehensions
- generators
- advanced collection types
- complex nested data
- database work
- API response parsing as an implementation requirement

---

# Assignments Supported

Primary support:

- Assignment 5 - List or Dictionary Mini-App

A5 asks students to build a small program that uses a list or dictionary in a
useful way.

Good beginner options include:

- task list
- simple course lookup
- small inventory
- score tracker
- recommendation lookup
- list of simple records

---

# Readiness Target

By the end of the session, students should be able to:

- create a small list
- access a list item by position
- add an item to a list
- loop through a list
- create a small dictionary
- access a dictionary value by key
- explain the difference between list positions and dictionary keys
- choose one structure for a small A5 program

---

# Primary Watch Point

The main risk is students mixing up list indexes and dictionary keys.

Use the contrast repeatedly:

```text
list -> position
dictionary -> meaningful key
```

Students should not be assigned lookup-heavy work until dictionary access has
been shown slowly and explicitly.

---

# Demo Set For This Session

Primary demos:

- `Demos/Week_03_Organizing_Code_and_Data/04_list_basics.py`
- `Demos/Week_03_Organizing_Code_and_Data/05_dictionary_lookup.py`
- `Demos/Week_03_Organizing_Code_and_Data/06_list_of_dictionaries.py`

Recommended use:

1. Use Demo 4 for list storage, indexing, appending, and iteration.
2. Use Demo 5 for dictionary key/value lookup.
3. Use Demo 6 only after list and dictionary basics are visible.

---

# Student Hands-On Bridge

Students should begin A5 by choosing one small data structure and one visible
behavior.

Suggested start:

```text
1. Choose list or dictionary.
2. Name the related data being stored.
3. Add a few sample values.
4. Retrieve or loop through the values.
5. Print useful output.
```

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-3 | Review / Core | Connect function organization to data organization |
| Today's Working Set | 4-5 | Core | Bound list/dictionary topics and defer advanced collections |
| Lists | 6-9 | Core / Demo | Teach related values, indexes, appending, and iteration |
| Dictionaries | 10-13 | Core / Demo | Teach keys, values, lookup, and list-vs-dictionary distinction |
| Combined Data Shape | 14 | Demo / Core | Show list of dictionaries as future-facing but practical |
| Assignment 5 Bridge | 15-17 | Lab Bridge / Evidence | Start A5 with one structure and useful behavior |
| Closing Check | 18 | Assessment / Evidence | Define successful data-structure understanding |

---

# Slide-by-Slide Source

## Slide 1 - Programs Become Useful When They Remember Things

**Delivery Category:** Review

**Student-Visible Text:**

Programs become more useful when they can keep related values together.

Lists and dictionaries help a program remember, retrieve, and use information.

Today, watch for:

- what data is stored
- how the data is accessed
- how the program uses the data
- which structure fits the task

**Instructor Notes:**

Frame data structures as practical storage tools. Avoid opening with terminology
density. Students should first see why storing related data matters.

**Transition Cue:**

Yesterday organized logic. Today organizes information.

**Visual Notes:**

Use grouped values flowing into a small useful program.

---

## Slide 2 - Logic Uses Data

**Delivery Category:** Review

**Student-Visible Text:**

Functions organize logic.

Lists and dictionaries organize information.

Small programs often need both:

- a function for the job
- a data structure for the values
- output that shows the result

**Instructor Notes:**

Connect directly to Monday. Students should see functions and collections as
partners, not isolated topics.

**Transition Cue:**

The first structure is a list.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Store related data -> retrieve useful values -> loop or look up -> show output.

For each data structure, ask:

- What values are stored?
- How do I access one value?
- How do I use all values?
- What visible behavior proves it works?

**Instructor Notes:**

This is the main Day 2 mental model. Keep returning to store/retrieve/use.

**Transition Cue:**

Let's name today's working set.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will use:

- lists
- indexes
- `append()`
- loops over lists
- dictionaries
- keys and values
- dictionary lookup

These tools help a program work with more than one related value.

**Instructor Notes:**

Keep the tools visible. This is a lot for beginners, but it is manageable if
each tool is tied to a small behavior.

**Transition Cue:**

Some data topics are useful later, but not today's target.

---

## Slide 5 - What We Will Skip For Now

**Delivery Category:** Core

**Student-Visible Text:**

We will skip comprehensions, generators, advanced collections, databases, and
complex nested data for now.

Today's goal is practical:

- store a few values
- access the right value
- loop or look up
- print a useful result

**Instructor Notes:**

This boundary is important because the textbook and future topics can get much
deeper. Keep A5 beginner-sized.

**Transition Cue:**

Start with lists: one name holding multiple related values.

---

## Slide 6 - Lists Keep Related Items Together

**Delivery Category:** Core

**Student-Visible Text:**

A list stores multiple related values in one variable.

Example:

```python
tasks = ["read", "practice", "submit"]
```

Use a list when order or repeated display matters.

**Instructor Notes:**

Use familiar examples: tasks, scores, menu options, names. Avoid abstract data
structure language.

**Transition Cue:**

Each list item has a position.

---

## Slide 7 - List Positions Start At Zero

**Delivery Category:** Core

**Student-Visible Text:**

List items are accessed by position.

Python starts counting positions at `0`.

Example:

```python
tasks[0]
```

This gets the first task.

**Instructor Notes:**

This is often surprising for beginners. Keep it concrete and visual. Do not
spend too long on why zero-based indexing exists.

**Transition Cue:**

Now watch a list store, display, and update tasks.

---

## Slide 8 - Demo 1: List Basics

**Delivery Category:** Demo

**Student-Visible Text:**

Watch the list change.

Trace:

- the starting values
- the item accessed by position
- the loop that displays all items
- the new item added with `append()`

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/04_list_basics.py`

Pause on `tasks[0]`, then on the `for task in tasks` loop, then on
`append()`.

**Transition Cue:**

Lists use positions. Dictionaries use meaningful keys.

**Demo Connection:**

Primary demo file: `04_list_basics.py`

---

## Slide 9 - Looping Makes A List Useful

**Delivery Category:** Core

**Student-Visible Text:**

A list becomes useful when the program can use each item.

Common beginner pattern:

```python
for task in tasks:
    print(task)
```

The loop handles one item at a time.

**Instructor Notes:**

Connect back to Week 2 loops. Students already know repetition; now the loop
repeats over stored data.

**Transition Cue:**

Now move from positions to labels.

---

## Slide 10 - Dictionaries Connect Meaning To Value

**Delivery Category:** Core

**Student-Visible Text:**

A dictionary stores values by key.

Example:

```python
course = {"title": "Python Programming", "credits": 2}
```

The key is a meaningful label for the value.

**Instructor Notes:**

Use the phrase "label to value" repeatedly. It helps students distinguish
dictionaries from lists.

**Transition Cue:**

Dictionary lookup uses the key, not a position.

---

## Slide 11 - Keys Are Not Positions

**Delivery Category:** Core

**Student-Visible Text:**

Lists use positions.

Dictionaries use keys.

Compare:

```python
tasks[0]
course["title"]
```

The list asks for a position. The dictionary asks for a label.

**Instructor Notes:**

This is the primary watch point. Slow down. Put list indexing and dictionary
lookup side by side.

**Transition Cue:**

Now watch a dictionary lookup in a small example.

---

## Slide 12 - Demo 2: Dictionary Lookup

**Delivery Category:** Demo

**Student-Visible Text:**

Watch how the dictionary connects keys to values.

Trace:

- each key
- each stored value
- the lookup expression
- the output created from the lookup

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/05_dictionary_lookup.py`

Pause on `course["number"]`, `course["title"]`, and adding
`course["meeting_days"]`.

**Transition Cue:**

Sometimes a program needs multiple records with the same shape.

**Demo Connection:**

Primary demo file: `05_dictionary_lookup.py`

---

## Slide 13 - Choosing A Structure

**Delivery Category:** Core

**Student-Visible Text:**

Choose the structure that matches the job.

Use a list when:

- you have several related items
- order matters
- you want to loop through all items

Use a dictionary when:

- labels matter
- you want to look up a value by name
- one item has several named parts

**Instructor Notes:**

This prepares A5 choices. Keep the distinction practical, not theoretical.

**Transition Cue:**

A common next step is a list of small dictionaries.

---

## Slide 14 - Demo 3: List Of Dictionaries

**Delivery Category:** Demo

**Student-Visible Text:**

A list of dictionaries can store multiple records.

In the demo, each student has:

- a name
- a score
- a status decision

The loop handles one record at a time.

**Instructor Notes:**

Use:

`Demos/Week_03_Organizing_Code_and_Data/06_list_of_dictionaries.py`

Make this a bridge, not an overload. It prepares later JSON/API structures,
but A5 can still use a simple list or simple dictionary.

**Transition Cue:**

Now students can choose one useful structure for A5.

**Demo Connection:**

Primary demo file: `06_list_of_dictionaries.py`

---

## Slide 15 - Assignment 5 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 5, build one small mini-app using a list or dictionary.

A good first version should include:

- one chosen structure
- a few sample values
- one useful lookup or loop
- visible output
- a short explanation of why the structure fits

**Instructor Notes:**

Keep students from overbuilding. A5 is a mini-app, but "mini" matters. Useful
behavior can be very small.

**Transition Cue:**

Start with the data before adding too many features.

**Lab Connection:**

Supports Assignment 5 - List or Dictionary Mini-App.

---

## Slide 16 - Data Planning Checklist

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

Before coding, write a small data plan.

Answer:

- What related values do I need?
- Should I use a list or dictionary?
- How will I access the data?
- What output proves the data was used?

**Instructor Notes:**

This is especially useful for students who stare at a blank file. The plan
should be short and practical.

**Transition Cue:**

The evidence should show both storage and use.

---

## Slide 17 - Evidence For A Data Mini-App

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your submission should show that the data structure is useful.

Useful evidence includes:

- one working `.py` file
- list or dictionary data
- retrieval, lookup, or loop behavior
- visible output
- short explanation of the structure choice

**Instructor Notes:**

If a student stores data but never uses it, the assignment is incomplete. The
program must do something visible with the structure.

**Transition Cue:**

Close by returning to store, retrieve, and use.

---

## Slide 18 - Closing Success Check

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

If you can store it, retrieve it, and use it, the structure is doing its job.

Before submitting A5, ask:

- What data is stored?
- How is one value accessed?
- How are multiple values used?
- Why did I choose this structure?

**Instructor Notes:**

Close around useful behavior. Thursday will compare rough and cleaner structure
using both functions and data choices.

**Transition Cue:**

Next session, we compare rough code to cleaner organized code.

---

# Demo Execution Notes

Recommended live sequence:

1. Review one function responsibility from Day 1.
2. Run `04_list_basics.py`.
3. Trace index access, loop display, and `append()`.
4. Run `05_dictionary_lookup.py`.
5. Emphasize key/value lookup and adding a new key.
6. Run `06_list_of_dictionaries.py` only after basics are clear.
7. Move students into A5 data planning.

Instructor pacing note:

If dictionary lookup is shaky, slow down before list-of-dictionaries. A simple
dictionary mini-app is more valuable than a rushed nested structure.

---

# Lab / Assignment Bridge

By the end of Day 2, students should have started A5 or have a clear data
plan.

Minimum A5 start target:

- selected list or dictionary
- sample values written
- one access or loop plan
- one expected output

---

# README / Submission Expectations

Suggested student evidence:

- clear `.py` filename
- code that runs without syntax errors
- list or dictionary data
- visible output using that data
- short explanation of why the chosen structure fits

---

# AI-Use Boundary

AI is not allowed for normal A5 work unless the instructor explicitly says
otherwise.

Students should first practice manually choosing, storing, retrieving, and
using data. If AI is later allowed for comparison, students must still explain
why the chosen structure makes sense.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Related values | Several values grouped into one useful program | Avoid database imagery this early |
| 2 | Logic plus data | Function box using list/dictionary data | Keep simple |
| 3 | Success pattern | Store -> retrieve -> loop/look up -> output | Avoid large architecture flow |
| 4 | Today's tools | Toolbox with list, index, append, loop, dictionary, key/value | Avoid advanced collections |
| 5 | Deferred data topics | Parked-for-later shelf: comprehensions, generators, databases | Keep reassuring |
| 6 | List container | One list holding several task values | Make list brackets visible |
| 7 | Zero-based index | List items labeled 0, 1, 2 | Do not over-explain |
| 8 | List demo | List before and after append plus loop output | Keep output readable |
| 10 | Dictionary pairs | Key/value cards connected by labels | Avoid table overload |
| 11 | Position vs key | Split visual: list position vs dictionary key | Make contrast clear |
| 12 | Dictionary lookup | `course["title"]` pointing to value | Keep code minimal |
| 13 | Choose structure | List use cases vs dictionary use cases | Avoid too many criteria |
| 14 | List of dictionaries | Three record cards inside a list container | Frame as bridge |
| 15 | A5 bridge | Mini-app data options: tasks, inventory, scores, lookup | Avoid making one required |
| 17 | Evidence | `.py` file, data structure, output, explanation note | Keep documentation light |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and opening | 8 min | Use Slides 1 and 3 only | Ask how a function might use data |
| Working set | 5 min | Combine Slides 4 and 5 verbally | Discuss future database/API bridge lightly |
| Lists | 15 min | Use Demo 4 only | Have students predict list output |
| Dictionaries | 18 min | Use one lookup only | Compare list index and dictionary key repeatedly |
| List of dictionaries | 8 min | Skip if needed | Trace one record through the loop |
| Assignment bridge | 20+ min | Assign one common option | Confer on structure choice |
| Closing check | 4 min | Ask two questions verbally | Have students justify list vs dictionary |

---

# Post-Lecture Notes

Use after delivery to record what worked, what needs adjustment, and what
should change in the next course run.

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
