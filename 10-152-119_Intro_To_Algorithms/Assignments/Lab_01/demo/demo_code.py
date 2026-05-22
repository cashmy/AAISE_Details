INITIAL_RULES = [
    "If the laptop battery is low, bring the charger.",
    "If the student will be on campus for a long time and does not have reliable outlet access, bring the charger.",
    "Otherwise, the charger is optional.",
]

REVISED_RULES = [
    "If battery_percent is 40 or below, bring the charger.",
    "Else if expected_hours is 4 or more and outlet_access is false, bring the charger.",
    "Otherwise, the charger is optional.",
]

PSEUDOCODE = [
    "if battery_percent <= 40:",
    "    recommend bringing charger",
    "else if expected_hours >= 4 and outlet_access is false:",
    "    recommend bringing charger",
    "else:",
    "    charger is optional",
]

PYTHON_STYLE = [
    "if battery_percent <= 40:",
    '    recommendation = "bring charger"',
    "elif expected_hours >= 4 and not outlet_access:",
    '    recommendation = "bring charger"',
    "else:",
    '    recommendation = "charger optional"',
]

TEST_CASES = [
    {
        "name": "1",
        "battery_percent": 25,
        "expected_hours": 2,
        "outlet_access": True,
        "expected": "bring charger",
    },
    {
        "name": "2",
        "battery_percent": 80,
        "expected_hours": 3,
        "outlet_access": False,
        "expected": "charger optional",
    },
    {
        "name": "3",
        "battery_percent": 55,
        "expected_hours": 5,
        "outlet_access": False,
        "expected": "bring charger",
    },
    {
        "name": "4",
        "battery_percent": 40,
        "expected_hours": 4,
        "outlet_access": False,
        "expected": "bring charger",
    },
    {
        "name": "5",
        "battery_percent": 39,
        "expected_hours": 1,
        "outlet_access": False,
        "expected": "bring charger",
    },
]


def recommend_charger_initial(battery_percent, expected_hours, outlet_access):
    if battery_percent < 40:
        return "bring charger"
    if expected_hours > 4 and not outlet_access:
        return "bring charger"
    return "charger optional"


def recommend_charger_revised(battery_percent, expected_hours, outlet_access):
    if battery_percent <= 40:
        return "bring charger"
    if expected_hours >= 4 and not outlet_access:
        return "bring charger"
    return "charger optional"


def format_input_summary(test_case):
    outlet_text = "available" if test_case["outlet_access"] else "unavailable"
    hour_label = "hour" if test_case["expected_hours"] == 1 else "hours"
    return (
        f"Battery {test_case['battery_percent']}%, "
        f"{test_case['expected_hours']} {hour_label} on campus, outlet {outlet_text}"
    )


def print_rule_list(title, rules):
    print(title)
    for rule in rules:
        print(f"- {rule}")
    print()


def print_representation_bridge():
    print("REPRESENTATION BRIDGE")
    print_rule_list("Precise Plain English", REVISED_RULES)
    print_rule_list("Pseudocode", PSEUDOCODE)
    print_rule_list("Python-Style Logic", PYTHON_STYLE)


def print_test_table(title, decision_function):
    print(title)
    header = (
        f"{'Test':<4} | {'Input Summary':<58} | {'Expected':<16} | "
        f"{'Actual':<16} | Pass?"
    )
    print(header)
    print("-" * len(header))

    for test_case in TEST_CASES:
        actual = decision_function(
            test_case["battery_percent"],
            test_case["expected_hours"],
            test_case["outlet_access"],
        )
        passed = "Yes" if actual == test_case["expected"] else "No"
        print(
            f"{test_case['name']:<4} | "
            f"{format_input_summary(test_case):<58} | "
            f"{test_case['expected']:<16} | "
            f"{actual:<16} | "
            f"{passed}"
        )

    print()


def main():
    print("LAB 01 DEMO - PRECISION AND CORRECTNESS")
    print()
    print_rule_list("Before Revision", INITIAL_RULES)
    print_rule_list("After Revision", REVISED_RULES)
    print_representation_bridge()
    print_test_table("Initial Rule Set (< 40)", recommend_charger_initial)
    print_test_table("Revised Rule Set (<= 40)", recommend_charger_revised)


if __name__ == "__main__":
    main()
