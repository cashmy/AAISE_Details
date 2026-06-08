# Week 05 Deck Source - Recursion, Iteration, and Strategy

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 5 |
| Phase / Unit | Unit 3 - Strategy Patterns and Observable Behavior |
| Lecture Title | Same Problem, Different Strategy |
| Related Lab | Lab 05 - Strategy Comparison |
| Related Demo | Nested Donation Envelopes |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students learn that a problem can often be solved by more than one algorithmic
strategy.

The goal is not to memorize strategy names. The goal is to compare strategies
using correctness, readability, growth behavior, scalability, and fit to the
problem's data shape.

This lesson also gives students a careful orientation to more theoretical
language from the textbook, including P, NP-Hard, and NP-Complete, without
turning those topics into mastery requirements.

---

# Possible Two-Session Split

The Week 5 reading includes strategy families and some advanced theory
orientation. This can be taught as one longer lecture with breaks, but a
two-session split may reduce overload.

## Session A - Design Concerns and Strategy Vocabulary

Recommended slides:

- 1-4: review and opening frame
- 5-10: textbook review and design concerns
- 11-16: functional/non-functional requirements, correctness, performance,
  scalability
- 17-22: P/NP orientation and strategy comparison frame

Session A target:

Students understand that algorithm design includes correctness, performance,
and scalability, and that advanced theoretical labels should be recognized
without panic.

## Session B - Strategy Families, Demo, and Lab Transfer

Recommended slides:

- 23-34: divide and conquer, dynamic programming, greedy, PageRank, linear
  programming
- 35-39: iteration and recursion
- 40-43: demo
- 44-47: lab bridge
- 48-50: wrap-up

Session B target:

Students can compare two strategies for one problem and explain which one fits
the context better.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook Ch. 4 | Basic concept of designing an algorithm | Frames design as choosing and justifying a strategy |
| Textbook Ch. 4 | Functional and non-functional requirements | Connects Week 1 requirements language to Week 5 strategy choice |
| Textbook Ch. 4 | Correctness | Reinforces expected results and evidence |
| Textbook Ch. 4 | Performance | Connects strategy to optimality and complexity |
| Textbook Ch. 4 | Scalability | Connects strategy to larger data and elasticity |
| Textbook Ch. 4 | Skim: polynomial, NP-Hard, NP-Complete | Recognition only; supports vocabulary and humility |
| Textbook Ch. 4 | Divide and conquer | Introduces strategy by splitting the problem |
| Textbook Ch. 4 | Dynamic programming | Recognition and light intuition; avoid full mastery |
| Textbook Ch. 4 | Greedy strategy | Introduces local choice strategy and risk |
| Textbook Ch. 4 | PageRank example | Used as an example of strategy applied at scale |
| Textbook Ch. 4 | Linear programming | Recognition-oriented example of optimizing under constraints |
| Course artifact | Lab 05 - Strategy Comparison | Student comparison of two strategies |
| Course artifact | Lab 05 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading moves from individual algorithms toward algorithm design.

The key idea is that algorithm design is not only about writing steps. It is
about selecting a strategy that fits the problem, the data, and the constraints.

The reading also includes advanced theory vocabulary such as polynomial time,
NP-Hard, and NP-Complete. For this course, those terms should be treated as
recognition and orientation. Students should know that some problems are
inherently harder to solve efficiently, but they do not need to master formal
complexity theory.

## Reading Key Ideas

- Algorithm design starts with requirements and constraints.
- Correctness asks whether the strategy produces the expected result.
- Performance asks whether the approach is reasonable and efficient enough.
- Scalability asks what happens when the data or demand grows.
- Divide and conquer breaks a problem into smaller pieces.
- Dynamic programming reuses prior results to avoid repeated work.
- Greedy strategies make the best-looking local choice.
- PageRank and linear programming show strategy applied beyond small examples.

## Terms To Carry Forward

| Term | Brief Meaning |
| --- | --- |
| Strategy | A general approach for solving a problem |
| Correctness | Whether the algorithm produces the expected result |
| Performance | How efficiently the algorithm uses work or resources |
| Scalability | How the approach behaves as size or demand grows |
| Elasticity | Ability to handle changing demand or scale when resources change |
| Polynomial | A growth pattern that can be expressed with powers such as n, n2, or n3 |
| NP-Hard | A class of problems that are at least as hard as the hardest problems in NP |
| NP-Complete | Problems that are both in NP and as hard as any problem in NP |
| Divide and conquer | Split, solve smaller pieces, then combine |
| Dynamic programming | Store and reuse results from overlapping subproblems |
| Greedy strategy | Make the best-looking choice at each step |
| Recursion | A function solves a smaller version of the same problem |
| Base case | The condition where recursion stops |

## What We Will Use Today

- correctness, performance, and scalability as strategy questions
- divide and conquer as a split-and-combine pattern
- dynamic programming as recognition of saved repeated work
- greedy as local choice with possible risk
- iteration and recursion as two strategy forms
- comparison table evidence
- strategy recommendation with conditions

## What We Will Revisit Later

- graphs and traversal strategy
- recommendation and ranking systems
- larger-scale algorithms
- explainability and limits of algorithmic solutions
- final-assessment explanation and justification

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain why one problem may have multiple valid strategies.
2. Compare strategies using correctness, readability, growth, and fit to data.
3. Recognize divide and conquer, dynamic programming, and greedy strategies at
   an introductory level.
4. Explain recursion using base case and smaller problem language.
5. Use evidence to support a strategy recommendation.
6. Avoid claiming that one strategy is always best without naming conditions.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from search preconditions to strategy fit |
| Textbook Review | 5-10 | Core | Curate Chapter 4 into design concerns and strategy families |
| Design Concerns | 11-16 | Core | Reframe correctness, performance, and scalability as strategy criteria |
| Theory Orientation | 17-22 | Core / Instructor Reserve | Skim P/NP vocabulary without overload |
| Algorithmic Strategies | 23-34 | Core / Optional | Introduce divide and conquer, dynamic programming, greedy, PageRank, and linear programming |
| Iteration and Recursion | 35-39 | Core | Prepare students for the demo and Lab 05 comparisons |
| Demo Bridge | 40-43 | Core | Compare iterative and recursive donation-envelope strategies |
| Lab Bridge | 44-47 | Core | Connect demo to Lab 05 requirements |
| Wrap-Up | 48-50 | Core | Consolidate and assign next action |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 04 Taught Us

**Delivery Category:** Core

**Slide Text:**

In Lab 04, search strategy depended on assumptions.

Binary search was powerful only when:

- the data was sorted
- the comparison rule matched the order
- the trace decisions were valid

**Instructor Notes:**

Use one Lab 04 binary-search trace if available. Keep the review short and
targeted. The point is that an algorithm's strategy cannot be separated from
its assumptions.

This prepares the move from a specific search strategy to broader strategy
families.

**Transition Cue:**

Last week we asked whether a search strategy was valid. This week we ask which
strategy fits a problem and why.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

How can two correct solutions still be different in quality?

**Instructor Notes:**

Let students answer briefly. They may mention readability, speed, memory,
complexity, or ease of testing.

Affirm that correctness is necessary, but not the only evaluation lens. Today
they will compare strategies, not just outputs.

**Transition Cue:**

The textbook frames this as algorithm design.

---

## Slide 3 - Same Problem, Different Strategy

**Delivery Category:** Core

**Slide Text:**

Many problems can be solved in more than one way.

Strategies may differ in:

- how they break down the problem
- how much work they repeat
- how easy they are to explain
- how well they fit the data shape

**Instructor Notes:**

Use an everyday example if useful: finding a lost item by checking every room
one by one versus first asking where it was last seen.

The goal is to help students see strategy as a design choice, not a code style
preference.

**Transition Cue:**

To compare strategies, students need success criteria.

---

## Slide 4 - Success Today

**Delivery Category:** Core

**Slide Text:**

Today you should be able to:

- describe two strategies
- test both strategies
- compare correctness and readability
- discuss likely growth behavior
- recommend one strategy with conditions

**Instructor Notes:**

This is the learning contract for the lesson. Emphasize "with conditions."

Students should not leave saying "recursion is better" or "greedy is better."
They should say "this strategy fits this problem because..."

**Transition Cue:**

Now anchor the lesson in the assigned reading.

---

# Textbook Review

## Slide 5 - Textbook Review: Designing Algorithms

**Delivery Category:** Core

**Slide Text:**

The reading focuses on designing algorithms.

Design means choosing a strategy that fits:

- the required result
- the problem constraints
- the data size
- the cost of the approach
- the explanation needed

**Instructor Notes:**

Connect this directly back to Week 1. Students have already worked with
problem framing, assumptions, and expected results. Week 5 adds named strategy
families and more explicit tradeoff reasoning.

**Transition Cue:**

Design still begins with requirements.

---

## Slide 6 - Textbook Review: Functional Requirements

**Delivery Category:** Core

**Slide Text:**

Functional requirements ask:

- What must the algorithm produce?
- What input does it need?
- What output is expected?
- What counts as a correct result?

**Instructor Notes:**

Keep this concrete. If the task is "find the best schedule," students need to
define "best" before comparing strategies.

Functional requirements are the anchor for correctness.

**Transition Cue:**

Non-functional requirements ask about quality under constraints.

---

## Slide 7 - Textbook Review: Non-Functional Requirements

**Delivery Category:** Core

**Slide Text:**

Non-functional requirements ask:

- How fast should it be?
- How readable should it be?
- How much memory can it use?
- How well should it scale?
- How explainable does it need to be?

**Instructor Notes:**

Students may think non-functional means optional. Correct that gently:
non-functional requirements are often the difference between "it works" and
"it works well enough for the situation."

**Transition Cue:**

The reading organizes those concerns around correctness, performance, and
scalability.

---

## Slide 8 - Textbook Review: Three Design Concerns

**Delivery Category:** Core

**Slide Text:**

When designing an algorithm, ask:

1. Is it correct?
2. Is the performance reasonable?
3. Can it scale when the data or demand grows?

**Instructor Notes:**

This is a returning anchor from Week 1, now used as a strategy-comparison
frame. Make students hear the continuity: the course is building one reasoning
habit in layers.

**Transition Cue:**

The reading also includes a theory-heavy skim section.

---

## Slide 9 - Textbook Review: Theory Vocabulary

**Delivery Category:** Core

**Slide Text:**

The reading includes skim-level vocabulary:

- polynomial
- NP-Hard
- NP-Complete

For this course:

- recognize the terms
- understand why some problems are harder
- do not try to master formal proof

**Instructor Notes:**

This slide is a pressure release. Tell students directly that the textbook is
giving a broader computer-science treatment.

They should understand that some problems become difficult because the search
space grows too quickly, but they do not need formal complexity theory.

**Transition Cue:**

The practical part of the chapter is strategy selection.

---

## Slide 10 - Textbook Review: Strategy Families

**Delivery Category:** Core

**Slide Text:**

The reading introduces strategy families:

- divide and conquer
- dynamic programming
- greedy strategy

It also presents larger examples:

- PageRank
- linear programming

**Instructor Notes:**

Frame the large examples as orientation. PageRank and linear programming show
that algorithm design matters in real systems, but students will not implement
full versions today.

**Transition Cue:**

Start with the three design concerns as comparison criteria.

---

# Design Concerns

## Slide 11 - Correctness

**Delivery Category:** Core

**Slide Text:**

Correctness asks:

- Did the algorithm produce the expected result?
- Did it handle normal cases?
- Did it handle edge cases?
- Can we show evidence?

**Instructor Notes:**

Reinforce that correctness comes before speed. A fast wrong answer is still
wrong.

Use this phrase if helpful: "Correctness is the entry ticket. It is not the
whole evaluation."

**Transition Cue:**

Once the answer is correct, we can ask how much work the strategy does.

---

## Slide 12 - Performance

**Delivery Category:** Core

**Slide Text:**

Performance asks:

- How much work does the strategy do?
- Does it repeat unnecessary work?
- How does the work grow?
- Is this approach reasonable for the problem size?

**Instructor Notes:**

Connect to Week 2. Students do not need a formal proof for every strategy, but
they should be able to describe repeated work and likely growth.

**Transition Cue:**

Performance on today's input does not always predict future fit.

---

## Slide 13 - Scalability

**Delivery Category:** Core

**Slide Text:**

Scalability asks:

- What happens with larger data?
- What happens with more users?
- What happens with frequent updates?
- Can the approach adapt when demand changes?

**Instructor Notes:**

Use "elasticity" carefully. At this level, explain it as the ability to handle
changing scale when resources or demand change.

Do not turn this into a cloud architecture lecture.

**Transition Cue:**

These three concerns help students compare strategies.

---

## Slide 14 - Strategy Comparison Frame

**Delivery Category:** Core

**Slide Text:**

Compare strategies by asking:

| Criterion | Strategy A | Strategy B |
| --- | --- | --- |
| Correctness |  |  |
| Readability |  |  |
| Growth |  |  |
| Fit to data |  |  |

**Instructor Notes:**

This table mirrors Lab 05. Students should see this table as the backbone of
the assignment.

Tell them that "readability" is not a soft extra. If they cannot explain the
strategy, they may not truly understand it.

**Transition Cue:**

The recommendation must be conditional.

---

## Slide 15 - Better Means Better For This Context

**Delivery Category:** Core

**Slide Text:**

Avoid:

- "This strategy is better."

Prefer:

- "This strategy is better for this problem because..."
- "This strategy may not be better when..."

**Instructor Notes:**

This is one of the most important communication slides. Students often want
absolute answers. Strategy selection is usually contextual.

Connect to professional practice: developers must justify fit, not just name a
technique.

**Transition Cue:**

Evidence keeps recommendations honest.

---

## Slide 16 - Evidence For Strategy Choice

**Delivery Category:** Core

**Slide Text:**

Evidence may include:

- test cases
- edge cases
- trace tables
- decision trees
- timing results
- comparison tables
- limitation notes

**Instructor Notes:**

This slide links directly to Lab 05 requirements. It also reinforces the
course-wide expectation that claims need evidence.

**Transition Cue:**

Now handle the reading's theory-heavy terms without letting them take over.

---

# Theory Orientation

## Slide 17 - Polynomial, In Plain Language

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

Polynomial growth uses powers of input size.

Examples:

- n
- n2
- n3

For now, connect it to growth vocabulary, not formal proof.

**Instructor Notes:**

Use this gently. Some students may be intimidated by the word "polynomial."
Translate it as "growth that can be described with powers of n."

Connect it to O(n) and O(n2) from Week 2.

**Transition Cue:**

The harder vocabulary describes problems that resist efficient solutions.

---

## Slide 18 - NP-Hard And NP-Complete: Recognition Only

**Delivery Category:** Instructor Reserve

**Slide Text:**

For this course:

- NP-Hard means very hard problem family
- NP-Complete means a special class of hard decision problems
- exact definitions require more theory

Main takeaway:

- some problems become hard very quickly

**Instructor Notes:**

Do not overteach this. The goal is recognition and humility, not mastery.

If students ask, explain that these terms matter because they warn developers
that a simple efficient solution may not exist for every problem.

**Transition Cue:**

When exact efficient solutions are hard, strategy choice becomes even more
important.

---

## Slide 19 - Why This Vocabulary Matters

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

Advanced complexity vocabulary helps developers ask:

- Is an exact solution realistic?
- Is a good-enough solution acceptable?
- Should we limit the problem size?
- Should we use a heuristic?
- Should we ask for expert review?

**Instructor Notes:**

This is the practical bridge. Students may never prove NP-completeness, but
they can learn to recognize when a problem may need approximation, constraints,
or expert help.

**Transition Cue:**

The course focus returns to usable strategy patterns.

---

## Slide 20 - Do Not Panic Over Theory

**Delivery Category:** Core

**Slide Text:**

You are not expected to master formal complexity theory today.

You are expected to:

- recognize that problem difficulty varies
- connect strategy choice to constraints
- explain tradeoffs honestly
- use AI and references carefully

**Instructor Notes:**

This slide protects learning confidence. Students need permission to not fully
absorb the advanced theory while still taking it seriously.

**Transition Cue:**

Now move to strategies students can recognize and use.

---

## Slide 21 - Strategy Is A Design Decision

**Delivery Category:** Core

**Slide Text:**

A strategy decides how the problem will be attacked.

Examples:

- try everything
- split the problem
- reuse earlier results
- choose the best-looking next step
- follow a recursive structure

**Instructor Notes:**

Use this as a clean conceptual reset after the theory slides. Students should
see strategy families as ways of thinking, not just names.

**Transition Cue:**

Before named strategies, recall the simplest strategy: direct attempt.

---

## Slide 22 - Brute Force As Baseline

**Delivery Category:** Core

**Slide Text:**

Brute force tries possibilities directly.

It can be useful when:

- the data is small
- correctness matters more than speed
- the baseline helps test another strategy

It can struggle when possibilities grow quickly.

**Instructor Notes:**

Brute force should not be mocked. It is often the clearest baseline for small
problems and for verifying a smarter method.

Connect to Lab 05 options involving brute force versus greedy selection.

**Transition Cue:**

One way to improve over direct attempt is to split the problem.

---

# Algorithmic Strategies

## Slide 23 - Divide And Conquer

**Delivery Category:** Core

**Slide Text:**

Divide and conquer:

1. divide the problem
2. solve smaller pieces
3. combine the results

Common examples:

- merge sort
- binary search
- some recursive strategies

**Instructor Notes:**

Connect this back to Weeks 4 and 5. Binary search divided the search space.
Merge sort divided the data and combined sorted pieces.

Do not imply every recursive algorithm is divide and conquer.

**Transition Cue:**

The key question is whether the smaller pieces can be combined cleanly.

---

## Slide 24 - Divide And Conquer Fit

**Delivery Category:** Core

**Slide Text:**

Divide and conquer fits when:

- the problem can be split
- smaller pieces are similar to the whole
- results can be combined
- splitting reduces the work or complexity

**Instructor Notes:**

Use this slide to make strategy fit explicit. Students should not choose divide
and conquer just because it sounds impressive.

**Transition Cue:**

Another strategy avoids repeating work by saving earlier results.

---

## Slide 25 - Dynamic Programming

**Delivery Category:** Core / Optional Deepening

**Slide Text:**

Dynamic programming is useful when:

- the problem has repeated subproblems
- earlier results can be saved
- saved results prevent repeated work

For this course: recognize the pattern.

**Instructor Notes:**

Keep this recognition-level unless the group is ready. Do not teach full DP
table design here.

Use a simple phrase: "If you keep solving the same smaller problem again, maybe
you should remember the answer."

**Transition Cue:**

Dynamic programming saves past work. Greedy strategies make local choices.

---

## Slide 26 - Greedy Strategy

**Delivery Category:** Core

**Slide Text:**

A greedy strategy chooses what looks best right now.

Examples:

- choose the cheapest item first
- choose the shortest task first
- choose the largest coin first
- choose the highest immediate score

**Instructor Notes:**

Greedy is easy to understand and often tempting. Emphasize that the local best
choice may or may not lead to the best overall result.

**Transition Cue:**

The risk is that local best does not always mean global best.

---

## Slide 27 - Greedy Risk

**Delivery Category:** Core

**Slide Text:**

Greedy strategies can fail when:

- an early choice blocks a better later choice
- the local score hides a global tradeoff
- the rule does not match the real goal

Greedy needs evidence.

**Instructor Notes:**

Use a small shopping or scheduling example if needed. Cheapest-first might buy
many low-value items and miss the best overall value.

This directly supports Lab 05 option paths.

**Transition Cue:**

Now compare the main strategy families.

---

## Slide 28 - Strategy Family Comparison

**Delivery Category:** Core

**Slide Text:**

| Strategy | Basic Idea | Watch For |
| --- | --- | --- |
| Brute force | try possibilities | too much work |
| Divide and conquer | split and combine | combine step |
| Dynamic programming | reuse saved results | identifying repeated subproblems |
| Greedy | best-looking next step | local choice may fail |

**Instructor Notes:**

This table is a recognition anchor. Students should not be expected to master
all implementation patterns today.

**Transition Cue:**

The textbook also uses PageRank as a larger strategy example.

---

## Slide 29 - PageRank As An Example

**Delivery Category:** Instructor Reserve

**Slide Text:**

PageRank is an example of algorithmic strategy at scale.

It considers:

- links between pages
- importance passed through relationships
- repeated updating of scores
- ranking based on structure

**Instructor Notes:**

Keep this conceptual. The purpose is to show that strategy families and data
relationships matter in real systems.

Do not derive PageRank mathematically. Connect it to graphs and ranking, which
return in later weeks.

**Transition Cue:**

PageRank also previews why graphs matter next week.

---

## Slide 30 - PageRank: What To Notice

**Delivery Category:** Instructor Reserve

**Slide Text:**

Notice the algorithmic questions:

- What is represented?
- What is repeated?
- What score changes over time?
- What does the rank claim?
- What are the limits of that claim?

**Instructor Notes:**

This is a bridge to explainability and limits. Ranking is not the same as truth
or quality. It is a result of a representation and scoring process.

**Transition Cue:**

The reading also introduces optimization under constraints.

---

## Slide 31 - Linear Programming: Recognition

**Delivery Category:** Instructor Reserve

**Slide Text:**

Linear programming helps optimize under constraints.

Plain-language frame:

- choose values
- follow constraints
- maximize or minimize a goal

For this course: recognize the idea.

**Instructor Notes:**

Keep this recognition-only. Students do not need simplex method or formal
linear optimization.

Connect it to scheduling, shopping, resource allocation, or budget examples.

**Transition Cue:**

This reinforces a broader point: strategy depends on constraints.

---

## Slide 32 - Constraints Shape Strategy

**Delivery Category:** Core

**Slide Text:**

The same problem can change strategy when constraints change.

Examples:

- exact answer required
- good-enough answer acceptable
- small data
- large data
- limited memory
- explanation required

**Instructor Notes:**

This slide brings the reserve examples back to the core lesson. Constraints
are not decoration; they determine which strategy is reasonable.

**Transition Cue:**

Now bring strategy back to code forms students can implement.

---

## Slide 33 - Strategy Before Code

**Delivery Category:** Core

**Slide Text:**

Before coding, describe:

- Strategy A
- Strategy B
- what each strategy assumes
- what evidence will compare them
- what would make one a better fit

**Instructor Notes:**

This slide directly supports Lab 05's requirement for two strategy
descriptions before code.

Make clear that "I wrote two functions" is not enough.

**Transition Cue:**

Two common implementation forms are iteration and recursion.

---

## Slide 34 - Same Strategy, Different Form

**Delivery Category:** Core

**Slide Text:**

Sometimes the strategy changes.

Sometimes the representation changes.

Sometimes both solutions solve the same task, but one fits the data shape more
clearly.

**Instructor Notes:**

This prepares the demo. The iterative and recursive donation-envelope demo
produces the same total, but the recursive form matches nested data more
directly.

**Transition Cue:**

Now define iteration and recursion.

---

# Iteration and Recursion

## Slide 35 - Iteration

**Delivery Category:** Core

**Slide Text:**

Iteration repeats steps using a loop.

Common signs:

- `for`
- `while`
- running total
- index or counter
- explicit work list or stack

**Instructor Notes:**

Students are already familiar with loops. The new point is that iteration is a
strategy form they can compare against recursion or other approaches.

**Transition Cue:**

Recursion repeats by calling a smaller version of the problem.

---

## Slide 36 - Recursion

**Delivery Category:** Core

**Slide Text:**

Recursion happens when a function solves a smaller version of the same problem.

It needs:

- a base case
- a recursive step
- progress toward stopping

**Instructor Notes:**

Use very plain language. The base case is the condition where the function
stops calling itself.

Emphasize progress toward stopping. Without progress, recursion does not end.

**Transition Cue:**

The base case is the safety rail.

---

## Slide 37 - Base Case

**Delivery Category:** Core

**Slide Text:**

The base case answers:

- When are we done?
- What result can we return directly?
- How do we stop the repeated calls?

No base case means no reliable recursion.

**Instructor Notes:**

This is a common student failure point. Ask students to identify the base case
before looking at code.

**Transition Cue:**

A trace makes recursive behavior visible.

---

## Slide 38 - Recursive Trace

**Delivery Category:** Core

**Slide Text:**

A recursive trace can show:

- call depth
- current input
- action taken
- returned result
- how totals combine

**Instructor Notes:**

Connect this to observable algorithm behavior. A trace is not busywork; it is
evidence that the student understands the hidden call structure.

**Transition Cue:**

Now compare recursion and iteration without declaring one universally better.

---

## Slide 39 - Iteration vs Recursion

**Delivery Category:** Core

**Slide Text:**

| Question | Iteration | Recursion |
| --- | --- | --- |
| How does it repeat? | loop | function calls itself |
| What must be tracked? | loop state | call state and base case |
| When does it fit? | flat repeated work | nested or self-similar work |

**Instructor Notes:**

Tell students that iteration and recursion can sometimes solve the same
problem. The question is which one is clearer, safer, and better matched to the
data shape.

**Transition Cue:**

The demo makes that comparison visible.

---

# Demo Bridge

## Slide 40 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo: nested donation envelopes.

We will calculate a total using:

- iterative processing with a work stack
- recursive processing of nested groups

**Instructor Notes:**

Use the existing Lab 05 demo. The donation-envelope scenario is intentionally
different from the student lab options.

Make clear that both strategies can be correct.

**Transition Cue:**

First, show the nested data shape.

---

## Slide 41 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

The demo produces:

- iterative total
- recursive total
- recursive call trace
- strategy comparison table
- key takeaway

**Instructor Notes:**

Do not rush the trace. Students need to see depth, action, and return behavior.

Use the trace to ask: "Where is the base case?" and "What smaller problem is
being solved?"

**Transition Cue:**

The comparison table turns the output into strategy reasoning.

---

## Slide 42 - Demo Comparison

**Delivery Category:** Core

**Slide Text:**

Compare:

- correctness
- readability
- growth
- fit to data

The answer alone is not the whole evaluation.

**Instructor Notes:**

The demo's recursive strategy matches nested data more naturally, while the
iterative strategy still works with extra bookkeeping.

This is the exact reasoning pattern students need for Lab 05.

**Transition Cue:**

Now model the explanation sentence students should be able to write.

---

## Slide 43 - Demo Explanation Pattern

**Delivery Category:** Core

**Slide Text:**

Example explanation:

> Both strategies produce the same total. The recursive strategy fits the
> nested data more directly because each nested group can be treated as a
> smaller version of the same problem.

**Instructor Notes:**

Encourage students to use their own words, but preserve the logical pattern:
same result, strategy difference, fit reason, condition.

**Transition Cue:**

Now transfer the same comparison pattern into Lab 05.

---

# Lab Bridge

## Slide 44 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 05, you will compare two strategies for a different problem.

Possible options include:

- cumulative product
- grouped values
- decision tree
- coin-change or greedy selection
- scheduling or shopping tradeoffs

**Instructor Notes:**

Stress that students should not copy the demo scenario. The demo gives the
comparison pattern; the lab uses different problems.

**Transition Cue:**

The lab requires strategy descriptions before code.

---

## Slide 45 - Lab 05 Evidence

**Delivery Category:** Core

**Slide Text:**

Your evidence should include:

- problem statement
- two strategy descriptions
- two implementations or simulations
- at least four tests
- trace, decision tree, or comparison table
- recommendation and limitation

**Instructor Notes:**

This is essentially the checklist students need before submitting. Keep it
practical and tie it to the README.

**Transition Cue:**

The recommendation should use the comparison table.

---

## Slide 46 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should show:

- what problem you solved
- what two strategies you compared
- what tests you ran
- what evidence you collected
- which strategy you recommend
- when your recommendation might change

**Instructor Notes:**

Reinforce that GitHub submission should include both code and explanation.

The README is where students make their thinking visible.

**Transition Cue:**

Clarify the AI-use boundary.

---

## Slide 47 - AI Use In Lab 05

**Delivery Category:** Core

**Slide Text:**

Use AI after you have:

- framed the problem
- described your first strategy
- attempted or planned evidence

AI may help:

- suggest a second strategy
- critique tradeoffs
- debug one implementation

**Instructor Notes:**

Make the boundary clear. AI can suggest a second strategy, but the student must
test it and explain it.

If AI generates code, students must explain the strategy in their own words.

**Transition Cue:**

Now close with the main lesson.

---

# Wrap-Up

## Slide 48 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Strategy choice is contextual.

Ask:

- Does it produce the expected result?
- Is it readable enough to explain?
- How does the work grow?
- Does it fit the data shape?
- What tradeoff did I accept?

**Instructor Notes:**

This is the Week 5 takeaway. Students should carry this directly into Lab 05
and the final assessment.

**Transition Cue:**

Now make the immediate next action concrete.

---

## Slide 49 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 05:

- choose a problem
- describe two strategies
- implement or simulate both
- create at least four tests
- collect visible evidence
- recommend one strategy with a limitation

**Instructor Notes:**

Remind students that the goal is not to prove one strategy is always best. The
goal is to justify which strategy fits their chosen problem.

**Transition Cue:**

Prepare students for the next reading once Week 6 reading details are assigned.

---

## Slide 50 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

For next week, read for connected systems.

Focus on:

- graph basics: nodes, edges, links, and networks
- graph representation
- simple, directed, undirected, and weighted graphs
- ego networks and neighborhoods
- shortest path intuition
- BFS and DFS traversal

Optional reading includes centrality, density, triangles, graph visualization,
and social network analysis.

**Instructor Notes:**

This slide prepares students for the Week 6 reading. Emphasize that graph
terminology uses familiar words in precise ways. Words like "network,"
"neighbor," and "path" should be read as graph-model terms.

Also prepare students for formula-heavy sections. They should not try to master
centrality formulas before class. The required focus is graph representation,
BFS, DFS, and explaining what the model shows and leaves out.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 3 | Strategy comparison | Clean visual showing one problem splitting into two different solution paths that rejoin at evidence | Avoid implying both paths are always equal |
| 8 | Three design concerns | Triangle or three-column visual for correctness, performance, and scalability | Keep labels plain and avoid dense theory imagery |
| 17 | Polynomial recognition | Simple growth curve labels for n, n2, n3 with "recognize, do not panic" feeling | Avoid formal equation-heavy visuals |
| 23 | Divide and conquer | Problem block splitting into smaller blocks and recombining | Do not make it look like generic business decomposition |
| 25 | Dynamic programming | Small repeated subproblem cards being stored and reused | Avoid implying students must build a full DP table |
| 27 | Greedy risk | Path choice where the nearest reward blocks a better later outcome | Keep it simple and not game-like unless useful |
| 38 | Recursive trace | Nested boxes or call stack visual showing depth and return | Do not replace the actual demo trace |
| 41 | Demo evidence | Nested envelopes or nested containers leading to a total and trace table | Use as support only; demo output remains primary |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 12 min | Use only Slides 2-3 | Discuss one Lab 04 trace example |
| Textbook Review | 18 min | Summarize theory vocabulary verbally | Add examples for requirements and constraints |
| Design Concerns | 20 min | Combine Slides 11-16 | Add student examples of strategy recommendations |
| Theory Orientation | 15 min | Use only Slides 19-20 | Discuss why some problems need heuristics |
| Algorithmic Strategies | 35 min | Use Slide 28 as summary anchor | Add examples for divide and conquer, DP, and greedy |
| Iteration and Recursion | 25 min | Use Slides 35-37 only | Trace a small recursive example on board |
| Demo | 20 min | Show one recursive trace and comparison table | Ask students to predict base case and total |
| Lab Bridge | 10 min | Combine Slides 44-47 | Walk through README expectations |

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
