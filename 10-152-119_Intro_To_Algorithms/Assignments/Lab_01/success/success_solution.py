SCENARIO_NAME = "Help desk ticket priority"

TEST_CASES = [
    {
        "name": "Normal 1",
        "input": {
            "severity": "critical",
            "users_affected": 50,
            "hours_until_deadline": 6,
            "work_blocked": True,
            "has_required_info": True,
        },
        "expected_priority": "high",
    },
    {
        "name": "Normal 2",
        "input": {
            "severity": "high",
            "users_affected": 2,
            "hours_until_deadline": 1,
            "work_blocked": False,
            "has_required_info": True,
        },
        "expected_priority": "high",
    },
    {
        "name": "Normal 3",
        "input": {
            "severity": "medium",
            "users_affected": 12,
            "hours_until_deadline": 24,
            "work_blocked": False,
            "has_required_info": True,
        },
        "expected_priority": "medium",
    },
    {
        "name": "Normal 4",
        "input": {
            "severity": "low",
            "users_affected": 1,
            "hours_until_deadline": 48,
            "work_blocked": False,
            "has_required_info": True,
        },
        "expected_priority": "low",
    },
    {
        "name": "Edge 1",
        "input": {
            "severity": "medium",
            "users_affected": 4,
            "hours_until_deadline": 12,
            "work_blocked": True,
            "has_required_info": False,
        },
        "expected_priority": "needs clarification",
    },
    {
        "name": "Edge 2",
        "input": {
            "severity": "low",
            "users_affected": 10,
            "hours_until_deadline": 12,
            "work_blocked": False,
            "has_required_info": True,
        },
        "expected_priority": "medium",
    },
]


def assign_priority(
    severity,
    users_affected,
    hours_until_deadline,
    work_blocked,
    has_required_info,
):
    severity = severity.lower()

    if not has_required_info:
        return "needs clarification", "missing required information"

    if severity == "critical":
        return "high", "critical issue"

    if work_blocked and users_affected >= 5:
        return "high", "blocked work and several affected users"

    if severity == "high" and hours_until_deadline <= 2:
        return "high", "high severity with a near deadline"

    if work_blocked or severity == "high" or users_affected >= 10:
        return "medium", "important issue but not in the highest rule group"

    return "low", "limited impact and no urgent blocker"


def format_input_summary(case_data):
    return (
        f"{case_data['severity']}, {case_data['users_affected']} users, "
        f"deadline {case_data['hours_until_deadline']}h, "
        f"blocked={case_data['work_blocked']}, "
        f"info={case_data['has_required_info']}"
    )


def run_tests():
    print(f"LAB 01 SUCCESS VERSION - {SCENARIO_NAME.upper()}")
    print()
    header = (
        f"{'Test':<8} | {'Input Summary':<70} | {'Expected':<20} | "
        f"{'Actual':<20} | Pass? | Reason"
    )
    print(header)
    print("-" * len(header))

    for test_case in TEST_CASES:
        actual_priority, reason = assign_priority(**test_case["input"])
        passed = "Yes" if actual_priority == test_case["expected_priority"] else "No"
        print(
            f"{test_case['name']:<8} | "
            f"{format_input_summary(test_case['input']):<70} | "
            f"{test_case['expected_priority']:<20} | "
            f"{actual_priority:<20} | "
            f"{passed:<5} | "
            f"{reason}"
        )


if __name__ == "__main__":
    run_tests()
