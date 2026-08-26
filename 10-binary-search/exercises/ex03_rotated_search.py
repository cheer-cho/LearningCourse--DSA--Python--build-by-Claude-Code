# Scenario: a circular log buffer got dumped starting from a random
# offset, so the sorted data now looks "sorted then wraps". Pattern:
# rotated binary search — at every step, one half is still normally
# sorted; use that half to decide where to go.
# Run: uv run pytest 10-binary-search -k ex03


def min_in_rotated(nums: list[int]) -> int:
    """Return the minimum value in `nums`, a sorted-ascending array of
    UNIQUE values that has been rotated some unknown number of times
    (possibly zero).

    [4, 5, 6, 7, 0, 1, 2] was [0, 1, 2, 4, 5, 6, 7] rotated by 4.
    min_in_rotated([4, 5, 6, 7, 0, 1, 2]) -> 0
    min_in_rotated([1, 2, 3, 4, 5]) -> 1   (rotation by 0)
    min_in_rotated([2, 1]) -> 1

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError


def search_rotated(nums: list[int], target: int) -> int:
    """Find `target` in `nums`, a sorted-ascending array of UNIQUE values
    rotated some unknown number of times. Return its index, or -1 if
    absent.

    search_rotated([4, 5, 6, 7, 0, 1, 2], 0) -> 4
    search_rotated([4, 5, 6, 7, 0, 1, 2], 3) -> -1
    search_rotated([1], 1) -> 0
    search_rotated([1, 2, 3, 4, 5], 5) -> 4   (rotation by 0)

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError
