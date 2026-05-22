# Rubric Evaluation v2

## Purpose

This rubric adapts the original `119` evaluation model for the v2 course
direction. It preserves consistent grading categories while reducing the
requirement that every lab contain a full AI-assisted implementation.

AI remains important, but the core of the course is algorithmic judgment:
framing, implementation, correctness, efficiency, evidence, comparison, and
explanation.

## AI Involvement Levels

The course uses the program AI progression:

```text
Manual First -> AI-Assisted -> AI-Injected -> AI-Integrated
```

- Manual First: the student frames the problem and attempts reasoning before AI.
- AI-Assisted: AI supports explanation, research, critique, or comparison.
- AI-Injected: AI provides coding help or code revision; the student must
  justify and explain the output.
- AI-Integrated: AI acts as a refraction-based collaborator in a larger
  structured process. This is optional in `119`.

## Standard Lab Rubric

### Category 1 - Problem Framing: 20%

Exceeds:

- Clearly defines the problem, inputs, outputs, constraints, assumptions, and
  edge cases.
- Shows structured thinking before implementation.

Meets:

- Defines the problem with minor gaps.
- Identifies most inputs, outputs, and constraints.

Developing:

- Gives an incomplete or partially unclear framing.
- Misses important assumptions or edge cases.

Needs Improvement:

- Provides vague, missing, or incorrect problem definition.

### Category 2 - Implementation or Simulation: 20%

Exceeds:

- Produces a correct, readable, well-structured Python implementation,
  pseudocode, simulation, or model appropriate to the lab.
- Demonstrates understanding of the algorithmic steps.

Meets:

- Produces a mostly correct solution with minor issues.

Developing:

- Produces a partially working solution with significant logic gaps.

Needs Improvement:

- Produces a non-functional, missing, or unexplained solution.

### Category 3 - Correctness and Testing: 20%

Exceeds:

- Tests normal cases, edge cases, and failure or assumption-bound cases.
- Explains why the results support correctness.

Meets:

- Tests reasonable cases and identifies expected outcomes.

Developing:

- Provides limited testing or weak explanation of results.

Needs Improvement:

- Provides little or no meaningful correctness check.

### Category 4 - Efficiency, Tradeoffs, and Evidence: 20%

Exceeds:

- Compares efficiency, readability, simplicity, assumptions, and maintainability.
- Uses Big-O vocabulary, timing data, traces, diagrams, charts, or other
  evidence appropriately.

Meets:

- Provides a basic comparison with some evidence.

Developing:

- Provides surface-level comparison or unsupported claims.

Needs Improvement:

- Provides no meaningful evaluation of efficiency or tradeoffs.

### Category 5 - Explanation and Communication: 15%

Exceeds:

- Explains the solution clearly to a technical or non-technical audience.
- Justifies the chosen approach using appropriate vocabulary.
- Identifies limitations and next steps.

Meets:

- Explains the solution and main decision points adequately.

Developing:

- Gives a limited or unclear explanation.

Needs Improvement:

- Cannot explain how the solution works or why it was chosen.

### Category 6 - AI Accountability When Used: 5%

Exceeds:

- Uses AI intentionally after providing context or prior thinking.
- Correctly identifies whether the use was AI-Assisted, AI-Injected, or
  AI-Integrated.
- Validates AI output and identifies assumptions, limitations, or needed
  changes.
- Clearly states what was accepted, changed, or rejected.

Meets:

- Uses AI appropriately with basic validation.

Developing:

- Uses AI with limited evaluation or weak disclosure.

Needs Improvement:

- Copies AI output without understanding, validation, or attribution.

Not Applicable:

- If AI is not used or not allowed for a specific lab, this category may be
  redistributed to correctness, evidence, or explanation at instructor
  discretion.

## Student AI Prompt Guidance

AI should be given the student's thinking first.

Baseline prompt:

```text
I am solving the following problem:
[problem description]

My current understanding is:
[inputs, outputs, constraints, assumptions]

My intended approach is:
[student's plan or pseudocode]

Review my approach or suggest an implementation. Explain your reasoning and
identify assumptions I should verify.
```

Evaluation prompt:

```text
Here is my current solution:
[code or pseudocode]

Evaluate it for:
- correctness
- edge cases
- efficiency
- readability
- assumptions

Suggest improvements, but also explain tradeoffs.
```

## Instructor Observation Guide

Watch for:

- immediate AI use before problem framing
- copied solutions the student cannot explain
- untested assumptions
- confusion between "runs" and "is correct"
- performance claims without evidence
- inability to explain why one approach was chosen

Useful instructor questions:

- What problem are you solving?
- What assumption does this approach require?
- What input would break this?
- What changes when the input gets much larger?
- Why did you choose this data structure?
- What would you do if AI or a library was not available?
- How would you explain this to someone who does not code?

## Quiz Model

Quizzes should reinforce reasoning rather than syntax trivia.

Appropriate quiz types:

- identify valid preconditions, such as when binary search is allowed
- choose a data structure for a scenario and justify the choice
- compare growth patterns
- identify an edge case
- trace a small algorithm
- explain why an AI-generated solution is incomplete or risky

Avoid:

- memorization-heavy algorithm trivia
- long hand-calculation complexity proofs
- language syntax details that do not support algorithmic reasoning
