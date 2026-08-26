import random


def kth_largest(nums: list[int], k: int) -> int:
    # Pattern: quickselect — reuse quick sort's partition step, but
    # recurse into only the ONE side that can contain the answer
    # (never both). Applies here because we only need one order
    # statistic, not a full sort. Complexity: O(n) average time (each
    # step throws away ~half the remaining array), O(n^2) worst case
    # (astronomically unlikely with a randomized pivot); O(n) space
    # for the working copy (never mutate the caller's list).
    nums = nums[:]  # partition in a scratch copy; never mutate the caller's list
    target_idx = len(nums) - k  # kth largest == (len - k)th smallest, 0-indexed
    lo, hi = 0, len(nums) - 1

    while True:
        p = _partition(nums, lo, hi)
        if p == target_idx:
            return nums[p]
        if p < target_idx:
            lo = p + 1
        else:
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
