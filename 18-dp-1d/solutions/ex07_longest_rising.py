from __future__ import annotations


def lis_length(nums: list[int]) -> int:
    # STATE: dp[i] = length of the longest increasing run ending at i.
    # CHOICE: which earlier index j (j < i, nums[j] < nums[i]) to extend.
    # RECURRENCE: dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i]).
    # BASE CASE: dp[i] = 1 for every i.
    # ORDER: bottom-up, i = 0..n-1, j = 0..i-1 (answer = max(dp)).
    # Time: O(n^2), Space: O(n).
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)


def _lower_bound(tails: list[int], x: int) -> int:
    # Module-10 half-open binary-search template: smallest index i in
    # [0, len(tails)) with tails[i] >= x; returns len(tails) if none.
    lo, hi = 0, len(tails)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if tails[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def lis_length_fast(nums: list[int]) -> int:
    # STATE: tails[k] = smallest possible tail value among all
    # increasing subsequences of length k + 1 seen so far.
    # CHOICE: for each x, replace the first tail >= x, or extend.
    # RECURRENCE: tails[lower_bound(tails, x)] = x (patience sorting).
    # BASE CASE: tails starts empty.
    # ORDER: left to right over nums; tails stays sorted throughout.
    # Time: O(n log n), Space: O(n).
    tails: list[int] = []
    for x in nums:
        pos = _lower_bound(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
