"""
Final Part 1 - Task 1 Starter
Equipment Checkout Eligibility

Use this file as a starting structure. You are responsible for defining precise
rules, completing the algorithm, creating test cases, and documenting evidence
in your README.md file.
"""


def decide_checkout_eligibility(request):
    """
    Return one decision:
    - "approved"
    - "denied"
    - "needs review"

    Suggested process:
    1. Check for missing or unclear information.
    2. Check rules that should deny the request.
    3. Check rules that require review.
    4. Approve only when the required conditions are met.
    """
    # TODO: read values from request.
    # TODO: write denial rules.
    # TODO: write needs-review rules.
    # TODO: write approval rule.
    return "TODO"


TEST_CASES = [
    {
        "name": "Normal approved",
        "input": {
            # TODO: add request fields.
        },
        "expected": "approved",
    },
    {
        "name": "Normal denied",
        "input": {
            # TODO: add request fields.
        },
        "expected": "denied",
    },
    {
        "name": "Normal review",
        "input": {
            # TODO: add request fields.
        },
        "expected": "needs review",
    },
    {
        "name": "Edge case 1",
        "input": {
            # TODO: add edge-case request fields.
        },
        "expected": "TODO",
    },
    {
        "name": "Edge case 2",
        "input": {
            # TODO: add edge-case request fields.
        },
        "expected": "TODO",
    },
]


def main():
    print("Task 1 starter loaded.")
    print("Complete decide_checkout_eligibility() and your test cases.")
    print("Record expected and actual results in your README.md evidence table.")


if __name__ == "__main__":
    main()
