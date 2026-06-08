# Week 04 Deck Source - Search and Sort Behavior

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 4 |
| Phase / Unit | Unit 2 - Data Structures: Search, Sort, and Growth |
| Lecture Title | Preconditions Make Algorithms Honest |
| Related Lab | Lab 04 - Search and Sort Behavior |
| Related Demo | Searching Book Titles on a Shelf |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students learn that search and sort algorithms are not just code patterns to
memorize. They are structured procedures that depend on assumptions about the
data, the desired result, and the cost of the operations being performed.

The practical focus for Week 4 is search behavior, especially the difference
between linear search and binary search. Sorting algorithms are introduced as
classic examples of algorithm strategy and performance tradeoffs, and as the
condition that makes binary search valid.

---

# Possible Two-Session Split

The Week 4 reading contains both sorting and searching. The lab is search
focused, but students need enough sorting context to understand why sorted
data changes the search problem.

## Session A - Sorting Ideas and Algorithm Tradeoffs

Recommended slides:

- 1-4: review and opening frame
- 5-9: textbook review and big picture
- 10-20: sorting algorithms and swapping
- 21-25: choosing a sorting approach

Session A target:

Students understand that sorting algorithms arrange data using different
strategies, and that those strategies create different performance behaviors.

## Session B - Searching, Preconditions, Demo, and Lab Transfer

Recommended slides:

- 26-34: search algorithms and performance
- 35-38: practical applications and historical database context
- 39-42: demo
- 43-46: lab bridge
- 47-49: wrap-up

Session B target:

Students can trace linear and binary search, explain why binary search requires
sorted data, and use evidence to justify whether a search approach is valid.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook | Big picture breakdown of four main points | Frames Week 4 as sorting, searching, performance, and application |
| Textbook | Brief definition of Natural Language Processing | Used as a brief context bridge, not a core NLP lesson |
| Textbook | Introducing sorting algorithms | Provides classic algorithm strategy examples |
| Textbook | Bubble sort, merge sort, insertion sort, shell sort, selection sort | Introduces strategy differences and performance tradeoffs |
| Textbook | Standard variable swapping | Shows a small mechanical operation that supports larger algorithms |
| Textbook | Bubble sort optimization | Demonstrates early-stop behavior and algorithm refinement |
| Textbook | Performance analysis of sorting algorithms | Connects sorting strategy to Big-O reasoning |
| Textbook | Choosing a sorting algorithm | Connects algorithm selection to context |
| Textbook | Linear search, binary search, interpolation search | Provides the search behavior vocabulary for Lab 04 |
| Textbook | Performance analysis of search algorithms | Supports comparison of O(n) and O(log n) behavior |
| Textbook | Practical application with primary and foreign keys | Used as a brief application example for lookup and relationship navigation |
| Course artifact | Lab 04 - Search and Sort Behavior | Student application of search tracing and precondition explanation |
| Course artifact | Lab 04 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading introduces search and sort algorithms as classic examples because
they make algorithm behavior visible. Sorting changes the order of data.
Searching tries to locate a target value. Performance analysis asks how much
work those procedures require as the data grows.

The chapter also briefly mentions Natural Language Processing. For this course
week, NLP should be treated as context: many systems that process language must
organize, search, rank, and compare data. Students do not need to learn NLP
algorithms this week.

The most important Week 4 idea is that algorithms have preconditions. Binary
search is efficient because it assumes the data is sorted. If that assumption
is false, the algorithm can make logical decisions that are not trustworthy.

## Reading Key Ideas

- Sorting arranges data into an order.
- Searching locates a target within data.
- Different sorting algorithms use different strategies.
- Different strategies produce different performance behavior.
- Binary search depends on sorted data.
- Preconditions are part of correctness.
- A faster algorithm is not automatically a better algorithm.

## Terms To Carry Forward

| Term | Brief Meaning |
| --- | --- |
| Sorting algorithm | A procedure that arranges data into a defined order |
| Searching algorithm | A procedure that tries to locate a target value |
| Swap | Exchanging the values stored in two variables or positions |
| Linear search | Search that checks values one at a time |
| Binary search | Search that repeatedly cuts a sorted search space in half |
| Interpolation search | Search that estimates likely target position from value distribution |
| Precondition | Something that must be true before an algorithm is valid |
| Primary key | A value that uniquely identifies a record |
| Foreign key | A value that connects one record to another related record |
| NLP | Natural Language Processing; computing work involving human language |

## What We Will Use Today

- sorting as preparation for efficient search
- variable swapping
- bubble, selection, insertion, merge, and shell sort recognition
- linear search
- binary search
- sorted-data precondition
- trace tables as evidence
- primary/foreign key lookup as a brief application context

## What We Will Revisit Later

- deeper recursion in merge sort
- ranking and similarity
- hashing and lookup
- database indexing
- graph and tree traversal
- advanced NLP and data-modeling applications

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain the difference between sorting and searching.
2. Recognize several common sorting algorithms and their basic strategies.
3. Explain why algorithm choice depends on data size, order, and purpose.
4. Trace linear search and binary search at an introductory level.
5. Explain the sorted-data precondition for binary search.
6. Use evidence to show when an algorithm works, fails, or becomes unreliable.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from data structure choice to algorithm assumptions |
| Textbook Review | 5-9 | Core | Curate the broad reading into usable categories |
| Sorting Foundations | 10-20 | Core | Introduce common sorting strategies and swapping |
| Sorting Performance and Choice | 21-25 | Core / Optional | Connect sorting choice to context and Big-O |
| Searching Foundations | 26-34 | Core | Compare linear, binary, and interpolation search |
| Practical Application Context | 35-38 | Core / Optional | Connect search/sort to records, keys, and NLP context |
| Demo Bridge | 39-42 | Core | Show search traces and binary-search precondition failure |
| Lab Bridge | 43-46 | Core | Connect demo to Lab 04 requirements |
| Wrap-Up | 47-49 | Core | Consolidate and assign next action |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 03 Taught Us

**Delivery Category:** Core

**Slide Text:**

In Lab 03, the structure changed the algorithm.

You compared:

- how data was stored
- what operation mattered most
- which structure made the operation clearer
- which structure made the operation easier or faster

**Instructor Notes:**

Use one simple example from Lab 03 if available. The key bridge is that a list,
dictionary, set, or tuple is not just a container. It shapes the operations
available to the algorithm.

Do not linger on every data structure. Use this as a bridge into sorting and
searching.

**Transition Cue:**

Today we ask what must be true before an algorithm can be trusted.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

When is a faster algorithm not actually better?

**Instructor Notes:**

Let students sit with the question briefly. A faster algorithm may be worse if
it is wrong, unclear, too expensive to prepare for, or depends on a condition
that is not true.

The main example today is binary search. It can be very efficient, but only
when the data is sorted.

**Transition Cue:**

This takes us to the idea of preconditions.

---

## Slide 3 - Preconditions Make Algorithms Honest

**Delivery Category:** Core

**Slide Text:**

A precondition is something that must be true before the algorithm is valid.

Examples:

- binary search requires sorted data
- division requires a non-zero divisor
- a username lookup requires comparable username values
- a date sort requires consistent date representation

**Instructor Notes:**

Be explicit that preconditions are not side notes. They are part of the
correctness claim.

If students say "the code runs," ask: "What did it assume?"

**Transition Cue:**

Searching and sorting are useful because they make these assumptions visible.

---

## Slide 4 - Searching And Sorting Work Together

**Delivery Category:** Core

**Slide Text:**

Sorting asks:

- how should the data be ordered?

Searching asks:

- how can we find the target?

The order of the data can change the search strategy.

**Instructor Notes:**

Use a physical shelf analogy. If books are randomly placed, you may have to
check one at a time. If books are alphabetized, you can use the order to make
better decisions.

This is the bridge into why sorting appears before searching in many textbook
treatments.

**Transition Cue:**

Now we will summarize the reading's big picture.

---

# Textbook Review

## Slide 5 - Textbook Review: Four Main Areas

**Delivery Category:** Core

**Slide Text:**

The reading covers:

1. sorting algorithms
2. searching algorithms
3. performance analysis
4. practical applications

It also briefly defines Natural Language Processing.

**Instructor Notes:**

Tell students that not all topics receive equal class time. Sorting and
searching are core. Performance analysis is threaded through both. The NLP and
historical database examples are context, not new major units.

**Transition Cue:**

Start by separating NLP context from this week's core algorithm work.

---

## Slide 6 - Textbook Review: NLP Context

**Delivery Category:** Instructor Reserve

**Slide Text:**

Natural Language Processing is computing work involving human language.

Examples:

- search suggestions
- document classification
- sentiment analysis
- text ranking
- chatbot response processing

This week is not an NLP lesson.

**Instructor Notes:**

This slide prevents confusion if the textbook opens with NLP references.
Explain that NLP systems often need searching, sorting, ranking, indexing, and
comparison. That is why the context appears.

Do not turn this into a full NLP lecture. The class will return to AI/data
bridges later.

**Transition Cue:**

The core algorithms this week begin with sorting.

---

## Slide 7 - Textbook Review: Sorting

**Delivery Category:** Core

**Slide Text:**

Sorting algorithms arrange values into a defined order.

The reading introduces:

- bubble sort
- selection sort
- insertion sort
- shell sort
- merge sort

**Instructor Notes:**

Tell students that they do not need to memorize every line of every sort
implementation this week. They should learn the strategy behind each sort and
notice why performance differs.

**Transition Cue:**

Sorting examples also give us another place to practice Big-O reasoning.

---

## Slide 8 - Textbook Review: Searching

**Delivery Category:** Core

**Slide Text:**

Searching algorithms try to find a target value.

The reading introduces:

- linear search
- binary search
- interpolation search

**Instructor Notes:**

Make clear that Lab 04 emphasizes linear and binary search. Interpolation
search is worth recognizing, but it will not be the main hands-on focus.

**Transition Cue:**

The reading also shows that performance analysis is not a separate chapter box.

---

## Slide 9 - Textbook Review: Performance Is Interspersed

**Delivery Category:** Core

**Slide Text:**

The reading discusses performance throughout the chapter.

For each algorithm, ask:

- What must be true before it works?
- How much work might it do?
- How does it behave as data grows?
- What tradeoff does it make?

**Instructor Notes:**

This slide gives students a stable reading pattern. Instead of treating every
algorithm as a brand-new topic, they can ask the same questions repeatedly.

**Transition Cue:**

Before the sorting algorithms, we need one small mechanical idea: swapping.

---

# Sorting Foundations

## Slide 10 - Variable Swapping

**Delivery Category:** Core

**Slide Text:**

Many sorting algorithms need to swap two values.

Conceptually:

1. remember one value
2. move the other value
3. put the remembered value into the open spot

**Instructor Notes:**

Do not make this too formal. Show a quick two-card example or two list
positions. The purpose is to make later sorting steps less mysterious.

If writing Python, you can mention that Python supports direct tuple-style
swapping, but students should still understand the concept.

**Transition Cue:**

The first sorting algorithm is intentionally simple and visible.

---

## Slide 11 - Bubble Sort

**Delivery Category:** Core

**Slide Text:**

Bubble sort repeatedly compares neighboring values.

If two neighbors are out of order:

- swap them
- continue across the list
- repeat passes until the list is sorted

**Instructor Notes:**

Use a tiny list such as `[5, 2, 4, 1]`. Walk through one pass only unless the
group needs more.

The important image is larger values "bubbling" toward the end after repeated
neighbor comparisons.

**Transition Cue:**

Bubble sort is easy to understand, but easy does not mean efficient.

---

## Slide 12 - Bubble Sort Performance

**Delivery Category:** Core

**Slide Text:**

Bubble sort usually performs poorly on larger lists.

Why?

- it makes repeated passes
- it compares neighboring values
- it may keep checking even after little changes

Common growth label: O(n2)

**Instructor Notes:**

Say "n squared" out loud, but keep the explanation concrete: as the list grows,
the repeated passes create a lot of comparisons.

Do not require students to prove the formula. Connect it to the repeated nested
work pattern from Week 2.

**Transition Cue:**

The textbook may mention an optimization for bubble sort.

---

## Slide 13 - Bubble Sort Optimization

**Delivery Category:** Core / Optional

**Slide Text:**

Bubble sort can stop early if a full pass makes no swaps.

That means:

- the list is already sorted
- another pass is unnecessary
- the algorithm can avoid wasted work

**Instructor Notes:**

This is a good example of refinement. The core idea stays the same, but the
algorithm gains a stopping condition.

Connect this to prior labs: evidence can reveal unnecessary work.

**Transition Cue:**

Another simple sorting strategy is selection.

---

## Slide 14 - Selection Sort

**Delivery Category:** Core

**Slide Text:**

Selection sort repeatedly selects the next smallest value.

Basic pattern:

- find the smallest remaining value
- place it in the next sorted position
- repeat until finished

**Instructor Notes:**

Use cards or a small list. The key difference from bubble sort is that
selection sort looks for the next value to place, instead of repeatedly
swapping neighbors.

**Transition Cue:**

Selection sort is organized, but it still scans repeatedly.

---

## Slide 15 - Selection Sort Performance

**Delivery Category:** Core

**Slide Text:**

Selection sort repeatedly searches the remaining unsorted values.

Common growth label: O(n2)

It may use fewer swaps than bubble sort, but it still performs many
comparisons.

**Instructor Notes:**

This is a good place to separate "number of swaps" from "number of
comparisons." Different operations matter in different contexts.

**Transition Cue:**

Insertion sort uses a different mental model.

---

## Slide 16 - Insertion Sort

**Delivery Category:** Core

**Slide Text:**

Insertion sort builds a sorted section one value at a time.

Basic pattern:

- take the next value
- find where it belongs in the sorted section
- shift values if needed
- insert it

**Instructor Notes:**

Use the playing-card analogy if helpful: people often sort a hand of cards by
inserting each new card into the correct position.

**Transition Cue:**

Insertion sort can be reasonable when the data is already close to sorted.

---

## Slide 17 - Insertion Sort Performance

**Delivery Category:** Core

**Slide Text:**

Insertion sort depends heavily on existing order.

It can be:

- efficient for small lists
- efficient for nearly sorted data
- poor for badly unordered larger lists

Common worst-case growth label: O(n2)

**Instructor Notes:**

This slide helps students avoid memorized rankings. Algorithm choice depends
on context.

The phrase "worst case" matters here. Nearly sorted data can behave very
differently from reversed data.

**Transition Cue:**

Shell sort modifies the insertion idea.

---

## Slide 18 - Shell Sort

**Delivery Category:** Instructor Reserve

**Slide Text:**

Shell sort compares values that are farther apart first.

Then it gradually reduces the gap.

Purpose:

- move values closer to their final position sooner
- finish with smaller local adjustments

**Instructor Notes:**

Keep this brief unless the group is ready. Shell sort can be difficult to
visualize on a first pass.

The important idea is not implementation mastery. It is recognition that a
strategy can be improved by changing how comparisons are organized.

**Transition Cue:**

Merge sort uses a more structured divide-and-combine strategy.

---

## Slide 19 - Merge Sort

**Delivery Category:** Core

**Slide Text:**

Merge sort divides, sorts, and combines.

Basic pattern:

- split the data
- sort smaller pieces
- merge sorted pieces back together

Common growth label: O(n log n)

**Instructor Notes:**

This is the cleanest bridge to recursion, but do not teach recursion in full
yet. Say that the course will return to recursive thinking later.

Use the phrase "divide and combine" as the plain-English anchor.

**Transition Cue:**

Now compare these sorting strategies without turning the lesson into a memory
test.

---

## Slide 20 - Sorting Strategy Comparison

**Delivery Category:** Core

**Slide Text:**

| Algorithm | Strategy | Beginner Takeaway |
| --- | --- | --- |
| Bubble | compare neighbors | visible but inefficient |
| Selection | choose next smallest | organized repeated scanning |
| Insertion | insert into sorted section | useful for small or nearly sorted data |
| Shell | compare by gaps | refined insertion idea |
| Merge | divide and combine | stronger growth behavior |

**Instructor Notes:**

Use this as a strategy table, not a memorization chart. Students should be able
to say what the algorithm is trying to do.

**Transition Cue:**

Choosing a sort depends on the context.

---

# Sorting Performance and Choice

## Slide 21 - Choosing A Sorting Algorithm

**Delivery Category:** Core

**Slide Text:**

Choosing a sort depends on:

- data size
- current order
- memory limits
- need for simplicity
- need for predictable performance
- whether built-in sorting is acceptable

**Instructor Notes:**

Mention that professional developers often use built-in library sorting, but
understanding sorting algorithms still matters. It helps developers reason
about performance, assumptions, and data preparation.

**Transition Cue:**

The simplest algorithm is sometimes the right teaching tool, not the right
production choice.

---

## Slide 22 - Simple Does Not Always Mean Wrong

**Delivery Category:** Core

**Slide Text:**

A simple algorithm can be appropriate when:

- the data is small
- clarity matters most
- the cost is acceptable
- the goal is learning or verification

But simple should still be explained honestly.

**Instructor Notes:**

This is important for beginner confidence. Do not imply that bubble sort or
linear search are "stupid." They are understandable and sometimes sufficient.

The honest answer is context-dependent.

**Transition Cue:**

The danger is claiming performance without evidence or assumptions.

---

## Slide 23 - Performance Claims Need Conditions

**Delivery Category:** Core

**Slide Text:**

Avoid claims like:

- "This is faster."
- "This is better."
- "This always works."

Use claims like:

- "This is faster when..."
- "This is valid if..."
- "This performs better for..."

**Instructor Notes:**

This slide supports rubric-aligned communication. Students should learn to add
conditions to technical claims.

**Transition Cue:**

Sorting matters because it can prepare data for a different search strategy.

---

## Slide 24 - Sorting As Preparation

**Delivery Category:** Core

**Slide Text:**

Sorting may be useful before searching when:

- many searches will happen
- the data will be reused
- the search strategy depends on order
- the sorting cost is worth the later benefit

**Instructor Notes:**

This is a key decision point. Sorting just to do one search may not be worth
it. Sorting once before many searches may be useful.

This prepares students for binary search without overselling it.

**Transition Cue:**

Now move from arranging data to finding a target.

---

## Slide 25 - From Sort To Search

**Delivery Category:** Core

**Slide Text:**

Sorting changes what search can assume.

Unsorted data:

- linear search is safe
- binary search is not trustworthy

Sorted data:

- linear search still works
- binary search can use the order

**Instructor Notes:**

This slide is the bridge into Lab 04. Stress that linear search works on sorted
data too. It just may not use the extra information.

**Transition Cue:**

Start with the search that makes the fewest assumptions.

---

# Searching Foundations

## Slide 26 - Linear Search

**Delivery Category:** Core

**Slide Text:**

Linear search checks values one at a time.

It asks:

- is this the target?
- if not, check the next value
- stop when found or when the list ends

**Instructor Notes:**

Use a small list and target near the end. Students should see that the
algorithm is simple and reliable, but may do a lot of work.

**Transition Cue:**

Linear search is reliable because it does not need sorted data.

---

## Slide 27 - Linear Search Performance

**Delivery Category:** Core

**Slide Text:**

Linear search:

- best case: target is first
- worst case: target is last or missing
- common growth label: O(n)

It may check every value.

**Instructor Notes:**

Tie this back to Week 2. The amount of work can grow with the number of values.

Emphasize that O(n) does not mean bad. It means the work grows roughly with
the input size.

**Transition Cue:**

Binary search uses order to reduce the search space.

---

## Slide 28 - Binary Search

**Delivery Category:** Core

**Slide Text:**

Binary search repeatedly checks the middle.

If the middle value is:

- the target: stop
- too low: search the upper half
- too high: search the lower half

**Instructor Notes:**

Point to low, high, and mid. Students must understand those three variables for
the lab trace.

Use a sorted list and ask which half can be ignored after each comparison.

**Transition Cue:**

This only works because the list is sorted.

---

## Slide 29 - The Sorted-Data Precondition

**Delivery Category:** Core

**Slide Text:**

Binary search requires sorted data.

If the data is not sorted:

- "too low" may not mean the target is above
- "too high" may not mean the target is below
- the algorithm can discard the wrong half

**Instructor Notes:**

This is the central Week 4 slide. Say plainly: binary search on unsorted data
is not just less efficient. It is logically unreliable.

**Transition Cue:**

The trace table makes that logic visible.

---

## Slide 30 - Binary Search Trace

**Delivery Category:** Core

**Slide Text:**

Trace the search using:

| Step | Low | High | Mid | Mid Value | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

**Instructor Notes:**

Explain each column. Low and high are the current search boundaries. Mid is the
position being checked. Decision explains which half remains possible.

If students can fill in this table, they are showing more than code execution.
They are showing algorithm understanding.

**Transition Cue:**

The textbook also introduces interpolation search.

---

## Slide 31 - Interpolation Search

**Delivery Category:** Instructor Reserve

**Slide Text:**

Interpolation search estimates where the target may be.

It works best when:

- data is sorted
- values are evenly distributed
- the target position can be estimated

**Instructor Notes:**

Keep this brief. Compare it to looking for a word in a dictionary by estimating
where it might appear, not always opening exactly in the middle.

Do not make this a lab requirement unless the group is advanced.

**Transition Cue:**

Searching algorithms have different assumptions.

---

## Slide 32 - Search Strategy Comparison

**Delivery Category:** Core

**Slide Text:**

| Search | Needs Sorted Data? | Basic Idea | Common Growth |
| --- | --- | --- | --- |
| Linear | no | check one at a time | O(n) |
| Binary | yes | cut search space in half | O(log n) |
| Interpolation | yes, plus distribution assumptions | estimate likely position | varies |

**Instructor Notes:**

This table is a good place to reinforce that "best" depends on requirements
and assumptions.

**Transition Cue:**

Now connect this back to evidence.

---

## Slide 33 - Evidence Before Claims

**Delivery Category:** Core

**Slide Text:**

For search algorithms, evidence can include:

- test cases
- found and not-found results
- trace tables
- sorted and unsorted comparisons
- explanation of preconditions

**Instructor Notes:**

Students may be tempted to submit only working code. This slide explains why
the lab requires trace evidence and precondition explanation.

**Transition Cue:**

AI can help review search code, but it cannot replace the student's
explanation.

---

## Slide 34 - AI-Assisted Search Review

**Delivery Category:** Core

**Slide Text:**

Useful AI prompt:

```text
Review this linear search and binary search code.
Identify any preconditions.
Check for off-by-one risks.
Explain whether each test case proves the behavior I claim.
Do not rewrite the code unless I ask.
```

**Instructor Notes:**

This is an AI-assisted review pattern, not a first-step coding prompt. Students
should have their own attempt and trace before using it.

Emphasize "Do not rewrite" because the goal is explanation and verification.

**Transition Cue:**

The textbook's application example shows how search ideas appear in real data.

---

# Practical Application Context

## Slide 35 - Records And Keys

**Delivery Category:** Core / Optional

**Slide Text:**

Real systems often search records by keys.

Examples:

- product ID
- student ID
- ticket number
- course code
- username

**Instructor Notes:**

Connect this to the lab suggestions. A key is a value used to identify or find
something.

Keep it simple. This is not a database design lecture.

**Transition Cue:**

The textbook uses primary and foreign keys as a brief example.

---

## Slide 36 - Primary And Foreign Keys

**Delivery Category:** Core / Optional

**Slide Text:**

Primary key:

- uniquely identifies one record

Foreign key:

- connects a record to another related record

Search and sort help systems find and connect records.

**Instructor Notes:**

Use a tiny example:

- `student_id` identifies a student
- `student_id` in an enrollment record connects that enrollment back to the
  student

Do not overbuild this. The textbook treatment is brief and conceptual.

**Transition Cue:**

The historical database example is about applying search/sort thinking, not
writing database code today.

---

## Slide 37 - Historical Database Example

**Delivery Category:** Instructor Reserve

**Slide Text:**

The reading's historical database example asks:

- what identifies a record?
- what connects records?
- what should be searched?
- what should be sorted?
- what lookup pattern matters most?

**Instructor Notes:**

This keeps the application grounded without adding a new coding requirement.
If time is short, summarize verbally instead of building a full slide from it.

**Transition Cue:**

These same ideas appear in language systems too.

---

## Slide 38 - NLP Connection, Briefly

**Delivery Category:** Instructor Reserve

**Slide Text:**

NLP systems may use search and sort ideas to:

- find matching terms
- rank documents
- sort likely responses
- retrieve related records
- compare text features

This is context, not today's coding target.

**Instructor Notes:**

This slide helps future AI/data alignment. Keep it short and practical.

Students should leave seeing why classic algorithms still matter in modern
systems.

**Transition Cue:**

Now show search behavior with a small visible demo.

---

# Demo Bridge

## Slide 39 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo: searching book titles on a shelf.

We will compare:

- linear search on a list
- binary search on a sorted list
- binary search on an unsorted list

**Instructor Notes:**

Use the existing Lab 04 demo. The demo scenario is book titles so students do
not receive one of the suggested lab scenarios as a near-complete answer.

**Transition Cue:**

First, show the data.

---

## Slide 40 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

The demo produces:

- a linear search trace
- a binary search trace on sorted data
- a binary search trace on unsorted data
- a sorted-vs-unsorted summary

**Instructor Notes:**

Do not rush the trace. Ask students what low, high, and mid mean before
running the binary search explanation.

The point is not that binary search "fails every time" on unsorted data. The
point is that it is not trustworthy because its reasoning no longer holds.

**Transition Cue:**

Watch the decisions, not just the final result.

---

## Slide 41 - Demo Key Question

**Delivery Category:** Core

**Slide Text:**

Ask after each search:

- What did the algorithm check?
- What did it assume?
- What did it ignore?
- Was that decision valid?

**Instructor Notes:**

This creates the habit students need for the lab. They should explain the
algorithm's behavior, not merely report the output.

**Transition Cue:**

The explanation should name the precondition.

---

## Slide 42 - Demo Explanation Pattern

**Delivery Category:** Core

**Slide Text:**

Example explanation:

> Binary search is valid on the sorted list because each comparison tells us
> which half can be ignored. On the unsorted list, that decision is unreliable
> because the values are not arranged in order.

**Instructor Notes:**

This is the sentence pattern students need: algorithm, condition, decision,
reason.

Encourage students to use their own words, but the same logical structure.

**Transition Cue:**

Now transfer the demo pattern to Lab 04.

---

# Lab Bridge

## Slide 43 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 04, you will use a different data set.

You must show:

- linear search
- binary search
- found and not-found tests
- binary search attempted on unsorted data
- trace evidence
- precondition explanation

**Instructor Notes:**

Name the allowed scenario examples only briefly. The demo used books; the lab
should use something else such as product IDs, usernames, ticket numbers,
course codes, or attendee names.

**Transition Cue:**

The trace table is part of the submission, not optional decoration.

---

## Slide 44 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should include:

- test case table
- trace table
- sorted-data precondition explanation
- comparison of linear and binary search
- AI-use note, if used

**Instructor Notes:**

Remind students that code and explanation belong together in the GitHub
submission. The README is where they make the algorithm visible.

**Transition Cue:**

Clarify what AI may and may not do here.

---

## Slide 45 - AI Use In Lab 04

**Delivery Category:** Core

**Slide Text:**

Manual first:

- write or trace your own attempt
- create your test cases
- identify the precondition

AI-assisted after:

- review logic
- check edge cases
- explain a confusing trace
- suggest tests

**Instructor Notes:**

If AI writes or revises code, students still own the explanation. They must be
able to explain low, high, mid, found, not found, and the sorted-data
precondition.

**Transition Cue:**

Now define what successful work looks like.

---

## Slide 46 - Lab 04 Success Check

**Delivery Category:** Core

**Slide Text:**

Successful Lab 04 work:

- searches correctly
- includes required test cases
- traces at least one search
- explains sorted-data requirements
- avoids claiming binary search is always better

**Instructor Notes:**

Make this practical. Students should compare this slide to their README before
submitting.

**Transition Cue:**

Wrap the week around the main lesson.

---

# Wrap-Up

## Slide 47 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Search and sort algorithms teach a larger lesson:

- algorithms depend on data conditions
- performance depends on context
- correctness includes assumptions
- evidence makes reasoning visible

**Instructor Notes:**

This is the conceptual close. Sorting and searching are specific topics, but
preconditions and evidence are transferable.

**Transition Cue:**

Now make the immediate next action concrete.

---

## Slide 48 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 04:

- choose a data set
- implement or simulate linear search
- implement or simulate binary search
- create required tests
- build a trace table
- explain the sorted-data precondition

**Instructor Notes:**

Remind students that binary search on unsorted data is intentionally included
to reveal the precondition. It is not a trick.

**Transition Cue:**

Prepare students for the next reading once Week 5 reading details are assigned.

---

## Slide 49 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

For next week, read for strategy choice.

Focus on:

- correctness, performance, and scalability
- functional and non-functional requirements
- divide and conquer
- dynamic programming
- greedy strategies
- PageRank and linear programming as examples

Skim the P, NP-Hard, and NP-Complete section for recognition only.

**Instructor Notes:**

This slide prepares students for the Week 5 reading. Emphasize that Chapter 4
contains some theory-heavy language. Students should not panic over formal
definitions. They should read for the main idea: some problems are harder than
others, and strategy choice depends on correctness, performance, and
scalability.

Tell students to treat PageRank and linear programming as examples of strategy
applied in larger contexts, not as implementation requirements for Week 5.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 3 | Preconditions | Clean visual of a checklist before an algorithm runs, with "sorted data" highlighted | Avoid legal-contract imagery |
| 10 | Variable swap | Two labeled boxes exchanging values with a temporary holding space | Keep it simple; no dense code |
| 20 | Sorting comparison | Five small panels showing bubble, selection, insertion, shell, and merge as different movement patterns | Avoid making exact algorithm animation too detailed |
| 24 | Sorting as preparation | Sorted shelf or ordered index leading to faster repeated lookup | Do not imply sorting is always worth it |
| 30 | Binary trace | Low/high/mid pointers over a sorted list | Make pointers clear and readable |
| 36 | Primary and foreign keys | Two simple tables connected by a matching ID | Avoid database schema complexity |
| 40 | Demo evidence | Linear trace and binary trace side by side | Use as support only; demo output remains primary |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 12 min | Use only Slides 2-3 | Discuss Lab 03 representation examples |
| Textbook Review | 15 min | Skip NLP slide or summarize verbally | Add student examples of search/sort systems |
| Sorting Foundations | 35 min | Compare strategies only with Slide 20 | Walk through one bubble or insertion pass |
| Sorting Performance and Choice | 20 min | Use Slides 23-25 only | Discuss sorting once for many searches |
| Searching Foundations | 35 min | Keep interpolation as verbal note | Trace binary search manually on board |
| Practical Application Context | 10 min | Skip Slides 37-38 | Add a primary/foreign key lookup example |
| Demo | 20 min | Run only one sorted and one unsorted binary trace | Ask students to predict each decision |
| Lab Bridge | 10 min | Combine Slides 43-46 | Walk through README requirements |

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
