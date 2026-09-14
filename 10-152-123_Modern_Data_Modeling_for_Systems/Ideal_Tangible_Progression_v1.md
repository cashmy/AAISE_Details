# Ideal Tangible Progression - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.1`  
Purpose: Define the tangible artifact progression students should see, practice, revise, and submit across the course

---

# Purpose

This artifact identifies the ideal tangible outputs for Course 123 before full demos and student-facing assignments are written.

The course should make modeling visible. Students should not only talk about data modeling; they should produce artifacts that show how a model is discovered, structured, visualized, revised, stressed, re-represented, operated on, and defended.

The tangible progression should follow the course movement:

```text
intent -> structure -> visualization -> refinement -> stress test -> representation comparison -> operation evidence -> defense
```

---

# Design Rule

Every assignment and instructor demo should produce a tangible artifact.

The artifact may be:

- a worksheet
- a table
- a diagram
- a revision log
- a comparison matrix
- a query/evidence map
- a final defense packet

But it should not be only a paragraph of explanation.

Explanation matters, but explanation should attach to an artifact.

---

# Tangible Progression Overview

| Assignment | Modeling Move | Instructor Demo Tangible | Student Tangible | Template/Form Needed |
| --- | --- | --- | --- | --- |
| A1 | Move from scenario to information shape | E-commerce conceptual model worksheet | Conceptual model worksheet for selected scenario | `Conceptual_Model_Worksheet.md` |
| A2 | Move from conceptual model to relational structure | E-commerce relational structure table and process map | Relational structure table and process-to-data map | `Relational_Structure_Table_Template.md` |
| A3 | Move from structure to visible ERD | E-commerce ERD in draw.io plus sample outputs from alternatives | Student ERD with assumptions, checklist, and tool notes | `ERD_Diagramming_Worksheet.md` |
| A4 | Move from first model to improved model | E-commerce revision plan and change log | Revision plan, revised model, change log | `Model_Revision_Log_Template.md` |
| A5 | Move from model to anomaly/risk reasoning | E-commerce anomaly/risk table | Anomaly/risk table and recommendation | `Anomaly_Risk_Table_Template.md` |
| A6 | Move from structure to responsibility/tradeoff | E-commerce rule placement and access-pattern table | Rule placement and performance tradeoff table | `Rule_Placement_Table_Template.md` |
| A7 | Move from relational model to document boundary | E-commerce document boundary worksheet | Document boundary worksheet and first sample document | `Document_Boundary_Worksheet.md` |
| A8 | Move from one representation to comparison | E-commerce relational vs document comparison | Relational vs document comparison table | `Relational_vs_Document_Comparison_Template.md` |
| A9 | Move from model to operation evidence | E-commerce query/access-pattern map | Query/access-pattern map and CRUD/query evidence | `Query_Access_Pattern_Map_Template.md` |
| A10 | Move from operation evidence to defense prep | E-commerce aggregation evidence and claim draft | Aggregation evidence, performance note, defense claim | `Aggregation_Evidence_Template.md` |
| Week 8 | Move from evidence to modeling defense | E-commerce final modeling defense packet | Final modeling defense packet | `Capstone_Modeling_Defense_Template.md` |

---

# Weekly Tangible Intent

## A1 - Conceptual Model Worksheet

The first tangible should help students avoid jumping directly to tables.

It should capture:

- system intent
- users or stakeholders
- candidate entities
- entity purpose
- plain-English relationships
- open modeling questions
- first quality revision

The worksheet should be intentionally incomplete. Its job is to make early thinking visible.

## A2 - Relational Structure Table and Process Map

The second tangible should sharpen the A1 model.

It should capture:

- entities
- attributes
- primary key candidates
- foreign key or relationship links
- relationship type
- integrity constraints
- system actions
- process-to-data mapping

This tangible should show that relational structure exists to support system behavior.

## A3 - ERD Creation and Diagramming Practice

The third tangible should be a first formal visual model and evidence that the student can use a diagramming tool well enough to communicate a model.

It should capture:

- entities
- key attributes
- important non-key attributes
- relationships
- cardinality
- assumptions
- notation uncertainty
- readability/self-review notes
- tool used and submitted file/export

This tangible should use draw.io unless another approved tool is chosen. Other acceptable tools may include Lucidchart, Miro, FigJam, ERDPlus, Visual Paradigm, Creately, or Mermaid. Tool features that generate SQL or database scripts should not be used in Course 123.

## A4 - Revision Plan and Change Log

The fifth tangible should show deliberate refinement.

It should capture:

- issues discovered
- planned revisions
- conceptual pattern considered
- change log
- revised model
- model quality self-assessment

This tangible should prevent random complexity growth.

## A5 - Anomaly/Risk Table

The fifth tangible should stress the model for maintenance risk.

It should capture:

- possible anomaly
- where the risk appears
- why it matters
- whether normalization helps
- structural recommendation

This tangible should teach normalization as a reasoning tool.

## A6 - Rule Placement and Performance Tradeoff Table

The sixth tangible should show model responsibility.

It should capture:

- business rule
- possible enforcement location
- placement reason
- risk of that placement
- access pattern
- performance or denormalization tradeoff

This tangible should teach students that models live inside systems.

## A7 - Document Boundary Worksheet

The seventh tangible should introduce document modeling through access patterns.

It should capture:

- selected relational area
- access patterns
- proposed collection boundary
- embedded data
- referenced data
- first sample document
- tradeoff note

This tangible should prevent "tables in JSON" thinking.

## A8 - Relational vs Document Comparison

The eighth tangible should compare representations.

It should capture:

- relational approach
- document approach
- what each makes easier
- what each makes harder
- duplication/update concerns
- recommended representation for selected access pattern

This tangible should show that modeling is choice under constraints.

## A9 - Query/Access-Pattern Map

The ninth tangible should connect operations to model behavior.

It should capture:

- system question
- expected result
- relevant collection or data structure
- query or CRUD operation
- result evidence
- retrieval explanation

This tangible should make operations evidence for the model, not disconnected syntax practice.

## A10 - Aggregation Evidence and Defense Claim

The tenth tangible should prepare the final defense.

It should capture:

- aggregation goal
- system question answered
- aggregation result
- performance awareness note
- selected capstone evidence
- draft modeling claim

This tangible should bridge MongoDB operations into modeling judgment.

## Week 8 - Final Modeling Defense Packet

The final tangible should synthesize the course.

It should capture:

- final model summary
- relational/document comparison
- access pattern and performance evidence
- AI-ready retrieval boundary notes
- tradeoff defense
- final recommendation

This tangible should answer:

```text
Given this system need, why is this representation a responsible choice,
and what are its tradeoffs?
```

---

# Template Priority

Markdown templates should be created in this order:

1. `AI_Assistance_Notes_Template.md`
2. `Conceptual_Model_Worksheet.md`
3. `Relational_Structure_Table_Template.md`
4. `ERD_Notation_Checklist.md`
5. `ERD_Review_Checklist.md`
6. `Model_Revision_Log_Template.md`
7. `Anomaly_Risk_Table_Template.md`
8. `Rule_Placement_Table_Template.md`
9. `Document_Boundary_Worksheet.md`
10. `Relational_vs_Document_Comparison_Template.md`
11. `Query_Access_Pattern_Map_Template.md`
12. `Aggregation_Evidence_Template.md`
13. `Capstone_Modeling_Defense_Template.md`

---

# Quality Check

Before approving a tangible, ask:

- Does this artifact make student thinking visible?
- Does it contain a CORE modeling decision?
- Does it avoid premature implementation detail?
- Does it create evidence the instructor can review?
- Does it prepare students for a later artifact?
- Does it transfer from the E-commerce demo to student-selected scenarios?
