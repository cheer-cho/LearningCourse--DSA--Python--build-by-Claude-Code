import math

from ex04_rate_on_answer import min_rate


def test_min_rate_typical():
    assert min_rate([3, 6, 7, 11], 8) == 4


def test_min_rate_tight_deadline_forces_max_pile():
    assert min_rate([30, 11, 23, 4, 20], 5) == 30


def test_min_rate_generous_deadline():
    assert min_rate([30, 11, 23, 4, 20], 6) == 23


def test_min_rate_all_ones():
    assert min_rate([1, 1, 1], 3) == 1


def test_min_rate_single_pile():
    assert min_rate([10], 3) == 4  # ceil(10/4) = 3 <= 3, ceil(10/3) = 4 > 3


def test_min_rate_h_equals_pile_count_forces_max_pile():
    piles = [5, 9, 2, 14, 7]
    assert min_rate(piles, len(piles)) == max(piles)


def test_min_rate_result_actually_meets_deadline():
    piles = [312, 88, 7, 421, 19, 5, 967, 44]
    h = 30
    rate = min_rate(piles, h)
    hours = sum(math.ceil(p / rate) for p in piles)
    hours_one_less = sum(math.ceil(p / (rate - 1)) for p in piles)
    assert hours <= h
    assert hours_one_less > h


def test_min_rate_large_piles_is_fast():
    piles = [10**9] * 500 + [1]
    h = 10**7
    rate = min_rate(piles, h)
    hours = sum(math.ceil(p / rate) for p in piles)
    assert hours <= h
