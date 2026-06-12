# Weekly Reading Guide

**10-152-117 Python Programming**

---

# Purpose

This artifact maps the course sequence to selected readings from:

**Learn Python Programming, Fourth Edition**  
Fabrizio Romano and Heinrich Kruger  
Packt Publishing, 2024  
ISBN: `978-1-83588-294-8`

The textbook is broader and more advanced than this 8-week introductory Python
course. Therefore, readings are assigned as weekly learning support, not as a
strict chapter-by-chapter march through the book.

The recommended structure is:

```text
weekly reading assignment
-> day-level reading focus
-> skim / future-reference guidance
-> do-not-worry-yet boundary
```

This keeps Schoology instructions simple while still helping students connect
the reading to each class meeting.

---

# Source Basis

This guide was drafted from the publicly available table of contents and product
information for the fourth edition.

Primary TOC references:

- Packt product page: `https://www.packtpub.com/en-gr/product/learn-python-programming-9781835882948`
- O'Reilly listing: `https://www.oreilly.com/library/view/learn-python-programming/9781835882948/`

Important note:

This guide maps by chapter and topic title, not by page number. Exact page
ranges should be added after the instructor reviews the physical or digital
textbook layout.

---

# Student Reading Posture

Students should use the textbook in three different ways:

1. **Read carefully** when the topic directly supports the current lab.
2. **Skim for recognition** when the topic is useful context but not yet a
   required skill.
3. **Save for later reference** when the book goes deeper than the current
   course target.

Students should not panic when the textbook introduces advanced concepts early.

This course will teach the required beginner path in lecture, demos, labs, and
practice. The textbook provides reinforcement, alternate explanations, and
future reference depth.

---

# Weekly Map At A Glance

| Week | Course Theme | Primary Textbook Areas | Reading Role |
| --- | --- | --- | --- |
| 1 | First Programs and Basic Values | A Gentle Introduction to Python; Built-In Data Types | Required foundation, curated heavily |
| 2 | Decision Logic and Repetition | Conditionals and Iteration | Required foundation |
| 3 | Organizing Code and Data | Functions; Built-In Data Types | Required foundation, curated |
| 4 | Debugging, Testing, and Code Literacy | Testing; Debugging and Profiling; OOP recognition | Required plus recognition |
| 5 | Files, Errors, and Data Persistence | Exceptions and Context Managers; Files and Data Persistence | Required foundation |
| 6 | APIs, External Data, and Architecture Preview | Files/Data Persistence requests sections; Introduction to API Development | Required plus recognition |
| 7 | RBA and Capstone Framing | Packaging Python Applications; Programming Challenges; AI/good-code sections | Reference and framing support |
| 8 | Capstone Build, Revision, and Explanation | Testing; Debugging; Packaging; Type Hinting optional | Reference and final support |

---

# Week 1 - First Programs and Basic Values

## Weekly Reading Assignment

Read or skim selected parts of:

- **A Gentle Introduction to Python**
- **Built-In Data Types**

## Monday Focus

Read for familiarity with:

- what programming is
- what Python is
- setting up the environment
- how to run a Python program
- Python's execution model
- the idea that code is organized into instructions
- a word about AI

Use this reading to support:

- running a tiny program
- seeing visible output
- understanding that Python follows instructions
- understanding that AI is not the first step for this assignment

## Tuesday Focus

Read for familiarity with:

- numbers
- strings
- simple values
- basic type awareness
- basic expressions

Use this reading to support:

- numeric values
- simple calculations
- value changes
- output formatting at a beginner level

## Thursday Focus

Read for familiarity with:

- strings and text values
- numbers versus text
- names and values
- final considerations about choosing basic data representations

Use this reading to support:

- combining strings and numbers carefully
- explaining value flow
- avoiding confusion between text and numeric values

## Skim / Save For Later

Skim only:

- virtual environments
- installing third-party libraries
- modules and packages
- namespaces and scopes
- deeper Python culture and style notes
- bytes, complex numbers, fractions, decimals
- collections module details
- dates and times

## Do Not Worry Yet

Students are not expected to master:

- virtual environments
- packages
- modules
- scopes
- advanced data types
- professional style rules
- third-party libraries

---

# Week 2 - Decision Logic and Repetition

## Weekly Reading Assignment

Read selected parts of:

- **Conditionals and Iteration**

## Monday Focus

Read carefully:

- conditional programming
- the `if` statement
- `elif`
- `else`
- nesting `if` statements

Use this reading to support:

- branch prediction
- small decision programs
- explaining why a branch runs

## Tuesday Focus

Read carefully:

- looping
- the `for` loop
- iterating over a range
- iterating over a sequence
- the `while` loop

Use this reading to support:

- repeated behavior
- counters
- accumulators
- stopping conditions

## Thursday Focus

Read for application:

- `break` and `continue`
- putting conditionals and loops together
- applying discounts or similar combined examples

Use this reading to support:

- menu-style logic
- repeated input patterns when introduced
- small programs that combine decisions and repetition

## Skim / Save For Later

Skim only:

- ternary operator
- pattern matching
- iterators and iterables in depth
- iterating over multiple sequences
- assignment expressions
- the walrus operator
- `itertools`
- combinatoric generators

## Do Not Worry Yet

Students are not expected to master:

- pattern matching
- advanced iterator behavior
- generator tools
- assignment expressions
- compact one-line decision syntax

---

# Week 3 - Organizing Code and Data

## Weekly Reading Assignment

Read selected parts of:

- **Functions, the Building Blocks of Code**
- **Built-In Data Types**

## Monday Focus

Read carefully:

- why use functions
- input parameters
- return values
- documenting your code

Use this reading to support:

- naming responsibility
- reducing repeated code
- writing small functions
- explaining what a function receives and returns

## Tuesday Focus

Read carefully or skim for support:

- mutable sequences
- lists
- mapping types
- dictionaries
- how to choose data structures

Use this reading to support:

- storing related data
- retrieving values
- iterating through a list
- looking up information in a dictionary

## Thursday Focus

Read for comparison:

- scopes and name resolution
- a few useful function tips
- final considerations about data structures

Use this reading to support:

- rough versus cleaner program structure
- why organization matters
- why manual baseline work should come before AI critique

## Skim / Save For Later

Skim only:

- recursive functions
- anonymous functions
- function attributes
- importing objects
- comprehensions and generators
- advanced built-in functions

## Do Not Worry Yet

Students are not expected to master:

- recursion
- lambdas
- decorators
- generators
- advanced import patterns
- full namespace theory

---

# Week 4 - Debugging, Testing, and Reading Structured Code

## Weekly Reading Assignment

Read or skim selected parts of:

- **Testing**
- **Debugging and Profiling**
- **OOP, Decorators, and Iterators**

## Monday Focus

Read carefully:

- debugging techniques
- troubleshooting guidelines

Use this reading to support:

- syntax versus logic bugs
- expected versus actual behavior
- print-debugging as evidence
- fixing a bug and explaining the fix

## Tuesday Focus

Skim for recognition:

- OOP overview
- the simplest Python class
- class and object namespaces
- the `self` argument
- initializing an instance

Use this reading to support:

- reading procedural code
- reading function-based code
- recognizing class-based structure
- making light modifications without deep OOP theory

## Thursday Focus

Read or skim:

- testing your application
- test-driven development as a concept
- debugging techniques review

Use this reading to support:

- simple test cases
- expected output checks
- pytest recognition
- explaining why a fix works

## Skim / Save For Later

Skim only:

- decorators
- decorator factories
- inheritance and composition
- multiple inheritance
- operator overloading
- polymorphism
- custom iterators
- profiling Python in depth

## Do Not Worry Yet

Students are not expected to master:

- full OOP design
- decorators
- inheritance hierarchies
- profiling tools
- test-driven development as a workflow
- pytest syntax mastery

---

# Week 5 - Files, Errors, and Data Persistence

## Weekly Reading Assignment

Read selected parts of:

- **Exceptions and Context Managers**
- **Files and Data Persistence**

## Monday Focus

Read carefully:

- working with files and directories
- opening files
- using a context manager to open a file
- reading from and writing to a file

Use this reading to support:

- programs that remember data
- text files
- reading saved values back into a program

## Tuesday Focus

Read carefully:

- exceptions
- tracebacks
- handling exceptions
- checking for file and directory existence
- data interchange formats
- working with JSON

Use this reading to support:

- `try` / `except`
- file-not-found handling
- invalid data handling
- JSON save/load patterns

## Thursday Focus

Read or skim:

- CSV/structured data as part of data interchange
- configuration files as a recognition topic
- database persistence as future reference

Use this reading to support:

- structured data reader work
- data representation comparison
- app-structure preview

## Skim / Save For Later

Skim only:

- binary file handling
- file compression
- custom JSON encoding/decoding
- pickle
- shelve
- databases
- INI and TOML configuration formats

## Do Not Worry Yet

Students are not expected to master:

- binary I/O
- database persistence
- custom serialization
- configuration-file systems
- advanced context manager design

---

# Week 6 - APIs, External Data, and Python App Architecture

## Weekly Reading Assignment

Read or skim selected parts of:

- **Files and Data Persistence**
- **Introduction to API Development**

## Monday Focus

Read or skim:

- I/O, streams, and requests
- making HTTP requests
- the Hypertext Transfer Protocol

Use this reading to support:

- request/response thinking
- sequential versus asynchronous recognition
- waiting for external data

## Tuesday Focus

Read carefully:

- what an API is
- the purpose of an API
- response status codes
- API data-exchange formats
- selecting values from returned data

Use this reading to support:

- approved API use
- simulated JSON fallback
- reading JSON-like responses
- extracting a few useful values

## Thursday Focus

Skim for architecture recognition:

- endpoints
- reading data
- creating data
- updating data
- deleting data
- documenting the API
- project setup and configuration as recognition only

Use this reading to support:

- Python beyond console scripts
- MVT/template/form recognition
- larger application flow

## Skim / Save For Later

Skim only:

- database modeling for the railway API
- authentication
- full endpoint implementation
- API documentation tooling
- deployment concerns

## Do Not Worry Yet

Students are not expected to master:

- building a full API
- authentication
- databases
- framework setup
- asynchronous programming syntax
- deployment

---

# Week 7 - RBA and Project Framing

## Weekly Reading Assignment

Use selected textbook sections as reference support rather than strict required
technical reading.

Recommended reference areas:

- **A Gentle Introduction to Python**: guidelines for writing good code, a word
  about AI
- **Packaging Python Applications**: project layout, README, dependencies,
  advice for starting new projects
- **Programming Challenges**: problem statements and solution discussion

## Monday Focus

Review or skim:

- a word about AI
- guidelines for writing good code
- problem statements from programming challenges

Use this reading to support:

- intent before generation
- project purpose
- manual framing before AI help

## Tuesday Focus

Skim:

- project layout
- README
- dependencies
- advice for starting new projects

Use this reading to support:

- project structure
- constraints
- scope control
- AI boundaries

## Thursday Focus

Review:

- problem statement examples
- final considerations in programming challenge sections
- README/project layout guidance

Use this reading to support:

- capstone proposal quality
- approval criteria
- explainable scope

## Skim / Save For Later

Skim only:

- PyPI publishing
- package metadata
- changelog
- license details
- scripts and entry points
- packaging build/publish workflow

## Do Not Worry Yet

Students are not expected to master:

- packaging a distributable Python project
- publishing to PyPI
- professional dependency management
- advanced project metadata

---

# Week 8 - Capstone Build, Revision, and Explanation

## Weekly Reading Assignment

Use selected textbook sections as final-reference support.

Recommended reference areas:

- **Testing**
- **Debugging and Profiling**
- **Packaging Python Applications**
- **Introduction to Type Hinting** as optional clarity support

## Monday Focus

Review:

- testing your application
- troubleshooting guidelines
- README/project layout guidance

Use this reading to support:

- capstone expectations
- validation evidence
- clear run instructions

## Tuesday Focus

Review:

- debugging techniques
- troubleshooting guidelines
- project layout
- README

Use this reading to support:

- revision
- refactoring
- reality contact
- coherence over feature sprawl

## Thursday Focus

Review or skim:

- benefits of type hinting
- documenting your code
- README guidance
- testing summary

Use this reading to support:

- final explanation
- presentation
- AI-use justification
- ownership of the final work

## Skim / Save For Later

Skim only:

- Mypy static type checker
- advanced type annotations
- package publishing
- performance profiling

## Do Not Worry Yet

Students are not expected to master:

- static type checking
- advanced type hint syntax
- distribution packaging
- profiling performance
- professional deployment workflow

---

# Instructor Notes

## Why Weekly Rather Than Daily Reading Assignments

The textbook does not align perfectly with the Monday/Tuesday/Thursday rhythm
of this course.

A weekly assignment with day-level focus prevents false precision. It allows the
instructor to say:

```text
This is the chapter area for the week.
Here is what to focus on for each class day.
Here is what to skim.
Here is what not to worry about yet.
```

That is cleaner for students and more accurate to the actual curriculum.

## How To Use This In Deck Sources

Each revised deck source should include a short `Reading Alignment` or
`Today's Reading Focus` section.

For Week 1 Day 1, for example:

- primary reading: A Gentle Introduction to Python
- focus: running Python, execution model, visible output, a word about AI
- boundary: do not require `input()`, packages, virtual environments, or
  advanced organization yet

## Future Revision

After the instructor reviews the physical or digital textbook, add exact page
ranges for each week.

