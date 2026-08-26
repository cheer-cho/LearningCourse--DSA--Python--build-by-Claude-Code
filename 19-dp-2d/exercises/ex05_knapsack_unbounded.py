# Scenario: a cashier counts ways to make change with an unlimited supply
# of each coin, and a mill maximizes revenue cutting a steel rod into
# reusable piece lengths.
# Pattern: unbounded knapsack -- each "item" may be reused any number of
# times, so the take branch reads THIS row/pass, not the previous one.
# Run: uv run pytest 19-dp-2d -k ex05

from __future__ import annotations


def count_coin_ways(coins: list[int], amount: int) -> int:
    """Return the number of distinct COMBINATIONS of `coins` (each
    denomination reusable any number of times) that sum to exactly
    `amount`. Combinations, not permutations: [1, 2] and [2, 1] are the
    SAME combination and must only be counted once.

    Loop order is the whole trick: coins in the OUTER loop, amount in
    the inner loop, swept forward (low to high) -- unbounded reuse.
    Fixing each coin's "era" before moving to the next coin is what
    stops [1, 2] and [2, 1] from being counted separately. Contrast with
    module 18's checkpoint `ways_to_fill`, where amount is the outer
    loop and order DOES matter (permutations).

    STATE: dp[a] = number of combinations that sum to exactly a.
    BASE CASE: dp[0] = 1 (one way to make 0: use no coins).
    RECURRENCE (coin c, amount a): dp[a] += dp[a - c].

    count_coin_ways([1, 2, 5], 5) -> 4    (5; 1+2+2; 1+1+1+2; 1*5)
    count_coin_ways([2], 3) -> 0
    count_coin_ways([10], 0) -> 1

    Target: O(len(coins) * amount) time, O(amount) space.
    """
    raise NotImplementedError


def max_ribbon_value(lengths: list[int], prices: list[int], total: int) -> int:
    """Maximize the total price from cutting a ribbon of length `total`
    into pieces of the given `lengths`, each with a matching entry in
    `prices`. Each length may be used any number of times (unbounded --
    rod-cutting shape).

    STATE: dp[w] = max price obtainable from a sub-ribbon of length w.
    BASE CASE: dp[0] = 0. You are never forced to use the whole ribbon --
    leftover length beyond what any combination of pieces fills is
    simply unused (worth 0), not an error.
    RECURRENCE: for each cut length_i <= w:
    dp[w] = max(dp[w], dp[w - length_i] + price_i). Loop order: lengths
    outer, capacity inner swept forward -- same unbounded shape as
    `count_coin_ways`.

    max_ribbon_value([1, 2, 3], [1, 5, 8], 4) -> 10   (two 2s: 5+5)
    max_ribbon_value([2], [5], 3) -> 5                (one 2, 1 left unused)
    max_ribbon_value([1], [2], 5) -> 10               (five 1s: 2*5)

    Target: O(len(lengths) * total) time, O(total) space.
    """
    raise NotImplementedError
