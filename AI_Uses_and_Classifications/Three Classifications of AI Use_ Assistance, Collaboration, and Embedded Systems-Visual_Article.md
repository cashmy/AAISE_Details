# Three Classifications of AI Use: Assistance, Collaboration, and Embedded Systems

## Introduction

“Using AI” is often discussed as though it were a single type of activity.

In practice, Human–AI interaction can take very different forms depending on what the Human User is trying to accomplish, how much work the AI performs, and how deeply AI capability is integrated into the tools or applications being used.

A useful starting point is to distinguish three broad classifications:

- **AI Assistance**
- **AI Enabled / Collaboration**
- **AI Embedded**

These are not rigid technical standards, nor are they levels in a maturity hierarchy. They are practical classifications that describe different relationships among the Human User, the AI, and the work being performed.

They are easiest to learn separately first.

In actual use, however, the boundaries frequently overlap.

---

## Figure 1 — Three Classifications of AI Use

**[PLACE FIGURE 1 HERE]**

*Figure 1. Three classifications of AI use. These categories describe different relationships among the Human User, AI, and the work rather than levels of AI maturity or quality.*

A useful shorthand is:

**AI Assistance — AI supports your thinking.**

**AI Enabled / Collaboration — AI works with you.**

**AI Embedded — AI works within the system.**

---

# AI Assistance

AI Assistance describes situations in which AI primarily supports human understanding, analysis, reflection, or decision-making.

The Human User remains the primary actor.

The AI may explain, summarize, research, reframe, compare, or provide feedback, but it is not primarily responsible for performing the work itself.

Common examples include:

- term definitions;
- research and information gathering;
- summarizing documents or artifacts;
- explaining concepts;
- analyzing code at a high level;
- reviewing a code block;
- brainstorming;
- high-level application design;
- reflective journaling;
- receiving feedback on intellectual or emotional processing;
- exploring alternative interpretations or perspectives.

In software development, this might involve asking:

> “Explain what this Python function does and identify anything I should examine more closely.”

The AI contributes analysis and understanding.

The Human User decides what, if anything, should happen next.

### Working Mental Model

**AI advises. You decide.**

---

# AI Enabled / Collaboration

AI Enabled or Collaborative use involves a more interactive relationship in which the AI contributes directly to creating, modifying, designing, or completing targeted portions of the work.

The Human User is still responsible for the goal, context, constraints, review, and authority over the final outcome.

However, the AI is now participating in the work rather than merely commenting on it.

Examples include:

- generating code snippets;
- creating functions or components;
- designing database schemas;
- assisting with database implementation;
- detailed application architecture;
- generating tests;
- debugging collaboratively;
- building features;
- refactoring;
- producing structured artifacts;
- completing targeted tasks;
- helping develop an entire application through sustained interaction.

This mode often involves iteration:

**Human context → AI contribution → Human review → Feedback → revised AI contribution**

The relationship is closer to co-production than consultation.

In sophisticated application development, governance methods such as Refraction-Based Architecture can help preserve context, authority, feedback, and realization boundaries throughout this interaction.

### Working Mental Model

**AI works with you.**

---

# AI Embedded

AI Embedded describes situations in which AI capability is integrated directly into an application, platform, workflow, or product.

The Human User primarily interacts with the application itself.

The AI operates inside or beneath that environment.

Examples include:

- AI functionality inside presentation software;
- writing or editing assistance inside document applications;
- AI features within spreadsheets;
- intelligent application-level recommendations;
- AI workflow automation;
- embedded coding agents;
- single-agent application features;
- multi-agent systems operating beneath a visible application interface.

One important distinction is that **Embedded does not automatically mean highly autonomous**.

A simple grammar suggestion can be deeply integrated into an application while exercising almost no independent agency.

A sophisticated multi-agent system may also be deeply integrated while performing substantial autonomous work.

“Embedded” therefore primarily describes **where AI operates relative to the application or workflow**, not how powerful the AI is.

### Working Mental Model

**AI works within the system.**

---

# In Practice, the Boundaries Overlap

The three classifications are useful because they simplify Human–AI interaction into recognizable modes.

Reality is less tidy.

A single interaction or project may move between all three.

---

## Figure 2 — In Practice, the Boundaries Overlap

**[PLACE FIGURE 2 HERE]**

*Figure 2. AI use frequently crosses classification boundaries. A single workflow may move between Assistance, Collaboration, and Embedded operation as the nature of the work changes.*

For example, an application-development workflow might begin with AI Assistance:

- research a technology;
- summarize requirements;
- explain an unfamiliar concept;
- compare architectural options.

It may then move into AI Enabled / Collaboration:

- design the database;
- generate code;
- create tests;
- implement a feature;
- iterate on the design.

The final application may itself contain AI Embedded capability:

- an in-app assistant;
- an agentic workflow;
- an automated AI feature;
- a multi-agent subsystem.

The classification changes because the **relationship between the Human User, AI, and work changes**.

The underlying model may even remain the same.

### A Conversation Can Change Modes

Consider the sequence:

> “Explain this concept.”

That is primarily Assistance.

Later:

> “Help me design this feature and generate a first implementation.”

The interaction has moved toward Collaboration.

Later still:

> “Inspect the project, summarize what must change, ask for approval, and then update the files.”

The AI is operating much more agentically against the working environment.

These modes are therefore best understood as **recognizable operating regions rather than hard boundaries**.

> **A single Human–AI interaction can change classification as the nature of the work changes.**

---

# A Second Lens: Agency and Integration

The overlap becomes easier to understand when the three classifications are examined using two independent dimensions.

The first is **AI Agency / Operational Autonomy**.

The second is **Application Integration**.

These dimensions explain why two AI systems can belong to the same broad classification while behaving very differently.

---

## Figure 3 — Agency × Integration

**[PLACE FIGURE 3 HERE]**

*Figure 3. AI Agency / Operational Autonomy and Application Integration are independent dimensions. An AI system can exercise substantial operational autonomy without being deeply embedded, or be deeply integrated while exercising very little autonomy.*

> **More integration does not automatically mean more agency. More agency does not require deeper integration.**

---

## AI Agency / Operational Autonomy

AI Agency / Operational Autonomy describes how much initiative the AI can exercise while accomplishing a task.

At lower agency, the AI primarily responds to Human requests.

Typical behavior includes:

- answering questions;
- explaining;
- summarizing;
- suggesting;
- comparing.

At higher agency, the AI may:

- select intermediate steps;
- use tools;
- inspect files;
- execute commands;
- modify artifacts;
- continue multi-step work;
- coordinate specialized agents;
- make operational decisions within defined boundaries.

This dimension concerns **how much the AI can act**, not where it is located.

---

## Application Integration

Application Integration describes how deeply AI capability is built into the application or workflow being used.

At low integration, AI may operate externally.

For example:

- a browser conversation;
- a separate AI coding interface;
- an external research assistant.

At high integration, AI operates directly within the application environment.

For example:

- AI inside a word processor;
- AI inside presentation software;
- an embedded application assistant;
- an AI subsystem operating beneath a product interface.

This dimension concerns **where and how AI participates in the system**, not how autonomous it is.

---

# The Four Agency × Integration Regions

The two dimensions create four useful regions.

## Low Agency / Low Integration

Typical examples include:

- definitions;
- summarization;
- research;
- explanations;
- reflection;
- brainstorming;
- simple code analysis.

AI primarily provides information or insight.

This region strongly aligns with **AI Assistance**.

---

## High Agency / Low Integration

Typical examples include:

- generating substantial code;
- database design;
- detailed application development;
- targeted task completion;
- sophisticated collaborative work performed outside the target application.

AI may perform substantial work even though it is not deeply integrated into the final application.

This region strongly aligns with **AI Enabled / Collaboration**.

---

## Low Agency / High Integration

Typical examples include:

- embedded grammar suggestions;
- spelling correction;
- application-level recommendations;
- simple summaries inside an application;
- narrow AI helpers.

These systems are clearly **AI Embedded**, even though their agency may be limited.

---

## High Agency / High Integration

Typical examples include:

- embedded agentic systems;
- AI capable of inspecting and modifying application artifacts;
- sophisticated application copilots;
- autonomous workflows;
- multi-agent systems;
- end-to-end AI-driven processes operating inside an application.

This region often contains substantial overlap between **AI Enabled / Collaboration** and **AI Embedded**.

---

# Where the Three Classifications Fit

The three classifications are therefore not isolated boxes.

They occupy recognizable but overlapping regions across the Agency × Integration dimensions.

---

## Figure 4 — Where the Classifications Fit on the Grid

**[PLACE FIGURE 4 HERE]**

*Figure 4. AI Assistance, AI Enabled / Collaboration, and AI Embedded occupy recognizable but overlapping regions on the Agency × Integration model. Their boundaries are intentionally gray because real Human–AI interaction compresses multiple dimensions into simplified categories.*

AI Assistance tends to cluster around lower agency and lower integration.

AI Enabled / Collaboration occupies a much broader range of agency and can exist at several levels of integration.

AI Embedded primarily occupies areas of higher application integration, but may range from very low agency to highly autonomous multi-agent operation.

This explains why classification sometimes feels ambiguous.

The ambiguity is not necessarily a weakness.

It reflects the underlying multidimensional nature of AI use.

> **The categories are simplified descriptions of Reality, not replacements for Reality.**

---

# Why the Classification Matters

The purpose of the model is not to determine which type of AI use is best.

There is no inherent progression in which Embedded AI is superior to Assistance, or highly agentic AI is automatically preferable to low-agency AI.

The appropriate mode depends upon the work.

A term definition may require nothing more than Assistance.

Detailed software development may benefit from Collaboration.

A persistent business process may justify Embedded AI.

The better question is:

> **What relationship with AI is appropriate for this part of the work?**

Consider:

- What is the goal?
- What Reality Context does the AI have?
- How much operational autonomy is useful?
- How much application integration is required?
- What happens if the AI is wrong?
- What authority has the Human User granted?
- Can the Human User meaningfully review the outcome?
- Does the task require explanation, collaboration, execution, or embedded capability?

Choosing the right mode is more important than maximizing AI capability.

---

# Human Responsibility Across All Three Modes

The Human–AI relationship changes across Assistance, Collaboration, and Embedded operation.

Human responsibility does not disappear.

The Human User remains responsible for:

- establishing the goal;
- supplying sufficient context;
- determining appropriate AI involvement;
- defining relevant constraints;
- setting permission boundaries;
- reviewing consequential outputs;
- testing and verifying results;
- identifying what changed;
- ensuring requirements are met;
- observing and recording appropriate evidence;
- standing behind the resulting work.

As AI agency and integration increase, these responsibilities may become more important rather than less important.

> **Capability does not remove Human responsibility. It changes what Human responsibility must govern.**

---

# A Practical Mental Model

For introductory use:

### AI Assistance
**AI supports your thinking.**

### AI Enabled / Collaboration
**AI works with you.**

### AI Embedded
**AI works within the system.**

For deeper analysis, ask two additional questions:

### How much operational autonomy does the AI have?

### How deeply is the AI integrated into the application or workflow?

Together, these models allow AI use to be described without pretending that every Human–AI interaction fits perfectly inside a rigid category.

---

# Conclusion

Artificial intelligence is not used in only one way.

Sometimes AI explains.

Sometimes it collaborates.

Sometimes it operates within the systems people use.

And increasingly, a single workflow may move among all three.

The three classifications provide an accessible starting point:

**Assistance → Collaboration → Embedded**

The Agency × Integration model reveals the deeper structure beneath them.

The important lesson is not to force every AI use case into one perfectly defined box.

It is to understand:

- what the AI is doing;
- how much autonomy it has;
- where it operates;
- what relationship it has to the Human User;
- and who remains responsible for the realized outcome.

The classifications are useful.

The boundaries are gray.

**The Human User remains responsible for choosing the right level of AI for the work.**