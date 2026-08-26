# Scenario: generalize ex01's segment tree to a different question.
# Pattern: same skeleton (array-based, 4n storage, node i's children
# at 2*node+1 / 2*node+2) -- only the merge function and identity
# element change: sum/0 becomes min/+infinity.
# Run: uv run pytest 21-advanced-structures-strings -k ex02

from __future__ import annotations

INF = float("inf")


class RangeMinTree:
    """Array-based segment tree answering range-MIN queries and
    point updates, each in O(log n).

    What changed vs `SegmentTree` (ex01): the merge function is now
    `min(a, b)` instead of `a + b`, and the identity element (the
    value returned for a range that's entirely outside a query, or
    the "no children" default) is `+infinity` instead of `0` --
    `+infinity` is the value that never wins a `min` comparison, the
    same role `0` played for `sum`. Everything else -- the tree
    shape, the build/query/update recursion, the complexity -- is
    identical. That's the point: a segment tree is really "merge
    function + identity," not "sum specifically."

    Target complexity: build O(n) time; range_min/update O(log n)
    time each, O(log n) recursion depth; O(n) space.
    """

    def __init__(self, nums: list[int]) -> None:
        """Build the tree over `nums` (may be empty).

        RangeMinTree([5, 2, 8, 1, 9]).range_min(0, 2) -> 2
        """
        raise NotImplementedError

    def range_min(self, i: int, j: int) -> int:
        """Return the minimum of `nums[i..j]`, both endpoints
        inclusive. `i` and `j` are valid indices with `i <= j`.

        rt = RangeMinTree([5, 2, 8, 1, 9])
        rt.range_min(0, 4) -> 1
        rt.range_min(2, 4) -> 1

        Target: O(log n) time.
        """
        raise NotImplementedError

    def update(self, i: int, value: int) -> None:
        """Set `nums[i] = value` and fix up every ancestor on the
        path back to the root.

        rt = RangeMinTree([5, 2, 8, 1, 9])
        rt.update(3, 20)
        rt.range_min(0, 4) -> 2   (the old minimum, 1, is gone)

        Target: O(log n) time.
        """
        raise NotImplementedError
