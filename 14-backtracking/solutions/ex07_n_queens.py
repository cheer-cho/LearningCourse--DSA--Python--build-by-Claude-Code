def solve_n_queens(n: int) -> list[list[str]]:
    # Pattern: backtracking, one queen per row (row is implicit in
    # recursion depth) + O(1) constraint-set pruning instead of an
    # O(n) rescan of already-placed queens per candidate square.
    # Why: a queen attacks its column and both diagonals; `row - col`
    # is constant along one diagonal direction, `row + col` along the
    # other, so set membership answers "is this square attacked?" in
    # O(1).
    # Complexity: O(n!) time worst case (pruned well below that in
    # practice), O(n) space for the sets and recursion, excl. output.
    results: list[list[str]] = []
    cols_used: set[int] = set()
    diag1_used: set[int] = set()  # row - col
    diag2_used: set[int] = set()  # row + col
    queen_col_per_row: list[int] = []

    def backtrack(row: int) -> None:
        if row == n:
            board = []
            for placed_col in queen_col_per_row:
                board.append("." * placed_col + "Q" + "." * (n - placed_col - 1))
            results.append(board)
            return

        for col in range(n):
            if col in cols_used or (row - col) in diag1_used or (row + col) in diag2_used:
                continue

            cols_used.add(col)
            diag1_used.add(row - col)
            diag2_used.add(row + col)
            queen_col_per_row.append(col)

            backtrack(row + 1)

            queen_col_per_row.pop()
            cols_used.remove(col)
            diag1_used.remove(row - col)
            diag2_used.remove(row + col)

    backtrack(0)
    return results


def count_n_queens(n: int) -> int:
    # Pattern: identical search to solve_n_queens, but counts leaves
    # instead of materializing boards — avoids the O(n^2) cost of
    # building a board string for every solution just to discard it.
    # Complexity: O(n!) time worst case, O(n) space for the sets.
    cols_used: set[int] = set()
    diag1_used: set[int] = set()
    diag2_used: set[int] = set()
    count = 0

    def backtrack(row: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if col in cols_used or (row - col) in diag1_used or (row + col) in diag2_used:
                continue

            cols_used.add(col)
            diag1_used.add(row - col)
            diag2_used.add(row + col)

            backtrack(row + 1)

            cols_used.remove(col)
            diag1_used.remove(row - col)
            diag2_used.remove(row + col)

    backtrack(0)
    return count
