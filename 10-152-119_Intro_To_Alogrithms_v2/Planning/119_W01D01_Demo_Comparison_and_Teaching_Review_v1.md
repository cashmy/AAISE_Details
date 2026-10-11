# W01D01 Demo Comparison and Teaching Review

## Subsequent Implementation: October 9, 2026

W01D01 has now been refactored as the first user-facing prototype. Its standard equipment-loan report preserves E01/E04 selection and explains exclusions in desk-user language. A subsequent bounded-Python review removed its early parser: a small menu now selects the standard report or a paused six-step walkthrough, all residual trace machinery is removed, and all 22 demos keep assertions in separate `test_demo.py` files. The updated instructor notes provide the request-to-contract-to-pseudocode-to-Python delivery sequence; the printed walkthrough now implements an isolated 50% boundary failure, corrected expected/actual comparisons, and the final useful report. All W01D01 application and test functions have short purpose docstrings. The collection passes 58 checks on Python 3.14.7 and 3.12.10. Instructor acceptance remains pending; other demos have received test separation but not this presentation refactor, and the original charger demo is unchanged. See the [standard testing and Python progression guidelines](119_Demo_Authoring_Guidelines_v1.md).

The review below records the pre-refactor findings; statements about unchanged code and illustrative output describe that earlier review, not the subsequent implementation. See the [implemented prototype and verified output](../Demos/Week_01/Demo_01_Equipment_Request_Contract/README.md).

Instructor review | October 9, 2026

## Finding

**The current W01D01 code is a useful behavioral example, but its default presentation is not yet a strong student-facing teaching demonstration.** The instructor's concern is supported: it compresses the learning sequence into technical verdicts, a Python list of IDs, and a responsibility label.

This is a presentation/pedagogy finding, not a claim that the functions teach an LLM rather than a person. The observable problem is that the program foregrounds implementation/evidence vocabulary while leaving much of the student's route from a practical question to an understandable answer to the instructor notes.

Keep the stronger structured-record task and useful checks. Restore the original demo's explicit explanatory progression and readable outcomes rather than reverting the course to its original scope.

This review compares only W01D01 with the specified early demo. W01D02/D03 were inspected for sequencing context, not fully audited. Neither demo's code has been changed by this review; no broader rewrite or new assignment packet is implemented.

## Sources and Execution

- [Original Lab 01 demo](../../10-152-119_Intro_To_Algorithms/Assignments/Lab_01/demo/demo_code.py): charger recommendation; ambiguous rules, precise rules, pseudocode/Python-style bridge, before/after test tables.
- [Current W01D01 main.py](../Demos/Week_01/Demo_01_Equipment_Request_Contract/main.py): equipment selection with validation, trace, copied selected records, self-checks.
- [Current student README](../Demos/Week_01/Demo_01_Equipment_Request_Contract/README.md) and local instructor notes.md.
- [Current W01D02](../Demos/Week_01/Demo_02_Filter_Boundaries/main.py) and [W01D03](../Demos/Week_01/Demo_03_Combined_Criteria/main.py): boundary diagnosis and combined-criteria/refactor work that should not all move into Monday.
- [Updated assignment map](119_Assignment_List_and_Progression_Map_v1.md): Week 1 remains an approachable collaboration-adjustment week, transferring to individual ticket work.

Both scripts ran successfully on Python 3.14.7. The original was captured with NO_COLOR=1. Its initial boundary failure is intentional teaching evidence, not a process failure. The current script's self_check completed. An additional isolated hours-boundary call was checked in the original without altering the file.

## Comparison

| Dimension | Original Charger Demo | Current Equipment Demo | Judgment |
| --- | --- | --- | --- |
| Practical purpose | A familiar question: should I bring a charger? Inputs have visible personal meaning | A useful loan-selection task, but presented as an EQUIPMENT REQUEST CONTRACT and then ID verdicts | Keep the new context; introduce it as a person's request before schema/algorithm language |
| Rule development | Shows ambiguous language and then explicit 40-percent/four-hour rules | Prints the already precise battery >= 50 request | Restore the decision-making bridge; students should see how unclear language becomes an agreed rule |
| Representation bridge | Named plain-English, pseudocode and Python-style sections | Python function boundaries exist, but console ends with validate -> select -> present | A useful architecture label is not a worked bridge from human rule to code |
| Inputs and outcomes | Battery percentage, hours, outlet availability and charger advice are visible | Per-record verdicts omit the actual equipment/battery/availability context; final result is ['E01', 'E04'] | Show the selected equipment and relevant attributes, not just raw identifiers |
| Correctness explanation | Expected, actual and pass/fail comparison exposes the revision's effect | Main output has reasons and Checks passed; expected outcomes are mostly hidden in self_check | Make selected independently justified expectations visible; preserve automated checks separately |
| Record/application depth | One decision on scalar inputs; little record validation | Structured records, missing/invalid data, exact threshold, responsibility separation and copied selections | Retain these stronger features; they fit the revised course's transfer needs |
| Console organization | Clear sections, descriptive summaries and supplementary color | Short, orderly, but dominated by terms such as match, invalid, selected IDs and responsibilities | Do not merely color technical output; change the language and information hierarchy |
| Delivery burden | The script visibly carries the explanatory sequence | Notes say to introduce ambiguity, but the program mainly displays the finished contract/result | Align notes, code, and visible reveal sequence |
| Screen-share length | 52 output lines; widest line 111 characters in the plain captured run | 13 output lines; widest line 76 characters | The new version is compact, but compression removed explanation. The old table needs a narrow-width fallback, not blind copying |

Length is not a quality score. A longer program or more output does not automatically teach better. The desired change is a clearer sequence and a useful readable result.

## Priority Findings

### 1. The Learner's Route Is Mostly Missing

Original landmarks: INITIAL_RULES at line 22, REVISED_RULES at 28, PSEUDOCODE at 34, PYTHON_STYLE at 43, and print_representation_bridge at 123.

Current landmarks: main at line 55 immediately prints a precise request and select_equipment's result. The ambiguity and agreed-rule discussion exists in notes but is not carried into the program's visible story.

**Direction:** Show a short everyday request, the question it leaves open, an agreed plain-language rule, a small pseudocode example, and the corresponding named Python function. Keep the code visible beside the output. Students already know Python; the lesson is translating requirements accurately, not reteaching if statements.

### 2. A Diagnostic Report Is Serving as the Main User Display

Current main.py lines 59-63 show record IDs/reasons, a serialized list of selected IDs, and the responsibilities arrow. This exposes the processing path but not a well-presented answer to the person's request.

**Direction:** Default output should identify the request, show ready-to-borrow equipment with battery percentages and availability meaning, and summarize exclusions with readable language. Missing data should remain explicit. A technical trace can be supplemental instructor/evidence output; it need not be the primary interface.

There is no need for a full menu, framework, database, or interactive app shell. A small console report can be useful and human-friendly.

### 3. Passing Internal Checks Is Not a Visible Correctness Lesson

validate_record/select_equipment and self_check supply useful foundations. However, the viewer sees Checks passed rather than the relevant input, independently expected outcome, actual outcome, and why they agree.

**Direction:** Make a few selected expected/actual observations visible in readable language. Do not replace internal assertions with presentation tables, and do not fill Monday with every Tuesday boundary case.

### 4. Monday Should Not Absorb the Whole Original Weekly Demonstration

The old script combines rule refinement, representation, a boundary defect, and corrected results. The revised course has distinct Monday/Tuesday/Thursday teaching purposes.

**Direction:** Monday establishes the practical problem and translation to a contract. Tuesday demonstrates a boundary failure and repair. Thursday distinguishes behavior-preserving refactoring from a changed rule. Retain the shared equipment context and separate Navigator recognition.

## What to Reuse From the Original

- Familiar scenario and inputs whose meaning is immediately clear.
- Ambiguous-to-precise rule progression.
- A concise plain-English -> pseudocode -> Python bridge.
- Expected/actual results expressed as decisions a person understands.
- Section hierarchy and optional color as reinforcement, not the sole carrier of meaning.

## What Not to Copy Unchanged

- The 111-character table can wrap poorly during remote screen sharing. Use a compact table or vertically grouped cases when space is narrow.
- USE_COLOR checks NO_COLOR but not terminal support or redirected output. Future presentation should have a plain fallback and avoid mandatory ANSI escape sequences in captured output.
- The table labels mention the battery comparison but omit the hours comparison that also changes. Label the complete rule change accurately.
- Test 4 combines exactly 40 percent and exactly four hours. It shows a failure but does not independently isolate both boundaries.
- An additional case with battery 55 percent, four hours on campus, and no outlet returns charger optional initially and bring charger after revision. That isolated hours-boundary case is absent from TEST_CASES. Preserve independent expected outcomes if this example is reused.
- The initial function is deliberately defective; do not describe all before/after outputs as equally correct under the revised rule.

## Proposed Output Direction, Not Implemented

A useful result from the existing equipment fixture could read:

```text
Equipment Loan Desk

Request: A laptop available to borrow today
Minimum battery: 50%

Ready to borrow
  E01 - Laptop - Battery 80%
  E04 - Laptop - Battery 50%

Not included
  E02 - Already on loan
  E03 - Tablet; this request is for a laptop
  E05 - Battery not recorded; not selected

Result: 2 laptops meet the request.
```

This is an illustrative display target, not verified output from changed code. It preserves the existing selection outcome. The teaching sequence would then connect those results to rules, a small worked case, and the corresponding functions; detailed traces/checks can remain available separately.

## Proposed 12-18 Minute Delivery

1. 0-3 min: read the person's request and ask what available and enough battery mean.
2. 3-6 min: agree on the input/output and inclusive minimum; show a short plain-English/pseudocode bridge.
3. 6-10 min: run a readable loan report, predict selected equipment and explain one exclusion.
4. 10-14 min: connect validate_record, select_equipment, and the presentation function to their responsibilities; show one readable expected/actual check.
5. Remaining time: ask about a changed assumption, then stop before the ticket assignment or Tuesday's full boundary investigation.

APP-M0 stays a separate 5-8 minute recognition introduction. Neither layer extends the allocated teaching/lab meeting.

## Next Review Gate

Refactor only W01D01's learner-facing presentation and reveal order first, then review its output with the instructor before applying a new pattern across the collection. Reuse its selection/validation behavior and regression checks unless a separate scope change is agreed.

After that, evaluate later demos using the same criteria: practical question first, explicit reasoning bridge, understandable results, selected observable evidence, technical detail only where it serves the current lesson. Some topics need traces, but traces should have labeled meaning and not stand in for the usable outcome.

The Week 4 modular scaffolding remains useful. Its recently expanded traces should still undergo this separate student-facing presentation review; contract consistency alone does not establish delivery quality.
