# Scenario: a firmware image processor needs three in-place grid
# moves: rotate a camera frame 90 degrees, read a sensor grid in
# spiral order, and zero out any row/column with a fault code -- all
# without allocating a second grid. Pattern: in-place matrix index
# math (transpose+reverse, shrinking bounds, marker row/col).
# Run: uv run pytest 20-bit-manipulation-math -k ex05


def rotate_90_in_place(grid: list[list[int]]) -> None:
    """Rotate a square `n x n` grid 90 degrees clockwise, IN PLACE
    (mutate `grid`; return nothing, allocate no second grid).

    Recipe: transpose (swap `grid[r][c]` with `grid[c][r]` for every
    `c > r`), then reverse each row. Transposing reflects across the
    main diagonal; reversing each row then turns that reflection into
    a true clockwise rotation.

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_90_in_place(grid) -> grid is now [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    `grid` is `n x n` with `n >= 1`. Target complexity: O(n^2) time,
    O(1) extra space.
    """
    raise NotImplementedError


def spiral_order(grid: list[list[int]]) -> list[int]:
    """Return every element of an `m x n` grid in clockwise spiral
    order, starting from the top-left corner.

    Walk with four shrinking bounds (`top`, `bottom`, `left`,
    `right`): sweep right across `top`, down along `right`, left
    across `bottom`, up along `left`, tightening the matching bound
    after each leg, stopping once `top > bottom` or `left > right`.
    No visited-set needed -- the bounds alone prevent revisiting.

    spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        -> [1, 2, 3, 6, 9, 8, 7, 4, 5]
    spiral_order([[1], [2], [3]]) -> [1, 2, 3]

    `grid` has `m >= 1` rows and `n >= 1` columns (rectangular, not
    necessarily square). Target complexity: O(m*n) time, O(1) extra
    space (excluding the returned list).
    """
    raise NotImplementedError


def zero_rows_cols(grid: list[list[int]]) -> None:
    """For every cell that is 0, zero out its entire row AND column --
    IN PLACE, using O(1) extra space (no second grid, no extra set).

    The classic trick: use the first row and first column of `grid`
    itself as marker storage.
      1. Record (in two plain booleans) whether the first row and
         first column ALREADY contain a 0 -- you're about to overwrite
         them with markers and would otherwise lose this information.
      2. Scan the interior (`row >= 1`, `col >= 1`): whenever
         `grid[row][col] == 0`, write a 0 marker at `grid[row][0]` and
         `grid[0][col]`.
      3. Scan the interior again: zero out `grid[row][col]` if its
         row marker `grid[row][0]` or column marker `grid[0][col]` is
         0.
      4. Apply the two saved booleans to zero the first row/column
         themselves, if needed.

    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    zero_rows_cols(grid) -> grid is now [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    `grid` is `m x n` with `m, n >= 1`. Target complexity: O(m*n)
    time, O(1) extra space.
    """
    raise NotImplementedError
