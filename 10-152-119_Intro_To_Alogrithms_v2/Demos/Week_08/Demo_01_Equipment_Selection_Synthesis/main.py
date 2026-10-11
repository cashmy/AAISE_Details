"""Defend two equivalent approaches, then change a requirement and retest."""

EQUIPMENT = [{"id": "E01", "type": "laptop", "available": True, "battery": 80},
             {"id": "E02", "type": "laptop", "available": False, "battery": 90},
             {"id": "E03", "type": "tablet", "available": True, "battery": 95},
             {"id": "E04", "type": "laptop", "available": True, "battery": 50}]


def eligible(row, minimum_battery):
    return row["type"] == "laptop" and row["available"] and row["battery"] >= minimum_battery


def scan_requests(rows, queries, minimum_battery):
    results, inspections = [], 0
    for query in queries:
        found = None
        for row in rows:
            inspections += 1
            if row["id"] == query and eligible(row, minimum_battery):
                found = row
                break
        results.append(found)
    return results, inspections


def indexed_requests(rows, queries, minimum_battery):
    index = {row["id"]: row for row in rows if eligible(row, minimum_battery)}
    return [index.get(query) for query in queries], len(rows), len(queries)


def main():
    print("EQUIPMENT SELECTION SYNTHESIS: validated records with unique IDs")
    queries = ["E01", "E04", "E03", "missing"]
    for threshold in (50, 80):
        scan, inspections = scan_requests(EQUIPMENT, queries, threshold)
        indexed, construction, lookups = indexed_requests(EQUIPMENT, queries, threshold)
        print(f"\nRequest: available laptops, battery >= {threshold}; queries={queries}")
        print("Selected results:", [row["id"] if row else None for row in indexed])
        print("Equivalent approaches:", scan == indexed)
        print(f"Scan inspections={inspections}; index construction inspections={construction}; lookup calls={lookups}")
    print("\nRule change: E04 no longer qualifies at 80. E01 must still qualify.")
    print("Counts establish observed work, not a universal runtime advantage.")
    print("A cached selection index must be rebuilt if its data or eligibility rule changes.")


if __name__ == "__main__":
    main()
