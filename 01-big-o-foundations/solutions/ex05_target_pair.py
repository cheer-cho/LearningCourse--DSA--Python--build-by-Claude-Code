def has_pair_brute(nums: list[int], target: int) -> bool:
    # Pattern: brute-force pair check (framework step 2).
    # O(n^2) time, O(1) extra space.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


def has_pair_fast(nums: list[int], target: int) -> bool:
    # Pattern: complement lookup via a hash set (framework step 4).
    # O(n) time, O(n) space -- check "have I already seen target - x?"
    # before adding x, so a single position never pairs with itself.
    seen: set[int] = set()
    for x in nums:
        complement = target - x
        if complement in seen:
            return True
        seen.add(x)
    return False
