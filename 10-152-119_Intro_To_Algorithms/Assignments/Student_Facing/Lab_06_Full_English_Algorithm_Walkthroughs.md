# LAB 6 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 6 - Graphs, Paths, and Models of Real Systems**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 6 graph modeling options before creating an adjacency list or traversal
evidence.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how a real or realistic system can be represented as
nodes, edges, and traversal steps.

---

# How To Use This Artifact

For your chosen system:

1. Read the matching walkthrough.
2. Identify at least six nodes.
3. Identify at least seven edges.
4. Build an adjacency-list representation.
5. Choose BFS or DFS.
6. Trace the traversal from a selected start node.
7. Explain what your model shows and what it leaves out.

Do not copy the wording directly as your final answer. Your submitted work must
include your own system description, nodes, edges, adjacency list, diagram or
text representation, traversal evidence, limitation note, and AI-use note if
applicable.

---

# What Makes This A Graph Model?

A graph represents relationships.

Nodes are the things in the system. Edges are the connections between those
things.

Traversal means moving through the graph in a specific pattern. BFS explores
nearby nodes first. DFS follows a path deeper before backing up.

The model is useful because it makes relationships visible. The model is also
limited because it leaves out details that may matter in the real world.

---

# Scenario 1 - Workflow Steps

First, identify the steps in the workflow. For example, a support request may
move from intake to triage, assignment, investigation, resolution, review, and
closure.

Each step becomes a node.

Then identify which steps can lead to which other steps. For example, triage
may lead to assignment, escalation, or request for more information. Each
allowed movement becomes an edge.

An adjacency list stores each step and the steps that can come next.

A BFS traversal might show the closest possible next steps from the starting
point. A DFS traversal might show one possible path from beginning to end.

Questions to guide your model:

- What are the steps?
- Can any step branch to more than one next step?
- Can the workflow loop back for revision?
- What real workflow details does your model leave out?

---

# Scenario 2 - Help Desk Escalation Paths

First, identify the support levels or teams. Nodes might include intake,
desktop support, network team, security team, software team, vendor support,
and management approval.

Then identify possible escalation paths. For example, intake can send a ticket
to desktop support. Desktop support can escalate to network, security, or
software. Vendor support may connect back to software or management approval.

The adjacency list should show where each team can send the issue next.

BFS may show all nearby escalation options from intake. DFS may show one
possible escalation path until the issue reaches a final support area.

Questions to guide your model:

- Which nodes are teams, roles, or states?
- Are edges one-way or two-way?
- Which traversal best explains the situation?
- What information is missing, such as priority or time delays?

---

# Scenario 3 - Transit Stops

First, identify the stops in a small transit system. Each stop is a node.

Then identify routes between stops. If a bus or train can travel directly from
one stop to another, create an edge between those stops.

The adjacency list should show each stop and the stops directly connected to
it.

BFS is useful for finding stops that are a small number of transfers away. DFS
is useful for exploring one possible route deeply before trying another.

Questions to guide your model:

- Are route connections one-way or two-way?
- What is the start stop?
- What does the traversal order mean?
- What real transit details are missing, such as travel time or schedules?

---

# Scenario 4 - Game Map Rooms

First, identify the rooms or locations in the game map. Each room is a node.

Then identify which rooms connect by doors, paths, portals, or hallways. Each
connection is an edge.

The adjacency list should show each room and the rooms reachable directly from
it.

DFS may feel natural for exploring one path until it reaches a dead end. BFS
may feel natural for discovering all rooms within a small number of moves from
the start.

Questions to guide your model:

- Which room is the starting location?
- Are any doors locked or one-way?
- Does the graph include every room or only important rooms?
- What gameplay details does the model leave out?

---

# Scenario 5 - Course Prerequisite Relationships

First, identify courses as nodes. Each course should be a separate node.

Then identify prerequisite or concurrent relationships. If one course must be
taken before another, create an edge showing that relationship.

The adjacency list can show which courses lead into later courses, or which
prerequisites each course depends on. Be clear which direction your edges mean.

BFS might show courses reachable after completing a starting course. DFS might
follow one chain of prerequisites through the program.

Questions to guide your model:

- What does each edge direction mean?
- Are concurrent courses included?
- What course should traversal start from?
- What program details are simplified or left out?

---

# Scenario 6 - Social Or Communication Network

First, identify people, groups, or communication channels as nodes.

Then identify direct relationships. An edge may represent a direct message,
team membership, shared project, reporting line, or communication path.

The adjacency list should show who or what is directly connected.

BFS can show who is close to the starting person or group. DFS can follow one
chain of relationships deeper into the network.

Questions to guide your model:

- What does a connection mean?
- Are connections mutual or one-way?
- What traversal result is meaningful?
- What personal or privacy details should not be included?

---

# Scenario 7 - Grid Movement Map

First, define a small grid. Each cell or location can be a node.

Then define allowed movement. For example, movement may be allowed up, down,
left, and right, but not through blocked cells.

Edges connect locations that can be reached in one move.

BFS is often useful for shortest number-of-step exploration on an unweighted
grid. DFS is useful for exploring paths, but may not find the shortest path
first.

Questions to guide your model:

- Which cells are open?
- Which cells are blocked?
- What is the start node?
- What does your traversal prove or not prove?

---

# Your Turn

After reading the walkthrough for your system, build the graph in your own
words before coding.

Your next step is not to make the diagram fancy. Your next step is to make the
relationships and traversal visible enough to explain.
