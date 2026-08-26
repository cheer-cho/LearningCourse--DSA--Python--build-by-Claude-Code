from __future__ import annotations


def max_loot(values: list[int]) -> int:
    # STATE: dp[i] = max loot achievable using houses 0..i.
    # CHOICE: skip house i (dp[i-1]) or rob it (values[i] + dp[i-2]).
    # RECURRENCE: dp[i] = max(dp[i-1], values[i] + dp[i-2]).
    # BASE CASE: dp[-1] = 0 (no houses).
    # ORDER: bottom-up, two rolling variables (dp[i] only reads i-1, i-2).
    # Time: O(n), Space: O(1).
    prev2, prev1 = 0, 0  # dp[-1] = 0 (no houses), rolling into dp[i-1]
    for value in values:
        prev2, prev1 = prev1, max(prev1, value + prev2)
    return prev1


def max_loot_circle(values: list[int]) -> int:
    # STATE: circle_best = max loot over a circular arrangement of the
    # houses.
    # CHOICE: a valid selection can never include BOTH wrap-around
    # neighbors (index 0 and the last index), so choose which end to
    # drop entirely.
    # RECURRENCE: circle_best = max(max_loot(values[:-1]), max_loot(values[1:])),
    # reusing max_loot's own dp[i] = max(dp[i-1], values[i] + dp[i-2])
    # recurrence on each excluded-end run.
    # BASE CASE: 0 houses -> 0; 1 house -> values[0] (no wrap-around
    # adjacency to worry about).
    # ORDER: run the (bottom-up) max_loot twice, once per excluded end,
    # then take the max.
    # Time: O(n), Space: O(1).
    if len(values) <= 1:
        return values[0] if values else 0
    return max(max_loot(values[:-1]), max_loot(values[1:]))
