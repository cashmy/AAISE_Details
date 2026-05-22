"""
Final Part 1 - Task 2 Starter
Duplicate Registration Detection

Compare a direct comparison approach with a structure-supported approach.
Document the evidence and tradeoffs in your README.md file.
"""

from time import perf_counter


SAMPLE_REGISTRATIONS = [
    {"id": "A100", "name": "Ava"},
    {"id": "B200", "name": "Luis"},
    {"id": "A100", "name": "Ava"},
    {"id": "C300", "name": "Mina"},
]


def find_duplicates_direct(records):
    """
    Use a direct comparison approach such as nested loops.
    Return duplicate IDs or records in a clear format.
    """
    # TODO: compare records directly.
    return []


def find_duplicates_with_structure(records):
    """
    Use a set or dictionary to support duplicate detection.
    Return duplicate IDs or records in the same format as the direct approach.
    """
    # TODO: use a set or dictionary to track what has already been seen.
    return []


def build_test_data(size):
    """
    Build registration records for one input size.

    You may replace this with your own data-building approach.
    Make sure both algorithms receive equivalent input.
    """
    records = []
    for index in range(size):
        records.append({"id": f"ID-{index}", "name": f"Person {index}"})

    if size >= 4:
        records.append({"id": "ID-1", "name": "Person 1"})
        records.append({"id": "ID-3", "name": "Person 3"})

    return records


def time_once(function, records):
    start = perf_counter()
    result = function(records)
    elapsed = perf_counter() - start
    return result, elapsed


def main():
    print("Task 2 starter loaded.")
    print("Complete both duplicate-detection approaches.")
    print("Use several input sizes or test sets.")
    print("Record comparison evidence in your README.md file.")

    # Optional pseudocode:
    # for each input size:
    #     records = build_test_data(size)
    #     result_a, time_a = time_once(find_duplicates_direct, records)
    #     result_b, time_b = time_once(find_duplicates_with_structure, records)
    #     compare result_a and result_b
    #     record the evidence in README.md


if __name__ == "__main__":
    main()
