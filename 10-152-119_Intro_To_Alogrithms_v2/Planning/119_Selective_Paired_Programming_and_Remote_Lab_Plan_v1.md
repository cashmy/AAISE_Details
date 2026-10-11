# 119 Selective Paired Programming and Remote Lab Plan

Instructor planning artifact v1 | October 8, 2026

Historical planning reference. The current [assignment progression](119_Assignment_List_and_Progression_Map_v1.md) and [student pairing/submission guide](../PreCourse_Setup/Paired_Programming_and_Assignment_Submission_Guide.md) supersede conflicting provisions below: AL01 is paired development; partners rotate per assignment; one formal peer-review activity belongs to AL06; shared public repos feed complete individual class-repo submissions; additional joint work uses independently scheduled Zoom sessions. The student guide is created, not future work.

## Design Decision

Use paired programming selectively during remote-synchronous labs. An assignment may be individual, paired, or a hybrid with explicitly designated collaborative phases. Not every assignment needs paired programming or peer review.

Pairing is intended to support shared reasoning, meaningful questions, testing, and revision. It does not replace direct instruction, increase assignment scope automatically, or establish individual understanding by itself.

Current cohort: nine students. Required collaboration should be achievable during scheduled lab time through breakout rooms. Off-class collaboration may be available, but coordinating additional shared time should not be a hidden requirement.

This document records the instructor-facing design. A student-facing paired-programming guide will be developed later, after the assignment modes and collaboration tools are selected.

## Choosing the Collaboration Mode

| Mode | Suitable Use | Ownership and Evidence |
| --- | --- | --- |
| Individual | Initial reasoning, readiness checks, independent implementation/transfer, personal explanations, final assessment | Student-owned code and evidence; peer involvement only if explicitly permitted |
| Paired | Comparing approaches, tracing/debugging unfamiliar logic, coordinating representations, testing and revising a shared solution | Shared implementation/evidence, rotating roles, a consequential question/decision, and individual explanations |
| Hybrid | Individual prediction or baseline followed by paired investigation; individual implementation followed by peer review; paired work followed by individual adaptation | Assignment explicitly identifies each phase and which artifacts are individual or shared |

Select the mode based on the learning outcome. Independent ownership matters for some tasks; examining alternatives and discovering defects may benefit from shared work. An individual assignment does not become paired simply because students share a breakout room.

Every assignment packet should identify its mode, permitted collaboration, phase boundaries, submission ownership, individual checks, and grading treatment. Retain one or two connected assignments per week; collaboration mode can differ between them.

## Group Structure for Nine Students

For a fully collaborative lab, use three pairs and one trio, occupying four breakout rooms. The trio is a three-role working group rather than a pair with an observer.

| Role | Responsibility |
| --- | --- |
| Driver | Writes/runs code, explains the intended change, and makes implementation decisions visible |
| Navigator | Checks the approach against the contract, predicts behavior, asks questions, and identifies alternatives |
| Tester/reviewer in the trio | Develops tests, checks expected outcomes and evidence, and challenges assumptions |

All roles contribute reasoning. Rotate approximately every 20-25 minutes or at a meaningful checkpoint. In the trio, every participant should serve in every role across the lab work. In a pair, testing is a shared responsibility rather than a missing third role.

Keep groups together for approximately two weeks where practical, then rotate membership. Rotate who participates in the trio over the course. Adjust groups for attendance, participation, support needs, and working relationships rather than making the arrangement rigid.

If a student is absent or disconnected, the instructor may regroup students, permit individual continuation, or adjust the collaborative checkpoint. A student should not be blocked from required progress because a partner is unavailable.

## Remote Lab Rhythm

Example for a two-hour Tuesday/Thursday lab:

| Minutes | Activity |
| ---: | --- |
| 10 | Whole-class framing, permitted-collaboration reminder, and brief individual prediction |
| 45 | Breakout implementation/investigation, with role rotation |
| 5 | Short progress checkpoint and help requests |
| 45 | Breakout testing, comparison, changed requirement, and revision |
| 15 | Whole-class discussion and short individual explanation |
| 120 | Total |

For the proposed 70-minute Monday lab, use a shorter version: 5 minutes of individual framing, 25 minutes of breakout work, 5 minutes of checkpoint/support, 25 minutes of continued work with role rotation, and 10 minutes of closing evidence/explanation. Monday's actual lecture/lab split remains adaptable.

The instructor visits rooms and monitors a small shared checkpoint record. Establish a help-request mechanism before starting. The record should show the current task, role ownership, one useful question/decision, and any blocker; it should not become a transcript of the session.

Use a shared code workspace if the selected tooling supports reliable collaboration. Screen sharing with an explicit handoff of the current files is an alternative. Confirm edit/run access for all participants, how versions are handed off, and where evidence is saved. Tool choice remains open.

## Meaningful Questions and Revision

Pairing creates opportunities for questions; productive technical questioning still needs an expectation. Examples include:

- What assumption does this branch or representation depend on?
- What result do we expect before running this test?
- What happens for an empty input, duplicate, tie, or missing record?
- Does this change preserve the contract and previous valid behavior?
- Are we comparing equivalent workloads and including setup cost?
- Which proposed improvement serves this week's learning target?

For a designated paired investigation, record one consequential question, the resulting decision, and supporting evidence. The response may be a tested revision or a justified decision not to adopt the suggestion. Do not require artificial questions after students have already reasoned through the solution together.

For an individual assignment with designated peer review, record the reviewer's question and the owner's response. For a fully individual task without peer review, use an individual prediction, counterexample, or revision explanation instead.

This makes the earlier scope review's proposed weekly peer-question requirement conditional on the assignment mode. There is no course-wide requirement to manufacture a peer exchange for every assignment.

## Individual Accountability and Assessment

Paired work may share implementation, tests, and evidence. Each participant must still explain the group's solution and one consequential decision. A short individual prediction before collaboration, a closing explanation, or a small independent adaptation can establish this without duplicating the entire assignment.

The assignment packet should specify whether the shared package is submitted once with all contributors named or referenced by each student's submission. Each student supplies their own required explanation and tool-use account. Record relevant shared AI assistance as well as individual assistance.

Grade shared technical evidence and individual understanding explicitly. Do not assume identical understanding from shared code or use time in a role as proof of proficiency. Exact weights should be set with the assignment rubric; this plan introduces no new course-grade percentages.

Observe whether one student dominates, whether another is disengaged, and whether disagreements lead to constructive testing. Intervene through role changes, targeted questions, or regrouping. Architectural style, speed, and confidence alone should not determine contribution judgments.

The final assessment remains individual under the current course design. Its permitted references and tool rules are separate from paired-lab permissions.

## Pilot and Evaluation

Pilot selective use in Weeks 1-2 rather than designating every assignment paired in advance. A possible pilot is individual Week 1 framing/baseline followed by paired testing/revision, then a paired Week 2 experiment with individual predictions and conclusions.

Review:

- Whether all participants can explain the logic and evidence.
- Whether roles actually rotate and the trio remains active.
- Whether questions produce better tests, decisions, or revisions.
- Whether breakout setup and file handoffs consume too much lab time.
- Whether completion time reflects shared understanding or one student's work.
- Whether required work fits scheduled collaboration time and the intended individual outside-class allowance.

Use the results to select modes for later assignments. Keep individual checkpoints where they reveal learning more clearly, and preserve optional extensions for students who finish the strengthened core early.

## Future Student-Facing Guide

Create the guide later in this refactor folder, using the selected platform and assignment conventions. It should explain:

1. How to identify whether an assignment or phase is individual, paired, or hybrid.
2. Driver/navigator/tester responsibilities and role rotation.
3. Breakout-room setup, file/workspace handoff, checkpoints, and help requests.
4. Asking useful questions, resolving disagreement through evidence, and handling unequal participation.
5. Shared versus individual submissions, explanation expectations, and permitted tool use.
6. What to do when a partner is absent or a connection fails.
7. A short worked example of a question leading to a test, decision, and revision.

Write that artifact as practical student guidance, distinct from this instructor plan. Do not imply that every assignment permits collaboration or requires off-class partner meetings.

Related planning artifacts: [Scope Adjustment Review](119_Cohort_Readiness_and_Scope_Adjustment_Review_v1.md) and [Daily Topic List](119_Daily_Lecture_Topic_List_Review_Draft_v1.md). This plan clarifies collaboration choices for the next IIM and assignment revisions; it does not regenerate those materials.
