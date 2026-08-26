# Scenario: a spell-checker scores how far a typed word is from a
# dictionary word, in single-character edits.
# Pattern: two-sequence DP -- the Wagner-Fischer edit-distance table.
# Run: uv run pytest 19-dp-2d -k ex03

from __future__ import annotations


def edit_distance(a: str, b: str) -> int:
    """Return the minimum number of single-character edits (insert,
    delete, replace -- each costing 1) needed to transform `a` into `b`.

    STATE: dp[i][j] = edit distance between a[0:i] and b[0:j].
    CHOICE: if a[i-1] == b[j-1], no edit needed here -- carry the
    diagonal value forward for free. Otherwise pick the cheapest of the
    three moves that feed this cell.
    RECURRENCE (each move maps to one edit operation):
      dp[i][j] = dp[i-1][j-1]                                if a[i-1] == b[j-1]  (match, free)
      dp[i][j] = 1 + min(dp[i-1][j-1],   # REPLACE a[i-1] with b[j-1]
                          dp[i][j-1],     # INSERT b[j-1] into a
                          dp[i-1][j])     # DELETE a[i-1]
                                                              otherwise
    BASE CASE: dp[0][j] = j (insert j characters into an empty a);
    dp[i][0] = i (delete all i characters of a).

    edit_distance("horse", "ros") -> 3
    edit_distance("intention", "execution") -> 5
    edit_distance("", "abc") -> 3
    edit_distance("abc", "abc") -> 0

    Target: O(n * m) time, O(n * m) space (n = len(a), m = len(b)).
    """
    raise NotImplementedError
