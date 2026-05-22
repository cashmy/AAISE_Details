import os

from success_solution import build_comparison_rows


def use_color():
    return not os.getenv("NO_COLOR")


def colorize(text, code):
    if not use_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def match_text(text):
    return colorize(text, "92")


def mismatch_text(text):
    return colorize(text, "91")


def note_text(text):
    return colorize(text, "95")


def padded_colored_text(text, width, style_function):
    padded_text = f"{text:<{width}}"
    return style_function(padded_text)


def print_representation_table(rows):
    print(heading("DATA REPRESENTATION TABLE"))
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
    print(heading("HASH COMPARISON TABLE"))
    header = f"{'Item':<16} | {'Original Hash':<12} | {'Current Hash':<12} | Status"
    print(header)
    print("-" * len(header))
    for row in rows:
        if row["status"] == "MATCH":
            status_cell = padded_colored_text(row["status"], 8, match_text)
        else:
            status_cell = padded_colored_text(row["status"], 8, mismatch_text)

        print(
            f"{row['name']:<16} | "
            f"{row['original_hash']:<12} | "
            f"{row['current_hash']:<12} | "
            f"{status_cell}"
        )
    print()


def print_notes():
    print(note_text("ASSUMPTIONS AND LIMITS"))
    print(
        note_text(
            "Assumption 1: exact text equality is the right integrity check for these records."
        )
    )
    print(
        note_text(
            "Assumption 2: using the same hash function on both versions makes the comparison meaningful."
        )
    )
    print(
        note_text(
            "Limitation/Risk: a hash mismatch shows that something changed, but it does not explain why the change happened or whether it matters semantically."
        )
    )
    print()
    print(note_text("AI/DATA CONNECTION"))
    print(
        note_text(
            "Hashing supports identity and integrity checks in data systems. It can help verify whether records, prompts, or artifacts changed before they are used in analytics or AI workflows."
        )
    )
    print()


def main():
    rows = build_comparison_rows()

    print(
        heading(
            "LAB 07 OPTIONAL COLORIZED SUCCESS VERSION - SIMILARITY, RANKING, AND HASHING"
        )
    )
    print(f"Option: {note_text('hashing demonstration')}")
    print()
    print_representation_table(rows)
    print_hash_comparison_table(rows)
    print_notes()


if __name__ == "__main__":
    main()
