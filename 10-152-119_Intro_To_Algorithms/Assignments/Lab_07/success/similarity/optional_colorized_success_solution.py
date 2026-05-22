import os

from success_solution import STUDENT_PROFILE, build_ranking_rows


def use_color():
    return not os.getenv("NO_COLOR")


def colorize(text, code):
    if not use_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def top_text(text):
    return colorize(text, "92")


def close_text(text):
    return colorize(text, "93")


def note_text(text):
    return colorize(text, "95")


def warning_text(text):
    return colorize(text, "91")


def padded_colored_text(text, width, style_function):
    padded_text = f"{text:<{width}}"
    return style_function(padded_text)


def print_profile_summary():
    print(heading("STUDENT NEED PROFILE"))
    print(f"Student: {note_text(STUDENT_PROFILE['name'])}")
    print(f"Goal: {STUDENT_PROFILE['goal']}")
    print(f"Need tags: {sorted(STUDENT_PROFILE['tags'])}")
    print()


def print_representation_table(rows):
    print(heading("RESOURCE REPRESENTATION TABLE"))
    header = f"{'Resource':<28} | {'Format':<18} | Tags"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(f"{row['name']:<28} | {row['format']:<18} | {row['tags']}")
    print()


def print_ranking_table(rows):
    print(heading("SIMILARITY RANKING TABLE"))
    header = (
        f"{'Rank':<4} | {'Resource':<28} | {'Shared Tags':<30} | {'Score':<5} | Note"
    )
    print(header)
    print("-" * len(header))
    for index, row in enumerate(rows, start=1):
        rank_cell = f"{index:<4}"
        score_text = f"{row['score']:.2f}"
        score_cell = f"{score_text:<5}"
        note_cell = row["note"]

        if row["note"] == "top recommendation":
            rank_cell = padded_colored_text(str(index), 4, top_text)
            score_cell = padded_colored_text(score_text, 5, top_text)
            note_cell = top_text(row["note"])
        elif row["note"] == "close option":
            rank_cell = padded_colored_text(str(index), 4, close_text)
            score_cell = padded_colored_text(score_text, 5, close_text)
            note_cell = close_text(row["note"])

        print(
            f"{rank_cell} | "
            f"{row['name']:<28} | "
            f"{str(row['shared_tags']):<30} | "
            f"{score_cell} | "
            f"{note_cell}"
        )
    print()


def print_final_recommendation(rows):
    top_row = rows[0]
    print(heading("FINAL RECOMMENDATION"))
    print(
        top_text(
            f"Recommend '{top_row['name']}' because it matches {len(top_row['shared_tags'])} of the student's need tags and scores {top_row['score']:.2f}."
        )
    )
    print(f"Shared tags: {top_text(str(top_row['shared_tags']))}")
    print(
        "Why it helps: it stays close to the student's need profile without claiming it is the only good study choice."
    )
    print()


def print_assumptions_and_limitations():
    print(note_text("ASSUMPTIONS AND LIMITATIONS"))
    print(
        note_text(
            "Assumption 1: simple shared tags are a reasonable way to compare a student's needs to a resource."
        )
    )
    print(
        note_text(
            "Assumption 2: each tag matters equally, even though a student might value debugging or practice more than other needs."
        )
    )
    print(
        warning_text(
            "Limitation: the ranking does not measure difficulty level, time required, or whether the student learns better from reading, video, or practice."
        )
    )
    print()


def print_ai_data_connection():
    print(note_text("AI/DATA CONNECTION"))
    print(
        note_text(
            "This is a small recommendation example. Many AI and data systems begin by representing people or items as features, comparing overlap, and ranking options before a human decides what to use."
        )
    )
    print()


def main():
    rows = build_ranking_rows()

    print(
        heading(
            "LAB 07 OPTIONAL COLORIZED SUCCESS VERSION - SIMILARITY / RECOMMENDATION OPTION"
        )
    )
    print(f"Option: {note_text('study resource recommendation by tag overlap')}")
    print()
    print_profile_summary()
    print_representation_table(rows)
    print_ranking_table(rows)
    print_final_recommendation(rows)
    print_assumptions_and_limitations()
    print_ai_data_connection()


if __name__ == "__main__":
    main()
