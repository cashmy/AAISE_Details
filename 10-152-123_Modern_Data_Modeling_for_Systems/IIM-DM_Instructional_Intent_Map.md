# Instructional Intent Map - Modern Data Modeling for Systems

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.2`  
Purpose: Instructor-facing scaffold map for lecture, demo, lab, assignment, and rubric design

---

# Delivery Constraint

This course runs for eight weeks, four class meetings per week:

```text
Monday, Tuesday, Thursday, Friday
9:30-11:23
```

The instructional design should assume:

- 2 lectures per week
- 2 labs per week
- Monday and Thursday as the primary lecture anchors
- Tuesday and Friday as the primary lab/application anchors
- assignment work that visibly connects to the two weekly lecture/lab pairs

Most weeks should support two assignment targets, one for each lecture/lab pair.

When a week uses a single assignment, that assignment must be iterative:

```text
Lecture 1 -> Lab 1 checkpoint -> Lecture 2 refinement lens -> Lab 2 final submission
```

For Course 123, the intended single-assignment iterative weeks are Weeks 1, 2, and 4.

---

# Design Premise

This course should not teach data modeling as a list of database topics. It should teach students how to move from an unclear system need toward a defensible data representation.

Course 123 may use relational modeling vocabulary such as tables, rows, columns, keys, relationships, and constraints. It should not require SQL syntax, SQL queries, SQL DDL, or SQL scripts. SQL belongs in `10-152-120 Database Query and Design`, which follows this course in the spring sequence.

MongoDB collections, documents, fields, arrays, embedded documents, references, BSON, CRUD, and introductory aggregation are allowed because they connect to prior student experience with JSON, dictionaries, lists, and arrays.

The repeated instructional movement is:

```text
System intent -> information shape -> representation choice -> evidence -> tradeoff defense
```

The course uses SKY, CORE, and BASE as instructional layers:

| Layer | Course Meaning | Student Evidence |
| --- | --- | --- |
| SKY | Purpose, audience, system need, business question, success condition | Scenario framing, modeling intent, decision questions |
| CORE | Entities, relationships, rules, access patterns, representation alternatives | Conceptual models, ERDs, comparison tables, mapping notes |
| BASE | Tool operation, syntax, implementation detail, query or document mechanics | Draw.io diagrams, schemas, MongoDB documents, CRUD or aggregation examples |

The course should avoid two common failures:

- Staying too vague at SKY level, where students can repeat broad ideas without producing model evidence.
- Dropping too quickly to BASE level, where students complete tool steps without understanding the modeling decision.

CORE is the hinge of the course.

AI use should be taught as a scaffolded modeling support, not as a shortcut around modeling judgment.

Course 123 uses the following AI prompt pattern:

```text
Context -> Attempt -> Allowed Help -> Constraints -> Questions -> Output
```

Course 123 also uses the following practical AI use classifications:

| Classification | Course Meaning | Typical Use in 123 |
| --- | --- | --- |
| AI Assistance | AI supports critique, explanation, review, questioning, or comparison | Weeks 1-8 after a manual attempt |
| AI Enabled / Collaboration | AI helps create, revise, compare, or complete a targeted part after student framing | Mainly Weeks 6-8 for JSON cleanup, MongoDB operation help, aggregation help, and capstone drafting support |
| AI Embedded | AI operates inside a tool or workflow | Awareness and disclosure only; not a required performance target |
| AI Creation/Development | Building LLMs, RAG/CAG systems, model-training workflows, or AI products | Out of scope for Course 123 |

Students should document AI use through:

- the classification of AI use
- the manual attempt completed first
- the prompt structure used
- suggestions accepted, rejected, or modified
- what the student verified
- the final responsibility statement

---

# Course Arc

| Phase | Weeks | Instructional Purpose | Student Shift |
| --- | --- | --- | --- |
| Phase 1 | 1-2 | Establish data modeling as systems thinking and convert scenario language into relational structure | From "database tables" to "information shape" |
| Phase 2 | 3-4 | Make models visible, reviewable, and improvable through ERDs and conceptual modeling process | From "I listed entities" to "I can communicate and refine a model" |
| Phase 3 | 5 | Stress the model with rules, anomalies, normalization, and performance exceptions | From "correct structure" to "responsible tradeoff" |
| Phase 4 | 6-7 | Re-represent the same information as documents and operate on it in MongoDB | From "one right model" to "model depends on access pattern" |
| Phase 5 | 8 | Synthesize relational, document, performance, and AI-ready concerns into a final modeling defense | From "I built a model" to "I can defend a modeling decision" |

---

# Week 1 - Data Modeling Foundations

## Intent

Students should experience data modeling as the act of discovering what information a system must remember, relate, protect, retrieve, and explain.

## SKY

- What is the system trying to support?
- Who needs the information?
- What decisions or actions depend on the information?
- What would count as a useful model at this early stage?

## CORE

- Identify candidate entities without finalizing them too early.
- Separate "thing," "event," "description," and "relationship."
- Draft a first conceptual model as a thinking artifact, not a final answer.
- Record open modeling questions.

## BASE

- Plain text entity list
- Simple relationship statements
- Optional rough sketch or draw.io draft

## Demo Intent

The instructor demo should start with an intentionally incomplete scenario and model aloud how to extract entities, relationships, and questions.

The demo should stop before it becomes a polished ERD.

## Student Evidence

- Scenario intent statement
- Candidate entity list with purposes
- Relationship statements
- At least three open modeling questions
- Brief explanation of what the model currently makes easier or harder

## AI Boundary

Manual First / AI Assistance. Students may ask AI to critique missing entities or ambiguous relationships only after they produce an initial model.

---

# Week 2 - Relational Structure and Data-Process Connection

## Intent

Students should convert conceptual thinking into relational structure while preserving the link to system behavior.

## SKY

- What processes does the system need to support?
- What must be created, updated, tracked, or reported?
- Which relationships are central to the system's purpose?

## CORE

- Identify entities, attributes, keys, and relationship types.
- Distinguish data about a thing from data about an event or transaction.
- Connect process steps to the data they require.
- Identify integrity constraints in plain language before notation.

## BASE

- Draft relational structure table
- Key and relationship notes
- Early cardinality labels

## Demo Intent

The instructor demo should take the Week 1 demo model and ask: "What would the system need to store for this process to work?"

The point is not complete relational design. The point is connecting model shape to process need.

## Student Evidence

- Updated entity/attribute table
- Primary key and foreign key candidates
- Relationship type notes
- Process-to-data mapping for two or three system actions
- Integrity constraint notes in plain English

## AI Boundary

AI Assistance after manual attempt. AI may be used to ask "what relationship or attribute might I be missing?" Students must accept, reject, or modify suggestions with reasons.

---

# Week 3 - ERD Design and Visualization

## Intent

Students should learn that a model becomes more useful when it can be inspected, challenged, and communicated visually.

## SKY

- Who needs to understand this model?
- What misunderstanding would the ERD help prevent?
- What part of the model should be visually obvious?

## CORE

- Translate entity/relationship notes into ERD notation.
- Make cardinality and optionality visible.
- Use layout to communicate structure.
- Treat the ERD as a review artifact, not decoration.

## BASE

- draw.io or equivalent ERD tool
- approved alternatives such as Lucidchart, Miro, FigJam, ERDPlus, Visual Paradigm, Creately, or Mermaid
- Entities, attributes, relationship lines, cardinality markers
- Exported image or submitted diagram file

## Demo Intent

The instructor demo should show how the same model can be expressed in more than one diagramming tool, then settle on draw.io as the supported lab tool. The demo should show one rough ERD and one improved ERD for the same concept, emphasizing readability, relationship clarity, and review value.

## Student Evidence

- ERD for selected scenario
- Short design rationale
- List of model assumptions
- Notation and readability checklist
- Tool-use evidence or exported diagram file

## AI Boundary

AI Assistance. AI may critique the written model or review exported diagram descriptions, but students remain responsible for the visual model and notation.

---

# Week 4 - Conceptual Modeling Process and Refinement

## Intent

Students should learn that models improve through systematic refinement, not by adding complexity randomly.

## SKY

- What changed in our understanding of the system?
- Which modeling questions are now clearer?
- What new ambiguity has appeared?

## CORE

- Revisit the model using a repeatable refinement process.
- Recognize roles, subtypes, hierarchies, categories, and weak areas.
- Distinguish useful complexity from premature complexity.
- Evaluate model quality against purpose.

## BASE

- Revised conceptual model
- Revised ERD or marked-up ERD
- Change log

## Demo Intent

The instructor demo should revise the Week 3 demo model in public. The key teaching move is explaining why a change is made, not merely showing the changed diagram.

## Student Evidence

- Revised model
- Change log with reasons
- Model quality self-assessment
- Remaining open questions

## AI Boundary

AI Assistance critique is appropriate. AI may identify possible missing cases, but students must decide whether the case belongs in this course-level model.

---

# Week 5 - Normalization, Business Rules, and Performance Exceptions

## Intent

Students should understand that a "clean" model can still fail if it ignores anomalies, rules, access patterns, or performance needs.

## SKY

- What could go wrong if this data is stored poorly?
- Which rules belong in the model, database, application, or process?
- When might duplication be responsible rather than careless?

## CORE

- Identify basic update, insert, and delete anomaly risks.
- Recognize normalization as a reasoning tool, not a ritual.
- Identify business rules and plausible enforcement locations.
- Explain denormalization as a deliberate tradeoff.

## BASE

- Normalization issue notes
- Rule placement table
- Performance/access pattern notes

## Demo Intent

The instructor demo should show a model that is understandable but risky, then walk through one normalization improvement and one responsible denormalization decision.

## Student Evidence

- Anomaly analysis
- Rule placement table
- One normalization recommendation
- One performance or denormalization tradeoff note

## AI Boundary

AI Assistance. Students may ask AI to challenge their rule placement or identify possible anomalies, but they must document the final reasoning themselves.

---

# Week 6 - MongoDB Fundamentals and Document Modeling

## Intent

Students should experience NoSQL as a different representation strategy, not as "tables but in JSON."

## SKY

- What access patterns does the document model support?
- What information tends to be retrieved together?
- What changes when the representation is document-shaped?

## CORE

- Compare embedding and referencing.
- Map relational entities to document boundaries.
- Identify what is gained and lost in the document model.
- Preserve the idea that model choice follows system need.

## BASE

- Local MongoDB setup or guided environment
- Database and collection creation
- Example documents

## Demo Intent

The instructor demo should convert part of the ongoing demo model into documents and explicitly compare two possible document boundaries.

## Student Evidence

- Document model draft
- Embedded vs referenced comparison
- Sample documents
- Relational vs document tradeoff notes

## AI Boundary

AI Assistance or limited AI Enabled / Collaboration. AI may help generate or clean up sample JSON only after students define document boundaries and explain why those boundaries fit the access pattern.

---

# Week 7 - MongoDB Operations, Aggregation, and Performance

## Intent

Students should connect data shape to retrieval, transformation, and performance behavior.

## SKY

- What questions should the system answer?
- What reports, summaries, or lookups matter?
- What would make retrieval efficient or difficult?

## CORE

- Translate system questions into query patterns.
- Use CRUD operations as evidence that the model can support real behavior.
- Use aggregation as a transformation and interpretation pattern.
- Identify simple indexing or performance considerations.

## BASE

- CRUD examples
- Query examples
- Aggregation pipeline
- Optional explain/index observation

## Demo Intent

The instructor demo should show how one document structure makes a query easy and another makes it awkward. The goal is to tie operations back to modeling decisions.

## Student Evidence

- CRUD operation examples
- At least one query tied to a system question
- At least one aggregation pipeline or guided aggregation exercise
- Note explaining how document shape affected retrieval

## AI Boundary

AI Enabled / Collaboration is acceptable for MongoDB operation or aggregation help only after students state the system question and expected result. Students must test and explain the operation.

---

# Week 8 - Capstone Modeling Defense and AI Accountability

## Intent

Students should synthesize the course by assembling and defending a coherent database model using appropriate evidence from the course.

## SKY

- What is the system supposed to support?
- What evidence best supports the design claim?
- What does the design not handle yet?
- What AI assistance was used, and what did the student personally verify?

## CORE

- Select a capstone pathway.
- Assemble a complete evidence packet.
- Include system scope, visual model, business rules, relational evidence, and representation consideration.
- Include NoSQL/document evidence when applicable.
- Justify the selected approach using evidence and stated limitations.
- Disclose AI assistance using the course classification and prompt structure.

## BASE

- Final ERD or revised diagram
- Business rules file
- Relational model evidence
- Document model evidence when applicable
- Final written defense
- AI assistance disclosure

## Demo Intent

The instructor demo should be a compact capstone defense, not a new full lecture. It should model how to assemble evidence, make a claim, acknowledge limitations, and disclose AI assistance.

## Student Evidence

- Final modeling packet
- Relational/document comparison
- System questions the database should answer
- Final explanation defense
- AI assistance disclosure

## AI Boundary

AI Assistance or AI Enabled / Collaboration by permission of the capstone pathway. AI may critique, generate alternatives, help with Pathway 2 compressed design, or help polish explanations, but students must disclose use, validate claims, and defend the final model.

---

# Repeated Evidence Spine

Every major assignment should produce some form of the following evidence:

1. System intent
2. Model artifact
3. Decision rationale
4. Evidence of fit
5. What the design fits and what it does not handle yet
6. AI-use statement when applicable
7. AI classification and prompt-structure evidence when AI was used

This repeated spine is more important than topic coverage density.

---

# Suggested Assignment Arc

| Week | Assignment Role | Output |
| --- | --- | --- |
| 1 | Start the model | Conceptual model and open questions |
| 2 | Structure the model | Entities, attributes, keys, relationships, process mapping |
| 3 | Make it visible | ERD and model assumptions |
| 4 | Refine it | Revised model, change log, quality assessment |
| 5 | Stress it | Normalization/rule/performance analysis |
| 6 | Re-represent it | MongoDB document model comparison |
| 7 | Operate on it | Queries, CRUD, aggregation, retrieval notes |
| 8 | Defend it | Capstone modeling defense and AI assistance disclosure |

---

# Instructor Design Check

Before creating a lecture, demo, lab, or assignment, ask:

- What layer is this primarily teaching: SKY, CORE, or BASE?
- What CORE artifact bridges the concept to student evidence?
- What should students be able to do after this that they could not do before?
- What visible evidence will show that the student made a modeling decision?
- What misconception is this activity designed to prevent?
- Is the demo close enough to guide transfer but different enough to prevent copying?
