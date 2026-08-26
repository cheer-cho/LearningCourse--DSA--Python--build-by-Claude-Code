# Scenario: a sensor logs one reading per second; you need rolling stats
# over a fixed window. Pattern: fixed-size sliding window (add one on the
# right, drop one on the left — never re-sum the whole window).
# Run: uv run pytest 05-sliding-window -k ex01


def max_window_sum(nums: list[int], k: int) -> int:
    """Return the largest sum of any k consecutive elements of `nums`.

    `k` is at least 1 and at most `len(nums)`; raise `ValueError` if not.
    Slide the window by adding the entering element and subtracting the
    leaving one — never re-sum a window from scratch.

    max_window_sum([2, 1, 5, 1, 3, 2], 3) -> 9   (5 + 1 + 3)
    max_window_sum([5], 1) -> 5

    Target: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def moving_averages(nums: list[int], k: int) -> list[float]:
    """Return the average of every window of `k` consecutive elements,
    in order: `result[i]` is the average of `nums[i:i+k]`.

    `k` is at least 1 and at most `len(nums)`; raise `ValueError` if not.
    The result has `len(nums) - k + 1` entries.

    moving_averages([1, 2, 3, 4], 2) -> [1.5, 2.5, 3.5]
    moving_averages([5, 5, 5], 3) -> [5.0]

    Target: O(n) time, O(1) extra space besides the output list.
    """
    raise NotImplementedError
