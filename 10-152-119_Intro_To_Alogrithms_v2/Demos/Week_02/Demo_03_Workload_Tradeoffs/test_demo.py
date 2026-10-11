"""Regression checks, separate from the classroom application."""

from main import (
    indexed,
    scan,
)


def self_check():
    records = [{"id": value} for value in range(2000)]
    for queries in ([0], [0, 1999, -1] * 100):
        assert scan(records, queries)[0] == indexed(records, queries)
    rows = [{"id": 0}, {"id": 1}]
    assert scan(rows, [0, 1, -1]) == ([rows[0], rows[1], None], 5)
    assert indexed(rows, [0, 1, -1]) == scan(rows, [0, 1, -1])[0]
    assert indexed([], [1]) == [None]
    assert scan(rows, []) == ([], 0)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
