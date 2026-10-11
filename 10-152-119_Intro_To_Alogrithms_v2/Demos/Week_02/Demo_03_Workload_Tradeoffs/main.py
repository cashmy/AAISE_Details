"""Compare small and large query workloads, including index construction."""

from statistics import median
from time import perf_counter


def scan(records, queries):
    results, count = [], 0
    for query in queries:
        found = None
        for row in records:
            count += 1
            if row["id"] == query:
                found = row
                break
        results.append(found)
    return results, count


def indexed(records, queries):
    index = {row["id"]: row for row in records}
    return [index.get(query) for query in queries]


def milliseconds(action):
    samples = []
    for _ in range(5):
        start = perf_counter()
        action()
        samples.append(1000 * (perf_counter() - start))
    return median(samples)


def main():
    print("WORKLOAD TRADEOFFS: 2,000 synthetic equipment records")
    rows = [{"id": value} for value in range(2000)]
    workloads = [("one early hit", [0]), ("many mixed queries", [0, 1999, -1] * 100)]
    for label, queries in workloads:
        results, inspections = scan(rows, queries)
        if not (results == indexed(rows, queries)):
            raise ValueError("Cannot compare methods that return different results.")
        scan_ms = milliseconds(lambda: scan(rows, queries))
        index_ms = milliseconds(lambda: indexed(rows, queries))
        print(f"\n{label}: q={len(queries)}")
        print(f"  Scan inspections: {inspections}")
        print(f"  Indexed work: {len(rows)} entries + {len(queries)} lookup API calls")
        print(f"  Scan median: {scan_ms:.4f} ms; fresh-index median: {index_ms:.4f} ms")
        observed = "scan" if scan_ms < index_ms else "fresh index"
        print(f"  Faster in this measured workload: {observed} (not a universal winner)")
    print("\nAn index needs additional storage. Reusing it changes the cost model.")
    print("Counts describe different operations; do not treat them as equal-duration units.")


if __name__ == "__main__":
    main()
