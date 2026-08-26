from checkpoint_18 import (
    longest_growth_streak,
    max_earnings,
    min_gear_cost,
    ways_to_fill,
)


def sawtooth(block_size: int, num_blocks: int) -> list[int]:
    """[1..block_size] repeated `num_blocks` times -- same helper shape
    as ex07's, reused here so the LIS efficiency test stays exact."""
    return list(range(1, block_size + 1)) * num_blocks


# --- max_earnings: house-robber shape ---


def test_max_earnings_empty():
    assert max_earnings([]) == 0


def test_max_earnings_single_day():
    assert max_earnings([50]) == 50


def test_max_earnings_classic_example():
    assert max_earnings([30, 200, 40, 90]) == 290


def test_max_earnings_adjacent_days_conflict():
    assert max_earnings([5, 5]) == 5


def test_max_earnings_does_not_mutate_input():
    day_pay = [30, 200, 40, 90]
    max_earnings(day_pay)
    assert day_pay == [30, 200, 40, 90]


def test_max_earnings_efficiency_large_input():
    n = 100_000
    day_pay = [(i * 37) % 101 for i in range(n)]
    result = max_earnings(day_pay)
    assert isinstance(result, int)
    assert result > 0


# --- min_gear_cost: min-cost-climb shape ---


def test_min_gear_cost_typical():
    assert min_gear_cost([10, 15, 20]) == 15


def test_min_gear_cost_both_free():
    assert min_gear_cost([0, 0]) == 0


def test_min_gear_cost_empty_calendar():
    assert min_gear_cost([]) == 0


def test_min_gear_cost_single_day_free_to_start():
    assert min_gear_cost([100]) == 0


def test_min_gear_cost_can_hop_over_expensive_middle_day():
    assert min_gear_cost([0, 5, 0]) == 0


# --- ways_to_fill: order-matters coin-change-count shape ---


def test_ways_to_fill_zero_days_is_one_way():
    assert ways_to_fill(0, [1, 2]) == 1


def test_ways_to_fill_classic_fib_shape():
    assert ways_to_fill(3, [1, 2]) == 3


def test_ways_to_fill_three_block_sizes():
    assert ways_to_fill(4, [1, 2, 3]) == 7


def test_ways_to_fill_single_exact_block():
    assert ways_to_fill(5, [5]) == 1


def test_ways_to_fill_block_too_large_has_no_way():
    assert ways_to_fill(3, [5]) == 0


def test_ways_to_fill_order_matters_more_than_a_combinations_count():
    # With block sizes {1, 2}, filling 4 days has 5 orderings (Fibonacci
    # shape), not the smaller count a combinations-only count would give.
    assert ways_to_fill(4, [1, 2]) == 5


# --- longest_growth_streak: LIS shape ---


def test_longest_growth_streak_empty():
    assert longest_growth_streak([]) == 0


def test_longest_growth_streak_single_month():
    assert longest_growth_streak([42]) == 1


def test_longest_growth_streak_classic_example():
    assert longest_growth_streak([3, 1, 4, 1, 5, 9, 2, 6]) == 4


def test_longest_growth_streak_all_declining():
    assert longest_growth_streak([9, 8, 7]) == 1


def test_longest_growth_streak_all_equal_never_grows():
    assert longest_growth_streak([4, 4, 4, 4]) == 1


def test_longest_growth_streak_efficiency_large_input():
    # n = 100_000: an O(n^2) approach (10^10 comparisons) is infeasible
    # here -- only an O(n log n) implementation finishes in time. The
    # sawtooth pattern keeps the answer exact and non-trivial.
    revenues = sawtooth(block_size=200, num_blocks=500)
    assert len(revenues) == 100_000
    assert longest_growth_streak(revenues) == 200
