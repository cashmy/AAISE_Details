# LAB 06 OPTION SOLUTION SKETCHES

**Lab:** Graph Traversal and Modeling  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches support evaluation of graph-modeling submissions. They are not
student-facing walkthroughs and are not full runnable graph solutions.

For Lab 06, a strong submission makes the relationship model visible. The graph
does not need to model the real system perfectly. It needs to define nodes,
edges, traversal behavior, and model limits honestly.

---

# Common Required Evidence

Every option should include:

- system description
- at least six nodes
- at least seven edges
- adjacency list
- diagram or clearly formatted text representation
- BFS or DFS traversal from a selected start node
- comparison or explanation of what changes if start node or traversal method
  changes
- model limitation

Suggested traversal table:

| Step | Current Node | Queue or Stack State | Visited Nodes |
| --- | --- | --- | --- |

---

# Option 1 - Workflow Steps

## Viable Framing

Model a workflow such as request intake, review, assignment, work, revision,
approval, and closure.

## Expected Representation

Nodes are workflow states. Edges are allowed transitions.

## Expected Traversal Meaning

BFS can show nearby possible next states. DFS can show one possible path through
the workflow.

## Edge Cases

- loop back for revision
- rejected or cancelled path
- terminal closed state

## Grading Watch-Fors

- Student lists steps but does not define edges.
- Student creates a linear list and calls it a graph without relationships.
- Student omits what the model leaves out, such as timing or ownership.

---

# Option 2 - Help Desk Escalation Paths

## Viable Framing

Model how a ticket can move between intake, tier 1, network, security,
software, vendor, and management.

## Expected Representation

Nodes are teams or escalation states. Edges show possible handoffs.

## Expected Traversal Meaning

BFS from intake can show the nearest escalation options. DFS can follow one
deep escalation chain.

## Edge Cases

- ticket returned for more information
- escalation loop
- vendor path requiring approval

## Grading Watch-Fors

- Student does not clarify whether edges are one-way.
- Student ignores loops or handbacks.
- Student treats traversal as a final business decision rather than a model of
  possible paths.

---

# Option 3 - Transit Stops

## Viable Framing

Model a small bus, train, or shuttle network.

## Expected Representation

Nodes are stops. Edges are direct travel connections.

## Expected Traversal Meaning

BFS can show stops reachable in the fewest number of transfers for an
unweighted graph. DFS can show route exploration but does not guarantee the
shortest path.

## Edge Cases

- one-way routes
- disconnected stop
- transfer station

## Grading Watch-Fors

- Student claims shortest time without modeling travel time.
- Student forgets to add reverse edges for two-way travel.
- Student has fewer than seven edges.

---

# Option 4 - Game Map Rooms

## Viable Framing

Model rooms connected by doors, hallways, or portals.

## Expected Representation

Nodes are rooms. Edges are direct movement options.

## Expected Traversal Meaning

DFS is natural for exploring one path deeply. BFS is natural for finding rooms
within a small number of moves.

## Edge Cases

- locked room
- one-way door
- dead end

## Grading Watch-Fors

- Student draws a map but does not provide adjacency list.
- Student does not explain start node.
- Student claims game strategy beyond what the graph shows.

---

# Option 5 - Course Prerequisite Relationships

## Viable Framing

Model courses and prerequisite or concurrent relationships.

## Expected Representation

Nodes are courses. Edges must have a clearly stated direction, such as
`prerequisite -> later course`.

## Expected Traversal Meaning

Traversal can show possible course paths or dependency chains, depending on
edge direction.

## Edge Cases

- concurrent courses
- course with multiple prerequisites
- course with no prerequisites

## Grading Watch-Fors

- Student does not define edge direction.
- Student mixes prerequisite and "taken together" relationships without
  labeling them.
- Student overclaims that traversal gives a complete degree plan.

---

# Option 6 - Social Or Communication Network

## Viable Framing

Model people, teams, or channels and their direct communication links.

## Expected Representation

Nodes are people/groups/channels. Edges are communication or relationship
links. Student should state whether links are mutual or one-way.

## Expected Traversal Meaning

BFS can show nearby communication reach. DFS can show one chain of connection.

## Edge Cases

- one-way communication
- disconnected person or team
- privacy-sensitive relationship

## Grading Watch-Fors

- Student uses personal data inappropriately.
- Student does not define what an edge means.
- Student treats graph closeness as proof of social importance.

---

# Option 7 - Grid Movement Map

## Viable Framing

Model a grid where open cells are nodes and allowed moves are edges.

## Expected Representation

Nodes are grid locations. Edges connect locations reachable in one allowed
move. Blocked cells should not be reachable.

## Expected Traversal Meaning

BFS can show shortest number of moves in an unweighted grid. DFS can explore a
path but may not find the shortest path first.

## Edge Cases

- blocked cell
- start or goal blocked
- no path exists

## Grading Watch-Fors

- Student includes blocked cells as reachable nodes.
- Student claims shortest path using DFS without justification.
- Student does not show queue or stack state.

---

# Cross-Option Grading Calibration

Strong work should:

- distinguish nodes from edges
- provide an adjacency list
- show traversal evidence
- explain what traversal means in the modeled system
- include at least one honest model limitation
