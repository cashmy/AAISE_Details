# Week 02 Deck Source - Growth and Big-O Intuition

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 2 |
| Phase / Unit | Unit 1 - Algorithmic Foundations |
| Lecture Title | When Working Code Starts to Slow Down |
| Related Lab | Lab 02 - Growth and Big-O Intuition |
| Related Demo | Lookup Growth Comparison |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students move from asking whether an algorithm works to asking how the
algorithm behaves as input size grows.

This lesson introduces performance analysis, space and time complexity, Big-O
growth vocabulary, best/worst/average cases, algorithm selection, validation,
and explainability. The goal is introductory reasoning, not advanced
mathematical proof.

---

# Possible Two-Session Split

The Week 2 reading is dense. This deck can be taught as one longer lecture with
breaks, but it may be cleaner as two shorter lecture segments.

## Session A - Growth Foundations

Recommended slides:

- 1-4: review and opening frame
- 5-10: textbook review and performance analysis
- 11-18: space/time complexity and scaling
- 19-29: Big-O notation and common growth classes

Session A target:

Students understand that Big-O describes growth behavior as input size changes.

## Session B - Applying Growth Reasoning

Recommended slides:

- 30-36: estimating performance, selecting, validating, explaining
- 37-40: demo
- 41-43: AI-assisted complexity review
- 44-46: lab bridge
- 47-50: wrap-up, next step, and next reading preparation

Session B target:

Students use timing evidence and introductory Big-O vocabulary to compare two
approaches responsibly, including AI-assisted review as a professional support
technique after their own reasoning and evidence collection.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook | Performance analysis from a complexity point of view | Frames correctness, understandability, and efficiency |
| Textbook | Key features: correct, understandable, efficient | Defines quality beyond "the code runs" |
| Textbook | Types of analysis: space and time | Separates memory use from execution time |
| Textbook | Space complexity: converging, diverging, and flat | Introduces memory-growth behavior conceptually |
| Textbook | Time complexity: scale, CPU, GPU, memory, larger datasets | Connects algorithm behavior to computing resources |
| Textbook | Estimating performance: best, worst, average case | Shows that one timing result is not the full story |
| Textbook | Big-O notation and formula | Introduces formal notation as a compact growth label |
| Textbook | Five complexity rules | Translates structure into growth estimates |
| Textbook | O(1), O(n), O(n2), O(log n) | Provides the main Week 2 growth vocabulary |
| Textbook | Selecting an algorithm | Connects performance analysis to design choice |
| Textbook | Validating exact, approximate, and randomized algorithms | Introduces validation expectations by algorithm type |
| Textbook | Explainability | Connects algorithm choice to human explanation |
| Textbook | Chapter 1 summary | Consolidates foundation concepts |
| Course artifact | Lab 02 - Growth and Big-O Intuition | Student application of timing and growth explanation |
| Course artifact | Lab 02 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading expands the idea of algorithm quality. Last week, students focused
on precision and correctness. This week, the reading adds performance analysis:
how much memory an algorithm may use, how much time it may require, and how
that behavior changes as input size grows.

The important shift is that a solution can be correct but still be a poor fit
for larger data. Performance analysis helps students compare approaches without
relying only on intuition or one small example.

The reading also introduces Big-O notation. In this course, Big-O will be used
as a practical vocabulary for growth behavior. Students should understand the
meaning before worrying about formal mathematical notation.

## Reading Key Ideas

- A good algorithm should be correct, understandable, and efficient enough for
  its context.
- Performance analysis includes both space and time.
- Space complexity asks how memory use changes.
- Time complexity asks how work changes as input grows.
- Big-O is a compact way to describe growth behavior.
- Timing evidence is useful, but it is not the same as formal complexity
  analysis.
- Algorithm selection depends on correctness, performance, data size,
  explainability, and validation needs.

## Terms To Carry Forward

| Term | Brief Meaning |
| --- | --- |
| Performance analysis | Studying how an algorithm behaves as resources and input size change |
| Space complexity | How memory use changes as input grows |
| Time complexity | How the amount of work or time changes as input grows |
| Input size | The amount of data the algorithm processes |
| Big-O | A notation for describing growth behavior |
| Best case | The easiest or fastest likely situation for an algorithm |
| Worst case | The hardest or slowest likely situation for an algorithm |
| Average case | Expected behavior across typical inputs |
| Exact algorithm | Designed to produce an exact correct result |
| Approximate algorithm | Designed to produce a good-enough result under constraints |
| Randomized algorithm | Uses randomness as part of its process |
| Explainability | Ability to describe how or why an algorithm produced a result |

## What We Will Use Today

- correct, understandable, efficient
- space and time analysis
- input size and growth behavior
- Big-O vocabulary
- best, worst, and average case
- timing evidence and its limits
- algorithm selection and explanation

## What We Will Revisit Later

- formal mathematical notation
- recursion-based complexity
- nested recursion
- memory optimization
- GPU/CPU details
- randomized and approximate algorithms in deeper AI/data contexts

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain why correctness alone is not enough to evaluate an algorithm.
2. Distinguish time complexity from space complexity at an introductory level.
3. Use O(1), O(log n), O(n), and O(n2) as practical growth labels.
4. Explain why timing evidence is useful but noisy.
5. Compare two approaches using timing evidence and cautious growth language.
6. Identify a basic limitation in a timing experiment.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from correctness to growth |
| Textbook Review | 5-10 | Core | Summarize assigned reading concepts |
| Performance Analysis Foundations | 11-18 | Core | Explain time, space, scale, resources |
| Big-O Vocabulary | 19-29 | Core / Optional | Introduce notation, rules, and common classes |
| Estimating and Selecting | 30-34 | Core | Connect cases, selection, and validation |
| Explainability | 35-36 | Core | Explain why students must justify algorithm choices |
| Demo Bridge | 37-40 | Core | Compare list lookup and set lookup |
| AI-Assisted Complexity Review | 41-43 | Core | Model AI as explanation and critique support |
| Lab Bridge | 44-46 | Core | Connect demo to Lab 02 |
| Wrap-Up | 47-50 | Core | Consolidate, assign next action, and prepare next reading |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 01 Taught Us

**Delivery Category:** Core

**Slide Text:**

Last week, we focused on:

- precise rules
- expected results
- actual results
- edge cases
- revision based on evidence

**Instructor Notes:**

Use one Lab 01 pattern or success example. Do not spend long re-teaching Lab
01. The goal is to remind students that evidence helped them decide whether a
small algorithm behaved as expected.

Point out that Week 1's evidence mostly answered: "Does this produce the
expected result?"

**Transition Cue:**

This week keeps the evidence habit but changes the question from correctness to
growth behavior.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

What happens when the amount of data gets larger?

**Instructor Notes:**

Make this the anchor question. Students should leave understanding that an
algorithm can work for five items and still become a poor fit for five thousand
or five million items.

**Transition Cue:**

That question is the beginning of performance analysis.

---

## Slide 3 - From Works To Scales

**Delivery Category:** Core

**Slide Text:**

Correctness asks:

- Does the algorithm produce the expected result?

Growth asks:

- How does the work change as input grows?

**Instructor Notes:**

Say clearly that correctness still matters. A fast wrong answer is not a good
algorithm. Week 2 adds another lens, not a replacement for Week 1.

**Transition Cue:**

The reading describes algorithm quality using more than one feature.

---

## Slide 4 - Success Today

**Delivery Category:** Core

**Slide Text:**

By the end of today, you should be able to:

- compare two approaches
- collect timing evidence
- describe growth cautiously
- use basic Big-O vocabulary
- identify a limitation of your evidence

**Instructor Notes:**

Emphasize "cautiously." Students should not overclaim from one timing table.
The goal is responsible introductory explanation.

**Transition Cue:**

Start with the reading's view of what makes an algorithm good.

---

# Textbook Review

## Slide 5 - Textbook Review: Algorithm Quality

**Delivery Category:** Core

**Slide Text:**

The reading describes strong algorithms as:

- correct
- understandable
- efficient

**Instructor Notes:**

Connect this to student work. A solution that works but cannot be explained is
hard to trust. A solution that is understandable but extremely slow may not fit
larger data. A solution that is fast but wrong fails the main purpose.

**Transition Cue:**

Performance analysis helps us reason about the efficiency part without
forgetting correctness and understandability.

---

## Slide 6 - Textbook Review: Performance Analysis

**Delivery Category:** Core

**Slide Text:**

Performance analysis asks:

- How much time might this take?
- How much memory might this use?
- What happens as input size grows?

**Instructor Notes:**

Keep this practical. Students do not need formal proof yet. They need to see
that algorithms consume resources, and those resources may change when the
input changes.

**Transition Cue:**

The reading separates performance analysis into two broad types: space and
time.

---

## Slide 7 - Textbook Review: Space And Time

**Delivery Category:** Core

**Slide Text:**

Two common analysis types:

- Space analysis: memory growth
- Time analysis: work or runtime growth

**Instructor Notes:**

Use a simple contrast. A dictionary may use extra memory but reduce repeated
lookup work. A list may use less structure but require more scanning. This is a
tradeoff students will keep seeing.

**Transition Cue:**

Start with space because memory growth is easier to visualize.

---

## Slide 8 - Textbook Review: Space Complexity

**Delivery Category:** Core

**Slide Text:**

Space complexity asks how memory use changes.

Patterns can be:

- flat
- converging
- diverging

**Instructor Notes:**

Use student-friendly language:

- Flat: memory stays about the same.
- Converging: memory growth slows or approaches a limit.
- Diverging: memory keeps increasing as input grows.

Do not spend long on the exact terminology if students are new to it. The main
point is that memory use can have a growth pattern too.

**Transition Cue:**

Time complexity asks a similar growth question, but about work.

---

## Slide 9 - Textbook Review: Time Complexity

**Delivery Category:** Core

**Slide Text:**

Time complexity asks:

- Can this scale?
- What work does the algorithm repeat?
- What happens with larger datasets?
- What resources are involved?

**Instructor Notes:**

Mention CPU, GPU, and memory as resource terms from the reading, but do not
turn this into a hardware lecture. For this week, CPU/GPU/memory are reminders
that algorithms run on real machines with real limits.

**Transition Cue:**

To reason about time, we need to identify the input size.

---

## Slide 10 - Textbook Review: Input Size

**Delivery Category:** Core

**Slide Text:**

Input size is the amount of data the algorithm works on.

Examples:

- number of list items
- number of records
- number of characters
- number of graph nodes

**Instructor Notes:**

Use the demo preview: in the lookup demo, input size is the number of items in
the collection. In Lab 02, each student comparison will need to define what
input size means for that task.

**Transition Cue:**

Once input size is named, we can ask how the work changes.

---

# Performance Analysis Foundations

## Slide 11 - Growth Pattern

**Delivery Category:** Core

**Slide Text:**

Growth pattern means:

- how work changes
- as input size changes

Small inputs can hide the pattern.

**Instructor Notes:**

Use a concrete phrase: "Two approaches can both feel instant with 10 items.
The difference may become visible with 10,000 items."

**Transition Cue:**

This is why one small example is not enough evidence for performance.

---

## Slide 12 - Timing Is Evidence

**Delivery Category:** Core

**Slide Text:**

Timing can show:

- what happened in a run
- on this machine
- with this code
- under these conditions

**Instructor Notes:**

Make timing useful but limited. Timing is not useless; it is evidence. But it
is evidence from a specific setup, not a universal law.

**Transition Cue:**

Because timing depends on conditions, timing results can be noisy.

---

## Slide 13 - Timing Can Be Noisy

**Delivery Category:** Core

**Slide Text:**

Timing can vary because of:

- background activity
- hardware differences
- setup code
- number of trials
- input construction

**Instructor Notes:**

Warn students not to panic if their exact numbers do not match the demo. Focus
them on the pattern across increasing input sizes, not one decimal value.

**Transition Cue:**

Big-O gives us language for the pattern behind the timing.

---

## Slide 14 - Big-O Is Pattern Language

**Delivery Category:** Core

**Slide Text:**

Big-O describes growth behavior.

It does not mean:

- exact seconds
- one timing result
- every machine behaves identically

**Instructor Notes:**

This is the central conceptual safety rail. Students should not confuse
measured runtime with Big-O. Timing can support a growth claim, but Big-O
describes how work tends to grow as input size changes.

**Transition Cue:**

Before naming Big-O classes, show what "work" can mean.

---

## Slide 15 - What Counts As Work?

**Delivery Category:** Core

**Slide Text:**

Work may include:

- comparisons
- loop iterations
- lookups
- calculations
- recursive calls
- memory writes

**Instructor Notes:**

Use the demo example: manual list lookup may compare the target to many values.
Set membership avoids walking through the list in the same visible way.

**Transition Cue:**

When work grows with input size, we start naming the growth shape.

---

## Slide 16 - Space And Time Tradeoff

**Delivery Category:** Core

**Slide Text:**

Sometimes an approach uses more memory to save time.

Example:

- list scanning: less structure, more repeated checking
- set lookup: extra structure, faster membership checks

**Instructor Notes:**

This is a preview of data structure choice. Do not fully teach sets yet. The
point is that algorithm selection often involves tradeoffs rather than one
perfect answer.

**Transition Cue:**

The reading also asks us to think about computing resources.

---

## Slide 17 - CPU, GPU, And Memory

**Delivery Category:** Optional Deepening

**Slide Text:**

Algorithms use machine resources:

- CPU: general processing
- GPU: many parallel operations
- memory: stored data and working space

**Instructor Notes:**

Keep this brief unless students ask. The purpose is to connect the reading to
real computing resources, not to teach computer architecture.

**Transition Cue:**

For Lab 02, we will focus mainly on CPU time and memory intuition.

---

## Slide 18 - Week 2 Practical Rule

**Delivery Category:** Core

**Slide Text:**

Ask:

- What is the input size?
- What work repeats?
- Does memory grow?
- Does timing suggest a pattern?

**Instructor Notes:**

This slide is the practical bridge into Big-O. It gives students questions they
can use before they fully master notation.

**Transition Cue:**

Now attach names to common growth patterns.

---

# Big-O Vocabulary

## Slide 19 - Big-O Notation

**Delivery Category:** Core

**Slide Text:**

Big-O gives a label to growth behavior.

Examples:

- O(1)
- O(log n)
- O(n)
- O(n2)

**Instructor Notes:**

The textbook may show mathematical notation here. Acknowledge the notation, but
translate immediately: `n` means input size, and the expression describes how
work grows as `n` grows.

Use `O(n2)` in slide text for ASCII compatibility, but say "O of n squared"
out loud.

**Transition Cue:**

Start with the simplest growth class: constant time.

---

## Slide 20 - Constant Time: O(1)

**Delivery Category:** Core

**Slide Text:**

O(1) means the work stays about the same as input grows.

Example idea:

- get one known item
- check one stored value
- return a cached count

**Instructor Notes:**

Be careful: O(1) does not mean zero time or always instant. It means the work
does not grow in proportion to the input size.

**Transition Cue:**

Many beginner algorithms are not constant; they look through data.

---

## Slide 21 - Linear Time: O(n)

**Delivery Category:** Core

**Slide Text:**

O(n) means work grows with the input size.

Example idea:

- look at each item once
- count matching records
- find a maximum with one pass

**Instructor Notes:**

Use a simple phrase: if the input doubles, the amount of work roughly doubles.
Do not overpromise exact timing; the idea is growth shape.

**Transition Cue:**

If an algorithm repeatedly loops through data inside another loop, growth can
be much steeper.

---

## Slide 22 - Quadratic Time: O(n2)

**Delivery Category:** Core

**Slide Text:**

O(n2) often appears when work is nested.

Example idea:

- compare each item to every other item
- check many possible pairs
- nested loops over the same input

**Instructor Notes:**

Say "O of n squared." Explain that if the input doubles, the work may grow by
much more than double. This is why small inputs can hide trouble.

**Transition Cue:**

Some algorithms grow more slowly than linear because they repeatedly divide the
problem.

---

## Slide 23 - Logarithmic Time: O(log n)

**Delivery Category:** Core

**Slide Text:**

O(log n) often appears when the search space is repeatedly divided.

Example idea:

- binary search
- cut the remaining possibilities in half
- stop when the target is found

**Instructor Notes:**

Keep this intuitive. Students do not need logarithm math yet. Use the idea of
guessing a number between 1 and 100 by cutting the range in half each time.

**Transition Cue:**

These labels help us compare growth shapes side by side.

---

## Slide 24 - Growth Shape Comparison

**Delivery Category:** Core

**Slide Text:**

From slower growth to faster growth:

- O(1)
- O(log n)
- O(n)
- O(n2)

**Instructor Notes:**

Stress that this is a simplified comparison for this course level. Real
performance also depends on constants, implementation details, and hardware,
but growth shape matters as input becomes large.

**Optional Visual Notes:**

Simple line chart with four curves. Keep it uncluttered.

**Transition Cue:**

The textbook also gives rules for estimating complexity from structure.

---

## Slide 25 - Rule 1: Sequential Structure

**Delivery Category:** Core

**Slide Text:**

Sequential steps add together.

If steps happen one after another, estimate the growth of each part and keep
the dominant pattern.

**Instructor Notes:**

Example: one loop followed by another loop is still usually discussed as
linear at this level, not "two separate linear things" as a scary new class.

**Transition Cue:**

Some structures divide the problem rather than scan everything.

---

## Slide 26 - Rule 2: Divided Structure

**Delivery Category:** Core

**Slide Text:**

Dividing the problem can reduce growth.

Example:

- cut the search space in half
- ignore half the remaining possibilities
- repeat

**Instructor Notes:**

Connect to logarithmic growth. This is the intuition behind binary search, not
a full binary-search lesson.

**Transition Cue:**

Recursive structures need special care because the function calls itself.

---

## Slide 27 - Rules 3 And 4: Recursion And Nested Recursion

**Delivery Category:** Optional Deepening

**Slide Text:**

Recursion:

- a function calls itself

Nested recursion:

- recursive work happens inside more recursive work

**Instructor Notes:**

Treat this as a preview. Recursion receives deeper treatment later in the
course. For Week 2, students only need to know that recursion can affect growth
and should not be ignored.

**Transition Cue:**

The final rule helps us focus on the growth pattern rather than exact
arithmetic.

---

## Slide 28 - Rule 5: Ignore Constant Multiples

**Delivery Category:** Core

**Slide Text:**

Big-O focuses on growth shape.

For introductory analysis, constant multiples are usually ignored.

Example:

- 3n still grows like n
- 100n still grows like n

**Instructor Notes:**

Students may find this strange because constants matter in real timing. Explain
the distinction: constants can matter in practical performance, but Big-O
focuses on how the work scales as input grows very large.

**Transition Cue:**

That distinction is why timing evidence and Big-O reasoning should be used
together carefully.

---

## Slide 29 - Timing Evidence vs Big-O Reasoning

**Delivery Category:** Core

**Slide Text:**

Timing asks:

- What happened in this experiment?

Big-O asks:

- What growth pattern should we expect?

Use both carefully.

**Instructor Notes:**

This slide prevents overclaiming. A timing table can suggest a pattern, but it
does not prove everything about an algorithm under every condition.

**Transition Cue:**

The reading also explains that performance can be estimated using best, worst,
and average cases.

---

# Estimating and Selecting

## Slide 30 - Best, Worst, And Average Case

**Delivery Category:** Core

**Slide Text:**

Performance can vary by input.

- Best case: easiest input
- Worst case: hardest input
- Average case: typical input

**Instructor Notes:**

Use list lookup. Best case: target is first. Worst case: target is missing or
last. Average case: target may appear somewhere in the middle across many
inputs.

**Transition Cue:**

That is why one test case does not describe the whole algorithm.

---

## Slide 31 - Why Case Matters

**Delivery Category:** Core

**Slide Text:**

The same algorithm may look different depending on:

- where the target appears
- whether the target exists
- whether input is already organized
- whether data has duplicates

**Instructor Notes:**

Connect this to Lab 02 timing. Students should run several input sizes and be
careful about what their input data represents.

**Transition Cue:**

After estimating performance, we still have to choose an approach.

---

## Slide 32 - Selecting An Algorithm

**Delivery Category:** Core

**Slide Text:**

Selection depends on:

- correctness
- understandability
- efficiency
- memory use
- data size
- explainability

**Instructor Notes:**

Avoid ranking efficiency as the only virtue. Sometimes the clearer approach is
fine for small data. Sometimes a more complex approach is justified because the
data is large or the repeated work is expensive.

**Transition Cue:**

After selecting an algorithm, we still need to validate it.

---

## Slide 33 - Validating Algorithms

**Delivery Category:** Core

**Slide Text:**

Validation depends on the algorithm type:

- exact
- approximate
- randomized

**Instructor Notes:**

Define simply:

- Exact: should return the correct result.
- Approximate: should return a useful result within acceptable limits.
- Randomized: may use randomness, so validation may involve repeated runs or
  probability-based expectations.

For Week 2, students are mostly working with exact algorithms.

**Transition Cue:**

Even when an algorithm is validated, students must be able to explain it.

---

## Slide 34 - What Evidence Does Not Prove

**Delivery Category:** Core

**Slide Text:**

A timing table does not prove:

- every machine will match
- every input will behave the same
- the algorithm is always best
- the code has no bugs

**Instructor Notes:**

This slide prepares students for the Lab 02 limitation note. Their evidence
should be useful and honest, not exaggerated.

**Transition Cue:**

That honesty is part of explainability.

---

# Explainability

## Slide 35 - Explainability

**Delivery Category:** Core

**Slide Text:**

Explainability means you can describe:

- what the algorithm does
- why the approach fits
- what evidence supports it
- what limits remain

**Instructor Notes:**

Tie this to the course's AI-use philosophy. If AI helps explain or improve a
solution, the student still has to own the final explanation.

**Transition Cue:**

A good explanation connects the code to evidence.

---

## Slide 36 - Good Growth Explanation

**Delivery Category:** Core

**Slide Text:**

A responsible explanation says:

- what changed
- what evidence showed
- what Big-O label likely fits
- what the evidence does not prove

**Instructor Notes:**

Give an example sentence:

"In my timing table, Approach A increased more as input size grew. This matches
the idea of repeated scanning, so linear or worse growth may be involved.
However, my timing results are limited by machine noise and only four input
sizes."

**Transition Cue:**

Now show those ideas in the instructor demo.

---

# Demo Bridge

## Slide 37 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo comparison:

- manual list lookup
- set membership lookup

Same goal:

- check whether values appear in a collection

**Instructor Notes:**

Make clear that both approaches are correct for the demo task. The comparison
is about how the approaches behave as input size grows.

**Demo File / Artifact:**

`Assignments/Lab_02/demo/demo_code.py`

**Transition Cue:**

Before running the demo, predict the repeated work.

---

## Slide 38 - Predict The Work

**Delivery Category:** Core

**Slide Text:**

List lookup may:

- check many values
- repeat scanning
- grow with collection size

Set membership may:

- use a structure built for lookup
- avoid visible full scanning

**Instructor Notes:**

Do not over-teach hash tables here. Students will learn data structures more
directly in Week 3. For now, say that sets are designed for membership checks.

**Transition Cue:**

Now run the timing table and look for the pattern, not one exact number.

---

## Slide 39 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

Watch the table for:

- input size
- list lookup time
- set lookup time
- change across rows
- reminder about noisy timing

**Instructor Notes:**

Run the demo. If the numbers vary from a prior run, treat that as a teaching
moment. Say: "This is why we do not worship one decimal. We look for a pattern
and describe our evidence cautiously."

**Observable Output / Evidence:**

The demo prints a timing table and comparison summary.

**Transition Cue:**

After the evidence appears, translate the table into a growth explanation.

---

## Slide 40 - Demo Explanation

**Delivery Category:** Core

**Slide Text:**

Demo explanation pattern:

- both approaches were correct
- timing changed as input grew
- list lookup grew more noticeably
- set lookup changed less in this demo
- exact numbers may vary

**Instructor Notes:**

Use the printed comparison summary. Emphasize "in this demo" and "may vary" to
model cautious technical language.

**Transition Cue:**

Now model a professional support technique: using AI to review complexity after
we have already made our own prediction and collected evidence.

---

# AI-Assisted Complexity Review

## Slide 41 - AI Can Help Review Complexity

**Delivery Category:** Core

**Slide Text:**

AI can help you:

- analyze likely time complexity
- analyze likely space complexity
- identify repeated work
- explain Big-O in plain language
- suggest alternative approaches

**Instructor Notes:**

Frame this as a legitimate professional support technique, not a shortcut.

Many developers do not keep formal Big-O analysis fully memorized. That does
not mean they should ignore growth behavior. It means they should use tools
responsibly to recover, check, and explain the reasoning.

Say explicitly: "AI does not replace your Big-O awareness. AI helps you review
and explain it, but you still have to verify the answer against the code and
evidence."

**Misconception Warning:**

Students may hear this as permission to ask AI for the answer immediately.
Clarify the order: manual prediction first, timing evidence second, AI-assisted
review third, student-owned explanation last.

**Transition Cue:**

The quality of the AI response depends heavily on the prompt and on whether the
student asks for reasoning instead of just an answer.

---

## Slide 42 - Useful AI Prompt Pattern

**Delivery Category:** Core

**Slide Text:**

Prompt pattern:

```text
Analyze this Python function for likely time and space complexity.
Explain the reasoning in beginner-friendly language.
Identify repeated work.
Suggest one alternative if the current approach may not scale.
Do not rewrite the code unless I ask.
```

**Instructor Notes:**

Use this as a model prompt, not a required script. The important pieces are:
ask for time complexity, ask for space complexity, ask for repeated work, ask
for explanation, and limit unwanted rewriting.

If demonstrating live, use the demo functions `manual_list_lookup` and
`batch_set_lookup` because those are already visible and not one of the student
lab submission options.

**Transition Cue:**

After AI responds, the student still needs to evaluate the response.

---

## Slide 43 - Verify The AI Review

**Delivery Category:** Core

**Slide Text:**

After AI responds, check:

- Does it match the code?
- Does it identify the repeated work?
- Does it match the timing pattern?
- Did it overclaim?
- Can you restate it yourself?

**Instructor Notes:**

This slide is the ownership step. Students should not paste AI's explanation
unexamined into their README.

Use the demo example. If AI says list lookup is linear for one lookup, connect
that to scanning through the list. If AI discusses repeated batch lookups,
connect that to the demo's repeated probes. If AI says set lookup is usually
constant-time membership, remind students that this is introductory language
and that real implementations still have details and edge cases.

The student-owned explanation should connect three things: the code, the timing
evidence, and the Big-O vocabulary.

**Transition Cue:**

The lab now asks students to run a different comparison and write their own
evidence-based explanation. AI may help review that explanation, but it may not
replace the student's collected evidence.

---

# Lab Bridge

## Slide 44 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 02, you will compare two approaches.

Your work must include:

- two implementations
- at least four input sizes
- timing table
- chart or comparison table
- growth explanation
- limitation note

**Instructor Notes:**

Make the transfer explicit. Students should not use the demo's list-vs-set
lookup scenario as their final comparison. They choose one of the lab options
or an instructor-approved alternative.

**Transition Cue:**

The walkthroughs help students see the comparison pattern before coding.

---

## Slide 45 - Walkthrough Support

**Delivery Category:** Core

**Slide Text:**

The walkthrough artifact can help you:

- identify both approaches
- predict repeated work
- decide what to time
- explain the difference

**Instructor Notes:**

If students use a walkthrough, they must explain the pattern in their own
words, how they adapted it, and what they decided themselves.

**Related Artifact:**

`Assignments/Student_Facing/Lab_02_Full_English_Algorithm_Walkthroughs.md`

**Transition Cue:**

The README is where students connect code, timing, and explanation.

---

## Slide 46 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should show:

- approaches compared
- input sizes
- timing evidence
- chart or comparison table
- likely growth pattern
- timing limitation
- AI-use note, if applicable

**Instructor Notes:**

Explain that the limitation note is not an apology. It is part of responsible
technical communication. A good limitation note shows that the student
understands what the evidence can and cannot claim.

**Transition Cue:**

End by restating the difference between evidence and overclaiming.

---

# Wrap-Up

## Slide 47 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Performance analysis asks:

- Does it work?
- Is it understandable?
- How does it grow?
- What evidence supports the claim?

**Instructor Notes:**

Tie back to the reading's quality features: correct, understandable, efficient.
All three matter.

**Transition Cue:**

Students now have the vocabulary needed for Lab 02.

---

## Slide 48 - Lab 02 Success Check

**Delivery Category:** Core

**Slide Text:**

Successful Lab 02 work:

- compares two correct approaches
- uses increasing input sizes
- reports measured timing
- explains likely growth
- names a limitation

**Instructor Notes:**

Make this slide practical. Students should be able to compare it directly to
their README before submitting.

**Transition Cue:**

Finish with the immediate next action.

---

## Slide 49 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 02:

- choose a comparison
- implement or attempt both approaches
- collect timing evidence
- build a table or chart
- explain the pattern cautiously

**Instructor Notes:**

Remind students to start manually. AI may help explain a pattern only after
they have selected approaches, attempted implementation, and collected at least
one timing result.

**Transition Cue:**

Before students leave, prepare them for the Week 3 reading.

---

## Slide 50 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

For next week, read for structure choice.

Focus on:

- what each structure is for
- what operations each structure makes easier
- what operations each structure makes harder
- how complexity tables can guide decisions
- why tabular, matrix, and abstract structures appear in algorithm work

Do not memorize every operation cost. Use the tables like reference maps.

**Instructor Notes:**

This slide prepares the Week 3 reading. The textbook covers a broad set of
structures, including Python built-ins, Series, DataFrames, matrices, vectors,
stacks, queues, and trees. Students do not need to master all of them before
class.

The expectation is that students arrive with basic recognition: they should
have seen the terms, noticed the operation tables, and be ready to ask which
structure fits which problem.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 2 | Growth from small to large input | Clean instructional visual showing a small list becoming a larger dataset while question marks appear over runtime | Avoid intimidating math imagery |
| 13 | Timing noise | Simple stopwatch visual with small fluctuation marks around repeated runs | Do not imply timing is useless |
| 24 | Growth shape comparison | Minimal line chart showing O(1), O(log n), O(n), O(n2) growth curves | Keep labels large and uncluttered |
| 30 | Best/worst/average case | Three lanes labeled best, average, worst using lookup target positions | Avoid dense probability notation |
| 39 | Timing table evidence | Table-to-pattern visual with highlighted trend across rows | Do not replace the actual demo output |
| 41 | AI-assisted review | Human reasoning and AI response shown as a review loop after evidence collection | Do not imply AI replaces student understanding |
| 50 | Data structure reading preview | A simple map of containers labeled list, dictionary, set, table, matrix, stack, queue, and tree | Keep it calm and reference-like, not encyclopedic |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 10 min | Use one Lab 01 example only | Discuss student ambiguity examples |
| Textbook Review | 20 min | Keep space complexity brief | Add more examples of correct/understandable/efficient |
| Performance Foundations | 25 min | Skip Slide 17 | Discuss timing noise with examples |
| Big-O Vocabulary | 35 min | Treat recursion slides as preview only | Add board examples for O(1), O(n), O(n2), O(log n) |
| Estimating and Selecting | 20 min | Combine Slides 32-34 | Discuss exact, approximate, randomized examples |
| Explainability | 10 min | Use only Slide 36 | Add AI-use accountability discussion |
| Demo | 20 min | Run one demo and discuss table | Rerun demo to show timing variation |
| AI-Assisted Complexity Review | 10 min | Use only Slide 41 and describe prompt verbally | Run a live AI review of one demo function |
| Lab Bridge | 10 min | Combine Slides 44-46 | Walk through README expectations |

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
