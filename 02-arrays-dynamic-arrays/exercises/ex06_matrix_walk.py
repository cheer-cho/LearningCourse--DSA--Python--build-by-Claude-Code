# Scenario: summarizing a spreadsheet-like grid of numbers by row and by
# column, and reflecting it for a different layout. Concepts: rows/cols
# indexing conventions (grid[row][col]) that every later grid-based module
# (graphs-as-grids, DP on grids) builds on.
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex06


def row_sums(grid: list[list[int]]) -> list[int]:
    """Return a list with the sum of each row of `grid`, in row order.
    `grid` may be non-square (rows can have different lengths).

    row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    row_sums([[1, 2], [3], []]) -> [3, 3, 0]
    row_sums([]) -> []

    Target complexity: O(rows * cols) time, O(rows) space.
    """
    raise NotImplementedError


def col_sums(grid: list[list[int]]) -> list[int]:
    """Return a list with the sum of each column of `grid`, in column
    order. Assumes every row has the same length (a true rectangular
    grid); `grid` may have zero rows.

    col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    col_sums([]) -> []
    col_sums([[7]]) -> [7]

    Target complexity: O(rows * cols) time, O(cols) space.
    """
    raise NotImplementedError


def main_diagonal(grid: list[list[int]]) -> list[int]:
    """Return the elements grid[0][0], grid[1][1], grid[2][2], ... — the
    main diagonal. For a non-square grid, stop at the smaller dimension
    (min(rows, cols) elements).

    main_diagonal([[1, 2], [3, 4]]) -> [1, 4]
    main_diagonal([[1, 2, 3], [4, 5, 6]]) -> [1, 5]
    main_diagonal([]) -> []

    Target complexity: O(min(rows, cols)) time, O(min(rows, cols)) space.
    """
    raise NotImplementedError


def transpose(grid: list[list[int]]) -> list[list[int]]:
    """Return a NEW grid that is the transpose of `grid` (rows become
    columns): result[c][r] == grid[r][c]. Works for non-square grids —
    an r x c grid transposes to a c x r grid. Does not modify `grid`.
    Assumes every row of `grid` has the same length.

    transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    transpose([[1]]) -> [[1]]
    transpose([]) -> []

    Target complexity: O(rows * cols) time, O(rows * cols) space.
    """
    raise NotImplementedError
