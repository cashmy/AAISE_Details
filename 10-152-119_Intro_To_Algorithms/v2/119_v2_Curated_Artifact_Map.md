# 10-152-119 Introduction to Algorithms v2 Curated Artifact Map

## Purpose

This document establishes a clean v2 workspace for redesigning
`10-152-119 Introduction to Algorithms`.

Unlike `10-152-117` and `10-152-118`, the existing `119` artifacts should be
treated as provisional design material rather than a locked canonical course
system. The v2 course should be rebuilt as a hybrid artifact set:

- grounded in the selected textbook
- aligned with the bridge degree sequence
- focused on algorithmic reasoning, comparison, correctness, efficiency, and
  data/AI foundations
- supported by visual and tangible labs without making the course web-based

## Textbook Reference

Primary text:

`50 Algorithms Every Programmer Should Know: Tackle computer science challenges
with classic to modern algorithms in machine learning, software design, data
systems, and cryptography`, 2nd edition, Imran Ahmad.

The textbook should be treated as a reference spine, not a coverage contract.
The course should select from the book intentionally and leave many chapters as
future reference material for students.

## Existing Artifact Disposition

### Pull Forward

`legacy/WIDS_Course_Competency_Framework.md`

- Retain the broad competency shape.
- Revise wording so AI remains important but does not dominate every learning
  move.
- Preserve problem analysis, implementation, correctness/efficiency,
  comparison, and adaptation.

`legacy/Rubric_Evaluation.md`

- Review for reusable criteria.
- Likely retain categories around problem framing, implementation,
  correctness, efficiency, explanation, and AI accountability.
- Modify after the v2 lab sequence stabilizes.

### Modify Heavily

`Course_Architecture.md`

- Treat as an early foundation artifact.
- Preserve the intent to develop algorithmic thinking for AI-augmented
  engineers.
- Replace the 8-week all-labs/every-week dual-mode structure with a
  textbook-guided course spine.
- Add explicit foundations for data analytics, AI, and later data modeling.

`Lab_Architecture.md`

- Preserve the useful repeated lab pattern:
  problem framing, manual solution, implementation, comparison, evaluation,
  adaptation.
- Reduce the expectation that every lab must contain equal-weight manual and
  AI-assisted solutions.
- Add visual/tangible lab options such as timing charts, grid pathfinding,
  search/sort animation, clustering plots, similarity ranking, and graph
  traversal diagrams.

`WIDS_CCF_Reflection.md`

- Retain as design history only.
- Extract useful language around dual-mode capability, comparison, evaluation,
  and adaptation.
- Do not treat the reflective/philosophical commentary as student-facing course
  architecture.

### Ignore or Archive for v2

Original root `Lecture_Outlines/`

- Removed from the root course folder when it contained inherited
  HTML/CSS/JavaScript material.
- Recreated as a root-level v2 scaffolding folder after the Algorithms lecture
  outline template was authored.
- Use the current root-level `Lecture_Outlines/` folder as the active
  Algorithms lecture-outline location.

`legacy/Course+Design.pdf`

- Keep as source-history material.
- Review only if needed to recover earlier design intent.
- Do not use as the organizing authority unless later inspection reveals unique
  content not present in the Markdown artifacts.

## Current Folder Organization

Root design-history files:

- None. Original v1 root files have been reviewed, accounted for, and moved to
  `legacy/`.

Legacy archived files:

- `legacy/Course_Architecture.md`
- `legacy/Course+Design.pdf`
- `legacy/Lab_Architecture.md`
- `legacy/Rubric_Evaluation.md`
- `legacy/WIDS_CCF_Reflection.md`
- `legacy/WIDS_Course_Competency_Framework.md`

Active v2 files:

- `v2/119_v2_Curated_Artifact_Map.md`
- `v2/10-152-119_Intro_to_Algorithms_COS_v2.docx`
- `v2/Design_Decision_Log_v2.md`
- `v2/Design_Reflection_and_Open_Refactor_Risks_v2.md`
- `v2/Introduction_to_Algorithms_High_Level_Course_Plan_v2.md`
- `v2/Unit_Week_Descriptions_v2.md`
- `v2/IIM_Matrix_v2.md`
- `v2/IIM_Matrix_v2.xlsx`
- `v2/Textbook_Coverage_and_Reference_Map_v2.md`
- `v2/WIDS_Course_Competency_Framework_v2.md`
- `v2/Rubric_Evaluation_v2.md`
- `v2/MRS-AL_Master_Rubric_System.md`

Active root-level scaffolding:

- `Lecture_Outlines/README.md`
- `Lecture_Outlines/LOT-AL_Alignment-Based_Lecture_Outline_Template.md`
- `Lecture_Outlines/Week_01_Algorithms_Precision_and_Correctness.md`
- `Lecture_Outlines/Week_02_Growth_and_Big_O_Intuition.md`
- `Lecture_Outlines/Week_03_Data_Structure_Choice.md`
- `Lecture_Outlines/Week_04_Search_and_Sort_Behavior.md`
- `Lecture_Outlines/Week_05_Recursion_Iteration_and_Strategy.md`
- `Lecture_Outlines/Week_06_Graph_Traversal_and_Modeling.md`
- `Lecture_Outlines/Week_07_Similarity_Ranking_and_Hashing.md`
- `Lecture_Outlines/Week_08_Final_Synthesis_and_Assessment.md`
- `Assignments/LASO-AL_Lab_Assignment_System_Overview.md`
- `Assignments/Lab_Progression_Ladder_v2.md`
- `Assignments/LDP-AL_Lab_Demo_Prompt_Pack.md`
- `Assignments/FINAL-AL_Final_Algorithmic_Reasoning_Assessment.md`
- `Assignments/FINAL-AL_WIDS_Final_Assessment_Rubric.md`
- `Assignments/README.md`
- `Assignments/Lab_01_Precision_and_Correctness.md`
- `Assignments/Lab_02_Growth_and_Big_O_Intuition.md`
- `Assignments/Lab_03_Data_Structure_Choice.md`
- `Assignments/Lab_04_Search_and_Sort_Behavior.md`
- `Assignments/Lab_05_Strategy_Comparison.md`
- `Assignments/Lab_06_Graph_Traversal_and_Modeling.md`
- `Assignments/Lab_07_Similarity_Ranking_and_Hashing.md`
- `Assignments/Week_08_Final_Synthesis_Demo_and_Practice.md`

## v2 Design Commitments

- This course is not web-based by default.
- Python should remain the primary implementation language because it follows
  `10-152-117` and keeps syntax overhead low.
- Visual/tangible labs are required where they improve understanding.
- Big-O and data structures are required foundations.
- Section 1 of the textbook should provide the main course spine.
- Sections 2 and 3 should be cherry-picked for AI, analytics, data-modeling, and
  systems-reasoning bridges.
- The course should make students better at choosing, testing, comparing, and
  explaining solution strategies.

## Textbook Selection Strategy

### Required Spine

From Section 1:

- Overview of algorithms
- Performance analysis and Big-O
- Data structures used in algorithms
- Searching and sorting
- Algorithm design concerns: correctness, performance, scalability
- Strategy comparison: brute force, divide and conquer, greedy, dynamic
  programming at an introductory level
- Graph basics, representations, BFS, DFS, and shortest-path intuition

### Selected AI and Data Bridges

From Section 2:

- Distance and similarity measures
- Clustering as an unsupervised-learning preview
- Decision trees or classification logic as an explainable supervised-learning
  preview
- Text-to-number representation such as TF-IDF as a light AI/data bridge

From Section 3:

- Recommendation engines as similarity, ranking, and data representation
- Hashing for identity, lookup, integrity, and security awareness
- Compression as a data-representation and tradeoff example, if time allows
- Explainability, bias, incorrect assumptions, and when not to use algorithms

### Defer or Reference Only

- Deep neural networks
- RNNs, GRUs, LSTMs, Seq2Seq, attention, transformers, and LLM internals
- CAP theorem in depth
- Spark, CUDA, large-scale cloud processing
- Full cryptography, PKI, blockchain, or SSL/TLS implementation
- Advanced machine-learning model training

## Next Artifacts to Create

Completed:

- `Introduction_to_Algorithms_High_Level_Course_Plan_v2.md`
- `Unit_Week_Descriptions_v2.md`
- `Lab_Progression_Ladder_v2.md`
- `WIDS_Course_Competency_Framework_v2.md`
- `Rubric_Evaluation_v2.md`
- `Textbook_Coverage_and_Reference_Map_v2.md`
- `IIM_Matrix_v2.md`
- `IIM_Matrix_v2.xlsx`
- `Design_Decision_Log_v2.md`
- `Design_Reflection_and_Open_Refactor_Risks_v2.md`
- `10-152-119_Intro_to_Algorithms_COS_v2.docx`
- `MRS-AL_Master_Rubric_System.md`
- `../Lecture_Outlines/README.md`
- `../Lecture_Outlines/LOT-AL_Alignment-Based_Lecture_Outline_Template.md`
- `../Lecture_Outlines/Week_01_Algorithms_Precision_and_Correctness.md`
- `../Lecture_Outlines/Week_02_Growth_and_Big_O_Intuition.md`
- `../Lecture_Outlines/Week_03_Data_Structure_Choice.md`
- `../Lecture_Outlines/Week_04_Search_and_Sort_Behavior.md`
- `../Lecture_Outlines/Week_05_Recursion_Iteration_and_Strategy.md`
- `../Lecture_Outlines/Week_06_Graph_Traversal_and_Modeling.md`
- `../Lecture_Outlines/Week_07_Similarity_Ranking_and_Hashing.md`
- `../Lecture_Outlines/Week_08_Final_Synthesis_and_Assessment.md`
- `../Assignments/LASO-AL_Lab_Assignment_System_Overview.md`
- `../Assignments/Lab_Progression_Ladder_v2.md`
- `../Assignments/LDP-AL_Lab_Demo_Prompt_Pack.md`
- `../Assignments/FINAL-AL_Final_Algorithmic_Reasoning_Assessment.md`
- `../Assignments/FINAL-AL_WIDS_Final_Assessment_Rubric.md`
- `../Assignments/README.md`
- `../Assignments/Lab_01_Precision_and_Correctness.md`
- `../Assignments/Lab_02_Growth_and_Big_O_Intuition.md`
- `../Assignments/Lab_03_Data_Structure_Choice.md`
- `../Assignments/Lab_04_Search_and_Sort_Behavior.md`
- `../Assignments/Lab_05_Strategy_Comparison.md`
- `../Assignments/Lab_06_Graph_Traversal_and_Modeling.md`
- `../Assignments/Lab_07_Similarity_Ranking_and_Hashing.md`
- `../Assignments/Week_08_Final_Synthesis_Demo_and_Practice.md`

Next:

1. Demo files, starter files, and success versions for Labs 1-7
2. Week 1 and Week 2 lecture PowerPoint decks
3. Reassess whether weekly outlines should split into Day 1 and Day 2 after
   the first demo/deck packages exist
4. Final Part 1 task set and Part 2 question-generation workflow
