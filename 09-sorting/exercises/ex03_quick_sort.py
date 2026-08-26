# Scenario: sorting a huge in-memory buffer where you can't afford the
# extra O(n) space merge sort needs.
# Concepts: Lomuto partition, randomized pivot, in-place sorting.
# Run: uv run pytest 09-sorting -k ex03


def quick_sort(nums: list[int]) -> None:
    """Sort `nums` ascending IN PLACE. Returns None (like `list.sort()`).

    Partition around a pivot (any correct partition scheme is fine —
    Lomuto is the one taught in the lesson) chosen RANDOMLY, so no
    input (including already-sorted data) reliably triggers the O(n^2)
    worst case. After partitioning, recurse into the SMALLER side and
    loop (don't recurse) into the larger side — this bounds recursion
    depth to O(log n) even on an adversarial or already-sorted input,
    which matters for arrays too large for a deep call stack.

    nums = [5, 2, 4, 1]; quick_sort(nums) -> nums is now [1, 2, 4, 5]
    nums = []; quick_sort(nums) -> nums is still []

    Target complexity: O(n log n) average time, O(n^2) worst-case time
    (astronomically unlikely with a randomized pivot), O(log n) space
    (recursion stack — bounded by the smaller-side-first trick above).
    """
    raise NotImplementedError
