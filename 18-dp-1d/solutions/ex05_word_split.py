from __future__ import annotations


def can_segment(s: str, words: list[str]) -> bool:
    # STATE: dp[i] = True if prefix s[:i] can be fully split.
    # CHOICE: which earlier split point j (s[:j] already splittable,
    # s[j:i] a whole dictionary word).
    # RECURRENCE: dp[i] = any(dp[j] and s[j:i] in word_set for j < i).
    # BASE CASE: dp[0] = True (empty prefix, zero words used).
    # ORDER: bottom-up, i = 1..n — every dp[j] with j < i already set.
    # Time: O(n^2), Space: O(n) for dp + the word set.
    word_set = set(words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
