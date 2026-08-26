# Scenario: a spreadsheet-like grid where every row is sorted ascending
# AND the first value of each row is greater than the last value of the
# row above it — so the whole grid reads like one long sorted list,
# row by row. Pattern: treat the 2D grid as a flat 1D index space and
# run ONE binary search over it.
# Run: uv run pytest 10-binary-search -k ex06


def search_matrix(grid: list[list[int]], target: int) -> bool:
    """Return True if `target` appears anywhere in `grid`, else False.

    `grid` has `m` rows and `n` columns (all rows the same length, `m,
    n >= 1`). Each row is sorted ascending, and `grid[i][0] >
    grid[i - 1][-1]` for every row after the first — so flattening the
    grid row by row gives one fully sorted list of length `m * n`.

    Map a flat index `i` to `grid[i // n][i % n]` and binary-search the
    flat index space directly — don't binary-search each row separately.

    search_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9) -> True
    search_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 4) -> False
    search_matrix([[1]], 1) -> True

    Target: O(log(m * n)) time, O(1) space.
    """
    raise NotImplementedError
