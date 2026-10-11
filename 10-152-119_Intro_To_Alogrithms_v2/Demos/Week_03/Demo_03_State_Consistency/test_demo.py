"""Regression checks, separate from the classroom application."""

from main import (
    deepcopy,
    deque,
    repair_queue,
    stale_ids,
)


def self_check():
    inventory = {"E01": {"available": True}, "E02": {"available": True}}
    pending = deque(["E01", "missing", "E02"])
    repaired, removed = repair_queue(inventory, pending)
    assert list(repaired) == ["E01", "E02"] and removed == ["missing"]
    assert list(pending) == ["E01", "missing", "E02"]
    assert not stale_ids(inventory, repaired)
    snapshot = deepcopy(list(inventory.values()))
    inventory["E01"]["available"] = False
    assert snapshot[0]["available"] is True
    assert repair_queue({}, deque())[1] == []


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
