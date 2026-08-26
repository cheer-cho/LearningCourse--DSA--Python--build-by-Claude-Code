from collections.abc import Callable


def fib_naive(n: int, tick: Callable[[], None]) -> int:
    # Pattern: naive tree recursion — no cache, so overlapping
    # subproblems (fib(3), fib(2), ...) get recomputed from scratch every
    # time they appear in the call tree.
    # Time: O(2^n) (call count follows 2*F(n+1)-1), Space: O(n) stack depth.
    tick()
    if n <= 1:
        return n
    return fib_naive(n - 1, tick) + fib_naive(n - 2, tick)


def fib_memo(n: int, tick: Callable[[], None]) -> int:
    # Pattern: top-down memoization — a cache keyed by n, local to this
    # call, collapses the exponential tree into one computation per
    # distinct value.
    # Time: O(n), Space: O(n) for the cache + call stack.
    memo: dict[int, int] = {}

    def helper(k: int) -> int:
        if k in memo:
            return memo[k]
        tick()
        value = k if k <= 1 else helper(k - 1) + helper(k - 2)
        memo[k] = value
        return value

    return helper(n)
