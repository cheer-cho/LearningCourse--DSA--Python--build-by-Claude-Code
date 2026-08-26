# Scenario: a SORTED list of temperature readings; find two readings
# that sum to a target value, using position in the sorted list only
# (no hash map). Pattern: two pointers, opposite ends.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex01


def pair_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """Find two indices in a SORTED list whose values sum to `target`.

    `nums` is sorted ascending (may contain duplicates). Walk from both
    ends toward the middle: if the current sum is too small, the only
    way to grow it is to move the left pointer up (everything to its
    right is >= it); if it's too big, move the right pointer down.

    This is the same problem module 03 solved with a hash set in O(n)
    time and O(n) extra space. Sorting buys the space back: same O(n)
    time, but O(1) extra space, in exchange for requiring sorted input.

    Returns the first matching pair of indices `(i, j)` with `i < j`
    found by the closing-in scan, or `None` if no pair sums to
    `target`.

    pair_sum_sorted([2, 7, 11, 15], 9) -> (0, 1)
    pair_sum_sorted([1, 2, 3], 100) -> None
    pair_sum_sorted([-3, -1, 0, 2, 5], 2) -> (0, 4)

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
