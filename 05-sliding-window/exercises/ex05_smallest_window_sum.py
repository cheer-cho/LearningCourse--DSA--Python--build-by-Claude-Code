# Scenario: reading meter counts until you've accumulated at least a
# target amount, minimizing how many readings you needed. Pattern:
# variable-size window, INVERTED shrink rule — shrink WHILE valid, to
# find the shortest window (not the longest).
# Run: uv run pytest 05-sliding-window -k ex05


def shortest_subarray_at_least(nums: list[int], target: int) -> int:
    """Return the length of the shortest contiguous subarray of `nums`
    (all elements >= 0) whose sum is >= `target` (`target` is a
    positive integer). Return 0 if no subarray reaches `target`.

    Grow the right edge, adding to a running sum. Once the window's sum
    is already >= target, shrink from the left WHILE it stays >= target
    (recording the length each time it does) — the opposite loop
    condition from a longest-window search. This inversion only works
    because every `nums[i] >= 0`: shrinking can only ever decrease the
    sum, so once it drops below target you know you shrank one step too
    far.

    shortest_subarray_at_least([2, 3, 1, 2, 4, 3], 7) -> 2   ([4, 3])
    shortest_subarray_at_least([1, 1, 1], 10) -> 0
    shortest_subarray_at_least([5], 5) -> 1

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
