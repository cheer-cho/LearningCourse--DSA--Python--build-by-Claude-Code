from ex06_matrix_search import search_matrix

GRID = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17],
]


def test_search_matrix_finds_middle_row_value():
    assert search_matrix(GRID, 9) is True


def test_search_matrix_finds_top_left():
    assert search_matrix(GRID, 1) is True


def test_search_matrix_finds_bottom_right():
    assert search_matrix(GRID, 17) is True


def test_search_matrix_value_missing_between_rows():
    assert search_matrix(GRID, 4) is False


def test_search_matrix_value_below_range():
    assert search_matrix(GRID, 0) is False


def test_search_matrix_value_above_range():
    assert search_matrix(GRID, 100) is False


def test_search_matrix_single_cell_hit():
    assert search_matrix([[1]], 1) is True


def test_search_matrix_single_cell_miss():
    assert search_matrix([[1]], 2) is False


def test_search_matrix_single_row():
    assert search_matrix([[1, 3, 5, 7, 9]], 7) is True
    assert search_matrix([[1, 3, 5, 7, 9]], 8) is False


def test_search_matrix_single_column():
    grid = [[1], [3], [5], [7]]
    assert search_matrix(grid, 5) is True
    assert search_matrix(grid, 6) is False


def test_search_matrix_large_grid_is_fast():
    n = 1000
    grid = [[r * n + c for c in range(n)] for r in range(n)]  # 1_000_000 cells
    assert search_matrix(grid, 999_999) is True
    assert search_matrix(grid, 1_000_000) is False
