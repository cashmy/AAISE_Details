# Git Commit Taxonomy for RBA Artifacts v1

## Purpose

This document proposes a working commit taxonomy for repositories that store
RBA-governed artifacts such as:

- framing documents
- architecture documents
- course artifacts
- program-design artifacts
- white papers
- case studies
- matrices and appendices

It is meant to preserve the useful structure of Conventional Commits while
adapting the commit types to artifact ecosystems that are not primarily
software-code repositories.

---

## Recommended Format

Use the same basic commit structure:

```text
type(scope): summary
```

Examples:

```text
frame(program): define current problem state for AI-era curriculum redesign
arch(bridge): establish two-track transition model
paper(whitepaper): draft executive summary and core sections
case(rba): capture program-design and white-paper case study
refactor(program): revise bridge logic after course-level analysis
```

---

## Proposed Commit Types

### Core Design and Architecture

- `frame`
  - use for problem framing, reframing, or clarifying the governing issue
- `arch`
  - use for architectural structure, transition models, or system logic
- `model`
  - use for capability models, workforce models, or conceptual models
- `refactor`
  - use for structural reorganization or upward refactoring
- `synth`
  - use for synthesis artifacts that combine multiple inputs into one coherent
    output

### Artifact Production

- `artifact`
  - use for generic artifact creation when no narrower type is helpful
- `paper`
  - use for white papers, executive summaries, or position papers
- `case`
  - use for case studies, reflections, or lessons learned
- `matrix`
  - use for matrices, mappings, and condensed tables
- `appendix`
  - use for appendix or companion reference materials

### Curriculum and Program Work

- `course`
  - use for course-level artifacts or redesign work
- `program`
  - use for program-level architecture or redesign work
- `bridge`
  - use for bridge-version design work
- `capability`
  - use for graduate capability or competency direction artifacts
- `constraint`
  - use for constraints and design-realities work

### Repository Maintenance

- `rename`
  - use for renaming artifacts
- `move`
  - use for moving or reorganizing files
- `meta`
  - use for repo guidance, process notes, or taxonomy updates
- `chore`
  - use for light housekeeping

---

## Suggested Minimal Starter Set

If a smaller and more practical set is preferred, start with:

- `frame`
- `arch`
- `artifact`
- `program`
- `course`
- `paper`
- `case`
- `refactor`
- `meta`

This smaller set is often enough for most RBA-governed artifact work.

---

## Suggested Internal Meanings

To keep commit history meaningful, the following distinctions may help:

- `frame`
  - changes the governing interpretation of the work
- `arch`
  - changes the structural logic of the artifact system
- `refactor`
  - reorganizes structure without changing the primary purpose
- `synth`
  - combines multiple prior artifacts into a new higher-order artifact
- `case`
  - captures reflective or comparative analysis of applied work

---

## Examples

```text
frame(program): define current problem state for AI-era curriculum redesign
arch(bridge): establish two-track transition model for legacy and successor paths
model(capability): draft graduate capability model for proposed AAISE direction
constraint(program): capture governance and sequencing realities
course(python): document bridge implementation patterns already in play
matrix(bridge): create condensed semester-by-semester course direction matrix
paper(whitepaper): draft full white paper and appendices
case(rba): document compressed program-design and white-paper case
refactor(program): revise bridge structure after course-level analysis
meta(repo): add commit taxonomy guidance for artifact ecosystem
```

---

## Important Note

This taxonomy is intentionally more artifact-centered than software-centered.

That is because the repository may contain complex interdependent design
artifacts whose value is architectural, instructional, analytical, or
persuasive rather than executable in the usual code sense.

Even so, the taxonomy should remain simple enough that it does not become a
burden to use.
