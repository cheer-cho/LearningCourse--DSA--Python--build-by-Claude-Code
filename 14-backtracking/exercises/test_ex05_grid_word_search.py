from ex05_grid_word_search import exists_in_grid


def test_exists_in_grid_classic_true():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exists_in_grid(board, "ABCCED") is True


def test_exists_in_grid_classic_false():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exists_in_grid(board, "ABCB") is False


def test_exists_in_grid_does_not_reuse_a_cell():
    # only 2 cells total; "AAA" would need one of them twice
    board = [["A", "A"]]
    assert exists_in_grid(board, "AAA") is False


def test_exists_in_grid_no_adjacency_returns_false():
    # A -> B is adjacent, but B -> C is a diagonal move (not adjacent);
    # only D and A neighbor B, so this trace is impossible.
    board = [
        ["A", "B"],
        ["C", "D"],
    ]
    assert exists_in_grid(board, "ABC") is False


def test_exists_in_grid_single_cell_match():
    assert exists_in_grid([["X"]], "X") is True


def test_exists_in_grid_single_cell_no_match():
    assert exists_in_grid([["X"]], "Y") is False


def test_exists_in_grid_full_snake_path():
    # A boustrophedon layout: ABCDEFGHI traces every cell exactly once,
    # moving only through adjacent cells (right, right, down, left,
    # left, down, right, right).
    board = [
        ["A", "B", "C"],
        ["F", "E", "D"],
        ["G", "H", "I"],
    ]
    assert exists_in_grid(board, "ABCDEFGHI") is True


def test_exists_in_grid_word_longer_than_board_is_false():
    board = [
        ["A", "B", "C"],
        ["F", "E", "D"],
        ["G", "H", "I"],
    ]
    assert exists_in_grid(board, "ABCDEFGHIJ") is False


def test_exists_in_grid_board_restored_after_search():
    board = [
        ["A", "B"],
        ["C", "D"],
    ]
    original = [row.copy() for row in board]
    exists_in_grid(board, "ABDC")
    assert board == original
