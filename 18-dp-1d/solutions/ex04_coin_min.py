from __future__ import annotations

INF = float("inf")


def min_coins(coins: list[int], amount: int) -> int:
    # STATE: dp[a] = minimum coins to make exactly amount a.
    # CHOICE: which coin denomination to use LAST (unbounded reuse).
    # RECURRENCE: dp[a] = min(dp[a - c] + 1 for c in coins if c <= a).
    # BASE CASE: dp[0] = 0, every other dp[a] starts at +infinity.
    # ORDER: bottom-up, a = 1..amount (avoids the RecursionError a
    # naive memoized-recursion version risks past the recursion limit).
    # Time: O(amount * len(coins)), Space: O(amount).
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1
