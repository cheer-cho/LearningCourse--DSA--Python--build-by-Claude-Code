def binary_search(nums: list[int], target: int) -> int:
    # Pattern: THE course template (half-open [lo, hi), lo < hi, mid
    # rounds down). feasible(i) = nums[i] >= target; the landing index
    # is a hit only if it actually holds target.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(nums) and nums[lo] == target:
        return lo
    return -1


def _lower_bound(nums: list[int], x: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _upper_bound(nums: list[int], x: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def count_occurrences(nums: list[int], target: int) -> int:
    # Pattern: boundary search. The run of matching values sits exactly
    # between lower_bound(target) and upper_bound(target); no need to
    # walk the run itself.
    # Time: O(log n) (two binary searches). Space: O(1).
    return _upper_bound(nums, target) - _lower_bound(nums, target)
