"""
Lab 02 Starter - Growth and Big-O Intuition

Use this file only as a starting structure.

Your job is to choose one comparison, implement both approaches, time them with
increasing input sizes, and record the evidence in your README.md file.
"""

TASK_DESCRIPTION = "Replace with the task both approaches solve"

APPROACH_A_NAME = "Replace with approach A"
APPROACH_B_NAME = "Replace with approach B"

INPUT_SIZES = [
    100,
    500,
    1000,
    2000,
]

GROWTH_PREDICTION_A = "Replace with your early prediction for approach A"
GROWTH_PREDICTION_B = "Replace with your early prediction for approach B"


def build_input(size):
    """
    Return the data for one input size.

    Replace this docstring with a short note about what changes when `size`
    gets larger.
    """
    # TODO: build the input data for one timing trial.
    # TODO: make sure both approaches use equivalent input.
    return None


def approach_a(data):
    """
    Solve the task using approach A.

    Replace this docstring with a short explanation of what repeated work this
    approach performs.
    """
    # TODO: write approach A.
    return None


def approach_b(data):
    """
    Solve the task using approach B.

    Replace this docstring with a short explanation of what repeated work this
    approach avoids or changes.
    """
    # TODO: write approach B.
    return None


def main():
    print("Lab 02 starter loaded.")
    print("Next steps:")
    print("1. Name the task and both approaches.")
    print("2. Build input data for at least four input sizes.")
    print("3. Write both approaches and confirm they solve the same problem.")
    print("4. Time both approaches with your own timing setup.")
    print(
        "5. Record the timing table, comparison table or chart, and limitation note in README.md."
    )
    print()
    print("Suggested pseudocode:")
    print("- for each size in INPUT_SIZES:")
    print("- build the input data")
    print("- time approach_a on that input")
    print("- time approach_b on that input")
    print("- record the results in your evidence table")
    print()
    print("This starter does not include a completed timing harness.")


if __name__ == "__main__":
    main()
