def three_sum_zero(nums: list[int]) -> list[tuple[int, int, int]]:
    # Pattern: sort + fix the first element + opposite-ends two
    # pointers on the remainder. Sorting turns "find a pair summing to
    # -first" into the same problem ex01 already solves, and sorted
    # order is what lets us skip duplicates in O(1) per skip.
    # O(n log n) sort + O(n^2) scan = O(n^2) time, O(1) extra space
    # (beyond the sort and the output).
    nums = sorted(nums)
    n = len(nums)
    triplets: list[tuple[int, int, int]] = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # already tried this value as the fixed element

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets
