# Three Classifications of AI Use: Assistance, Collaboration, and Embedded Systems

## Introduction

Artificial intelligence is often discussed as though “using AI” were a single kind of activity.

In practice, people interact with AI in very different ways depending on the task, the amount of work the AI performs, and how deeply the AI is integrated into the tools being used.

A useful starting point is to distinguish three broad classifications of AI use:

- **AI Assistance**
- **AI Enabled / Collaboration**
- **AI Embedded**

These classifications are not rigid technical standards. They are practical mental models that help describe how AI participates in human work.

They are easiest to understand separately first. In actual use, however, their boundaries often overlap.

---

## 1. AI Assistance

AI Assistance describes situations in which AI primarily supports human thinking, understanding, analysis, or reflection.

The Human User remains the primary actor.

Typical examples include:

- asking for term definitions;
- conducting research;
- summarizing documents or artifacts;
- explaining code;
- analyzing a block of code at a high level;
- brainstorming application ideas;
- exploring alternative designs;
- reframing a problem;
- receiving feedback during intellectual or personal reflection.

In this mode, the AI generally does not own or independently execute the work.

A useful shorthand is:

**AI advises. You decide.**

### Example

A developer may paste a Python function into an AI interface and ask:

“Explain what this function does and identify any areas I should examine more closely.”

The AI provides understanding and analysis, but the developer remains responsible for deciding what to change.

---

## 2. AI Enabled / Collaboration

AI Enabled or Collaborative use involves a more interactive working relationship.

The AI contributes directly to creating, modifying, designing, or completing targeted portions of the work.

Examples include:

- generating code snippets;
- designing database structures;
- developing application architecture;
- implementing individual features;
- generating tests;
- debugging iteratively;
- creating portions of an application;
- helping build an entire application through sustained collaboration;
- performing targeted task completion.

The key distinction is that AI is no longer only explaining or advising.

It is **participating in the work itself**.

A useful shorthand is:

**AI works with you.**

The Human User still provides goals, context, constraints, review, and final authority.

In more mature Human–AI collaboration, governance approaches such as Refraction-Based Architecture can help establish clearer Reality Context, permission boundaries, feedback, and realization control.

---

## 3. AI Embedded

AI Embedded describes situations in which AI capability is integrated directly into an application, platform, or workflow.

The user may primarily interact with the application rather than with a separate AI interface.

Examples include:

- AI capabilities inside presentation software;
- AI writing or editing assistance inside document software;
- intelligent features embedded in business applications;
- automated workflow assistance;
- embedded coding agents;
- single-agent systems operating within an application;
- multi-agent systems coordinating beneath the visible interface.

A useful shorthand is:

**AI works within the system.**

The degree of capability can vary dramatically.

One embedded AI feature may simply suggest wording or formatting.

Another may inspect documents, perform multiple tasks, use tools, coordinate agents, and modify application state.

Therefore, “embedded” describes **where and how AI is integrated**, not necessarily how powerful or autonomous it is.

---

## The Boundaries Are Not Hard

Although these classifications are useful for teaching and orientation, real AI use frequently moves across them.

A single workflow might begin with Assistance:

- research a topic;
- summarize requirements;
- explore possible approaches.

It may then become Collaborative:

- design the solution;
- generate code;
- iterate on implementation.

Finally, the completed solution may itself contain Embedded AI:

- an AI assistant inside the application;
- an agentic workflow;
- a multi-agent subsystem.

The classifications therefore describe recognizable regions rather than rigid boundaries.

One interaction can also change modes over time.

A conversation that begins with:

“Explain this concept.”

may eventually become:

“Help me design the feature.”

and later:

“Modify these files after I approve the proposed changes.”

The AI relationship has shifted even though the underlying model or interface may not have changed.

---

# A Second Lens: Agency and Integration

The three classifications become easier to understand when viewed through two additional dimensions.

## AI Agency / Operational Autonomy

This dimension describes how much initiative the AI takes.

At low agency, AI primarily responds with information, explanation, or suggestions.

At higher agency, AI may:

- make decisions;
- choose steps;
- use tools;
- execute tasks;
- continue multi-step work;
- coordinate other agents.

## Application Integration

This dimension describes how deeply AI capability is built into an application or workflow.

At low integration, the AI exists largely outside the target application.

At high integration, the AI operates within the application, workspace, or workflow itself.

These dimensions are independent.

A highly collaborative AI may have high agency but little application integration.

A deeply embedded AI feature may have high integration but very little agency.

---

## The 2×2 Model

This creates four useful regions.

### Low Agency / Low Integration

Typical examples:

- definitions;
- explanations;
- summarization;
- research;
- reflection;
- basic code analysis.

This region aligns strongly with **AI Assistance**.

### High Agency / Low Integration

Typical examples:

- code generation;
- database design;
- detailed application development;
- targeted task execution;
- sophisticated AI collaboration outside the target application.

This region aligns strongly with **AI Enabled / Collaboration**.

### Low Agency / High Integration

Typical examples:

- embedded grammar suggestions;
- document recommendations;
- simple application-level summaries;
- narrow AI helpers inside software.

These systems are clearly **AI Embedded**, even though their agency may be limited.

### High Agency / High Integration

Typical examples:

- agentic systems embedded inside applications;
- AI that can inspect and modify workspace artifacts;
- autonomous workflows;
- sophisticated AI copilots;
- multi-agent systems operating beneath an application interface.

This region often combines characteristics of both **AI Enabled / Collaboration** and **AI Embedded**.

---

# Where the Three Classifications Fit

The three classifications therefore should not be treated as isolated boxes.

They occupy overlapping regions on the Agency × Integration model.

**AI Assistance** tends to cluster around lower agency and lower integration.

**AI Enabled / Collaboration** extends toward greater agency and can occur across several levels of integration.

**AI Embedded** primarily occupies the higher-integration region but may range from very low agency to highly autonomous multi-agent systems.

This explains why classification sometimes feels ambiguous.

The ambiguity is not necessarily a weakness in the model.

It reflects the fact that AI use is multidimensional.

The three classifications simplify that complexity enough to make it understandable, while the Agency × Integration model reveals why the boundaries become gray in practice.

---

# Why the Classification Matters

The purpose of these classifications is not to decide which form of AI use is “best.”

Each mode can be appropriate.

The important question is:

**What relationship with AI best fits this particular task?**

A definition may require only Assistance.

Application development may benefit from Collaboration.

A business workflow may justify Embedded AI.

More capability is not automatically better.

More autonomy is not automatically better.

More integration is not automatically better.

The appropriate level depends on:

- the goal;
- the context;
- the consequences of error;
- the authority granted to the AI;
- the ability of the Human User to review the result;
- the amount of operational autonomy appropriate for the task.

---

# Human Responsibility Remains

Across all three classifications, the Human User retains responsibility for how AI is employed.

That includes the responsibility to:

- understand what the AI is being asked to do;
- provide sufficient context;
- establish appropriate boundaries;
- review important outputs;
- verify results;
- observe and record relevant evidence;
- determine whether AI involvement is appropriate for the task.

The nature of Human–AI interaction may change.

Human responsibility does not disappear.

---

# Closing Mental Model

A simple first model is:

**AI Assistance** — AI supports your thinking.

**AI Enabled / Collaboration** — AI works with you.

**AI Embedded** — AI works within the system.

A more realistic model adds two dimensions:

**How much operational autonomy does the AI have?**

and

**How deeply is the AI integrated into the application or workflow?**

Together, these models provide a practical way to understand modern AI use without pretending that the boundaries are absolute.

The classifications are useful.

The boundaries are gray.

The Human User remains responsible for choosing the right level of AI for the work.