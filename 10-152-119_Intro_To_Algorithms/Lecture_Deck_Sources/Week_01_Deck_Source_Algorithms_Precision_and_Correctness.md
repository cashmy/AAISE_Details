# Week 01 Deck Source - Algorithms, Precision, and Correctness

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 1 |
| Phase / Unit | Unit 1 - Algorithmic Foundations |
| Lecture Title | From Ambiguous Instructions to Testable Algorithms |
| Related Lab | Lab 01 - Precision and Correctness |
| Related Demo | Laptop Charger Decision Algorithm |
| Estimated Live Lecture Time | 90-150 minutes, expandable with breaks and discussion |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students begin the course by learning that an algorithm is not merely code or
mathematical notation. An algorithm is a clear, repeatable, testable process
for solving a problem.

This lesson moves students from everyday vague instructions into algorithmic
precision: inputs, outputs, assumptions, expected results, test cases, and
revision based on evidence.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook | What is an algorithm | Defines the course's working meaning of algorithm |
| Textbook | Phases of an algorithm: design and coding | Frames algorithm work as design before implementation |
| Textbook | Functional and non-functional requirements | Introduces expected result, optimization, and larger-dataset concerns |
| Textbook | Python as the development environment | Connects algorithm design to executable examples |
| Textbook | Algorithm design concerns | Supports correctness, optimality, and scale questions |
| Textbook | Data-intensive, compute-intensive, and mixed algorithms | Introduces data and compute dimensions without overloading Week 1 |
| Textbook | Data dimension: volume, velocity, variety | Connects algorithms to real-world data conditions |
| Textbook | Compute dimension, with Chapter 16 reference | Preview only; deeper compute concerns return later |
| Course artifact | Lab 01 - Precision and Correctness | Student application of precise decision logic |
| Course artifact | Lab 01 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading introduces algorithms as structured approaches for solving
problems. The important idea for Week 1 is that an algorithm begins before the
code. It starts with deciding what problem is being solved, what information is
needed, what output is expected, and what constraints shape the solution.

The reading also separates algorithm work into design and coding. Design asks
whether the procedure is clear, correct, and appropriate. Coding turns that
procedure into something executable in a development environment such as
Python.

For this course, Python is the execution language because students already have
Python background and because Python lets us focus on problem solving without
adding unnecessary syntax friction.

## Reading Key Ideas

- Algorithms are structured procedures for solving problems.
- Algorithm work includes both design and coding.
- Functional requirements describe what the algorithm must do.
- Non-functional requirements describe qualities such as performance,
  readability, scale, and maintainability.
- Data and compute demands affect whether an approach remains reasonable.

## Terms To Carry Forward

| Term | Brief Meaning |
| --- | --- |
| Algorithm | A clear, repeatable, testable process for solving a problem |
| Design phase | The planning and reasoning work before or alongside coding |
| Coding phase | The implementation of the designed procedure |
| Functional requirement | What the algorithm must produce or do |
| Non-functional requirement | How well the algorithm should behave under constraints |
| Data-intensive | Work shaped mainly by the amount, speed, or variety of data |
| Compute-intensive | Work shaped mainly by the amount of processing required |
| Edge case | A boundary or unusual input that tests hidden assumptions |

## What We Will Use Today

- definition of algorithm
- design before coding
- expected result
- ambiguity and assumptions
- test cases and edge cases
- data and compute as early design concerns

## What We Will Revisit Later

- formal Big-O notation
- large dataset behavior
- deeper optimization
- compute-heavy algorithms
- Chapter 16 compute concepts

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain an algorithm as a clear, repeatable, testable problem-solving
   process.
2. Separate algorithm design concerns from coding concerns.
3. Identify inputs, outputs, assumptions, and expected results for a small
   decision problem.
4. Explain why edge cases help reveal ambiguity.
5. Connect correctness, optimality, and larger-dataset behavior to early
   algorithm design.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Opening Frame | 1-5 | Core | Establish the course view of algorithms and textbook posture |
| Textbook Review | 6-9 | Core | Summarize assigned reading without replacing it |
| Algorithm Definition | 10-13 | Core | Translate algorithm meaning across representations |
| Design and Coding Phases | 14-17 | Core | Separate reasoning from implementation |
| Design Concerns | 18-22 | Core | Introduce correctness, optimality, and scale |
| Data and Compute Dimensions | 23-27 | Core / Optional | Introduce data-intensive and compute-intensive framing |
| Demo Bridge | 28-32 | Core | Prepare and run charger decision demo |
| Demo Add-On: Console Color | 33-34 | Core / Optional | Add ANSI color after the plain demo works |
| Lab Bridge | 35-37 | Core | Connect demo to Lab 01 |
| Optional Deepening | 38-41 | Optional | Extend for stronger groups or extra time |
| Wrap-Up | 42-44 | Core | Consolidate, assign next action, and prepare next reading |

---

# Opening Frame

## Slide 1 - Algorithmic Problem Solving

**Delivery Category:** Core

**Slide Text:**

- Algorithms are not just code.
- Algorithms are structured ways to solve problems.
- This course focuses on designing, testing, explaining, and improving them.

**Instructor Notes:**

Open by positioning the course as a bridge from "I can write Python" to "I can
reason about a solution before and after I write Python."

Make clear that this course is not abandoning coding. Instead, it slows down
the thinking around the code: why this approach, why this data, why this test,
and why this result should be trusted.

**Optional Visual Notes:**

Simple visual path: problem -> steps -> evidence -> revision.

**Transition Cue:**

Students may already associate algorithms with code, math, or intimidating
formal notation. Start there, then broaden the word so it means a structured
problem-solving process that can eventually be implemented and tested.

---

## Slide 2 - How To Use The Textbook

**Delivery Category:** Core

**Slide Text:**

The textbook may look more mathematical than this course feels at first.

For now:

- skim for the idea
- notice key terms
- mark what looks unfamiliar
- do not panic over every formula
- connect the concept back to Python functions

**Instructor Notes:**

Use this slide to lower unnecessary anxiety without lowering expectations.

Explain that the textbook is intentionally broad and sometimes gives a fuller
mathematical treatment than beginning developers need on first contact. That is
not a failure by the student. The first goal is to recognize the idea, become
familiar with the vocabulary, and understand why the concept matters.

Say explicitly: "When you write a Python function that takes input, follows
steps, and returns a result, you are already creating an algorithm. This course
will help you recognize, test, explain, and improve that process."

Also explain that some textbook topics may appear before students are ready to
master them fully. Later topics such as P, NP, NP-Complete, and NP-Hard are
important in computer science, but the beginning developer does not need to
master them to become competent at introductory algorithmic problem solving.

**Misconception Warning:**

Students may interpret unfamiliar formulas as proof that they are "not math
people" or that they cannot learn algorithms. Reframe the formulas as one way
experts compress reasoning, not the only way to begin understanding the idea.

**Transition Cue:**

With that textbook posture in mind, today we will start with the developer
version of algorithmic thinking: turning a vague instruction into a testable
process.

---

## Slide 3 - Today's Question

**Delivery Category:** Core

**Slide Text:**

How do we turn a vague instruction into a testable algorithm?

**Instructor Notes:**

This is the anchor question for the entire lesson. Keep returning to it during
the demo and lab bridge.

Explain that "testable" means another person can follow the rule, predict an
expected result, run or simulate the process, and compare the actual result to
the expected one.

**Optional Visual Notes:**

Before/after contrast: "Do the right thing" versus a small decision table.

**Transition Cue:**

Most everyday instructions feel clear to the person who wrote them. The problem
appears when another person or a computer has to follow those instructions
without sharing the hidden context.

---

## Slide 4 - Course Pattern

**Delivery Category:** Core

**Slide Text:**

- Lecture concept
- Instructor demo
- Related but different lab
- Evidence and explanation
- Responsible AI use

**Instructor Notes:**

Explain the repeated course rhythm. Emphasize that the demo will be similar to
the lab but not the same.

The demo is a teaching example. The lab is a transfer task. Students should
look for the pattern from the demo, then apply that pattern to a different
scenario instead of copying the demo's exact rules.

**Transition Cue:**

That pattern starts today with a small decision algorithm because decision
rules are easy to understand but still reveal ambiguity, assumptions, and edge
cases.

---

## Slide 5 - What Counts As Success Today

**Delivery Category:** Core

**Slide Text:**

By the end of class, you should be able to:

- name the inputs and outputs
- state assumptions
- write precise steps
- test normal and edge cases
- revise when evidence exposes ambiguity

**Instructor Notes:**

This slide makes the success target concrete and lowers anxiety. It also sets
up the Lab 01 grading emphasis.

Mention that the first week is not about clever code. It is about making a
small solution precise enough that it can be reviewed, tested, and improved.

**Transition Cue:**

The assigned reading gives vocabulary for this work. The lecture will use those
terms, but it will also translate them into small examples students can apply
in Lab 01.

---

# Textbook Review

## Slide 6 - Textbook Review: What Is An Algorithm?

**Delivery Category:** Core

**Slide Text:**

An algorithm is a structured process for solving a problem.

It should be:

- clear
- repeatable
- testable
- explainable
- implementable

**Instructor Notes:**

Use the course phrase explicitly: "An algorithm does not have to look
mathematical to be real."

Then add the working standard for the course: it must be clear, repeatable,
testable, explainable, and implementable. This definition is intentionally
practical because students will use it in labs.

**Optional Visual Notes:**

Five-part checklist beside a simple procedure.

**Transition Cue:**

Once students understand what an algorithm is, the next question is how an
algorithm is developed. The reading separates that work into design and coding.

---

## Slide 7 - Textbook Review: Design And Coding

**Delivery Category:** Core

**Slide Text:**

Algorithm work has two connected phases:

- Design: decide the logic
- Coding: implement the logic

Good coding cannot fully rescue unclear design.

**Instructor Notes:**

Do not overstate the separation. In real work, design and coding can loop. The
teaching point is that design questions should be visible before students race
into code.

Give a simple example: before writing a function that recommends "bring
charger," we should decide what counts as low battery and long time on campus.

**Transition Cue:**

Design is where we decide what the algorithm is supposed to do and how we will
know whether it did it correctly.

---

## Slide 8 - Textbook Review: Requirements

**Delivery Category:** Core

**Slide Text:**

Functional requirements:

- What result should the algorithm produce?

Non-functional requirements:

- How well should it perform?
- How readable should it be?
- How well should it handle growth?

**Instructor Notes:**

Keep this introductory. Week 1 does not need full software requirements theory.
Students only need the difference between "what it does" and "how well it
behaves."

Use a quick example: a functional requirement might be "return approved,
denied, or needs review." A non-functional requirement might be "the decision
should be easy to explain" or "the approach should still work when there are
many records."

**Transition Cue:**

Those requirements lead to three design questions we will keep using in the
course: expected result, reasonable approach, and larger-data behavior.

---

## Slide 9 - Textbook Review: Three Design Questions

**Delivery Category:** Core

**Slide Text:**

When designing an algorithm, ask:

1. Does it produce the expected result?
2. Is this a reasonable way to get the result?
3. What happens when the data gets larger?

**Instructor Notes:**

Use these three as the Week 1 version of correctness, approach fit, and scale.
Formal Big-O comes later.

Do not introduce formal notation here. The goal is to plant the questions so
Week 2's growth and Big-O discussion has somewhere to attach.

**Transition Cue:**

Now move from the reading summary into the course's working definition of an
algorithm: a procedure that starts with information, follows steps, produces a
result, and can be checked.

---

# Topic Block 1 - Algorithm Meaning

## Topic Purpose

Students need to understand that "algorithm" names the reasoning pattern, not
only the final code.

## Key Terms

| Term | Student-Friendly Meaning |
| --- | --- |
| Algorithm | A precise process for solving a problem |
| Procedure | Ordered steps |
| Expected result | What should happen if the algorithm is correct |
| Testable | Clear enough that we can check the result |

---

## Slide 10 - An Algorithm Is A Procedure

**Delivery Category:** Core

**Slide Text:**

An algorithm answers:

- What information do I start with?
- What steps do I follow?
- What result should I produce?
- How will I know it worked?

**Instructor Notes:**

Ask students for one everyday process that has steps. If they hesitate, offer
examples such as deciding what to wear, calculating a tip, choosing a route, or
prioritizing a task.

Then ask them to identify the starting information and final decision for that
example. The goal is to help them see that algorithmic thinking can begin with
ordinary decision processes before it becomes code.

**Transition Cue:**

Once we can describe the process, we can represent that same process in more
than one form. The representation changes, but the underlying reasoning should
stay the same.

---

## Slide 11 - Same Idea, Different Forms

**Delivery Category:** Core

**Slide Text:**

An algorithm can be represented as:

- plain English
- pseudocode
- Python code
- a table of rules
- a flowchart or diagram

**Instructor Notes:**

Use this slide to directly address the misconception that algorithms are only
equations or only code.

Say explicitly that plain English can be a valid starting representation when
the steps are precise enough to follow and test. Pseudocode and Python are not
separate ideas; they are more structured ways to express the same reasoning.

**Optional Visual Notes:**

Four-column visual: English, pseudocode, Python, table.

**Transition Cue:**

Next we need to ask what separates a real algorithm from a vague suggestion.
The answer is not the format. The answer is whether the process is ordered,
precise, repeatable, testable, and connected to a result.

---

## Slide 12 - What Makes It Algorithmic?

**Delivery Category:** Core

**Slide Text:**

The process must be:

- ordered
- precise
- repeatable
- testable
- connected to a result

**Instructor Notes:**

Use a deliberately weak instruction: "Pick the best option."

Ask students what makes that instruction hard for someone else to follow. The
problem is that "best" has not been defined. Best could mean cheapest, fastest,
healthiest, easiest, highest quality, or most appropriate for a specific
person.

Then connect the weak instruction back to the slide. It is not precise enough,
not repeatable across people, and not testable unless "best" is defined with
specific rules or scoring criteria.

**Misconception Warning:**

Students may think everyday steps are too simple to be algorithms. That is not
true if the steps are precise and testable.

**Transition Cue:**

That is why precision matters. Vague instructions often feel obvious to the
person who wrote them because that person is silently filling in hidden
decisions. Algorithms require those hidden decisions to be written down.

---

## Slide 13 - Vague Instructions Hide Decisions

**Delivery Category:** Core

**Slide Text:**

Vague words often hide rules:

- low
- soon
- many
- best
- reasonable
- urgent

**Instructor Notes:**

Ask: "What counts as urgent?"

Let students give two or three different answers. One student may define
urgent as "due today." Another may define urgent as "affects many people."
Another may define it as "blocks all work."

Point out that those answers are not just opinions. Each answer implies a
different rule. Those hidden rules are part of the algorithm even before code
exists.

**Transition Cue:**

The design phase is where we make those hidden rules explicit before we ask
Python to execute them.

---

# Topic Block 2 - Design Before Coding

## Topic Purpose

Students need to see that coding is implementation, not the whole algorithmic
thinking process.

## Key Terms

| Term | Student-Friendly Meaning |
| --- | --- |
| Design | Deciding how the solution should work |
| Coding | Turning the design into executable instructions |
| Assumption | Something treated as true for the solution |
| Constraint | A limit or rule the solution must respect |

---

## Slide 14 - Design Phase

**Delivery Category:** Core

**Slide Text:**

Before coding, define:

- problem
- inputs
- outputs
- assumptions
- constraints
- expected results

**Instructor Notes:**

Connect each bullet directly to Lab 01.

Students will not only submit code or pseudocode. They will also submit the
problem statement, inputs, outputs, assumptions, constraints, and expected
results in their README. These design pieces are part of the assessed work
because they show whether the student understands the problem before trying to
solve it.

**Transition Cue:**

Once the design is clear enough to test, coding becomes the act of making that
design executable.

---

## Slide 15 - Coding Phase

**Delivery Category:** Core

**Slide Text:**

Coding turns the design into something executable.

In this course, Python helps us:

- run the logic
- test cases quickly
- compare results
- revise based on evidence

**Instructor Notes:**

Mention that Python is chosen because students have already used it and because
it keeps the course focused on algorithmic thinking.

The point is not that Python is the only language for algorithms. The point is
that Python gives the class a familiar execution environment where students can
run small examples, inspect output, and revise quickly.

**Transition Cue:**

However, getting Python to run is only one part of the job. A running program
can still implement the wrong rule or miss an important boundary case.

---

## Slide 16 - Running Is Not The Same As Correct

**Delivery Category:** Core

**Slide Text:**

A program can run and still be wrong.

It may:

- use the wrong rule
- miss an edge case
- return the wrong result
- work only for one example

**Instructor Notes:**

This is one of the most important Week 1 points.

Students often equate "no error message" with correctness. Make the distinction
plain: no error message only means Python was able to execute the instructions.
It does not prove that the instructions match the intended rule or produce the
right result for important cases.

**Transition Cue:**

That is why we write expected results. The expected result records what we
believe should happen before we compare it to what the algorithm actually did.

---

## Slide 17 - Expected Results

**Delivery Category:** Core

**Slide Text:**

Expected result:

- what we believe should happen
- based on the rule we intended
- written before or alongside the test

Actual result:

- what the algorithm produced

**Instructor Notes:**

Explain that expected outputs in tests represent our mental expectation. They
are not usually handed to us in real-world data.

In a lab or success example, expected values are included so we can check
whether the algorithm behaved the way we intended. In a real-world dataset, the
answer usually has to be reasoned out, validated by a subject-matter expert, or
confirmed through business rules, tests, or user feedback.

**Optional Visual Notes:**

Expected column beside Actual column with Pass? indicator.

**Transition Cue:**

Now connect expected and actual results to the three design concerns from the
reading: Does it produce the expected result, is the approach reasonable, and
what happens when the data gets larger?

---

# Topic Block 3 - Algorithm Design Concerns

## Topic Purpose

Students need an introductory version of correctness, approach fit, and scale
before formal complexity analysis begins.

## Key Terms

| Term | Student-Friendly Meaning |
| --- | --- |
| Correctness | Whether the algorithm gives expected results for the right reasons |
| Optimality | Whether the approach is reasonably efficient or suitable |
| Scale | What happens as the input grows |
| Evidence | Output, tests, tables, or traces that support a claim |

---

## Slide 18 - Concern 1: Expected Result

**Delivery Category:** Core

**Slide Text:**

First question:

Does the algorithm produce the expected result?

Evidence may include:

- test cases
- input/output tables
- traces
- before/after comparisons

**Instructor Notes:**

Do not drift into formal proofs.

For Week 1, correctness evidence should be practical and visible. Students
should understand that a test table, a trace, or a before/after comparison can
support a claim that the algorithm is improving.

**Transition Cue:**

After we have some evidence that the result is correct, we can ask a second
question: even if this works, is this a reasonable way to solve the problem?

---

## Slide 19 - Concern 2: Reasonable Approach

**Delivery Category:** Core

**Slide Text:**

Second question:

Is this a reasonable way to get the result?

Consider:

- rule order
- readability
- unnecessary steps
- confusing assumptions

**Instructor Notes:**

Use a small decision problem. If a denial rule should stop the process, checking
extra rules first may be confusing or wasteful.

For example, if an event registration requires payment and seats are available,
the algorithm might check payment first or seat availability first. Either may
work, but the order should be intentional. A reasonable approach is one that a
person can read, maintain, and explain.

**Transition Cue:**

The same approach may feel fine when there are only a few examples. Later, when
there are hundreds or thousands of inputs, the amount of repeated work starts
to matter.

---

## Slide 20 - Concern 3: Larger Data

**Delivery Category:** Core

**Slide Text:**

Third question:

What happens when the input gets larger?

Ask:

- Does the work grow slowly?
- Does the work grow quickly?
- Does the algorithm repeat work?

**Instructor Notes:**

This is only Big-O intuition. Avoid notation unless students ask. The formal
growth vocabulary comes in Week 2.

For now, the point is only that algorithms do work, and that work may increase
as the input grows. Students do not need to calculate complexity yet. They only
need to start noticing repeated work and growth behavior.

**Transition Cue:**

Tests and small evidence tables help reveal whether the algorithm behaves as
expected. Normal cases and edge cases give us two different kinds of evidence.

---

## Slide 21 - Normal Cases And Edge Cases

**Delivery Category:** Core

**Slide Text:**

Normal cases test expected everyday behavior.

Edge cases test boundaries, missing information, or unusual combinations.

Both matter.

**Instructor Notes:**

Give the charger example verbally: 25% battery is normal low-battery behavior;
exactly 40% is an edge case because it tests the boundary.

Make the distinction clear. A normal case checks an ordinary situation that the
algorithm should handle easily. An edge case checks a boundary, missing value,
tie, threshold, or unusual combination that may expose an unclear rule.

**Transition Cue:**

When an edge case fails, it often reveals an assumption that was never written
down clearly enough.

---

## Slide 22 - Revision Is Part Of The Process

**Delivery Category:** Core

**Slide Text:**

Testing may show:

- the rule is unclear
- the threshold is wrong
- the order matters
- the output needs more detail

Revision is not failure. It is evidence-driven improvement.

**Instructor Notes:**

This slide sets up the demo failure as a productive moment, not an instructor
mistake.

Tell students that revision is part of algorithm design. The first version is
often useful because it gives us something concrete to test. The goal is not to
pretend the first version is perfect. The goal is to use evidence to improve
it.

**Transition Cue:**

Before the demo, connect one more reading idea: algorithms are shaped by both
the data they process and the amount of work they ask the computer to do.

---

# Topic Block 4 - Data and Compute Dimensions

## Topic Purpose

Students should get a first-pass understanding that algorithms are affected by
the data they process and the work they require from the computer.

## Key Terms

| Term | Student-Friendly Meaning |
| --- | --- |
| Data-intensive | The challenge is mainly the data |
| Compute-intensive | The challenge is mainly the processing |
| Volume | How much data exists |
| Velocity | How fast data arrives or changes |
| Variety | How many different forms the data takes |

---

## Slide 23 - Data-Intensive Algorithms

**Delivery Category:** Core

**Slide Text:**

A data-intensive algorithm is shaped mainly by the data.

Questions:

- How much data?
- How fast does it arrive?
- How many forms does it take?

**Instructor Notes:**

Keep this concrete: registration records, support tickets, logs, form
submissions, product reviews.

**Transition Cue:**

The reading names this as the data dimension.

---

## Slide 24 - The Data Dimension

**Delivery Category:** Core

**Slide Text:**

Data can be described by:

- volume: how much
- velocity: how fast
- variety: how many forms

These affect which algorithmic approach fits.

**Instructor Notes:**

Do not make this a big-data lecture. It is a vocabulary bridge for later data
analytics and AI foundations.

**Transition Cue:**

Some algorithms are shaped less by data size and more by processing demand.

---

## Slide 25 - Compute-Intensive Algorithms

**Delivery Category:** Core

**Slide Text:**

A compute-intensive algorithm is shaped mainly by how much processing it
requires.

Examples may include:

- simulations
- image processing
- cryptography
- model training
- repeated calculations

**Instructor Notes:**

The reading references Chapter 16 for deeper compute topics. Treat this as a
preview, not a deep dive.

**Transition Cue:**

Some problems are both data-intensive and compute-intensive.

---

## Slide 26 - Both Data And Compute

**Delivery Category:** Optional Deepening

**Slide Text:**

Some algorithms are affected by both:

- large data volume
- frequent updates
- varied data types
- heavy processing

Design must consider both dimensions.

**Instructor Notes:**

Use an AI example lightly: ranking many support resources by many features can
become both a data and compute problem as scale increases.

**Transition Cue:**

For Week 1, the practical takeaway is simple: ask about data and work early.

---

## Slide 27 - Week 1 Practical Takeaway

**Delivery Category:** Core

**Slide Text:**

Before coding, ask:

- What data do I need?
- How much data might there be?
- What work must the algorithm do?
- How will I test the result?

**Instructor Notes:**

This connects the data/compute dimension back to Lab 01 without overwhelming
students.

**Transition Cue:**

Now we will apply these ideas to a small decision algorithm.

---

# Demo Setup

## Slide 28 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo problem:

Should a student bring a laptop charger to campus?

Inputs:

- battery percent
- expected hours on campus
- outlet access

Output:

- bring charger
- charger optional

**Instructor Notes:**

Make clear that this is not a lab scenario option. It is the demo scenario.

**Demo File / Artifact:**

`Assignments/Lab_01/demo/demo_code.py`

**Transition Cue:**

Start with a vague version.

---

## Slide 29 - Vague Rule Version

**Delivery Category:** Core

**Slide Text:**

Initial rule:

- If the battery is low, bring the charger.
- If campus time is long and outlets are unreliable, bring the charger.
- Otherwise, the charger is optional.

**Instructor Notes:**

Ask students to identify the vague terms before showing the revised rule.

Expected answers include "low," "long," and "unreliable." If students do not
name them, point to each word and ask what number, threshold, or condition
would make the word testable.

**Misconception Warning:**

Students may think the rule is obvious because they fill in their own hidden
thresholds.

**Transition Cue:**

Now replace the vague words with thresholds that a person or program can
actually test.

---

## Slide 30 - Precise Rule Version

**Delivery Category:** Core

**Slide Text:**

Revised rule:

- If battery percent is 40 or below, bring the charger.
- Else if expected hours is 4 or more and outlet access is false, bring the charger.
- Otherwise, the charger is optional.

**Instructor Notes:**

Point out that the revised version still may not be perfect, but it is now
testable.

The important improvement is that the rule now names exact boundaries:
`40 or below`, `4 or more`, and `outlet access is false`. These boundaries make
it possible to create expected results and compare them to actual results.

**Transition Cue:**

Before running the code, show that this same decision logic can be represented
in plain English, pseudocode, Python-style logic, and a test table.

---

## Slide 31 - Representation Bridge

**Delivery Category:** Core

**Slide Text:**

Same algorithm, different forms:

- precise plain English
- pseudocode
- Python-style logic
- test table

**Instructor Notes:**

Use the demo output to show the bridge. Emphasize that the reasoning should
stay stable as representation changes.

Say explicitly: if the plain-English rule says `40 or below`, the pseudocode
and Python should not quietly change that to `below 40`. A representation
bridge is useful because it helps us detect when the same idea has drifted
between formats.

**Observable Output / Evidence:**

The demo prints the revised rules, pseudocode, Python-style logic, and test
tables.

**Transition Cue:**

Now run the tests and let the evidence show whether the initial rule and
revised rule behave the way we expected.

---

## Slide 32 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

Watch for:

- expected result
- actual result
- pass or fail
- boundary case
- revised rule

**Instructor Notes:**

Run the initial rule set first. Ask students to predict the boundary case
before revealing the result. The boundary case is battery exactly `40`,
expected campus time `4` hours, and no outlet access.

After the initial rule set fails that case, pause and ask what caused the
failure. The intended answer is that the first version used strict comparisons
where the intended rule needed inclusive comparisons. Then run the revised rule
set to show that the corrected threshold passes.

**Observable Output / Evidence:**

Test 4 should expose the exact-threshold issue in the initial version.

**Transition Cue:**

Before moving to the lab, add one small refinement to the demo. The algorithm
already works in plain text. Now we will add console color as a presentation
layer so the evidence is easier for human readers to scan.

---

# Demo Add-On: Console Color

## Slide 33 - Add-On Step: Colorize The Evidence

**Delivery Category:** Core

**Slide Text:**

After the plain demo works, add light console color.

The color helps highlight:

- section headings
- passed tests
- failed tests
- important boundary cases

**Instructor Notes:**

Present this as an add-on step after the plain-text version has already been
run and tested.

Say explicitly: "The algorithm is already complete. We are not changing the
decision rule. We are improving how the evidence is displayed."

Then add the color support code and rerun the demo. Use the output as the
example. The green and red pass/fail indicators make the failed boundary case
easier to notice. This supports learning because students can see where the
evidence points without hunting through plain text.

Do not over-teach ANSI escape codes in Week 1. The main point is readability:
console output can be designed for humans, even when the program is still
simple.

**Misconception Warning:**

Students may think colorized output is a requirement for Lab 01. Clarify that
it is not required. The lab requirement is clear evidence. Color is an optional
presentation improvement.

**Transition Cue:**

Because this is only a presentation add-on, the program should still work and
remain understandable without color.

---

## Slide 34 - Add-On Principle: Presentation Is Separate From Logic

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

Keep these separate:

- algorithm logic: makes the decision
- evidence output: shows what happened
- presentation layer: makes output easier to scan

**Instructor Notes:**

Point out that the final demo includes a `NO_COLOR` fallback. This means the
same algorithm and evidence table can still run in plain text if color is
disabled or unsupported.

This is a small example of a larger professional habit: do not mix the core
logic so tightly with the display layer that the algorithm becomes hard to
test, read, or reuse.

For Week 1, students do not need to implement color. They only need to notice
the design principle: build the working logic first, verify the evidence, and
then optionally improve presentation without changing the algorithm.

**Optional Visual Notes:**

Three-layer diagram: logic -> evidence table -> presentation polish.

**Transition Cue:**

Now the lab asks students to use the same thinking pattern with a different
scenario: define the rule, expose hidden assumptions, test the boundary, and
revise based on evidence.

---

# Lab Bridge

## Slide 35 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In the lab, you will choose a different scenario and create:

- problem statement
- inputs and outputs
- assumptions
- pseudocode or Python
- normal and edge-case tests
- revision note

**Instructor Notes:**

Make the transfer explicit: the lab is not about copying the charger demo. It
is about applying the same reasoning pattern.

Name the reasoning pattern out loud: choose a small decision problem, identify
inputs and outputs, write precise rules, test normal and edge cases, compare
expected and actual results, and revise one ambiguity.

**Related Lab Requirements:**

Lab 01 requires at least 5 test cases, including 3 normal cases and 2 edge
cases.

**Transition Cue:**

Some students may need help seeing how an everyday scenario becomes an
algorithm. The walkthrough artifact is there for that support, but it is not a
finished answer to copy.

---

## Slide 36 - Walkthrough Support

**Delivery Category:** Core

**Slide Text:**

The walkthrough artifact can help you see the pattern.

If you use it, explain:

- what pattern it showed
- how you adapted it
- what you still decided yourself

**Instructor Notes:**

This preserves scaffolding while preventing mindless copying.

If a student uses the walkthrough, the student must explain the general pattern
in their own words and identify what they changed for their own scenario. This
turns the walkthrough into a learning support instead of a substitute for
thinking.

**Related Artifact:**

`Assignments/Student_Facing/Lab_01_Full_English_Algorithm_Walkthroughs.md`

**Transition Cue:**

The README is where students make the thinking visible. The code or pseudocode
shows the algorithm, but the README shows the evidence, assumptions, revision,
and explanation.

---

## Slide 37 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should show:

- inputs and outputs
- assumptions
- test table
- expected vs actual results
- before/after revision
- AI-use note, if applicable

**Instructor Notes:**

This reinforces the GitHub/README submission model and sets expectations early.

Explain that the README is not extra paperwork. It is part of the algorithmic
evidence. When grading, the instructor should be able to open the repository
and see the problem, assumptions, tests, expected results, actual results, and
revision without hunting through separate documents.

**Transition Cue:**

If students seem ready or if time remains, use the optional examples to deepen
the design concerns. If the class is saturated, skip the optional section and
move directly to lab work.

---

# Optional Deepening Section

## Slide 38 - Example: Expected Result Is Not Always Obvious

**Delivery Category:** Optional Deepening

**Slide Text:**

Two people may disagree about the expected result when:

- the rule is vague
- the threshold is missing
- priorities conflict
- information is incomplete

**Instructor Notes:**

Use help desk priority as a quick verbal example without solving the lab
scenario.

**When To Use:**

Use if students are struggling to see why expected results matter.

---

## Slide 39 - Example: Rule Order Matters

**Delivery Category:** Optional Deepening

**Slide Text:**

Changing rule order can change the result.

Ask:

- Which rule should be checked first?
- Which rule wins if two rules conflict?
- Should the algorithm stop early?

**Instructor Notes:**

This will matter in later search/sort and decision-ladder labs. For Week 1,
keep it simple.

**When To Use:**

Use if students ask why the charger rule checks battery before time.

---

## Slide 40 - Example: Small Data Can Hide Problems

**Delivery Category:** Optional Deepening

**Slide Text:**

An approach may seem fine with 5 examples.

It may struggle with:

- 500 records
- 5,000 records
- repeated updates
- mixed data formats

**Instructor Notes:**

This foreshadows Week 2 without teaching full complexity yet.

**When To Use:**

Use if time allows or students ask why larger datasets matter in an algorithms
course.

---

## Slide 41 - Example: Data And Compute Together

**Delivery Category:** Instructor Reserve

**Slide Text:**

Recommendation systems can involve:

- many users
- many resources
- many tags or features
- frequent score updates
- repeated ranking calculations

**Instructor Notes:**

This is a light preview of later AI/data bridge topics. Do not overdevelop it
in Week 1.

**Use When:**

Use for advanced learners or if the class asks how this connects to AI.

---

# Wrap-Up

## Slide 42 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Algorithms are not just code.

They are:

- designed
- represented
- tested
- revised
- explained

**Instructor Notes:**

This is the core Week 1 takeaway.

**Transition Cue:**

End with the immediate lab action.

---

## Slide 43 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 01:

- choose a scenario
- write precise rules
- create normal and edge-case tests
- compare expected and actual results
- revise one ambiguity

**Instructor Notes:**

Remind students to start manually. AI critique comes only after their first
version and at least three test cases.

**Transition Cue:**

Before students leave, prepare them for the Week 2 reading.

---

## Slide 44 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

For next week, read for growth behavior.

Focus on:

- what time complexity means
- what space complexity means
- why input size matters
- what O(1), O(n), O(n2), and O(log n) are trying to describe
- how best, worst, and average cases differ

Do not panic over formulas. Mark them, skim for meaning, and connect them back
to the code examples.

**Instructor Notes:**

This slide prepares the Week 2 reading without suggesting that the reading is
optional. Tell students that the textbook may use compact mathematical notation
because that is how computer science often communicates growth patterns.

The practical goal for the next reading is recognition and translation:
students should come in ready to talk about how an algorithm's behavior changes
when the amount of input grows.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 2 | Textbook posture | Calm visual showing a textbook page with formulas beside a Python function, connected by a simple "same idea, different representation" bridge | Avoid making the textbook look scary or mocking mathematical notation |
| 3 | Vague-to-testable transformation | Create a clean instructional image showing a blurry instruction becoming a clear test table, modern classroom style, minimal text, high contrast | Avoid making the image look like a generic business funnel |
| 11 | Representation bridge | Four-panel visual: plain English, pseudocode, Python, and test table as different views of the same algorithm | Keep readable text minimal; exact text should be on the slide, not embedded in the image |
| 24 | Data dimension | Simple three-axis visual for volume, velocity, variety using data cards or streams | Avoid overwhelming big-data imagery |
| 32 | Edge case evidence | Boundary line visual at 40 percent battery with one point exactly on the line | Use as support only; do not replace the test table |
| 44 | Growth reading preview | A calm visual of a small dataset growing into a larger dataset beside simple labels for time and space | Avoid dense formula imagery |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Opening Frame | 12 min | Combine Slides 2-5 | Ask students for everyday algorithms |
| Textbook Review | 15 min | Move data/compute preview later | Add student examples for requirements |
| Algorithm Meaning | 20 min | Skip Slide 13 discussion | Add representation examples |
| Design and Coding | 20 min | Compress Slides 14-17 | Discuss expected vs actual results |
| Design Concerns | 25 min | Briefly define scale only | Add edge-case exercises |
| Data and Compute | 15 min | Teach Slides 23, 24, 27 only | Include Slides 25-26 and 41 |
| Demo | 20 min | Run only failed and revised cases | Predict each test before running |
| Demo Add-On: Console Color | 5 min | Skip the color add-on and proceed to lab bridge | Add color live and discuss presentation vs logic separation |
| Lab Bridge | 10 min | Combine Slides 35-37 | Walk through README expectations |

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
