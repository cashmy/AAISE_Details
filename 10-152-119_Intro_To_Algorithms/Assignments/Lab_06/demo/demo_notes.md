# LAB 06 DEMO NOTES - GRAPH TRAVERSAL AND MODELING

**Demo Title:** Campus Route Map Traversal
**Related Lab:** Lab 06 - Graph Traversal and Modeling
**Concept Transfer Target:** Model a real system as a graph and compare BFS and DFS traversal behavior
**Estimated Time:** 12-15 minutes

---

# Assumptions

- creating a fresh `Assignments/Lab_06/` package
- treating the student-facing Lab 06 file as authoritative
- using a generic starter rather than a scenario-specific starter
- using a campus route map for the demo and a different real-system graph for
  the plain success version
- using a text diagram, adjacency list, and traversal tables as the visible
  evidence
- using light ANSI color in the instructor demo when it helps distinguish BFS,
  DFS, section boundaries, traversal summaries, and the key takeaway
- keeping the primary success version plain while providing optional colorized
  refinements separately when useful

---

# Opening Frame

Today we are moving from step-by-step algorithms on simple data to using a
graph as a model of a system. The goal is to show that BFS and DFS do not only
visit nodes. They reveal different patterns in how the system can be explored.

---

# Demo Problem

Model a small campus route map with buildings as nodes and sidewalks as edges.

Demonstrate:

- a text diagram of the route map
- adjacency-list creation
- BFS traversal from one start building
- DFS traversal from the same start building

---

# What Students Should Notice

- a graph is a model of relationships, not the full real system
- adjacency lists make the connections explicit
- BFS and DFS can visit the same graph in different orders
- traversal order depends on the chosen start node and neighbor order
- a diagram helps check whether the graph model matches the intended system

---

# Demo Evidence

Run `demo_code.py` to produce:

- a simple text diagram of the campus routes
- an adjacency list for the campus graph
- a BFS traversal table with queue state and visited nodes
- a DFS traversal table with stack state and visited nodes
- a short comparison summary of the traversal orders

Students should be able to explain why the same graph can produce different
orders and what that means for the modeled system.

Console presentation note:

The demo uses light ANSI color to make BFS, DFS, section headings, traversal
summaries, and the final takeaway easier to inspect. This is instructor-demo
presentation polish, not a student lab requirement.

---

# Transfer Bridge

> In the demo, we modeled campus routes and compared BFS and DFS from the same
> start node. In the lab, students will model a different system, produce their
> own traversal evidence, and explain what the graph reveals and what it leaves
> out.

---

# Stop Point

Stop after one traversal comparison from one start building. Do not turn the
demo into a full workflow, escalation path, transit, game map, prerequisite, or
social-network solution.

---

# Likely Misconceptions

- students may assume the graph is the real system instead of a simplified model
- students may expect one traversal order to be universally better
- students may forget that neighbor order affects the printed traversal order
- students may describe the graph without stating what the model leaves out

---

# Instructor Notes

- Keep the graph small enough for students to follow the traversal tables.
- Use the same start node for BFS and DFS so the difference in order is easy to
  see.
- Ask students what the graph does not capture, such as distance, crowding, or
  travel time.
- Remind students that their lab needs visible traversal evidence, not only code.
