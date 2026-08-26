def move_zeroes(nums: list[int]) -> None:
    # Pattern: same-direction reader/writer. `write` marks the next
    # slot a non-zero value should occupy; `read` scans ahead of it.
    # O(n) time, O(1) extra space (in-place swaps).
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


def partition_even_odd(nums: list[int]) -> None:
    # Pattern: opposite-ends two pointers, swapping a misplaced odd
    # (found from the left) with a misplaced even (found from the
    # right). O(n) time, O(1) extra space.
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
