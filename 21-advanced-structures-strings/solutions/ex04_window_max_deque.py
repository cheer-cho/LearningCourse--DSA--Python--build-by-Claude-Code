from __future__ import annotations

from collections import deque


def window_maxes(nums: list[int], k: int) -> list[int]:
    # Pattern: monotonic deque, storing indexes in strictly
    # decreasing value order front-to-back -- the two-ended sibling
    # of a monotonic stack (module 06). Complexity: O(n) time total
    # (each index pushed and popped at most once), O(k) space.
    if not nums or k <= 0 or k > len(nums):
        return []

    dq: deque[int] = deque()
    result: list[int] = []

    for i, val in enumerate(nums):
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
