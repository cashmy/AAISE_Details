# Week 06 Deck Source - Graph Traversal and Modeling

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 6 |
| Phase / Unit | Unit 3 - Strategy Patterns and Observable Behavior |
| Lecture Title | Modeling Connected Things |
| Related Lab | Lab 06 - Graph Traversal and Modeling |
| Related Demo | Campus Route Map Traversal |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students learn how graphs model connected parts of a system and how traversal
algorithms make movement through those connections visible.

The goal is not to master graph theory formulas. The goal is to represent a
small real or realistic system as nodes and edges, create an adjacency list,
run or simulate BFS or DFS, and explain what the model shows and what it leaves
out.

---

# Possible Two-Session Split

The Week 6 reading includes graph basics, network theory language, traversal
algorithms, optional centrality material, and social network analysis context.
This can be taught as one longer lecture with breaks, but a two-session split
may reduce overload.

## Session A - Graph Models and Network Vocabulary

Recommended slides:

- 1-4: review and opening frame
- 5-10: textbook review and formula posture
- 11-20: graph terms, representation, mechanics, and types
- 21-27: ego networks, neighborhoods, shortest path, and optional metrics

Session A target:

Students can name nodes, edges, graph types, neighborhoods, and model limits in
plain language.

## Session B - Traversals, Demo, and Lab Transfer

Recommended slides:

- 28-34: BFS, DFS, traversal evidence, and neighbor-order effects
- 35-38: optional network analysis context and social network analysis
- 39-42: demo
- 43-46: lab bridge
- 47-50: wrap-up

Session B target:

Students can produce and explain traversal evidence for a small graph model.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook Ch. 5 | Graph algorithm overview | Frames graph representation, network analysis, traversal, case study, and neighborhoods |
| Textbook Ch. 5 | Graph representation | Core model-building focus |
| Textbook Ch. 5 | Graph basics: vertices/nodes, edges/links, network | Required vocabulary |
| Textbook Ch. 5 | Graph mechanics and types: simple, directed, undirected, weighted | Required recognition and model choice |
| Textbook Ch. 5 | Ego-centered networks: ego nets, one-hop, two-hop, beyond | Brief required treatment for neighborhood thinking |
| Textbook Ch. 5 | Shortest path and neighborhoods | Required conceptual treatment |
| Textbook Ch. 5 | Optional centrality material: triangles, density, degree, betweenness, closeness, eigenvector centrality | Recognition / instructor reserve |
| Textbook Ch. 5 | Optional Python centrality examples and graph visualization | Optional reference only |
| Textbook Ch. 5 | Social network analysis | Optional context only |
| Textbook Ch. 5 | BFS and DFS with examples | Required traversal focus |
| Textbook Ch. 5 | Fraud detection case study and fraud analytics | Skipped |
| Course artifact | Lab 06 - Graph Traversal and Modeling | Student graph model and traversal evidence |
| Course artifact | Lab 06 Demo Notes | Instructor demo bridge |

---

# Textbook Review

The reading introduces graphs as a way to represent connected things.

In everyday language, words like "network," "node," "edge," and "neighbor" may
feel familiar. In graph work, those words become more precise. A network is not
just "a bunch of connected stuff." It is a model made of defined parts and
defined relationships.

The reading also includes formulas and metrics that are more advanced than
students need for Lab 06. Those formulas are worth noticing, but they should
not become the center of this week. The live work focuses on representation,
adjacency lists, BFS, DFS, traversal evidence, and model limits.

## Reading Key Ideas

- Graphs represent relationships.
- Nodes or vertices are the things being connected.
- Edges or links are the connections between them.
- Graphs may be directed, undirected, simple, or weighted.
- A neighborhood describes what is near a node by connection.
- BFS explores outward by layers.
- DFS follows a path deeply before backtracking.
- Network metrics can describe structure, but they do not tell the whole story.

## Terms To Carry Forward

| Term | General Meaning | Graph / Network Meaning |
| --- | --- | --- |
| Network | Any connected system | A graph model of connected nodes and edges |
| Node | A point or object | A specific item in the graph |
| Vertex | A corner or point | Another term for node |
| Edge | Outside boundary | A relationship or connection between nodes |
| Link | A connection | Another term for edge |
| Neighbor | Something nearby | A node directly connected to another node |
| Path | A route | A sequence of connected nodes |
| Traversal | Moving through something | Visiting graph nodes using an algorithm |
| Centrality | Importance | A metric estimating structural importance |
| Density | How compact something is | How many possible connections actually exist |

## What We Will Use Today

- graph vocabulary
- directed, undirected, simple, and weighted graph recognition
- adjacency-list representation
- neighborhoods and shortest-path intuition
- BFS and DFS traversal
- queue and stack state as evidence
- model-limit explanation

## What We Will Revisit Later

- similarity and recommendation
- ranking and centrality ideas
- AI/data relationship modeling
- explainability and limits of graph-based claims
- optional social network analysis context

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain a graph as a model of connected things.
2. Identify nodes, edges, neighbors, paths, and graph types.
3. Represent a small system with an adjacency list.
4. Trace BFS or DFS using visible evidence.
5. Explain how traversal order depends on method, start node, and neighbor order.
6. State what a graph model leaves out.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from strategy comparison to connected-system modeling |
| Textbook Review | 5-10 | Core | Curate graph reading and protect against formula overload |
| Graph Basics and Representation | 11-20 | Core | Define graph vocabulary and graph types |
| Network Analysis Orientation | 21-27 | Core / Optional | Introduce neighborhoods, shortest paths, ego nets, and metrics as recognition |
| Graph Traversals | 28-34 | Core | Teach BFS, DFS, traversal evidence, and neighbor-order effects |
| Optional Network Context | 35-38 | Optional / Reserve | Place centrality and SNA in context without requiring mastery |
| Demo Bridge | 39-42 | Core | Model campus routes and compare BFS/DFS |
| Lab Bridge | 43-46 | Core | Connect demo to Lab 06 requirements |
| Wrap-Up | 47-50 | Core | Consolidate and assign next action |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 05 Taught Us

**Delivery Category:** Core

**Slide Text:**

In Lab 05, strategy choice depended on problem shape.

You compared:

- correctness
- readability
- growth
- fit to data
- limitations

**Instructor Notes:**

Use one student-safe example if available. The bridge is that strategy depends
on representation. Week 6 begins with a representation choice: model the system
as connected parts.

**Transition Cue:**

This week, the shape we care about is connection.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

How can we model connected parts so an algorithm can move through them?

**Instructor Notes:**

Let students name connected systems: maps, workflows, course prerequisites,
social networks, game rooms, web pages, file dependencies.

The goal is to make "connection" concrete enough to represent and traverse.

**Transition Cue:**

That model is called a graph.

---

## Slide 3 - Graphs Model Relationships

**Delivery Category:** Core

**Slide Text:**

A graph is a model of connected things.

It can represent:

- places connected by routes
- tasks connected by dependencies
- people connected by communication
- steps connected in a workflow
- rooms connected by paths

**Instructor Notes:**

Emphasize "model." A graph is not the full real system. It is a simplified
representation that highlights relationships.

This is the primary Week 6 mental model.

**Transition Cue:**

A model helps us see, but it also leaves things out.

---

## Slide 4 - Success Today

**Delivery Category:** Core

**Slide Text:**

Today you should be able to:

- define nodes and edges
- build an adjacency list
- trace BFS or DFS
- explain traversal evidence
- name what the graph leaves out

**Instructor Notes:**

This mirrors Lab 06. Students do not need advanced centrality calculations for
success. They need a clear graph model and visible traversal behavior.

**Transition Cue:**

Now anchor the lesson in the reading.

---

# Textbook Review

## Slide 5 - Textbook Review: Graph Algorithm Overview

**Delivery Category:** Core

**Slide Text:**

The reading covers:

1. graph representation
2. network theory analysis
3. graph traversals
4. case study
5. neighborhood techniques

**Instructor Notes:**

Tell students that not all areas receive equal depth. Representation and
traversal are the core for this course week. Network metrics are mostly
recognition and optional context.

**Transition Cue:**

The first reading challenge is vocabulary.

---

## Slide 6 - Textbook Review: Terms Become Precise

**Delivery Category:** Core

**Slide Text:**

Some familiar words become technical:

- network
- node
- edge
- neighbor
- path
- traversal
- density
- centrality

Use the graph meaning during this lesson.

**Instructor Notes:**

This slide responds to the risk that students will use everyday meanings too
loosely. The lesson should repeatedly ask: "What does this term mean in the
graph model?"

**Transition Cue:**

The reading also includes formulas.

---

## Slide 7 - Textbook Review: Do Not Panic Over Formulas

**Delivery Category:** Core

**Slide Text:**

The reading includes advanced graph formulas.

For this week:

- notice the term
- read for the idea
- connect it to a simple graph
- do not try to master every formula

**Instructor Notes:**

Be explicit: some formulas are complex and advanced. Students should not treat
formula mastery as the Week 6 goal.

The practical goal is graph representation, BFS/DFS traversal, and explanation.

**Transition Cue:**

The required core begins with graph basics.

---

## Slide 8 - Textbook Review: Graph Basics

**Delivery Category:** Core

**Slide Text:**

Core graph pieces:

- vertices or nodes
- edges or links
- network structure
- simple, directed, undirected, weighted types

**Instructor Notes:**

Tie each term to a tiny example. For a campus map, buildings are nodes and
sidewalks are edges.

**Transition Cue:**

The reading also discusses neighborhoods and ego-centered networks.

---

## Slide 9 - Textbook Review: Neighborhoods

**Delivery Category:** Core

**Slide Text:**

A neighborhood asks:

- what is directly connected?
- what is one hop away?
- what is two hops away?
- what can be reached from here?

**Instructor Notes:**

Use "hop" as a friendly bridge. One-hop neighbors are directly connected.
Two-hop nodes are reachable through one intermediate node.

This prepares BFS.

**Transition Cue:**

The required traversal section is the main lab bridge.

---

## Slide 10 - Textbook Review: Traversals

**Delivery Category:** Core

**Slide Text:**

The reading introduces:

- breadth-first search (BFS)
- depth-first search (DFS)
- traversal order
- specific searches using traversal

**Instructor Notes:**

Frame BFS and DFS as ways to move through the graph. They are not just code
recipes. They produce visible behavior that can be traced.

**Transition Cue:**

Start with the basic pieces of the model.

---

# Graph Basics and Representation

## Slide 11 - Node Or Vertex

**Delivery Category:** Core

**Slide Text:**

A node is one thing in the graph.

Examples:

- building
- person
- task
- course
- web page
- game room

Vertex is another term for node.

**Instructor Notes:**

Use both words because the textbook may use vertex. For students, "node" will
probably be friendlier.

**Transition Cue:**

Nodes matter because edges connect them.

---

## Slide 12 - Edge Or Link

**Delivery Category:** Core

**Slide Text:**

An edge is a connection between nodes.

Examples:

- sidewalk between buildings
- prerequisite relationship
- communication link
- workflow transition
- door between rooms

**Instructor Notes:**

Ask students to distinguish the node from the edge in two examples. This
prevents a common confusion where students list things but not relationships.

**Transition Cue:**

Together, nodes and edges form a graph.

---

## Slide 13 - Network

**Delivery Category:** Core

**Slide Text:**

In graph work, a network means:

- defined nodes
- defined edges
- a model of relationships

It does not mean "everything about the real system."

**Instructor Notes:**

This is a key term distinction. A real campus has distances, weather, stairs,
doors, crowds, and accessibility. A graph may choose to model only direct
routes.

**Transition Cue:**

Different graph types model different relationship rules.

---

## Slide 14 - Simple Graph

**Delivery Category:** Core

**Slide Text:**

A simple graph usually avoids:

- duplicate edges
- self-loops
- extra edge complexity

It is often a good beginner model.

**Instructor Notes:**

Keep this practical. A simple graph is enough for most Lab 06 submissions.

If students ask about self-loops, explain that a node connecting to itself is
possible in graph theory but usually not needed for the lab.

**Transition Cue:**

Some relationships have direction.

---

## Slide 15 - Directed Graph

**Delivery Category:** Core

**Slide Text:**

A directed graph has one-way relationships.

Examples:

- course prerequisite
- workflow step
- escalation path
- one-way route

Direction changes what can be reached.

**Instructor Notes:**

Use a prerequisite example: Course A can lead to Course B, but Course B does
not lead backward to Course A.

This prepares the lab option on prerequisites and workflows.

**Transition Cue:**

Other relationships work both ways.

---

## Slide 16 - Undirected Graph

**Delivery Category:** Core

**Slide Text:**

An undirected graph has two-way relationships.

Examples:

- sidewalk between buildings
- hallway between rooms
- mutual connection
- two-way transit route

**Instructor Notes:**

Make clear that undirected edges usually need to appear in both directions if
represented as an adjacency list.

This is a major Lab 06 watch-for.

**Transition Cue:**

Some edges also carry a cost or value.

---

## Slide 17 - Weighted Graph

**Delivery Category:** Core / Optional

**Slide Text:**

A weighted graph adds a value to edges.

Weights may represent:

- distance
- time
- cost
- risk
- strength of connection

**Instructor Notes:**

Keep this recognition-level unless students are ready. Lab 06 does not require
weighted path algorithms.

Emphasize that if a model does not include weights, it cannot claim shortest
time or lowest cost.

**Transition Cue:**

Now we need a practical way to store graph connections.

---

## Slide 18 - Adjacency List

**Delivery Category:** Core

**Slide Text:**

An adjacency list stores each node with its neighbors.

Example:

```text
Parking: Library, Student Center
Library: Parking, Science Hall, Cafeteria
```

**Instructor Notes:**

This is one of the most important implementation slides. Students should be
able to read the adjacency list as "from this node, these neighbors are
directly reachable."

**Transition Cue:**

The adjacency list should match the diagram.

---

## Slide 19 - Diagram And Adjacency List Must Agree

**Delivery Category:** Core

**Slide Text:**

Check the model both ways:

- Does every diagram connection appear in the adjacency list?
- Does every adjacency-list connection appear in the diagram?
- Are directed edges shown clearly?
- Are two-way edges listed both ways?

**Instructor Notes:**

This is a practical debugging slide. Students often draw a graph and write an
adjacency list that do not match.

This is also a good AI-assisted critique use case after the student drafts the
model.

**Transition Cue:**

Before traversing, ask what the model leaves out.

---

## Slide 20 - A Graph Is A Model

**Delivery Category:** Core

**Slide Text:**

A graph may leave out:

- distance
- time
- priority
- capacity
- direction
- human judgment
- real-world messiness

A model is useful, but incomplete.

**Instructor Notes:**

This is core to Lab 06. Students must include what their graph leaves out.

Connect this to professional honesty: a model can be useful without being
complete.

**Transition Cue:**

Now use graph vocabulary to talk about neighborhoods.

---

# Network Analysis Orientation

## Slide 21 - Neighborhood

**Delivery Category:** Core

**Slide Text:**

A neighborhood is what can be reached near a node.

Think:

- direct neighbors
- one hop away
- two hops away
- beyond

**Instructor Notes:**

Use the campus map idea. From Parking, Library and Student Center may be one
hop away. Cafeteria might be two hops away depending on the edges.

This prepares BFS as outward exploration.

**Transition Cue:**

Ego networks focus on one selected node.

---

## Slide 22 - Ego-Centered Network

**Delivery Category:** Core / Optional

**Slide Text:**

An ego-centered network starts with one focal node.

It asks:

- who or what is directly connected?
- what is one hop away?
- what is two hops away?
- what pattern surrounds this node?

**Instructor Notes:**

Use this briefly. It is useful vocabulary, especially for social networks and
communication networks, but it should not consume the lesson.

**Transition Cue:**

One common graph question is the shortest path.

---

## Slide 23 - Shortest Path

**Delivery Category:** Core

**Slide Text:**

Shortest path asks:

- what route uses the fewest steps?
- what route has the lowest cost?
- what route reaches the target most directly?

The answer depends on the model.

**Instructor Notes:**

Be precise: if the graph is unweighted, shortest may mean fewest edges. If the
graph is weighted, shortest may mean lowest total weight.

Do not teach Dijkstra's algorithm unless as brief reserve language.

**Transition Cue:**

BFS can help explore by layers in unweighted graphs.

---

## Slide 24 - Creating A Neighborhood

**Delivery Category:** Core

**Slide Text:**

To create a neighborhood:

1. choose a start node
2. find direct neighbors
3. find neighbors of neighbors
4. decide how far to expand
5. state what the neighborhood means

**Instructor Notes:**

This slide connects textbook neighborhood language to student lab work.

Ask: "If we start at this node, what is one hop away? What is two hops away?"

**Transition Cue:**

The optional reading extends this into network metrics.

---

## Slide 25 - Optional Metrics: Recognition Only

**Delivery Category:** Instructor Reserve

**Slide Text:**

The optional reading includes:

- triangles
- density
- degree
- betweenness
- closeness
- eigenvector centrality

For this course: recognize the ideas.

**Instructor Notes:**

This is another pressure-release slide. The formulas may look intimidating.
Students do not need to calculate centrality metrics for Lab 06.

**Transition Cue:**

One metric is simple enough to recognize immediately: degree.

---

## Slide 26 - Degree And Density

**Delivery Category:** Optional Deepening

**Slide Text:**

Degree:

- how many edges connect to a node

Density:

- how many possible connections actually exist

Both describe structure.

**Instructor Notes:**

Use only if time allows. Degree is easy to count visually. Density is more
abstract and should be kept conceptual.

**Transition Cue:**

Other centrality measures describe different kinds of structural importance.

---

## Slide 27 - Centrality Is Not Importance By Itself

**Delivery Category:** Instructor Reserve

**Slide Text:**

Centrality measures estimate structural position.

They do not automatically prove:

- value
- authority
- quality
- fairness
- truth

Metrics need interpretation.

**Instructor Notes:**

This is a high-value caution. Especially in social network analysis, metrics
can be misleading if interpreted without context.

Do not turn this into a full ethics lecture, but plant the idea.

**Transition Cue:**

Now return to the required traversal algorithms.

---

# Graph Traversals

## Slide 28 - Traversal

**Delivery Category:** Core

**Slide Text:**

Traversal means visiting nodes by following edges.

Traversal depends on:

- start node
- graph structure
- neighbor order
- traversal method

**Instructor Notes:**

Students may expect traversal to be one fixed answer. Make clear that traversal
order can change when start node, neighbor order, or method changes.

**Transition Cue:**

BFS explores outward by layers.

---

## Slide 29 - Breadth-First Search

**Delivery Category:** Core

**Slide Text:**

BFS explores outward by layers.

It tends to visit:

- the start node
- direct neighbors
- neighbors of neighbors
- later layers

**Instructor Notes:**

Use "ripples in water" or "layers from the start" if helpful. This is the
plain-English anchor.

**Transition Cue:**

BFS usually uses a queue.

---

## Slide 30 - BFS Evidence

**Delivery Category:** Core

**Slide Text:**

BFS evidence can show:

| Step | Current Node | Queue State | Visited Nodes |
| --- | --- | --- | --- |
|  |  |  |  |

**Instructor Notes:**

Explain queue state as the nodes waiting to be visited next. Students do not
need to love the queue mechanics, but they need to see why BFS visits by
layers.

**Transition Cue:**

DFS follows one path more deeply.

---

## Slide 31 - Depth-First Search

**Delivery Category:** Core

**Slide Text:**

DFS follows a path deeply before backing up.

It tends to:

- choose a neighbor
- continue from that neighbor
- keep going until it cannot
- backtrack and try another path

**Instructor Notes:**

Use a hallway or maze analogy if useful. Emphasize that DFS is not "random";
it follows a rule based on neighbor order and stack/call behavior.

**Transition Cue:**

DFS evidence often uses a stack.

---

## Slide 32 - DFS Evidence

**Delivery Category:** Core

**Slide Text:**

DFS evidence can show:

| Step | Current Node | Stack State | Visited Nodes |
| --- | --- | --- | --- |
|  |  |  |  |

**Instructor Notes:**

Explain stack state as the nodes waiting while the traversal follows a path.

If students compare BFS and DFS tables, they can see the same graph explored in
different orders.

**Transition Cue:**

The same graph can produce different traversal orders.

---

## Slide 33 - BFS vs DFS

**Delivery Category:** Core

**Slide Text:**

| Question | BFS | DFS |
| --- | --- | --- |
| Explores how? | outward by layers | deeply by path |
| Common state | queue | stack or call stack |
| Useful for | near/reachable layers | path exploration |

**Instructor Notes:**

Do not overstate. BFS is often associated with shortest paths in unweighted
graphs, but this course should keep the claim careful and beginner-friendly.

**Transition Cue:**

Traversal order depends on neighbor order too.

---

## Slide 34 - Neighbor Order Matters

**Delivery Category:** Core

**Slide Text:**

Traversal order can change when:

- the start node changes
- the neighbor order changes
- the graph is directed
- the traversal method changes

The evidence should name the conditions.

**Instructor Notes:**

This is a common source of confusion. Two correct BFS implementations may show
different orders if neighbors are listed differently.

Connect this directly to Lab 06 explanation requirements.

**Transition Cue:**

The optional material shows how graph ideas scale into network analysis.

---

# Optional Network Context

## Slide 35 - Visualizing A Graph

**Delivery Category:** Optional Deepening

**Slide Text:**

A graph can be shown as:

- diagram
- adjacency list
- traversal table
- Python output
- library visualization

Each view reveals something different.

**Instructor Notes:**

This references the optional Python/visualization reading without requiring
students to use graph libraries.

Manual diagrams or Markdown diagrams are acceptable for Lab 06.

**Transition Cue:**

Social network analysis is one applied context.

---

## Slide 36 - Social Network Analysis Context

**Delivery Category:** Instructor Reserve

**Slide Text:**

Social network analysis uses graphs to study relationships.

It may ask:

- who is connected?
- who bridges groups?
- where are clusters?
- how dense is the network?

Use caution when interpreting results.

**Instructor Notes:**

Keep this as context. The fraud detection case study and fraud analytics are
skipped for this course week.

Do not encourage students to use sensitive personal data in Lab 06.

**Transition Cue:**

The key caution is that graph metrics do not replace judgment.

---

## Slide 37 - Fairness And Closeness

**Delivery Category:** Instructor Reserve

**Slide Text:**

Graph metrics can influence decisions.

Ask:

- What data created the graph?
- What relationships were included?
- What relationships were ignored?
- Who could be misrepresented?

**Instructor Notes:**

This connects optional closeness/fairness language to responsible reasoning.
The goal is not metric calculation; it is interpretive caution.

**Transition Cue:**

Now return to what students must do in Lab 06.

---

## Slide 38 - What To Deeply Learn vs Recognize

**Delivery Category:** Core

**Slide Text:**

Deeply learn now:

- nodes and edges
- adjacency list
- BFS and DFS
- traversal evidence
- model limits

Recognize for later:

- centrality metrics
- SNA
- graph libraries

**Instructor Notes:**

This slide is important for cognitive load. It tells students where to put
their effort.

**Transition Cue:**

The demo now shows the required pieces in a small graph.

---

# Demo Bridge

## Slide 39 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo: campus route map.

We will show:

- buildings as nodes
- sidewalks as edges
- adjacency list
- BFS traversal
- DFS traversal

**Instructor Notes:**

Use the existing Lab 06 demo. The campus route scenario is intentionally
different from the student lab options.

**Transition Cue:**

First, inspect the graph model.

---

## Slide 40 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

The demo produces:

- text diagram
- adjacency list
- BFS traversal table
- DFS traversal table
- traversal summary

**Instructor Notes:**

Ask students to compare the text diagram and adjacency list before running the
traversals. This reinforces model consistency.

**Transition Cue:**

Watch how queue and stack states change.

---

## Slide 41 - Demo Key Question

**Delivery Category:** Core

**Slide Text:**

Ask during the demo:

- What is the current node?
- What neighbors are available?
- What is waiting in the queue or stack?
- What has already been visited?
- What does the model leave out?

**Instructor Notes:**

These questions prepare students for their own traversal table and explanation.

Do not let the demo become only "run the code and admire the output."

**Transition Cue:**

The explanation should name why BFS and DFS differ.

---

## Slide 42 - Demo Explanation Pattern

**Delivery Category:** Core

**Slide Text:**

Example explanation:

> The graph model stayed the same, but BFS and DFS visited nodes in different
> orders because BFS explores outward by layers while DFS follows a path more
> deeply before backing up.

**Instructor Notes:**

Encourage students to preserve this logic while using their own words:
same graph, different method, different order, reason.

**Transition Cue:**

Now transfer this to Lab 06.

---

# Lab Bridge

## Slide 43 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 06, you will model a different system.

Options include:

- workflow steps
- escalation paths
- transit stops
- game rooms
- prerequisites
- communication network
- grid movement map

**Instructor Notes:**

Stress that students should not copy the campus route demo. They should use the
same modeling and traversal pattern with a different system.

**Transition Cue:**

The lab requires both a model and evidence.

---

## Slide 44 - Lab 06 Evidence

**Delivery Category:** Core

**Slide Text:**

Your evidence should include:

- at least 6 nodes
- at least 7 edges
- adjacency list
- diagram or text representation
- BFS or DFS traversal
- traversal table
- model limitation

**Instructor Notes:**

This is the practical submission checklist. Remind students that a node list
without relationships is not enough.

**Transition Cue:**

The README makes the graph reasoning visible.

---

## Slide 45 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should explain:

- what the graph models
- what the nodes represent
- what the edges represent
- what traversal you used
- what the traversal shows
- what the graph leaves out

**Instructor Notes:**

Students should understand that the README is not extra paperwork. It is where
they explain the model.

**Transition Cue:**

Now clarify the AI-use boundary.

---

## Slide 46 - AI Use In Lab 06

**Delivery Category:** Core

**Slide Text:**

Manual first:

- draft your graph
- write your adjacency list
- choose your start node
- attempt traversal evidence

AI-assisted after:

- check diagram/list consistency
- explain BFS or DFS vocabulary
- critique model limits

**Instructor Notes:**

Make clear that AI should not replace the student's graph design. AI can help
critique or clarify after the student has a draft.

This matches the student-facing AI-use rule.

**Transition Cue:**

Now close with the main lesson.

---

# Wrap-Up

## Slide 47 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Graphs help us reason about connected systems.

Carry forward:

- model the relationships
- make connections explicit
- trace the traversal
- explain what the model shows
- state what the model leaves out

**Instructor Notes:**

This is the Week 6 takeaway. Graphs are useful precisely because they force
relationships to become visible.

**Transition Cue:**

Now make the immediate next action concrete.

---

## Slide 48 - Lab 06 Success Check

**Delivery Category:** Core

**Slide Text:**

Successful Lab 06 work:

- represents relationships clearly
- uses graph vocabulary correctly
- includes adjacency-list evidence
- shows BFS or DFS behavior
- explains model limits

**Instructor Notes:**

Students should compare this slide directly to their submission before turning
it in.

**Transition Cue:**

Now assign the immediate lab action.

---

## Slide 49 - Next Step

**Delivery Category:** Core

**Slide Text:**

For Lab 06:

- choose a system
- identify nodes and edges
- build an adjacency list
- create a diagram or text representation
- run or simulate BFS or DFS
- explain what the model leaves out

**Instructor Notes:**

Remind students that a simple, well-explained model is better than a fancy
model they cannot explain.

**Transition Cue:**

Prepare students for the next reading once Week 7 reading details are assigned.

---

## Slide 50 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

Next week connects algorithms to AI, data, recommendations, and security.

As you read:

- focus on representation before advanced methods
- notice how similarity and recommendation depend on chosen features
- skim advanced ML language for recognition
- learn the security vocabulary without trying to master cryptography
- watch for limitations such as cold start, sparse data, and weakest links

**Instructor Notes:**

Use this slide to prepare students for the breadth of Week 7. The next reading
touches unsupervised learning, recommendation engines, cryptography basics, and
recommended decision-tree material.

Tell students that the Week 7 goal is not to master all of those fields. The
goal is to see how small algorithmic choices appear inside AI/data systems.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 3 | Graph model | Clean visual of buildings, tasks, and people becoming node-edge diagrams | Avoid looking like a generic social media network |
| 6 | Term precision | Split visual showing everyday word vs graph meaning for "network" and "neighbor" | Keep text minimal |
| 7 | Formula posture | Calm visual of formulas beside a simple graph, with focus moving back to nodes and edges | Avoid making formulas look scary or silly |
| 18 | Adjacency list | Side-by-side graph diagram and adjacency list with matching highlighted edge | Ensure diagram and list agree |
| 23 | Shortest path | Small unweighted graph with two possible paths and highlighted fewest-edge route | Do not imply weighted path math |
| 30 | BFS evidence | Layered ripple visual from a start node, beside queue table | Keep layers clear |
| 32 | DFS evidence | Path-following visual through nodes, beside stack table | Avoid maze clutter |
| 40 | Demo evidence | Campus map-style graph with adjacency list and traversal table | Do not use real campus map if unnecessary |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 10 min | Use only Slides 2-3 | Discuss one Lab 05 strategy comparison |
| Textbook Review | 18 min | Use Slide 38 early as effort filter | Add more examples of everyday vs graph meanings |
| Graph Basics and Representation | 30 min | Combine graph type slides | Have students identify nodes/edges in examples |
| Network Analysis Orientation | 20 min | Skip Slides 25-27 | Add one-hop/two-hop neighborhood exercise |
| Graph Traversals | 35 min | Focus on BFS and DFS tables only | Trace BFS/DFS manually on board |
| Optional Network Context | 10 min | Skip completely if needed | Discuss SNA caution and metric interpretation |
| Demo | 20 min | Show one traversal table only | Ask students to predict traversal order |
| Lab Bridge | 10 min | Combine Slides 43-46 | Walk through README expectations |

---

# Post-Lecture Notes

Use after delivery to record what worked, what needs adjustment, and what
should change in the next course run.

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
