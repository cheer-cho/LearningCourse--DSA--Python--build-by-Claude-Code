from __future__ import annotations


def best_feature_set(costs: list[int], impacts: list[int], budget: int) -> list[int]:
    # Pattern: 0/1 knapsack, full 2-D table kept for reconstruction.
    # STATE: dp[i][w] = best impact using features[0:i], budget w.
    # CHOICE: skip feature i, or take it if it fits.
    # RECURRENCE: dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost]+impact).
    # BASE CASE: dp[0][*] = 0. Backtrack: dp[i][w] != dp[i-1][w] -> feature
    # i-1 was included; move to dp[i-1][w-cost]; else move to dp[i-1][w].
    # Time: O(n * budget), Space: O(n * budget) -- the table must survive
    # for the backtrack, so the 1-D optimization from ex04 doesn't apply.
    n = len(costs)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost, impact = costs[i - 1], impacts[i - 1]
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if cost <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + impact)

    chosen: list[int] = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= costs[i - 1]
    chosen.sort()
    return chosen


def slogan_similarity(a: str, b: str) -> int:
    # Pattern: two-sequence DP, full table (Wagner-Fischer) -- same shape
    # as ex03's edit_distance, re-implemented from scratch here.
    # STATE: dp[i][j] = edit distance between a[0:i] and b[0:j].
    # RECURRENCE: match -> carry diagonal free; else 1 + min(replace,
    # insert, delete).
    # BASE CASE: dp[0][j] = j, dp[i][0] = i.
    # Time: O(n * m), Space: O(n * m).
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]


def bundle_ways(pack_sizes: list[int], order_size: int) -> int:
    # Pattern: unbounded knapsack, combination count -- same shape as
    # ex05's count_coin_ways, re-implemented from scratch here.
    # STATE: dp[a] = combinations of pack sizes seen so far summing to a.
    # RECURRENCE: dp[a] += dp[a - size].
    # BASE CASE: dp[0] = 1.
    # ORDER: pack sizes OUTER, order size inner swept LOW to HIGH.
    # Time: O(len(pack_sizes) * order_size), Space: O(order_size).
    dp = [0] * (order_size + 1)
    dp[0] = 1
    for size in pack_sizes:
        for a in range(size, order_size + 1):
            dp[a] += dp[a - size]
    return dp[order_size]


def is_fair_split(workloads: list[int]) -> bool:
    # Pattern: 0/1 subset-sum reduction -- same shape as ex04's
    # can_partition_equal, re-implemented from scratch here.
    # STATE: dp[w] = can some subset of workloads seen so far sum to w.
    # RECURRENCE: dp[w] |= dp[w - workload].
    # BASE CASE: dp[0] = True; odd total -> impossible.
    # ORDER: capacity swept HIGH to LOW per workload.
    # Time: O(n * sum(workloads)), Space: O(sum(workloads)).
    total = sum(workloads)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for workload in workloads:
        for w in range(target, workload - 1, -1):
            if dp[w - workload]:
                dp[w] = True
    return dp[target]
