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


INPUT_SIZES = [1000, 10000, 50000, 100000]
TRIALS = 3
PROBE_REPEATS = 50


def manual_list_lookup(items, target):
    for value in items:
        if value == target:
            return True
    return False


def batch_list_lookup(items, targets):
    results = []
    for target in targets:
        results.append(manual_list_lookup(items, target))
    return results


def batch_set_lookup(item_set, targets):
    results = []
    for target in targets:
        results.append(target in item_set)
    return results


def build_probe_values(size):
    base_targets = [size - 1, size // 2, size, -1]
    return base_targets * PROBE_REPEATS


def measure_average_seconds(function, *args):
    total_seconds = 0.0
    for _ in range(TRIALS):
        start_time = perf_counter()
        function(*args)
        total_seconds += perf_counter() - start_time
    return total_seconds / TRIALS


def describe_change(previous_row, current_row):
    if previous_row is None:
        return "Both are fast at small size", "neutral"

    list_growth = current_row["list_time"] / previous_row["list_time"]
    set_growth = current_row["set_time"] / previous_row["set_time"]

    if list_growth > set_growth * 2:
        return "List lookup grows more noticeably", "warning"
    if list_growth > 1 and set_growth > 1:
        return "Both changed, but list lookup grew more", "warning"
    return "Set lookup changes less in this demo", "success"


def build_rows():
    rows = []

    for size in INPUT_SIZES:
        items = list(range(size))
        item_set = set(items)
        targets = build_probe_values(size)

        list_results = batch_list_lookup(items, targets)
        set_results = batch_set_lookup(item_set, targets)
        if list_results != set_results:
            raise ValueError("The two demo approaches produced different results.")

        row = {
            "size": size,
            "list_time": measure_average_seconds(batch_list_lookup, items, targets),
            "set_time": measure_average_seconds(batch_set_lookup, item_set, targets),
        }
        row["change"], row["change_style"] = describe_change(
            rows[-1] if rows else None, row
        )
        rows.append(row)

    return rows


def print_timing_table(rows):
    print(colorize("DEMO TIMING TABLE", Style.BOLD, Style.CYAN))
    header = (
        f"{'Input Size':<12} | {'Manual List Lookup':<20} | "
        f"{'Set Membership':<16} | What Changed?"
    )
    print(header)
    print("-" * len(header))

    for row in rows:
        change_text = row["change"]
        if row["change_style"] == "warning":
            change_text = colorize(change_text, Style.YELLOW)
        elif row["change_style"] == "success":
            change_text = colorize(change_text, Style.GREEN)
        print(
            f"{row['size']:<12,} | "
            f"{row['list_time']:<20.6f} | "
            f"{row['set_time']:<16.6f} | "
            f"{change_text}"
        )

    print()


def print_comparison_summary(rows):
    list_ratio = rows[-1]["list_time"] / rows[0]["list_time"]
    set_ratio = rows[-1]["set_time"] / rows[0]["set_time"]

    print(colorize("DEMO COMPARISON SUMMARY", Style.BOLD, Style.CYAN))
    header = (
        f"{'Approach':<22} | {'Informal Growth Description':<34} | Evidence From Demo"
    )
    print(header)
    print("-" * len(header))
    print(
        f"{'Manual list lookup':<22} | "
        f"{'Time rises as input grows':<34} | "
        f"{colorize(f'Last run was about {list_ratio:.1f}x the first run', Style.YELLOW)}"
    )
    print(
        f"{'Set membership':<22} | "
        f"{'Time changes less in this demo':<34} | "
        f"{colorize(f'Last run was about {set_ratio:.1f}x the first run', Style.GREEN)}"
    )
    print()


def main():
    rows = build_rows()
    print(colorize("LAB 02 DEMO - GROWTH AND BIG-O INTUITION", Style.BOLD, Style.CYAN))
    print()
    print("This demo compares manual list lookup with set membership lookup.")
    print(f"Each timing row averages {TRIALS} trial(s) over repeated lookups.")
    print()
    print_timing_table(rows)
    print_comparison_summary(rows)
    print(
        colorize(
            "Reminder: exact numbers may vary by machine and background activity.",
            Style.YELLOW,
        )
    )


if __name__ == "__main__":
    main()
