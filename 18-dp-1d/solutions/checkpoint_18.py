from __future__ import annotations

from bisect import bisect_left


def max_earnings(day_pay: list[int]) -> int:
    # STATE: dp[i] = max pay achievable using gig-days 0..i.
    # CHOICE: skip day i (dp[i-1]) or take it (day_pay[i] + dp[i-2]).
    # RECURRENCE: dp[i] = max(dp[i-1], day_pay[i] + dp[i-2]).
    # BASE CASE: dp[-1] = 0 (no days).
    # ORDER: bottom-up, two rolling variables (dp[i] only reads i-1, i-2).
    # Time: O(n), Space: O(1).
    prev2, prev1 = 0, 0
    for pay in day_pay:
        prev2, prev1 = prev1, max(prev1, pay + prev2)
    return prev1


def min_gear_cost(day_costs: list[int]) -> int:
    # STATE: dp[i] = min gear cost to reach day i (0/1 = free starts).
    # CHOICE: arrive at i from i-1 (pay day_costs[i-1]) or i-2 (pay
    # day_costs[i-2]).
    # RECURRENCE: dp[i] = min(dp[i-1] + day_costs[i-1], dp[i-2] + day_costs[i-2]).
    # BASE CASE: dp[0] = dp[1] = 0.
    # ORDER: bottom-up, two rolling variables (dp[i] only reads i-1, i-2).
    # Time: O(n), Space: O(1).
    prev2, prev1 = 0, 0
    for i in range(2, len(day_costs) + 1):
        prev2, prev1 = prev1, min(prev1 + day_costs[i - 1], prev2 + day_costs[i - 2])
    return prev1


def ways_to_fill(n_days: int, block_sizes: list[int]) -> int:
    # STATE: dp[d] = number of distinct orderings of blocks summing to d.
    # CHOICE: which block size is placed LAST.
    # RECURRENCE: dp[d] = sum(dp[d - b] for b in block_sizes if b <= d).
    # BASE CASE: dp[0] = 1 (one way to book zero days: book nothing).
    # ORDER: bottom-up, d = 1..n_days (each dp[d] reads only smaller d).
    # Time: O(n_days * len(block_sizes)), Space: O(n_days).
    dp = [0] * (n_days + 1)
    dp[0] = 1
    for d in range(1, n_days + 1):
        dp[d] = sum(dp[d - b] for b in block_sizes if b <= d)
    return dp[n_days]


def longest_growth_streak(revenues: list[int]) -> int:
    # STATE: tails[k] = smallest possible tail value among all strictly
    # increasing subsequences of length k + 1 seen so far.
    # CHOICE: for each revenue x, replace the first tail >= x, or extend.
    # RECURRENCE: tails[lower_bound(tails, x)] = x (patience sorting,
    # same shape as ex07's lis_length_fast).
    # BASE CASE: tails starts empty.
    # ORDER: left to right over revenues; tails stays sorted throughout.
    # Time: O(n log n), Space: O(n).
    tails: list[int] = []
    for revenue in revenues:
        pos = bisect_left(tails, revenue)
        if pos == len(tails):
            tails.append(revenue)
        else:
            tails[pos] = revenue
    return len(tails)
