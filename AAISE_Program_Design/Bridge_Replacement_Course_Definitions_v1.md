# Bridge Replacement Course Definitions v1

## Purpose

This document provides first-pass definitions for likely replacement or new
course candidates in the AI-injected bridge version of the Southwest Tech IT
Software Developer program.

It is not a final approved course map.

Its purpose is to move from broad candidate areas into more concrete
bridge-level course definitions that can later support:

- bridge curriculum decisions
- white paper examples
- advisory-facing discussion
- transition planning toward a future AAISE successor program

---

## Why This Artifact Matters

At this stage, several existing course slots appear weak, redundant, or
over-scoped for the bridge.

That creates opportunity, but also risk.

If replacements are chosen too loosely, the bridge may become a collection of
interesting ideas rather than a coherent progression.

This artifact helps reduce that risk by asking a more disciplined question:

if a replacement course is added, what specific job is it supposed to do?

---

## Replacement Definition Format

Each candidate below is defined in terms of:

- purpose
- why it belongs in the bridge
- likely workforce-model support
- likely capability contributions
- placement logic
- cautions

---

## Candidate 1. Modern Data Modeling for AI-Enabled Systems

### Likely replacement target

- `10-152-123 SQL Programming Advanced`

### Purpose

This course would move the bridge beyond a second traditional SQL course and
toward a broader model of modern data-system reasoning.

Its purpose would be to teach students how to think about the shape, structure,
retrieval, and architectural use of data across different kinds of systems,
especially where AI-enabled applications are involved.

### Why it belongs in the bridge

This course directly supports one of the bridge's clearest current needs:

students need more than query-writing practice.

They need to understand:

- when relational design fits
- when non-relational approaches fit
- what abstractions such as ORMs hide and reveal
- how data structure affects retrieval and application behavior
- why vector and embedding-oriented patterns matter in AI-supported systems

This is bridge-appropriate because it supports both modern employability and
future AAISE alignment without demanding full AI-native specialization.

### Workforce Model support

- `WM1 Native`: database and application data reasoning
- `WM2 AI-Assisted`: validating AI-produced queries and schema ideas
- `WM3 AI-Injected`: data structures for AI-supported application behavior
- `WM4 AI-Embedded`: retrieval and data-flow awareness for internal AI systems

### Capability contributions

- data, context, and input-quality reasoning
- AI-injected application design
- AI-embedded systems awareness
- systems and architectural thinking

### Likely placement

For the bridge version, the most practical placement is likely after the first
SQL course by using this course as the replacement for `10-152-123`.

That is not the cleanest conceptual order, but it may be the most workable
bridge order under current structural constraints.

For the future AAISE successor model, a cleaner order may be:

- modern data modeling first
- SQL implementation second

### Cautions

This course should not become:

- abstract database theory without practical relevance
- a disguised second SQL course
- an overloaded survey of every possible database technology

It should stay focused on design reasoning and practical system fit.

It also should not silently pretend that bridge order and ideal order are the
same thing.

The bridge may need a practical compromise sequence even if the successor
program later uses a cleaner pedagogical sequence.

---

## Candidate 2. Collaborative Delivery, GitHub, and CI/CD

### Likely replacement target

- `10-152-125 ASP.NET Programming` if ASP.NET is merged into C#
- or expansion path connected to `10-152-129 Agile Practices`

### Purpose

This course would formalize professional development workflow as a real bridge
capability rather than an assumed side behavior.

Its purpose would be to teach students how software actually moves through
collaborative environments, including version control, review, automation, and
AI-assisted workflow discipline.

### Why it belongs in the bridge

This is one of the clearest employability upgrades available.

It supports:

- regional software practice
- immediate job readiness
- team-based development
- AI-assisted coding under governance rather than isolation

It also helps the bridge avoid a common weakness:

students may learn languages and frameworks without learning how modern teams
actually deliver software together.

### Workforce Model support

- `WM1 Native`: standard professional delivery workflow
- `WM2 AI-Assisted`: AI inside review, coding, debugging, and delivery process
- `WM3 AI-Injected`: team workflow for building AI-supported applications

### Capability contributions

- software foundations
- human governance and professional judgment
- testing, validation, and uncertainty handling
- adaptability and continuous learning

### Likely placement

Semester 4 is the clearest placement, though some pieces could appear earlier.

It pairs naturally with Agile Practices and a final applied course.

### Cautions

This course should not collapse into:

- tool demos without real workflow discipline
- GitHub branding without transferable concepts
- CI/CD vocabulary without actual practice

The goal is governed delivery, not superficial tooling awareness.

---

## Candidate 3. Applied AI Integration Studio

### Likely replacement target

- `10-152-130 Software Career Experience`

### Purpose

This course would replace a loose, lengthy end-of-program experience with a
more bounded and demonstrable applied integration course.

Its purpose would be to require students to build, justify, test, and present a
coherent software artifact or system slice that reflects the bridge's intended
capabilities.

### Why it belongs in the bridge

The current bridge needs a clearer professional synthesis point.

A studio model fits that need better than an open-ended time-based experience
because it emphasizes:

- integration
- accountability
- demonstration
- design reasoning
- evidence of applied capability

This would give the bridge a more visible ending and a stronger discussion
point in the white paper.

### Workforce Model support

- `WM1 Native`: software build and delivery
- `WM2 AI-Assisted`: governed use of AI during build process
- `WM3 AI-Injected`: intentional AI-supported application or workflow design
- `WM4 AI-Embedded`: possible internal AI-supported system behavior if scoped
  appropriately

### Capability contributions

- AI-assisted development practice
- AI-injected application design
- testing, validation, and uncertainty handling
- human governance and professional judgment
- architectural and systems thinking

### Likely placement

Semester 4 is the clear fit.

This course should function as one of the bridge's signature culmination points.

### Cautions

This course should not become:

- a vague capstone with weak standards
- a time sink without clear outputs
- an unstructured internship substitute with uneven quality

The bridge needs a bounded, assessable integration experience.

---

## Candidate 4. Systems Performance and AI Runtime Foundations

### Likely target

- radical reframe of `10-152-128 C++ Programming`

### Purpose

This course would repurpose the C++ slot to teach systems-level realities that
are often hidden by higher-level languages and abstractions.

Its purpose would be to give students practical understanding of:

- memory behavior
- performance tradeoffs
- abstraction boundaries
- control versus convenience
- lower-level runtime thinking

It may also include selective advanced exposure to AI-runtime ecosystems such as
LibTorch and TensorFlow where that supports the course's systems purpose.

### Why it belongs in the bridge

This candidate is strong because it gives the bridge something distinct that
Python and C# do not provide as directly.

It helps students understand not only how to build software, but why certain
software and AI-system design choices carry different runtime costs and
constraints.

This is especially valuable in an AI era where many students may otherwise only
experience high-level abstractions.

### Workforce Model support

- `WM1 Native`: systems and performance reasoning
- `WM3 AI-Injected`: understanding infrastructure and runtime constraints
- `WM4 AI-Embedded`: lower-level awareness of model-serving and runtime tradeoffs

### Capability contributions

- architectural and systems thinking
- data, context, and input-quality reasoning
- testing, validation, and uncertainty handling
- adaptability and continuous learning

### Likely placement

Semester 3 is the strongest fit.

It should follow C# as a prerequisite and enough earlier programming maturity
that students can use C++ to examine system behavior rather than relearn basic
programming.

### Cautions

This course should not become:

- a generic second intro programming course
- an overloaded deep-learning survey
- an attempt to teach LibTorch and TensorFlow in excessive depth

Its identity should remain disciplined:

systems, performance, memory, runtime, and abstraction awareness first;
advanced AI-runtime exposure second.

---

## Candidate 5. Flutter/Dart Mobile and Intelligent App Delivery

### Likely replacement target

- redesign pathway for `10-152-132 Mobile Development`

### Purpose

This course would give mobile development a clearer technological and
conceptual identity if mobile remains part of the bridge.

Its purpose would be to connect application delivery, cross-platform
development, AI-assisted workflow, and modern client experience more coherently
than a generic mobile course may currently do.

### Why it belongs in the bridge

This is a conditional candidate rather than a core requirement.

It belongs in the bridge only if the program wants to preserve a clear
application-delivery lane that includes mobile or edge-facing experiences.

If retained, it could become much stronger by connecting mobile work to:

- API use
- cloud backends
- AI-assisted development
- AI-enabled user experiences

### Workforce Model support

- `WM1 Native`: mobile app development
- `WM2 AI-Assisted`: AI-supported development workflow
- `WM3 AI-Injected`: AI-enabled mobile application behavior

### Capability contributions

- software foundations
- AI-assisted development practice
- AI-injected application design
- adaptability and continuous learning

### Likely placement

Semester 3 or 4 depending on what other replacements are chosen.

### Cautions

This is not currently a top-tier bridge necessity.

It should only remain if it contributes clearly to the bridge's broader
coherence.

---

## Candidate 6. Secure AI-Enabled Systems

### Likely replacement target

- future review pathway for `10-151-101 Introduction to Security`

### Purpose

This course would modernize security-related preparation so that it reflects
software, API, data, and AI-enabled system realities more directly.

Its purpose would be to move beyond introductory awareness toward practical
development-side security thinking.

### Why it belongs in the bridge

This candidate is not the highest immediate priority, but it may become more
important in later refinement.

It would strengthen the bridge by connecting:

- secure coding habits
- auth and API concerns
- data discipline
- AI-related governance and misuse risks

### Workforce Model support

- `WM1 Native`: secure software habits
- `WM3 AI-Injected`: secure AI-enabled application behavior
- `WM4 AI-Embedded`: governance and boundary awareness for internal AI systems

### Capability contributions

- human governance and professional judgment
- testing, validation, and uncertainty handling
- systems and architectural thinking

### Likely placement

Semester 1 or 2 depending on whether the current security slot is retained and
how much redesign freedom exists.

### Cautions

This is a meaningful candidate, but it should not outrank the more urgent
bridge needs related to data, delivery workflow, and applied integration.

---

## Working Definition Summary

At the current stage, the most bridge-ready replacement definitions appear to
be:

1. Modern Data Modeling for AI-Enabled Systems
2. Collaborative Delivery, GitHub, and CI/CD
3. Applied AI Integration Studio
4. Systems Performance and AI Runtime Foundations

These four together would meaningfully strengthen the bridge's:

- data spine
- delivery realism
- end-of-program coherence
- WM3 and WM4 capability support

They also appear more aligned with current bridge needs than simply preserving
legacy-heavy course structures.

---

## Next Questions

The next design-stage questions likely include:

- Which of these replacement definitions should be locked into the bridge as
  actual proposed courses?
- Which should appear in the white paper as illustrative examples versus formal
  proposals?
- Which definitions belong only to the bridge, and which should later be
  deepened in the AAISE successor model?
