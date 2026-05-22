import os


USE_COLOR = os.environ.get("NO_COLOR") is None


class Style:
    RESET = "\033[0m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    CYAN = "\033[36m" if USE_COLOR else ""
    GREEN = "\033[32m" if USE_COLOR else ""
    RED = "\033[31m" if USE_COLOR else ""
    YELLOW = "\033[33m" if USE_COLOR else ""


def colorize(text, *styles):
    if not USE_COLOR:
        return text
    return "".join(styles) + text + Style.RESET


def colorized_cell(text, width, *styles):
    return colorize(f"{text:<{width}}", *styles)


TEST_CASES = [
    {"name": "Normal 1", "input": [2, 3, 4], "expected": 24},
    {"name": "Normal 2", "input": [5, 2], "expected": 10},
    {"name": "Normal 3", "input": [7], "expected": 7},
    {"name": "Edge case", "input": [], "expected": 1},
]


def cumulative_product_iterative(values):
    total = 1
    for value in values:
        total *= value
    return total


def cumulative_product_recursive(values, depth=0, trace_rows=None):
    if trace_rows is None:
        trace_rows = []

    trace_rows.append(
        {
            "depth": depth,
            "values": str(values),
            "action": "inspect input",
        }
    )

    if not values:
        trace_rows.append(
            {
                "depth": depth,
                "values": str(values),
                "action": "base case -> return 1",
            }
        )
        return 1

    head = values[0]
    tail = values[1:]
    trace_rows.append(
        {
            "depth": depth,
            "values": str(values),
            "action": f"multiply {head} by product of {tail}",
        }
    )
    result = head * cumulative_product_recursive(tail, depth + 1, trace_rows)
    trace_rows.append(
        {
            "depth": depth,
            "values": str(values),
            "action": f"return {result}",
        }
    )
    return result


def print_test_results():
    print(colorize("TEST RESULTS", Style.BOLD, Style.CYAN))
    header = f"{'Test':<10} | {'Input':<16} | {'Expected':<8} | {'Iterative':<9} | {'Recursive':<9} | Pass?"
    print(header)
    print("-" * len(header))

    for test_case in TEST_CASES:
        iterative_result = cumulative_product_iterative(test_case["input"])
        recursive_result = cumulative_product_recursive(
            test_case["input"], trace_rows=[]
        )
        passed = (
            iterative_result == test_case["expected"]
            and recursive_result == test_case["expected"]
        )
        pass_text = (
            colorize("Yes", Style.GREEN)
            if passed
            else colorize("No", Style.RED, Style.BOLD)
        )
        print(
            f"{test_case['name']:<10} | "
            f"{str(test_case['input']):<16} | "
            f"{test_case['expected']:<8} | "
            f"{iterative_result:<9} | "
            f"{recursive_result:<9} | "
            f"{pass_text}"
        )

    print()


def print_recursive_trace(trace_rows):
    print(colorize("RECURSIVE TRACE", Style.BOLD, Style.CYAN))
    header = f"{'Depth':<5} | {'Values':<16} | Action"
    print(header)
    print("-" * len(header))
    for row in trace_rows:
        action = row["action"]
        if "base case" in action:
            action = colorize(action, Style.YELLOW)
        elif action.startswith("return"):
            action = colorize(action, Style.GREEN)
        print(f"{row['depth']:<5} | {row['values']:<16} | {action}")
    print()


def print_comparison_table():
    rows = [
        {
            "criterion": "Correctness",
            "strategy_a": "Produces the correct product when the loop is right",
            "strategy_b": "Produces the correct product when the base case is right",
            "notes": "Both strategies pass the tests in this version",
            "style": "success",
        },
        {
            "criterion": "Readability",
            "strategy_a": "Short and direct for a flat list",
            "strategy_b": "Clear if the reader is comfortable with recursion",
            "notes": "Iteration is easier for many beginners here",
            "style": "success",
        },
        {
            "criterion": "Growth",
            "strategy_a": "Processes each value once",
            "strategy_b": "Processes each value once plus call overhead",
            "notes": "Both are acceptable at this scale, but recursion adds call overhead",
            "style": "warning",
        },
        {
            "criterion": "Fit to data",
            "strategy_a": "Strong fit for a simple flat list",
            "strategy_b": "Works, but the data does not need nesting-aware logic",
            "notes": "Iteration is the better overall fit for this problem",
            "style": "success",
        },
    ]

    print(colorize("STRATEGY COMPARISON TABLE", Style.BOLD, Style.CYAN))
    header = f"{'Criterion':<12} | {'Iterative Strategy':<40} | {'Recursive Strategy':<42} | Notes"
    print(header)
    print("-" * len(header))
    for row in rows:
        notes = row["notes"]
        if row["style"] == "warning":
            notes = colorize(notes, Style.YELLOW)
        else:
            notes = colorize(notes, Style.GREEN)
        print(
            f"{row['criterion']:<12} | "
            f"{row['strategy_a']:<40} | "
            f"{row['strategy_b']:<42} | "
            f"{notes}"
        )
    print()


def print_recommendation():
    print(colorize("RECOMMENDATION", Style.BOLD, Style.CYAN))
    print(
        "For cumulative product on a flat list, the "
        f"{colorize('iterative strategy', Style.GREEN)} is the "
        "better overall fit because it is direct, readable, and avoids recursive "
        "call overhead. The recursive strategy still works, but it is less natural "
        "for this simple data shape."
    )
    print()
    print(colorize("WHEN THE PREFERRED STRATEGY MIGHT NOT BE BEST", Style.BOLD, Style.CYAN))
    print(
        colorize(
            "If the problem involved nested groups or a tree-like structure, recursion "
            "could become the clearer fit even if iteration works.",
            Style.YELLOW,
        )
    )
    print()


def main():
    print(colorize("LAB 05 SUCCESS VERSION - STRATEGY COMPARISON", Style.BOLD, Style.CYAN))
    print("Problem: cumulative product")
    print(colorize("Optional colorized readability version", Style.YELLOW))
    print()
    print_test_results()

    trace_rows = []
    cumulative_product_recursive([2, 3, 4], trace_rows=trace_rows)
    print_recursive_trace(trace_rows)
    print_comparison_table()
    print_recommendation()


if __name__ == "__main__":
    main()
