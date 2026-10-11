"""Observe deterministic BFS/DFS frontier and discovered-state transitions."""

from collections import deque

GRAPH = {"Library": ["Atrium", "Lab"], "Atrium": ["Library", "Cafe"],
         "Lab": ["Library", "Studio"], "Cafe": ["Atrium", "Studio"],
         "Studio": ["Lab", "Cafe"], "Annex": []}


def traverse(graph, start, strategy):
    if start not in graph:
        raise ValueError("start node must exist")
    if strategy not in ("BFS", "DFS"):
        raise ValueError("strategy must be BFS or DFS")
    frontier = deque([start]) if strategy == "BFS" else [start]
    discovered, order, trace, edges_examined = {start}, [], [], 0
    while frontier:
        node = frontier.popleft() if strategy == "BFS" else frontier.pop()
        order.append(node)
        neighbors = graph[node] if strategy == "BFS" else list(reversed(graph[node]))
        for neighbor in neighbors:
            edges_examined += 1
            if neighbor not in graph:
                raise ValueError(f"unknown neighbor {neighbor}")
            if neighbor not in discovered:
                discovered.add(neighbor)
                frontier.append(neighbor)
        trace.append((node, list(frontier), sorted(discovered)))
    return order, trace, edges_examined


def main():
    print("BFS AND DFS FRONTIERS: mark discovered when adding to frontier")
    for strategy in ("BFS", "DFS"):
        order, trace, edges = traverse(GRAPH, "Library", strategy)
        print(f"\n{strategy}: (processed node | remaining frontier | discovered)")
        for node, frontier, discovered in trace:
            print(f"{node:<8} | {str(frontier):<25} | {discovered}")
        print("Visit order:", order, "; adjacency entries examined:", edges)
    print("\nNeighbor order is fixed. DFS pushes neighbors in reverse for readable order.")
    print("Undirected edges appear twice in adjacency data. Work is O(V+E).")
    print("Visit order is not necessarily a route between consecutive entries.")


if __name__ == "__main__":
    main()
