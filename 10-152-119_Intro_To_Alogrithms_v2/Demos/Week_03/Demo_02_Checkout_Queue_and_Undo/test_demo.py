"""Regression checks, separate from the classroom application."""

from main import (
    checkout_next,
    enqueue,
    make_state,
    undo_checkout,
)


def self_check():
    state = make_state()
    assert checkout_next(state) == "queue empty"
    assert undo_checkout(state) == "nothing to undo"
    enqueue(state, "E01")
    enqueue(state, "E02")
    checkout_next(state)
    assert state["inventory"]["E01"] is False and list(state["pending"]) == ["E02"]
    undo_checkout(state)
    assert state["inventory"]["E01"] is True and list(state["pending"]) == ["E01", "E02"]
    checkout_next(state)
    checkout_next(state)
    undo_checkout(state)
    assert list(state["pending"]) == ["E02"] and state["inventory"]["E01"] is False


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run verification without Python optimization (-O).")
    self_check()
    print("Checks passed.")
