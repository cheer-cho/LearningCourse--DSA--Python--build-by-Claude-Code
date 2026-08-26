from collections.abc import Callable


def has_duplicate_naive(nums: list[int], tick: Callable[[], None]) -> bool:
    # Pattern: brute-force all-pairs comparison, one tick per pair.
    # O(n^2) time, O(1) extra space. Deliberately naive -- see
    # has_duplicate_fast for the pattern that removes the bottleneck.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            tick()
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicate_fast(nums: list[int]) -> bool:
    # Pattern: "have I seen this before?" via a hash set.
    # O(n) time, O(n) space -- trades memory for a single linear pass
    # instead of re-scanning the list for every element.
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
