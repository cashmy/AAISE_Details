# Git Commit Taxonomy Cheatsheet

## Format

| Pattern | Example |
| --- | --- |
| `type(scope): summary` | `frame(program): redefine current problem state for AI-era redesign` |

---

## Commit Types

| Type | Use When | Typical Examples |
| --- | --- | --- |
| `frame` | The governing understanding changes | problem reframing, scope clarification, correcting a higher-order assumption |
| `build` | Creating substantial new work | new artifacts, new sections, new matrices, new program/course content |
| `refactor` | Structure improves without major change to core intent | reorganizing documents, tightening structure, improving sequence or alignment |
| `synth` | Combining multiple artifacts into a higher-order output | merging sections into a full draft, combining several artifacts into one summary |
| `review` | A change is driven mainly by feedback or inspection | supervisor revisions, advisory revisions, review-response changes |
| `meta` | Process or repo guidance changes | workflow notes, commit taxonomy, README/process guidance |
| `chore` | Light maintenance only | renaming, moving files, formatting cleanup |

---

## Default Scopes

| Scope | Use For |
| --- | --- |
| `program` | program design, transition models, bridge/successor work |
| `course` | course-level artifacts and redesign work |
| `whitepaper` | white paper sections, appendices, full draft work |
| `case-study` | case studies and reflections |
| `workflow` | process conventions, commit taxonomy, operational guidance |
| `repo` | repo-level organization and maintenance |

---

## Quick Decision Rule

| If the main move is... | Use |
| --- | --- |
| changing the governing meaning | `frame` |
| creating substantial new material | `build` |
| reorganizing existing structure | `refactor` |
| combining multiple strands | `synth` |
| revising from feedback | `review` |
| updating process/repo guidance | `meta` |
| doing minor maintenance only | `chore` |

---

## Sample Commits

| Situation | Sample Commit |
| --- | --- |
| redefine the core problem | `frame(program): redefine bridge and successor relationship` |
| add new course artifact work | `build(course): add Python bridge implementation patterns` |
| tighten existing program structure | `refactor(program): tighten semester-by-semester bridge structure` |
| merge paper sections into one draft | `synth(whitepaper): merge sections and appendices into full draft` |
| revise after supervisor feedback | `review(whitepaper): revise framing for supervisor readability` |
| update the commit system itself | `meta(workflow): simplify commit taxonomy for artifact ecosystems` |
| rename or reorganize files | `chore(repo): rename and reorganize support files` |

---

## Keep It Simple

| Rule | Reminder |
| --- | --- |
| 1 | Prefer consistency over perfect precision |
| 2 | Use broad scopes, not overly specific ones |
| 3 | Avoid inventing new types unless needed repeatedly |
| 4 | If a commit spans multiple artifacts, classify by the dominant action |
