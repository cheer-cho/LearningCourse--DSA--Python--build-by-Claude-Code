def rotate_90_in_place(grid: list[list[int]]) -> None:
    # Pattern: transpose + reverse rows. Transposing reflects across
    # the main diagonal; reversing each row completes a clockwise
    # rotation. Time: O(n^2). Space: O(1).
    n = len(grid)
    for r in range(n):
        for c in range(r + 1, n):
            grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
    for row in grid:
        row.reverse()


def spiral_order(grid: list[list[int]]) -> list[int]:
    # Pattern: four shrinking bounds. Sweep right/down/left/up along
    # the current bounds, tightening after each leg. Time: O(m*n).
    # Space: O(1) extra (excluding output).
    result: list[int] = []
    top, bottom = 0, len(grid) - 1
    left, right = 0, len(grid[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(grid[top][c])
        top += 1

        for r in range(top, bottom + 1):
            result.append(grid[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(grid[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(grid[r][left])
            left += 1

    return result


def zero_rows_cols(grid: list[list[int]]) -> None:
    # Pattern: first row/col as marker storage -- O(1) extra space
    # beyond two booleans. Time: O(m*n). Space: O(1).
    rows, cols = len(grid), len(grid[0])
    first_row_has_zero = any(grid[0][c] == 0 for c in range(cols))
    first_col_has_zero = any(grid[r][0] == 0 for r in range(rows))

    for r in range(1, rows):
        for c in range(1, cols):
            if grid[r][c] == 0:
                grid[r][0] = 0
                grid[0][c] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if grid[r][0] == 0 or grid[0][c] == 0:
                grid[r][c] = 0

    if first_row_has_zero:
        for c in range(cols):
            grid[0][c] = 0

    if first_col_has_zero:
        for r in range(rows):
            grid[r][0] = 0
