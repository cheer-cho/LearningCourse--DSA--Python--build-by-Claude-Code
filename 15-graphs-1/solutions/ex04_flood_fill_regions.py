DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def flood_fill(image: list[list[int]], r: int, c: int, color: int) -> list[list[int]]:
    # Pattern: grid-as-graph iterative flood fill. The same-color
    # base-case check is what stops an infinite loop when target ==
    # original color (every neighbor would otherwise look "not yet
    # filled" forever).
    # Complexity: O(rows * cols) time, O(rows * cols) space worst case.
    rows, cols = len(image), len(image[0])
    original = image[r][c]
    if original == color:
        return image

    stack = [(r, c)]
    image[r][c] = color
    while stack:
        cr, cc = stack.pop()
        for dr, dc in DIRS:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = color
                stack.append((nr, nc))
    return image


def capture_regions(board: list[list[str]]) -> list[list[str]]:
    # Pattern: invert the question. Flood fill from every border 'O'
    # first, marking survivors with a temporary sentinel. Then a single
    # pass flips remaining 'O's (enclosed) to 'X' and restores the
    # sentinel back to 'O' (survivors).
    # Why: checking "is this region surrounded" directly means tracing
    # each region's full boundary; border-first flood fill answers the
    # same question in one linear pass.
    # Complexity: O(rows * cols) time, O(rows * cols) space.
    rows, cols = len(board), len(board[0])
    if rows == 0 or cols == 0:
        return board

    SAFE = "#"
    stack = []
    for r in range(rows):
        for c in (0, cols - 1):
            if board[r][c] == "O":
                stack.append((r, c))
    for c in range(cols):
        for r in (0, rows - 1):
            if board[r][c] == "O":
                stack.append((r, c))

    for r, c in stack:
        board[r][c] = SAFE

    while stack:
        cr, cc = stack.pop()
        for dr, dc in DIRS:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                board[nr][nc] = SAFE
                stack.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == SAFE:
                board[r][c] = "O"
    return board
