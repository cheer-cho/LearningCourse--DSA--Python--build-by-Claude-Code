def lower_bound(nums: list[int], x: int) -> int:
    # Pattern: THE template with feasible(i) = nums[i] >= x.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(nums: list[int], x: int) -> int:
    # Pattern: THE template with feasible(i) = nums[i] > x.
    # Time: O(log n). Space: O(1).
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def insert_position(nums: list[int], x: int) -> int:
    # Pattern: insert_position is lower_bound by definition (leftmost
    # valid slot keeps existing equal elements to the right of the
    # inserted value).
    # Time: O(log n). Space: O(1).
    return lower_bound(nums, x)
