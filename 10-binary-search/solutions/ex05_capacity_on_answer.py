def _days_needed(weights: list[int], capacity: int) -> int:
    days = 1
    current = 0
    for w in weights:
        if current + w > capacity:
            days += 1
            current = w
        else:
            current += w
    return days


def min_capacity(weights: list[int], d: int) -> int:
    # Pattern: search on the answer. can(cap) = "finishes within d days
    # at this capacity" is monotone -- a bigger capacity never needs
    # more days -- so binary-search the smallest feasible capacity in
    # [max(weights), sum(weights)].
    # Time: O(n log(sum(weights))). Space: O(1).
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if _days_needed(weights, mid) <= d:
            hi = mid
        else:
            lo = mid + 1
    return lo


def split_min_largest(nums: list[int], k: int) -> int:
    # Pattern: identical predicate to min_capacity -- "can I split into
    # <= k contiguous parts each with sum <= X?" -- just asked about a
    # general list instead of a shipping schedule.
    # Time: O(n log(sum(nums))). Space: O(1).
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if _days_needed(nums, mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
