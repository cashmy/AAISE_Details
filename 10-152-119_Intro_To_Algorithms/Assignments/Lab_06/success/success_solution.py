WORKFLOW_GRAPH = {
    "Request Received": ["Triage"],
    "Triage": ["Account Check", "Network Check", "Escalate"],
    "Account Check": ["Resolution"],
    "Network Check": ["Resolution"],
    "Escalate": ["Supervisor Review", "Resolution"],
    "Supervisor Review": ["Resolution"],
    "Resolution": [],
}

START_NODE = "Request Received"
ALTERNATE_START_NODE = "Escalate"


def breadth_first_traversal(graph, start_node):
    visited = []
    seen = {start_node}
    queue = [start_node]
    trace_rows = []
    step = 1

    while queue:
        current = queue.pop(0)
        visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

        trace_rows.append(
            {
                "step": step,
                "current_node": current,
                "state": list(queue),
                "visited": list(visited),
            }
        )
        step += 1

    return visited, trace_rows


def depth_first_traversal(graph, start_node):
    visited = []
    seen = {start_node}
    stack = [start_node]
    trace_rows = []
    step = 1

    while stack:
        current = stack.pop()
        visited.append(current)

        for neighbor in reversed(graph[current]):
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

        trace_rows.append(
            {
                "step": step,
                "current_node": current,
                "state": list(stack),
                "visited": list(visited),
            }
        )
        step += 1

    return visited, trace_rows


def print_text_diagram():
    print("WORKFLOW DIAGRAM")
    print("Request Received -> Triage")
    print("Triage -> Account Check")
    print("Triage -> Network Check")
    print("Triage -> Escalate")
    print("Account Check -> Resolution")
    print("Network Check -> Resolution")
    print("Escalate -> Supervisor Review")
    print("Escalate -> Resolution")
    print("Supervisor Review -> Resolution")
    print()


def print_adjacency_list(graph):
    print("ADJACENCY LIST")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    print()


def print_traversal_table(title, trace_rows, state_name):
    print(title)
    header = f"{'Step':<4} | {'Current Node':<18} | {state_name:<28} | Visited Nodes"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        print(
            f"{row['step']:<4} | "
            f"{row['current_node']:<18} | "
            f"{str(row['state']):<28} | "
            f"{row['visited']}"
        )
    print()


def print_comparison_note(bfs_order, dfs_order, alternate_bfs_order):
    print("TRAVERSAL COMPARISON")
    print(f"BFS from {START_NODE}: {bfs_order}")
    print(f"DFS from {START_NODE}: {dfs_order}")
    print(f"BFS from {ALTERNATE_START_NODE}: {alternate_bfs_order}")
    print()
    print(
        "Changing the traversal method changes the order in which the workflow is "
        "explored. Changing the start node changes which part of the workflow is "
        "seen first and may skip earlier steps entirely in this directed model."
    )
    print()


def print_model_limit_note():
    print("MODEL LIMIT NOTE")
    print(
        "This graph model shows possible escalation paths, but it leaves out time, "
        "priority, repeated loops, staff availability, and the reason a request might "
        "branch one way instead of another."
    )
    print()


def main():
    bfs_order, bfs_trace = breadth_first_traversal(WORKFLOW_GRAPH, START_NODE)
    dfs_order, dfs_trace = depth_first_traversal(WORKFLOW_GRAPH, START_NODE)
    alternate_bfs_order, _ = breadth_first_traversal(
        WORKFLOW_GRAPH, ALTERNATE_START_NODE
    )

    print("LAB 06 SUCCESS VERSION - GRAPH TRAVERSAL AND MODELING")
    print("System: help desk escalation workflow")
    print()
    print_text_diagram()
    print_adjacency_list(WORKFLOW_GRAPH)
    print_traversal_table("BFS TRAVERSAL TABLE", bfs_trace, "Queue State")
    print_traversal_table("DFS TRAVERSAL TABLE", dfs_trace, "Stack State")
    print_comparison_note(bfs_order, dfs_order, alternate_bfs_order)
    print_model_limit_note()


if __name__ == "__main__":
    main()
