# Scenario: each stair has a cost to leave it. Start standing on step 0
# or step 1 (free), then always move 1 or 2 steps at a time, paying the
# cost of whichever step you leave. Find the cheapest way past the top.
# Pattern: DP framework transfer #1 — swap "count the ways" for "min
# cost to reach a state" (same recurrence shape, different combiner).
# Run: uv run pytest 18-dp-1d -k ex02

from __future__ import annotations


def min_cost_climb(costs: list[int]) -> int:
    """Return the minimum total cost to climb past the top of a
    staircase with len(costs) steps (0-indexed), where `costs[i]` is
    paid when you STEP OFF step i. You may start standing on step 0 or
    step 1 for free, and from any step you may advance 1 or 2 steps.
    "The top" is one past the last index (`len(costs)`) — you stop
    paying once you've climbed past the last step.

    STATE: dp[i] = min cost to reach step i (0 = start, not a real
    step; len(costs) = the top).
    CHOICE: arrive at i from i-1 (pay costs[i-1]) or from i-2 (pay
    costs[i-2]).
    RECURRENCE: dp[i] = min(dp[i-1] + costs[i-1], dp[i-2] + costs[i-2]).
    BASE CASE: dp[0] = dp[1] = 0 (both starting steps are free to
    stand on).

    min_cost_climb([10, 15, 20]) -> 15
        (start at step 1 for free, pay 15 to jump straight to the top)
    min_cost_climb([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) -> 6
    min_cost_climb([0, 0]) -> 0

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
