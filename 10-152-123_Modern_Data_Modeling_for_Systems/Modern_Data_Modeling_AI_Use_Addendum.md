# MODERN DATA MODELING AI USE ADDENDUM

---

# Relationship to the Standard Policy

This addendum applies the [Standard Student AI Use Policy](D:\@Artifact_Generation\108_AAISE_Details\Standard_Student_AI_Use_Policy.md:1) to `10-152-123 Modern Data Modeling for Systems`.

It defines how the general standard is implemented in this specific course.

Where this addendum is more specific than the standard policy, this addendum takes precedence for this course.

---

# Course Position

This course uses AI as a modeling review and revision aid, not as a replacement for student modeling decisions.

Students are learning how to identify system boundaries, entities, relationships, attributes, rules, model quality issues, representation choices, and evidence-based design claims. Because those decisions are the main learning target, most AI use in this course should happen after a manual attempt.

The normal course pattern is:

1. Make a manual modeling attempt.
2. Use AI to critique, question, compare, or revise the attempt.
3. Review the AI output.
4. Accept, modify, or reject suggestions.
5. Explain the final modeling decision in the student's own words.

AI output can inform the work, but the student remains responsible for the final model.

---

# Important Course Boundary

This course introduces database modeling before database querying.

Students may use the concepts of:

* tables
* rows
* columns
* entities
* relationships
* attributes
* collections
* documents
* fields
* BSON / JSON-style document structure

Students should not use SQL in this course unless the instructor explicitly gives a special exception.

SQL will be introduced in `10-152-120 Database Query and Design`.

---

# AI Progression in This Course

## Weeks 1-5: AI Assistance After Manual Modeling

During the conceptual, relational, diagramming, revision, normalization, and business-rule portions of the course, AI should mostly be used for:

* critique
* clarification
* alternative questions
* missing assumption checks
* model quality review
* revision suggestions

Students should complete the required manual attempt before using AI when the assignment says manual-first.

## Weeks 6-7: Limited AI Collaboration for MongoDB Evidence

When MongoDB concepts are introduced, AI may help students:

* understand collection and document structure
* revise sample document shape
* explain MongoDB operations
* troubleshoot an operation that does not return the expected result
* compare relational and document representations
* identify whether an operation reveals a modeling issue

Students must still define the system question, expected result, model boundary, and final explanation.

## Week 8: Capstone Modeling Defense

AI assistance is allowed for the capstone, but it must be disclosed.

Students who choose a new database option from `Database_Concept_Options_v1.md` are expected to use especially clear AI disclosure because AI may reduce the time required to generate a first draft. The disclosure must show what AI produced, what the student verified, what changed, and what the student can defend independently.

---

# Course Prompting Pattern

When AI is allowed, students should use the course prompting pattern:

> Context -> Attempt -> Allowed Help -> Constraints -> Questions -> Output

For example:

> I am modeling an e-commerce order system. Here is my manual entity list and relationship draft. Please critique it for missing entities, unclear relationships, and assumptions. Do not create the final answer for me. Ask me questions if the business rule is unclear. Return suggestions in a table with issue, why it matters, and possible revision.

The prompt should make the student's manual attempt visible before AI gives feedback.

---

# AI Use Classifications in This Course

Students should identify the closest AI use classification when disclosure is required:

* **AI Assistance**: AI supported critique, explanation, review, questioning, or revision thinking.
* **AI Enabled / Collaboration**: AI helped create, revise, compare, or complete a targeted artifact after the student supplied manual framing.
* **AI Embedded**: AI was used inside a tool or system that directly supported the workflow.

AI development or full AI-generated system creation is outside the normal scope of this course.

---

# Restrictions in This Course

In this course, students may not:

* ask AI to complete an entire assignment without first doing the required manual work
* submit AI-generated models, diagrams, rules, sample documents, or MongoDB operations they cannot explain
* use AI to bypass entity, relationship, cardinality, normalization, or document-boundary decisions
* treat AI output as automatically correct
* hide meaningful AI use when disclosure is required
* use SQL for course assignments unless the instructor explicitly allows it
* submit a final capstone defense that depends on AI claims the student cannot verify or explain

---

# Disclosure Expectations in This Course

When AI is used, students may be required to complete `ai_assistance_notes.md` or `ai_assistance_disclosure.md`.

Students should be prepared to explain:

* what they were trying to do
* what AI tool or system they used
* which AI use classification fits the work
* what prompt or question they used
* what AI suggested or produced
* what they accepted, changed, or rejected
* how they verified the final model or evidence
* what decisions remained their own

If no AI was used on the capstone, students should state that clearly in the capstone disclosure file.

---

# Final Standard for This Course

In `10-152-123 Modern Data Modeling for Systems`, responsible AI use means:

* the student makes the core modeling decisions
* AI supports review, questioning, revision, and explanation
* the final model is understandable and defensible by the student
* AI use is disclosed honestly when required
* the student can explain why the final design choices fit the system being modeled

