from collections.abc import Callable


def climb_ways_naive(n: int, tick: Callable[[], None]) -> int:
    # STATE: ways(i) = number of distinct ways to reach stair i.
    # CHOICE: the last step taken to land on i was a 1-step or 2-step.
    # RECURRENCE: ways(i) = ways(i-1) + ways(i-2).
    # BASE CASE: ways(0) = ways(1) = 1.
    # ORDER: no cache, naive top-down recursion recomputes every state.
    # Time: O(2^n), Space: O(n) stack depth.
    tick()
    if n <= 1:
        return 1
    return climb_ways_naive(n - 1, tick) + climb_ways_naive(n - 2, tick)


def climb_ways_memo(n: int, tick: Callable[[], None]) -> int:
    # STATE: ways(i) = number of distinct ways to reach stair i.
    # CHOICE: the last step taken to land on i was a 1-step or 2-step.
    # RECURRENCE: ways(i) = ways(i-1) + ways(i-2).
    # BASE CASE: ways(0) = ways(1) = 1.
    # ORDER: top-down — recursion driven, cache checked before recursing
    # so each distinct i is computed exactly once.
    # Time: O(n), Space: O(n) for the cache + call stack.
    cache: dict[int, int] = {}

    def helper(i: int) -> int:
        if i in cache:
            return cache[i]
        tick()
        value = 1 if i <= 1 else helper(i - 1) + helper(i - 2)
        cache[i] = value
        return value

    return helper(n)


def climb_ways_table(n: int) -> int:
    # STATE: ways(i) = number of distinct ways to reach stair i.
    # CHOICE: the last step taken to land on i was a 1-step or 2-step.
    # RECURRENCE: ways(i) = ways(i-1) + ways(i-2).
    # BASE CASE: ways(0) = ways(1) = 1.
    # ORDER: bottom-up, i = 2..n — dp[i-1] and dp[i-2] already filled.
    # Time: O(n), Space: O(n) for the table.
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climb_ways_optimized(n: int) -> int:
    # STATE: ways(i) = number of distinct ways to reach stair i.
    # CHOICE: the last step taken to land on i was a 1-step or 2-step.
    # RECURRENCE: ways(i) = ways(i-1) + ways(i-2).
    # BASE CASE: ways(0) = ways(1) = 1.
    # ORDER: bottom-up, table collapsed to two rolling variables since
    # dp[i] only ever needs the previous two values.
    # Time: O(n), Space: O(1).
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1  # ways(0), ways(1)
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
