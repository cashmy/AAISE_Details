"""
Lab 06 Starter - Graph Traversal and Modeling

Use this file only as a starting structure.

Your job is to choose one system, model it as a graph, build an adjacency list,
perform BFS or DFS, and record the evidence in README.md.
"""

SYSTEM_NAME = "Replace with the system you are modeling"

NODES = [
    "TODO_NODE_1",
    "TODO_NODE_2",
    "TODO_NODE_3",
    "TODO_NODE_4",
    "TODO_NODE_5",
    "TODO_NODE_6",
]

EDGES = [
    ("TODO_NODE_1", "TODO_NODE_2"),
    ("TODO_NODE_1", "TODO_NODE_3"),
    ("TODO_NODE_2", "TODO_NODE_4"),
]

START_NODE = "TODO_NODE_1"


def build_adjacency_list(nodes, edges):
    """
    Build an adjacency list from your chosen nodes and edges.

    Replace this docstring with a note about whether your graph is directed,
    undirected, or otherwise simplified.
    """
    # TODO: create the adjacency list.
    return None


def breadth_first_traversal(graph, start_node):
    """
    Traverse the graph with BFS.

    Suggested evidence columns:
    - step
    - current node
    - queue state
    - visited nodes
    """
    # TODO: write BFS if you choose BFS for your traversal evidence.
    return None


def depth_first_traversal(graph, start_node):
    """
    Traverse the graph with DFS.

    Suggested evidence columns:
    - step
    - current node
    - stack state
    - visited nodes
    """
    # TODO: write DFS if you choose DFS for your traversal evidence.
    return None


def main():
    print("Lab 06 starter loaded.")
    print("Next steps:")
    print("1. Describe the system you are modeling.")
    print("2. Replace the nodes and edges with your own graph.")
    print("3. Build the adjacency list.")
    print("4. Run BFS or DFS from a selected start node.")
    print(
        "5. Record a traversal table and explain what the model leaves out in README.md."
    )
    print()
    print("Suggested pseudocode:")
    print("- define nodes and edges")
    print("- build the adjacency list")
    print("- choose a start node")
    print("- run BFS or DFS")
    print("- record the traversal evidence and model limitation")
    print()
    print(
        "This starter is intentionally incomplete. You must design the graph and traversal evidence."
    )


if __name__ == "__main__":
    main()
