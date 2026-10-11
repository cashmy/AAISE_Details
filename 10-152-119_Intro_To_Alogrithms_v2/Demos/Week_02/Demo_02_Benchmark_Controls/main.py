"""Separate preprocessing, queries, and end-to-end timing on matched inputs."""

import argparse
from statistics import median
from time import perf_counter


def scan(records, queries):
    return [next((row for row in records if row["id"] == query), None) for query in queries]


def build_index(records):
    return {row["id"]: row for row in records}


def query_index(index, queries):
    return [index.get(query) for query in queries]


def indexed_end_to_end(records, queries):
    return query_index(build_index(records), queries)


def measure(action, repeats=5):
    samples = []
    for _ in range(repeats):
        started = perf_counter()
        action()
        samples.append((perf_counter() - started) * 1000)
    return median(samples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=2000)
    args = parser.parse_args()
    if not 1 <= args.size <= 20000:
        parser.error("--size must be 1 through 20000 to bound live-demo work")
    rows = [{"id": value} for value in range(args.size)]
    queries = [0, args.size - 1, -1] * 20
    index = build_index(rows)
    if not (scan(rows, queries) == query_index(index, queries)):
        raise ValueError("Cannot compare methods that return different results.")
    print("BENCHMARK CONTROLS: unique IDs, identical hit/miss queries")
    print("Misleading comparison: scan queries vs prebuilt-index queries, labeled as total.")
    print("The index-only number omits construction. It is not an end-to-end result.")
    actions = [
        ("scan queries (no setup needed)", lambda: scan(rows, queries)),
        ("index construction only", lambda: build_index(rows)),
        ("queries on an existing index", lambda: query_index(index, queries)),
        ("fresh index + all queries", lambda: indexed_end_to_end(rows, queries)),
    ]
    print("\nMedian of 5 runs; data generation and printing are outside measurements.")
    for label, action in actions:
        print(f"{label:<34} {measure(action):9.4f} ms")
    print("Timings vary; independently measured medians need not add exactly.")


if __name__ == "__main__":
    main()
