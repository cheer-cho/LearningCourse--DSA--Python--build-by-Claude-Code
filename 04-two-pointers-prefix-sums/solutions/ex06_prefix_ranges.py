def build_prefix(nums: list[int]) -> list[int]:
    # Pattern: prefix sums. prefix[0] = 0 is the empty-range base case;
    # each step folds in one more element. O(n) time, O(n) space.
    prefix = [0] * (len(nums) + 1)
    for i, value in enumerate(nums):
        prefix[i + 1] = prefix[i] + value
    return prefix


class RangeSum:
    # Pattern: prefix sums precomputed once so every query is a single
    # subtraction. Build O(n) time/space; query O(1) time.
    def __init__(self, nums: list[int]) -> None:
        self._prefix = build_prefix(nums)

    def query(self, i: int, j: int) -> int:
        return self._prefix[j + 1] - self._prefix[i]


def pivot_index(nums: list[int]) -> int:
    # Pattern: prefix sums via a running total, no array needed.
    # Track the left-side running sum; the right side is always
    # total - left - nums[i]. O(n) time, O(1) extra space.
    total = sum(nums)
    left_sum = 0
    for i, value in enumerate(nums):
        right_sum = total - left_sum - value
        if left_sum == right_sum:
            return i
        left_sum += value
    return -1
