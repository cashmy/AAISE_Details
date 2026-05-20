# Database Query and Design High-Level Course Plan v1

## Course

`10-152-120` - `Database Query and Design`

Credits: `3`  
Lecture/Lab: `36/36`  
Prerequisite: `n/a`

## Source Description

Learners develop database skills by working with data models, structured queries,
and relational design concepts. The course emphasizes organizing information,
defining relationships, and constructing valid queries to create, retrieve, and
manage data. Students practice using database tools to build tables, enforce keys,
join related data, and generate useful outputs. The course is designed to support
evolving platforms and workflows while strengthening the learner's ability to
reason about how data is structured, accessed, and maintained in modern software
systems.

## Planning Position

This course should function as the bridge sequence's practical relational
database foundation. It should teach students how structured data is organized,
queried, constrained, and maintained before they encounter broader modeling
choices in `10-152-123 Modern Data Modeling for Systems`.

The course should prioritize durable database reasoning over tool-specific
coverage:

```text
data entities -> tables
attributes    -> columns
records       -> rows
relationships -> keys and joins
questions     -> queries
integrity     -> constraints
```

Students should leave the course able to explain both what a query does and why
the database design makes that query possible.

## Delivery Frame

This is an 8-week, 3-credit course. In practice, the course will have more
contiguous weekly meeting time than a standard 17-week course.

The exact weekly format should remain flexible:

- 2 longer sessions per week, or
- 3 shorter sessions per week

The plan below is organized by week-level instructional movement rather than by
fixed meeting count.

## Relationship to Concurrent Courses

This course is expected to run during the first 8-week block of Semester 2,
alongside the beginning of:

- `10-152-121 Advanced Python Systems`
- `10-152-122 C# Application Development`

Its most important coordination point is with `10-152-122`:

- Early C# data work should use collections, files, JSON, and in-memory storage
  while this course builds relational foundations.
- By the end of this course, students should have enough database vocabulary and
  query fluency for C# to begin introducing database-backed data access.
- Course examples should avoid becoming application-development projects, but
  they should use realistic application-oriented data contexts.

This course is also the prerequisite base for `10-152-123`, so it should provide
the relational reference point that students will later compare against
non-relational and modern data-modeling patterns.

This course should also reactivate basic Big-O and growth-rate reasoning from
`10-152-119 Algorithmic Problem Solving`. The goal is not formal algorithm
analysis, but applied performance literacy: students should begin to understand
why scans, joins, sorting, grouping, indexes, and table design choices matter
more as data grows.

## High-Level Time Allocation

Suggested emphasis:

```text
25% relational database concepts and design vocabulary
35% SQL querying and result interpretation
20% table design, keys, relationships, and constraints
10% data modification and maintenance
10% reporting, outputs, debugging, tool workflow, and applied performance
    reasoning
```

## 8-Week Draft Structure

### Week 1 - Database Purpose, Tables, and Structured Data

Purpose: establish why databases exist and how relational structure differs from
files, spreadsheets, and in-memory collections.

Topics:

- What databases do in software systems
- Tables, rows, columns, records, and fields
- Data types and basic schema decisions
- Primary keys and identity
- Reading simple tables and result sets

Lab direction:

- Explore an existing sample database
- Identify entities, attributes, records, and keys
- Run basic `SELECT` queries
- Compare table data to CSV, spreadsheet, JSON, and application objects

### Week 2 - Basic SQL Queries

Purpose: build confidence retrieving and filtering data.

Topics:

- `SELECT`, `FROM`, `WHERE`, and `ORDER BY`
- Comparison operators and logical conditions
- Pattern matching and null handling
- Limiting and sorting results
- Query readability and formatting

Lab direction:

- Write queries against single tables
- Translate plain-language questions into SQL
- Debug common syntax and logic errors
- Explain query output in writing or discussion

### Week 3 - Relationships and Joins

Purpose: show how relational design supports connected information.

Topics:

- One-to-many and many-to-many relationships
- Foreign keys
- Inner joins and basic outer joins
- Join conditions and result shape
- Avoiding duplicate or misleading results

Lab direction:

- Query related tables
- Trace how keys connect records
- Build multi-table result sets
- Compare correct and incorrect join behavior

### Week 4 - Aggregation and Useful Outputs

Purpose: move from row retrieval to useful summaries.

Topics:

- Aggregate functions
- `GROUP BY` and `HAVING`
- Calculated fields
- Summary queries
- Reporting-oriented outputs

Lab direction:

- Answer business-style questions with grouped queries
- Build summary outputs from transactional-style data
- Interpret aggregate results
- Refine queries for clearer reporting

### Week 5 - Table Design and Normalization Foundations

Purpose: introduce design reasoning behind durable relational structures.

Topics:

- Entities and attributes
- Redundancy, update problems, and data integrity
- Basic normalization concepts
- Controlled denormalization as a justified exception, not a shortcut
- Primary and foreign key design
- Required versus optional data

Lab direction:

- Convert messy data into table structures
- Identify repeated groups and design problems
- Draft simple relational schemas
- Explain design choices using database vocabulary
- Compare one normalized design with one intentionally denormalized alternative
  and name the tradeoff

### Week 6 - Constraints, Data Modification, and Integrity

Purpose: show how databases protect meaning while data changes.

Topics:

- Constraints and validation at the database level
- `INSERT`, `UPDATE`, and `DELETE`
- Referential integrity
- Safe modification practices
- Basic transaction awareness

Lab direction:

- Add and modify records in controlled exercises
- Observe constraint violations
- Practice safe update/delete conditions
- Explain how database rules support application reliability

### Week 7 - Query Composition and Applied Scenarios

Purpose: combine design and querying skills in realistic data tasks.

Topics:

- Multi-step query thinking
- Subqueries or common table expressions at an introductory level
- Views or saved queries, if supported by the selected platform
- Query debugging and validation
- Matching query output to user or application needs
- Applying Big-O-style growth reasoning to scans, joins, sorting, grouping, and
  indexes at a conceptual level

Lab direction:

- Solve larger applied query problems
- Produce outputs for operational or reporting scenarios
- Review peer queries for correctness and readability
- Connect query choices to application requirements
- Explain why a query or design that works on a small dataset may become
  problematic as the data grows

### Week 8 - Integration and Transition to Modern Data Modeling

Purpose: consolidate relational database foundations and prepare students for
broader modeling choices.

Topics:

- Review tables, keys, joins, constraints, and query design
- Relational strengths and limitations
- When relational design rules may be intentionally bent for performance,
  reporting, or application needs
- How applications interact with databases
- How relational modeling prepares students for other storage patterns
- Transition into `10-152-123 Modern Data Modeling for Systems`

Lab direction:

- Complete an integrated database/query task
- Explain a small schema and its query capabilities
- Reflect on how data structure affects application code
- Identify which parts of the work would connect to C# data access

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Explain the purpose of relational databases in software systems.
- Interpret tables, records, fields, keys, relationships, and result sets.
- Write SQL queries to retrieve, filter, sort, join, and summarize data.
- Design simple relational table structures using keys and relationships.
- Apply basic growth-rate reasoning to explain why query and design choices
  affect performance as data volume increases.
- Apply constraints and basic modification statements to maintain data integrity.
- Debug and refine queries based on expected outputs.
- Explain how database structure affects application behavior and data access.

## Notes for Future Detailed Design

- Use realistic but bounded data contexts such as students/courses, inventory,
  orders, support tickets, appointments, media libraries, or simple operations.
- Avoid turning this into a full database administration course.
- Avoid deep optimization, indexing, stored procedures, advanced transactions,
  or platform-specific administration unless needed for local tooling.
- Keep performance analysis introductory and connected to prior Big-O exposure:
  enough to compare choices, not enough to become a query-optimization course.
- Coordinate examples with C# so later data-access labs can reuse familiar
  domains without duplicating this course's SQL instruction.
- Preserve flexibility around database platform. The plan can work with SQLite,
  SQL Server, PostgreSQL, MySQL/MariaDB, or an educational database environment.
