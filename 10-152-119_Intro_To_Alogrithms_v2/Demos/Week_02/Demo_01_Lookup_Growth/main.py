"""Count work before interpreting wall-clock measurements."""


def scan_lookup(records, queries):
    results, inspected = [], 0
    for query in queries:
        found = None
        for record in records:
            inspected += 1
            if record["id"] == query:
                found = record
                break
        results.append(found)
    return results, inspected


def indexed_lookup(records, queries):
    index = {row["id"]: row for row in records}
    return [index.get(query) for query in queries], len(records), len(queries)


def halving_trace(size):
    trace = []
    while size > 1:
        trace.append(size)
        size = (size + 1) // 2
    return trace + [size]


def main():
    print("LOOKUP GROWTH: controlled synthetic equipment IDs")
    print("Every query misses: count each inspected record, index entry, and query.")
    print(f"{'n':>6} {'q':>6} {'scan inspections':>18} {'index entries':>15} {'indexed queries':>17}")
    for size in (4, 8, 16, 32):
        rows = [{"id": value} for value in range(size)]
        queries = [-1] * size
        scan, inspections = scan_lookup(rows, queries)
        indexed, builds, lookups = indexed_lookup(rows, queries)
        if not (scan == indexed):
            raise ValueError("Cannot compare methods that return different results.")
        print(f"{size:>6} {size:>6} {inspections:>18} {builds:>15} {lookups:>17}")
    print("\nScan work is O(q*n); here q=n, so it grows quadratically.")
    print("Index construction is O(n); queries are expected average-case O(q).")
    print("An indexed query is an API-operation count, not a CPU instruction count.")
    print("Halving contrast:", halving_trace(32), "-> logarithmic number of reductions")


if __name__ == "__main__":
    main()
