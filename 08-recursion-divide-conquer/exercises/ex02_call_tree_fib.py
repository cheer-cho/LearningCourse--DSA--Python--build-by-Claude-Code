# Scenario: prove memoization works with a counter, not vibes. `tick` is a
# zero-argument callable the tests use to count calls/computations.
# Pattern: naive recursion's exponential call tree vs. memoized recursion.
# Run: uv run pytest 08-recursion-divide-conquer -k ex02

from collections.abc import Callable


def fib_naive(n: int, tick: Callable[[], None]) -> int:
    """Compute the n-th Fibonacci number (fib(0)=0, fib(1)=1) via plain
    recursion, with no cache. Call `tick()` exactly once per function
    call (including base cases) so tests can count the call-tree size.

    Base case: n <= 1 -> n.
    Shrinking step: fib_naive(n - 1) + fib_naive(n - 2).

    fib_naive(0, tick) -> 0   (1 call)
    fib_naive(1, tick) -> 1   (1 call)
    fib_naive(10, tick) -> 55 (177 calls — the exponential blowup)

    Target: O(2^n) time, O(n) space (deepest call-stack path).
    """
    raise NotImplementedError


def fib_memo(n: int, tick: Callable[[], None]) -> int:
    """Compute the n-th Fibonacci number via recursion with memoization
    (a cache local to this call, fresh each time). Call `tick()` exactly
    once per NEWLY COMPUTED value (never on a cache hit) — computing
    fib(0..n) each exactly once means n + 1 ticks total for n >= 2 (k=1
    is itself a base case and never triggers a separate call for k=0, so
    n=0 and n=1 each tick only once).

    Base case: k <= 1 -> k (still counted as "computed" -> tick).
    Shrinking step: cache miss on k -> compute helper(k-1) + helper(k-2),
    store it, tick once.

    fib_memo(0, tick) -> 0   (1 tick: k=0)
    fib_memo(1, tick) -> 1   (1 tick: k=1, a base case on its own)
    fib_memo(10, tick) -> 55 (11 ticks: k=0..10, one each)

    Target: O(n) time, O(n) space (cache + call-stack depth).
    """
    raise NotImplementedError
