from ex06_matrix_walk import col_sums, main_diagonal, row_sums, transpose


def test_row_sums_typical():
    assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]


def test_row_sums_ragged_rows():
    assert row_sums([[1, 2], [3], []]) == [3, 3, 0]


def test_row_sums_empty_grid():
    assert row_sums([]) == []


def test_col_sums_typical():
    assert col_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]


def test_col_sums_empty_grid():
    assert col_sums([]) == []


def test_col_sums_single_row():
    assert col_sums([[7, 8, 9]]) == [7, 8, 9]


def test_col_sums_single_column():
    assert col_sums([[1], [2], [3]]) == [6]


def test_main_diagonal_square():
    assert main_diagonal([[1, 2], [3, 4]]) == [1, 4]


def test_main_diagonal_wide_rectangle():
    assert main_diagonal([[1, 2, 3], [4, 5, 6]]) == [1, 5]


def test_main_diagonal_tall_rectangle():
    assert main_diagonal([[1, 2], [3, 4], [5, 6]]) == [1, 4]


def test_main_diagonal_empty_grid():
    assert main_diagonal([]) == []


def test_main_diagonal_single_cell():
    assert main_diagonal([[9]]) == [9]


def test_transpose_typical_non_square():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_square():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_transpose_single_cell():
    assert transpose([[1]]) == [[1]]


def test_transpose_empty_grid():
    assert transpose([]) == []


def test_transpose_does_not_mutate_input():
    grid = [[1, 2, 3], [4, 5, 6]]
    transpose(grid)
    assert grid == [[1, 2, 3], [4, 5, 6]]


def test_transpose_twice_returns_original():
    grid = [[1, 2, 3], [4, 5, 6]]
    assert transpose(transpose(grid)) == grid
