# Scenario: some inputs are too deep for the call stack. Python's default
# recursion limit (sys.getrecursionlimit()) is 1000 — a naive recursive
# call chasing a nested list or a countdown 5,000 levels deep raises
# RecursionError. Any recursion can become a loop + an explicit stack (a
# plain list you push/pop yourself, standing in for the call stack) — that
# is the recipe you implement here. 5,000 is chosen well above the 1000
# default limit (proving the point) but small enough to run instantly.
# Run: uv run pytest 08-recursion-divide-conquer -k ex06

from typing import Any


def deep_sum_iterative(nested: list[Any]) -> int:
    """Sum every integer inside an arbitrarily nested list — same
    contract as ex04's deep_sum — but WITHOUT recursion, so it survives
    inputs nested deeper than the recursion limit.

    Recursive reference (do not call it — for deep inputs it overflows):
        def deep_sum_rec(nested):
            total = 0
            for item in nested:
                total += deep_sum_rec(item) if isinstance(item, list) else item
            return total

    Recipe: replace the call stack with an explicit stack (a list). Push
    work instead of calling; pop work instead of returning. Each list you
    encounter gets pushed for later processing instead of recursed into.

    deep_sum_iterative([1, [2, 3], [4, [5, 6]]]) -> 21
    deep_sum_iterative([]) -> 0

    Target: O(total elements) time, O(max depth) space (the explicit
    stack, not the call stack).
    """
    raise NotImplementedError


def countdown_iterative(n: int) -> list[int]:
    """Build [n, n-1, ..., 1] — same contract as ex01's countdown — but
    WITHOUT recursion, so it survives n deeper than the recursion limit.

    Recursive reference (do not call it — for large n it overflows):
        def countdown_rec(n):
            if n <= 0:
                return []
            return [n] + countdown_rec(n - 1)

    Recipe: replace the call stack with an explicit stack (a list). Push
    the starting value; each pop either extends the result (if positive)
    and pushes the next smaller value, or is discarded (base case).

    countdown_iterative(4) -> [4, 3, 2, 1]
    countdown_iterative(0) -> []

    Target: O(n) time, O(n) space (the explicit stack, not the call
    stack).
    """
    raise NotImplementedError
