# Scenario: how many distinct ways can you climb `n` stairs, taking 1 or
# 2 steps at a time? Same problem, four times, tracing the framework from
# naive recursion through memoization, tabulation, and space optimization.
# Pattern: THE 5-step DP framework (state/choice/recurrence/base/order).
# Run: uv run pytest 18-dp-1d -k ex01

from collections.abc import Callable


def climb_ways_naive(n: int, tick: Callable[[], None]) -> int:
    """Count distinct ways to climb `n` stairs (steps of 1 or 2), via
    plain recursion with no cache. Call `tick()` exactly once per
    function call (including base cases), so tests can count the
    call-tree size — this is fib_naive's exact call-tree shape (module
    08), just relabeled.

    STATE: ways(i) = number of distinct ways to reach stair i.
    CHOICE: the last step taken to land on i was a 1-step or a 2-step.
    RECURRENCE: ways(i) = ways(i-1) + ways(i-2).
    BASE CASE: ways(0) = 1, ways(1) = 1.

    climb_ways_naive(0, tick) -> 1   (1 call)
    climb_ways_naive(5, tick) -> 8   (15 calls — the exponential blowup)
    climb_ways_naive(10, tick) -> 89 (177 calls)

    Target: O(2^n) time, O(n) space (deepest call-stack path).
    """
    raise NotImplementedError


def climb_ways_memo(n: int, tick: Callable[[], None]) -> int:
    """Count distinct ways to climb `n` stairs via recursion with
    memoization (a cache local to this call, fresh each time). Call
    `tick()` exactly once per NEWLY COMPUTED value (never on a cache
    hit) — computing ways(0..n) each exactly once means n + 1 ticks
    total.

    Same STATE/CHOICE/RECURRENCE/BASE CASE as `climb_ways_naive`;
    ORDER is top-down, driven by the recursion, cache-checked first.

    climb_ways_memo(0, tick) -> 1   (1 tick)
    climb_ways_memo(10, tick) -> 89 (11 ticks: i=0..10, one each)

    Target: O(n) time, O(n) space (cache + call-stack depth).
    """
    raise NotImplementedError


def climb_ways_table(n: int) -> int:
    """Count distinct ways to climb `n` stairs via a bottom-up table:
    fill dp[0..n] left to right, each entry built from two entries
    already computed.

    Same STATE/CHOICE/RECURRENCE/BASE CASE as `climb_ways_naive`;
    ORDER is bottom-up — iterate i = 2..n so dp[i-1] and dp[i-2] both
    already exist.

    climb_ways_table(0) -> 1
    climb_ways_table(1) -> 1
    climb_ways_table(10) -> 89

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def climb_ways_optimized(n: int) -> int:
    """Count distinct ways to climb `n` stairs, keeping only the two
    most recent values instead of a full table — dp[i] only ever reads
    dp[i-1] and dp[i-2], so nothing further back needs to stay around.

    Same STATE/CHOICE/RECURRENCE/BASE CASE as `climb_ways_naive`;
    ORDER is bottom-up with the table collapsed to two rolling
    variables.

    climb_ways_optimized(0) -> 1
    climb_ways_optimized(10) -> 89

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
