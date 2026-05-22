import os


USE_COLOR = os.environ.get("NO_COLOR") is None


class Style:
    RESET = "\033[0m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    CYAN = "\033[36m" if USE_COLOR else ""
    GREEN = "\033[32m" if USE_COLOR else ""
    YELLOW = "\033[33m" if USE_COLOR else ""


def colorize(text, *styles):
    if not USE_COLOR:
        return text
    return "".join(styles) + text + Style.RESET


DONATION_GROUP = [10, [5, 5], [20, [1, 4]], 3]


def total_donations_iterative(donations):
    total = 0
    work_stack = [donations]

    while work_stack:
        current = work_stack.pop()
        for item in current:
            if isinstance(item, list):
                work_stack.append(item)
            else:
                total += item

    return total


def total_donations_recursive(donations, depth=0, trace_rows=None):
    if trace_rows is None:
        trace_rows = []

    trace_rows.append(
        {
            "depth": depth,
            "data": str(donations),
            "action": "inspect group",
        }
    )

    total = 0
    for item in donations:
        if isinstance(item, list):
            trace_rows.append(
                {
                    "depth": depth,
                    "data": str(item),
                    "action": "recurse into nested group",
                }
            )
            total += total_donations_recursive(item, depth + 1, trace_rows)
        else:
            trace_rows.append(
                {
                    "depth": depth,
                    "data": str(item),
                    "action": f"add value {item}",
                }
            )
            total += item

    trace_rows.append(
        {
            "depth": depth,
            "data": str(donations),
            "action": f"return total {total}",
        }
    )
    return total


def print_recursive_trace(trace_rows):
    print(colorize("RECURSIVE CALL TRACE", Style.BOLD, Style.CYAN))
    header = f"{'Depth':<5} | {'Data':<20} | Action"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        action = row["action"]
        if action == "recurse into nested group":
            action = colorize(action, Style.YELLOW)
        elif action.startswith("add value") or action.startswith("return total"):
            action = colorize(action, Style.GREEN)
        print(f"{row['depth']:<5} | {row['data']:<20} | {action}")
    print()


def print_comparison_table():
    rows = [
        {
            "criterion": "Correctness",
            "strategy_a": "Works when the stack is managed correctly",
            "strategy_b": "Works when the base case and recursive step are correct",
            "notes": "Both strategies reach the same total here",
        },
        {
            "criterion": "Readability",
            "strategy_a": "Needs extra stack bookkeeping",
            "strategy_b": "Matches the nested shape more directly",
            "notes": "Recursive structure is easier to explain in this demo",
        },
        {
            "criterion": "Growth",
            "strategy_a": "Processes each value and nested group",
            "strategy_b": "Processes each value and nested group",
            "notes": "The main difference here is strategy fit, not the final total",
        },
        {
            "criterion": "Fit to data",
            "strategy_a": "Solves the problem indirectly",
            "strategy_b": "Fits nested data naturally",
            "notes": "The data shape makes recursion feel more natural",
        },
    ]

    print(colorize("STRATEGY COMPARISON TABLE", Style.BOLD, Style.CYAN))
    header = f"{'Criterion':<12} | {'Iterative Strategy':<38} | {'Recursive Strategy':<42} | Notes"
    print(header)
    print("-" * len(header))
    for row in rows:
        notes = row["notes"]
        if row["criterion"] in ("Readability", "Fit to data"):
            notes = colorize(notes, Style.GREEN)
        elif row["criterion"] == "Growth":
            notes = colorize(notes, Style.YELLOW)
        print(
            f"{row['criterion']:<12} | "
            f"{row['strategy_a']:<38} | "
            f"{row['strategy_b']:<42} | "
            f"{notes}"
        )
    print()


def main():
    trace_rows = []
    iterative_total = total_donations_iterative(DONATION_GROUP)
    recursive_total = total_donations_recursive(DONATION_GROUP, trace_rows=trace_rows)

    print(colorize("LAB 05 DEMO - STRATEGY COMPARISON", Style.BOLD, Style.CYAN))
    print("Nested donation envelopes:")
    print(DONATION_GROUP)
    print()
    print(f"Iterative total: {colorize(str(iterative_total), Style.GREEN)}")
    print(f"Recursive total: {colorize(str(recursive_total), Style.GREEN)}")
    print()
    print_recursive_trace(trace_rows)
    print_comparison_table()
    print(
        colorize(
            "Key point: both strategies can be correct, but the better fit depends on the problem structure.",
            Style.YELLOW,
        )
    )


if __name__ == "__main__":
    main()
