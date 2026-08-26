# Scenario: build a Fenwick tree (Binary Indexed Tree) -- smaller and
# faster than a segment tree, at the cost of being locked to
# prefix-style (invertible) aggregation. Pattern: lowbit trick,
# i & (-i), to climb/descend the implicit tree in O(log n).
# Then use it to solve a classic hard: counting, for every element,
# how many later elements are strictly smaller.
# Run: uv run pytest 21-advanced-structures-strings -k ex03

from __future__ import annotations


class Fenwick:
    """Binary Indexed Tree over `n` slots (indices `0..n-1` from the
    outside), supporting point-add and prefix-sum in O(log n) each.

    Internally 1-indexed (a Fenwick tree needs index 0 to stay
    unused -- `lowbit(0)` is 0 and would loop forever). Keep the
    public API 0-indexed and translate at the boundary.

    Target complexity: O(n) space; add/prefix_sum O(log n) time
    each; range_sum O(log n) time (two prefix_sum calls).
    """

    def __init__(self, n: int) -> None:
        """Create a Fenwick tree over `n` slots, all initialized to 0.

        Fenwick(5).prefix_sum(4) -> 0
        """
        raise NotImplementedError

    def add(self, i: int, delta: int) -> None:
        """Add `delta` to the value at index `i` (0-indexed).

        fw = Fenwick(5)
        fw.add(2, 7)
        fw.prefix_sum(4) -> 7

        Target: O(log n) time.
        """
        raise NotImplementedError

    def prefix_sum(self, i: int) -> int:
        """Return the sum of indices `0..i`, inclusive. `i` may be
        `-1` (meaning "empty prefix"), which must return 0.

        fw = Fenwick(5); fw.add(0, 3); fw.add(2, 4)
        fw.prefix_sum(1) -> 3
        fw.prefix_sum(2) -> 7

        Target: O(log n) time.
        """
        raise NotImplementedError

    def range_sum(self, i: int, j: int) -> int:
        """Return the sum of indices `i..j`, both inclusive, via
        `prefix_sum(j) - prefix_sum(i - 1)`.

        fw = Fenwick(5); fw.add(0, 3); fw.add(2, 4); fw.add(4, 1)
        fw.range_sum(1, 4) -> 5

        Target: O(log n) time.
        """
        raise NotImplementedError


def count_smaller_after(nums: list[int]) -> list[int]:
    """For each index `i`, count how many elements AFTER `i` (to the
    right) are strictly smaller than `nums[i]`. Return the list of
    those counts, same length and order as `nums`.

    count_smaller_after([5, 2, 6, 1]) -> [2, 1, 1, 0]
        (5 has 2 and 1 after it that are smaller: 2, 1
         2 has 1 after it that is smaller: 1
         6 has 1 after it that is smaller: 1
         1 has nothing after it)
    count_smaller_after([]) -> []
    count_smaller_after([1, 1, 1]) -> [0, 0, 0]   (strictly smaller only)

    HARD PART, scaffolded:
    1. Coordinate-compress `nums` -- map each distinct value to its
       rank (0-indexed position) among the sorted distinct values.
       This bounds the Fenwick tree's size by the number of DISTINCT
       values instead of the raw value range.
    2. Walk `nums` RIGHT TO LEFT. For each element, its rank `r`
       tells you: "how many already-inserted elements have rank
       `< r`?" -- that's exactly `prefix_sum(r - 1)` on a Fenwick
       tree where `add(rank, 1)` marks "one element with this rank
       has been seen so far" (seen = to the right, since we're going
       right to left).
    3. Insert the current element's rank (`add(r, 1)`) AFTER
       recording its count, so it doesn't count itself.

    Target: O(n log n) time, O(n) space.
    """
    raise NotImplementedError
