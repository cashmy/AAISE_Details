# SCHOOLOGY ASSIGNMENT SUMMARY

## 10-152-123 Modern Data Modeling for Systems

This summary is intended for Schoology assignment setup. Full assignment directions live in the `Assignments` folder. Student-facing submission templates live in `Student_Submission_Templates`.

Students should submit work as instructed in Schoology. When using the course GitHub repo structure, each assignment should be placed in the matching `week_<n>` folder and assignment folder listed below.

AI use is governed by the root-level `Standard_Student_AI_Use_Policy.md` and the course-specific `Modern_Data_Modeling_AI_Use_Addendum.md`.

---

# Course Submission Pattern

Each submitted assignment folder should include:

* the required template files for that assignment
* a completed `README.md`
* required evidence files
* `ai_assistance_notes.md` or `ai_assistance_disclosure.md` when AI was used or required

The `README.md` is part of the submitted evidence. It supports reflection, instructor feedback, and audit visibility.

---

# Scheduled Assignment Overview

| Week | Assignment | Schoology title | Student task | Required evidence summary | Submission folder |
| ---- | ---------- | --------------- | ------------ | ------------------------- | ----------------- |
| 1 | A1 | Conceptual Model Start and Quality Revision | Define an initial system concept, identify core entities and relationships, then revise after quality review. | `README.md`, `conceptual_model_worksheet.md`, optional sketch, AI notes if used. | `week_01/A1_conceptual_model_start_and_quality_revision` |
| 2 | A2 | Relational Structure and Process Mapping | Convert the system idea into a beginning relational structure and connect it to system process thinking. | `README.md`, `relational_structure_worksheet.md`, optional relational sketch, AI notes if used. | `week_02/A2_relational_structure_and_process_mapping` |
| 3 | A3 | ERD Creation and Diagramming Practice | Create a readable ERD or comparable model diagram using draw.io or another approved diagramming tool. | `README.md`, `erd_diagramming_worksheet.md`, `erd_notation_readability_checklist.md`, tool notes, diagram evidence, AI notes if used. | `week_03/A3_erd_creation_and_diagramming_practice` |
| 4 | A4 | Conceptual Modeling Refinement | Revisit the model, identify quality issues, and produce a more defensible revised version. | `README.md`, `model_revision_worksheet.md`, `conceptual_pattern_review.md`, `model_quality_self_assessment.md`, revised model evidence, AI notes if used. | `week_04/A4_conceptual_modeling_refinement` |
| 5 | A5 | Normalization and Anomaly Analysis | Analyze a model for redundancy, update problems, insertion problems, deletion problems, and normalization concerns. | `README.md`, `anomaly_analysis_worksheet.md`, optional marked-up model, AI notes if used. | `week_05/A5_normalization_and_anomaly_analysis` |
| 5 | A6 | Business Rules and Performance Tradeoffs | Identify business rules, decide where rules belong, and explain tradeoffs between clarity, integrity, and performance. | `README.md`, `rule_placement_tradeoff_worksheet.md`, optional model annotation, AI notes if used. | `week_05/A6_business_rules_and_performance_tradeoffs` |
| 6 | A7 | MongoDB Setup and Document Boundary Draft | Set up MongoDB evidence and draft a document model boundary using sample JSON-style documents. | `README.md`, `document_boundary_worksheet.md`, `mongodb_setup_evidence.md`, `sample_document.json`, AI notes if used. | `week_06/A7_mongodb_setup_and_document_boundary` |
| 6 | A8 | Relational vs Document Model Comparison | Compare relational and document-based representations for the same system need. | `README.md`, `representation_comparison_worksheet.md`, `sample_document_option_a.json`, `sample_document_option_b.json`, AI notes if used. | `week_06/A8_relational_vs_document_model_comparison` |
| 7 | A9 | MongoDB CRUD and Query Evidence | Use MongoDB operations as evidence that a model can support stated system questions. | `README.md`, `query_evidence_worksheet.md`, `operation_evidence.md`, operation results or screenshots if requested, AI notes if used. | `week_07/A9_mongodb_crud_and_query_evidence` |
| 7 | A10 | Aggregation, Performance, and Final Modeling Defense Prep | Use aggregation or performance reasoning to prepare final model-defense evidence. | `README.md`, `aggregation_defense_prep_worksheet.md`, `capstone_evidence_selection.md`, operation evidence if requested, AI notes if used. | `week_07/A10_aggregation_performance_and_defense_prep` |
| 8 | Capstone | Capstone Modeling Defense | Finalize and defend a database design using one of the approved capstone pathways. | `README.md`, system scope, visual model, business rules, relational model evidence, relational vs document consideration, final defense, AI disclosure, and NoSQL evidence if applicable. | `week_08/capstone_modeling_defense` |

---

# Copy/Paste Assignment Descriptions

## A1 - Conceptual Model Start and Quality Revision

Create an initial conceptual model for your selected database idea. Begin manually by identifying the system purpose, users, entities, relationships, attributes, assumptions, and early quality concerns. After the manual checkpoint, revise the model using class feedback, instructor guidance, and allowed AI assistance if you choose to use it.

Submit the completed files in `week_01/A1_conceptual_model_start_and_quality_revision`.

AI note: Complete the manual sections before using AI. AI may critique or question your model, but it may not replace your own modeling decisions.

## A2 - Relational Structure and Process Mapping

Extend your model by translating your conceptual idea into a beginning relational structure. Identify tables, rows, columns, keys, relationships, and system processes without using SQL. The goal is to show how the system's information can be organized and how the structure supports expected use.

Submit the completed files in `week_02/A2_relational_structure_and_process_mapping`.

AI note: AI may help critique the structure or point out unclear relationships after your manual attempt.

## A3 - ERD Creation and Diagramming Practice

Create a readable ERD or comparable data model diagram from your current design. Use draw.io or another approved diagramming tool. Focus on notation, readability, entity names, relationship clarity, cardinality, and layout choices.

Submit the completed files in `week_03/A3_erd_creation_and_diagramming_practice`.

AI note: AI may critique a manual diagram plan or identify questions to check, but it may not make the core relationship decisions for you.

## A4 - Conceptual Modeling Refinement

Revise your model using evidence from earlier work. Identify specific model issues, explain why they matter, and produce a revised model that better fits the system boundary and intended use.

Submit the completed files in `week_04/A4_conceptual_modeling_refinement`.

AI note: AI may help critique your revision plan after you identify the issues manually.

## A5 - Normalization and Anomaly Analysis

Analyze your model for redundancy and data anomalies. Identify where repeated data, unclear dependencies, update problems, insertion problems, or deletion problems may appear. Explain how normalization thinking improves the model.

Submit the completed files in `week_05/A5_normalization_and_anomaly_analysis`.

AI note: AI may help explain or check anomaly reasoning after you complete your own analysis.

## A6 - Business Rules and Performance Tradeoffs

Identify important business rules in your system and decide where they should be represented. Explain tradeoffs among data integrity, clarity, flexibility, and performance. The goal is not a perfect enterprise design, but a defensible modeling decision.

Submit the completed files in `week_05/A6_business_rules_and_performance_tradeoffs`.

AI note: AI may help compare rule-placement options, but your final rule and tradeoff explanation must be your own.

## A7 - MongoDB Setup and Document Boundary Draft

Set up MongoDB-related evidence and draft a document boundary for part of your system. Create a limited sample document using JSON/BSON-style structure and explain what belongs together in one document.

Submit the completed files in `week_06/A7_mongodb_setup_and_document_boundary`.

AI note: AI may help review document shape or field choices after you define the system need and document boundary.

## A8 - Relational vs Document Model Comparison

Compare relational and document-based representations for the same system scenario. Explain what each representation makes easier or harder and identify which representation better fits the selected part of the system.

Submit the completed files in `week_06/A8_relational_vs_document_model_comparison`.

AI note: AI may help compare options, but you must verify the comparison and explain your chosen representation.

## A9 - MongoDB CRUD and Query Evidence

Use MongoDB operations as model evidence. Define system questions, state expected results, run or document appropriate operations, and explain what the result shows about the model.

Submit the completed files in `week_07/A9_mongodb_crud_and_query_evidence`.

AI note: AI may help explain or troubleshoot MongoDB operations, but you must state the system question and expected result first.

## A10 - Aggregation, Performance, and Final Modeling Defense Prep

Use aggregation or performance reasoning to prepare evidence for your final modeling defense. Select the strongest evidence from your course work and connect it to a defensible claim about your design.

Submit the completed files in `week_07/A10_aggregation_performance_and_defense_prep`.

AI note: AI may help critique the defense plan or explain operations, but you must decide what evidence best supports your model.

## Capstone - Modeling Defense

Finalize and defend a database design using one of the approved capstone pathways:

1. Expand or finalize the database design used throughout the course.
2. Choose a remaining unused option from `Database_Concept_Options_v1.md`.
3. Choose a database layer connected to a Python or Web Development capstone project.
4. Propose a new option with instructor approval.

Your submission must include a Capstone Evidence Index in the `README.md` and enough evidence to support your final design claim.

Submit the completed files in `week_08/capstone_modeling_defense`.

AI note: AI assistance is allowed but must be disclosed. Pathway 2 requires especially clear disclosure because AI may be used to accelerate a new design.

---

# Schoology Policy Attachment Note

Recommended Schoology attachments or links:

* `Assignments/<assignment file>.md` for the detailed assignment directions
* `Student_Submission_Templates/<week>/<assignment folder>` for student starter files
* `Modern_Data_Modeling_AI_Use_Addendum.md`
* root-level `Standard_Student_AI_Use_Policy.md`

---

# Instructor Setup Notes

Schoology due dates can be added after the semester calendar is finalized.

The weekly structure assumes:

* two lecture days per week
* two lab days per week
* one assignment for Weeks 1-4, with iterative checkpoint/final-submission behavior where appropriate
* two assignments in Weeks 5-7
* a Week 8 capstone modeling defense

