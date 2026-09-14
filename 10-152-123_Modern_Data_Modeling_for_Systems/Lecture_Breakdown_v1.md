# Lecture Breakdown - Modern Data Modeling for Systems
## Course 123 - Lecture Structure with 2 Lectures per Week

---

## Course Technology Boundary

- Relational concepts such as tables, rows, columns, keys, relationships, and constraints are appropriate.
- SQL syntax, SQL queries, SQL DDL, SQL joins, and SQL scripts are not part of this course.
- SQL is introduced in the following `10-152-120 Database Query and Design` course.
- MongoDB collections, documents, fields, arrays, embedded documents, references, BSON, CRUD, and introductory aggregation are appropriate because students have prior experience with JSON, dictionaries, lists, and arrays.

---

## Week 1 - Data Modeling Foundations

**Lecture 1:** Data-Centric Design Principles
- What is data modeling as systems design (not just table creation)
- Layers of abstraction (conceptual, logical, physical)
- Anatomy of a data model
- Repositioning from database querying to systems thinking

**Lecture 2:** Model Quality and Evaluation
- Types of data models
- Measures of a good data model
- Introduction to conceptual thinking before technical details
- RBA Process: Intent and SKY-level thinking for data systems

---

## Week 2 - Relational Model Components

**Lecture 1:** Core Relational Concepts
- Entities, attributes, relationships
- Keys and relationship types
- Basic integrity constraints
- Relational model as a foundation

**Lecture 2:** Data-Process Connection
- Relationship between data and process modeling
- How data modeling supports system design
- Mapping data structures to process requirements
- System boundaries and data-process relationships

---

## Week 3 - ERD Design and Visualization (Practical Focus)

**Lecture 1:** ERD Fundamentals and Notation
- Entity-relationship diagram fundamentals
- ERD notation and conventions
- draw.io tool introduction
- brief exposure to alternate ERD tools and sample outputs
- Translating conceptual models to visual diagrams

**Lecture 2:** draw.io Training and Practice
- draw.io installation and setup
- Tool interface navigation
- Hands-on practice with basic ERD creation
- Common draw.io patterns and shortcuts
- Major ERD assignment completion and review
- acceptable alternatives: Lucidchart, Miro, FigJam, ERDPlus, Visual Paradigm, Creately, Mermaid, or another instructor-approved ERD-capable tool

---

## Week 4 - Conceptual Modeling Process

**Lecture 1:** The Modeling Process
- Preparation and solution design
- Conceptual vs. logical modeling differences
- Creating the model step-by-step
- Bottom-up vs. top-down approaches

**Lecture 2:** Advanced Conceptual Patterns
- Generic models and patterns
- Roles vs. subtypes
- Hierarchies, networks, and linked lists
- Subject areas and model evaluation
- ERD as communication tool (integrated from Week 3)

---

## Week 5 - Normalization and Business Rules

**Lecture 1:** Normalization Awareness
- Basic normalization concepts (1NF-3NF overview)
- Insert, delete, update anomalies
- When normalization is needed
- Reference-level treatment (not deep implementation)

**Lecture 2:** Denormalization and Business Rules
- Denormalization for performance efficiency
- **Critical human governor role** for performance
- Business rules impact on database design
- Greenfield vs. legacy business rules placement

---

## Week 6 - MongoDB Fundamentals

**Lecture 1:** MongoDB Architecture and Setup
- MongoDB architecture (mongod, mongos, replica sets, sharding)
- Mapping MongoDB components to relational structures
- Installation and local deployment
- First database and collection creation

**Lecture 2:** Document Data Modeling
- Schema design in MongoDB
- Embedding vs. referencing strategies
- Relationship patterns in NoSQL
- NoSQL paradigm shift absorption time

---

## Week 7 - MongoDB Operations

**Lecture 1:** CRUD Operations
- Create, Read, Update, Delete in MongoDB
- Basic query patterns
- Comparison with relational/table-shaped access needs, not SQL syntax
- Practical operation exercises

**Lecture 2:** Aggregation and Performance
- Aggregation framework basics
- Performance tools (indexes, .explain(), profiling)
- Query performance considerations
- Practical aggregation pipelines

---

## Week 8 - AI-Ready Data and Capstone (Restructured)

**Lecture 1:** Non-Essential/Optional
- Available if additional time proves necessary for capstone work
- Buffer time for unexpected challenges
- AI-ready concepts covered offline if not used

**Lecture 2:** Offline or Integrated Content
- AI-ready data concepts (MongoDB Atlas Search, Vector Search, RAG)
- Performance reasoning for AI-ready patterns
- **OR:** Integrated into Week 6-7 lectures as bonus content
- Primary focus: capstone lab time and presentation preparation

---

## Database Concepts for Assignments

### Assignment Concepts (Student Selection)
1. **Student/Course/Schedule Tracker**
   - Complex relationships, many-to-many
   - Temporal data (schedules, semesters)
   - Multiple entities and constraints

2. **Customer/Orders/Invoicing**
   - Business process modeling
   - Transactional relationships
   - Payment and status tracking

3. **Books/Library**
   - Cataloging system
   - Author/title relationships
   - Checkout/inventory management

4. **Music Collection**
   - Hierarchical patterns (genres, artists, albums)
   - Collection management
   - Metadata and categorization

### Demo Concept (Instructor Use Only)
**E-commerce with Reviews/Ratings**
- Shows relational structure with customer/product/order relationships
- Extends to AI-ready search concepts (product recommendations, semantic search)
- Complex enough for demonstration purposes
- Not used in student assignments to avoid template copying

### Capstone Options
- Students choose from remaining concepts not used in their assignments
- OR: Students propose original scenario with instructor approval
- Requires relational and NoSQL comparison
- Must include AI-ready considerations

---

## Lecture Structure Notes

**Week 3 Practical Focus:**
- Emphasis on draw.io tool training and hands-on practice
- Communication concepts moved to Week 4 integration
- BASE-level tool competency before SKY-level communication theory

**Week 8 Capstone Priority:**
- Lecture 1: Optional buffer time
- Lecture 2: Moved to offline or integrated earlier
- Primary lab time dedicated to capstone work and presentation

**Assignment Concept Strategy:**
- 4 concepts available for assignment selection
- 1 concept reserved for instructor demos
- Capstone allows concept flexibility
- Prevents template copying while providing structured options
