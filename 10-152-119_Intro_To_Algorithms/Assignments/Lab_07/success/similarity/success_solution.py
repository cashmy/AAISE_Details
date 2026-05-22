STUDENT_PROFILE = {
    "name": "Jordan",
    "goal": "Prepare for a Python and algorithms quiz with practice and debugging support.",
    "tags": {"python", "algorithms", "practice", "debugging"},
}

STUDY_RESOURCES = [
    {
        "name": "Python Drill Cards",
        "format": "flash cards",
        "tags": {"python", "practice", "visual"},
    },
    {
        "name": "Algorithm Walkthrough Videos",
        "format": "video series",
        "tags": {"algorithms", "visual", "practice"},
    },
    {
        "name": "Debugging Lab Sheets",
        "format": "worksheet pack",
        "tags": {"python", "debugging", "practice"},
    },
    {
        "name": "Data Story Notes",
        "format": "reading guide",
        "tags": {"data", "ai", "visual"},
    },
    {
        "name": "Code Trace Clinic",
        "format": "guided examples",
        "tags": {"python", "algorithms", "debugging", "visual"},
    },
    {
        "name": "AI Prompt Reflection",
        "format": "reflection prompt",
        "tags": {"ai", "debugging", "writing"},
    },
]


def similarity_score(profile_tags, resource_tags):
    shared_tags = profile_tags & resource_tags
    all_tags = profile_tags | resource_tags
    score = len(shared_tags) / len(all_tags)
    return score, shared_tags, all_tags


def classify_match(score, top_score):
    if score == top_score:
        return "top recommendation"
    if top_score - score <= 0.10 and score > 0:
        return "close option"
    if score > 0:
        return "support option"
    return "not aligned"


def build_ranking_rows():
    rows = []
    for resource in STUDY_RESOURCES:
        score, shared_tags, all_tags = similarity_score(
            STUDENT_PROFILE["tags"], resource["tags"]
        )
        rows.append(
            {
                "name": resource["name"],
                "format": resource["format"],
                "tags": sorted(resource["tags"]),
                "shared_tags": sorted(shared_tags),
                "union_size": len(all_tags),
                "score": score,
            }
        )

    rows.sort(key=lambda row: (-row["score"], row["name"]))
    top_score = rows[0]["score"] if rows else 0.0
    for row in rows:
        row["note"] = classify_match(row["score"], top_score)
    return rows


def print_profile_summary():
    print("STUDENT NEED PROFILE")
    print(f"Student: {STUDENT_PROFILE['name']}")
    print(f"Goal: {STUDENT_PROFILE['goal']}")
    print(f"Need tags: {sorted(STUDENT_PROFILE['tags'])}")
    print()


def print_representation_table(rows):
    print("RESOURCE REPRESENTATION TABLE")
    header = f"{'Resource':<28} | {'Format':<18} | Tags"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(f"{row['name']:<28} | {row['format']:<18} | {row['tags']}")
    print()


def print_ranking_table(rows):
    print("SIMILARITY RANKING TABLE")
    header = (
        f"{'Rank':<4} | {'Resource':<28} | {'Shared Tags':<30} | {'Score':<5} | Note"
    )
    print(header)
    print("-" * len(header))
    for index, row in enumerate(rows, start=1):
        score_text = f"{row['score']:.2f}"
        print(
            f"{index:<4} | "
            f"{row['name']:<28} | "
            f"{str(row['shared_tags']):<30} | "
            f"{score_text:<5} | "
            f"{row['note']}"
        )
    print()


def print_final_recommendation(rows):
    top_row = rows[0]
    print("FINAL RECOMMENDATION")
    print(
        f"Recommend '{top_row['name']}' because it matches {len(top_row['shared_tags'])} of the student's need tags and scores {top_row['score']:.2f}."
    )
    print(f"Shared tags: {top_row['shared_tags']}")
    print(
        "Why it helps: it stays close to the student's need profile without claiming it is the only good study choice."
    )
    print()


def print_assumptions_and_limitations():
    print("ASSUMPTIONS AND LIMITATIONS")
    print(
        "Assumption 1: simple shared tags are a reasonable way to compare a student's needs to a resource."
    )
    print(
        "Assumption 2: each tag matters equally, even though a student might value debugging or practice more than other needs."
    )
    print(
        "Limitation: the ranking does not measure difficulty level, time required, or whether the student learns better from reading, video, or practice."
    )
    print()


def print_ai_data_connection():
    print("AI/DATA CONNECTION")
    print(
        "This is a small recommendation example. Many AI and data systems begin by representing people or items as features, comparing overlap, and ranking options before a human decides what to use."
    )
    print()


def main():
    rows = build_ranking_rows()

    print("LAB 07 SUCCESS VERSION - SIMILARITY / RECOMMENDATION OPTION")
    print("Option: study resource recommendation by tag overlap")
    print()
    print_profile_summary()
    print_representation_table(rows)
    print_ranking_table(rows)
    print_final_recommendation(rows)
    print_assumptions_and_limitations()
    print_ai_data_connection()


if __name__ == "__main__":
    main()
