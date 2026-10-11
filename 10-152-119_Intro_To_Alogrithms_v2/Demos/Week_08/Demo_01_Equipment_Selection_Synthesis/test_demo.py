"""Regression checks, separate from the classroom application."""

from main import (
    EQUIPMENT,
    indexed_requests,
    scan_requests,
)


def self_check():
    queries = ["E01", "E02", "E03", "E04", "missing"]
    for threshold in (0, 50, 80, 100):
        assert scan_requests(EQUIPMENT, queries, threshold)[0] == indexed_requests(
            EQUIPMENT, queries, threshold)[0]
    assert indexed_requests(EQUIPMENT, ["E04"], 50)[0] == [EQUIPMENT[3]]
    assert indexed_requests(EQUIPMENT, ["E04"], 80)[0] == [None]
    assert scan_requests([], queries, 50)[0] == [None] * 5
    assert scan_requests(EQUIPMENT, [], 50) == ([], 0)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
