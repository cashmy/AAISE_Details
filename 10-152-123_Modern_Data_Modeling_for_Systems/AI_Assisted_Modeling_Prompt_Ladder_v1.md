# AI-Assisted Modeling Prompt Ladder - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.2`  
Purpose: Define the staged use of AI prompts across demos, assignments, tangible artifacts, and student reflection

---

# Purpose

This artifact defines how AI assistance and AI-enabled collaboration should be introduced across Course 123.

AI should support modeling judgment, not replace it.

The repeated pattern is:

```text
manual attempt -> structured prompt -> AI feedback or targeted contribution -> human review -> revised tangible
```

Students should learn to use AI as a reviewer, critic, question generator, comparison partner, and explanation aid before using it as a targeted generator.

This course uses two shared AI framing models:

1. AI use classification:
   - AI Assistance: AI supports thinking, critique, explanation, or review.
   - AI Enabled / Collaboration: AI works with the student to revise, compare, generate, or complete a targeted part after student framing.
   - AI Embedded: AI operates inside a tool, platform, or workflow.
2. Prompt structure:
   - Context
   - Attempt
   - Allowed help
   - Constraints
   - Clarifying questions
   - Output format

---

# Core Principle

AI enters after the student has created a manual attempt.

Students should not use AI to produce the first version of a model artifact unless a specific assignment explicitly permits that later in the course.

The course should preserve:

- manual authorship
- student explanation
- human judgment
- evidence-based revision
- transparent AI use

---

# AI Use Levels and Classifications

| Course Level | AI Classification | Meaning | Typical Use |
| --- | --- | --- | --- |
| Manual First | No AI or delayed AI | Student creates initial artifact before AI use | Weeks 1-3 |
| AI-Assisted | AI Assistance | AI critiques, questions, compares, explains, or checks | Weeks 1-8 |
| AI-Enabled | AI Enabled / Collaboration | AI may generate or revise a targeted piece after student framing | Weeks 6-8 |
| AI-Embedded Awareness | AI Embedded | Student recognizes that a tool may contain AI capability inside the workflow | Optional discussion and disclosure |
| AI Creation/Development | Out of scope for this course | Building LLMs, RAG/CAG systems, model-training workflows, or AI products | Not assessed in Course 123 |

---

# Approved Prompt Behaviors

Good AI prompts should ask AI to:

- critique
- identify gaps
- challenge assumptions
- ask clarifying questions
- compare options
- explain tradeoffs
- identify risks
- suggest verification steps
- review for clarity

Good AI prompts should include:

- context for the assignment and artifact
- the student's manual attempt
- the kind of help allowed
- constraints on what AI should not do
- clarifying-question behavior when context may be missing
- requested output format

Early prompts should avoid asking AI to:

- complete the assignment
- produce the final model
- design the whole database
- generate the final answer
- replace the student's explanation

---

# Required Student AI Assistance Notes

Every assignment that permits AI should include this short evidence section:

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

This section should be concise. The purpose is to document student judgment, not create a long reflection essay.

---

# Prompt Ladder Overview

| Assignment | Manual First Artifact | AI Prompt Function | Student Review Output | Revised Tangible |
| --- | --- | --- | --- | --- |
| A1 | Conceptual model draft | AI Assistance: critique missing/ambiguous entities and relationships | Accepted/rejected suggestion notes | Revised conceptual model |
| A2 | Relational structure draft | AI Assistance: challenge keys, relationships, attributes, process gaps | Process-driven revision notes | Revised relational structure and process map |
| A3 | Text model and ERD draft | AI Assistance: identify cardinality, notation, and readability risks | Diagram issue list and accepted/rejected notes | ERD with assumptions and checklist |
| A4 | Revision plan | AI Assistance: suggest conceptual refinement possibilities | Pattern decision notes | Revised model and change log |
| A5 | Anomaly analysis | AI Assistance: challenge anomaly reasoning | Verified risk notes | Anomaly/risk table |
| A6 | Rule placement draft | AI Assistance: compare rule placement and performance risks | Final placement reasoning | Rule/performance tradeoff table |
| A7 | Document boundary draft | AI Assistance or Collaboration: critique boundary; optionally clean a sample JSON after framing | Boundary revision note | First document model |
| A8 | Representation comparison | AI Assistance or Collaboration: challenge tradeoffs; optionally clean sample JSON variants | Accepted/rejected tradeoff notes | Final comparison table |
| A9 | Query intent and expected result | AI Enabled / Collaboration: suggest or critique a MongoDB operation after intent is stated | Tested query notes | Query/access-pattern evidence |
| A10 | Aggregation goal and defense claim | AI Enabled / Collaboration: critique evidence, aggregation, and claim strength | Defense revision priorities | Aggregation evidence and revised claim |
| Week 8 | Final defense draft | AI Assistance or Collaboration depending on pathway | Final revision notes and disclosure | Final modeling defense |

---

# Assignment-Level Prompt Guidance

## A1 - Conceptual Model Start and Quality Revision

AI role: critique early conceptual thinking.

Use AI after the student has:

- selected a scenario
- written system intent
- identified candidate entities
- written relationship statements
- listed open questions

Prompt should ask AI to:

- identify missing entities
- identify ambiguous relationships
- surface assumptions
- ask clarifying questions

Student must decide what to accept or reject.

## A2 - Relational Structure and Process Mapping

AI role: challenge relational structure.

Use AI after the student has:

- entity/attribute table
- key candidates
- relationship links
- process map draft

Prompt should ask AI to:

- challenge primary key choices
- identify missing relationship links
- flag misplaced attributes
- identify process gaps

Student must revise based on process support, not AI authority.

## A3 - ERD Creation and Diagramming Practice

AI role: identify diagramming risks before or after the student creates a draft.

Use AI after the student has:

- text model
- relationship list
- manual ERD draft or planned ERD
- assumptions or uncertainty notes

Prompt should ask AI to:

- identify cardinality questions
- find possible many-to-many relationships
- flag associative entity needs
- surface assumptions
- critique readability from a written description of the diagram

Student must create the diagram in draw.io or another approved ERD-capable tool. AI may critique; it should not replace the student's diagramming work.

## A4 - Conceptual Modeling Refinement

AI role: suggest refinement possibilities without requiring all of them.

Use AI after the student has:

- revision plan
- model issue list
- current ERD/model notes

Prompt should ask AI to:

- identify roles, subtypes, categories, hierarchies, event entities, associative entities, or boundary issues
- explain which suggestions fit the current scope
- warn against unnecessary complexity

Student must document the selected conceptual pattern decision.

## A5 - Normalization and Anomaly Analysis

AI role: challenge anomaly reasoning.

Use AI after the student has:

- identified a possible anomaly
- explained the risk
- proposed a normalization-related recommendation

Prompt should ask AI to:

- check anomaly type
- identify missing maintenance risks
- explain whether normalization helps
- identify over-normalization risk

Student must verify the final risk explanation.

## A6 - Business Rules and Performance Tradeoffs

AI role: compare rule placement and performance implications.

Use AI after the student has:

- business rule list
- first rule placement table
- access pattern note

Prompt should ask AI to:

- critique enforcement location
- identify risks of placement
- identify performance pressure
- suggest responsible denormalization considerations

Student must justify final placement.

## A7 - MongoDB Setup and Document Boundary Draft

AI role: critique document boundary.

Use AI after the student has:

- access patterns
- proposed collection boundary
- first sample document idea

Prompt should ask AI to:

- compare embedding and referencing
- identify update or duplication concerns
- connect design to access patterns
- avoid generating a full database

Student may use AI suggestions to revise the first document.

## A8 - Relational vs Document Model Comparison

AI role: challenge representation tradeoffs.

Use AI after the student has:

- sample document models
- initial comparison table
- stated access patterns

Prompt should ask AI to:

- compare read ease
- compare update difficulty
- identify duplication
- evaluate fit to access patterns

Student must decide which tradeoffs matter most.

## A9 - MongoDB CRUD and Query Evidence

AI role: help with query after intent and expected result are stated.

Use AI after the student has:

- system question
- expected result
- document shape
- attempted query or query plan

Prompt may ask AI to:

- suggest query approach
- explain operators
- identify test steps
- troubleshoot query logic

Student must test and explain the final query.

## A10 - Aggregation, Performance, and Final Modeling Defense Prep

AI role: critique evidence and draft claim.

Use AI after the student has:

- aggregation goal
- aggregation result
- performance note
- draft modeling claim

Prompt should ask AI to:

- check whether evidence supports the claim
- identify weak performance reasoning
- compare relational/document claims fairly
- recommend evidence for final defense

Student must revise the defense claim.

## Week 8 - Final Modeling Defense

AI role: critique the final defense.

Use AI after the student has:

- final model packet
- comparison table
- retrieval boundary notes
- draft defense

Prompt should ask AI to:

- identify unsupported claims
- identify missing tradeoffs
- critique AI-ready retrieval boundaries
- suggest revision priorities

Student must remain responsible for the final defense.

---

# Instructor Demo Requirement

Each instructor AI demo should show:

1. the manual attempt
2. the prompt
3. the AI response or prepared AI response excerpt
4. instructor review labels:
   - Accept
   - Reject
   - Modify
   - Verify Later
   - Out of Scope
5. the final tangible

---

# Quality Check

Before approving a prompt, ask:

- Does it preserve manual attempt first?
- Does it ask for critique before generation?
- Does it require student judgment?
- Does it produce useful feedback for the tangible artifact?
- Does it avoid completing the assignment for the student?
- Does it include a verification or review expectation?
