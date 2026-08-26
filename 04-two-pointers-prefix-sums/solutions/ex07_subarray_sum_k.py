def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    # Pattern: prefix sum + hash map of prefix-sum frequencies. Works
    # with negatives, unlike a sliding window. O(n) time, O(n) space.
    prefix_counts: dict[int, int] = {0: 1}  # empty prefix seen once
    running = 0
    total = 0
    for value in nums:
        running += value
        total += prefix_counts.get(running - k, 0)
        prefix_counts[running] = prefix_counts.get(running, 0) + 1
    return total
