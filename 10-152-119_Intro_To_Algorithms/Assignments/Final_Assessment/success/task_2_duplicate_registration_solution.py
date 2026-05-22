"""
Final Success Example - Task 2
Duplicate Registration Detection

This is one acceptable solution, not the only correct solution.
"""

from time import perf_counter


INPUT_SIZES = [100, 500, 1000, 2000]


def build_test_data(size):
    records = []
    for index in range(size):
        records.append({"id": f"ID-{index}", "name": f"Person {index}"})

    if size >= 4:
        records.append({"id": "ID-1", "name": "Person 1"})
        records.append({"id": "ID-3", "name": "Person 3"})

    return records


def find_duplicates_direct(records):
    duplicates = set()
    for outer_index in range(len(records)):
        for inner_index in range(outer_index + 1, len(records)):
            if records[outer_index]["id"] == records[inner_index]["id"]:
                duplicates.add(records[outer_index]["id"])
    return sorted(duplicates)


def find_duplicates_with_structure(records):
    seen = set()
    duplicates = set()
    for record in records:
        record_id = record["id"]
        if record_id in seen:
            duplicates.add(record_id)
        else:
            seen.add(record_id)
    return sorted(duplicates)


def time_once(function, records):
    start = perf_counter()
    result = function(records)
    elapsed = perf_counter() - start
    return result, elapsed


def print_results():
    print("TASK 2 SUCCESS EXAMPLE - DUPLICATE REGISTRATION DETECTION")
    print("This is one acceptable solution, not the only correct solution.")
    print()
    header = (
        f"{'Input Size':<12} | {'Direct Time':<12} | {'Set Time':<12} | "
        f"{'Same Output?':<12} | Duplicates"
    )
    print(header)
    print("-" * len(header))

    for size in INPUT_SIZES:
        records = build_test_data(size)
        direct_result, direct_time = time_once(find_duplicates_direct, records)
        set_result, set_time = time_once(find_duplicates_with_structure, records)
        same_output = "Yes" if direct_result == set_result else "No"
        print(
            f"{len(records):<12} | "
            f"{direct_time:<12.6f} | "
            f"{set_time:<12.6f} | "
            f"{same_output:<12} | "
            f"{set_result}"
        )

    print()
    print(
        "The set-based approach is a better fit here because it avoids comparing "
        "every record to every other record."
    )


if __name__ == "__main__":
    print_results()
