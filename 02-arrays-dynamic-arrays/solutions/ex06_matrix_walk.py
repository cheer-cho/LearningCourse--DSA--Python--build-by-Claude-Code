def row_sums(grid: list[list[int]]) -> list[int]:
    # Pattern: straightforward grid walk, row by row. Establishes
    # grid[row][col] indexing used throughout later grid-based modules.
    # Time: O(rows * cols) — every cell visited once. Space: O(rows).
    return [sum(row) for row in grid]


def col_sums(grid: list[list[int]]) -> list[int]:
    # Pattern: grid walk transposed — accumulate into one running total
    # per column while sweeping rows, instead of building a transposed
    # grid first.
    # Time: O(rows * cols) — every cell visited once. Space: O(cols).
    if not grid:
        return []
    cols = len(grid[0])
    totals = [0] * cols
    for row in grid:
        for c in range(cols):
            totals[c] += row[c]
    return totals


def main_diagonal(grid: list[list[int]]) -> list[int]:
    # Pattern: single-index walk where row == col. Stopping at
    # min(rows, cols) keeps it safe for non-square grids.
    # Time: O(min(rows, cols)). Space: O(min(rows, cols)) for the result.
    if not grid:
        return []
    steps = min(len(grid), len(grid[0]))
    return [grid[i][i] for i in range(steps)]


def transpose(grid: list[list[int]]) -> list[list[int]]:
    # Pattern: grid walk building a brand-new grid so the input is never
    # mutated; result[c][r] pulls from grid[r][c].
    # Time: O(rows * cols) — every cell visited once. Space: O(rows * cols).
    if not grid:
        return []
    rows, cols = len(grid), len(grid[0])
    return [[grid[r][c] for r in range(rows)] for c in range(cols)]
