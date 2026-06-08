# Week 03 Deck Source - Data Structure Choice

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 3 |
| Phase / Unit | Unit 2 - Data Structures: Search, Sort, and Growth |
| Lecture Title | Choosing How the Data Lives |
| Related Lab | Lab 03 - Data Structure Choice |
| Related Demo | Attendance Tracking With a List and a Dictionary |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students learn that data structure choice is an algorithmic design decision.

The goal is not to memorize every operation table from the textbook. The goal
is to understand that lists, tuples, dictionaries, sets, dataframes, matrices,
and abstract data types make different operations easier, harder, clearer, or
more expensive.

---

# Possible Two-Session Split

The Week 3 reading is broad. It covers Python built-ins, data-analysis
structures, matrix operations, and abstract data types. This can be taught as
one longer lecture with breaks, but a two-session split may reduce overload.

## Session A - Built-In Structures and Operation Fit

Recommended slides:

- 1-4: review and opening frame
- 5-9: reading overview and decision frame
- 10-19: list, tuple, dictionary, set
- 20-23: operation comparison and complexity tables

Session A target:

Students understand that built-in Python structures support different access
patterns.

## Session B - Broader Structures, Demo, and Lab Transfer

Recommended slides:

- 24-30: Series, DataFrames, matrices
- 31-37: abstract data types
- 38-41: demo
- 42-44: lab bridge
- 45-48: wrap-up and Week 4 reading preparation

Session B target:

Students can compare two structures for the same problem and justify which one
better fits the operations.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook | Big picture breakdown of four main points | Frames Week 3 as a curated tour of structure choices |
| Textbook | Built-in data types | Primary focus for developer-level structure choice |
| Textbook | Lists | Sequence, iteration, append, lookup tradeoffs |
| Textbook | Tuples | Fixed ordered records and immutability |
| Textbook | Dictionaries | Key-based lookup and update |
| Textbook | Sets | Membership and uniqueness |
| Textbook | Time complexity of built-in operations | Used as reference, not memorization target |
| Textbook | Series and DataFrames | Introduces tabular data representation for analytics |
| Textbook | DataFrame subset, column selection, row selection | Shows that data representation affects access patterns |
| Textbook | Time complexity analysis for sets | Reinforces membership and uniqueness behavior |
| Textbook | Matrices and matrix operations | Brief bridge to AI/data/math-heavy structures |
| Textbook | Abstract data types | Introduces structure by behavior rather than implementation |
| Textbook | Vectors, stacks, queues, trees | Recognition and use-case framing |
| Course artifact | Lab 03 - Data Structure Choice | Student comparison of two structures |
| Course artifact | Lab 03 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading introduces a large set of data structures. Some are Python built-in
types students have already seen. Others, such as Series, DataFrames, matrices,
vectors, stacks, queues, and trees, may be newer or more abstract.

The key idea is that a data structure is not just a container. It shapes the
algorithm. It affects what is easy to add, find, update, remove, compare, or
explain.

The textbook includes time-complexity information for many operations. Students
do not need to memorize every operation table this week. They should learn how
to read those tables as reference material and connect them to practical
questions:

- What operation matters most?
- How often does that operation happen?
- Does the structure make that operation clear?
- Does the structure make that operation expensive?

## Reading Key Ideas

- Data structure choice is part of algorithm design.
- Python built-in types support different access patterns.
- Complexity tables are reference tools, not panic triggers.
- Series and DataFrames matter when data becomes tabular.
- Matrices matter in many AI, data, graphics, and scientific contexts.
- Abstract data types define behavior even when implementation details vary.

## Terms To Carry Forward

| Term | Brief Meaning |
| --- | --- |
| Data structure | A way to organize data for use by an algorithm |
| Access pattern | The operations the algorithm performs most often |
| List | Ordered, changeable collection |
| Tuple | Ordered, fixed collection |
| Dictionary | Key-value structure for direct lookup |
| Set | Collection focused on uniqueness and membership |
| Series | One-dimensional labeled data structure |
| DataFrame | Two-dimensional table-like data structure |
| Matrix | Rectangular arrangement of values used in mathematical operations |
| Abstract data type | A structure defined by behavior, not one specific implementation |
| Stack | Last-in, first-out access pattern |
| Queue | First-in, first-out access pattern |
| Tree | Hierarchical structure with parent-child relationships |

## What We Will Use Today

- list, tuple, dictionary, and set behavior
- operation-based comparison
- access pattern as the reason for choosing a structure
- Series/DataFrame and matrix recognition
- stacks, queues, and trees as abstract patterns
- Lab 03 comparison table

## What We Will Revisit Later

- deeper search and sort behavior
- graph structures
- recursion and tree traversal
- matrix-heavy algorithms
- data modeling and analytics structures
- library-specific performance details

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain why data structure choice affects algorithm design.
2. Compare lists, tuples, dictionaries, and sets using common operations.
3. Identify when tabular or matrix structures may be relevant.
4. Recognize stacks, queues, trees, and vectors as abstract data types.
5. Justify a structure choice using operation fit and tradeoffs.
6. Avoid choosing a structure only because it is familiar.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from growth behavior to representation choice |
| Textbook Review | 5-9 | Core | Curate the broad reading into a usable decision frame |
| Built-In Data Types | 10-19 | Core | Compare list, tuple, dictionary, and set |
| Operation Fit and Complexity | 20-23 | Core | Translate Big-O tables into developer questions |
| Series, DataFrames, Matrices | 24-30 | Core / Optional | Introduce data-analysis and matrix structures without overload |
| Abstract Data Types | 31-37 | Core / Optional | Recognize vectors, stacks, queues, and trees |
| Demo Bridge | 38-41 | Core | Compare list and dictionary attendance tracking |
| Lab Bridge | 42-44 | Core | Connect demo to Lab 03 |
| Wrap-Up | 45-48 | Core | Consolidate, assign next action, and prepare Week 4 reading |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 02 Taught Us

**Delivery Category:** Core

**Slide Text:**

Last week, we compared approaches by looking at:

- input size
- timing evidence
- repeated work
- growth pattern
- limitation notes

**Instructor Notes:**

Use one Lab 02 timing table or demo output. Keep the review brief. The goal is
to remind students that algorithm behavior changes when the amount of data
changes.

**Transition Cue:**

This week keeps the growth-awareness lens but shifts the focus to how the data
is organized before the algorithm works on it.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

What structure makes this problem easier to solve?

**Instructor Notes:**

Make this the anchor question. Students should leave understanding that the
same information can be stored in more than one way, and that each way changes
the code.

**Transition Cue:**

The structure is not just storage. It shapes the algorithm.

---

## Slide 3 - Data Structures Shape Algorithms

**Delivery Category:** Core

**Slide Text:**

Data structure choice affects:

- how data is stored
- how data is found
- how data is updated
- how data is removed
- how the code reads

**Instructor Notes:**

Use the phrase "how the data lives." This is not only a performance topic. It
is also a clarity and design topic.

**Transition Cue:**

That is why choosing a familiar structure is not always the same as choosing
the right structure.

---

## Slide 4 - Familiar Is Not Always Fit

**Delivery Category:** Core

**Slide Text:**

A familiar structure may work.

But a better-fitting structure may make the solution:

- clearer
- shorter
- easier to test
- easier to update
- more efficient

**Instructor Notes:**

This slide prepares students for Lab 03. They should not automatically choose
lists because lists are familiar, and they should not automatically choose
dictionaries because dictionaries feel powerful.

**Transition Cue:**

Start with the reading's big picture: four categories of structure topics.

---

# Textbook Review

## Slide 5 - Textbook Review: Four Main Areas

**Delivery Category:** Core

**Slide Text:**

The reading covers:

1. built-in data types
2. Series and DataFrames
3. matrices and matrix operations
4. abstract data types

**Instructor Notes:**

Tell students that not all four areas receive equal depth in this course week.
Built-ins and operation fit are the core. DataFrames, matrices, and abstract
types are important recognition and future-reference areas.

**Transition Cue:**

The built-in types are the most immediately useful for Lab 03.

---

## Slide 6 - Textbook Review: Built-In Types

**Delivery Category:** Core

**Slide Text:**

Built-in structures include:

- list
- tuple
- dictionary
- set

Each supports different operations.

**Instructor Notes:**

Students have likely used these before. The new move is to ask why one
structure fits a task better than another.

**Transition Cue:**

For each structure, ask the same developer question: what operations does this
make easy?

---

## Slide 7 - Textbook Review: Tabular Data

**Delivery Category:** Core

**Slide Text:**

Series and DataFrames help represent labeled or tabular data.

Common operations include:

- selecting columns
- selecting rows
- creating subsets
- summarizing data

**Instructor Notes:**

Frame this as a bridge to data analytics and later AI/data work. Students do
not need to master pandas this week, but they should recognize why table-like
structures matter.

**Transition Cue:**

The reading also introduces matrix structures, which often look more
mathematical.

---

## Slide 8 - Textbook Review: Matrices

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

Matrices organize values in rows and columns.

They appear in:

- data science
- graphics
- machine learning
- scientific computing
- transformations

**Instructor Notes:**

This may look math-heavy. Do not turn the lecture into matrix algebra. The
developer-level takeaway is recognition: a matrix is a structured rectangular
representation that supports certain operations.

**Transition Cue:**

Finally, the reading introduces abstract data types.

---

## Slide 9 - Textbook Review: Abstract Data Types

**Delivery Category:** Core

**Slide Text:**

Abstract data types describe behavior.

Examples:

- vector
- stack
- queue
- tree

**Instructor Notes:**

Emphasize "behavior." A stack is not important because of one specific Python
class. It is important because of the last-in, first-out access pattern.

**Transition Cue:**

Now start with the built-in type students will reach for most often: the list.

---

# Built-In Data Types

## Slide 10 - List

**Delivery Category:** Core

**Slide Text:**

the built-in type students will reach for most often: the list.

**Instructor Notes:**

Use a simple example: attendance names in order of check-in. The list preserves
sequence and allows duplicates.

**Transition Cue:**

Lists are flexible, but some operations require searching through the list.

---

## Slide 11 - List Operation Fit

**Delivery Category:** Core

**Slide Text:**

Lists are often good for:

- append
- iteration
- ordered display

Lists may be awkward for:

- repeated direct lookup
- frequent membership checks
- updating one item by name

**Instructor Notes:**

Tie this to Week 2. A list can be perfectly correct and still require repeated
scanning for certain operations.

**Transition Cue:**

Tuples look similar to lists, but they communicate a different intent.

---

## Slide 12 - Tuple

**Delivery Category:** Core

**Slide Text:**

A tuple is an ordered, fixed collection.

Useful when:

- values belong together
- the group should not change
- position has meaning

**Instructor Notes:**

Example: `(x, y)` coordinates or a fixed record such as `(student_id, name)`.
Do not overdevelop tuple internals. The key idea is fixed grouped values.

**Transition Cue:**

When direct lookup by name or ID matters, dictionaries become more natural.

---

## Slide 13 - Dictionary

**Delivery Category:** Core

**Slide Text:**

A dictionary stores key-value pairs.

Useful when:

- each item has an identifier
- direct lookup matters
- updates are based on a key
- labels make code clearer

**Instructor Notes:**

Use the demo preview: `{"Ava": 2}` directly connects a student name to an
attendance count.

**Transition Cue:**

Dictionaries are powerful, but they are not automatically the answer to every
problem.

---

## Slide 14 - Dictionary Operation Fit

**Delivery Category:** Core

**Slide Text:**

Dictionaries often fit:

- lookup by key
- update by key
- counting
- grouping records

Watch for:

- key choice
- missing keys
- order requirements

**Instructor Notes:**

Students may hear "dictionary lookup is fast" and conclude dictionaries are
always better. Push back gently: if order is the main requirement, or if keys
are unclear, a dictionary may not be the simplest fit.

**Transition Cue:**

When the question is membership or uniqueness, sets become important.

---

## Slide 15 - Set

**Delivery Category:** Core

**Slide Text:**

A set stores unique values.

Useful when:

- membership matters
- duplicates should collapse
- uniqueness is the point

**Instructor Notes:**

Use examples: registered usernames, completed IDs, blocked words, already-seen
items. Sets are about "have we seen this?" more than "where is this in order?"

**Transition Cue:**

Sets are excellent for membership, but they intentionally remove duplicates.

---

## Slide 16 - Set Operation Fit

**Delivery Category:** Core

**Slide Text:**

Sets often fit:

- membership checks
- duplicate removal
- uniqueness tracking
- intersections and differences

Sets may not fit:

- preserving duplicates
- preserving original order
- storing attached values

**Instructor Notes:**

Connect to Week 2's lookup demo. Set membership can be a better fit when the
operation is "is this value present?"

**Transition Cue:**

Now compare the four built-ins using the operation lens.

---

## Slide 17 - Built-In Structure Comparison

**Delivery Category:** Core

**Slide Text:**

Ask what the problem needs:

- order?
- fixed grouping?
- key-based lookup?
- uniqueness?
- duplicates?
- updates?

**Instructor Notes:**

This is a decision slide. Students should not ask "What structure do I like?"
They should ask "What does the problem need me to do often?"

**Transition Cue:**

The textbook's complexity tables help answer that question, but they should be
read as references.

---

## Slide 18 - Complexity Tables Are Reference Tools

**Delivery Category:** Core

**Slide Text:**

When you see Big-O operation tables:

- do not panic
- find the operation
- compare likely costs
- connect cost to your use case
- verify with evidence when needed

**Instructor Notes:**

This slide is important for math-heavy textbook anxiety. The table is a tool,
not a character test. Developers commonly look up operation costs when they
need them.

**Transition Cue:**

In Lab 03, the comparison should name operations instead of giving only a
general opinion.

---

## Slide 19 - Operation Names Matter

**Delivery Category:** Core

**Slide Text:**

Avoid:

```text
Dictionaries are better.
```

Prefer:

```text
For lookup by student name, the dictionary is a better fit.
```

**Instructor Notes:**

This is the most important communication move for Lab 03. Students must tie
their recommendation to an operation and access pattern.

**Transition Cue:**

Now connect operation names to comparison language.

---

# Operation Fit and Complexity

## Slide 20 - Access Pattern

**Delivery Category:** Core

**Slide Text:**

Access pattern means:

- how data is usually added
- how data is usually found
- how data is usually updated
- how data is usually removed
- how data is usually displayed

**Instructor Notes:**

Use the phrase "usually." A structure choice should fit the common operation,
not only a rare operation.

**Transition Cue:**

A comparison table makes the access pattern visible.

---

## Slide 21 - Operation Comparison Table

**Delivery Category:** Core

**Slide Text:**

Compare structures by operation:

| Operation | Structure A | Structure B | Better Fit | Why? |
| --- | --- | --- | --- | --- |
| lookup | list scan | dictionary key | dictionary | direct lookup |

**Instructor Notes:**

Tell students this is the evidence format they will use in Lab 03. The table
forces them to name the operation, compare both structures, and justify the
better fit.

**Transition Cue:**

Complexity can support the comparison, but clarity also matters.

---

## Slide 22 - Complexity And Clarity

**Delivery Category:** Core

**Slide Text:**

A good structure choice considers:

- correctness
- operation cost
- code clarity
- memory use
- future change

**Instructor Notes:**

Connect to Week 2 and Week 3 together. Complexity matters, but students should
not ignore readability and maintainability.

**Transition Cue:**

Now consider a structure category that becomes important when data looks like a
table.

---

## Slide 23 - AI-Assisted Structure Review

**Delivery Category:** Core

**Slide Text:**

AI can help review a structure choice.

Ask AI to:

- identify the access pattern
- compare two structures
- explain tradeoffs
- suggest an alternative
- avoid rewriting unless asked

**Instructor Notes:**

Follow the same pattern from Week 2. Students choose and explain first, then
AI may critique or suggest alternatives.

Useful prompt:

```text
I am solving this problem with [structure A] and [structure B].
Compare them for add, lookup, update, remove, and display.
Explain which structure fits the access pattern better.
Do not rewrite my code unless I ask.
```

**Transition Cue:**

The textbook also introduces data structures that are common in analytics.

---

# Series, DataFrames, Matrices

## Slide 24 - Series

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

A Series is like a labeled one-dimensional data structure.

Think:

- one column
- labels or index
- values

**Instructor Notes:**

Keep this recognition-level unless students already know pandas. A Series is
not central to Lab 03, but it matters for data analytics foundations.

**Transition Cue:**

A DataFrame extends this idea into a table.

---

## Slide 25 - DataFrame

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

A DataFrame is table-like.

It supports:

- columns
- rows
- labels
- subsets
- summaries

**Instructor Notes:**

Use a spreadsheet analogy carefully. A DataFrame is not just a spreadsheet, but
the table analogy helps beginners.

**Transition Cue:**

DataFrame operations often ask which rows or columns we want.

---

## Slide 26 - DataFrame Subsets

**Delivery Category:** Optional Deepening

**Slide Text:**

Common DataFrame questions:

- Which column?
- Which row?
- Which subset?
- Which condition?

**Instructor Notes:**

This is a bridge to later data analytics and data modeling. Do not teach pandas
syntax here unless it directly serves the class.

**Transition Cue:**

The reading also mentions matrices, which may look more mathematical.

---

## Slide 27 - Matrices Without Panic

**Delivery Category:** Core

**Slide Text:**

A matrix is a rectangular structure of values.

For now, recognize:

- rows
- columns
- positions
- operations across values

**Instructor Notes:**

Use this as a math-anxiety bridge. Students do not need matrix algebra today.
They need to recognize that matrices are structured data used heavily in AI,
graphics, science, and analytics.

**Transition Cue:**

Matrix operations can have important complexity costs, but Week 3 only needs a
brief treatment.

---

## Slide 28 - Matrix Operations

**Delivery Category:** Instructor Reserve

**Slide Text:**

Matrix operations may involve:

- accessing a value
- adding matrices
- multiplying matrices
- transforming data

Complexity depends on the operation and dimensions.

**Instructor Notes:**

Use only if time allows or if students ask why matrices matter. Avoid turning
this into a formula lecture.

**Transition Cue:**

The developer question remains the same: what operation matters?

---

## Slide 29 - Data Structures For AI And Analytics

**Delivery Category:** Optional Deepening

**Slide Text:**

Later AI and analytics work uses:

- tables
- vectors
- matrices
- graphs
- indexes

Week 3 gives the recognition layer.

**Instructor Notes:**

This helps students see why the textbook includes broader structures. They are
not all immediate Lab 03 requirements, but they are part of the future
technical landscape.

**Transition Cue:**

Now move from concrete Python structures to abstract data types.

---

## Slide 30 - What To Deeply Learn vs Recognize

**Delivery Category:** Core

**Slide Text:**

Deeply learn now:

- list
- dictionary
- set
- operation comparison

Recognize for now:

- Series/DataFrame
- matrix
- vector
- stack/queue/tree

**Instructor Notes:**

This is the curation slide. It protects students from treating the whole
chapter as equal-weight memorization.

**Transition Cue:**

Recognition matters because abstract data types appear everywhere in software.

---

# Abstract Data Types

## Slide 31 - Abstract Data Type

**Delivery Category:** Core

**Slide Text:**

An abstract data type is defined by behavior.

It asks:

- what operations are allowed?
- what access pattern is expected?
- what rules shape use?

**Instructor Notes:**

Use the phrase "behavior before implementation." The same abstract pattern may
be implemented in different ways.

**Transition Cue:**

Start with vector because it connects to arrays, coordinates, and AI/data
topics.

---

## Slide 32 - Vector

**Delivery Category:** Optional Deepening

**Slide Text:**

A vector is an ordered collection of values.

It may represent:

- coordinates
- measurements
- features
- direction or magnitude

**Instructor Notes:**

Keep this recognition-level. Vectors become more important in AI/data contexts,
but Week 3 does not need vector math.

**Transition Cue:**

Stacks and queues are easier because they are about access order.

---

## Slide 33 - Stack

**Delivery Category:** Core

**Slide Text:**

A stack uses last-in, first-out behavior.

Think:

- undo history
- browser back stack
- nested tasks
- function call stack

**Instructor Notes:**

The key phrase is last-in, first-out. The most recent item is handled first.

**Transition Cue:**

A queue uses the opposite access pattern.

---

## Slide 34 - Queue

**Delivery Category:** Core

**Slide Text:**

A queue uses first-in, first-out behavior.

Think:

- help desk tickets
- print jobs
- checkout line
- task scheduling

**Instructor Notes:**

The key phrase is first-in, first-out. The earliest item is handled first.

**Transition Cue:**

Trees organize data hierarchically.

---

## Slide 35 - Tree

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

A tree represents hierarchy.

Think:

- folders
- organization charts
- decision trees
- parent-child relationships

**Instructor Notes:**

Do not teach tree traversal yet. This is recognition and use-case framing.
Traversal appears later.

**Transition Cue:**

Now compare these abstract structures by access pattern.

---

## Slide 36 - Abstract Types By Access Pattern

**Delivery Category:** Core

**Slide Text:**

Ask:

- Need last item first? Stack.
- Need first item first? Queue.
- Need hierarchy? Tree.
- Need ordered values? Vector.

**Instructor Notes:**

This is intentionally simplified. Students need recognition and vocabulary
before deeper implementation.

**Transition Cue:**

The same decision pattern applies to built-ins and abstract types: match the
structure to the operation.

---

## Slide 37 - Week 3 Decision Frame

**Delivery Category:** Core

**Slide Text:**

Choose a structure by asking:

- What data do I store?
- What operation happens most?
- What should be fast or clear?
- What tradeoff am I accepting?

**Instructor Notes:**

This slide sets up the demo and the lab. It is the Week 3 version of the
general algorithmic problem-solving frame.

**Transition Cue:**

Now apply the decision frame to attendance tracking.

---

# Demo Bridge

## Slide 38 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo problem:

Track attendance check-ins.

Compare:

- list of names
- dictionary of attendance counts

**Instructor Notes:**

Make clear that both structures can represent the attendance information, but
they make different operations easier or harder.

**Demo File / Artifact:**

`Assignments/Lab_03/demo/demo_code.py`

**Transition Cue:**

Start by identifying the core operation.

---

## Slide 39 - Demo Core Operation

**Delivery Category:** Core

**Slide Text:**

Core operation:

Record one more check-in for Ava.

Then inspect:

- how the list changes
- how the dictionary changes
- how lookup works

**Instructor Notes:**

Use the before/after printed representation. The list appends another name.
The dictionary updates one count by key.

**Transition Cue:**

The comparison table makes the operation fit visible.

---

## Slide 40 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

Watch for:

- before/after representation
- lookup result
- operation comparison
- better fit
- why the fit is better

**Instructor Notes:**

Run the demo. Point to the comparison table, not just the output. The important
claim is not "dictionary good, list bad." The claim is "dictionary better fits
direct lookup and update by student name."

**Observable Output / Evidence:**

The demo prints representation snapshots and an operation comparison table.

**Transition Cue:**

Now translate the demo into the lab pattern.

---

## Slide 41 - Demo Explanation Pattern

**Delivery Category:** Core

**Slide Text:**

Good explanation:

- names the operation
- compares both structures
- identifies the better fit
- explains the tradeoff

**Instructor Notes:**

Model one sentence:

"For looking up Ava's attendance count, the dictionary is a better fit because
the name is used as a key and the count can be read directly. The list can
still work, but it has to scan and count matching names."

**Transition Cue:**

The lab uses a different scenario but the same comparison pattern.

---

# Lab Bridge

## Slide 42 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 03, choose a different scenario and compare two structures.

Your work must include:

- two structures
- at least three operations
- implementation or simulation
- comparison table
- recommendation

**Instructor Notes:**

Make the transfer explicit. Students should not use attendance tracking as
their submission unless specifically assigned. They should apply the same
comparison method to a different scenario.

**Transition Cue:**

The comparison table is the center of the lab evidence.

---

## Slide 43 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should show:

- problem statement
- structures compared
- operations tested
- comparison table
- recommendation
- AI-use note, if applicable

**Instructor Notes:**

Remind students that "better fit" must be tied to a specific operation or
access pattern.

**Transition Cue:**

AI may help critique the structure choice, but students choose and explain
first.

---

## Slide 44 - AI Use In Lab 03

**Delivery Category:** Core

**Slide Text:**

Manual first:

- choose two structures
- explain your first comparison
- identify key operations

Then AI may help:

- suggest alternatives
- critique tradeoffs
- clarify operation fit

**Instructor Notes:**

This matches the student-facing AI use rule. AI can help after the student has
made an initial structure choice and comparison.

**Transition Cue:**

End with what students should carry forward.

---

# Wrap-Up

## Slide 45 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Data structures are choices.

Choose based on:

- operations
- access patterns
- clarity
- tradeoffs

**Instructor Notes:**

This is the core Week 3 takeaway. The structure should fit the problem's most
important operations.

**Transition Cue:**

Now make the next action concrete.

---

## Slide 46 - Lab 03 Success Check

**Delivery Category:** Core

**Slide Text:**

Successful Lab 03 work:

- uses two structures meaningfully
- compares specific operations
- explains tradeoffs
- avoids habit-only choices
- gives a clear recommendation

**Instructor Notes:**

Students should be able to use this slide as a checklist before submission.

**Transition Cue:**

Finish with the immediate lab action.

---

## Slide 47 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 03:

- choose a scenario
- choose two structures
- compare at least three operations
- build the comparison table
- recommend the better fit

**Instructor Notes:**

Remind students that a simple comparison done clearly is better than a complex
comparison they cannot explain.

---

## Slide 48 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

Next week focuses on search and sort behavior.

As you read, focus on:

- sorting as a way to arrange data
- searching as a way to find a target
- variable swapping as a small mechanical step
- linear search, binary search, and interpolation search
- why binary search requires sorted data
- performance differences among search and sort strategies
- practical lookup ideas such as primary and foreign keys

Treat Natural Language Processing as context, not as a new coding target.

**Instructor Notes:**

Use this slide to prepare students for the breadth of the Week 4 reading. The
reading introduces several sorting algorithms and several searching algorithms,
but students should not treat the week as a memorization test.

Tell students to read for behavior and assumptions:

- What does the algorithm do?
- What must be true before it works?
- What evidence would show that it works?
- What tradeoff does it make?

Emphasize that the Week 4 lab will focus especially on linear search, binary
search, trace evidence, and the sorted-data precondition.

**Transition Cue:**

Next week, the question becomes: when is a faster algorithm not actually
better?

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 3 | Data structure shapes algorithm | Clean visual of the same data stored as a list, dictionary, and set, with different arrows showing lookup/update paths | Avoid cluttered code screenshots |
| 17 | Built-in structure comparison | Four simple panels: list/order, tuple/fixed group, dictionary/key-value, set/unique membership | Keep labels large and beginner-friendly |
| 18 | Textbook operation tables as reference | Calm visual showing an operation table being used like a reference map, not a test sheet | Avoid implying students can ignore the textbook |
| 21 | Operation comparison table | Table-centered visual showing operation -> better fit -> why | Do not replace the actual lab table |
| 27 | Matrices without panic | Simple row-column grid connected to data science and graphics icons | Avoid dense equations |
| 36 | Abstract types access pattern | Stack, queue, tree, vector shown as simple access patterns | Keep abstract types visually distinct |
| 40 | Demo evidence | Before/after attendance list and dictionary side by side | Use as support only; demo output remains primary |
| 48 | Week 4 reading preparation | Simple visual showing a sorted list, search target, and precondition checklist | Avoid dense algorithm animations |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 12 min | Use only Slide 2 as the anchor | Discuss student Lab 02 timing examples |
| Textbook Review | 18 min | Treat matrices as preview only | Add examples of each reading category |
| Built-In Data Types | 35 min | Combine tuple and set treatment | Add mini examples for each structure |
| Operation Fit and Complexity | 20 min | Use only Slides 20-21 | Discuss operation tables and AI review |
| Series/DataFrames/Matrices | 20 min | Use Slides 24, 25, 27, 30 only | Add analytics and AI examples |
| Abstract Data Types | 20 min | Use Slides 31, 33, 34, 35 only | Add stack/queue/tree scenarios |
| Demo | 20 min | Show only before/after and comparison table | Discuss operation-by-operation evidence |
| Lab Bridge | 10 min | Combine Slides 42-44 | Walk through README expectations |

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
