# Demo Authoring Guidelines

Course: 10-152-119 Introduction to Algorithms | October 9, 2026

## Purpose and Presentation

Every demo solves a concrete problem, including deliberately small or fictional ones. Ordinary application output presents a useful answer in user-oriented language. Technical evidence is labeled and reserved for a teaching/debugging context, not treated as the application's normal interface.

A teaching walkthrough may explicitly expose ambiguity, precise rules, plain English, pseudocode, Python, expected/actual results, an isolated failure, revision, and the useful final result. This is instructional output, distinct from application output. Deliberately incorrect code must be clearly identified and confined to the walkthrough; expected results must be independently specified.

Keep daily demos focused and independent of the Learning Resource Navigator. Navigator milestone demonstrations remain additional reinforcement. Do not add frameworks, application shells, or unfamiliar Python machinery solely for convenience.

Give every function a short purpose-focused docstring. Use it to explain the responsibility before walking through the implementation; avoid comments or docstrings that merely restate individual statements. W01D01 now demonstrates this habit in both application and test functions.

## Standard Test Separation

- Each demo contains `main.py`, student `README.md`, instructor-only `notes.md`, and `test_demo.py`.
- Put comprehensive regression assertions in `test_demo.py`, importing the local application functions. Application code must not import or run its test file.
- Run `py -3.14 main.py` for the demonstration and `py -3.14 test_demo.py` for verification. Only the test run prints `Checks passed.`
- Maintain independently stated expected results, boundaries, empty/no-match cases, invalid data, and relevant state-preservation checks. Do not calculate expectations using the implementation being tested.
- Use explicit runtime validation for unsafe input or invalid measurements; moving assertions is not a reason to remove application safeguards.
- Keep visible expected/actual comparisons in the walkthrough. Assertions must not replace the teaching explanation. A focused assertion can be explained in the test file when revisiting that concept, without requiring students to study the full suite.
- Run the collection verifier from an unrelated working directory as well as individual scripts. Reject optimized verification rather than silently passing with assertions disabled.
- Instructor notes remain Git-ignored; test files remain student-accessible. Tests do not imply a new assignment requirement unless specified separately.

All 22 current Python demos now use this file separation. Week 1 now separates useful reports from guided teaching walkthroughs; later weeks still require individual presentation reviews.

W01D01 now implements a small menu separating the useful report from a six-step teaching walkthrough, including discussion pauses, an isolated 50% boundary failure, corrected expected/actual comparisons, and the final report. Its old trace machinery is removed. Tuesday adds purposeful boundary/invalid cases and repair; Thursday uses named rules to distinguish refactor parity from a laptop-only requirement. Both end with useful reports.

## Bounded Python Enhancements

Each enhancement needs an explicit introduction, a concrete purpose, and limited scope. Reuse familiar patterns afterward; do not introduce new syntax merely because a library supports it.

| Demo | Proposed enhancement | Boundary |
| --- | --- | --- |
| W01D01 and remaining Week 1 demos | Familiar function arguments and explicit expected/actual comparisons | No parser prerequisite; comprehensive assertions stay in tests |
| W02D02: Benchmark Controls | First `argparse` introduction, using `--size` | `ArgumentParser`, one `add_argument` with `type=int`/default, `parse_args`, `--help`, existing 1-20000 range validation |
| W05D03: Memoization Call Counts | Reuse the integer-option pattern for `--n` | Preserve the small safe recursion bound; no new parser abstraction |
| W06D03: Restricted Routes | Extend to multiple values with `--blocked` | Explain `nargs` and list output explicitly; distinguish parsing from route logic |
| W07D02: Weighted Song Ranking | Extend to constrained choices with `--emphasis` | Explain `choices`; retain clear defaults and ranking rules |

Suggested W02D02 sequence: first run the known default benchmark; ask how to change dataset size without editing code; show the small parser block; run a different size and `--help`; show one rejected input. Keep parser setup outside measured work and pass its integer result into existing algorithm functions.

Allow approximately 3-5 minutes in the lecture before the daily benchmark demonstration, not additional time silently added to its 12-18 minute delivery budget. If unavailable, postpone the enhancement rather than compress the core comparison/correctness discussion. Later recurrence/route/ranking introductions should explicitly revisit only the parser feature needed that day.

This is a proposed placement for evaluation, not a completed lecture-outline revision or a requirement to add a parser to every subsequent demo. Existing later parser code is available; its instructional integration still needs to be reflected when lecture outlines are regenerated.
