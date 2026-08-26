# Scenario: compare two DNA strands and find how much they share, where
# "shared" allows gaps but never reorders characters.
# Pattern: two-sequence DP -- dp[i][j] over prefixes of both strings.
# Run: uv run pytest 19-dp-2d -k ex02

from __future__ import annotations


def lcs_length(a: str, b: str) -> int:
    """Return the length of the Longest Common Subsequence (LCS) of `a`
    and `b`. A subsequence keeps the original order but may skip
    characters (it need not be contiguous -- that would be a substring).

    STATE: dp[i][j] = LCS length of a[0:i] and b[0:j].
    CHOICE: if a[i-1] == b[j-1], extend the diagonal match; otherwise
    take the best of dropping the last character of a or of b.
    RECURRENCE: dp[i][j] = dp[i-1][j-1] + 1 if a[i-1] == b[j-1], else
    max(dp[i-1][j], dp[i][j-1]).
    BASE CASE: dp[0][j] = dp[i][0] = 0 (an empty prefix shares nothing).

    lcs_length("ace", "abcde") -> 3   ("ace")
    lcs_length("abc", "abc") -> 3
    lcs_length("abc", "def") -> 0
    lcs_length("", "abc") -> 0

    Target: O(n * m) time, O(n * m) space (n = len(a), m = len(b)).
    """
    raise NotImplementedError


def lcs_string(a: str, b: str) -> str:
    """Reconstruct one actual Longest Common Subsequence of `a` and `b`.

    Fill the same table as `lcs_length`, then walk it BACKWARDS from
    dp[n][m]: if a[i-1] == b[j-1], that character is in the LCS -- step
    diagonally (i-1, j-1) and record it; otherwise step toward whichever
    neighbor holds the larger value, dp[i-1][j] or dp[i][j-1] (ties go
    up). Collect matches back-to-front, then reverse them.

    lcs_string("ace", "abcde") -> "ace"
    lcs_string("abcba", "abcbcba") -> "abcba"
    lcs_string("", "abc") -> ""

    Target: O(n * m) time, O(n * m) space.
    """
    raise NotImplementedError
