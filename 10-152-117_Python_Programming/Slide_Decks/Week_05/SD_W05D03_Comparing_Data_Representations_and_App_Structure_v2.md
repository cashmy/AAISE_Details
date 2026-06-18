# Slide Deck Source - Week 5 Day 3

**Course:** 10-152-117 Python Programming  
**Week / Day:** Week 5 / Thursday  
**Date:** September 17, 2026  
**Weekly Theme:** Files, Errors, and Data Persistence  
**Lecture Title:** Comparing Data Representations and App Structure  
**Assignments Supported:** A9 - Structured Data Reader; A10 - Data Representation and App-Structure Preview  
**Readiness Target:** Students can compare multiple representations of the same information.  
**Primary Watch Point:** This is a recognition bridge, not a database implementation lesson.

---

# Session Purpose

This session helps students notice that the same information can be represented
in different forms.

The goal is comparison and explanation:

- What does this representation make easy?
- What does it make harder?
- What kind of program might need this shape?

The session launches A10 as a preview assignment. It should not drift into SQL,
ORM setup, or full application design.

---

# Review / Prior Work Bridge

Review from Day 2:

- CSV stores row/column style data.
- JSON stores labeled and nested values.
- Programs must understand the structure they read.
- Failure should be named specifically.

Bridge question:

> If the same information can be stored several ways, how do we decide which
> representation is better?

Today's answer:

> Better depends on use.

---

# Reading Alignment

Reference:

- `Weekly_Reading_Guide.md`, Week 5
- Textbook areas: **Files and Data Persistence**

Today's focus:

- CSV and structured data as data interchange
- configuration files as recognition
- database persistence as future reference
- comparing data representations

Skim or save for later:

- database persistence implementation
- INI and TOML configuration formats
- custom serialization
- advanced context manager design

---

# What We Will Use Today

Today we will use:

- plain text representation
- CSV representation
- JSON representation
- dictionary/list representation
- simple model-like or table-like preview
- easier/harder comparison language

Today we will not use yet:

- SQL implementation
- ORM implementation
- database setup
- full application architecture
- production data modeling

---

# Assignments Supported

Assignments supported:

- A9 - Structured Data Reader
- A10 - Data Representation and App-Structure Preview

A9 closes around reading structured data.

A10 asks students to compare representations and explain tradeoffs at a
recognition level.

---

# Demo Set For The Session

Primary demo:

- `Demos/Week_05_Files_Errors_and_Data_Persistence/08_data_representation_preview.py`

Supporting examples:

- A9 success example, if useful for review
- A10 success markdown, if useful for showing response shape

Do not add database implementation during this session.

---

# Slide Sequence Overview

| Section | Slides | Purpose |
| --- | ---: | --- |
| Opening / Review | 1-3 | Frame representation as a design choice |
| Working Set | 4-5 | Name what is comparison and what is deferred |
| Core Comparison | 6-10 | Compare text, CSV, JSON, dictionary/list, and model-like forms |
| Demo / Preview | 11-12 | Show same data represented multiple ways |
| Assignment Bridge | 13-15 | Launch A10 and close A9 expectations |
| Close | 16 | Define success as explanation, not implementation |

---

## Slide 1 - Same Information, Different Forms

**Delivery Category:** Core

**Student-Visible Text:**

The same information can live in different forms.

A note, a CSV row, a JSON object, a dictionary, and a table-like record may all
describe the same real thing.

**Instructor Notes:**

Frame this as a design-thinking day. Students are comparing, not building a new
database system.

**Transition Cue:**

Before comparing new forms, connect back to the structured shapes students used
on Day 2.

**Visual Notes:**

One "task" represented as text, CSV, JSON, and table row.

---

## Slide 2 - Review: Structured Data Has Shape

**Delivery Category:** Review

**Student-Visible Text:**

CSV shape helps with rows and columns.

JSON shape helps with labels and nested information.

Different shapes make different tasks easier.

**Instructor Notes:**

Bridge from A9. Ask for one student example of "what got easier" in CSV or JSON.

**Transition Cue:**

Once students see that each structure helps differently, introduce the main
decision idea for the day.

---

## Slide 3 - Today's Success Pattern

**Delivery Category:** Core

**Student-Visible Text:**

Today's success pattern:

- recognize at least two representations
- compare what each makes easier
- compare what each makes harder
- connect the representation to a larger application need
- avoid treating advanced structures as automatically better

**Instructor Notes:**

This prepares A10. The assignment is about reasoned comparison, not picking the
most advanced-looking option.

**Transition Cue:**

Now name the comparison set students will use to practice that pattern.

---

## Slide 4 - What We Will Use Today

**Delivery Category:** Core

**Student-Visible Text:**

Today we will compare:

- plain text
- CSV
- JSON
- list/dictionary structures
- table-like or model-like previews

We will ask what each form makes easier or harder.

**Instructor Notes:**

Use this to keep the lesson grounded in examples.

**Transition Cue:**

And just as important, separate recognition-level comparison from later
implementation work.

---

## Slide 5 - What We Will Save For Later

**Delivery Category:** Core

**Student-Visible Text:**

We will save these for later:

- building a database
- writing SQL
- implementing an ORM
- designing a production data model

Today is recognition and comparison.

**Instructor Notes:**

This is a hard scope boundary. Repeat it if students get anxious or ambitious.

**Transition Cue:**

Start the comparison with the simplest representation: plain text.

---

## Slide 6 - Plain Text Is Human Friendly

**Delivery Category:** Core

**Student-Visible Text:**

Plain text is easy for humans to read.

It becomes harder when the program needs to reliably select fields, filter
records, or compare values.

**Instructor Notes:**

Plain text is not bad. It is just limited for structured operations.

**Transition Cue:**

When records start to repeat in a similar shape, CSV becomes easier to reason
about.

---

## Slide 7 - CSV Is Table Friendly

**Delivery Category:** Core

**Student-Visible Text:**

CSV works well when data fits rows and columns.

It is useful for lists of similar records, but it can get awkward when data
needs deeper nested structure.

**Instructor Notes:**

Use familiar spreadsheet thinking without implying Excel mastery.

**Transition Cue:**

When the information needs labels or grouping, JSON gives a different kind of
structure.

---

## Slide 8 - JSON Is Structure Friendly

**Delivery Category:** Core

**Student-Visible Text:**

JSON works well when data needs labels, groups, or nested pieces.

It can be very useful, but it can also become hard to read if the nesting gets
too deep.

**Instructor Notes:**

Connect JSON back to dictionaries and lists.

**Transition Cue:**

The stored shape also affects the way the Python code tends to be organized.

---

## Slide 9 - Code Structures Can Mirror Data

**Delivery Category:** Core

**Student-Visible Text:**

Lists, dictionaries, and simple classes can mirror the shape of stored data.

The program's structure often follows the data's structure.

**Instructor Notes:**

This connects Week 3 structure to Week 5 representation without turning into
advanced OOP.

**Transition Cue:**

Instead of asking which structure is best in the abstract, ask what the program
needs to do.

---

## Slide 10 - Better Depends On Use

**Delivery Category:** Core

**Student-Visible Text:**

Ask:

- What needs to be read?
- What needs to be searched?
- What needs to be updated?
- What needs to be explained?

The answers guide the representation choice.

**Instructor Notes:**

This is the reusable heuristic for A10.

**Transition Cue:**

Now watch the same information move through several representations and compare
what changes.

---

## Slide 11 - Demo: Same Data, Different Representations

**Delivery Category:** Demo

**Student-Visible Text:**

Watch what changes when the same information appears as:

- plain text
- CSV-style data
- JSON-style data
- dictionary/list structure

**Instructor Notes:**

Use with:

`D:\@Artifact_Generation\108_AAISE_Details\10-152-117_Python_Programming\Demos\Week_05_Files_Errors_and_Data_Persistence\08_data_representation_preview.py`

Focus on comparison. Ask students to name one advantage and one limitation for
each form.

**Demo Connection:**

Primary demo file: `08_data_representation_preview.py`

**Transition Cue:**

The demo shows the small version. The same reasoning explains why larger apps
need stronger structure later.

---

## Slide 12 - Preview: Larger Apps Need Stronger Structure

**Delivery Category:** Core

**Student-Visible Text:**

As programs grow, data often needs more structure.

That does not mean we build a database today. It means we can recognize why
larger applications need organized data.

**Instructor Notes:**

This is the bridge to A10 and later Week 6 architecture.

**Transition Cue:**

Before launching A10, correct the common assumption that more complex always
means better.

---

## Slide 13 - Common Failure: Bigger Is Not Automatically Better

**Delivery Category:** Core

**Student-Visible Text:**

A database is not automatically better than a file.

A class is not automatically better than a dictionary.

The representation should fit the problem.

**Instructor Notes:**

Useful correction for prestige bias. Students may assume advanced tools are
always the right answer.

**Transition Cue:**

That right-sized thinking becomes the center of Assignment 10.

---

## Slide 14 - Assignment 10 Bridge

**Delivery Category:** Lab Bridge

**Student-Visible Text:**

For Assignment 10, compare at least two representations of the same information.

Explain what each form makes easier, what it makes harder, and where a larger
application might need more structure.

**Instructor Notes:**

This assignment can be worksheet, markdown, annotated code, or guided response.
It is intentionally recognition-level.

**Transition Cue:**

Make the evidence concrete so students know what a complete comparison looks
like.

---

## Slide 15 - Evidence For A10

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Your response should include:

- at least two representations
- clear easier/harder comparison
- beginner-level vocabulary
- connection to a larger application need
- AI-use note if AI helped explain a term

**Instructor Notes:**

This gives Schoology/README clarity. Students should not submit vague opinions.

**Transition Cue:**

End with the portable explanation students should be able to use beyond this
assignment.

---

## Slide 16 - Success Check

**Delivery Category:** Core

**Student-Visible Text:**

By the end of today, you should be able to say:

> This representation is useful for this purpose, but another representation may
> be better for a different purpose.

**Instructor Notes:**

Close on judgment and explanation. That is the actual readiness target.

---

# Demo Execution Notes

Recommended order:

1. Briefly review one A9 structured reader result.
2. Run `08_data_representation_preview.py`.
3. Pause after each representation and ask:
   - What got easier?
   - What got harder?
4. Show A10 response expectations.

Do not add database setup or live ORM examples.

---

# Lab / Assignment Bridge

A9 closeout:

- readable structured output
- meaningful selected values
- explanation of data shape

A10 launch:

- compare two or more representations
- use specific examples
- avoid implementation sprawl

---

# README / Submission Expectations

For A10, a markdown response may use:

```text
# Data Representation Comparison

## Representation 1

## Representation 2

## What became easier?

## What became harder?

## Where might a larger application need more structure?

## AI-use note, if used
```

---

# AI-Use Boundary

AI may be useful as a bounded explainer for terms such as:

- JSON
- CSV
- table
- model
- ORM

Students must restate explanations in their own words and connect them to the
provided examples.

AI should not turn A10 into a generated database essay.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt Direction | Cautions |
| --- | --- | --- | --- |
| 1 | Same data in forms | One task represented as note, CSV row, JSON, table | Keep all labels readable |
| 2 | Structured data review | CSV and JSON shapes making different tasks easier | Keep review visual simple |
| 3 | Today's success pattern | Recognize forms, compare tradeoffs, and connect to larger app needs | Avoid abstract theory |
| 4 | Working comparison set | Plain text, CSV, JSON, dictionary/list, table-like preview | Avoid implementation details |
| 5 | Scope boundary | Recognition path separated from database build path | Avoid making databases look forbidden |
| 6 | Plain text tradeoff | Human-readable note versus hard-to-select fields | Do not make plain text look wrong |
| 7 | CSV tradeoff | Row/column records useful for similar items | Avoid spreadsheet software UI |
| 8 | JSON tradeoff | Labeled/nested structure useful but can get deep | Avoid dense nesting |
| 9 | Code mirrors data | Stored data shape connected to list/dictionary/simple class | Avoid advanced OOP diagram |
| 10 | Choice heuristic | Four question cards: read, search, update, explain | Avoid dashboard style |
| 11 | Representation demo | Same data flowing into four representation boxes | No complex schema |
| 12 | Larger app preview | Stronger structure as future need, not today's build | Avoid database implementation |
| 13 | Bigger not better | Advanced-looking option versus right-sized fit | Avoid ranking advanced tools |
| 14 | A10 bridge | Compare forms and explain tradeoff | Keep response-focused |
| 15 | A10 evidence | Comparison worksheet/checklist | Avoid legal audit look |

---

# Instructor Timing Notes

Suggested timing:

- Review and framing: 10 minutes
- Representation comparison: 20 minutes
- Demo: 15 minutes
- A10 bridge: 10 minutes
- Lab / assignment time: remaining time

If students need more A9 support, reduce the model-like preview and protect
structured reader completion.

---

# Post-Lecture Notes

Use after teaching:

- Did students understand comparison rather than implementation?
- Did "database" create anxiety or excitement that needs bounding?
- Did A10 need a more concrete template?
- Which representation examples landed best?
