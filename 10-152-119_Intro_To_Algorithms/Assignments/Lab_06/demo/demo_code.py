import os


def use_color():
    return not os.getenv("NO_COLOR")


def colorize(text, code):
    if not use_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def bfs_text(text):
    return colorize(text, "92")


def dfs_text(text):
    return colorize(text, "93")


def summary_text(text):
    return colorize(text, "95")


CAMPUS_GRAPH = {
    "Parking": ["Library", "Student Center"],
    "Library": ["Parking", "Science Hall", "Cafeteria"],
    "Student Center": ["Parking", "Cafeteria", "Gym"],
    "Science Hall": ["Library", "Gym"],
    "Cafeteria": ["Library", "Student Center", "Gym"],
    "Gym": ["Student Center", "Science Hall", "Cafeteria"],
}

START_NODE = "Parking"


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


def print_diagram():
    print(heading("CAMPUS ROUTE DIAGRAM"))
    print("Parking -> Library")
    print("Parking -> Student Center")
    print("Library -> Science Hall")
    print("Library -> Cafeteria")
    print("Student Center -> Cafeteria")
    print("Student Center -> Gym")
    print("Science Hall -> Gym")
    print("Cafeteria -> Gym")
    print()


def print_adjacency_list(graph):
    print(heading("ADJACENCY LIST"))
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    print()


def print_traversal_table(title, trace_rows, state_name):
    if title.startswith("BFS"):
        print(bfs_text(title))
    elif title.startswith("DFS"):
        print(dfs_text(title))
    else:
        print(heading(title))
    header = f"{'Step':<4} | {'Current Node':<14} | {state_name:<22} | Visited Nodes"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        print(
            f"{row['step']:<4} | "
            f"{row['current_node']:<14} | "
            f"{str(row['state']):<22} | "
            f"{row['visited']}"
        )
    print()


def main():
    bfs_order, bfs_trace = breadth_first_traversal(CAMPUS_GRAPH, START_NODE)
    dfs_order, dfs_trace = depth_first_traversal(CAMPUS_GRAPH, START_NODE)

    print(heading("LAB 06 DEMO - GRAPH TRAVERSAL AND MODELING"))
    print(f"Start node: {summary_text(START_NODE)}")
    print()
    print_diagram()
    print_adjacency_list(CAMPUS_GRAPH)
    print_traversal_table("BFS TRAVERSAL TABLE", bfs_trace, "Queue State")
    print_traversal_table("DFS TRAVERSAL TABLE", dfs_trace, "Stack State")
    print(summary_text("TRAVERSAL SUMMARY"))
    print(f"{bfs_text('BFS order:')} {bfs_order}")
    print(f"{dfs_text('DFS order:')} {dfs_order}")
    print()
    print(
        summary_text(
            "Key point: the graph stays the same, but the traversal order changes with the method."
        )
    )


if __name__ == "__main__":
    main()
