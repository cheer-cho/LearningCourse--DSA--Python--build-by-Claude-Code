# Scenario: counting how many contiguous stretches of a hiking log's
# daily elevation deltas (uphill days are positive, downhill days are
# negative) net to exactly k meters of gain.
# Pattern: prefix sum + hash map of prefix-value frequencies.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex07


def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    """Return how many contiguous subarrays of `nums` sum to exactly
    `k`. `nums` may contain negative numbers.

    Walk the array once, tracking a running prefix sum. A subarray
    ending at the current position sums to `k` exactly when an earlier
    prefix sum equals `running - k` -- so a hash map counting how many
    times each prefix sum has been seen turns "how many subarrays end
    here with sum k" into an O(1) lookup.

    Because `nums` can hold negatives (the tests include them), a
    sliding window (module 05) can't be used here: shrinking a window
    doesn't monotonically shrink its sum once negative numbers are in
    play, so there's no reliable rule for when to pull the left edge
    in. Prefix sum + hash map works regardless of sign.

    count_subarrays_with_sum([1, 1, 1], 2) -> 2        # [1,1] twice
    count_subarrays_with_sum([1, 2, 3], 3) -> 2         # [1,2] and [3]
    count_subarrays_with_sum([1, -1, 0], 0) -> 3        # [1,-1], [1,-1,0], [0]

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
