from ex05_infection_spread import minutes_to_infect, shortest_exit


def test_minutes_to_infect_basic():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    assert minutes_to_infect(grid) == 4


def test_minutes_to_infect_blocked_by_empty_relay():
    grid = [
        [2, 1],
        [0, 1],
    ]
    assert minutes_to_infect(grid) == 2


def test_minutes_to_infect_unreachable_returns_minus_one():
    grid = [[2, 0, 1]]
    assert minutes_to_infect(grid) == -1


def test_minutes_to_infect_no_healthy_servers():
    assert minutes_to_infect([[0, 0], [0, 0]]) == 0


def test_minutes_to_infect_healthy_with_no_source_is_unreachable():
    grid = [[1, 0], [0, 0]]
    assert minutes_to_infect(grid) == -1


def test_minutes_to_infect_multi_source_spreads_simultaneously():
    # two sources on opposite ends meet in the middle -> faster than
    # either source alone would achieve
    grid = [[2, 1, 1, 1, 2]]
    assert minutes_to_infect(grid) == 2


def test_minutes_to_infect_all_already_infected():
    assert minutes_to_infect([[2, 2], [2, 2]]) == 0


def test_shortest_exit_walled_in_returns_minus_one():
    maze = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ]
    assert shortest_exit(maze, (1, 1)) == -1


def test_shortest_exit_one_move_to_border():
    maze = [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ]
    assert shortest_exit(maze, (1, 1)) == 1


def test_shortest_exit_start_already_on_border():
    assert shortest_exit([[0]], (0, 0)) == 0


def test_shortest_exit_start_on_border_of_larger_maze():
    maze = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert shortest_exit(maze, (0, 0)) == 0


def test_shortest_exit_picks_shortest_of_multiple_paths():
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    # open corridor straight up from (2,1) to the border at (0,1): 2 moves
    assert shortest_exit(maze, (2, 1)) == 2
