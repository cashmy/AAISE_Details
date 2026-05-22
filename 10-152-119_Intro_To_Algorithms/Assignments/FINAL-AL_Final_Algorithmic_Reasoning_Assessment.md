# FINAL ALGORITHMIC REASONING ASSESSMENT

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This artifact defines the final assessment model for `10-152-119 Algorithmic
Problem Solving`.

This course does not use a traditional capstone project as the primary final
assessment. A large build project does not fit the main course goal as well as
a structured algorithmic reasoning assessment.

The final is designed to verify that students can:

- create working algorithmic solutions
- use data structures and algorithms appropriately
- test and submit evidence
- use AI responsibly when allowed
- explain the solution they submitted
- identify assumptions, weaknesses, and tradeoffs

The final should reflect a realistic development situation: working code
matters, imperfect code still has value, and explanation is used to verify
understanding rather than punish students.

---

# Assessment Structure

The final has two parts.

```text
Part 1 - Applied Solution Set
Part 2 - Personalized Explanation Defense
```

Part 1 produces the submitted work.

Part 2 verifies student understanding of the submitted work.

---

# Assessment Philosophy

This final is not a gotcha assessment.

Students should not be punished simply because they used AI, rehearsed an
explanation, or produced code that works but is not elegant. Those are all
realistic conditions in modern technical work.

The assessment rewards:

- getting something working
- submitting evidence
- being able to explain what was built
- recognizing where the solution is weak
- showing responsible use of tools

The highest scores still require deeper reasoning, but a functioning solution
with basic explanation should represent meaningful achievement.

---

# Part 1 - Applied Solution Set

## Purpose

Students complete several bounded algorithmic tasks and submit their solutions.

The tasks should be large enough to require reasoning, but small enough to
finish within the final assessment window.

## Student Deliverables

Students submit:

- code, pseudocode, or documented simulation as required by each task
- tests or sample runs
- visible evidence such as a trace, timing table, comparison table, chart, or
  diagram
- a short AI-use statement
- brief notes explaining assumptions or limitations

## Possible Task Types

The solution set may include several of the following:

- choose and use an appropriate data structure
- implement or compare search behavior
- evaluate two algorithmic approaches
- produce timing or growth evidence
- model a small system as a graph
- create a ranking, similarity, clustering, or hashing example
- explain assumptions and edge cases
- revise or critique an AI-assisted solution

## AI Use

AI may be allowed in Part 1.

If AI is used, students must disclose:

- what AI helped with
- what they changed
- what they tested
- what they still understand and own

AI use is acceptable, but unexamined AI output is not.

---

# Part 2 - Personalized Explanation Defense

## Purpose

Part 2 verifies that students understand the submitted solution set.

The instructor reviews each student's Part 1 submission and creates
personalized follow-up questions. A Codex-style LLM may help analyze the
submission and draft questions, but the instructor remains responsible for the
final questions and scoring.

## Format

Part 2 may be delivered as:

- an online interactive test
- a short oral check
- a written response set
- a live or recorded explanation
- an LMS quiz with personalized questions

The preferred model is an online interactive test that asks students to explain
their own submitted work.

## Question Intent

Questions should verify understanding, not trap the student.

Good questions ask students to explain:

- what a function or section of code does
- why a data structure was chosen
- what assumption the solution depends on
- what test proves or fails to prove
- what happens for a specific edge case
- where the solution is inefficient
- what AI contributed, if AI was used
- what the student would improve with more time

Questions should avoid:

- obscure trivia
- unrelated textbook recall
- punishing different valid approaches
- asking about code the student did not submit
- treating imperfect code as automatically failed work

---

# Suggested Grade Weighting

The final assessment should heavily reward functioning submitted work.

Suggested weighting:

| Component | Weight | Purpose |
| --- | ---: | --- |
| Part 1 - Applied Solution Set | 70% | Rewards working solutions, evidence, testing, and submitted artifacts |
| Part 2 - Explanation Defense | 30% | Verifies ownership, understanding, assumptions, tradeoffs, and AI accountability |

## Score Interpretation

Working code that actually solves the assigned task should account for a large
portion of the grade, even if the code is not elegant.

Part 2 can raise a student into the `80-85%` range through credible explanation
of a working or mostly working solution, even if the explanation is rehearsed.

Higher scores should require stronger evidence of adaptive understanding:

- explaining edge cases
- identifying weaknesses
- comparing approaches
- describing efficiency tradeoffs
- justifying AI-assisted choices
- proposing reasonable improvements

---

# Suggested Part 1 Scoring

| Category | Suggested Weight | Notes |
| --- | ---: | --- |
| Working solutions | 35% | Code or simulation runs and addresses the assigned task |
| Problem framing and assumptions | 10% | Inputs, outputs, constraints, and assumptions are stated |
| Testing and evidence | 15% | Tests, traces, timing, tables, charts, or diagrams support the solution |
| Algorithm/data structure fit | 15% | Approach and representation fit the problem reasonably |
| AI-use disclosure and accountability | 10% | AI use is disclosed and validated when applicable |
| Submission completeness and clarity | 15% | Work is organized, readable, and complete enough to review |

The instructor may adjust these weights depending on the exact final task set.

---

# Suggested Part 2 Scoring

| Category | Suggested Weight | Notes |
| --- | ---: | --- |
| Basic explanation of submitted code | 35% | Student can explain what the solution does |
| Correctness and evidence explanation | 20% | Student can connect tests or evidence to correctness |
| Assumptions and edge cases | 15% | Student can identify limits or fragile points |
| Tradeoff and efficiency awareness | 15% | Student can discuss performance, readability, or alternate approaches |
| AI accountability, if applicable | 15% | Student can explain what AI contributed and how it was checked |

If AI was not used, the AI accountability points may be redistributed across
the other categories.

---

# Personalized Question Generation Guide

After reviewing a student's Part 1 submission, create `4-8` questions.

A useful question set should include:

1. One basic walkthrough question.
2. One correctness or testing question.
3. One assumption or edge-case question.
4. One tradeoff or efficiency question.
5. One AI-use question, if AI was used.
6. One improvement question, if appropriate.

## Instructor/Codex Prompt

Use this prompt with a Codex-capable LLM when drafting personalized questions.

```text
You are helping create Part 2 explanation-defense questions for
10-152-119 Algorithmic Problem Solving.

This is not a gotcha assessment. The goal is to verify that the student
understands the submitted work and can explain assumptions, tests, tradeoffs,
and AI use where applicable.

Read the student's Part 1 submission files.

Create 4-8 personalized questions.

Question requirements:
- ask about the student's submitted work
- include at least one basic walkthrough question
- include at least one correctness or testing question
- include at least one assumption or edge-case question
- include at least one tradeoff or efficiency question
- include an AI accountability question if AI was used or disclosed
- avoid obscure trivia or unrelated textbook recall
- do not assume the solution is wrong only because it is imperfect

For each question, include:
- the question
- what the question is trying to verify
- what a minimally acceptable answer should include
- what a stronger answer would add
```

---

# Example Personalized Questions

## Basic Walkthrough

> Explain what your main function does from input to output.

Verifies that the student understands the overall flow of the submitted
solution.

## Correctness and Evidence

> Which test case gives you the most confidence that your solution works, and
> why?

Verifies that the student can connect evidence to correctness.

## Assumption or Edge Case

> What input would make your solution behave poorly or incorrectly?

Verifies that the student can identify limits.

## Tradeoff or Efficiency

> What is one reason your solution might be slower or less clear than another
> possible approach?

Verifies introductory performance and tradeoff awareness.

## AI Accountability

> If AI helped with this solution, what part did it contribute, and how did you
> verify that part?

Verifies responsible AI use and student ownership.

## Improvement

> If you had one more hour to improve this solution, what would you change
> first?

Verifies reflection and practical improvement judgment.

---

# Relationship to MRS-AL

This final assessment may observe all MRS-AL categories:

- **T1. Problem Framing and Algorithmic Analysis**
- **T2. Data Structures and Representation**
- **T3. Algorithm Implementation and Testing**
- **T4. Correctness, Efficiency, and Tradeoff Evaluation**
- **T5. Observable Algorithm Behavior and Communication Evidence**
- **T6. AI/Data Foundations and Responsible Tool Use**
- **C1. Solve Problems**
- **C2. Communicate Clearly**
- **C3. Work Productively**
- **C4. Value Learning**
- **C6. Act Professionally**

`C5. Work Cooperatively` should be scored only if the final includes a
collaborative component.

---

# Design Notes

- Part 1 should carry enough weight that students are rewarded for functioning
  work.
- Part 2 should verify understanding and ownership, not punish the use of help.
- Rehearsed explanation can still count because professionals often prepare to
  explain their work.
- Poor but working code can still represent a real technical scenario.
- The highest grades require students to move beyond "it works" into evidence,
  assumptions, tradeoffs, and improvement.
