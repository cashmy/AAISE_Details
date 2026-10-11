"""Validate an explicit undirected campus adjacency-list model."""

GRAPH = {
    "Library": ["Atrium", "Lab"],
    "Atrium": ["Library", "Cafe"],
    "Lab": ["Library", "Studio"],
    "Cafe": ["Atrium", "Studio"],
    "Studio": ["Lab", "Cafe"],
    "Annex": [],
}


def validate_graph(graph, undirected=True):
    errors = []
    for node, neighbors in graph.items():
        if len(neighbors) != len(set(neighbors)):
            errors.append(f"{node}: duplicate neighbor")
        for neighbor in neighbors:
            if neighbor not in graph:
                errors.append(f"{node}: unknown node {neighbor}")
            elif undirected and node not in graph[neighbor]:
                errors.append(f"{node}->{neighbor}: missing reciprocal connection")
    return errors


def main():
    print("CAMPUS GRAPH MODEL (fictional map)")
    print("Node = building; edge = an allowed direct walk; undirected, no distance weights.")
    for node, neighbors in GRAPH.items():
        print(f"{node:<8} -> {neighbors}")
    print("\nCycle: Library -> Atrium -> Cafe -> Studio -> Lab -> Library")
    print("Annex is a valid disconnected node, not a missing reference.")
    broken = {node: list(neighbors) for node, neighbors in GRAPH.items()}
    broken["Library"].append("Gym")
    print("Broken model:", validate_graph(broken))
    print("Valid model: ", validate_graph(GRAPH))
    print("This model omits distance, opening hours, accessibility, and travel time.")


if __name__ == "__main__":
    main()
