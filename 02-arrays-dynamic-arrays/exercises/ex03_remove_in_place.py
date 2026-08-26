# Scenario: cleaning up an inventory list — drop every unit of a recalled
# item, and collapse duplicate sensor readings — without allocating a new
# list. Concepts: the reader/writer two-index sweep.
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex03


def remove_value(nums: list[int], val: int) -> int:
    """Remove every occurrence of `val` from `nums`, in place, packing the
    surviving elements at the front in their original relative order.
    Return the new logical length. Elements past the returned length are
    left in an unspecified state (don't care what they are).

    nums = [3, 2, 3, 5]; remove_value(nums, 3) -> 2, and nums[:2] == [2, 5]
    nums = [1, 1, 1]; remove_value(nums, 1) -> 0
    nums = []; remove_value(nums, 9) -> 0

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def dedupe_sorted(nums: list[int]) -> int:
    """`nums` is sorted ascending. Remove duplicates in place so each
    distinct value appears once, keeping the survivors at the front in
    sorted order. Return the new logical length. Elements past the
    returned length are left in an unspecified state.

    nums = [1, 1, 2, 2, 3]; dedupe_sorted(nums) -> 3, and nums[:3] == [1, 2, 3]
    nums = []; dedupe_sorted(nums) -> 0
    nums = [5]; dedupe_sorted(nums) -> 1

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
