# Scenario: a pricing tool needs to find two receipts whose totals add
# up to an exact refund amount, and report WHICH two. Pattern:
# complement lookup — the two-sum shape.
# Run: uv run pytest 03-hashing -k ex02


def pair_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return a tuple of two DISTINCT indices (i, j), in any order,
    such that nums[i] + nums[j] == target. Return None if no such pair
    exists. If several pairs work, return any one of them.

    In module 01's "target-pair" exercise, `has_pair_brute` checked
    every index pair (O(n^2)) and `has_pair_fast` only answered
    yes/no. Here we need the actual indices, and we get them in one
    pass: for each value, check whether its COMPLEMENT (target - value)
    was already seen, before adding the current value to the map. That
    ordering also means an element is never paired with itself unless
    it appears twice.

    pair_sum([2, 7, 11, 15], 9) -> (0, 1)      # 2 + 7 == 9
    pair_sum([3, 3], 6) -> (0, 1)              # duplicate values work
    pair_sum([1, 2, 3], 100) -> None

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError
