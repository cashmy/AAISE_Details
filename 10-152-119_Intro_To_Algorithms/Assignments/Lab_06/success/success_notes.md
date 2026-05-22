# LAB 06 SUCCESS NOTES - GRAPH TRAVERSAL AND MODELING

This package shows one acceptable successful version for Lab 06. It is not the
only correct answer because the student-facing lab allows multiple real or
realistic systems.

---

# Assumptions

- fresh `Assignments/Lab_06/` package
- student-facing Lab 06 treated as authoritative
- generic starter rather than scenario-specific scaffolding
- demo scenario different from the withheld success-version system
- text diagram, adjacency list, and traversal tables used as the main evidence
- primary success version kept plain and focused on required behavior

---

# Chosen System

Help desk escalation workflow

This successful version models the workflow as a directed graph where steps are
nodes and possible next steps are edges.

This stays in the same concept family as the lab while remaining different from
the campus-route demo.

---

# Problem Statement

Represent a help desk escalation workflow as a graph, show the adjacency-list
representation, and compare traversal behavior from a chosen start node.

The successful version includes both BFS and DFS evidence so the difference in
traversal order is easy to inspect.

---

# Inputs and Outputs

## Inputs

- seven workflow nodes
- directed edges showing the possible escalation paths
- a selected start node for traversal

## Outputs

- adjacency-list representation
- text diagram of the workflow
- BFS traversal evidence
- DFS traversal evidence
- explanation of what changes when the start node or traversal method changes
- statement of what the model leaves out

---

# Evidence Included

`success_solution.py` prints:

- a workflow diagram in text form
- an adjacency list for the directed graph
- a BFS traversal table with queue state and visited nodes
- a DFS traversal table with stack state and visited nodes
- a short comparison note about traversal method and start-node changes
- a model-limit note

This aligns to the student-facing requirement for nodes, edges, adjacency list,
diagram or text representation, traversal evidence, comparison or explanation,
and model limitation.

---

# Interpretation

- BFS and DFS visit the same workflow graph in different orders
- starting at `Request Received` shows the whole workflow path outward from the
  beginning
- starting at `Escalate` skips earlier steps and highlights only the later part
  of the model
- the graph is useful for showing relationships and reachability, but it is not
  a full simulation of real help desk work

---

# Model Limit Note

This graph leaves out timing, priority, repeated loops, human judgment, and the
reasons one branch might be chosen instead of another. It is a useful model of
possible paths, not a complete description of the real system.

---

# AI-Use Accountability Example

Lab 06 allows AI for explanation or critique after the student has drafted the
graph.

Example disclosure a student could make:

> After drafting my adjacency list and diagram, I asked AI to check whether they
> matched. AI pointed out one missing edge from an escalation step to the final
> resolution node. I verified that mismatch myself, fixed the graph, and then
> reran the traversal to make sure the output still matched the revised model.

---

# Rubric Categories Illustrated

- `T2` Data Structures and Representation
- `T5` Observable Algorithm Behavior and Communication Evidence
- `T1` Problem Framing and Algorithmic Analysis
- `T3` Algorithm Implementation and Testing
- `T4` Correctness, Efficiency, and Tradeoff Evaluation
- `T6` Responsible AI/tool-use disclosure, if the optional AI note is used
- `C1` Solve Problems
- `C2` Communicate Clearly