# Advanced Python Systems High-Level Course Plan v1

## Course

`10-152-121` - `Advanced Python Systems`

Credits: `3`  
Lecture/Lab: `36/36`  
Prerequisites: `10-152-117 Python Programming Foundations`,
`10-152-118 Web Development Foundations`

## Source Description

Learners deepen their Python skills by designing more capable, maintainable, and
efficient software solutions. The course emphasizes structured program design,
reusable components, data handling, testing, profiling, and the use of widely
adopted libraries and development tools, including structured data handling and
ORM-style application workflows. Students work with larger workflows involving
files, datasets, automation, and analysis while practicing debugging,
documentation, and code quality techniques. By the end of the course, learners
are able to build and explain more advanced Python-based systems and adapt their
approach to a range of technical problems and environments.

## Planning Position

This course should function as the bridge sequence's advanced Python, analytics,
and AI-readiness course. It should deepen students' prior Python foundation while
moving them toward larger workflows, third-party libraries, data analysis,
application structure, and framework-backed development.

The course should not become a full machine-learning course. That role belongs
more directly to `10-152-131 Machine Learning Foundations`. Instead, this course
should prepare students to succeed there by building the Python fluency,
data-library habits, testing practices, and dataset reasoning that later
model-oriented work requires.

The central course movement is:

```text
manual Python refresh and accountability
-> Django setup, project anatomy, ORM, templates, forms, and serializers
-> reusable components inside a framework-backed application
-> testing-first, integration, and end-to-end thinking
-> Jupyter-supported analytics libraries and larger data workflows
-> AI-assisted and AI-integrated Python development habits
```

The AI-use progression should mirror the broader bridge pattern:

```text
manual first -> AI-assisted/explained -> AI-integrated with accountability
```

Students should first build or trace a working manual baseline, then use AI to
explain, extend, test, refactor, or compare approaches, and finally integrate AI
support into larger workflows while retaining authorship and verification.

## Relationship to Prerequisite Python Course

`10-152-117 Python Programming Foundations` already gives students a compressed
but meaningful base in:

- variables, expressions, input/output, decisions, loops, functions, lists, and
  dictionaries
- simple debugging, expected-versus-actual testing, and code explanation
- recognition-level procedural, function-based, and class-based code reading
- file persistence, text files, CSV, JSON, config files, and error handling
- API endpoints, requests, responses, and JSON parsing
- recognition-level Python app architecture, including Django MVT, templates,
  and forms
- RBA project framing, AI-use boundaries, capstone build, and final explanation

Therefore, this course should not repeat those as first-exposure topics. It
should instead convert them into more durable practice:

```text
intro functions          -> reusable components and modules
simple debugging/testing -> testing-first habits, integration/e2e checks,
                            logging, profiling, and code quality
basic files/APIs         -> brief bridge into imports, serializers, and
                            ORM-backed integrations
class recognition        -> more confident use of objects and framework models
Django preview           -> actual Django setup, project anatomy, ORM, and APIs
AI-use awareness         -> documented, accountable AI-assisted and
                            AI-integrated workflows
```

## Relationship to Concurrent Courses

This course runs during Semester 2 alongside:

- `10-152-120 Database Query and Design`
- `10-152-122 C# Application Development`
- `10-152-123 Modern Data Modeling for Systems`

The intended semester structure appears to imply:

```text
Weeks 1-8:   10-152-120 Database Query and Design
Weeks 9-16:  10-152-123 Modern Data Modeling for Systems
Weeks 1-17:  10-152-121 Advanced Python Systems
Weeks 1-17:  10-152-122 C# Application Development
```

This course should coordinate with the data sequence in a staged way:

- Early Python data work should build on prior `10-152-117` exposure to text,
  CSV, JSON, config files, APIs, and endpoints rather than reteaching those
  topics as first exposure.
- Early framework work should use Django ORM to place some relational and
  data-modeling concerns under the hood while students are concurrently learning
  explicit SQL concepts in `10-152-120`.
- A brief file/API bridge is enough: students should connect prior CSV, JSON,
  config, and endpoint skills to Django imports, fixtures, serializers, and
  API-shaped output rather than spend a full unit on basic file I/O.
- Mid-course analytics work can connect pandas, NumPy, SQL query outputs, ORM
  querysets, and serialized data.
- Later work can connect Python dataframes, ORM models, serializers, JSON
  structures, and AI-ready datasets to the broader modeling ideas in
  `10-152-123`.
- The course should complement C# by showing Python's strengths in automation,
  analysis, experimentation, and data-heavy workflows.

## High-Level Time Allocation

Suggested emphasis:

```text
15% advanced Python language, structure, modules, and maintainability
25% Django setup, project structure, ORM, serializers, URL mapping, settings,
    templates, forms, and web-oriented Python application patterns
25% analytics foundations with Jupyter notebooks, NumPy, pandas, SciPy, Polars,
    PyArrow, and related data libraries
15% testing-first, debugging, integration testing, end-to-end testing,
    profiling, documentation, and code quality
10% advanced data integration with prior file/API foundations, SQL, ORM-backed
    data, serializers, and structured workflows
10% AI-ready Python workflows, APIs, embeddings/vector-shaped data, and
    data-preparation habits
```

## Library and Tooling Scope

The course should include widely adopted third-party tools, but should avoid
turning library coverage into a checklist. The goal is transfer: students should
learn how to adopt Python libraries responsibly, read documentation, inspect data,
debug library-driven workflows, and explain why a tool fits a task.

Likely library/tool families:

- Core environment: VS Code, `venv`, `pip`, project folders, `.env` patterns,
  dependency files, command-line execution, and quick recognition of `uv` as a
  modern alternative workflow
- Testing and quality: test-first development habits, Django tests, integration
  tests, end-to-end checks, `pytest` where useful, debugging tools, logging, and
  formatting/linting at an introductory level
- Data structures and analysis: `NumPy`, `pandas`
- Scientific and statistical foundations: selected `SciPy` concepts where
  appropriate
- Larger/faster data workflows: `Polars`, `PyArrow`, and parquet concepts at a
  survey or applied-comparison level
- Notebook and exploratory workflow: Jupyter notebooks and/or JupyterLab as
  tools for exploration, analysis, explanation, and lightweight AI/data
  experimentation
- Visualization and communication: selected plotting and notebook-based
  reporting workflows
- Web and ORM patterns: Django setup, project/app structure, settings, URL
  mapping, views, templates, Django ORM, migrations, serializers, and forms or
  API views at an introductory level
- AI-adjacent workflows: API calls, structured outputs, embeddings/vector data at
  a conceptual or light applied level, and dataset preparation
- Adjacent ecosystem recognition: FastAPI, SQLAlchemy, and Pydantic should be
  named as tools students may encounter in Python shops, but this course should
  not make them required build targets unless later detailed design creates a
  specific integration need.
- Deployment foreshadowing: Docker/containerization can be shown briefly as a
  preview of `10-152-124 Containerized App Deployment`, especially to explain why
  Python/Django dependencies and environments matter.

## 17-Week Draft Structure

### Week 1 - Advanced Python Course Orientation

Purpose: reposition students from introductory Python into larger, maintained,
library-supported systems.

Topics:

- Review of prior Python foundations
- What makes Python "advanced" in this bridge context
- Scripts versus modules versus systems versus notebooks
- Python's role in analytics, automation, web, and AI workflows
- Relationship to C#, databases, and data modeling
- VS Code as the primary development environment, with brief recognition of
  Jupyter and `uv` as additional workflow tools

Lab direction:

- Set up a course Python environment
- Review a small Python program and identify maintainability issues
- Revisit a familiar prior-course style workflow and identify what would need to
  change for reuse, testing, documentation, or analysis

### Weeks 2-4 - Django Setup, Project Anatomy, ORM, Templates, Forms, and Serializers

Purpose: make Django the early working frame so students repeatedly apply
Python, data, web, and modeling concepts inside a real framework structure.

Topics:

- Django environment setup and dependency workflow
- Django project and app structure
- `settings.py`, installed apps, configuration, and development server workflow
- URL mapping, views, templates, and request/response behavior
- Django models, migrations, admin, and introductory ORM querying
- Forms and basic validation
- Serializers and API-shaped data, likely through Django REST Framework or a
  lightweight equivalent
- Manual-first build, AI-assisted explanation, then AI-assisted extension

Lab direction:

- Set up a Django project and app from scratch
- Trace how settings, URLs, views, templates, models, migrations, forms, and
  serializers connect
- Build a small Django application around a familiar data domain
- Define simple ORM models and query them through views, templates, and
  serialized output
- Compare Django ORM concepts to SQL and C# data access concepts

### Weeks 5-6 - Reusable Components Inside Django Applications

Purpose: strengthen Python organization by applying it inside the Django project
students are already using.

Topics:

- Modules, packages, imports, and project organization
- Functions, classes, dataclasses, type hints, and service-style helpers
- Separating view logic, model logic, forms, serializers, and utility code
- Configuration and environment values
- Logging and structured error handling
- Brief bridge to prior file/API work: CSV, JSON, config, endpoints, and imports
- Carrying forward AI-use boundaries from prior Python project work

Lab direction:

- Refactor Django-adjacent logic into reusable modules or helper functions
- Add import/export or API-shaped data behavior without reteaching basic file I/O
- Build a small data import, fixture, or serializer-backed workflow
- Add type hints and documentation strings where useful
- Introduce logging and structured error handling in the Django context

### Week 7 - Testing-First, Integration, and End-to-End Thinking

Purpose: move beyond simple expected-versus-actual checks into testing styles
that fit framework-backed applications.

Topics:

- Testing-first habits for small features
- Django model, view, form, serializer, and route tests at an introductory level
- Integration tests and simple end-to-end workflow checks
- Debugging strategies in a framework-backed application
- Basic profiling and performance observation
- Code readability, documentation, and review

Lab direction:

- Write tests before or alongside a small Django feature
- Test a form submission, route, model behavior, or serialized response
- Debug a broken workflow across URL, view, model, template, or serializer
- Profile or inspect a slow or inefficient data-facing path
- Improve naming, structure, and documentation

### Weeks 8-11 - Jupyter, Analytics Foundations, and Third-Party Data Libraries

Purpose: build the Python data-library fluency needed for analytics, AI
preparation, and later machine-learning coursework.

Topics:

- Jupyter notebooks as an exploratory, explanatory, and analytical workflow
- Notebook cells, markdown, outputs, rerun order, and reproducibility concerns
- Arrays, series, and dataframes
- Loading, inspecting, filtering, sorting, and grouping data
- Missing values and data types
- Joins/merges from a dataframe perspective
- Summary statistics and exploratory analysis
- Selected SciPy concepts where appropriate
- Visualization or lightweight reporting where useful
- Connecting ORM querysets, SQL outputs, CSV/JSON data, and dataframe workflows

Lab direction:

- Create a Jupyter notebook that explains an analysis as well as performs it
- Analyze a small dataset using pandas
- Use NumPy for array-oriented operations where appropriate
- Use selected SciPy tools for a bounded analysis task if appropriate
- Clean, filter, group, and summarize data
- Connect dataframe operations to SQL concepts students are learning or have
  recently completed
- Move data between Django/ORM-shaped sources and dataframe-shaped analysis
- Compare when a notebook, script, or Django feature is the better workflow

### Week 12 - Larger Data Workflows and Performance-Aware Libraries

Purpose: show that tool choice matters as data size and workflow complexity grow.

Topics:

- Applying prior Big-O and growth-rate reasoning to Python data workflows
- Vectorized operations versus row-by-row loops
- Memory, file format, and data size awareness
- Parquet and columnar data concepts
- Introductory comparison of pandas, Polars, and PyArrow

Lab direction:

- Compare loop-based and vectorized approaches
- Read and write tabular data in multiple formats
- Explore a larger dataset with pandas and/or Polars
- Explain tool tradeoffs without overclaiming one universal best choice

### Weeks 13-14 - AI-Ready Python Workflows and Data Preparation

Purpose: prepare students for later machine-learning and AI-integration work.

Topics:

- Notebooks versus scripts versus applications
- Jupyter as an experimentation and explanation environment for AI/data work
- Dataset preparation for model-oriented workflows
- API calls and structured responses
- Embeddings and vector-shaped data at a conceptual or light applied level
- AI-assisted explanation, refactoring, testing, and data inspection
- AI-integrated workflows inside scripts, notebooks, or Django-backed features
- Reproducibility, documentation, and responsible experimentation

Lab direction:

- Prepare a small dataset for later analysis or model work
- Call an API or process structured API-like data
- Create a documented notebook or script-based analysis
- Extend a Django or analytics workflow with AI-assisted explanation or
  AI-integrated behavior
- Identify what makes a dataset usable, trustworthy, and explainable

### Weeks 15-16 - Integrated Advanced Python Build

Purpose: consolidate Django, ORM-backed data, analytics libraries, testing, and
AI-integrated workflow habits into a coherent applied system.

Topics:

- Feature planning and scope control
- Combining Django, serializers, data libraries, and analysis outputs
- Testing-first or test-alongside development
- Manual baseline, AI-assisted refinement, and AI-integrated extension
- Documentation, explanation, and accountability

Lab direction:

- Build or extend a small Django-backed/data-backed Python system
- Include at least one analytics or data-library workflow
- Include tests or end-to-end checks for a meaningful user/data path
- Document AI use, verification, rejected suggestions, and student-owned
  decisions

### Week 17 - Integration, Demonstration, and Transfer

Purpose: consolidate advanced Python as a flexible systems, analytics, and
AI-readiness tool.

Topics:

- Review structured Python development
- Compare script, module, notebook, Django, ORM, serializer, and data-analysis
  workflows
- Connect Python to databases, data modeling, C#, and later ML foundations
- Preview how containerized environments will be treated more fully in
  `10-152-124`
- Discuss adapting as libraries and frameworks change

Lab direction:

- Final integrated workflow demonstration
- Code explanation and debugging conversation
- Reflection on tool choice and transfer to future courses

## Recommended Course-Level Outcome Frame

By the end of the course, students should be able to:

- Organize Python code into maintainable modules, functions, classes, and
  reusable components within script, analysis, and framework-backed contexts.
- Build a small Django application workflow that uses project/app structure,
  settings, URL mapping, ORM models, migrations, forms, templates, serializers,
  and API-shaped data.
- Use testing-first, debugging, logging, integration/end-to-end checks,
  profiling, and documentation practices to improve Python systems.
- Build focused data workflows using prior file/API foundations, SQL-oriented
  data, ORM-backed data, serializers, and structured transformations.
- Use NumPy, pandas, SciPy where appropriate, and selected related libraries to
  inspect, clean, transform, summarize, and communicate datasets.
- Use Jupyter notebooks to explore, explain, document, and communicate analysis
  and AI-ready data workflows.
- Explain when larger-data tools such as Polars, PyArrow, and columnar formats
  may be useful.
- Prepare Python workflows and datasets for later AI, analytics, and
  machine-learning coursework.
- Explain Python's role alongside C#, relational databases, modern data
  modeling, and later machine-learning systems.

## Notes for Future Detailed Design

- Move Django early enough that students use it as a repeated working frame,
  not a late survey topic. Students should understand how Django uniquely
  organizes projects, apps, settings, URL mapping, models, migrations, templates,
  forms, and serializers.
- Keep Django bounded even with the early block. It should demonstrate ORM and
  framework patterns, not become a full Django specialization.
- Avoid making this a machine-learning course. The course should prepare
  students for ML foundations rather than replace it.
- Avoid making library coverage a race through package names. Prefer a few
  meaningful workflows with clear transfer value.
- Treat Jupyter as a real workflow mode, not merely a side tool. Students should
  understand when notebooks help exploration and explanation, and when scripts,
  modules, or Django features are more appropriate.
- Introduce Docker only as a lightweight foreshadowing concept for
  `10-152-124`; do not make containerization a required build target here.
- Name FastAPI, SQLAlchemy, and Pydantic as adjacent Python ecosystem tools, but
  keep them recognition-level in this course unless later curriculum mapping
  assigns them here explicitly.
- Keep file, CSV, JSON, config, and API review brief because `10-152-117` already
  teaches those foundations. Use them as bridge material for imports, serializers,
  ORM-backed data, and analysis workflows.
- Preserve the prior course's authorship and AI-accountability expectations:
  students should be able to explain what they wrote, what AI assisted with, how
  they checked it, and what design decisions remained theirs.
- Use datasets and domains that can coordinate with the database, C#, and modern
  data-modeling courses.
- Include enough performance reasoning to connect to `10-152-119`, especially
  around vectorized operations, data size, and library choice.
- Favor cumulative workflows where students refine, test, analyze, and explain
  the same or related systems over time.
