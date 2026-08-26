# Scenario: count how "unsorted" a list is, in O(n log n), by riding
# along with merge sort's merge step. Pattern: divide & conquer.
# Run: uv run pytest 08-recursion-divide-conquer -k ex05


def count_inversions(nums: list[int]) -> int:
    """Count the inversions in `nums`: pairs of indices (i, j) with
    i < j and nums[i] > nums[j]. A sorted list has 0 inversions; a
    reverse-sorted list has the maximum, n * (n - 1) / 2.

    Uses divide & conquer, not the O(n^2) pairwise scan:
    - Split: divide nums into a left half and a right half.
    - Solve: recursively count inversions inside each half.
    - Combine: merge the two (already-sorted-by-recursion) halves back
      together, and while merging, every time an element from the right
      half is placed before elements still remaining in the left half,
      each of those remaining left elements forms an inversion with it —
      add that count.

    Does not mutate `nums`.

    count_inversions([1, 2, 3]) -> 0
    count_inversions([3, 2, 1]) -> 3
    count_inversions([2, 4, 1, 3, 5]) -> 3

    Target: O(n log n) time, O(n) space.
    """
    raise NotImplementedError
