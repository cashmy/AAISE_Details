"""Regression checks, separate from the classroom application."""

from main import (
    build_index,
    fixture,
    scan_lookup,
)


def self_check():
    rows = fixture()
    index = build_index(rows)
    assert scan_lookup(rows, "E03") == (rows[2], 3)
    assert index.get("missing") is None
    index["E01"]["available"] = False
    assert rows[0]["available"] is True
    try:
        build_index(rows + [rows[0]])
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate IDs must be rejected")
    assert build_index([]) == {}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
