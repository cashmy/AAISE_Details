# Modern Data Modeling for Systems High-Level Course Plan v1

## Course

`10-152-123` - `Modern Data Modeling for Systems`

Credits: `3`  
Lecture/Lab: `36/36`  
Prerequisite: `10-152-120 Database Query and Design`

## Source Description

Learners examine modern approaches to organizing, modeling, and managing data for
software systems. The course emphasizes selecting appropriate data structures and
storage patterns, working across relational and non-relational models, and
understanding how data design affects reporting, integration, security, and
scalability. Students compare alternative approaches, transform and interpret
data, and practice reasoning about how information should be represented for
different technical and business needs. By the end of the course, learners are
able to explain and apply data-modeling choices in contemporary software
environments.

## Planning Position

This course should extend the relational foundations from `10-152-120` into a
broader systems-oriented view of data. Students should learn that data modeling is
not only about making tables; it is about choosing representations that fit the
application, reporting need, integration pattern, operational constraint, AI
retrieval pattern, and future change pressure.

The central course question should be:

```text
Given this information and this system need, how should the data be represented,
stored, exchanged, retrieved, bounded, and evolved?
```

This course should help students compare options rather than memorize one
preferred storage pattern.

The official description names security as one factor affected by data design,
but this plan should not treat security implementation as a major course thread.
In this course, the relevant emphasis is data quality, provenance, retrieval
boundaries, and exposure-aware modeling decisions that later cloud, deployment,
and DevOps coursework can implement more deeply.

Because this is part of a bridge into an AI Software Engineering degree, the
course should include an AI-ready data modeling thread. Students should learn how
data representation affects semantic search, retrieval-augmented generation,
vector indexes, metadata filtering, provenance, and model-facing boundaries
without turning the course into a machine-learning implementation course.

## Delivery Frame

This is an 8-week, 3-credit course. In practice, the course will have more
contiguous weekly meeting time than a standard 17-week course.

The exact weekly format should remain flexible:

- 2 longer sessions per week, or
- 3 shorter sessions per week

The plan below is organized by week-level instructional movement rather than by
fixed meeting count.

## Relationship to Concurrent Courses

This course is expected to run during the second 8-week block of Semester 2,
after `10-152-120` and alongside the later portion of:

- `10-152-121 Advanced Python Systems`
- `10-152-122 C# Application Development`

Its most important coordination point is with `10-152-122`:

- As C# moves into data access and ASP.NET Core APIs, this course gives students
  a richer vocabulary for models, DTOs, persistence choices, validation, and
  system boundaries.
- C# labs can demonstrate a small implementation of ideas that this course treats
  more broadly and conceptually.
- AI-ready retrieval concepts can give C# API work a later bridge into semantic
  search and model-grounded application patterns.
- This course should not become a second programming course, but it should use
  technical artifacts students can recognize: schemas, JSON documents, table
  diagrams, API payloads, logs, reports, vector-index sketches, and integration
  examples.

## High-Level Time Allocation

Suggested emphasis:

```text
25% modeling choices and representation tradeoffs
20% relational versus non-relational comparison
20% data transformation, exchange formats, and integration
15% reporting, analytics, and interpretation needs
10% data quality, provenance, and retrieval boundaries
10% scalability, evolution, and applied performance reasoning
```

## 8-Week Draft Structure

### Week 1 - From Relational Design to Data Modeling Choices

Purpose: reposition students from "how do I query a database?" to "how should
this system represent information?"

Topics:

- Review of relational tables, keys, joins, and constraints
- Data modeling as system design
- Conceptual, logical, and physical models
- Entities, attributes, relationships, events, and documents
- Choosing representations based on use case

Lab direction:

- Compare multiple representations of the same information
- Explain what each representation makes easier or harder
- Identify data needs from a short application or business scenario
- Draft a simple conceptual model

### Week 2 - Relational Models in Application Context

Purpose: deepen relational reasoning by connecting schema choices to application
and reporting needs.

Topics:

- Relational strengths and limitations
- Normalization and denormalization as tradeoffs
- Knowing when to intentionally bend data-modeling rules
- Transactional versus reporting-oriented structures
- Lookup tables, reference data, and status values
- How relational design affects application code
- Applying Big-O-style growth reasoning to modeling choices and access patterns

Lab direction:

- Revise a relational model for a changed requirement
- Compare normalized and denormalized alternatives
- Identify reporting impacts of schema choices
- Map tables to application-facing models
- Name the pressure, benefit, risk, and maintenance plan behind an intentional
  rule-bending choice

### Week 3 - Document, Key-Value, and Non-Relational Models

Purpose: introduce common non-relational patterns and why they exist.

Topics:

- Document-oriented data
- Key-value storage
- Wide-column and graph concepts at a survey level
- Embedded versus referenced data
- Query and update tradeoffs in non-relational structures
- Modeling choices for application access patterns and semantic retrieval

Lab direction:

- Model a relational scenario as JSON documents
- Compare embedded and referenced document designs
- Identify use cases where non-relational models may fit
- Discuss what is gained and lost compared with relational modeling

### Week 4 - Data Exchange, APIs, and System Boundaries

Purpose: connect data modeling to movement between systems and model-facing
contexts.

Topics:

- JSON, CSV, XML, and tabular exchange concepts
- API payloads and DTOs
- Internal models versus external contracts
- Validation and schema expectations
- Versioning and compatibility
- Data exposed to applications versus data exposed to AI retrieval workflows

Lab direction:

- Design request and response payloads for a small API
- Transform table-shaped data into JSON-shaped data
- Identify missing, invalid, or ambiguous data
- Discuss how C# ASP.NET Core endpoints might expose or protect model details
- Decide which fields belong in an API payload, a persistence model, and a
  model-facing retrieval context

### Week 5 - Transformation, Interpretation, and Data Quality

Purpose: teach students to reason about data changes, cleanup, and meaning.

Topics:

- Data transformation and mapping
- Derived fields and calculated values
- Missing, duplicated, inconsistent, and stale data
- Data quality checks
- Interpreting data in context

Lab direction:

- Clean or transform a small dataset
- Define rules for acceptable data
- Compare raw data with application-ready data
- Explain how data-quality problems affect software behavior

### Week 6 - Reporting, Analytics, and Read Models

Purpose: show that operational storage and reporting needs are related but not
identical.

Topics:

- Operational versus analytical data use
- Summary tables, views, extracts, and read models
- Metrics, dimensions, and aggregation
- Designing for questions people need answered
- Reporting tradeoffs and data lineage

Lab direction:

- Derive reporting needs from a scenario
- Design a read-oriented model or output structure
- Compare application data with reporting data
- Trace how a value in a report is produced

### Week 7 - AI-Ready Retrieval, Provenance, and System Boundaries

Purpose: introduce data-modeling choices that support semantic retrieval,
grounded AI responses, and responsible model-facing boundaries.

Topics:

- Embeddings as vector representations of text, records, or documents
- Vector indexes as similarity-search structures
- Relational plus vector hybrid models
- NoSQL/document plus vector retrieval patterns
- Chunking, metadata, source tracking, and provenance
- Retrieval boundaries: what should be searchable, summarizable, filtered, or
  excluded
- Scalability and applied performance reasoning for retrieval patterns

Lab direction:

- Sketch a relational plus vector model for a document or knowledge-retrieval
  scenario
- Compare keyword search, structured query, and vector similarity search
- Decide what metadata is needed to filter, explain, or limit retrieval
- Document tradeoffs behind chunking, denormalization, and retrieval boundaries

### Week 8 - Applied Modeling Decision and Transition Forward

Purpose: consolidate the course around justified modeling decisions.

Topics:

- Comparing modeling alternatives
- Selecting storage and exchange patterns
- Explaining tradeoffs to technical and nontechnical audiences
- Applying Big-O-style reasoning and access-pattern analysis to modeling choices
- Connecting data modeling to application development, cloud, deployment, and
  systems analysis
- Preparing for later integration work in the bridge sequence

Lab direction:

- Complete a bounded modeling case
- Present at least two possible representations and justify one
- Include implications for application code, reporting, AI-ready retrieval,
  boundaries, and change
- Reflect on how the model could be implemented in C#, Python, or a database

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Explain data modeling as a systems-design activity.
- Compare relational and non-relational representation patterns.
- Select data structures and storage patterns based on application, reporting,
  integration, AI-retrieval, and scalability needs.
- Transform and interpret data across tables, documents, files, and API payloads.
- Identify data-quality, provenance, and retrieval-boundary concerns in a
  proposed model.
- Justify modeling choices using clear tradeoff reasoning.
- Apply prior Big-O and growth-rate concepts to compare access patterns,
  denormalization choices, retrieval structures, and scale pressures.
- Connect data-modeling decisions to application development in C#, Python, and
  later cloud or deployment contexts.

## Notes for Future Detailed Design

- Keep the course tool-flexible. The goal is modeling judgment, not commitment to
  a single database product.
- Use artifacts students can see and discuss: ERDs, table sketches, JSON
  examples, API payloads, reports, data dictionaries, vector-index sketches, and
  transformation notes.
- Avoid making this a deep NoSQL implementation course.
- Avoid making this a business-intelligence course, though reporting and
  analytics should be visible.
- Avoid making this a security implementation course. Do not drift into IAM,
  encryption, cloud policy, compliance frameworks, or DevSecOps. Keep the focus
  on data quality, provenance, retrieval boundaries, and exposure-aware modeling.
- Avoid making this a machine-learning course. Embeddings and vector indexes
  should be introduced as data-retrieval structures and AI-integration concepts.
- Coordinate examples with C# so ASP.NET Core API labs can reinforce model,
  payload, validation, and persistence concepts.
- Favor comparison cases: one scenario, multiple plausible data representations,
  explicit tradeoffs.
