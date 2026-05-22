# 10-152-119 Assignments

This folder contains the lab assignment system for `10-152-119 Algorithmic
Problem Solving`.

## Control Artifacts

- `LASO-AL_Lab_Assignment_System_Overview.md`
- `Lab_Progression_Ladder_v2.md`
- `LDP-AL_Lab_Demo_Prompt_Pack.md`
- `FINAL-AL_Final_Algorithmic_Reasoning_Assessment.md`
- `FINAL-AL_WIDS_Final_Assessment_Rubric.md`

## Lab Assignment Set

- `Lab_01_Precision_and_Correctness.md`
- `Lab_02_Growth_and_Big_O_Intuition.md`
- `Lab_03_Data_Structure_Choice.md`
- `Lab_04_Search_and_Sort_Behavior.md`
- `Lab_05_Strategy_Comparison.md`
- `Lab_06_Graph_Traversal_and_Modeling.md`
- `Lab_07_Similarity_Ranking_and_Hashing.md`

## Week 8 Synthesis and Final

- `Week_08_Final_Synthesis_Demo_and_Practice.md`
- `Final_Assessment/`

- `FINAL-AL_Final_Algorithmic_Reasoning_Assessment.md`
- `FINAL-AL_WIDS_Final_Assessment_Rubric.md`

Week 8 uses one synthesis/demo practice day followed by the two-part final
assessment:

- Part 1: students submit working algorithmic solutions with evidence
- Part 2: students complete a personalized explanation defense based on their
  own submitted work

Each lab includes:

- student-facing task requirements
- instructor demo plan
- evidence requirements
- AI-use boundary
- success criteria
- successful-version release note

The instructor demo should be related to the lab, but not identical to the lab.
This preserves near transfer and keeps students responsible for reasoning.

Labs 1-7 form the graded lab progression. Week 8 is reserved for synthesis and
the final assessment rather than a full additional lab.

The concrete student-facing final task set, starter files, README template, and
standardized Part 2 question bank are stored in `Final_Assessment/`.

## Instructor Prompt Support

Use `LDP-AL_Lab_Demo_Prompt_Pack.md` with a Codex-capable LLM in VS Code to
generate final lab packets, companion demo files, starter files, and withheld
successful versions.

## Instructor Testing Environment

Use one shared virtual environment at the `Assignments` folder level for manual
testing of demo code and withheld success code.

Recommended local structure:

```text
Assignments/
  .venv/
  requirements.txt
  Lab_01/
  Lab_02/
  ...
```

The `.venv` folder is local execution infrastructure and should not be treated
as a course artifact.

Use `requirements.txt` for course-level instructor testing dependencies. Most
labs should use only the Python standard library. If a lab requires a
third-party package, add it to `requirements.txt` and document the requirement
in that lab's instructor notes.

## Optional Colorized Success Versions

Some lab `success/` folders may include:

```text
optional_colorized_success_solution.py
optional_colorized_notes.md
```

These files demonstrate a refinement layer after the plain successful version is
already correct, observable, and explainable.

They are not grading requirements. They show how console output can be improved
when color helps make evidence easier to inspect, such as pass/fail results,
growth warnings, edge cases, comparison winners, or summary recommendations.

This pattern supports the reusable progression documented in:

```text
../MVP_Development_Progression_Instructional_Artifact.md
```

Lab 07 may also include an optional Rich formatted version:

```text
optional_rich_success_solution.py
optional_rich_notes.md
```

This demonstrates a further refinement layer using a documented third-party
dependency when structured tables and panels help make AI/data evidence easier
to inspect.

Lab 07 may also include an optional Rich demo:

```text
demo/optional_rich_demo_code.py
demo/optional_rich_demo_notes.md
```

This lets the instructor compare ANSI output and Rich formatted output before
showing the withheld success-version progression.

## Future Third-Party Data Packages

Possible future use of packages such as `numpy`, `pandas`, `scipy`,
`matplotlib`, or `networkx` is captured in:

```text
Future_Design_Note_Third_Party_Data_Packages.md
```

These packages are deferred until the lecture materials make their instructional
purpose clear.
