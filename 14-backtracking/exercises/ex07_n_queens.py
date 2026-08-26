# Scenario: a puzzle-generator needs every way to place N chess queens
# on an N x N board so none attack each other. Pattern: backtracking,
# one queen per row, with O(1) constraint-set pruning instead of
# rescanning the board.
# Run: uv run pytest 14-backtracking -k ex07


def solve_n_queens(n: int) -> list[list[str]]:
    """Return every distinct solution to the N-queens puzzle on an
    `n` x `n` board. Each solution is a list of `n` strings, one per
    row, each string `n` characters long using 'Q' for a queen and
    '.' for an empty square.

    Place exactly one queen per row, choosing its column. Track which
    columns and which diagonals are already occupied using SETS (a
    column set, and two diagonal sets keyed by `row - col` and
    `row + col`) — checking "is this square attacked?" must be O(1),
    not an O(n) rescan of already-placed queens.

    solve_n_queens(1) -> ["Q"]  (i.e. [["Q"]])
    solve_n_queens(2) -> []      (no solution exists for n=2 or n=3)
    solve_n_queens(4) -> 2 boards, e.g.
        [".Q..","...Q","Q...","..Q."] and ["..Q.","Q...","...Q",".Q.."]
        (any order of the outer list; each board's rows must be exact)

    Target: O(n!) time worst case (bounded further by pruning),
    O(n) space for the constraint sets and recursion depth, excluding
    the output.
    """
    raise NotImplementedError


def count_n_queens(n: int) -> int:
    """Return the NUMBER of distinct solutions to the N-queens puzzle
    on an `n` x `n` board, without building the boards themselves
    (count as you go — don't call `solve_n_queens(n)` and take
    `len(...)`, that wastes the work of materializing every board).

    count_n_queens(1) -> 1
    count_n_queens(4) -> 2
    count_n_queens(8) -> 92

    Target: O(n!) time worst case, O(n) space for the constraint sets
    and recursion depth.
    """
    raise NotImplementedError
