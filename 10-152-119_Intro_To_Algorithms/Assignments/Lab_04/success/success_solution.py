SORTED_COURSE_CODES = [
    "ALG-101",
    "CIS-103",
    "CIS-110",
    "CIS-120",
    "CIS-130",
    "DB-210",
    "NET-220",
    "PY-101",
    "PY-201",
    "SEC-250",
    "WEB-105",
    "WEB-205",
]

UNSORTED_COURSE_CODES = [
    "WEB-105",
    "CIS-130",
    "ALG-101",
    "PY-101",
    "DB-210",
    "SEC-250",
    "CIS-103",
    "WEB-205",
    "NET-220",
    "CIS-110",
    "PY-201",
    "CIS-120",
]

TEST_CASES = [
    {
        "name": "Beginning",
        "dataset_name": "sorted",
        "target": "CIS-103",
    },
    {
        "name": "End",
        "dataset_name": "sorted",
        "target": "WEB-205",
    },
    {
        "name": "Missing",
        "dataset_name": "sorted",
        "target": "UX-300",
    },
    {
        "name": "Unsorted binary",
        "dataset_name": "unsorted",
        "target": "NET-220",
    },
]


def linear_search(values, target, collect_trace=False):
    trace_rows = []
    for step, value in enumerate(values, start=1):
        matched = value == target
        if collect_trace:
            trace_rows.append({"step": step, "current_value": value, "match": matched})
        if matched:
            return step - 1, trace_rows
    return -1, trace_rows


def binary_search(values, target, collect_trace=False):
    low = 0
    high = len(values) - 1
    trace_rows = []
    step = 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = values[mid]

        if mid_value == target:
            if collect_trace:
                trace_rows.append(
                    {
                        "step": step,
                        "low": low,
                        "high": high,
                        "mid": mid,
                        "mid_value": mid_value,
                        "decision": "found target",
                    }
                )
            return mid, trace_rows

        if mid_value < target:
            decision = "search upper half"
            if collect_trace:
                trace_rows.append(
                    {
                        "step": step,
                        "low": low,
                        "high": high,
                        "mid": mid,
                        "mid_value": mid_value,
                        "decision": decision,
                    }
                )
            low = mid + 1
        else:
            decision = "search lower half"
            if collect_trace:
                trace_rows.append(
                    {
                        "step": step,
                        "low": low,
                        "high": high,
                        "mid": mid,
                        "mid_value": mid_value,
                        "decision": decision,
                    }
                )
            high = mid - 1

        step += 1

    return -1, trace_rows


def result_text(index):
    return f"found at index {index}" if index >= 0 else "not found"


def print_test_summary():
    print("TEST SUMMARY")
    header = (
        f"{'Test':<16} | {'Dataset':<10} | {'Target':<10} | {'Linear Search':<18} | "
        f"{'Binary Search':<18} | Note"
    )
    print(header)
    print("-" * len(header))

    for test_case in TEST_CASES:
        dataset = (
            SORTED_COURSE_CODES
            if test_case["dataset_name"] == "sorted"
            else UNSORTED_COURSE_CODES
        )
        linear_index, _ = linear_search(
            dataset, test_case["target"], collect_trace=False
        )
        binary_index, _ = binary_search(
            dataset, test_case["target"], collect_trace=False
        )

        if test_case["dataset_name"] == "sorted":
            note = "Sorted data supports correct binary search reasoning"
        else:
            note = "Binary search is unreliable because the data is unsorted"

        print(
            f"{test_case['name']:<16} | "
            f"{test_case['dataset_name']:<10} | "
            f"{test_case['target']:<10} | "
            f"{result_text(linear_index):<18} | "
            f"{result_text(binary_index):<18} | "
            f"{note}"
        )

    print()


def print_linear_trace(title, trace_rows):
    print(title)
    header = f"{'Step':<4} | {'Current Value':<12} | Match?"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        match_text = "Yes" if row["match"] else "No"
        print(f"{row['step']:<4} | {row['current_value']:<12} | {match_text}")
    print()


def print_binary_trace(title, trace_rows):
    print(title)
    header = f"{'Step':<4} | {'Low':<3} | {'High':<4} | {'Mid':<3} | {'Mid Value':<12} | Decision"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        print(
            f"{row['step']:<4} | {row['low']:<3} | {row['high']:<4} | {row['mid']:<3} | "
            f"{row['mid_value']:<12} | {row['decision']}"
        )
    print()


def print_precondition_note():
    print("PRECONDITION NOTE")
    print(
        "Binary search depends on sorted data because each decision removes half "
        "of the remaining values based on the ordering. If the data is unsorted, "
        "the algorithm can remove the half that actually contains the target."
    )
    print()


def main():
    print("LAB 04 SUCCESS VERSION - SEARCH AND SORT BEHAVIOR")
    print("Data set: course codes")
    print()
    print_test_summary()

    _, linear_trace = linear_search(SORTED_COURSE_CODES, "CIS-103", collect_trace=True)
    _, binary_trace_sorted = binary_search(
        SORTED_COURSE_CODES, "WEB-205", collect_trace=True
    )
    _, binary_trace_unsorted = binary_search(
        UNSORTED_COURSE_CODES, "NET-220", collect_trace=True
    )

    print_linear_trace("LINEAR SEARCH TRACE - FOUND NEAR THE BEGINNING", linear_trace)
    print_binary_trace("BINARY SEARCH TRACE - SORTED DATA", binary_trace_sorted)
    print_binary_trace("BINARY SEARCH TRACE - UNSORTED DATA", binary_trace_unsorted)
    print_precondition_note()


if __name__ == "__main__":
    main()
