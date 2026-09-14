# Course 123 Technology Boundary

Course: `10-152-123 Modern Data Modeling for Systems`  
Version: `0.1`  
Purpose: Define what technical representations are allowed in Course 123 and what belongs in the following course

---

# Boundary Statement

Course 123 is a data modeling course, not a SQL course.

Students may learn and use relational modeling concepts such as:

- tables
- rows
- columns
- entities
- attributes
- keys
- relationships
- constraints
- normalization concepts
- ERD-style reasoning

Students should not be required to write SQL in this course.

Do not require:

- SQL queries
- SQL `CREATE TABLE` statements
- SQL joins
- SQL DDL
- SQL DML
- SQL comparison exercises
- SQL scripts as assignment evidence

SQL belongs in the following course:

```text
10-152-120 Database Query and Design
```

---

# Allowed Relational Language

Course 123 may use table-shaped thinking when useful:

| Allowed Concept | Course 123 Use |
| --- | --- |
| Table | A conceptual structure for grouping similar records |
| Row | One record or instance inside a table-shaped structure |
| Column | One attribute or field-like value in a table-shaped structure |
| Primary key | Candidate identifier for a record |
| Foreign key | Conceptual link between related records |
| Constraint | Plain-language rule the data should obey |

These should be used as modeling vocabulary, not SQL implementation tasks.

---

# Allowed MongoDB Language

MongoDB concepts are allowed because students will already have prior exposure to JSON, dictionaries, lists, arrays, and object-like structures from Python and Web Development Foundations.

Course 123 may use:

- MongoDB
- databases
- collections
- documents
- fields
- arrays
- embedded documents
- references
- BSON
- CRUD operations
- aggregation at an introductory level

MongoDB work should still support modeling judgment. It should not become a deep database administration course.

---

# Design Implication

Assignments should ask students to compare:

```text
relational/table-shaped representation vs document-shaped representation
```

They should not ask students to compare:

```text
SQL query vs MongoDB query
```

The appropriate Course 123 question is:

```text
Which representation better fits this system need, access pattern, reporting need,
performance concern, or AI-ready retrieval boundary?
```

---

# Instructor Check

Before approving a demo, assignment, or template, check:

- Does this require SQL syntax? If yes, move it to Course 120.
- Does this use table/row/column vocabulary only as modeling language? If yes, it is allowed.
- Does MongoDB work connect to representation, access pattern, or modeling tradeoff? If yes, it is allowed.
- Does the artifact preserve the distinction between relational concepts and SQL implementation? If yes, it fits Course 123.

