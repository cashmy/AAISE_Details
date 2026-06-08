# Deck Source Continuity Brief

**10-152-119 Algorithmic Problem Solving**

---

# Purpose

This governance artifact preserves the stable lecture deck source pattern for
Weeks 5-8.

It exists to reduce context drift after a long artifact-generation sequence.
Future deck source work should use Weeks 1-4 as the strong foundational base,
not the full conversation history.

The goal is to preserve:

- instructional sequence
- textbook handling
- demo-to-lab transfer
- AI-use boundaries
- instructor-note quality
- visual prompt support
- timing-note structure
- student-facing clarity

---

# Current Status

Existing deck source artifacts:

| Week | Deck Source | Slide Count | Status |
| --- | --- | ---: | --- |
| Week 1 | `Week_01_Deck_Source_Algorithms_Precision_and_Correctness.md` | 44 | Source complete; PPTX created from it and validated as useful |
| Week 2 | `Week_02_Deck_Source_Growth_and_Big_O_Intuition.md` | 50 | Source complete |
| Week 3 | `Week_03_Deck_Source_Data_Structure_Choice.md` | 48 | Source complete; next-reading slide updated for Week 4 |
| Week 4 | `Week_04_Deck_Source_Search_and_Sort_Behavior.md` | 49 | Source complete; next-reading slide updated for Week 5 |
| Week 5 | `Week_05_Deck_Source_Recursion_Iteration_and_Strategy.md` | 50 | Source complete; next-reading slide updated for Week 6 |
| Week 6 | `Week_06_Deck_Source_Graph_Traversal_and_Modeling.md` | 50 | Source complete; next-reading slide updated for Week 7 |
| Week 7 | `Week_07_Deck_Source_Similarity_Ranking_and_Hashing.md` | 50 | Source complete; next-reading slide updated for Week 8 |
| Week 8 | `Week_08_Deck_Source_Final_Synthesis_and_Explainability.md` | 50 | Source complete; final synthesis slide replaces normal next-reading pattern |

The Week 1 PowerPoint production confirmed that the slide-by-slide source
format is highly useful for final deck construction. No structural revision to
the deck source format is currently needed.

---

# Source Artifacts To Treat As Canonical Pattern

Use these artifacts as the primary pattern base:

- `Lecture_Outlines/LDS-AL_Lecture_Deck_Source_Design_Guide.md`
- `Lecture_Outlines/LDST-AL_Lecture_Deck_Source_Template.md`
- `Lecture_Deck_Sources/Week_01_Deck_Source_Algorithms_Precision_and_Correctness.md`
- `Lecture_Deck_Sources/Week_02_Deck_Source_Growth_and_Big_O_Intuition.md`
- `Lecture_Deck_Sources/Week_03_Deck_Source_Data_Structure_Choice.md`
- `Lecture_Deck_Sources/Week_04_Deck_Source_Search_and_Sort_Behavior.md`

Do not derive the remaining deck format from memory alone.

---

# Confirmed Deck Source Structure

Each deck source should include:

1. Deck metadata
2. Lesson purpose
3. Possible two-session split when the lesson is dense
4. Reading alignment
5. Textbook review
6. Reading key ideas
7. Terms to carry forward
8. What we will use today
9. What we will revisit later
10. Lesson outcomes
11. Slide sequence overview
12. Slide-by-slide source blocks
13. Demo bridge
14. Lab bridge
15. Wrap-up
16. Image prompt notes
17. Instructor timing notes
18. Post-lecture notes

Slide-level blocks should include:

- delivery category
- student-visible slide text
- instructor notes
- transition cue
- optional visual notes when useful
- demo/lab/evidence connection when applicable

The final PowerPoint deck is instructor-authored from this source. The deck
source should be PowerPoint-ready, but it should not attempt to dictate final
visual layout.

---

# Confirmed Slide Count Range

Weeks 1-4 established a practical source range of approximately 44-50 slides.

This is acceptable because:

- the course can support up to about three hours of lecture per week
- slides are modular
- optional and reserve sections can be skipped
- the instructor can condense during PowerPoint production
- the source preserves instructional logic even when not every slide is used

Do not reduce slide count artificially if the topic needs multiple small
conceptual steps.

Each slide should have one clear instructional job.

---

# Stable Instructional Flow

The recurring pattern should remain:

```text
review / bridge from previous lab
-> textbook review
-> core concept blocks
-> representation or evidence bridge
-> instructor demo
-> related but different student lab
-> README/evidence expectations
-> AI-use boundary
-> success check
-> next step
-> next reading preparation when reading details are available
```

This flow is now validated by Weeks 1-4.

---

# Textbook Handling Rules

Do not say:

```text
If students did not complete the reading
```

Use:

```text
Textbook Review
Reading Review
Key Ideas from the Reading
```

The reading is required before lecture, but the deck should still provide a
brief synopsis and then teach the key concepts in accessible form.

For math-heavy or theory-heavy sections:

- do not dismiss the math
- do not imply the textbook is wrong
- frame advanced notation as fuller computer-science treatment
- translate the idea back into developer reasoning
- distinguish "deeply learn now" from "recognize for later"
- connect concepts to functions, inputs, outputs, evidence, and tradeoffs

Core reminder:

```text
When you write a function that takes input, follows steps, and returns a
result, you are already participating in algorithmic thinking.
```

---

# Next-Reading Slide Pattern

The current pattern is:

- Week 1 includes an early textbook posture slide and a closing Week 2
  pre-reading slide.
- Week 2 includes a closing Week 3 pre-reading slide.
- Week 3 has a closing Week 4 pre-reading slide.
- Week 4 has a closing Week 5 pre-reading slide.
- Week 5 has a closing Week 6 pre-reading slide.
- Week 6 has a closing Week 7 pre-reading slide.
- Week 7 has a closing Week 8 pre-reading slide.
- Week 8 uses a course-forward reference slide rather than a normal
  next-reading slide.

For Weeks 5-8:

- Use a closing `How To Use The Textbook For Next Week's Reading` slide when
  there is a next reading.
- Do not invent next-reading guidance without the curated reading topics.
- If reading topics have not been provided, include an explicit placeholder
  marked for replacement.
- Week 8 should not include a normal next-reading slide unless it is reframed
  as future reference or course wrap-up.

Important process rule:

If asked to craft a deck source without the detailed reading assignment topics,
stop and request the reading topics before drafting.

---

# AI-Use Framing

The stable AI-use pattern for the course is:

1. Manual first
2. AI-assisted for explanation, critique, or research
3. AI-injected only when students justify and explain output
4. AI-integrated as a refraction-based collaborator only when appropriate

Deck sources should model AI as:

- explanation support
- critique support
- edge-case support
- complexity-review support
- assumption-checking support

Deck sources should not frame AI as:

- a first-step code generator
- a replacement for trace evidence
- a replacement for student explanation
- a way to avoid understanding the algorithm

Common phrasing pattern:

```text
Manual first:
- frame the problem
- attempt the logic
- create evidence

AI-assisted after:
- review assumptions
- check edge cases
- explain a confusing result
- critique tradeoffs
```

---

# Demo and Lab Alignment Rules

Each deck must preserve near transfer:

```text
lecture concept
-> instructor demo with similar concept
-> student lab with related but different scenario
```

The demo should not be the same as the lab scenario.

The demo should:

- make the concept observable
- produce evidence students can inspect
- be close enough for transfer
- remain different enough to prevent copying

The lab bridge should:

- name the related lab
- state what students must adapt
- identify required evidence
- remind students of README expectations
- include AI-use boundaries where appropriate

---

# README and Evidence Expectations

Deck sources should continue to emphasize GitHub/README evidence.

Students should learn that code, evidence, and explanation belong together.

README reminders may include:

- problem statement
- inputs and outputs
- assumptions or constraints
- data representation
- test table
- trace table
- timing table
- comparison table
- expected vs actual results
- recommendation
- limitations
- AI-use note, if applicable

The exact evidence type should match the lab.

---

# Instructor Notes Standard

Instructor notes and transition cues are a high-value part of the deck source.

They should be written for:

- the original instructor after time has passed
- a future instructor inheriting the course
- quality preservation across course deliveries

Notes should be brief but meaningful.

They should preserve:

- what to emphasize
- why the teaching move matters
- what example to use
- what misconception to watch for
- how the slide connects to the next slide

Avoid compressed notes that only work while the design conversation is fresh.

Example of preferred specificity:

```text
Use the weak instruction "Pick the best option." Ask students why that
instruction is hard for another person to follow. The issue is that "best" is
undefined; it could mean cheapest, fastest, healthiest, or most convenient.
Connect this back to precision and testability.
```

---

# Image Prompt Notes Standard

Keep image prompt notes.

Week 1 production confirmed that they are useful when visual support is needed,
even if not used for every slide.

Image prompt notes should:

- identify the visual need
- suggest a prompt or visual direction
- warn against misleading visuals
- support meaning rather than decoration

Do not overuse images. Visual frequency should be governed so the deck does not
become noisy or stock-like.

---

# Timing Notes Standard

Keep instructor timing notes.

They are provisional until live delivery, but they support:

- pacing judgment
- optional compression
- optional expansion
- future delivery adjustment

Timing notes should include:

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |

After live presentation, use post-lecture notes to refine timing.

---

# Current Week 1 Production Feedback

Week 1 was converted into a full PowerPoint deck.

Observed feedback:

- individual slide layout in the source was extremely helpful
- no revision to the deck source format is currently needed
- image prompt notes were useful on several occasions
- timing notes cannot be validated until after live delivery
- instructor notes/options/transitions on nearly every slide have high handoff
  value
- the final PowerPoint production remains a human-authored process, even when
  PowerPoint Designer and AI image generation assist with layout or visuals

This confirms the deck source as an intermediate instructional architecture,
not as a finished slide artifact.

---

# Drift Risks To Avoid

Avoid these risks in Weeks 5-8:

- overfitting to the recent RBA/HOMSP discussion rather than the Algorithms
  course
- turning deck sources into RBA lectures
- turning Week 7 into a full machine-learning course
- turning Week 8 into a capstone project presentation
- making AI use sound like unrestricted code generation
- treating textbook advanced topics as full mastery targets
- making the demo identical to the lab
- omitting README/evidence expectations
- omitting instructor notes or transition cues
- writing compressed instructor notes that will not make sense later
- inventing reading guidance without the curated reading assignment

---

# Remaining Decks To Create / Maintain

## Week 5 - Recursion, Iteration, and Strategy Patterns

Status:

- source complete
- closing reading slide updated for Week 6

Known course role:

- Unit 3 - Strategy Patterns and Observable Behavior
- supports Lab 05 - Strategy Comparison
- likely textbook support: Chapter 4 - Designing Algorithms
- expected focus: recursion, iteration, brute force, divide and conquer,
  greedy, dynamic programming recognition, strategy comparison

Guardrail:

- do not teach P, NP, NP-Complete, or NP-Hard in depth
- keep dynamic programming as recognition or light exposure unless reading
  details require a specific guided treatment
- emphasize strategy comparison and explainable tradeoffs

## Week 6 - Graph Traversal and Modeling

Status:

- source complete
- closing reading slide updated for Week 7

Known course role:

- Unit 3 - Strategy Patterns and Observable Behavior
- supports Lab 06 - Graph Traversal and Modeling
- likely textbook support: Chapter 5 - Graph Algorithms
- expected focus: graph vocabulary, nodes, edges, adjacency lists, BFS, DFS,
  paths, traversal evidence, real-system modeling

Guardrail:

- keep implementation modest and visual
- do not drift into advanced graph analytics unless used as reserve only
- emphasize model limits and what the graph can and cannot claim

## Week 7 - Similarity, Ranking, and Hashing

Status:

- source complete
- closing reading slide updated for Week 8

Known course role:

- Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation
- supports Lab 07 - Similarity, Ranking, and Hashing
- likely textbook support: Chapter 6, Chapter 12, selected Chapter 14
- expected focus: small data representation, similarity, clustering,
  recommendation, hashing, assumptions, limitations, AI/data connection

Guardrail:

- this is not a full ML course
- avoid neural network, transformer, and LLM internals
- keep examples small, visual, and explainable
- connect to AI/data foundations without overclaiming what tiny examples prove

## Week 8 - Final Synthesis and Assessment

Status:

- source complete
- no normal next-reading slide; course closes with future-reference questions

Known course role:

- Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation
- supports final synthesis and two-part final assessment
- likely textbook support: Chapter 16 - Practical Considerations; review from
  Chapter 4
- expected focus: tradeoffs, explainability, assumptions, bias, responsible AI
  use, final preparation, evidence, and explanation

Guardrail:

- this course does not use a normal capstone
- preserve the two-part final model
- do not reveal instructor-only final grading strategy in student-facing deck
- focus on explanation, justification, and evidence

---

# Required Pre-Drafting Check For Weeks 5-8

Before drafting any remaining deck source, confirm:

1. Week number and title
2. detailed reading assignment topics
3. related lab
4. related demo package, if already created
5. any changed instructional emphasis from the instructor

## Hard Reading-Alignment Gate

For Weeks 1-4, deck sources were created only after the instructor provided a
curated topic list from the assigned textbook reading.

The same constraint applies to Weeks 5-8.

Do not generate a deck source for a chosen week unless the curated reading
topic list for that week has been provided in the current working context.

If the instructor asks to create a deck source and the curated reading topic
list is missing, stop and request it before drafting.

This is required because the textbook is broader than the course and the deck
must reflect the instructor-curated reading assignment, not the textbook chapter
in full and not AI memory of the chapter.

---

# Final Governance Reminder

The deck source is not merely a content outline.

It is an instructional handoff artifact.

It should preserve:

- what students see
- what instructors need to remember
- how concepts bridge
- how demos transfer to labs
- how AI use is bounded
- how evidence supports grading
- how future instructors can recover the teaching flow

Weeks 5-8 should continue the pattern established by Weeks 1-4 unless the
instructor explicitly changes the design constraint.
