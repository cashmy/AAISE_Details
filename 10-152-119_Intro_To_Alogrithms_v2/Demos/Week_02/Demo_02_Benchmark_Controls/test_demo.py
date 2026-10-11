"""Regression checks, separate from the classroom application."""

from main import (
    build_index,
    indexed_end_to_end,
    query_index,
    scan,
)


def self_check():
    for size in (1, 20, 2000):
        rows = [{"id": value} for value in range(size)]
        queries = [0, size - 1, -1] * 20
        assert scan(rows, queries) == indexed_end_to_end(rows, queries)
    rows = [{"id": 1}, {"id": 3}]
    queries = [3, 2, 1]
    assert scan(rows, queries) == [rows[1], None, rows[0]]
    assert indexed_end_to_end(rows, queries) == scan(rows, queries)
    assert scan([], [1]) == indexed_end_to_end([], [1]) == [None]
    assert query_index(build_index(rows), []) == []


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
