# Scenario: build the engine the next few exercises rest on. Pattern:
# segment tree as a flat array (4n storage), node i's children at
# 2*node+1 / 2*node+2, merge = sum, identity = 0.
# Run: uv run pytest 21-advanced-structures-strings -k ex01

from __future__ import annotations


class SegmentTree:
    """Array-based segment tree answering range-SUM queries and
    point updates, each in O(log n).

    Internally: a flat list `tree` of size `4 * n`. `tree[node]` holds
    the sum of the data range `[lo, hi]` that `node` covers; children
    of `node` live at `2*node + 1` and `2*node + 2`.

    Target complexity: build O(n) time; range_sum/update O(log n)
    time each, O(log n) recursion depth; O(n) space.
    """

    def __init__(self, nums: list[int]) -> None:
        """Build the tree over `nums` (may be empty).

        SegmentTree([2, 5, 1, 4, 9, 3]).range_sum(1, 4) -> 19
        SegmentTree([]).range_sum(0, -1) is never called (n == 0).
        """
        raise NotImplementedError

    def range_sum(self, i: int, j: int) -> int:
        """Return the sum of `nums[i..j]`, both endpoints inclusive.

        `i` and `j` are valid indices with `i <= j`.

        st = SegmentTree([2, 5, 1, 4, 9, 3])
        st.range_sum(0, 2) -> 8
        st.range_sum(0, 5) -> 24

        Target: O(log n) time.
        """
        raise NotImplementedError

    def update(self, i: int, value: int) -> None:
        """Set `nums[i] = value` and fix up every ancestor on the path
        back to the root so future queries see the change.

        st = SegmentTree([2, 5, 1, 4])
        st.update(2, 10)
        st.range_sum(0, 3) -> 21   (2+5+10+4)

        Target: O(log n) time.
        """
        raise NotImplementedError
