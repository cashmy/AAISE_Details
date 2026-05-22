import os


REFERENCE_SONG = {
    "name": "Skyline Echo",
    "tags": {"synth-pop", "uplifting", "fast", "vocal"},
}

CANDIDATE_SONGS = [
    {"name": "Neon Steps", "tags": {"synth-pop", "uplifting", "dance", "vocal"}},
    {"name": "Quiet Harbor", "tags": {"acoustic", "calm", "slow", "instrumental"}},
    {"name": "Midnight Drive", "tags": {"synth-pop", "moody", "fast", "instrumental"}},
    {"name": "City Sparks", "tags": {"uplifting", "fast", "guitar", "vocal"}},
    {"name": "Rain Signals", "tags": {"electronic", "moody", "slow", "vocal"}},
]


def use_color():
    return not os.getenv("NO_COLOR")


def colorize(text, code):
    if not use_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def heading(text):
    return colorize(text, "96")


def top_match_text(text):
    return colorize(text, "92")


def note_text(text):
    return colorize(text, "95")


def padded_colored_text(text, width, style_function):
    padded_text = f"{text:<{width}}"
    return style_function(padded_text)


def similarity_score(reference_tags, candidate_tags):
    shared = reference_tags & candidate_tags
    union = reference_tags | candidate_tags
    score = len(shared) / len(union)
    return score, shared


def build_ranking_rows():
    rows = []
    for candidate in CANDIDATE_SONGS:
        score, shared_tags = similarity_score(REFERENCE_SONG["tags"], candidate["tags"])
        rows.append(
            {
                "name": candidate["name"],
                "tags": sorted(candidate["tags"]),
                "score": score,
                "shared_tags": sorted(shared_tags),
            }
        )

    rows.sort(key=lambda row: (-row["score"], row["name"]))
    return rows


def print_feature_table(ranking_rows):
    print(heading("ITEM-FEATURE TABLE"))
    print(f"Reference song: {note_text(REFERENCE_SONG['name'])}")
    print(f"Reference tags: {sorted(REFERENCE_SONG['tags'])}")
    print()

    header = f"{'Song':<16} | Tags"
    print(header)
    print("-" * len(header))
    for row in ranking_rows:
        print(f"{row['name']:<16} | {row['tags']}")
    print()


def print_ranking_table(ranking_rows):
    print(heading("RANKING TABLE"))
    header = f"{'Rank':<4} | {'Song':<16} | {'Shared Tags':<30} | {'Score':<5} | Note"
    print(header)
    print("-" * len(header))

    for index, row in enumerate(ranking_rows, start=1):
        score_text = f"{row['score']:.2f}"
        note = "top match" if index == 1 else "candidate"

        rank_cell = f"{index:<4}"
        score_cell = f"{score_text:<5}"
        note_cell = note

        if index == 1:
            rank_cell = padded_colored_text(str(index), 4, top_match_text)
            score_cell = padded_colored_text(score_text, 5, top_match_text)
            note_cell = top_match_text(note)

        print(
            f"{rank_cell} | "
            f"{row['name']:<16} | "
            f"{str(row['shared_tags']):<30} | "
            f"{score_cell} | "
            f"{note_cell}"
        )
    print()


def print_summary(ranking_rows):
    top_row = ranking_rows[0]
    print(note_text("ASSUMPTION AND LIMIT SUMMARY"))
    print(
        "Assumption 1: shared tags are a reasonable proxy for similarity in this tiny example."
    )
    print(
        "Assumption 2: all tags matter equally in the score, even though some music features may matter more than others."
    )
    print(
        "Limitation: the ranking ignores lyrics, artist preference, song length, and many other factors that could change a real recommendation."
    )
    print()
    print(
        top_match_text(
            f"Top recommendation: {top_row['name']} with score {top_row['score']:.2f}"
        )
    )


def main():
    ranking_rows = build_ranking_rows()

    print(heading("LAB 07 DEMO - SIMILARITY, RANKING, AND HASHING"))
    print()
    print_feature_table(ranking_rows)
    print_ranking_table(ranking_rows)
    print_summary(ranking_rows)


if __name__ == "__main__":
    main()
