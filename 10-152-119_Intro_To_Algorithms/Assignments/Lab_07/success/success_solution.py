import hashlib


DATA_RECORDS = [
    {
        "name": "syllabus.txt",
        "original_text": "Course overview with schedule and grading.",
        "current_text": "Course overview with schedule and grading.",
    },
    {
        "name": "policy.txt",
        "original_text": "AI use must be disclosed in each lab reflection.",
        "current_text": "AI use must be disclosed in each lab reflection.",
    },
    {
        "name": "rubric.txt",
        "original_text": "Visible evidence is required for each submission.",
        "current_text": "Visible evidence is required for every submission.",
    },
    {
        "name": "faq.txt",
        "original_text": "Late work may be accepted with instructor approval.",
        "current_text": "Late work may be accepted with instructor approval.",
    },
    {
        "name": "checklist.txt",
        "original_text": "Include tests, explanation, and AI note if used.",
        "current_text": "Include tests, explanation, and AI note if used.",
    },
    {
        "name": "reference.txt",
        "original_text": "Hashing can support integrity checks and lookup.",
        "current_text": "Hashing can support integrity checks and lookup!",
    },
]


def compute_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def preview_text(text, width=34):
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def build_comparison_rows():
    rows = []
    for record in DATA_RECORDS:
        original_hash = compute_hash(record["original_text"])
        current_hash = compute_hash(record["current_text"])
        status = "MATCH" if original_hash == current_hash else "MISMATCH"
        rows.append(
            {
                "name": record["name"],
                "original_preview": preview_text(record["original_text"]),
                "current_preview": preview_text(record["current_text"]),
                "original_hash": original_hash[:12],
                "current_hash": current_hash[:12],
                "status": status,
            }
        )
    return rows


def print_representation_table(rows):
    print("DATA REPRESENTATION TABLE")
    header = (
        f"{'Item':<16} | {'Original Text Preview':<34} | {'Current Text Preview':<34}"
    )
    print(header)
    print("-" * len(header))
    for row in rows:
        print(
            f"{row['name']:<16} | "
            f"{row['original_preview']:<34} | "
            f"{row['current_preview']:<34}"
        )
    print()


def print_hash_comparison_table(rows):
    print("HASH COMPARISON TABLE")
    header = f"{'Item':<16} | {'Original Hash':<12} | {'Current Hash':<12} | Status"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(
            f"{row['name']:<16} | "
            f"{row['original_hash']:<12} | "
            f"{row['current_hash']:<12} | "
            f"{row['status']}"
        )
    print()


def print_assumptions_and_limits():
    print("ASSUMPTIONS AND LIMITS")
    print(
        "Assumption 1: exact text equality is the right integrity check for these records."
    )
    print(
        "Assumption 2: using the same hash function on both versions makes the comparison meaningful."
    )
    print(
        "Limitation/Risk: a hash mismatch shows that something changed, but it does not explain why the change happened or whether it matters semantically."
    )
    print()


def print_ai_data_connection():
    print("AI/DATA CONNECTION")
    print(
        "Hashing supports identity and integrity checks in data systems. It can help verify whether records, prompts, or artifacts changed before they are used in analytics or AI workflows."
    )
    print()


def main():
    rows = build_comparison_rows()

    print("LAB 07 SUCCESS VERSION - SIMILARITY, RANKING, AND HASHING")
    print("Option: hashing demonstration")
    print()
    print_representation_table(rows)
    print_hash_comparison_table(rows)
    print_assumptions_and_limits()
    print_ai_data_connection()


if __name__ == "__main__":
    main()
