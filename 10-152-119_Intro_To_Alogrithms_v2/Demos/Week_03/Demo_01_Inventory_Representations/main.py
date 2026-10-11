"""Match equipment representations to lookup, update, and membership tasks."""


def build_index(records):
    index = {}
    for record in records:
        if record["id"] in index:
            raise ValueError(f"duplicate ID: {record['id']}")
        index[record["id"]] = record.copy()
    return index


def scan_lookup(records, equipment_id):
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == equipment_id:
            return record, inspected
    return None, inspected


def fixture():
    return [
        {"id": "E01", "type": "laptop", "available": True},
        {"id": "E02", "type": "tablet", "available": True},
        {"id": "E03", "type": "laptop", "available": False},
    ]


def main():
    rows = fixture()
    index = build_index(rows)
    types = {row["type"] for row in rows}
    print("INVENTORY REPRESENTATIONS")
    print("List lookup E03:", scan_lookup(rows, "E03"))
    print("Dictionary lookup E03:", index.get("E03"))
    print("Unique equipment types:", sorted(types))
    print("Is camera a known type?", "camera" in types)
    index["E01"]["available"] = False
    print("\nUpdate in independent index:", index["E01"])
    print("Original list record remains:", rows[0])
    print("Available records still require a filter:", [key for key, row in index.items() if row["available"]])
    try:
        build_index(rows + [rows[0]])
    except ValueError as error:
        print("Duplicate policy:", error)
    print("ID lookup, arbitrary filtering, and membership are different contracts.")


if __name__ == "__main__":
    main()
