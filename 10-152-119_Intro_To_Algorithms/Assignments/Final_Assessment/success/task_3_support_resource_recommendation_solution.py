"""
Final Success Example - Task 3
Support Resource Recommendation

This is one acceptable solution, not the only correct solution.
"""


REQUEST_PROFILE = {
    "summary": "User cannot sign in and needs beginner-friendly password help.",
    "tags": {"account", "password", "beginner", "documentation"},
}

SUPPORT_RESOURCES = [
    {
        "name": "Password Reset Guide",
        "tags": {"password", "account", "documentation", "beginner"},
    },
    {
        "name": "Network Troubleshooting Checklist",
        "tags": {"network", "device", "documentation"},
    },
    {
        "name": "Account Recovery Video",
        "tags": {"account", "password", "video", "beginner"},
    },
    {
        "name": "Urgent Escalation Form",
        "tags": {"urgent", "account", "staff"},
    },
    {
        "name": "Device Setup Walkthrough",
        "tags": {"device", "beginner", "video"},
    },
]


def similarity_score(request_tags, resource_tags):
    shared_tags = request_tags & resource_tags
    all_tags = request_tags | resource_tags
    score = len(shared_tags) / len(all_tags)
    return score, shared_tags


def classify_score(score, top_score):
    if score == top_score:
        return "top recommendation"
    if score >= 0.40:
        return "strong option"
    if score > 0:
        return "partial match"
    return "not aligned"


def build_ranking_rows():
    rows = []
    for resource in SUPPORT_RESOURCES:
        score, shared_tags = similarity_score(
            REQUEST_PROFILE["tags"], resource["tags"]
        )
        rows.append(
            {
                "name": resource["name"],
                "tags": sorted(resource["tags"]),
                "shared_tags": sorted(shared_tags),
                "score": score,
            }
        )

    rows.sort(key=lambda row: (-row["score"], row["name"]))
    top_score = rows[0]["score"]
    for row in rows:
        row["note"] = classify_score(row["score"], top_score)
    return rows


def print_representation_table(rows):
    print("RESOURCE REPRESENTATION TABLE")
    header = f"{'Resource':<34} | Tags"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(f"{row['name']:<34} | {row['tags']}")
    print()


def print_ranking_table(rows):
    print("RANKING TABLE")
    header = f"{'Rank':<4} | {'Resource':<34} | {'Shared Tags':<34} | {'Score':<5} | Note"
    print(header)
    print("-" * len(header))
    for index, row in enumerate(rows, start=1):
        print(
            f"{index:<4} | "
            f"{row['name']:<34} | "
            f"{str(row['shared_tags']):<34} | "
            f"{row['score']:<5.2f} | "
            f"{row['note']}"
        )
    print()


def print_results():
    rows = build_ranking_rows()
    top_row = rows[0]

    print("TASK 3 SUCCESS EXAMPLE - SUPPORT RESOURCE RECOMMENDATION")
    print("This is one acceptable solution, not the only correct solution.")
    print()
    print(f"Request: {REQUEST_PROFILE['summary']}")
    print(f"Request tags: {sorted(REQUEST_PROFILE['tags'])}")
    print()
    print_representation_table(rows)
    print_ranking_table(rows)
    print(
        f"Recommendation: {top_row['name']} because it shares "
        f"{len(top_row['shared_tags'])} tags and scores {top_row['score']:.2f}."
    )
    print(
        "Limitation: this simple tag-overlap model does not measure resource quality, "
        "reading level, time required, or user preference."
    )


if __name__ == "__main__":
    print_results()
