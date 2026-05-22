import os


def use_color():
    return not os.getenv("NO_COLOR")


def colorize(text, code):
    if not use_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def success_text(text):
    return colorize(text, "92")


def warning_text(text):
    return colorize(text, "91")


def padded_colored_text(text, width, style_function):
    padded_text = f"{text:<{width}}"
    return style_function(padded_text)


SORTED_TITLES = [
    "1984",
    "Brave New World",
    "Dune",
    "Fahrenheit 451",
    "Foundation",
    "Moby Dick",
    "Neuromancer",
    "The Hobbit",
]

UNSORTED_TITLES = [
    "Dune",
    "1984",
    "The Hobbit",
    "Foundation",
    "Neuromancer",
    "Moby Dick",
    "Brave New World",
    "Fahrenheit 451",
]


def linear_search(values, target):
    trace_rows = []
    for step, value in enumerate(values, start=1):
        matched = value == target
        trace_rows.append({"step": step, "current_value": value, "match": matched})
        if matched:
            return step - 1, trace_rows
    return -1, trace_rows


def binary_search(values, target):
    low = 0
    high = len(values) - 1
    trace_rows = []
    step = 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = values[mid]

        if mid_value == target:
            decision = "found target"
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
            return mid, trace_rows

        if mid_value < target:
            decision = "search upper half"
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


def print_linear_trace(trace_rows):
    print(heading("LINEAR SEARCH TRACE"))
    header = f"{'Step':<4} | {'Current Value':<20} | Match?"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        match_text = "Yes" if row["match"] else "No"
        print(f"{row['step']:<4} | {row['current_value']:<20} | {match_text}")
    print()


def print_binary_trace(title, trace_rows):
    print(heading(title))
    header = (
        f"{'Step':<4} | {'Low':<3} | {'High':<4} | {'Mid':<3} | "
        f"{'Mid Value':<20} | Decision"
    )
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        print(
            f"{row['step']:<4} | {row['low']:<3} | {row['high']:<4} | {row['mid']:<3} | "
            f"{row['mid_value']:<20} | {row['decision']}"
        )
    print()


def print_summary_table(
    sorted_target, sorted_index, unsorted_target, unsorted_linear, unsorted_binary
):
    print(heading("SORTED VS UNSORTED SUMMARY"))
    header = (
        f"{'Case':<18} | {'Target':<18} | {'Linear Search':<16} | "
        f"{'Binary Search':<16} | Note"
    )
    print(header)
    print("-" * len(header))

    sorted_binary_text = padded_colored_text(
        f"found at {sorted_index}", 16, success_text
    )
    binary_text = (
        "not found" if unsorted_binary == -1 else f"found at {unsorted_binary}"
    )
    unsorted_binary_text = padded_colored_text(binary_text, 16, warning_text)

    print(
        f"{'Sorted list':<18} | {sorted_target:<18} | {'not shown here':<16} | "
        f"{sorted_binary_text} | "
        f"Binary search works because the data is sorted"
    )

    print(
        f"{'Unsorted list':<18} | {unsorted_target:<18} | {f'found at {unsorted_linear}':<16} | "
        f"{unsorted_binary_text} | "
        f"Binary search is unreliable because the data is unsorted"
    )
    print()


def main():
    sorted_target = "Moby Dick"
    unsorted_target = "Brave New World"

    print(heading("LAB 04 DEMO - SEARCH AND SORT BEHAVIOR"))
    print()
    print("Sorted shelf list:")
    print(SORTED_TITLES)
    print()
    print("Unsorted shelf list:")
    print(UNSORTED_TITLES)
    print()

    linear_index, linear_trace = linear_search(UNSORTED_TITLES, unsorted_target)
    sorted_binary_index, sorted_binary_trace = binary_search(
        SORTED_TITLES, sorted_target
    )
    unsorted_binary_index, unsorted_binary_trace = binary_search(
        UNSORTED_TITLES, unsorted_target
    )

    print_linear_trace(linear_trace)
    print_binary_trace("BINARY SEARCH TRACE - SORTED LIST", sorted_binary_trace)
    print_binary_trace("BINARY SEARCH TRACE - UNSORTED LIST", unsorted_binary_trace)
    print_summary_table(
        sorted_target,
        sorted_binary_index,
        unsorted_target,
        linear_index,
        unsorted_binary_index,
    )

    print(
        success_text(
            "Key point: binary search narrows correctly only when the list is sorted."
        )
    )
    print(
        warning_text(
            "A lucky result on unsorted data would still not prove the method is valid."
        )
    )


if __name__ == "__main__":
    main()
