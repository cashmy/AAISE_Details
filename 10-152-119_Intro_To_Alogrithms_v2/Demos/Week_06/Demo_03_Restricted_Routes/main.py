"""Reconstruct unweighted paths and apply explicit node restrictions."""

import argparse
from collections import deque

GRAPH = {"Library": ["Atrium", "Lab"], "Atrium": ["Library", "Cafe"],
         "Lab": ["Library", "Studio"], "Cafe": ["Atrium", "Studio"],
         "Studio": ["Lab", "Cafe"], "Annex": []}
DISTANCES = {frozenset(("Library", "Atrium")): 1, frozenset(("Atrium", "Cafe")): 1,
             frozenset(("Cafe", "Studio")): 1, frozenset(("Library", "Lab")): 8,
             frozenset(("Lab", "Studio")): 8}


def shortest_hop_path(graph, start, goal, blocked=()):
    blocked = set(blocked)
    if start not in graph or goal not in graph or not blocked <= graph.keys():
        raise ValueError("start, goal, and blocked nodes must exist")
    if start in blocked or goal in blocked:
        return None, {}
    parents, queue = {start: None}, deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            return list(reversed(path)), parents
        for neighbor in graph[node]:
            if neighbor not in parents and neighbor not in blocked:
                parents[neighbor] = node
                queue.append(neighbor)
    return None, parents


def route_distance(path):
    return sum(DISTANCES[frozenset((a, b))] for a, b in zip(path, path[1:]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocked", nargs="*", choices=list(GRAPH), default=["Lab"])
    args = parser.parse_args()
    print("RESTRICTED ROUTES: BFS minimizes hops, not distance")
    path, parents = shortest_hop_path(GRAPH, "Library", "Studio")
    print("Baseline route:", path, "; hops:", len(path) - 1, "; distance:", route_distance(path))
    print("Parents:", parents)
    restricted, _ = shortest_hop_path(GRAPH, "Library", "Studio", args.blocked)
    print("Blocked nodes:", args.blocked, "-> route:", restricted)
    if restricted is not None:
        print("Restricted hops:", len(restricted) - 1, "; distance:", route_distance(restricted))
    print("Unreachable Annex:", shortest_hop_path(GRAPH, "Library", "Annex")[0])
    print("Start equals goal:", shortest_hop_path(GRAPH, "Library", "Library")[0])
    print("A 3-hop path can be shorter in distance than this 2-hop path.")


if __name__ == "__main__":
    main()
