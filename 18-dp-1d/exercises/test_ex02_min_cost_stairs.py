from ex02_min_cost_stairs import min_cost_climb


def test_two_steps_picks_cheaper_start():
    assert min_cost_climb([10, 15, 20]) == 15


def test_classic_ten_step_example():
    assert min_cost_climb([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_both_free():
    assert min_cost_climb([0, 0]) == 0


def test_single_expensive_middle_step_is_skippable():
    # A 2-step jump can hop clean over an expensive middle step.
    assert min_cost_climb([0, 5, 0]) == 0


def test_equal_costs_still_finds_minimum_path():
    assert min_cost_climb([3, 3, 3, 3]) == 6


def test_no_steps_costs_nothing():
    assert min_cost_climb([]) == 0


def test_efficiency_large_staircase():
    n = 50_000
    costs = [(i % 7) + 1 for i in range(n)]
    result = min_cost_climb(costs)
    assert isinstance(result, int)
    assert result > 0
