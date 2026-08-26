from __future__ import annotations


def edit_distance(a: str, b: str) -> int:
    # Pattern: two-sequence DP, full table (Wagner-Fischer).
    # STATE: dp[i][j] = edit distance between a[0:i] and b[0:j].
    # CHOICE: match is free (diagonal); else cheapest of replace/insert/delete.
    # RECURRENCE: dp[i][j] = dp[i-1][j-1] if match, else
    #   1 + min(dp[i-1][j-1] replace, dp[i][j-1] insert, dp[i-1][j] delete).
    # BASE CASE: dp[0][j] = j, dp[i][0] = i (pure insertions/deletions).
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
