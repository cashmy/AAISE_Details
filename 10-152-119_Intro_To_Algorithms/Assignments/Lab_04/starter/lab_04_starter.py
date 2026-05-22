"""
Lab 04 Starter - Search and Sort Behavior

Use this file only as a starting structure.

Your job is to choose a data set, implement linear search and binary search,
create the required tests, and record trace evidence in your README.md file.
"""

DATASET_NAME = "Replace with your chosen data set"

SORTED_VALUES = [
    "TODO",
    "TODO",
    "TODO",
]

UNSORTED_VALUES = [
    "TODO",
    "TODO",
    "TODO",
]

REQUIRED_TESTS = [
    "value found near the beginning",
    "value found near the end",
    "value not found",
    "binary search attempted on unsorted data",
]


def linear_search(values, target):
    """
    Search from left to right until you find the target or reach the end.

    Suggested trace columns:
    - step
    - current value
    - match or not
    """
    # TODO: write linear search.
    # TODO: decide whether you want to collect trace rows while searching.
    return None


def binary_search(values, target):
    """
    Search a sorted list by checking the middle value and removing half of the
    remaining search space each step.

    Suggested trace columns:
    - step
    - low
    - high
    - mid
    - mid value
    - decision
    """
    # TODO: write binary search.
    # TODO: explain the sorted-data precondition in your README.md file.
    return None


def main():
    print("Lab 04 starter loaded.")
    print("Next steps:")
    print("1. Replace the data set with at least 12 values.")
    print("2. Write linear_search() and binary_search().")
    print("3. Create the four required tests.")
    print("4. Build at least one trace table for your README.md file.")
    print("5. Explain why binary search needs sorted data.")
    print()
    print("Suggested pseudocode:")
    print("- run linear search on the target values")
    print("- run binary search on the sorted data")
    print("- attempt binary search on unsorted data")
    print("- record the steps in a trace table")
    print()
    print(
        "This starter is intentionally incomplete. You must design the tests and traces."
    )


if __name__ == "__main__":
    main()
