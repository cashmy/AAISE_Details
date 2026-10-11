"""Regression checks, separate from the classroom application."""

from main import (
    SONGS,
    rank_songs,
    weighted_similarity,
)


def self_check():
    baseline = rank_songs(SONGS, {"calm", "piano"}, {})
    weighted = rank_songs(SONGS, {"calm", "piano"}, {"calm": 4})
    assert [row[0] for row in baseline] == ["S01", "S03", "S02", "S04"]
    assert [row[0] for row in weighted] == ["S01", "S02", "S03", "S04"]
    assert weighted[1][1] == 4 / 6
    assert weighted_similarity([], [], {})[0] == 0
    assert weighted_similarity(["calm"], ["calm"], {"calm": 0})[0] == 0
    assert rank_songs(SONGS, [], {}, 0) == []
    ties = [{"id": "B", "tags": []}, {"id": "A", "tags": []}]
    assert [row[0] for row in rank_songs(ties, [], {})] == ["A", "B"]
    for invalid in (-1, float("nan"), float("inf"), True):
        try:
            weighted_similarity(["calm"], ["calm"], {"calm": invalid})
        except ValueError:
            pass
        else:
            raise AssertionError("invalid weight accepted")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
