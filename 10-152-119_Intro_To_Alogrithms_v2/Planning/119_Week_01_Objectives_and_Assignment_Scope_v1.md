# Week 1 Objectives and Assignment Scope

October 9, 2026 | Current instructor production baseline

## Design Authority

Use the [AL01 packet](../Assignments/AL01/AL01_Ticket_Rules_and_Regression.md),
[IIM](IIM_Matrix_v3.md), [curated readings](../Reading_Assignments.md), and
[assignment progression](119_Assignment_List_and_Progression_Map_v1.md).
This document reflects the lean, paired-development design; earlier draft
requirements for mandatory pseudocode, test counts, and duplicate writeups no
longer apply. Institutional hours and master rubric descriptors remain unchanged.

## Week 1 Objectives

| ID | Observable objective | Evidence |
| --- | --- | --- |
| W1-O1 | Interpret the practical request and its input/output and data rules | Working decisions and brief explanation; no rewritten specification |
| W1-O2 | Connect precise English rules to Python behavior | Explain the relevant condition; pseudocode is optional teaching support |
| W1-O3 | Process ticket dictionaries with validation, selection, and presentation responsibilities | Two useful lists, readable issues, order/input preservation |
| W1-O4 | Test ordinary, boundary, invalid, empty/no-match, and grouped-condition cases | Separate executable tests with independently chosen expectations |
| W1-O5 | Repair the supplied defect, revise policy, and refactor without unintended changes | Tests and brief README observations of changed/preserved behavior |
| W1-O6 | Participate in paired development and explain personal contributions and learning | Role rotation, handoffs, observed participation, individual README |

Week 1 does not require Big-O, benchmarking, sorting, recursion, graph algorithms,
or a large application architecture.

## Reading-to-Instruction Reconciliation

| Reading | Role in Week 1 | Instructional Boundary |
| --- | --- | --- |
| Ch. 1 pp. 3-7, development environment | Required selection retained from the curated list; readiness/context review | No reinstall/setup project or extended tooling lecture; students have the previously released setup materials |
| Ch. 1 p. 9 through the first portion of p. 12, ending before Performance Analysis | Required conceptual preparation before Monday | Read for explicit procedures, design decisions, and problem boundaries; detailed performance/Big-O starts in Week 2 |
| Ch. 16 pp. 458-460, explainability | Recommended context, not an assignment prerequisite | Apply the idea to a small record decision; no advanced algorithm implementation |
| Instructor-supplied record/rule/testing examples | Required learning support delivered through instruction and packet resources | Explain the chosen contract, predicates, boundary testing, AND/OR grouping, regression, and refactor evidence even if no exact textbook implementation is provided |

The page split denoted `12a`/`12b` in planning uses a heading boundary on printed page 12; student instructions should use start/stop headings. Page references retain the instructor's validation record, not a new independent textbook verification. Reading preparation remains an estimated 45-60 minutes, not a measured duration or additional written essay. Tuesday/Thursday support stays optional.


## AL01: Ticket Rules and Follow-Up

One assignment developed across three days in a shared public repository.
Each student copies the complete solution into their own class repository and
submits that URL in Schoology. No formal peer-review session or discussion post
is required for AL01.

Use the 12 supplied fictional records, including three invalid examples.

### Fixed Data Contract

| Field | Accepted Value | Boundary |
| --- | --- | --- |
| `id` | Nonempty string | Supplied usable IDs are unique; no duplicate-ID management task |
| `status` | Exactly `open` or `closed` | No additional state workflow |
| `category` | Exactly `software`, `network`, or `access` | Exact lowercase values; no text-normalization task |
| `age_days` | Integer >= 0, excluding Python booleans | Already calculated; no date/time parsing or calendar logic |
| `priority` | Exactly `low`, `normal`, or `high` | No numeric priority score or sorting requirement |

All five fields are required. Validate before using rule fields. Missing, unknown, or wrongly typed values are excluded and reported for checking, not guessed, coerced, or defaulted. The surrounding driver supplies a list of dictionaries; arbitrary objects, files, and malformed outer containers are outside the task.

Selection preserves fixture order and does not mutate input records. Returning original references versus copies is not an additional Week 1 assessment target. No general schema library or validation framework is required.

### Exactly Two Required Selection Operations

1. **Open-ticket view:** a single-criterion operation selects valid records whose status is `open`.
2. **Follow-up selection:** a combined operation applies the current follow-up policy to valid records.

Use named functions for validation, the selection rules, and presentation. A small age predicate may be factored out if useful; it is not a third required application feature. The starter interfaces should return selected records and invalid-record messages consistently. A simple `(selected, issues)` pair is the packet's default interface; issues are readable strings, not technical traces.

Normal output shows the request/policy, selected ticket IDs and useful fields, a selected count, and records needing checking. Empty/no-match results have explicit messages. A raw Python list or debug trace is not the ordinary interface. Valid nonmatches do not need a detailed technical decision log.

### Staged Rule and Revision Contract

| Stage | Rule | Purpose |
| --- | --- | --- |
| Monday baseline | Select valid open tickets | Apply a precise single criterion and establish contract/presentation responsibilities |
| Tuesday follow-up v1 | Valid AND open AND `age_days >= 2` | Apply availability/status and an inclusive boundary; systematically justify expected outcomes |
| Supplied Tuesday defect | A separate clearly labeled snippet uses `age_days > 2` instead of `>= 2` | Reproduce a failing exact-boundary case and repair it; do not supply the complete student selector |
| Thursday follow-up v2 | Valid AND open AND `age_days >= 2` AND (`priority == high` OR `category == access`) | Focus limited follow-up capacity; practice combined criteria and preserve mandatory status/age checks |
| Thursday refactor | Improve a focused responsibility/name/duplicated rule without changing v2's contract | Rerun the same expected outcomes and show behavior preservation |

The Thursday revision is an issued change, not a student-designed rules engine. An old normal-priority software ticket may now be omitted deliberately; an old open access ticket remains selected. A closed access ticket and a one-day-old high-priority ticket remain excluded. The OR condition never bypasses validation, open status, or minimum age.

Keep one active final selector, not two full maintained applications. Preserve compact v1/v2 output evidence or a version-control checkpoint to explain the policy change. Do not require a second before/after codebase or a general strategy-injection interface.

### Instructor Acceptance Checks

These cases define production checks for the fixture, demos/packet transfer, and instructor solution. Do not distribute the complete expected-result table as the student's prewritten tests; students independently justify their own expectations.

| Valid Scenario | Follow-up v1 | Follow-up v2 | Meaning |
| --- | --- | --- | --- |
| Open, software, age 1, high | Exclude | Exclude | Below boundary; high priority cannot override minimum age |
| Open, software, age 2, high | Select | Select | Inclusive boundary and preserved match |
| Open, software, age 3, normal | Select | Exclude | Intentional policy change, not a regression defect |
| Open, access, age 3, normal | Select | Select | Access category qualifies without high priority |
| Closed, access, age 3, high | Exclude | Exclude | Grouped OR cannot override open status |
| Open, access, age 1, normal | Exclude | Exclude | Access category cannot override minimum age |

Invalid records are excluded with an issue in both versions. Empty input returns empty selections/issues; a nonempty valid collection with no qualifying records returns an empty selection without falsely reporting invalid data. The independent open-ticket view retains its original rule when follow-up policy changes.


## Student Work and Support

Required files: main.py, ticket_data.py, test_assignment.py, and an individual
README; include any imported support modules. Implement the two selectors with
the packet's (selected, issues) interfaces. Normal results are useful reports,
not technical traces.

Use the packet's test coverage checklist, not a fixed number of checks.
Executable tests provide evidence; no duplicate expected/actual table or
worked-decision essay is required. Append brief observations, debugging
challenges, changes, and learnings to the README, plus assistance/contribution
notes and a reserved Instructor Comments section.

The optional full-English starter has distinct M/T/Th sections. Students wait
for each day's instruction, maintain one application, and commit progressively.
Support use requires only a brief note within normal README reflections.
Instructor solutions remain separate from student distribution. Color support
is optional; it is not an extra graded feature.

Bounded AI explanation, drafting, debugging, and refactoring are permitted after
stating intended behavior. A complete manual implementation or three-case
pre-code gate is not required. Students independently reason about expected
results and explain/test contributions. Individual understanding checks use no
generative AI.

## Collaboration and Submission

Follow the [pairing guide](../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md)
and [GitHub submission guide](../PreCourse_Setup/GitHub_Class_Repository_and_Submission_Guide.md).
Partners rotate per assignment; nine students use three pairs and an active trio.
Switch drivers about every 20 minutes with save/check/commit/push/pull handoffs.
Lab work uses Zoom breakout rooms, instructor visits, and chat help. Students
schedule their own Zoom sessions if more joint time is needed.

Each student submits the complete copied code and personal README once.
Exclude the shared repository's .git directory; verify the destination copy.
Preserve earlier graded iterations in new folders when applicable. Daily stages
of AL01 do not require separate submitted applications.

Formal peer review occurs once in Week 5 for individual AL06 applications,
with separate Schoology review grading. It does not block Week 1 release.

## Evaluation

| Emphasis | Categories |
| --- | --- |
| Primary | T1, T3, T5, C1, C5 |
| Secondary | T2, T6, C2 |
| Light / Incidental | C3, C4, C6 |
| Not Assessed | T4 only |

Use existing MRS definitions and descriptors. N/A receives automatic full points.
Assess through work, observations, tests, and brief explanations, not additional
paperwork. AI use itself is optional. The course-wide assignment mapping follows
later completed packets; no bulk rubric rewrite or new weights are required.

## Time and Production Status

| Day | Instruction | Lab | Lab focus |
| --- | ---: | ---: | --- |
| Monday | 50 min | 70 min | Paired open view, validation, role adjustment |
| Tuesday | 60 min | 120 min | Paired follow-up v1, boundary tests/repair, handoffs |
| Thursday | 60 min | 120 min | Paired revision/refactor; individual copy and README |
| Total | 170 min | 310 min | One progressive assignment |

Daily demos and APP-M0/M1 remain within instruction. Initial estimates of
155-230 task minutes and 270-285 usable lab minutes are historical, unmeasured
estimates, not a validated claim about the revised paired workflow. Retain
support/adjustment time; do not add features to fill perceived slack.

Packet, fixture, optional starter, instructor solution, guides, and demo
refactors are created. [Pre-rehearsal checks](119_Week_01_Pre_Rehearsal_Check.md)
pass; actual pacing and Zoom readability await the instructor's later rehearsal.
Outlines/decks, final deadline directions, and student distribution checks remain.
Thursday instruction must bridge the demo's AND example to AL01's grouped OR.
Original reading material, master rubric, and legacy assignments remain preserved.
