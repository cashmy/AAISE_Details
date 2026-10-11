"""Regression checks, separate from the classroom application."""

from main import (
    GRAPH,
    traverse,
)


def self_check():
    bfs, _, edges = traverse(GRAPH, "Library", "BFS")
    dfs, _, _ = traverse(GRAPH, "Library", "DFS")
    assert bfs == ["Library", "Atrium", "Lab", "Cafe", "Studio"]
    assert dfs == ["Library", "Atrium", "Cafe", "Studio", "Lab"]
    assert edges == 10 and len(bfs) == len(set(bfs))
    assert set(bfs) == set(dfs) == set(GRAPH) - {"Annex"}
    assert traverse(GRAPH, "Annex", "BFS")[0] == ["Annex"]
    assert traverse({"A": ["A"]}, "A", "DFS")[0] == ["A"]


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
