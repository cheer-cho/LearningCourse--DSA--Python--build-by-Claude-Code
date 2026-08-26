def max_subarray_sum(nums: list[int]) -> int:
    # Pattern: greedy running-best (Kadane). Reset the running sum to
    # the current element whenever extending would be worse — a
    # negative-going prefix can only drag down what follows it.
    # Complexity: O(n) time, O(1) space.
    best = cur = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)
        best = max(best, cur)
    return best


def max_subarray_bounds(nums: list[int]) -> tuple[int, int, int]:
    # Pattern: Kadane's, tracking the start index of the current run
    # so a reset can also reset "where the best run started."
    # Complexity: O(n) time, O(1) extra space.
    best = cur = nums[0]
    best_start = best_end = cur_start = 0
    for i in range(1, len(nums)):
        num = nums[i]
        if cur + num < num:
            cur = num
            cur_start = i
        else:
            cur = cur + num
        if cur > best:
            best = cur
            best_start = cur_start
            best_end = i
    return (best, best_start, best_end)


def best_trades_unlimited(prices: list[int]) -> int:
    # Pattern: greedy — take every positive daily delta, skip every
    # negative one. Why: a multi-day rise decomposes exactly into the
    # sum of its daily deltas (telescoping), so summing every gain and
    # skipping every loss reconstructs the best possible total.
    # Complexity: O(n) time, O(1) space.
    profit = 0
    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        if delta > 0:
            profit += delta
    return profit
