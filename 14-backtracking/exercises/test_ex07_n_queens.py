from ex07_n_queens import count_n_queens, solve_n_queens


def is_valid_board(board: list[str]) -> bool:
    n = len(board)
    queens = [(r, row.index("Q")) for r, row in enumerate(board) if "Q" in row]
    assert len(queens) == n, "every row must have exactly one queen"
    cols = {c for _, c in queens}
    diag1 = {r - c for r, c in queens}
    diag2 = {r + c for r, c in queens}
    return len(cols) == n and len(diag1) == n and len(diag2) == n


def test_solve_n_queens_size_one():
    assert solve_n_queens(1) == [["Q"]]


def test_solve_n_queens_no_solution_for_two_or_three():
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []


def test_solve_n_queens_four_has_exactly_two_boards():
    result = solve_n_queens(4)
    assert len(result) == 2
    for board in result:
        assert len(board) == 4
        assert all(len(row) == 4 for row in board)
        assert is_valid_board(board)


def test_solve_n_queens_boards_are_distinct():
    result = solve_n_queens(5)
    as_tuples = {tuple(board) for board in result}
    assert len(as_tuples) == len(result)


def test_solve_n_queens_every_board_is_valid():
    for board in solve_n_queens(6):
        assert is_valid_board(board)


def test_count_n_queens_matches_known_values():
    assert count_n_queens(1) == 1
    assert count_n_queens(2) == 0
    assert count_n_queens(3) == 0
    assert count_n_queens(4) == 2


def test_count_n_queens_eight_is_ninety_two():
    assert count_n_queens(8) == 92


def test_count_n_queens_matches_solve_n_queens_length():
    for n in (1, 4, 5, 6):
        assert count_n_queens(n) == len(solve_n_queens(n))
