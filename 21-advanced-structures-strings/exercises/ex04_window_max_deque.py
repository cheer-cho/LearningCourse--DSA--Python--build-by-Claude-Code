# Scenario: report the maximum of every sliding window of size k, in
# one linear pass. Pattern: monotonic deque -- the two-ended sibling
# of module 06's monotonic stack. `collections.deque` is fine here
# (this exercise is about the deque TECHNIQUE, not building a deque
# from scratch).
# Run: uv run pytest 21-advanced-structures-strings -k ex04

from __future__ import annotations


def window_maxes(nums: list[int], k: int) -> list[int]:
    """Return the maximum of every contiguous window of size `k` in
    `nums`, in order, using a monotonic deque of INDEXES.

    Keep the deque's indexes in strictly decreasing value order,
    front to back:
    - Before pushing index `i`, pop indexes off the BACK whose value
      is `<= nums[i]` -- they can never be a window max again while
      `nums[i]` is still in play.
    - After pushing, if the FRONT index has fallen outside the
      current window (`front_index <= i - k`), pop it off the front.
    - Once the first full window is formed (`i >= k - 1`), the front
      of the deque is that window's max.

    window_maxes([1, 3, -1, -3, 5, 3, 6, 7], k=3) ->
        [3, 3, 5, 5, 6, 7]
    window_maxes([9, 9, 9], k=1) -> [9, 9, 9]
    window_maxes([], k=3) -> []

    Target: O(n) time total (each index pushed and popped at most
    once), O(k) space.
    """
    raise NotImplementedError
