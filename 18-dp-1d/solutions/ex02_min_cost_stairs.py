from __future__ import annotations


def min_cost_climb(costs: list[int]) -> int:
    # STATE: dp[i] = min cost to reach step i (0/1 = free starts, top = len(costs)).
    # CHOICE: arrive at i from i-1 (pay costs[i-1]) or i-2 (pay costs[i-2]).
    # RECURRENCE: dp[i] = min(dp[i-1] + costs[i-1], dp[i-2] + costs[i-2]).
    # BASE CASE: dp[0] = dp[1] = 0.
    # ORDER: bottom-up, two rolling variables (dp[i] only reads i-1, i-2).
    # Time: O(n), Space: O(1).
    prev2, prev1 = 0, 0  # dp[0], dp[1] -- both free starting steps
    for i in range(2, len(costs) + 1):
        prev2, prev1 = prev1, min(prev1 + costs[i - 1], prev2 + costs[i - 2])
    return prev1
