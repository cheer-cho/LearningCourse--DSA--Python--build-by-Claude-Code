def first_unique_index(s: str) -> int:
    # Pattern: counting map. Pass 1 tallies every character; pass 2 finds
    # the first index whose tally is 1. Two O(n) passes stay O(n) total.
    # Time: O(n). Space: O(k) for k distinct characters.
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


def majority_item(nums: list[int]) -> int:
    # Pattern: counting map. Tally every value, return the one whose
    # count exceeds half the list. Time: O(n). Space: O(n) worst case.
    counts: dict[int, int] = {}
    threshold = len(nums) // 2
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
        if counts[n] > threshold:
            return n
    raise ValueError("no majority element found")
