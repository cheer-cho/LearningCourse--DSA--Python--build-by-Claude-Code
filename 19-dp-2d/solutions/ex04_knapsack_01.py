from __future__ import annotations


def max_value(weights: list[int], values: list[int], capacity: int) -> int:
    # Pattern: 0/1 knapsack, 1-D space optimization.
    # STATE: dp[w] = best value using items considered so far, budget w.
    # CHOICE: skip the item, or take it if it fits.
    # RECURRENCE: dp[w] = max(dp[w], dp[w-weight] + value).
    # BASE CASE: dp[*] = 0 (no items chosen yet).
    # ORDER: capacity swept HIGH to LOW per item -- the 0/1 direction rule.
    # Time: O(n * capacity), Space: O(capacity).
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + value)
    return dp[capacity]


def can_partition_equal(nums: list[int]) -> bool:
    # Pattern: 0/1 subset-sum reduction (feasibility, not value).
    # STATE: dp[w] = can some subset of nums seen so far sum to exactly w.
    # CHOICE: skip the number, or take it if it fits.
    # RECURRENCE: dp[w] |= dp[w - num].
    # BASE CASE: dp[0] = True (empty subset sums to 0); odd total -> impossible.
    # ORDER: capacity swept HIGH to LOW per number -- same 0/1 direction rule.
    # Time: O(n * sum(nums)), Space: O(sum(nums)).
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for c in range(target, num - 1, -1):
            if dp[c - num]:
                dp[c] = True
    return dp[target]
