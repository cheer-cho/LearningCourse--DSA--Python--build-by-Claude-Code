import pytest
from checkpoint_05 import (
    has_pattern_burst,
    longest_within_budget,
    shortest_breach,
    worst_minute,
)


def test_worst_minute_uniform_traffic():
    assert worst_minute([1] * 60) == 60


def test_worst_minute_finds_the_busiest_window():
    counts = [1] * 200
    counts[50:110] = [10] * 60  # one obviously-worst 60-second window
    assert worst_minute(counts) == 600


def test_worst_minute_rejects_too_short_a_log():
    with pytest.raises(ValueError):
        worst_minute([1] * 30)


def test_worst_minute_efficiency_large_input():
    n = 100_000
    counts = [1] * n
    counts[40_000:40_060] = [50] * 60
    assert worst_minute(counts) == 50 * 60


def test_longest_within_budget_typical():
    assert longest_within_budget([2, 1, 1, 4, 1], 4) == 3


def test_longest_within_budget_everything_too_expensive():
    assert longest_within_budget([5, 5, 5], 4) == 0


def test_longest_within_budget_empty_counts():
    assert longest_within_budget([], 10) == 0


def test_longest_within_budget_whole_log_fits():
    assert longest_within_budget([1, 1, 1, 1], 10) == 4


def test_longest_within_budget_efficiency_large_input():
    n = 100_000
    counts = [1] * n
    assert longest_within_budget(counts, n - 1) == n - 1


def test_longest_within_budget_negative_budget_never_satisfiable():
    assert longest_within_budget([0, 0, 0], -1) == 0


def test_shortest_breach_typical():
    assert shortest_breach([1, 2, 3, 4, 5], 11) == 3


def test_shortest_breach_never_reached():
    assert shortest_breach([1, 1, 1], 100) == 0


def test_shortest_breach_single_second_breaches():
    assert shortest_breach([50], 10) == 1


def test_shortest_breach_efficiency_large_input():
    n = 100_000
    counts = [1] * n
    assert shortest_breach(counts, n - 1) == n - 1


def test_shortest_breach_zero_threshold_any_single_second_breaches():
    assert shortest_breach([5, 5, 5], 0) == 1


def test_has_pattern_burst_found_reordered():
    assert has_pattern_burst([1, 5, 2, 9, 2, 5], [5, 2, 9]) is True


def test_has_pattern_burst_not_found():
    assert has_pattern_burst([1, 2, 3], [4, 5]) is False


def test_has_pattern_burst_pattern_longer_than_counts():
    assert has_pattern_burst([1, 2], [1, 2, 3]) is False


def test_has_pattern_burst_finds_a_permuted_window():
    assert has_pattern_burst([1, 1, 2], [1, 2]) is True


def test_has_pattern_burst_respects_multiplicity():
    assert has_pattern_burst([1, 1, 2, 1], [1, 1, 2]) is True
    assert has_pattern_burst([1, 2, 2, 1], [1, 1, 2]) is False


def test_has_pattern_burst_efficiency_large_input():
    n = 100_000
    counts = [0] * n
    pattern = [7, 3, 9, 1, 5] * 200  # length 1000
    counts[60_000 : 60_000 + len(pattern)] = pattern[::-1]
    assert has_pattern_burst(counts, pattern) is True
