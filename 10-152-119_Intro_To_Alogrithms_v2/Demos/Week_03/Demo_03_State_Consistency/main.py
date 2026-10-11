"""Expose stale references and distinguish shallow aliases from snapshots."""

from collections import deque
from copy import deepcopy


def stale_ids(inventory, pending):
    return [equipment_id for equipment_id in pending if equipment_id not in inventory]


def repair_queue(inventory, pending):
    removed = stale_ids(inventory, pending)
    return deque(equipment_id for equipment_id in pending if equipment_id in inventory), removed


def main():
    print("STATE CONSISTENCY AND SNAPSHOTS")
    inventory = {"E01": {"id": "E01", "available": True},
                 "E02": {"id": "E02", "available": True}}
    pending = deque(["E01", "E02"])
    del inventory["E02"]
    print("Invariant: every pending equipment ID exists in inventory.")
    print("After removal, stale IDs:", stale_ids(inventory, pending))
    repaired, removed = repair_queue(inventory, pending)
    print("Repair policy: remove stale requests:", removed, "-> pending", list(repaired))
    aliases = list(inventory.values())
    snapshot = deepcopy(aliases)
    inventory["E01"]["available"] = False
    print("\nCurrent record: ", inventory["E01"])
    print("Shallow list:   ", aliases[0], "(same mutable record)")
    print("Deep snapshot:  ", snapshot[0], "(independent, but still mutable)")
    print("Hierarchy: nested ownership; network: general relationships (preview only).")


if __name__ == "__main__":
    main()
