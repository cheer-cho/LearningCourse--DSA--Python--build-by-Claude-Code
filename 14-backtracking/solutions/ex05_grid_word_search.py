def exists_in_grid(board: list[list[str]], word: str) -> bool:
    # Pattern: DFS + backtracking on a grid; choose = mark the cell
    # visited in place, explore = recurse into 4 neighbors, unchoose =
    # restore the cell's original character.
    # Why: in-place marking avoids a separate O(rows*cols) visited set
    # per call; restoring on the way back is what lets a DIFFERENT
    # trace reuse this cell later.
    # Complexity: O(rows * cols * 4^len(word)) time, O(len(word)) extra
    # space (recursion stack; the mutation itself is O(1) extra space).
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        original = board[r][c]
        board[r][c] = "#"  # sentinel: can't match any real letter

        found = (
            dfs(r + 1, c, index + 1)
            or dfs(r - 1, c, index + 1)
            or dfs(r, c + 1, index + 1)
            or dfs(r, c - 1, index + 1)
        )

        board[r][c] = original  # unchoose: restore before returning
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
