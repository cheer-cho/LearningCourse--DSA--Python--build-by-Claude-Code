import pytest
from ex03_fast_pow import power, power_mod


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def __call__(self) -> None:
        self.count += 1


def test_power_base_case_zero_exponent():
    assert power(5, 0) == 1


def test_power_typical():
    assert power(2, 10) == 1024


def test_power_exponent_one():
    assert power(7, 1) == 7


def test_power_negative_exponent():
    assert power(2, -2) == pytest.approx(0.25)


def test_power_negative_exponent_odd():
    assert power(2, -3) == pytest.approx(0.125)


def test_power_zero_base_positive_exponent():
    assert power(0, 5) == 0


def test_power_one_base_large_negative_exponent():
    assert power(1, -1000) == pytest.approx(1.0)


def test_power_call_count_is_logarithmic_for_power_of_two():
    counter = Counter()
    assert power(2, 1024, counter) == 2**1024
    # n halves each call: 1024 -> 512 -> ... -> 1 -> 0, i.e. 11 halvings
    # plus the base-case call itself.
    assert counter.count == 12


def test_power_call_count_stays_logarithmic_for_large_n():
    counter = Counter()
    power(1.0001, 10**9, counter)
    # log2(10**9) ~= 30; well under a linear scan of a billion calls.
    assert counter.count < 40


def test_power_mod_base_case():
    assert power_mod(7, 0, 5) == 1


def test_power_mod_typical():
    assert power_mod(2, 10, 1000) == 24


def test_power_mod_matches_naive_modulo():
    assert power_mod(3, 5, 7) == pow(3, 5) % 7


def test_power_mod_large_exponent_stays_fast_and_correct():
    counter = Counter()
    result = power_mod(123, 10**9, 1_000_000_007, counter)
    assert result == pow(123, 10**9, 1_000_000_007)
    assert counter.count < 40
