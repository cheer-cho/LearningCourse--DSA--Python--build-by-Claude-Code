def reverse(nums: list[int]) -> None:
    # Pattern: opposite-ends two-pointer sweep. Walk one index from the
    # front and one from the back, swapping as they close in — no second
    # array needed.
    # Time: O(n) — each element is touched once. Space: O(1) extra.
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def _reverse_range(nums: list[int], start: int, end: int) -> None:
    """Reverse nums[start:end+1] in place."""
    left, right = start, end
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate_right(nums: list[int], k: int) -> None:
    # Pattern: triple-reversal rotation. Reversing the whole array puts
    # every element in its final "wrapped" order but backwards within each
    # half; reversing each half separately fixes the internal order back
    # up, all without allocating a second array.
    # Time: O(n) — three linear passes. Space: O(1) extra.
    n = len(nums)
    if n == 0:
        return
    k %= n
    if k == 0:
        return
    _reverse_range(nums, 0, n - 1)
    _reverse_range(nums, 0, k - 1)
    _reverse_range(nums, k, n - 1)
