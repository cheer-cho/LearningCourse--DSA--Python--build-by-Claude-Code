# Scenario: a sensor logs a daily net-change reading (can be negative)
# and a trading desk wants the best unlimited-trades strategy on a
# price history. Pattern: greedy running-best (Kadane's algorithm).
# Run: uv run pytest 17-greedy-intervals -k ex01


def max_subarray_sum(nums: list[int]) -> int:
    """Return the largest sum of any contiguous, non-empty subarray of
    `nums`. `nums` has at least one element and may be all negative —
    in that case return the largest (least negative) single element.

    Kadane's algorithm: carry a running sum `cur`. At each element,
    `cur` is either "extend the previous run" (`cur + nums[i]`) or
    "start fresh here" (`nums[i]`) — take whichever is larger. A run
    that has gone negative can only drag down anything appended after
    it, so restarting loses nothing.

    max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6   ([4,-1,2,1])
    max_subarray_sum([-3, -1, -2]) -> -1
    max_subarray_sum([5]) -> 5

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def max_subarray_bounds(nums: list[int]) -> tuple[int, int, int]:
    """Same problem as `max_subarray_sum`, but also report WHERE the
    best subarray is. Return `(best_sum, start_index, end_index)` with
    both indices inclusive. If several subarrays tie for the best sum,
    return any one of them.

    max_subarray_bounds([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> (6, 3, 6)
    max_subarray_bounds([5]) -> (5, 0, 0)

    Target: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def best_trades_unlimited(prices: list[int]) -> int:
    """`prices[i]` is a stock's price on day `i`. You may buy and sell
    an unlimited number of times, but must sell before buying again
    (never hold more than one share). Return the maximum total profit.

    Greedy proof sketch: any profitable multi-day rise `prices[a] ->
    prices[b]` (a < b) equals the sum of every single-day delta
    `prices[i+1] - prices[i]` for `a <= i < b` — buying at `a` and
    selling at `b` nets exactly the sum of those daily deltas, since
    the sale/purchase prices in between cancel out telescopically.
    So summing every POSITIVE daily delta (and skipping every negative
    one, since you'd simply not trade on those days) reconstructs the
    best possible total — no exchange argument beats "take every gain,
    skip every loss."

    best_trades_unlimited([7, 1, 5, 3, 6, 4]) -> 7   (1->5, 3->6)
    best_trades_unlimited([7, 6, 4, 3, 1]) -> 0      (never profitable)
    best_trades_unlimited([]) -> 0

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
