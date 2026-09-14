# Master Rubric System (MRS-DM)
## Modern Data Modeling for Systems

Version: `2.0`  
Purpose: Assignment-aligned rubric system for Course 123 using revised WIDS T1-T6 and fixed institutional Core Abilities C1-C6

---

# Part 1 - System Position

This rubric system evaluates the actual evidence students produce in the scaffolded Course 123 assignment sequence.

The MRS is aligned to:

- `WIDS_Course_Competencies_v0.2.md`
- `Assignments_Overview_v1.md`
- Week 1-8 demos
- Week 1-8 student submission templates
- Course 123 technology boundary: no SQL implementation in this course

Course 123 assesses database modeling judgment before SQL implementation. Students may use relational/table-shaped vocabulary and MongoDB concepts, but they are not assessed on SQL syntax.

---

# Part 2 - Performance Scale

| Score | Level | General Meaning |
| --- | --- | --- |
| 4 | Exceeds | Strong, complete, clear, and well-supported evidence; may go beyond requirements responsibly |
| 3 | Meets | Complete and appropriate evidence with minor gaps or refinements needed |
| 2 | Developing | Partial evidence; important gaps, weak explanation, or inconsistent reasoning |
| 1 | Needs Improvement | Minimal, unclear, incorrect, or mostly unsupported evidence |
| 0 | Missing | Missing, not submitted, or not assessable |

---

# Part 3 - Applicability Levels

Each T/C row can apply differently by assignment.

| Level | Meaning | Grading Use |
| --- | --- | --- |
| Primary | Central evidence for the assignment | Usually selected as a scored rubric row |
| Secondary | Important supporting evidence | Often selected, especially for larger assignments |
| Light/Tertiary | Present but not a major grading focus | Score only when useful or explicitly observable |
| Not Used | Not part of this assignment's evidence | Do not score |

This allows the same stable rubric rows to be reused without creating one-off rubrics for each assignment.

---

# Part 4 - Technical Rubric Rows

## T1. Data Modeling Foundations

Course evidence:

- system intent
- entity purpose
- relationship statements
- attributes, key candidates, and constraints
- model-quality review
- open questions and model boundaries

| Level | Description |
| --- | --- |
| 4 | Identifies a clear system purpose, meaningful entities, relationships, attributes, constraints, and model-quality questions; revisions show strong reasoning and scope awareness |
| 3 | Identifies appropriate entities, relationships, attributes, and basic constraints; explanation is mostly clear with minor gaps |
| 2 | Identifies some useful model elements, but important entities, relationships, constraints, or explanations are incomplete or unclear |
| 1 | Model elements are minimal, mismatched to the scenario, or mostly unsupported |

---

## T2. ERD Design and Model Communication

Course evidence:

- ERD or equivalent visual model
- notation and readability checklist
- assumptions
- relationship/cardinality explanation
- revised visual model evidence

| Level | Description |
| --- | --- |
| 4 | Creates a clear, readable visual model with appropriate entities, relationships, cardinality/notation, assumptions, and communication value |
| 3 | Creates a mostly accurate and readable ERD or visual model with minor notation, layout, or assumption gaps |
| 2 | Visual model is partially complete but has significant relationship, notation, readability, or assumption problems |
| 1 | Visual model is missing, very unclear, or does not represent the submitted scenario accurately |

---

## T3. Relational Modeling and Data Integrity

Course evidence:

- entity/attribute/key/relationship table
- process-to-data map
- integrity constraints
- anomaly/risk analysis
- normalization awareness
- business rule placement

| Level | Description |
| --- | --- |
| 4 | Explains relational/table-shaped structure, keys, relationships, constraints, anomaly risks, and business rules with strong evidence and appropriate scope |
| 3 | Provides reasonable relational/table-shaped structure and data-integrity reasoning with minor gaps |
| 2 | Shows partial understanding of keys, relationships, constraints, anomalies, or rules, but reasoning is incomplete or inconsistent |
| 1 | Relational/table-shaped evidence is missing, inaccurate, or disconnected from the scenario |

---

## T4. Document Modeling and Representation Choice

Course evidence:

- collection/document boundary decision
- embedding vs referencing comparison
- sample JSON/BSON-style documents
- relational vs document consideration
- representation recommendation

| Level | Description |
| --- | --- |
| 4 | Designs a document boundary that clearly fits stated system questions; embedding/reference choices and representation explanation are well-supported |
| 3 | Creates an appropriate document model and comparison with minor gaps in boundary, embedding/reference, or explanation |
| 2 | Document model or comparison is partially developed, but choices are unclear, arbitrary, or weakly connected to system questions |
| 1 | Document model evidence is missing, invalid, or treats documents as tables in JSON without modeling reasoning |

---

## T5. MongoDB Operations as Model Evidence

Course evidence:

- CRUD/query evidence
- expected-result notes
- query/access-pattern map
- aggregation evidence
- performance awareness note
- retrieval explanation

| Level | Description |
| --- | --- |
| 4 | Uses MongoDB operations or guided equivalents as clear evidence that the document model supports system questions; expected results, outputs, and model explanation are strong |
| 3 | Provides appropriate operation or aggregation evidence with expected result and reasonable explanation |
| 2 | Provides partial operation evidence, but expected results, outputs, or model explanation are incomplete or weak |
| 1 | Operation evidence is missing, disconnected from the model, or submitted as syntax without explanation |

---

## T6. Modeling Defense and AI-Assisted Design Practice

Course evidence:

- evidence index
- final design claim
- limitation statement
- AI assistance disclosure
- accepted/rejected AI suggestion notes
- final defense

| Level | Description |
| --- | --- |
| 4 | Defends the design with well-chosen evidence, clear limitations, responsible AI disclosure, and strong ownership of final decisions |
| 3 | Provides a clear design defense with appropriate evidence and adequate AI disclosure when relevant |
| 2 | Defense is partially supported, but evidence selection, limitations, or AI disclosure are incomplete |
| 1 | Defense is unsupported, unclear, or lacks required accountability for AI/tool assistance |

---

# Part 5 - Core Ability Rubric Rows

Core Ability names are fixed institution/program competencies. The evidence descriptions below define how each Core Ability is observed in Course 123.

---

## C1. Solve Problems

Course 123 evidence:

- issue identification
- revision planning
- anomaly/risk reasoning
- rule placement decisions
- operation troubleshooting
- limitation recognition

| Level | Description |
| --- | --- |
| 4 | Identifies modeling problems clearly, uses evidence to choose responsible solutions, and explains limitations or recovery steps independently |
| 3 | Solves the main modeling problem with reasonable evidence and limited guidance |
| 2 | Attempts the problem but needs frequent support; solution is partial or weakly justified |
| 1 | Struggles to identify or address the modeling problem |

---

## C2. Communicate Clearly

Course 123 evidence:

- diagrams
- rationale statements
- assumptions
- comparison tables
- README reflections
- final defense

| Level | Description |
| --- | --- |
| 4 | Communicates model choices, assumptions, evidence, and limits clearly enough for another person to inspect and discuss the design |
| 3 | Communicates the main design and reasoning adequately with minor gaps |
| 2 | Explanation is vague, incomplete, or difficult to connect to submitted artifacts |
| 1 | Cannot clearly explain the submitted model or design decisions |

---

## C3. Work Productively

Course 123 evidence:

- complete required files
- organized folders
- checkpoint completion
- tool/source/export evidence
- setup evidence when required

| Level | Description |
| --- | --- |
| 4 | Completes and organizes evidence reliably, uses lab time well, and meets checkpoint/final expectations |
| 3 | Completes required work with minor organization, timing, or completeness issues |
| 2 | Submission is partially complete or inconsistently organized |
| 1 | Submission is significantly incomplete, disorganized, or not usable for assessment |

---

## C4. Value Learning

Course 123 evidence:

- revision notes
- self-assessment
- feedback use
- AI critique review
- accepted/rejected suggestion notes
- improved artifacts

| Level | Description |
| --- | --- |
| 4 | Uses feedback, resources, demos, and critique to make meaningful improvements and explain learning decisions |
| 3 | Uses feedback or resources appropriately with minor gaps |
| 2 | Uses feedback or resources inconsistently; revisions are limited or weakly explained |
| 1 | Shows little evidence of using feedback, resources, or revision opportunities |

---

## C5. Work Cooperatively

Course 123 evidence:

- peer review notes
- partner checks
- collaborative diagram/model feedback
- respectful critique
- shared lab discussion evidence

| Level | Description |
| --- | --- |
| 4 | Contributes useful, respectful, and specific feedback or collaboration that improves modeling work |
| 3 | Participates appropriately in cooperative modeling activity |
| 2 | Participation is limited, passive, or only partially helpful |
| 1 | Does not participate constructively when cooperation is required |

Note:

C5 should be scored only when the assignment or lab creates observable cooperative evidence.

---

## C6. Act Professionally

Course 123 evidence:

- academic integrity
- tool/AI transparency
- complete README reflection
- organized submission
- accountability for design decisions
- professional final defense

| Level | Description |
| --- | --- |
| 4 | Submits organized, accountable work; discloses AI/tool use transparently; demonstrates integrity and professional responsibility |
| 3 | Acts professionally with minor issues in organization, preparation, or disclosure |
| 2 | Professionalism, accountability, or disclosure is inconsistent or incomplete |
| 1 | Submission or conduct raises significant concerns about preparation, integrity, accountability, or transparency |

---

# Part 6 - Assignment Applicability Matrix

Legend:

| Mark | Meaning |
| --- | --- |
| P | Primary |
| S | Secondary |
| L | Light/Tertiary |
| - | Not Used |

---

## Technical Competency Applicability

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 |
| --- | --- | --- | --- | --- | --- | --- |
| A1 Conceptual Model Start and Quality Revision | P | - | L | - | - | L |
| A2 Relational Structure and Process Mapping | S | L | P | - | - | L |
| A3 ERD Creation and Diagramming Practice | S | P | S | - | - | L |
| A4 Conceptual Modeling Refinement | P | S | S | - | - | S |
| A5 Normalization and Anomaly Analysis | L | L | P | - | - | L |
| A6 Business Rules and Performance Tradeoffs | L | - | P | - | - | L |
| A7 MongoDB Setup and Document Boundary Draft | L | - | L | P | L | S |
| A8 Relational vs Document Model Comparison | L | - | S | P | L | S |
| A9 MongoDB CRUD and Query Evidence | - | - | L | S | P | S |
| A10 Aggregation, Performance, and Defense Prep | - | - | L | S | P | P |
| Week 8 Capstone Modeling Defense | S | S | S | S | S | P |

---

## Core Ability Applicability

| Assignment | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- |
| A1 Conceptual Model Start and Quality Revision | S | P | S | S | - | L |
| A2 Relational Structure and Process Mapping | P | S | S | S | - | L |
| A3 ERD Creation and Diagramming Practice | S | P | P | S | L | S |
| A4 Conceptual Modeling Refinement | P | S | S | P | L | S |
| A5 Normalization and Anomaly Analysis | P | S | S | S | - | L |
| A6 Business Rules and Performance Tradeoffs | P | S | S | S | - | L |
| A7 MongoDB Setup and Document Boundary Draft | S | S | P | P | - | S |
| A8 Relational vs Document Model Comparison | P | P | S | S | - | S |
| A9 MongoDB CRUD and Query Evidence | P | S | S | S | - | S |
| A10 Aggregation, Performance, and Defense Prep | P | P | S | S | - | S |
| Week 8 Capstone Modeling Defense | S | P | S | S | L | P |

---

# Assignment Mapping Table

This table provides the same assignment-to-rubric alignment in the dot-based AMM format used across the other course MRS artifacts.

Use this table to quickly identify the most relevant rubric rows for each assignment. It is not intended to require scoring every row on every assignment. A competency should be scored only when the submitted evidence makes that competency observable.

---

## Assignment Mapping Legend

| Symbol | Meaning |
| --- | --- |
| **●●●** | Primary focus / major grading emphasis |
| **●●** | Secondary focus |
| **●** | Light/Tertiary focus or optional assessment when explicitly observable |
| **-** | Not assessed or not relevant |

---

## Technical Competency Codes

| Code | Description |
| --- | --- |
| T1 | Data Modeling Foundations |
| T2 | ERD Design and Model Communication |
| T3 | Relational Modeling and Data Integrity |
| T4 | Document Modeling and Representation Choice |
| T5 | MongoDB Operations as Model Evidence |
| T6 | Modeling Defense and AI-Assisted Design Practice |

---

## Core Ability Codes

| Code | Description |
| --- | --- |
| C1 | Solve Problems |
| C2 | Communicate Clearly |
| C3 | Work Productively |
| C4 | Value Learning |
| C5 | Work Cooperatively |
| C6 | Act Professionally |

---

## Phase 1 - Modeling Foundations and Early Structure

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 Conceptual Model Start and Quality Revision | ●●● | - | ● | - | - | ● | ●● | ●●● | ●● | ●● | - | ● |
| A2 Relational Structure and Process Mapping | ●● | ● | ●●● | - | - | ● | ●●● | ●● | ●● | ●● | - | ● |

---

## Phase 2 - Visual Modeling and Evidence-Based Revision

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A3 ERD Creation and Diagramming Practice | ●● | ●●● | ●● | - | - | ● | ●● | ●●● | ●●● | ●● | ● | ●● |
| A4 Conceptual Modeling Refinement | ●●● | ●● | ●● | - | - | ●● | ●●● | ●● | ●● | ●●● | ● | ●● |

---

## Phase 3 - Relational Quality, Rules, and Tradeoffs

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A5 Normalization and Anomaly Analysis | ● | ● | ●●● | - | - | ● | ●●● | ●● | ●● | ●● | - | ● |
| A6 Business Rules and Performance Tradeoffs | ● | - | ●●● | - | - | ● | ●●● | ●● | ●● | ●● | - | ● |

---

## Phase 4 - Document Modeling and MongoDB Evidence

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A7 MongoDB Setup and Document Boundary Draft | ● | - | ● | ●●● | ● | ●● | ●● | ●● | ●●● | ●●● | - | ●● |
| A8 Relational vs Document Model Comparison | ● | - | ●● | ●●● | ● | ●● | ●●● | ●●● | ●● | ●● | - | ●● |
| A9 MongoDB CRUD and Query Evidence | - | - | ● | ●● | ●●● | ●● | ●●● | ●● | ●● | ●● | - | ●● |
| A10 Aggregation, Performance, and Defense Prep | - | - | ● | ●● | ●●● | ●●● | ●●● | ●●● | ●● | ●● | - | ●● |

---

## Phase 5 - Capstone Modeling Defense

| Assignment | T1 | T2 | T3 | T4 | T5 | T6 | C1 | C2 | C3 | C4 | C5 | C6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 8 Capstone Modeling Defense | ●● | ●● | ●● | ●● | ●● | ●●● | ●● | ●●● | ●● | ●● | ● | ●●● |

---

# Part 7 - Recommended Schoology Row Sets

Use these as default row selections. Add or remove rows if a specific assignment variation changes the evidence.

| Assignment | Recommended Rows |
| --- | --- |
| A1 | T1, C2, C1, C4 |
| A2 | T3, T1, C1, C2 |
| A3 | T2, C2, C3, T1 |
| A4 | T1, T2, T3, C1, C4 |
| A5 | T3, C1, C2 |
| A6 | T3, C1, C2 |
| A7 | T4, C3, C4, C6 |
| A8 | T4, C2, C1, C6 |
| A9 | T5, C1, C2, C6 |
| A10 | T5, T6, C1, C2 |
| Week 8 Capstone | T6, C2, C6, plus T1/T2/T3/T4/T5 rows that match the selected pathway evidence |

Notes:

- C5 should be added only when peer review or collaborative evidence is explicitly collected.
- C6 should be included when AI disclosure, professional submission, or final defense accountability is central.
- T6 should be used lightly before Week 7 unless the assignment includes AI-assisted design evidence or defense preparation.

---

# Part 8 - Assignment Evidence Alignment

## A1 - Conceptual Model Start and Quality Revision

Primary evidence:

- conceptual model worksheet
- entity purpose list
- relationship statements
- open questions
- quality revision note

Best-fit rows:

- T1 Primary
- C2 Primary
- C1 Secondary
- C4 Secondary

---

## A2 - Relational Structure and Process Mapping

Primary evidence:

- entity/attribute/key table
- relationship link table
- integrity constraints
- process-to-data map
- process-driven revision

Best-fit rows:

- T3 Primary
- T1 Secondary
- C1 Primary
- C2 Secondary

---

## A3 - ERD Creation and Diagramming Practice

Primary evidence:

- ERD source/export
- notation and readability checklist
- assumptions
- design rationale
- tool-use notes

Best-fit rows:

- T2 Primary
- C2 Primary
- C3 Primary
- T1 Secondary

---

## A4 - Conceptual Modeling Refinement

Primary evidence:

- issue list
- revision plan
- revised model evidence
- conceptual pattern review
- change log
- model quality self-assessment

Best-fit rows:

- T1 Primary
- T2 Secondary
- T3 Secondary
- C1 Primary
- C4 Primary

---

## A5 - Normalization and Anomaly Analysis

Primary evidence:

- model excerpt
- anomaly/risk table
- normalization awareness explanation
- structural recommendation

Best-fit rows:

- T3 Primary
- C1 Primary
- C2 Secondary

---

## A6 - Business Rules and Performance Tradeoffs

Primary evidence:

- business rule list
- rule placement table
- system question/performance pressure note
- denormalization or performance tradeoff explanation

Best-fit rows:

- T3 Primary
- C1 Primary
- C2 Secondary

---

## A7 - MongoDB Setup and Document Boundary Draft

Primary evidence:

- setup/guided environment evidence
- access/system question notes
- collection boundary decision
- embed/reference draft
- sample document

Best-fit rows:

- T4 Primary
- C3 Primary
- C4 Primary
- C6 Secondary

---

## A8 - Relational vs Document Model Comparison

Primary evidence:

- two sample document options or variants
- embedding/reference comparison
- relational vs document comparison
- representation decision

Best-fit rows:

- T4 Primary
- C2 Primary
- C1 Primary
- C6 Secondary

---

## A9 - MongoDB CRUD and Query Evidence

Primary evidence:

- document shape summary
- system question
- expected result
- operation/query evidence
- retrieval explanation

Best-fit rows:

- T5 Primary
- C1 Primary
- C2 Secondary
- C6 Secondary

---

## A10 - Aggregation, Performance, and Defense Prep

Primary evidence:

- aggregation goal
- aggregation evidence/result
- aggregation-to-system-question map
- performance awareness note
- capstone evidence selection
- draft modeling claim

Best-fit rows:

- T5 Primary
- T6 Primary
- C1 Primary
- C2 Primary

---

## Week 8 - Capstone Modeling Defense

Primary evidence:

- capstone evidence index
- system scope
- ERD or visual model
- business rules
- relational model evidence
- NoSQL/document model evidence, if used
- relational vs document consideration
- final design defense
- AI assistance disclosure

Best-fit rows:

- T6 Primary
- C2 Primary
- C6 Primary
- T1/T2/T3/T4/T5 as supported by selected pathway evidence

---

# Part 9 - AI Assistance Scoring Guidance

AI use should usually be evaluated through C4 and C6, not as a standalone technical row.

Use C4 when AI evidence shows learning behavior:

- student used AI for critique
- student revised after feedback
- student accepted/rejected suggestions thoughtfully

Use C6 when AI evidence shows professional accountability:

- student disclosed AI use
- student identified what AI generated
- student verified claims
- student explained final ownership

Use T6 when AI evidence is part of modeling defense or explicit assignment evidence:

- capstone evidence index
- final design defense
- Pathway 2 compressed design disclosure
- AI-ready retrieval boundary notes, if assigned

Do not penalize a student for not using AI unless AI use is explicitly required. Do assess transparency and accountability when AI is used.

---

# Part 10 - Instructor Workflow

Recommended grading workflow:

1. Identify assignment pathway and required files.
2. Select the recommended rows for that assignment.
3. Score primary technical evidence first.
4. Score communication and problem-solving evidence next.
5. Score C6 only when professionalism, AI disclosure, or evidence organization is meaningfully observable.
6. Use instructor feedback sections:
   - Good
   - Improvements
   - Suggestions

Avoid scoring all T1-T6 and C1-C6 on every assignment. The applicability matrix exists to keep grading focused and repeatable.

---

# Final System Statement

MRS-DM v2 aligns the rubric system to the actual scaffolded assignments and demos for Course 123.

The technical rows reflect the revised WIDS competencies. The Core Ability rows preserve institutional competency names while defining Course 123-specific evidence lenses.
