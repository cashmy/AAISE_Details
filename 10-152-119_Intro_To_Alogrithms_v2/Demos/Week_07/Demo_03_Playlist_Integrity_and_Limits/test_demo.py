"""Regression checks, separate from the classroom application."""

from main import (
    PLAYLIST,
    deepcopy,
    digest,
    rank,
)


def self_check():
    reordered = deepcopy(list(reversed(PLAYLIST)))
    for song in reordered:
        song["tags"].reverse()
    assert digest(reordered) == digest(PLAYLIST)
    renamed = deepcopy(PLAYLIST)
    renamed[0]["title"] = "Renamed"
    assert digest(renamed) != digest(PLAYLIST)
    assert rank(renamed, {"calm", "piano"}) == rank(PLAYLIST, {"calm", "piano"})
    missing = deepcopy(PLAYLIST)
    missing[0]["tags"] = []
    assert rank(missing, {"calm", "piano"})[0][0] == "S02"
    assert len(digest([])) == 64


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
