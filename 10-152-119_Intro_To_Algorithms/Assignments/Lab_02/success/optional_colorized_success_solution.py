import os
from time import perf_counter


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


SCENARIO_NAME = "Count duplicates with nested loops vs dictionary counting"
INPUT_SIZES = [400, 800, 1600, 3200]
TRIALS = 2


def build_input(size):
    distinct_values = max(10, size // 10)
    return [index % distinct_values for index in range(size)]


def count_duplicates_nested(items):
    counts = {}
    for item in items:
        total = 0
        for candidate in items:
            if candidate == item:
                total += 1
        counts[item] = total
    return counts


def count_duplicates_with_dict(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def measure_average_seconds(function, items):
    total_seconds = 0.0
    for _ in range(TRIALS):
        start_time = perf_counter()
        function(items)
        total_seconds += perf_counter() - start_time
    return total_seconds / TRIALS


def describe_change(previous_row, current_row):
    if previous_row is None:
        return "Both approaches are manageable at small size", "neutral"

    nested_growth = current_row["nested_time"] / previous_row["nested_time"]
    dict_growth = current_row["dict_time"] / previous_row["dict_time"]

    if nested_growth > dict_growth * 2:
        return "Nested-loop counting grows more quickly", "warning"
    if nested_growth > 1 and dict_growth > 1:
        return "Both changed, but dictionary counting grew less", "warning"
    return "Dictionary counting stays steadier in this run", "success"


def build_rows():
    rows = []

    for size in INPUT_SIZES:
        items = build_input(size)
        nested_counts = count_duplicates_nested(items)
        dict_counts = count_duplicates_with_dict(items)
        same_output = nested_counts == dict_counts
        if not same_output:
            raise ValueError("The two approaches did not produce the same counts.")

        row = {
            "size": size,
            "nested_time": measure_average_seconds(count_duplicates_nested, items),
            "dict_time": measure_average_seconds(count_duplicates_with_dict, items),
            "same_output": "Yes",
        }
        row["change"], row["change_style"] = describe_change(
            rows[-1] if rows else None, row
        )
        rows.append(row)

    return rows


def style_change(row):
    if row["change_style"] == "warning":
        return colorize(row["change"], Style.YELLOW)
    if row["change_style"] == "success":
        return colorize(row["change"], Style.GREEN)
    return row["change"]


def style_same_output_cell(value, width):
    return colorize(f"{value:<{width}}", Style.GREEN)


def print_timing_table(rows):
    print(colorize("TIMING TABLE", Style.BOLD, Style.CYAN))
    header = (
        f"{'Input Size':<12} | {'Nested Loop Time':<18} | {'Dictionary Time':<17} | "
        f"{'Same Output?':<12} | What Changed?"
    )
    print(header)
    print("-" * len(header))

    for row in rows:
        same_output = style_same_output_cell(row["same_output"], 12)
        print(
            f"{row['size']:<12,} | "
            f"{row['nested_time']:<18.6f} | "
            f"{row['dict_time']:<17.6f} | "
            f"{same_output} | "
            f"{style_change(row)}"
        )

    print()


def print_comparison_summary(rows):
    nested_ratio = rows[-1]["nested_time"] / rows[0]["nested_time"]
    dict_ratio = rows[-1]["dict_time"] / rows[0]["dict_time"]

    print(colorize("COMPARISON SUMMARY", Style.BOLD, Style.CYAN))
    header = (
        f"{'Approach':<24} | {'Informal Growth Description':<36} | Evidence From Run"
    )
    print(header)
    print("-" * len(header))
    print(
        f"{'Nested-loop counting':<24} | "
        f"{'Time rises quickly as input grows':<36} | "
        f"{colorize(f'Last run was about {nested_ratio:.1f}x the first run', Style.YELLOW)}"
    )
    print(
        f"{'Dictionary counting':<24} | "
        f"{'Time rises more slowly in this run':<36} | "
        f"{colorize(f'Last run was about {dict_ratio:.1f}x the first run', Style.GREEN)}"
    )
    print()


def print_limitation_note():
    print(colorize("LIMITATION NOTE", Style.BOLD, Style.CYAN))
    print(
        colorize(
            "These timings come from one computer, a small set of input sizes, "
            "and a simple average. Exact seconds may change on another machine "
            "or with more trials.",
            Style.YELLOW,
        )
    )
    print()


def main():
    rows = build_rows()
    print(colorize("LAB 02 SUCCESS VERSION - GROWTH AND BIG-O INTUITION", Style.BOLD, Style.CYAN))
    print(SCENARIO_NAME)
    print(colorize("Optional colorized readability version", Style.YELLOW))
    print()
    print_timing_table(rows)
    print_comparison_summary(rows)
    print_limitation_note()


if __name__ == "__main__":
    main()
