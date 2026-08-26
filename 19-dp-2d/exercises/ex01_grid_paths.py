# Scenario: a delivery robot on a warehouse floor can only move right or
# down. Count its routes, handle blocked cells, and find the cheapest route
# through a grid of per-cell costs.
# Pattern: grid DP -- dp[r][c] built from the cell above and the cell left.
# Run: uv run pytest 19-dp-2d -k ex01

from __future__ import annotations


def count_paths(rows: int, cols: int) -> int:
    """Count distinct paths from the top-left to the bottom-right corner
    of a `rows` x `cols` grid, moving only right or down one cell at a
    time.

    STATE: dp[r][c] = number of ways to reach cell (r, c).
    CHOICE: arrive from the cell above (r-1, c) or from the cell to the
    left (r, c-1).
    RECURRENCE: dp[r][c] = dp[r-1][c] + dp[r][c-1].
    BASE CASE: dp[0][c] = 1 for every c, dp[r][0] = 1 for every r (only
    one way to reach any cell on the top row or the left column).

    Space optimization required: collapse the table to a single 1-D row
    of length `cols`, updated left to right -- `dp[c]` (before this
    update) holds "from above", `dp[c-1]` (already updated this pass)
    holds "from the left".

    count_paths(3, 3) -> 6
    count_paths(3, 7) -> 28
    count_paths(1, 1) -> 1

    Target: O(rows * cols) time, O(cols) space (1-row optimization).
    """
    raise NotImplementedError


def count_paths_blocked(grid: list[list[int]]) -> int:
    """Count distinct paths from the top-left to the bottom-right of
    `grid`, moving only right or down, where `grid[r][c] == 1` means an
    obstacle (impassable) and `0` means open. If the start or the end
    cell is blocked, no path exists.

    Same STATE/CHOICE/RECURRENCE as `count_paths`; a blocked cell simply
    contributes 0 ways regardless of what feeds it.

    count_paths_blocked([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) -> 2
    count_paths_blocked([[0, 1], [0, 0]]) -> 1
    count_paths_blocked([[1, 0], [0, 0]]) -> 0

    Target: O(rows * cols) time, O(cols) space.
    """
    raise NotImplementedError


def min_path_cost(grid: list[list[int]]) -> int:
    """Return the minimum-cost path from the top-left to the
    bottom-right of `grid` (non-negative integers), moving only right or
    down. A path's cost is the sum of every cell it visits, including
    the start and the end.

    STATE: dp[r][c] = minimum cost to reach cell (r, c).
    CHOICE: arrive from above or from the left; take the cheaper one.
    RECURRENCE: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]).
    BASE CASE: dp[0][0] = grid[0][0]; the rest of row 0 and column 0
    accumulate left-to-right / top-to-bottom (no other option exists).

    min_path_cost([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) -> 7
    min_path_cost([[1, 2], [3, 4]]) -> 7
    min_path_cost([[5]]) -> 5

    Target: O(rows * cols) time, O(cols) space.
    """
    raise NotImplementedError
