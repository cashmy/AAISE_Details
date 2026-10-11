"""Aggregate equivalent nested donation data with recursion and an explicit stack."""

DONATIONS = [10, [5, [2, 3], []], 7]


def recursive_total(node, path="root", trace=None):
    if trace is None:
        trace = []
    if type(node) is int and node >= 0:
        trace.append(f"{path}: leaf {node}")
        return node, trace
    if not isinstance(node, list):
        raise ValueError("leaves must be nonnegative integers; groups must be lists")
    trace.append(f"{path}: enter group of {len(node)}")
    total = 0
    for position, child in enumerate(node):
        subtotal, _ = recursive_total(child, f"{path}[{position}]", trace)
        total += subtotal
    trace.append(f"{path}: return {total}")
    return total, trace


def iterative_total(node):
    stack, total, trace = [("root", node)], 0, []
    while stack:
        path, current = stack.pop()
        if type(current) is int and current >= 0:
            total += current
            action = f"add {current}; total={total}"
        elif isinstance(current, list):
            for position in range(len(current) - 1, -1, -1):
                stack.append((f"{path}[{position}]", current[position]))
            action = f"expand group of {len(current)}"
        else:
            raise ValueError("leaves must be nonnegative integers; groups must be lists")
        trace.append(f"{path}: {action}; pending={[entry[0] for entry in stack]}")
    return total, trace


def main():
    print("NESTED DONATION TOTALS: nonnegative integer units, not floating-point currency")
    print("Input:", DONATIONS)
    for label, algorithm in (("Recursive calls", recursive_total), ("Explicit stack", iterative_total)):
        result, trace = algorithm(DONATIONS)
        print(f"\n{label} -> {result}")
        for step in trace:
            print(" ", step)
    print("\nBoth traverse the same nested input; no free pre-flattening step.")
    print("Recursion stores pending work in calls; iteration stores it in an explicit stack.")


if __name__ == "__main__":
    main()
