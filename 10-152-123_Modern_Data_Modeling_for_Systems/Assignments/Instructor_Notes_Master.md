# Instructor Notes Master
## 10-152-123 Modern Data Modeling for Systems

Purpose: Collate instructor-facing notes from the student assignment artifacts for quick review and revision.

---

# A1 - Conceptual Model Start and Quality Revision

This assignment should remain concept-first and confidence-building.

The key teaching target is:

```text
scenario -> system intent -> entities -> relationships -> open questions -> quality revision
```

Do not let students jump to:

- formal ERD notation
- SQL
- MongoDB document design
- implementation details

Useful feedback patterns:

- Good: clear entity purpose statements, honest uncertainty, meaningful relationships.
- Improvements: vague entities, missing system intent, relationships that are really attributes, AI suggestions accepted without judgment.
- Suggestions: ask sharper modeling questions, reduce scope, explain why an entity should be kept, identify one relationship to revisit in Week 2.

---

# A2 - Relational Structure and Process Mapping

This assignment should help students move from concept-first modeling into relational structure without turning the work into SQL.

The key teaching target is:

```text
conceptual model -> attributes and keys -> relationship links -> constraints -> process-to-data map -> focused revision
```

Do not let students jump to:

- SQL syntax
- formal ERD notation as the primary deliverable
- fully normalized schema design
- implementation details

Useful feedback patterns:

- Good: clear relationship links, purposeful key candidates, process map reveals data needs, constraints written plainly.
- Improvements: attributes treated as entities, vague key candidates, process map not connected to revision, SQL syntax appearing in the model.
- Suggestions: test one system action more carefully, clarify one relationship type, add one missing constraint, preserve boundary questions for later weeks.

---

# A3 - ERD Creation and Diagramming Practice

This assignment should treat diagramming as model communication, not tool decoration.

The key teaching target is:

```text
relational structure -> ERD plan -> cardinality decisions -> visual layout -> readability review -> diagram evidence
```

Do not let students jump to:

- SQL
- tool features that hide the modeling decisions
- over-decorated diagrams
- unexamined many-to-many relationships

Useful feedback patterns:

- Good: readable diagram layout, clear cardinality labels, key assumptions documented, relationship lines match Week 2 reasoning.
- Improvements: missing key attributes, unclear cardinality, crossed lines that obscure meaning, diagram does not match the worksheet.
- Suggestions: simplify the layout, move related entities closer together, explain one assumption near the diagram, revisit one many-to-many relationship.

---

# A4 - Conceptual Modeling Refinement

This assignment should teach students that revision is a modeling skill, not a correction penalty.

The key teaching target is:

```text
prior evidence -> issue identification -> focused revision -> pattern consideration -> change log -> boundary discipline
```

Do not let students jump to:

- redesigning the entire model
- adding complexity to look advanced
- SQL
- treating every pattern as required

Useful feedback patterns:

- Good: revision is evidence-based, tradeoff is named, deferrals show scope control, pattern use is purposeful.
- Improvements: vague issue list, revision not connected to evidence, excessive redesign, quality self-assessment has no examples.
- Suggestions: narrow the revision, document one deferred question, explain why a pattern fits or does not fit, compare the revised artifact to the earlier version.

---

# A5 - Normalization and Anomaly Analysis

This assignment should make normalization concrete by tying it to maintenance risk.

The key teaching target is:

```text
model excerpt -> repeated or mixed facts -> anomaly risk -> normalization awareness -> focused recommendation
```

Do not let students jump to:

- SQL
- complete schema redesign
- memorized normal-form definitions without model evidence
- forcing all anomaly types when only one risk is visible

Useful feedback patterns:

- Good: risk is specific, cause is explained, recommendation is focused, tradeoff is acknowledged.
- Improvements: anomaly label is vague, model excerpt is too broad, recommendation redesigns too much, normalization claim is unsupported.
- Suggestions: narrow the excerpt, identify the fact being repeated, explain what could go wrong over time, name one risk of over-normalizing.

---

# A6 - Business Rules and Performance Tradeoffs

This assignment should help students see that model design includes responsibility decisions, not just entity lists.

The key teaching target is:

```text
business rule -> placement choice -> placement risk -> access pressure -> tradeoff -> human governor question
```

Do not let students jump to:

- SQL
- backend implementation
- advanced performance tuning
- treating denormalization as automatically good or bad

Useful feedback patterns:

- Good: rules are plain-English and specific, placement reasoning is defensible, tradeoff includes both benefit and risk.
- Improvements: rules are too vague, placement is asserted without reason, access pattern is not connected to the model, recommendation ignores consequences.
- Suggestions: choose one rule to analyze more deeply, name what could go wrong, defer a tradeoff if evidence is weak, add a human policy question.

---

# A7 - MongoDB Setup and Document Boundary Draft

This assignment should introduce MongoDB as a modeling choice, not as a syntax comparison.

The key teaching target is:

```text
current model area -> access patterns -> collection boundary -> embed/reference choice -> sample document -> tradeoff
```

Do not let students jump to:

- SQL versus MongoDB syntax comparisons
- full database implementation
- large multi-collection designs
- setup evidence replacing modeling evidence

Useful feedback patterns:

- Good: boundary is tied to an access pattern, sample document is inspectable, embed/reference reasoning includes risk.
- Improvements: collection boundary is arbitrary, sample document does not match the reasoning, setup evidence dominates the submission, tradeoff is missing.
- Suggestions: choose one access pattern to prioritize, simplify the sample document, explain what stays outside the document, identify possible stale data.

---

# A8 - Relational vs Document Model Comparison

This assignment should teach representation choice as contextual, not as a universal ranking of database types.

The key teaching target is:

```text
access pattern -> document option A -> document option B -> table-shaped comparison -> tradeoff -> recommendation
```

Do not let students jump to:

- SQL syntax comparisons
- "MongoDB is better" or "relational is better" claims
- choosing the simpler-looking document without update reasoning
- full implementation

Useful feedback patterns:

- Good: comparison is tied to access pattern, duplication risk is named, recommendation includes a tradeoff, both document options are inspectable.
- Improvements: options are nearly identical, relational comparison is superficial, update responsibility is ignored, recommendation is unsupported.
- Suggestions: make Option B meaningfully different, identify stale data risk, explain when the table-shaped model would still fit, add a boundary question.

---

# A9 - MongoDB CRUD and Query Evidence

This assignment should use operations as model evidence, not as isolated command practice.

The key teaching target is:

```text
document shape -> system question -> expected result -> operation evidence -> result explanation -> model insight
```

Do not let students jump to:

- disconnected command lists
- SQL comparisons
- advanced query coverage
- model changes that are not supported by operation evidence

Useful feedback patterns:

- Good: system question is clear, expected result is stated first, operation result is explained, model insight is connected to document shape.
- Improvements: operation has no system purpose, expected result is missing, result evidence is unclear, explanation only describes the command.
- Suggestions: write the question before the command, identify one field the result should show, explain what an empty result would mean, connect one result to a modeling decision.

---

# A10 - Aggregation, Performance, and Final Modeling Defense Prep

This assignment should prepare students to defend a model using selected evidence, not overwhelm them with advanced aggregation.

The key teaching target is:

```text
system question -> aggregation evidence -> performance note -> evidence selection -> draft claim -> limitation
```

Do not let students jump to:

- advanced aggregation requirements
- disconnected pipeline examples
- SQL comparisons
- final defense polish before evidence is selected

Useful feedback patterns:

- Good: aggregation supports a real system question, performance note is specific, selected evidence supports the draft claim, limitation is honest.
- Improvements: aggregation is disconnected from the claim, performance note is generic, evidence selection includes everything, limitation is missing.
- Suggestions: choose the three strongest evidence items, explain one aggregation step in plain language, name one performance concern, soften an overclaim.

---

# Capstone Modeling Defense

This capstone should assess whether students can assemble and defend a coherent model, not whether they can build a production database.

The key teaching target is:

```text
pathway choice -> evidence index -> scope -> visual model -> rules -> representation evidence -> defense claim -> limitation -> AI disclosure
```

Do not let students jump to:

- SQL
- production implementation
- unsupported claims about database superiority
- hiding AI-generated design work
- submitting a pile of prior artifacts without a capstone evidence index

Useful feedback patterns:

- Good: evidence index is complete, design claim is supported, limitations are honest, AI disclosure shows verification and ownership.
- Improvements: scope is too broad, visual model is hard to inspect, relational/document consideration is superficial, final claim overreaches.
- Suggestions: narrow the system boundary, identify the three strongest evidence items, add one missing business rule, clarify what AI helped with and what the student personally verified.
