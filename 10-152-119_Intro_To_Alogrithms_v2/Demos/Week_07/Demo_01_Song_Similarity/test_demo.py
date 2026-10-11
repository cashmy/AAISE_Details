"""Regression checks, separate from the classroom application."""

from main import (
    SONGS,
    jaccard,
    score_songs,
    shared_count,
)


def self_check():
    assert shared_count(["calm", "calm"], ["calm"]) == 1
    assert jaccard({"calm", "piano"}, {"calm", "piano"}) == 1
    assert jaccard({"calm", "acoustic"}, {"calm", "piano"}) == 1 / 3
    assert jaccard([], []) == 0 and jaccard(["piano"], []) == 0
    scored = score_songs(SONGS, {"calm", "piano"})
    assert scored[3][1:3] == (0, 0.0)
    assert scored[0][1] == scored[4][1] == 2 and scored[0][2] > scored[4][2]


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
