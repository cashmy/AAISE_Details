"""A bounded exhaustive reference challenges a greedy optimality claim."""


def validate(denominations, target):
    if type(target) is not int or not 0 <= target <= 12:
        raise ValueError("target must be an integer from 0 through 12 for this small reference")
    if not denominations or any(type(coin) is not int or coin <= 0 for coin in denominations):
        raise ValueError("denominations must be nonempty positive integers")
    return sorted(set(denominations), reverse=True)


def greedy_change(denominations, target):
    coins = validate(denominations, target)
    chosen, remaining = [], target
    for coin in coins:
        while remaining >= coin:
            chosen.append(coin)
            remaining -= coin
    return chosen if remaining == 0 else None


def exhaustive_change(denominations, target):
    coins = validate(denominations, target)
    best = None
    # Enumerate nonincreasing combinations to avoid permutations of the same solution.
    def visit(remaining, start, chosen):
        nonlocal best
        if remaining == 0:
            if best is None or len(chosen) < len(best):
                best = chosen.copy()
            return
        for position in range(start, len(coins)):
            coin = coins[position]
            if coin <= remaining:
                visit(remaining - coin, position, chosen + [coin])
    visit(target, 0, [])
    return best


def main():
    print("GREEDY COUNTEREXAMPLE: minimize coin count, unlimited coins")
    for coins, target in (([1, 3, 4], 6), ([3, 4], 6), ([2, 4], 3), ([1, 5, 10], 12)):
        greedy = greedy_change(coins, target)
        best = exhaustive_change(coins, target)
        print(f"\nDenominations={coins}, target={target}")
        print("  Largest-first:", greedy, "(None means no complete greedy result)")
        print("  Exhaustive minimum:", best)
    print("\n4+1+1 uses 3 coins; 3+3 uses 2. Largest-first is not universally optimal.")
    print("A greedy failure also need not mean no solution exists.")


if __name__ == "__main__":
    main()
