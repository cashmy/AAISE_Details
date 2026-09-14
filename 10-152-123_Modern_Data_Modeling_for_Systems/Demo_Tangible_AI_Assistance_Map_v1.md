# Demo Tangible and AI Assistance Map - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.2`  
Purpose: Define instructor demo tangibles, AI-assistance moments, and student transfer artifacts before drafting full assignments

---

# Design Position

The course demos should teach the modeling process, not simply reveal finished answers.

Each instructor-led demo should follow a scaffolded pattern:

```text
manual attempt -> structured AI prompt -> AI output or targeted contribution -> instructor review -> finalized tangible
```

This pattern preserves student authorship and human judgment:

1. The instructor first models a human attempt.
2. The instructor demonstrates a bounded AI-assistance prompt.
3. The instructor reviews the AI output critically.
4. The instructor accepts, rejects, or revises suggestions.
5. The instructor produces a final tangible artifact.

The AI output should help inform the tangible, not replace the modeling decision.

Course AI demos should use the shared prompt pattern:

```text
Context -> Attempt -> Allowed Help -> Constraints -> Questions -> Output
```

Course AI demos should also name the closest AI use classification:

- AI Assistance: AI supports critique, explanation, review, or thinking.
- AI Enabled / Collaboration: AI helps create, revise, compare, or complete a targeted part after manual framing.
- AI Embedded: AI operates inside a tool or system that directly supports the workflow.

---

# Demo Scenario Strategy

## Primary Progressive Demo: E-Commerce with Reviews/Ratings

E-commerce will be the instructor-led demo scenario across the weekly course arc.

Purpose:

- Provide a consistent, familiar domain.
- Show the same model evolving over time.
- Demonstrate how weekly modeling decisions accumulate.
- Avoid using the same scenarios students select for assignments.

E-commerce should appear in instructor demos, not as a student assignment option.

## Full Reference Demo: Project Management System

Project Management will serve a different function. It is a full-fledged database design reference system, similar in function to PageForge in Course 118.

Purpose:

- Provide a mature, completed reference model.
- Show what a fully developed database design can look like.
- Backfill the finished design into the progressive weekly scaffold.
- Help the instructor compare early-stage student tangibles against a more complete design without expecting students to produce that level of complexity immediately.

Project Management should not replace the E-commerce weekly demo. It should be used as a reference, contrast, or optional enrichment artifact.

---

# Student Scenario Transfer Guardrail

Student scenarios should remain separate from instructor demo scenarios:

1. Student/Course/Schedule Tracker
2. Customer/Orders/Invoicing
3. Books/Library
4. Music Collection

The demo and student assignments may share artifact forms, but not scenario content.

Example:

| Instructor Demo | Student Transfer |
| --- | --- |
| E-commerce entity purpose list | Student creates entity purpose list for selected scenario |
| E-commerce ERD revision | Student revises ERD for selected scenario |
| E-commerce document boundary decision | Student chooses document boundaries for selected scenario |

This supports transfer without enabling copying.

---

# AI Assistance Pattern

Every AI-assisted demo should show four visible moves.

## 1. Manual Attempt

The instructor creates an imperfect but reasonable first attempt.

This may include:

- entity list
- relationship statements
- ERD draft
- rule placement table
- document boundary decision
- query/access-pattern map

## 2. Appropriate AI Prompt

The prompt should ask AI to critique, challenge, question, compare, or identify risks.

The prompt should visibly include:

- context
- the manual attempt
- the allowed kind of help
- constraints on what AI should not do
- clarifying-question or assumption behavior
- requested output format

Preferred prompt verbs:

- critique
- identify gaps
- challenge assumptions
- ask clarifying questions
- compare options
- suggest risks
- explain tradeoffs

Avoid early prompt verbs:

- complete
- create the final model
- do my assignment
- design the whole database
- generate the final answer

## 3. AI Output

The instructor should show or summarize AI output.

Prepared AI output may be better than live AI output when the goal is to teach judgment. A prepared output can include:

- useful suggestion
- plausible but out-of-scope suggestion
- incorrect suggestion
- ambiguity-revealing question
- overcomplicated recommendation

## 4. Review and Finalized Output

The instructor reviews the AI output visibly.

Recommended review labels:

- Accept
- Reject
- Modify
- Verify Later
- Out of Scope

The finalized tangible should show what changed because of AI review and what did not change.

---

# Reusable Student AI Assistance Notes

Each AI-enabled assignment should include a small reflection section:

```text
AI use classification:
Manual work completed before AI:
Context provided:
Attempt shown:
Allowed help requested:
Constraints stated:
Questions / assumptions requested:
Output format requested:
Exact prompt used:
Most useful AI suggestion:
Suggestion I rejected:
Change I made after reviewing AI:
What I verified myself:
```

This should remain short. The goal is AI accountability, not a second essay.

---

# Weekly Demo and Tangible Map

## A1 - Conceptual Model Start and Quality Revision

Week: 1  
Instructor demo scenario: E-commerce with reviews/ratings  
Student transfer scenarios: student-selected scenario

### Manual Demo Tangible

- E-commerce system intent statement
- Candidate entity list
- Entity purpose notes
- Plain-English relationship statements
- Open modeling questions

### AI Prompt Type

Critique missing or ambiguous entities and relationships.

Example prompt:

```text
I am creating an early conceptual data model for an e-commerce system with customers, products, orders, reviews, and categories.

Do not create a final model. Critique my first attempt.

Identify:
1. entities that may be missing,
2. relationships that may be ambiguous,
3. assumptions I should write down,
4. questions I should answer before making a formal ERD.

Keep the feedback appropriate for beginning data modeling students.
```

### AI Output Review Focus

- Does AI invent unnecessary complexity?
- Does AI identify real ambiguity?
- Does AI confuse implementation detail with conceptual modeling?

### Finalized Demo Tangible

- Revised entity purpose list
- Revised relationship statements
- AI-informed open question list
- Quality revision note

### Student Tangible

- Conceptual model worksheet
- Entity purpose list
- Relationship statement list
- Open modeling questions
- AI assistance notes, if AI is used

---

## A2 - Relational Structure and Process Mapping

Week: 2  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Entity/attribute/key table
- Relationship type notes
- Plain-language integrity constraints
- Initial process-to-data map

### AI Prompt Type

Challenge keys, relationships, attributes, and process gaps.

Example prompt:

```text
Here is my draft relational structure for an e-commerce model.

Critique it as a reviewer. Do not rewrite the whole model.

Look for:
1. weak or unclear primary key choices,
2. missing foreign key relationships,
3. attributes that may belong on a different entity,
4. system actions that the model may not support,
5. integrity constraints I should write in plain language.

Keep feedback introductory and explain why each issue matters.
```

### AI Output Review Focus

- Are suggested attributes necessary for the current scope?
- Are relationship changes supported by system processes?
- Are constraints stated in student-understandable language?

### Finalized Demo Tangible

- Revised relational structure table
- Revised process-to-data map
- Process-driven revision note

### Student Tangible

- Relational structure worksheet
- Process-to-data map
- Integrity constraints
- AI assistance notes, if AI is used

---

## A3 - ERD Creation and Diagramming Practice

Week: 3  
Instructor demo scenario: E-commerce with reviews/ratings  
Tool focus: draw.io

### Manual Demo Tangible

- E-commerce ERD plan
- Draft E-commerce ERD in draw.io
- Notation checklist
- Assumption and uncertainty notes
- Tool alternatives exposure notes

### AI Prompt Type

Review the textual model before or after diagram drafting.

Example prompt:

```text
I am preparing to draw an ERD from this entity and relationship list.

Do not draw the diagram for me.

Review the text and identify:
1. relationships that need cardinality clarification,
2. possible many-to-many relationships,
3. entities that may need an associative entity,
4. assumptions I should show or note before diagramming.
```

### AI Output Review Focus

- Does AI correctly identify many-to-many relationships?
- Does AI overuse associative entities?
- Does AI assume details not present in the scenario?

### Finalized Demo Tangible

- ERD
- Notation checklist
- AI-informed uncertainty notes
- Tool-use notes

### Student Tangible

- draw.io ERD or approved equivalent
- Notation checklist
- Assumption list
- Design rationale

---

## A4 - Conceptual Modeling Refinement

Week: 4  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Revision plan
- Model issue list
- Change log draft

### AI Prompt Type

Suggest conceptual refinement possibilities without applying all of them.

Example prompt:

```text
I have an ERD for an e-commerce system with customers, products, orders, reviews, and categories.

Critique the model for conceptual refinement.

Identify where I should consider:
1. roles,
2. subtypes,
3. categories or hierarchies,
4. event entities,
5. associative entities,
6. boundary clarification.

Do not tell me to add everything. Explain which possibilities are most important and which may be too advanced for the current scope.
```

### AI Output Review Focus

- Does AI distinguish useful complexity from premature complexity?
- Does AI recommend changes that fit the current course scope?
- Does AI expose a real weakness in the current model?

### Finalized Demo Tangible

- Revised model
- Change log
- Conceptual pattern note
- Model quality self-assessment

### Student Tangible

- Revision plan
- Revised ERD or model notes
- Change log
- Conceptual pattern note

---

## A5 - Normalization and Anomaly Analysis

Week: 5  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Sample risky table or model excerpt
- Anomaly/risk notes
- Normalization recommendation

### AI Prompt Type

Challenge anomaly reasoning.

Example prompt:

```text
Here is a simplified table/model excerpt from an e-commerce system.

Critique my anomaly analysis.

Identify:
1. possible insert, update, or delete anomalies,
2. whether my explanation of the risk is accurate,
3. whether normalization would help,
4. one risk of over-normalizing for this course-level model.
```

### AI Output Review Focus

- Does AI correctly identify anomaly types?
- Does AI over-normalize beyond the course need?
- Does AI recognize when a design may be acceptable?

### Finalized Demo Tangible

- Verified anomaly/risk table
- Normalization awareness explanation
- Structural recommendation

### Student Tangible

- Anomaly/risk table
- Normalization recommendation
- AI assistance notes, if AI is used

---

## A6 - Business Rules and Performance Tradeoffs

Week: 5  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Business rule list
- Rule placement table
- Access pattern note
- Performance tradeoff explanation

### AI Prompt Type

Compare rule placement options and performance implications.

Example prompt:

```text
I am deciding where to enforce business rules in an e-commerce system.

Critique this rule placement table.

For each rule, identify:
1. whether database, application/backend, user process, or mixed enforcement seems appropriate,
2. what could go wrong with that placement,
3. whether a performance or denormalization tradeoff should be considered.

Keep the response focused on beginner-level database design judgment.
```

### AI Output Review Focus

- Does AI distinguish rule enforcement from data storage?
- Does AI identify realistic performance pressure?
- Does AI recommend denormalization responsibly?

### Finalized Demo Tangible

- Revised rule placement table
- Access pattern note
- Performance tradeoff explanation

### Student Tangible

- Rule placement table
- Access-pattern tradeoff note
- AI assistance notes, if AI is used

---

## A7 - MongoDB Setup and Document Boundary Draft

Week: 6  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Access pattern notes
- Collection boundary decision
- First sample document

### AI Prompt Type

Critique collection boundaries after manual framing.

Example prompt:

```text
I am converting part of an e-commerce relational model into MongoDB documents.

My main access patterns are:
1. show a product detail page with recent reviews,
2. show a customer's order history.

Critique my proposed collection boundary.

Do not generate a full database. Identify whether embedding or referencing seems appropriate and what tradeoff I should explain.
```

### AI Output Review Focus

- Does AI tie suggestions to access patterns?
- Does AI treat MongoDB as documents rather than tables-in-JSON?
- Does AI ignore update or duplication concerns?

### Finalized Demo Tangible

- Document boundary decision
- First sample document
- Tradeoff note

### Student Tangible

- Access pattern notes
- Document boundary worksheet
- First sample document

---

## A8 - Relational vs Document Model Comparison

Week: 6  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Embedded vs referenced comparison
- Relational vs document tradeoff table
- Two sample documents

### AI Prompt Type

Challenge representation tradeoffs.

Example prompt:

```text
I have two possible MongoDB document designs for an e-commerce scenario.

Critique the tradeoffs.

Compare:
1. what each design makes easier to read,
2. what each design makes harder to update,
3. where duplication may appear,
4. which design better fits the stated access patterns.

Do not choose only based on what looks simpler.
```

### AI Output Review Focus

- Does AI connect tradeoffs to access patterns?
- Does AI identify duplication and update concerns?
- Does AI treat both options fairly?

### Finalized Demo Tangible

- Revised comparison table
- Selected document approach
- Representation decision explanation

### Student Tangible

- Embedded/reference comparison
- Relational/document tradeoff table
- Sample documents

---

## A9 - MongoDB CRUD and Query Evidence

Week: 7  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Query/access-pattern map
- Expected-result note
- CRUD/query evidence

### AI Prompt Type

Generate or critique a query after students state intent and expected result.

Example prompt:

```text
I have a MongoDB collection for products with embedded recent reviews.

System question:
Find products in a category with an average rating above 4.

Expected result:
A list of matching product names, category names, and average ratings.

Suggest a MongoDB query or aggregation approach. Explain each stage or operator, and identify what I should test to verify the result.
```

### AI Output Review Focus

- Does the query match the stated document shape?
- Does the query produce the expected result?
- Can the student explain the operators?

### Finalized Demo Tangible

- Tested query
- Result evidence
- Retrieval explanation

### Student Tangible

- Query/access-pattern map
- Expected result notes
- CRUD/query evidence

---

## A10 - Aggregation, Performance, and Final Modeling Defense Prep

Week: 7  
Instructor demo scenario: E-commerce with reviews/ratings

### Manual Demo Tangible

- Aggregation-to-system-question map
- Aggregation result
- Performance awareness note
- Draft modeling claim

### AI Prompt Type

Critique aggregation and final defense claim.

Example prompt:

```text
I am preparing a final modeling defense for an e-commerce data model.

Here is my aggregation goal and draft claim.

Critique:
1. whether the aggregation evidence supports the system question,
2. whether my performance note is specific enough,
3. whether my claim fairly compares relational and document representations,
4. what evidence I should bring into the final defense.

Do not rewrite the defense for me. Help me identify what needs strengthening.
```

### AI Output Review Focus

- Does AI ask for stronger evidence?
- Does AI overstate the benefits of one representation?
- Does AI help connect operations to modeling decisions?

### Finalized Demo Tangible

- Aggregation evidence
- Performance note
- Capstone evidence selection
- Revised modeling claim

### Student Tangible

- Aggregation map
- Performance note
- Capstone evidence selection
- Draft modeling claim

---

# Week 8 Capstone Demo

Instructor demo scenario: E-commerce with reviews/ratings  
Student transfer scenarios: selected student scenario

## Manual Demo Tangible

- Final E-commerce model packet summary
- Relational/document comparison
- Access pattern and performance evidence
- AI-ready retrieval boundary notes
- Final defense claim

## AI Prompt Type

Critique the final defense for evidence, design-fit reasoning, and AI-ready data boundaries.

Example prompt:

```text
I am preparing a short final defense of an e-commerce data model.

Critique my defense.

Look for:
1. unsupported claims,
2. unclear explanation of what the design does not handle yet,
3. weak comparison between relational and document approaches,
4. unclear AI-ready retrieval boundaries,
5. places where I need to mention filtering, metadata, provenance, or excluded data.

Do not rewrite the final response. Give critique and revision priorities.
```

## AI Output Review Focus

- Does AI expose unsupported claims?
- Does AI improve retrieval-boundary thinking?
- Does AI preserve the student's responsibility to defend the model?

## Finalized Demo Tangible

- Final modeling defense example
- AI-ready boundary notes
- Evidence checklist

## Student Tangible

- Final model packet
- Modeling defense
- AI-ready retrieval boundary map
- AI assistance notes, if AI is used

---

# Template Candidates

The following templates should be created before full student-facing assignments are produced:

1. `Conceptual_Model_Worksheet.md`
2. `Relational_Structure_Table_Template.md`
3. `ERD_Review_Checklist.md`
4. `Model_Revision_Log_Template.md`
5. `Anomaly_Risk_Table_Template.md`
6. `Rule_Placement_Table_Template.md`
7. `Document_Boundary_Worksheet.md`
8. `Relational_vs_Document_Comparison_Template.md`
9. `Query_Access_Pattern_Map_Template.md`
10. `Aggregation_Evidence_Template.md`
11. `Capstone_Modeling_Defense_Template.md`
12. `AI_Assistance_Notes_Template.md`

---

# Instructor Quality Check

Before drafting a demo, verify:

- Does the demo begin with a manual attempt?
- Does the AI prompt ask for critique or comparison before generation?
- Does the demo include an AI output review step?
- Does the finalized tangible show human judgment?
- Is the student tangible similar in form but different in content?
- Does the demo preserve transfer from E-commerce to student-selected scenarios?
- Does the demo avoid revealing a finished answer for student scenarios?
