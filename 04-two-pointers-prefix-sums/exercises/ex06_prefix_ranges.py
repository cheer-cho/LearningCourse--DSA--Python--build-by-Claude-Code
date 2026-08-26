# Scenario: answering repeated "net change over this date range"
# queries on a year of daily stock-price deltas, without re-summing
# the range from scratch every time. Pattern: prefix sums, precompute
# once, O(1) range queries.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex06


def build_prefix(nums: list[int]) -> list[int]:
    """Return the prefix-sum array of `nums`: length `len(nums) + 1`,
    where `prefix[0] == 0` and `prefix[k]` is the sum of the first `k`
    elements of `nums`.

    build_prefix([3, 1, 4, 1, 5]) -> [0, 3, 4, 8, 9, 14]
    build_prefix([]) -> [0]

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


class RangeSum:
    """Precompute once, then answer inclusive range-sum queries in
    O(1) each -- built on the same prefix-sum idea as `build_prefix`.

    rs = RangeSum([3, 1, 4, 1, 5])
    rs.query(1, 3) -> 6      # 1 + 4 + 1
    rs.query(0, 4) -> 14     # the whole array
    rs.query(2, 2) -> 4      # a single element

    Target complexity: build O(n) time / O(n) space; query O(1) time.
    """

    def __init__(self, nums: list[int]) -> None:
        raise NotImplementedError

    def query(self, i: int, j: int) -> int:
        """Inclusive sum of nums[i..j]."""
        raise NotImplementedError


def pivot_index(nums: list[int]) -> int:
    """Return the leftmost index where the sum of every element to its
    left equals the sum of every element to its right (the pivot
    itself is excluded from both sides). Return -1 if no such index
    exists.

    pivot_index([1, 7, 3, 6, 5, 6]) -> 3   # left 1+7+3=11, right 5+6=11
    pivot_index([1, 2, 3]) -> -1
    pivot_index([0]) -> 0                  # both sides sum to 0

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
