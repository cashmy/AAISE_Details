"""
Final Part 1 - Task 3 Starter
Support Resource Recommendation

Create a small ranking or recommendation algorithm using request tags and
resource tags. Document the ranking evidence in your README.md file.
"""


REQUEST_PROFILE = {
    "summary": "Replace with a support request summary",
    "tags": {"replace", "these", "tags"},
}

SUPPORT_RESOURCES = [
    {
        "name": "Replace Resource 1",
        "tags": {"replace", "tags"},
    },
    {
        "name": "Replace Resource 2",
        "tags": {"replace", "tags"},
    },
    {
        "name": "Replace Resource 3",
        "tags": {"replace", "tags"},
    },
    {
        "name": "Replace Resource 4",
        "tags": {"replace", "tags"},
    },
    {
        "name": "Replace Resource 5",
        "tags": {"replace", "tags"},
    },
]


def similarity_score(request_tags, resource_tags):
    """
    Return a score that compares request_tags and resource_tags.

    A simple option:
    score = number of shared tags / number of unique tags across both sets
    """
    # TODO: calculate shared tags.
    # TODO: calculate all unique tags.
    # TODO: return a numeric score and any evidence you want to display.
    return 0.0, set()


def build_ranking_rows():
    """
    Build sorted ranking rows for the support resources.
    """
    rows = []
    for resource in SUPPORT_RESOURCES:
        # TODO: calculate score and shared-tag evidence.
        # TODO: append a row with resource name, tags, score, and note.
        pass

    # TODO: sort rows from strongest recommendation to weakest.
    return rows


def main():
    print("Task 3 starter loaded.")
    print("Replace the request profile and support resources.")
    print("Complete the similarity score and ranking rows.")
    print("Record representation, ranking, recommendation, assumptions, and limitations in README.md.")


if __name__ == "__main__":
    main()
