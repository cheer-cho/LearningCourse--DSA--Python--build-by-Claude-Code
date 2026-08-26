# Checkpoint 19 -- Product launch
#
# A product team picks features under a budget, scores a slogan against
# the brand guide, counts ways to pack an order, and checks whether an
# engineering workload can be split fairly across two squads. Four
# independent instances of this module's patterns -- name each one, don't
# reinvent the recurrence.
# Run: uv run pytest 19-dp-2d -k checkpoint

from __future__ import annotations


def best_feature_set(costs: list[int], impacts: list[int], budget: int) -> list[int]:
    """Choose the set of features that maximizes total impact without
    exceeding `budget`, where each feature is taken at most once (0/1
    knapsack) -- but this time return WHICH features were chosen, not
    just the best value.

    Build the FULL 2-D dp[i][w] table (items x budget) -- reconstruction
    needs to look back through every row, so the 1-D space optimization
    from ex04 doesn't apply here. Then backtrack from dp[n][budget]: if
    dp[i][w] != dp[i-1][w], feature i-1 was included -- record it and
    move to dp[i-1][w - costs[i-1]]; otherwise it was skipped -- move to
    dp[i-1][w].

    best_feature_set([1, 3, 4, 5], [1, 4, 5, 7], 7) -> [1, 2]
    (0-indexed; cost 3+4=7 fits exactly, impact 4+5=9 is optimal)
    best_feature_set([], [], 10) -> []
    best_feature_set([10], [42], 5) -> []   (doesn't fit)

    Target: O(n * budget) time, O(n * budget) space (full 2-D table
    required for reconstruction).
    """
    raise NotImplementedError


def slogan_similarity(a: str, b: str) -> int:
    """Return the edit distance between proposed slogan `a` and brand
    guide phrase `b` -- the minimum insert/delete/replace edits to turn
    `a` into `b`. Identical shape to ex03's `edit_distance`;
    re-implement it here from scratch.

    slogan_similarity("kitten", "sitting") -> 3
    slogan_similarity("launch", "launch") -> 0
    slogan_similarity("", "abc") -> 3

    Target: O(n * m) time, O(n * m) space.
    """
    raise NotImplementedError


def bundle_ways(pack_sizes: list[int], order_size: int) -> int:
    """Count the number of distinct COMBINATIONS of `pack_sizes` (each
    size reusable any number of times) that add up to exactly
    `order_size`. Order doesn't matter -- same unbounded-combination
    shape as ex05's `count_coin_ways` (pack sizes outer loop,
    order_size inner loop, swept forward).

    bundle_ways([1, 2, 5], 5) -> 4
    bundle_ways([2], 3) -> 0
    bundle_ways([1, 2], 0) -> 1     (one way to fill an empty order: nothing)
    bundle_ways([], 0) -> 1
    bundle_ways([], 3) -> 0

    Target: O(len(pack_sizes) * order_size) time, O(order_size) space.
    """
    raise NotImplementedError


def is_fair_split(workloads: list[int]) -> bool:
    """Return True if `workloads` can be split into two subsets with
    equal total work. Identical reduction to ex04's
    `can_partition_equal` (odd total -> impossible; otherwise subset-sum
    to total // 2); re-implement it here from scratch.

    is_fair_split([1, 5, 11, 5]) -> True
    is_fair_split([1, 2, 3, 5]) -> False
    is_fair_split([4]) -> False
    is_fair_split([]) -> True

    Target: O(n * sum(workloads)) time, O(sum(workloads)) space.
    """
    raise NotImplementedError
