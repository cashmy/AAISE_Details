"""Compare recursive call work using a fresh explicit cache for every experiment."""

import argparse


def validate(n):
    if type(n) is not int or not 0 <= n <= 20:
        raise ValueError("n must be an integer from 0 through 20 for the live demo")


def uncached_fibonacci(n):
    validate(n)
    calls = 0
    def calculate(value):
        nonlocal calls
        calls += 1
        if value < 2:
            return value
        return calculate(value - 1) + calculate(value - 2)
    result = calculate(n)
    return result, calls


def cached_fibonacci(n):
    validate(n)
    cache, calls, hits = {}, 0, 0
    def calculate(value):
        nonlocal calls, hits
        calls += 1
        if value in cache:
            hits += 1
            return cache[value]
        if value < 2:
            result = value
        else:
            result = calculate(value - 1) + calculate(value - 2)
        cache[value] = result
        return result
    result = calculate(n)
    return result, calls, hits, cache


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10)
    args = parser.parse_args()
    try:
        validate(args.n)
    except ValueError as error:
        parser.error(str(error))
    print("MEMOIZATION: F(0)=0, F(1)=1; a new cache for every run")
    result, plain_calls = uncached_fibonacci(args.n)
    cached_result, calls, hits, cache = cached_fibonacci(args.n)
    print(f"F({args.n})={result}; uncached calls={plain_calls}")
    print(f"Cached result={cached_result}; total calls={calls}; cache hits={hits}")
    print(f"Computed subproblems/cache entries={len(cache)}; values={dict(sorted(cache.items()))}")
    print("Call counts include cache hits; cache entries count computations, not all calls.")
    print("Memoization avoids repeated work in exchange for stored results.")


if __name__ == "__main__":
    main()
