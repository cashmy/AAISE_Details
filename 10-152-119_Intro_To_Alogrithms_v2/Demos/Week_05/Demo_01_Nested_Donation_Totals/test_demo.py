"""Regression checks, separate from the classroom application."""

from main import (
    DONATIONS,
    iterative_total,
    recursive_total,
)


def self_check():
    for node, expected in ((DONATIONS, 27), ([], 0), ([[]], 0), (0, 0), ([1, 2], 3)):
        assert recursive_total(node)[0] == iterative_total(node)[0] == expected
    for invalid in (True, -1, "5", [None]):
        for algorithm in (recursive_total, iterative_total):
            try:
                algorithm(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError("malformed donation must be rejected")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
