from ex05_knapsack_unbounded import count_coin_ways, max_ribbon_value


def test_count_coin_ways_classic_example():
    assert count_coin_ways([1, 2, 5], 5) == 4


def test_count_coin_ways_impossible_amount():
    assert count_coin_ways([2], 3) == 0


def test_count_coin_ways_zero_amount_is_one_way():
    assert count_coin_ways([10], 0) == 1


def test_count_coin_ways_no_coins_zero_amount():
    assert count_coin_ways([], 0) == 1


def test_count_coin_ways_no_coins_positive_amount():
    assert count_coin_ways([], 5) == 0


def test_count_coin_ways_counts_combinations_not_permutations():
    # [1, 1, 1], [1, 2] -- NOT [2, 1] counted separately.
    assert count_coin_ways([1, 2], 3) == 2


def test_count_coin_ways_efficiency_large_amount():
    assert count_coin_ways([1, 5, 10, 25], 1_000) > 0


def test_max_ribbon_value_classic_example():
    assert max_ribbon_value([1, 2, 3], [1, 5, 8], 4) == 10


def test_max_ribbon_value_zero_total():
    assert max_ribbon_value([1, 2], [5, 10], 0) == 0


def test_max_ribbon_value_no_lengths():
    assert max_ribbon_value([], [], 5) == 0


def test_max_ribbon_value_reuses_a_single_length():
    assert max_ribbon_value([1], [2], 5) == 10


def test_max_ribbon_value_leftover_length_goes_unused():
    assert max_ribbon_value([2], [5], 3) == 5


def test_max_ribbon_value_longer_piece_can_beat_many_short_ones():
    assert max_ribbon_value([1, 3], [2, 10], 3) == 10
