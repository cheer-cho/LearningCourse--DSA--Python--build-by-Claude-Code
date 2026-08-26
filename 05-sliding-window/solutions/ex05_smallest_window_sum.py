def shortest_subarray_at_least(nums: list[int], target: int) -> int:
    # Pattern: variable-size window, INVERTED shrink rule — shrink WHILE
    # valid to find the shortest window. Safe only because every
    # nums[i] >= 0, so shrinking the window can only ever decrease its
    # sum. Guard `left <= right` defensively (the documented contract
    # requires target > 0, but this keeps the loop safe either way).
    # Time: O(n). Space: O(1).
    left = 0
    total = 0
    best: int | None = None
    for right, value in enumerate(nums):
        total += value
        while total >= target and left <= right:
            length = right - left + 1
            if best is None or length < best:
                best = length
            total -= nums[left]
            left += 1
    return best if best is not None else 0
