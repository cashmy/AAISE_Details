"""Regression checks, separate from the classroom application."""

from main import (
    cached_fibonacci,
    uncached_fibonacci,
)


def self_check():
    for n, expected in ((0, 0), (1, 1), (2, 1), (5, 5), (10, 55)):
        assert uncached_fibonacci(n)[0] == cached_fibonacci(n)[0] == expected
    assert uncached_fibonacci(5)[1] == 15
    result, calls, hits, cache = cached_fibonacci(5)
    assert (result, calls, hits, len(cache)) == (5, 9, 3, 6)
    assert cached_fibonacci(5) == cached_fibonacci(5)
    for invalid in (-1, True, 21):
        try:
            cached_fibonacci(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid recurrence input accepted")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
