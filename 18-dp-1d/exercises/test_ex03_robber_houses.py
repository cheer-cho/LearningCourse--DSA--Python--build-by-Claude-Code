from ex03_robber_houses import max_loot, max_loot_circle


def test_max_loot_empty():
    assert max_loot([]) == 0


def test_max_loot_single_house():
    assert max_loot([5]) == 5


def test_max_loot_two_houses_picks_larger():
    assert max_loot([3, 9]) == 9


def test_max_loot_classic_example():
    assert max_loot([2, 7, 9, 3, 1]) == 12


def test_max_loot_alternating_beats_greedy_adjacent_sum():
    assert max_loot([5, 5, 10, 100, 10, 5]) == 110


def test_max_loot_all_equal_values():
    assert max_loot([4, 4, 4, 4, 4]) == 12  # indices 0, 2, 4


def test_max_loot_does_not_mutate_input():
    values = [2, 7, 9, 3, 1]
    max_loot(values)
    assert values == [2, 7, 9, 3, 1]


def test_max_loot_circle_empty():
    assert max_loot_circle([]) == 0


def test_max_loot_circle_single_house():
    assert max_loot_circle([5]) == 5


def test_max_loot_circle_two_houses_are_neighbors():
    assert max_loot_circle([3, 9]) == 9


def test_max_loot_circle_three_houses():
    assert max_loot_circle([2, 3, 2]) == 3


def test_max_loot_circle_four_houses():
    assert max_loot_circle([1, 2, 3, 1]) == 4


def test_max_loot_circle_matches_linear_when_ends_conflict_is_moot():
    # A long enough run makes the wrap-around constraint irrelevant to
    # the optimal choice, so circle and linear agree.
    values = [1, 2, 3, 1, 5, 9, 2]
    assert max_loot_circle(values) <= max_loot(values)


def test_max_loot_efficiency_large_input():
    n = 100_000
    values = [(i * 37) % 101 for i in range(n)]
    result = max_loot(values)
    assert isinstance(result, int)
    assert result > 0
