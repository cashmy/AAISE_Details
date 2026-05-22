"""
Final Success Example - Task 1
Equipment Checkout Eligibility

This is one acceptable solution, not the only correct solution.
"""


# The expected values are included here for instructional clarity.
# In a real-world dataset, the correct answer usually would not be supplied.
# For this success example, the expected value records our mental expectation
# so the algorithm's actual output can be checked against it.
TEST_CASES = [
    {
        "name": "Approved",
        "input": {
            "account_active": True,
            "training_complete": True,
            "device_available": True,
            "has_overdue_items": False,
            "requested_days": 3,
            "supervisor_approved": False,
        },
        "expected": "approved",
    },
    {
        "name": "Inactive account",
        "input": {
            "account_active": False,
            "training_complete": True,
            "device_available": True,
            "has_overdue_items": False,
            "requested_days": 3,
            "supervisor_approved": False,
        },
        "expected": "denied",
    },
    {
        "name": "Training missing",
        "input": {
            "account_active": True,
            "training_complete": False,
            "device_available": True,
            "has_overdue_items": False,
            "requested_days": 3,
            "supervisor_approved": False,
        },
        "expected": "needs review",
    },
    {
        "name": "No devices",
        "input": {
            "account_active": True,
            "training_complete": True,
            "device_available": False,
            "has_overdue_items": False,
            "requested_days": 3,
            "supervisor_approved": False,
        },
        "expected": "denied",
    },
    {
        "name": "Long checkout approved",
        "input": {
            "account_active": True,
            "training_complete": True,
            "device_available": True,
            "has_overdue_items": False,
            "requested_days": 10,
            "supervisor_approved": True,
        },
        "expected": "approved",
    },
    {
        "name": "Long checkout no approval",
        "input": {
            "account_active": True,
            "training_complete": True,
            "device_available": True,
            "has_overdue_items": False,
            "requested_days": 10,
            "supervisor_approved": False,
        },
        "expected": "needs review",
    },
]


def decide_checkout_eligibility(request):
    if not request["account_active"]:
        return "denied"

    if request["has_overdue_items"]:
        return "denied"

    if not request["device_available"]:
        return "denied"

    if not request["training_complete"]:
        return "needs review"

    if request["requested_days"] > 7 and not request["supervisor_approved"]:
        return "needs review"

    return "approved"


def print_results():
    print("TASK 1 SUCCESS EXAMPLE - EQUIPMENT CHECKOUT ELIGIBILITY")
    print("This is one acceptable solution, not the only correct solution.")
    print()
    header = f"{'Test':<28} | {'Expected':<12} | {'Actual':<12} | Pass?"
    print(header)
    print("-" * len(header))

    for test_case in TEST_CASES:
        actual = decide_checkout_eligibility(test_case["input"])
        passed = "Yes" if actual == test_case["expected"] else "No"
        print(
            f"{test_case['name']:<28} | "
            f"{test_case['expected']:<12} | "
            f"{actual:<12} | "
            f"{passed}"
        )


if __name__ == "__main__":
    print_results()
