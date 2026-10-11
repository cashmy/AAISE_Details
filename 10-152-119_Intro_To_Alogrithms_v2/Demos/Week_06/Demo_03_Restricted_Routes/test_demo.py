"""Regression checks, separate from the classroom application."""

from main import (
    GRAPH,
    route_distance,
    shortest_hop_path,
)


def self_check():
    path, _ = shortest_hop_path(GRAPH, "Library", "Studio")
    assert path == ["Library", "Lab", "Studio"] and route_distance(path) == 16
    restricted, _ = shortest_hop_path(GRAPH, "Library", "Studio", ["Lab"])
    assert restricted == ["Library", "Atrium", "Cafe", "Studio"]
    assert route_distance(restricted) == 3
    assert shortest_hop_path(GRAPH, "Library", "Annex")[0] is None
    assert shortest_hop_path(GRAPH, "Library", "Library")[0] == ["Library"]
    assert shortest_hop_path(GRAPH, "Library", "Studio", ["Studio"])[0] is None
    assert shortest_hop_path(GRAPH, "Library", "Studio", ["Lab", "Cafe"])[0] is None
    assert all(b in GRAPH[a] for a, b in zip(restricted, restricted[1:]))


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
