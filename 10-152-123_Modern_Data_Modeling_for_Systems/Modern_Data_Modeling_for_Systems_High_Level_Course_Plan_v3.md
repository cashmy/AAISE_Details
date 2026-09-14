# Modern Data Modeling for Systems High-Level Course Plan v3

## Course

`10-152-123` - `Modern Data Modeling for Systems`

Credits: `3`  
Lecture/Lab: `36/36`  
Spring sequence note: This course runs before `10-152-120 Database Query and Design` in the spring schedule.

## Delivery Context

**Schedule:** 8-week course, 2 hours × 4 days/week (M,T,Th,F 9:30-11:23) = 8 hours/week  
**Format:** Synchronous online with flexible lecture/lab split based on Reality Contact  
**Reading:** Assigned as homework/offline time  
**Labs:** Online lab time with early dismissal for students completing work early  
**Optional:** Paired programming opportunities for selected assignments

## Source Description

Learners examine modern approaches to organizing, modeling, and managing data for software systems. The course emphasizes selecting appropriate data structures and storage patterns, working across relational and non-relational models, and understanding how data design affects reporting, integration, security, and scalability. Students compare alternative approaches, transform and interpret data, and practice reasoning about how information should be represented for different technical and business needs. By the end of the course, learners are able to explain and apply data-modeling choices in contemporary software environments.

## Planning Position

This course should build relational modeling concepts before students take
`10-152-120 Database Query and Design`. Students should learn that data modeling is
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

## Textbook Integration

**Primary Text:** Data Modeling: A Beginner's Guide by Andy Oppel  
**Reading Strategy:** Curated selection emphasizing conceptual modeling, ERD design, and basic principles  
**Supplemental Text:** MongoDB Essentials by The MongoDB Team (ISBN: 978-1806706099)  
**MongoDB Teaching Strategy:** Collective teaching approach to allow cognitive absorption of NoSQL paradigm shift  
**Bonus Content:** API and integration patterns offered as offline, student-paced optional material

## Technology Boundary

Course 123 may introduce relational modeling vocabulary such as tables, rows, columns, keys, relationships, and constraints. It should not require SQL syntax, SQL queries, SQL DDL, SQL joins, or SQL scripts. SQL belongs in `10-152-120 Database Query and Design`, which follows this course in the spring sequence.

MongoDB collections, documents, fields, arrays, embedded documents, references, BSON, CRUD, and introductory aggregation are appropriate because students will already have prior experience with JSON, dictionaries, lists, and arrays in Python and Web Development Foundations.

## RBA Process Integration

**Instructor-Level Awareness:** Temporal data, analytical patterns, and enterprise boundaries will be discovered through the RBA process rather than separate theoretical modules. Students will learn to identify these needs through iterative Sky-Bounce and Reality Contact during their modeling work.

## Relationship to Concurrent Courses

This course runs during the first 8-week block of Semester 2, alongside:

- `10-152-121 Advanced Python Systems` (same time block, afternoon slot)

Key coordination with concurrent courses:

- ERD skills support system design in both Python and C# contexts
- Data modeling concepts prepare students for later database querying and inform API design in C# course
- Performance reasoning applies across all concurrent technical work

## 8-Week Structure with Textbook Alignment

### Week 1 - Data Modeling Foundations and Conceptual Thinking

**Textbook Reading:** Chapter 1: Introduction to Data Modeling  
**Focus:** Reposition from database querying to systems-level data thinking

**Topics:**

- Data-centric design principles
- Anatomy of a data model
- Layers of data abstraction (conceptual, logical, physical)
- Types of data models
- Importance of data modeling for system design
- Measures of a good data model

**Lab Direction:**

- Compare multiple representations of the same information
- Explain what each representation makes easier or harder
- Identify data needs from a short application scenario
- Draft a simple conceptual model
- **Optional paired programming:** Collaborative conceptual modeling exercise

**RBA Process Awareness:** Students begin practicing "big picture" thinking before technical details

---

### Week 2 - Relational Model Components and Data-Process Connection

**Textbook Reading:** Chapter 2: Relational Model Components, Chapter 3: Data and Process Modeling  
**Focus:** Core relational concepts and their relationship to system processes

**Topics:**

- Core relational concepts (entities, attributes, relationships)
- Keys and relationship types
- Basic integrity constraints
- Relationship between data and process modeling
- How data modeling supports system design

**Lab Direction:**

- Analyze a simple system scenario
- Identify entities, attributes, and relationships
- Map data structures to process requirements
- Begin thinking about system boundaries

**RBA Process Awareness:** Students practice seeing relationships between data structures and system processes

---

### Week 3 - ERD Design and Visualization (Strong Treatment)

**Textbook Reading:** Chapter 4: ERD Design and Practice  
**Focus:** Practical ERD creation using draw.io or similar tool

**Topics:**

- Entity-relationship diagram fundamentals
- ERD notation and conventions
- Creating effective ERDs
- Translating conceptual models to visual diagrams
- ERD as communication tool for technical and non-technical stakeholders

**Lab Direction:**

- **Major ERD Assignment:** Create detailed ERD for assigned scenario using draw.io
- Apply proper notation and conventions
- Ensure clarity and readability
- Present design rationale
- **Optional paired programming:** Collaborative ERD design and review

**Assessment Alignment:** T2 (ERD Design and Visualization) - Primary focus

---

### Week 4 - Conceptual Modeling Process

**Textbook Reading:** Chapter 5: Conceptual Data Modeling  
**Focus:** The systematic process of conceptual modeling

**Topics:**

- The conceptual modeling process
- Preparation and solution design
- What differentiates conceptual from logical modeling
- Creating the model
- Generic models and patterns
- Roles vs. subtypes
- Dealing with hierarchies, networks, and linked lists
- Bottom-up vs. top-down modeling
- Subject areas
- Evaluating the model and what makes a good conceptual model

**Lab Direction:**

- Apply conceptual modeling process to complex scenario
- Develop generic models and patterns
- Handle hierarchies and network relationships
- Evaluate and refine conceptual models

**RBA Process Awareness:** Students practice systematic approach to complex modeling problems

---

### Week 5 - Normalization Reference and Business Rules Summary

**Textbook Reading:** Chapter 6: Normalization (Reference), Chapter 9: Business Rules (Summary)  
**Focus:** Basic normalization awareness and business rules placement

**Topics:**

- Basic normalization concepts at awareness level
- The need for normalization (insert, delete, update anomalies)
- First through Third Normal Forms overview
- Denormalization for performance efficiency
- **Critical human responsibility:** AI does not automatically consider denormalization for operational efficiency
- When and why to break normalization rules
- Business rules impact on database design
- Greenfield vs. legacy application considerations
- Business rules placement: backend vs. database design

**Lab Direction:**

- Analyze a schema for normalization issues
- Identify denormalization opportunities for performance
- Determine appropriate business rules placement for given scenario
- Document performance tradeoff decisions

**RBA Process Awareness:** Students practice human governor role for performance optimization

---

### Week 6 - MongoDB Fundamentals and Data Modeling

**Textbook Reading:** MongoDB Essentials Chapters 1-3 (Architecture, Getting Started, Data Modeling)  
**Focus:** MongoDB paradigm shift and conceptual foundations

**Topics:**

- MongoDB architecture (mongod, mongos, replica sets, sharding)
- Mapping MongoDB components to relational database structures
- Client libraries and interaction (pymongo)
- Installation and local deployment
- Schema design and data modeling in MongoDB
- Embedding vs. referencing strategies
- One-to-one, one-to-many, many-to-many relationships in MongoDB
- Optimization strategies and denormalization in NoSQL context

**Lab Direction:**

- Install and configure MongoDB environment
- Create first database and collection
- Model a relational scenario as MongoDB documents
- Compare embedded and referenced document designs
- Identify use cases where NoSQL models may fit
- Discuss what is gained and lost compared with relational modeling
- **Cognitive absorption time:** Allow students to process NoSQL paradigm shift

**Assessment Alignment:** T3 (Relational vs Non-Relational Data Structures) - Primary focus

---

### Week 7 - MongoDB Operations and Performance

**Textbook Reading:** MongoDB Essentials Chapters 4-6 (CRUD Operations, Aggregation, Performance Strategies)  
**Focus:** Practical MongoDB operations and performance understanding

**Topics:**

- Create, Read, Update, Delete operations in MongoDB
- Aggregation framework for complex data analysis
- Aggregation stages ($match, $group, $sort, $project)
- Operators ($gt, $lt, $eq, $ne) and expressions ($sum, $avg, $push, $addToSet)
- Conditionals ($cond, $ifNull, $switch) and path expressions
- Array operators ($lookup, $unwind)
- Performance strategies and tools (indexes, .explain(), profiling, stats())
- Query performance and scaling considerations

**Lab Direction:**

- Practice CRUD operations on MongoDB collections
- Build aggregation pipelines for data analysis
- Apply performance optimization techniques
- Compare MongoDB query patterns with relational/table-shaped access needs, not SQL syntax
- Analyze performance using MongoDB tools

**Assessment Alignment:** T4 (Data Transformation and Integration) - Secondary focus through aggregation exercises

---

### Week 8 - AI-Ready Data Concepts and Applied Modeling Decisions

**Textbook Reading:** MongoDB Essentials Chapter 7 (Intelligent Applications with MongoDB) + Supplemental AI content  
**Focus:** AI-ready data modeling and comprehensive applied decisions

**Topics:**

- MongoDB tools for AI-based applications (Atlas Search, Atlas Vector Search)
- Lexical search, semantic search, and RAG (Retrieval-Augmented Generation)
- Embeddings as vector representations of text, records, or documents
- Vector indexes as similarity-search structures
- Relational plus vector hybrid models
- Chunking, metadata, source tracking, and provenance
- Retrieval boundaries: what should be searchable, summarizable, filtered, or excluded
- Performance and scalability reasoning for AI-ready patterns
- Comparing modeling alternatives across relational and NoSQL approaches
- Selecting storage and exchange patterns
- Explaining tradeoffs to technical and nontechnical audiences

**Lab Direction:**

- **Capstone Modeling Project:** Complete a bounded modeling case
- Present at least two possible representations and justify one
- Include implications for application code, reporting, AI-ready retrieval, boundaries, and change
- Consider both relational and NoSQL approaches in analysis
- Reflect on how the model could be implemented in C#, Python, or a database
- **Optional paired programming:** Collaborative capstone project

**Assessment Alignment:** T5 (Performance and Scalability Reasoning), T6 (AI-Ready Data Concepts) - Primary focus

**Bonus Content (Optional Offline):**

- API and integration patterns (JSON, CSV, XML, API payloads, DTOs)
- Data exchange formats and system boundaries
- Students can access on their own schedule for additional depth

---

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Explain data modeling as a systems-design activity.
- Create ERDs using standard notation to visualize data structures.
- Compare relational and non-relational representation patterns.
- Select data structures and storage patterns based on application, reporting, integration, AI-retrieval, and scalability needs.
- Transform and interpret data across tables, documents, files, and API payloads.
- Identify data-quality, provenance, and retrieval-boundary concerns in a proposed model.
- Apply denormalization strategies for performance efficiency (human governor role).
- Justify modeling choices using clear tradeoff reasoning.
- Connect data-modeling decisions to application development in C#, Python, and later cloud or deployment contexts.

## Notes for Implementation

**Textbook Integration:**

- Reading assignments map directly to weekly topics
- MongoDB Essentials taught collectively (Chapters 1-3 Week 6, Chapters 4-6 Week 7) to allow cognitive absorption of NoSQL paradigm shift
- MongoDB Chapter 7 supports Week 8 AI-ready concepts
- Emphasis on conceptual modeling and ERD skills (Oppel Chapters 1-5)
- Reference treatment for normalization (Oppel Chapter 6)
- Summary treatment for business rules (Oppel Chapter 9)
- Bonus content (API/integration patterns) offered as optional offline material

**RBA Process Discovery:**

- Temporal data, analytical patterns, enterprise boundaries discovered through iterative modeling work
- Instructor guides Sky-Bounce process during lab work
- Students learn to identify needs through Reality Contact rather than separate modules

**Assessment Alignment:**

- Week 3: T2 (ERD Design) - Major ERD assignment
- Week 6: T3 (Non-Relational Comparison) - MongoDB fundamentals and modeling
- Week 7: T4 (Data Transformation) - MongoDB operations and aggregation (secondary focus)
- Week 8: T5/T6 (Performance/AI-Ready) - Capstone project with AI-ready concepts

**Optional Paired Programming:**

- Week 1: Collaborative conceptual modeling
- Week 3: Collaborative ERD design and review
- Week 8: Collaborative capstone project

**Flexible Lecture/Lab Split:**

- Lecture length determined by student comprehension (Reality Contact)
- Remaining time allocated to lab work
- Early dismissal for students completing labs early
- Maintains flexibility while ensuring core content delivery
