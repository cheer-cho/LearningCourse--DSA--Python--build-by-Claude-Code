def max_window_sum(nums: list[int], k: int) -> int:
    # Pattern: fixed-size sliding window. Seed the sum for the first
    # window, then slide right by adding the entering element and
    # subtracting the leaving one — never re-sum a window from scratch.
    # Time: O(n). Space: O(1).
    n = len(nums)
    if k < 1 or k > n:
        raise ValueError("k must be between 1 and len(nums)")

    window_sum = sum(nums[:k])
    best = window_sum
    for right in range(k, n):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)
    return best


def moving_averages(nums: list[int], k: int) -> list[float]:
    # Pattern: fixed-size sliding window, same add/drop update as
    # max_window_sum, dividing by k at each step instead of tracking a max.
    # Time: O(n). Space: O(1) besides the output list.
    n = len(nums)
    if k < 1 or k > n:
        raise ValueError("k must be between 1 and len(nums)")

    window_sum = sum(nums[:k])
    result = [window_sum / k]
    for right in range(k, n):
        window_sum += nums[right] - nums[right - k]
        result.append(window_sum / k)
    return result
