import random


def quick_sort(nums: list[int]) -> None:
    # Pattern: divide & conquer via in-place partitioning (Lomuto).
    # Applies here for O(1) extra space vs merge sort's O(n). Randomized
    # pivot avoids the O(n^2) worst case on adversarial/sorted input;
    # recursing into the smaller side (and looping the larger, instead
    # of recursing) bounds stack depth to O(log n) regardless of pivot
    # luck. Complexity: O(n log n) average time, O(log n) space.
    _quick_sort(nums, 0, len(nums) - 1)


def _quick_sort(nums: list[int], lo: int, hi: int) -> None:
    while lo < hi:
        p = _partition(nums, lo, hi)
        if p - lo < hi - p:
            _quick_sort(nums, lo, p - 1)
            lo = p + 1
        else:
            _quick_sort(nums, p + 1, hi)
            hi = p - 1


def _partition(nums: list[int], lo: int, hi: int) -> int:
    pivot_idx = random.randint(lo, hi)
    nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
    pivot = nums[hi]

    i = lo - 1
    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
    return i + 1
