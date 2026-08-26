from ex01_grid_paths import count_paths, count_paths_blocked, min_path_cost


def test_count_paths_square_grid():
    assert count_paths(3, 3) == 6


def test_count_paths_wide_grid():
    assert count_paths(3, 7) == 28


def test_count_paths_single_cell():
    assert count_paths(1, 1) == 1


def test_count_paths_single_row():
    assert count_paths(1, 5) == 1


def test_count_paths_single_column():
    assert count_paths(5, 1) == 1


def test_count_paths_efficiency_large_grid():
    assert count_paths(100, 100) > 0


def test_count_paths_blocked_obstacle_in_middle():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert count_paths_blocked(grid) == 2


def test_count_paths_blocked_obstacle_off_diagonal():
    grid = [[0, 1], [0, 0]]
    assert count_paths_blocked(grid) == 1


def test_count_paths_blocked_start_blocked():
    grid = [[1, 0], [0, 0]]
    assert count_paths_blocked(grid) == 0


def test_count_paths_blocked_end_blocked():
    grid = [[0, 0], [0, 1]]
    assert count_paths_blocked(grid) == 0


def test_count_paths_blocked_no_obstacles_matches_count_paths():
    grid = [[0, 0, 0], [0, 0, 0]]
    assert count_paths_blocked(grid) == count_paths(2, 3)


def test_min_path_cost_typical():
    assert min_path_cost([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7


def test_min_path_cost_small_square():
    assert min_path_cost([[1, 2], [3, 4]]) == 7


def test_min_path_cost_single_cell():
    assert min_path_cost([[5]]) == 5


def test_min_path_cost_single_row_sums_everything():
    assert min_path_cost([[1, 2, 3, 4]]) == 10


def test_min_path_cost_single_column_sums_everything():
    assert min_path_cost([[1], [2], [3]]) == 6
