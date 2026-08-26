def find_peak(nums: list[int]) -> int:
    # Pattern: binary search on an unsorted array. The array isn't
    # monotone, but the slope at mid is: uphill (nums[mid] <
    # nums[mid+1]) guarantees a peak to the right, downhill-or-flat
    # guarantees one at mid or to the left. Exactly one half is ruled
    # out per step, which is all binary search actually requires.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
