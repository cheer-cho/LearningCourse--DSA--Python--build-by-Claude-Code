from __future__ import annotations


def decode_ways(digits: str) -> int:
    # STATE: dp[i] = number of ways to decode the prefix digits[:i].
    # CHOICE: the last decoded letter used 1 digit or 2 digits.
    # RECURRENCE: dp[i] = dp[i-1] (if digits[i-1] valid alone) +
    # dp[i-2] (if digits[i-2:i] is "10".."26").
    # BASE CASE: dp[0] = 1 (empty prefix, one way: nothing).
    # ORDER: bottom-up, two rolling variables (dp[i] only reads i-1, i-2).
    # Time: O(n), Space: O(1).
    prev2, prev1 = 1, 1  # dp[0] = 1 (empty prefix); prev1 rolls into dp[1]
    for i in range(1, len(digits) + 1):
        current = 0
        if digits[i - 1] != "0":
            current += prev1
        if i >= 2 and "10" <= digits[i - 2 : i] <= "26":
            current += prev2
        prev2, prev1 = prev1, current
    return prev1
