"""
Lab 01 Starter - Precision and Correctness

Use this file only as a starting structure.

Your job is to define a precise decision process, create test cases, run or
trace those tests, and document the evidence in your README.md file.
"""

SCENARIO_NAME = "Replace with your chosen scenario"

PROBLEM_STATEMENT = """
Describe the decision your algorithm makes.
"""

INPUTS = [
    "Replace with input 1",
    "Replace with input 2",
    "Replace with input 3",
]

OUTPUTS = [
    "Replace with the decision or result your algorithm produces",
]

ASSUMPTIONS = [
    "Replace with assumption or constraint 1",
    "Replace with assumption or constraint 2",
    "Replace with assumption or constraint 3",
]


def make_decision(case_data):
    """
    Decide the output for one test case.

    Replace this docstring with a short explanation of your rule order.

    Suggested process:
    1. Read the values from case_data.
    2. Check the most important rule first.
    3. Return a clear decision label.
    4. Make sure your rules handle edge cases.
    """
    # TODO: get the needed values from case_data.
    # TODO: write your first decision rule.
    # TODO: write any additional decision rules.
    # TODO: return the final decision.
    return "TODO"


TEST_CASES = [
    {
        "name": "Normal 1",
        "input": {
            # TODO: add input values for this test.
        },
        "expected": "TODO",
    },
    {
        "name": "Normal 2",
        "input": {
            # TODO: add input values for this test.
        },
        "expected": "TODO",
    },
    {
        "name": "Normal 3",
        "input": {
            # TODO: add input values for this test.
        },
        "expected": "TODO",
    },
    {
        "name": "Edge 1",
        "input": {
            # TODO: add input values for this edge case.
        },
        "expected": "TODO",
    },
    {
        "name": "Edge 2",
        "input": {
            # TODO: add input values for this edge case.
        },
        "expected": "TODO",
    },
]


def main():
    """
    Optional helper area.

    You may use this function to manually call make_decision() on your test
    cases. You are still responsible for building the evidence table in your
    README.md file.
    """
    print("Lab 01 starter loaded.")
    print("Next steps:")
    print("1. Replace the scenario, inputs, outputs, and assumptions.")
    print("2. Write your decision rules inside make_decision().")
    print("3. Complete at least five test cases.")
    print("4. Record expected and actual results in your README.md table.")

    # Optional pseudocode:
    # for each test_case in TEST_CASES:
    #     actual = make_decision(test_case["input"])
    #     compare actual to test_case["expected"]
    #     record the result in your README.md evidence table


if __name__ == "__main__":
    main()
