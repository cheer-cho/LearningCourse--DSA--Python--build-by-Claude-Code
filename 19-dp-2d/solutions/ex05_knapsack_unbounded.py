from __future__ import annotations


def count_coin_ways(coins: list[int], amount: int) -> int:
    # Pattern: unbounded knapsack, combination count.
    # STATE: dp[a] = number of combinations of coins seen so far summing to a.
    # CHOICE: use one more of the current coin, any number of times.
    # RECURRENCE: dp[a] += dp[a - coin].
    # BASE CASE: dp[0] = 1 (one way to make 0: use nothing).
    # ORDER: coins OUTER, amount inner swept LOW to HIGH -- fixes each coin's
    # "era" so [1,2] and [2,1] are counted once, not twice.
    # Time: O(len(coins) * amount), Space: O(amount).
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]


def max_ribbon_value(lengths: list[int], prices: list[int], total: int) -> int:
    # Pattern: unbounded knapsack, value maximization (rod cutting).
    # STATE: dp[w] = max price obtainable from a sub-ribbon of length w.
    # CHOICE: use one more of the current cut length, any number of times.
    # RECURRENCE: dp[w] = max(dp[w], dp[w - length] + price).
    # BASE CASE: dp[0] = 0; leftover length nothing fits is simply unused.
    # ORDER: lengths OUTER, capacity inner swept LOW to HIGH -- same unbounded shape.
    # Time: O(len(lengths) * total), Space: O(total).
    dp = [0] * (total + 1)
    for length, price in zip(lengths, prices):
        for w in range(length, total + 1):
            dp[w] = max(dp[w], dp[w - length] + price)
    return dp[total]
