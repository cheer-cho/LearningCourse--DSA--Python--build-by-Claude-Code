def pair_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    # Pattern: two pointers, opposite ends. Sorted input lets the sum's
    # comparison to target tell us which single pointer must move.
    # O(n) time (each pointer moves at most n times total), O(1) space.
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None
