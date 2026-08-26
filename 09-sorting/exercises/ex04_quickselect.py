# Scenario: a live scoreboard only ever needs "what's the kth highest
# score right now?" — sorting the whole board every time wastes work.
# Concepts: quickselect, partition-based selection, average O(n).
# Run: uv run pytest 09-sorting -k ex04


def kth_largest(nums: list[int], k: int) -> int:
    """Return the kth largest value in `nums` (k=1 is the maximum,
    k=len(nums) is the minimum). Does not need to fully sort `nums` —
    use quickselect: partition (like quick sort) and recurse into only
    the one side that can contain the answer. Do NOT call `sorted()`,
    `list.sort()`, or `heapq` — those defeat the point of the exercise.

    `nums` has at least `k` elements. Ties (duplicate values) are
    allowed; any occurrence may be returned.

    kth_largest([3, 1, 4, 1, 5], 1) -> 5
    kth_largest([3, 1, 4, 1, 5], 5) -> 1   (the minimum)
    kth_largest([7], 1) -> 7

    Target complexity: O(n) average time, O(n) space (working copy —
    do not mutate the caller's list).
    """
    raise NotImplementedError
