import copy

from ex05_matrix_moves import rotate_90_in_place, spiral_order, zero_rows_cols

# -- rotate_90_in_place -----------------------------------------------------


def test_rotate_90_in_place_typical():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_90_in_place(grid)
    assert grid == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_rotate_90_in_place_single_cell():
    grid = [[5]]
    rotate_90_in_place(grid)
    assert grid == [[5]]


def test_rotate_90_in_place_two_by_two():
    grid = [[1, 2], [3, 4]]
    rotate_90_in_place(grid)
    assert grid == [[3, 1], [4, 2]]


def test_rotate_90_in_place_four_times_is_identity():
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grid = copy.deepcopy(original)
    for _ in range(4):
        rotate_90_in_place(grid)
    assert grid == original


def test_rotate_90_in_place_mutates_the_same_object():
    grid = [[1, 2], [3, 4]]
    result = rotate_90_in_place(grid)
    assert result is None
    assert grid == [[3, 1], [4, 2]]


# -- spiral_order ---------------------------------------------------------


def test_spiral_order_square():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(grid) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_spiral_order_single_cell():
    assert spiral_order([[7]]) == [7]


def test_spiral_order_single_row():
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]


def test_spiral_order_single_column():
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]


def test_spiral_order_rectangular_wider_than_tall():
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(grid) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_spiral_order_rectangular_taller_than_wide():
    grid = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert spiral_order(grid) == [1, 2, 4, 6, 8, 7, 5, 3]


def test_spiral_order_does_not_mutate_input():
    grid = [[1, 2], [3, 4]]
    spiral_order(grid)
    assert grid == [[1, 2], [3, 4]]


# -- zero_rows_cols ---------------------------------------------------------


def test_zero_rows_cols_typical():
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    zero_rows_cols(grid)
    assert grid == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_zero_rows_cols_no_zeros_unchanged():
    grid = [[1, 2], [3, 4]]
    zero_rows_cols(grid)
    assert grid == [[1, 2], [3, 4]]


def test_zero_rows_cols_zero_in_first_row_and_col():
    grid = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
    zero_rows_cols(grid)
    assert grid == [[0, 0, 0], [0, 5, 6], [0, 8, 9]]


def test_zero_rows_cols_multiple_zeros():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    zero_rows_cols(grid)
    assert grid == [[1, 1, 0], [1, 1, 0], [0, 0, 0]]


def test_zero_rows_cols_all_zeros():
    grid = [[0, 0], [0, 0]]
    zero_rows_cols(grid)
    assert grid == [[0, 0], [0, 0]]


def test_zero_rows_cols_single_row():
    grid = [[1, 0, 3]]
    zero_rows_cols(grid)
    assert grid == [[0, 0, 0]]
