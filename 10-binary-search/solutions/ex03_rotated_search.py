def min_in_rotated(nums: list[int]) -> int:
    # Pattern: rotated binary search. Compare nums[mid] to the last
    # element: if nums[mid] > nums[-1], the minimum is strictly to the
    # right of mid (mid is on the "high" plateau before the drop);
    # otherwise mid could itself be the minimum, so keep it in range.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def search_rotated(nums: list[int], target: int) -> int:
    # Pattern: rotated binary search. At every mid, one half is
    # guaranteed normally sorted (compare nums[mid] to nums[lo]); check
    # if target lies within that sorted half's range to decide which
    # way to go.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half [lo..mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half [mid..hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
