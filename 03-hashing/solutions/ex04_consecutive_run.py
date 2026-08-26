def longest_consecutive(nums: list[int]) -> int:
    # Pattern: the set trick. Only start walking a run from its true
    # start (num - 1 not in the set), so each number is visited exactly
    # once across the whole function, not once per run attempt.
    # Time: O(n). Space: O(n).
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 in num_set:
            continue  # not a run start; it'll be counted from its start

        length = 1
        current = num
        while current + 1 in num_set:
            current += 1
            length += 1
        longest = max(longest, length)

    return longest
