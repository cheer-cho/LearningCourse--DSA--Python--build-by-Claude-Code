import pytest
from ex04_amortized_append import append_costs, total_cost


def test_append_costs_empty():
    assert append_costs(0) == []


def test_append_costs_single_append():
    assert append_costs(1) == [1]


def test_append_costs_known_sequence():
    assert append_costs(4) == [1, 2, 3, 1]


def test_append_costs_longer_known_sequence():
    assert append_costs(9) == [1, 2, 3, 1, 5, 1, 1, 1, 9]


def test_append_costs_length_matches_n():
    assert len(append_costs(37)) == 37


def test_append_costs_resize_cost_equals_size_before_resize_plus_one():
    costs = append_costs(5)
    # Resizes happen when size == capacity (capacities: 1, 2, 4, 8, ...).
    assert costs[1] == 2  # size was 1 when capacity doubled to 2
    assert costs[2] == 3  # size was 2 when capacity doubled to 4


def test_total_cost_matches_sum_of_append_costs():
    assert total_cost(9) == sum(append_costs(9))


def test_total_cost_zero():
    assert total_cost(0) == 0


@pytest.mark.parametrize("n", [1, 2, 5, 10, 100, 1_000, 100_000])
def test_total_cost_stays_within_the_amortized_bound(n):
    assert total_cost(n) <= 3 * n
