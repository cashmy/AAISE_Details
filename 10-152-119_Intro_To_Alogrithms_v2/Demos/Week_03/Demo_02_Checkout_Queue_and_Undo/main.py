"""A FIFO request queue and a bounded LIFO checkout undo."""

from collections import deque


def make_state():
    return {"inventory": {"E01": True, "E02": True}, "pending": deque(), "undo": []}


def enqueue(state, equipment_id):
    if equipment_id not in state["inventory"]:
        raise ValueError("unknown equipment ID")
    if equipment_id in state["pending"]:
        raise ValueError("duplicate pending request")
    state["pending"].append(equipment_id)


def checkout_next(state):
    if not state["pending"]:
        return "queue empty"
    equipment_id = state["pending"].popleft()
    previous = state["inventory"][equipment_id]
    if not previous:
        return f"{equipment_id}: denied (unavailable); request consumed"
    state["inventory"][equipment_id] = False
    state["undo"].append((equipment_id, previous))
    return f"{equipment_id}: checked out"


def undo_checkout(state):
    if not state["undo"]:
        return "nothing to undo"
    equipment_id, previous = state["undo"].pop()
    state["inventory"][equipment_id] = previous
    # Restore the consumed request as well as inventory availability.
    if equipment_id not in state["pending"]:
        state["pending"].appendleft(equipment_id)
    return f"{equipment_id}: checkout undone; request restored at front"


def display(state, action):
    print(f"\n{action}")
    print("  Availability:", state["inventory"])
    print("  Pending FIFO:", list(state["pending"]))
    print("  Undo LIFO:   ", state["undo"])


def main():
    print("CHECKOUT QUEUE AND UNDO: only checkout is reversible")
    state = make_state()
    enqueue(state, "E01")
    enqueue(state, "E02")
    display(state, "Initial requests")
    display(state, checkout_next(state))
    display(state, checkout_next(state))
    display(state, undo_checkout(state))
    print("\nThe most recent checkout is undone first; FIFO request order is restored.")


if __name__ == "__main__":
    main()
