# Scenario: a courier can carry at most `capacity` kg and wants the most
# valuable haul from a set of packages, each takeable at most once.
# Pattern: 0/1 knapsack -- item index and remaining budget both move the
# state; also: reducing "equal split" to subset-sum.
# Run: uv run pytest 19-dp-2d -k ex04

from __future__ import annotations


def max_value(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum total value achievable by choosing a subset of
    items (each weights[i]/values[i] pair usable AT MOST ONCE) whose
    total weight doesn't exceed `capacity`.

    STATE: dp[i][w] = best value using items[0:i] with budget w.
    CHOICE: skip item i, or take it if it fits.
    RECURRENCE: dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight_i] + value_i)
    (the take branch only applies when weight_i <= w).
    BASE CASE: dp[0][w] = 0 for every w (no items chosen yet).

    Space optimization required: 1-D array of length capacity + 1,
    capacity swept HIGH to LOW each item -- this is the 0/1 direction
    rule from the lesson (sweeping low to high would let an item be
    "taken" twice in the same pass).

    max_value([1, 3, 4, 5], [1, 4, 5, 7], 7) -> 9   (items 1 and 2: 3+4=7, 4+5=9)
    max_value([2, 3, 4], [3, 4, 5], 5) -> 7
    max_value([], [], 10) -> 0

    Target: O(n * capacity) time, O(capacity) space.
    """
    raise NotImplementedError


def can_partition_equal(nums: list[int]) -> bool:
    """Return True if `nums` can be split into two subsets with equal
    sums.

    THE REDUCTION (the point of this exercise): if the total is odd,
    an equal split is impossible -- return False immediately. Otherwise
    the question becomes "does some subset of nums sum to exactly
    total // 2?" -- a 0/1 knapsack where each item is used at most once
    and you only need to know if a capacity is REACHABLE (a boolean
    dp[w]), not the best value.

    Implementation: 1-D boolean dp[w], swept HIGH to LOW (same 0/1
    direction rule as `max_value`) so each number is used at most once.

    can_partition_equal([1, 5, 11, 5]) -> True    ([1, 5, 5] and [11])
    can_partition_equal([1, 2, 3, 5]) -> False
    can_partition_equal([2, 2]) -> True
    can_partition_equal([]) -> True   (two empty subsets, both sum to 0)

    Target: O(n * sum(nums)) time, O(sum(nums)) space.
    """
    raise NotImplementedError
