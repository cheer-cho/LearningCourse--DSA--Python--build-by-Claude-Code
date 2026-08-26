# Scenario: a vending machine gives change using an arbitrary set of
# coin denominations, unlimited supply of each. Find the fewest coins
# that add up to exactly `amount`, or report it's impossible.
# Pattern: unbounded-choice DP — each state may reuse the same "item"
# any number of times (contrast ex05/ex06, where indices only advance).
# Run: uv run pytest 18-dp-1d -k ex04

from __future__ import annotations


def min_coins(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins (each denomination usable an
    unlimited number of times) that sum to exactly `amount`. Return -1
    if `amount` cannot be made with the given coins.

    STATE: dp[a] = minimum coins to make exactly amount a.
    CHOICE: which coin denomination to use LAST to reach a (unbounded:
    the same denomination can be the "last coin" for many states, and
    a state can reuse a coin already used elsewhere).
    RECURRENCE: dp[a] = min(dp[a - c] + 1 for c in coins if c <= a),
    reading dp[a - c] from a SMALLER amount in the SAME pass — that's
    what makes reuse legal (contrast a 0/1 choice, module 19, which
    must read from a previous row).
    BASE CASE: dp[0] = 0 (zero coins make amount 0). Initialize every
    other dp[a] to +infinity ("not yet known to be reachable") — NOT 0,
    which would make every amount look free.

    Why greedy (always take the biggest coin that fits) fails: with
    coins [1, 3, 4] and amount 6, greedy takes 4, then 1, then 1 — 3
    coins — but 3 + 3 = 6 uses only 2. Greedy is only optimal for coin
    systems specially designed for it (e.g. US currency); DP is correct
    for ANY coin set. (Same honesty box as module 17's greedy chapter:
    greedy needs a proof, DP never does.)

    min_coins([1, 5, 10, 25], 30) -> 2      (25 + 5)
    min_coins([2], 3) -> -1                 (odd amount, only even coin)
    min_coins([1, 3, 4], 6) -> 2            (3 + 3, beats greedy's 3 coins)
    min_coins([1], 0) -> 0

    Target: O(amount * len(coins)) time, O(amount) space.
    """
    raise NotImplementedError
