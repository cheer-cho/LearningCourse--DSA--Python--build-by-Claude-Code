from ex03_island_count import count_islands, max_island_area


def test_count_islands_basic():
    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]
    assert count_islands(grid) == 2


def test_count_islands_no_land():
    assert count_islands([[0, 0], [0, 0]]) == 0


def test_count_islands_all_land_is_one_island():
    grid = [[1, 1], [1, 1]]
    assert count_islands(grid) == 1


def test_count_islands_single_cell_land():
    assert count_islands([[1]]) == 1


def test_count_islands_diagonal_land_is_not_connected():
    # diagonal adjacency does NOT count -> 4 separate islands
    grid = [
        [1, 0],
        [0, 1],
    ]
    assert count_islands(grid) == 2


def test_count_islands_does_not_mutate_input():
    grid = [
        [1, 1, 0],
        [0, 0, 1],
    ]
    original = [row.copy() for row in grid]
    count_islands(grid)
    assert grid == original


def test_count_islands_large_grid_is_fast():
    # 300x300 grid: forces visited discipline (an unvisited-tracking
    # bug re-explores cells and blows up time/recursion); iterative or
    # careful recursion must finish quickly regardless.
    size = 300
    grid = [[1] * size for _ in range(size)]
    # carve out water stripes every other row to create many islands
    for r in range(1, size, 2):
        for c in range(size):
            grid[r][c] = 0
    result = count_islands(grid)
    assert result == (size + 1) // 2  # one island per remaining land row


def test_max_island_area_basic():
    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]
    assert max_island_area(grid) == 3


def test_max_island_area_no_land():
    assert max_island_area([[0, 0], [0, 0]]) == 0


def test_max_island_area_all_land():
    grid = [[1, 1], [1, 1]]
    assert max_island_area(grid) == 4


def test_max_island_area_picks_the_bigger_of_two():
    grid = [
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 0, 0, 1],
    ]
    # left island = 2 cells, right island = 5 cells
    assert max_island_area(grid) == 5
