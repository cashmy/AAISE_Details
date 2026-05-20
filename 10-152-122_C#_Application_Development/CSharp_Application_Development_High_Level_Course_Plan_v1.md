# C# Application Development High-Level Course Plan v1

## Course

`10-152-122` - `C# Application Development`

Credits: `3`  
Lecture/Lab: `36/36`  
Prerequisite: `10-152-117 Python Programming Foundations`

## Source Description

Learners develop application-development skills using C# and related web application
concepts to design and implement interactive software solutions. The course
emphasizes core programming structures, object-oriented design, event-driven
behavior, collections, file handling, exception management, and data access, while
also introducing web-oriented application patterns. Students practice debugging,
extending, and refining applications in ways that can adapt to changing tools and
frameworks. By the end of the course, learners are able to build, explain, and
improve applications that integrate both software logic and user-facing
functionality.

## Planning Position

This course should be treated as a C# and .NET application-development course
with a focused ASP.NET Core finish, not as a legacy ASP.NET course.

The conceptual relationship should be introduced early and revisited throughout:

```text
C#           = programming language
.NET         = runtime, libraries, tooling, project system, package ecosystem
ASP.NET Core = modern .NET framework for web applications and web APIs
```

Students entering from Python can map this relationship approximately as:

```text
Python : Django/Flask :: C# : ASP.NET Core
```

The analogy is useful but imperfect. C# and .NET are more tightly integrated than
Python and its common web frameworks. That tighter integration should become part
of the course's transfer-learning value.

## Legacy ASP.NET Distinction

The opening course orientation should explicitly distinguish older ASP.NET
contexts from modern ASP.NET Core.

Important distinctions:

- Classic ASP.NET Web Forms was page/event oriented and tied to older .NET
  Framework-era development patterns.
- Older ASP.NET MVC remains important historically and may appear in legacy
  systems, but it should not define this course.
- ASP.NET Core is the current cross-platform, modern .NET web framework.
- For this bridge course, ASP.NET Core should be used primarily to teach
  web-oriented application patterns, routing, request/response behavior, APIs,
  dependency injection, and data-backed application structure.

## Relationship to Concurrent Courses

This course runs during Semester 2 alongside:

- `10-152-120 Database Query and Design`
- `10-152-121 Advanced Python Systems`
- `10-152-123 Modern Data Modeling for Systems`

The intended 8-week block structure appears to imply:

```text
Weeks 1-8:   10-152-120 Database Query and Design
Weeks 9-16:  10-152-123 Modern Data Modeling for Systems
Weeks 1-17:  10-152-122 C# Application Development
```

That sequencing creates a useful staging pattern for C#:

- Early C# data work should use collections, files, JSON, and in-memory
  repositories rather than assuming database fluency.
- Database-connected work should begin after students have meaningful exposure
  to relational tables, keys, joins, and queries.
- ASP.NET Core should arrive late enough that students can connect routes,
  models, services, and data access to the modeling concepts they are studying in
  `10-152-123`.
- The course should preserve transfer bridges back to Python and forward to
  later C++ systems-performance work.

## High-Level Time Allocation

Suggested emphasis:

```text
50% C# language, programming structures, and OOP
20% .NET tooling, debugging, testing, files, packages, and application structure
15% data access, persistence, repositories, and integration patterns
15% ASP.NET Core and web-oriented application patterns
```

This keeps ASP.NET Core relevant without allowing it to absorb the course.

## 17-Week Draft Structure

### Week 1 - Orientation: C#, .NET, and ASP.NET Core

Purpose: establish the mental model for the course.

Topics:

- C# as a programming language
- .NET as runtime, library ecosystem, CLI, project model, and tooling
- ASP.NET Core as one application framework within .NET
- Classic ASP.NET/Web Forms/older MVC versus modern ASP.NET Core
- Mapping from prior Python and web-development coursework

Lab direction:

- Install or verify development tools
- Create and run a C# console application
- Create and run a minimal ASP.NET Core endpoint for comparison
- Discuss what is language, what is framework, and what is tooling

### Weeks 2-4 - C# Programming Foundations

Purpose: transfer existing Python programming foundations into typed C#.

Topics:

- Variables, types, operators, strings, and type conversion
- Control flow, conditionals, loops, and methods
- Scope, parameters, return values, and basic program organization
- Debugging and tracing program behavior
- Console input and output

Lab direction:

- Small console programs
- Input validation
- Menu-based interaction
- Problem-solving exercises translated from familiar Python patterns into C#

### Weeks 5-7 - Object-Oriented C# and Interactive Applications

Purpose: make object-oriented structure concrete and usable.

Topics:

- Classes, objects, constructors, properties, and methods
- Encapsulation and object responsibilities
- Composition, inheritance, and interfaces
- Event-driven behavior as a general application pattern
- Application state and user interaction loops

Lab direction:

- Small domain models such as inventory, courses, tickets, tasks, or banking
- Interactive console applications with menus and user choices
- Refactoring procedural code into object-oriented structure

### Weeks 8-9 - Collections, Exceptions, Files, and JSON

Purpose: build practical data-handling skills before database integration.

Topics:

- Arrays, lists, dictionaries, and collection selection
- LINQ filtering, mapping, sorting, and grouping
- Exception handling and defensive programming
- File input/output
- JSON serialization and deserialization

Lab direction:

- Persist application data to files
- Load, validate, search, and update records
- Use LINQ to answer application questions
- Improve error handling in existing programs

### Weeks 10-11 - .NET Tooling, Testing, and Application Structure

Purpose: name and organize the development environment students have been using.

Topics:

- Projects, solutions, assemblies, and namespaces
- `dotnet` CLI workflow
- NuGet packages
- Debugging workflow
- Unit testing basics
- Introductory dependency injection and service structure

Lab direction:

- Create a multi-project solution
- Separate domain classes, application services, and tests
- Add basic unit tests
- Refactor an earlier application into cleaner layers

### Weeks 12-13 - Data Access Foundations

Purpose: connect C# application logic to the database and data-modeling sequence.

Topics:

- Repository pattern as a bridge between application logic and persistence
- In-memory, file-backed, and database-backed data access
- Basic database connectivity concepts
- CRUD operations from an application perspective
- Data validation and model consistency

Lab direction:

- Replace file-backed or in-memory storage with a simple database-backed layer
- Connect application models to tables and records
- Discuss how data design affects application code

Note: The exact database technology can remain flexible. Depending on local
tooling, this may use direct SQL access, lightweight local databases, or an
introductory Entity Framework Core workflow.

### Weeks 14-16 - ASP.NET Core and Web-Oriented Application Patterns

Purpose: apply C# and .NET skills in a modern web application context.

Topics:

- HTTP request/response basics
- Routing and endpoints
- Minimal APIs and/or controllers
- Model binding and validation
- JSON APIs
- Middleware at a conceptual level
- Dependency injection in ASP.NET Core
- Connecting web endpoints to application services and data access

Lab direction:

- Build a small ASP.NET Core web API from an earlier domain model
- Add routes for create, read, update, and delete operations
- Use Swagger, HTTP files, or an API client to test endpoints
- Connect API behavior to data access and validation logic

### Week 17 - Integration, Demonstration, and Transfer

Purpose: consolidate the course into a coherent application-development identity.

Topics:

- Review C#, .NET, and ASP.NET Core relationships
- Compare console, class library, test, and web API project types
- Reflect on Python-to-C# transfer
- Preview later C++ and systems-performance transfer
- Discuss how tools and frameworks change while core concepts persist

Lab direction:

- Final project demonstration or practical integration check
- Code explanation and debugging conversation
- Course-level reflection on application design choices

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Write and explain C# programs using typed variables, control flow, methods,
  collections, exceptions, and file handling.
- Design small object-oriented applications with appropriate classes, services,
  and responsibilities.
- Use the .NET development environment to create, run, debug, package, and test
  applications.
- Implement basic data access using staged persistence approaches.
- Explain the relationship between C#, .NET, and ASP.NET Core.
- Build a modest ASP.NET Core web API that connects user-facing request behavior
  to software logic and stored data.
- Adapt programming concepts across Python, C#, web development, data modeling,
  and later systems-performance contexts.

## Notes for Future Detailed Design

- Use Minimal APIs first unless there is a strong reason to begin with
  controllers. Minimal APIs make the route-to-code relationship visible.
- Introduce controllers as a more structured pattern students may encounter in
  larger applications.
- Avoid overcommitting to full-stack UI, Razor Pages, Blazor, authentication,
  complex EF Core modeling, or deployment in this course.
- Keep data access aligned with `10-152-120` and `10-152-123` so C# reinforces
  rather than duplicates the database sequence.
- Labs should favor cumulative application growth over disconnected syntax
  drills whenever possible.
- The final project should be modest but integrated: domain model, interaction,
  validation, persistence, and a small web-oriented surface.

