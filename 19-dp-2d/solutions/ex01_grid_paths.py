from __future__ import annotations


def count_paths(rows: int, cols: int) -> int:
    # Pattern: grid DP, collapsed to a single row.
    # STATE: dp[c] = ways to reach the current row at column c.
    # CHOICE: from above (dp[c] pre-update) or from the left (dp[c-1] just updated).
    # RECURRENCE: dp[c] += dp[c-1] each row.
    # BASE CASE: row 0 (and column 0, never touched) is all 1s.
    # Time: O(rows * cols), Space: O(cols).
    dp = [1] * cols
    for _ in range(1, rows):
        for c in range(1, cols):
            dp[c] += dp[c - 1]
    return dp[-1]


def count_paths_blocked(grid: list[list[int]]) -> int:
    # Pattern: grid DP, collapsed to a single row, obstacles zero a cell.
    # STATE: dp[c] = ways to reach the current row at column c.
    # CHOICE: same as count_paths, but a blocked cell contributes 0 ways.
    # RECURRENCE: dp[c] += dp[c-1] when open; dp[c] = 0 when blocked.
    # BASE CASE: (0, 0) starts at 1 unless blocked.
    # Time: O(rows * cols), Space: O(cols).
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    dp = [0] * cols
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dp[c] = 0
                continue
            if r == 0 and c == 0:
                dp[c] = 1
            elif c > 0:
                dp[c] += dp[c - 1]
            # c == 0 and r > 0: dp[c] already holds the value from above.
    return dp[-1]


def min_path_cost(grid: list[list[int]]) -> int:
    # Pattern: grid DP, collapsed to a single row.
    # STATE: dp[c] = min cost to reach the current row at column c.
    # CHOICE: arrive from above or from the left; take the cheaper one.
    # RECURRENCE: dp[c] = grid[r][c] + min(dp[c], dp[c-1]).
    # BASE CASE: (0, 0) starts at grid[0][0]; row 0 / column 0 only accumulate.
    # Time: O(rows * cols), Space: O(cols).
    rows, cols = len(grid), len(grid[0])
    dp = [0] * cols
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[c] = grid[r][c]
            elif r == 0:
                dp[c] = dp[c - 1] + grid[r][c]
            elif c == 0:
                dp[c] = dp[c] + grid[r][c]
            else:
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
    return dp[-1]
