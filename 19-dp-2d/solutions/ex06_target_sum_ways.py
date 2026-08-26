from __future__ import annotations


def ways_to_target(nums: list[int], target: int) -> int:
    # Pattern: subset-sum reduction (signed assignment -> 0/1 knapsack count).
    # STATE: dp[w] = number of subsets of nums seen so far summing to w.
    # CHOICE: put the number in the '+' subset (skip in this dp) or the
    # '-' subset (counted via the complementary reduction below).
    # RECURRENCE: dp[w] += dp[w - num], where P = (sum(nums) + target) // 2.
    # BASE CASE: dp[0] = 1; odd (sum + target) or |target| > sum -> 0 ways.
    # ORDER: capacity swept HIGH to LOW per number -- the 0/1 direction rule.
    # Time: O(n * P), Space: O(P).
    total = sum(nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0
    positive_sum = (total + target) // 2

    dp = [0] * (positive_sum + 1)
    dp[0] = 1
    for num in nums:
        for w in range(positive_sum, num - 1, -1):
            dp[w] += dp[w - num]
    return dp[positive_sum]
