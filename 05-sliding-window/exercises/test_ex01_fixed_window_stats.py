import pytest
from ex01_fixed_window_stats import max_window_sum, moving_averages


def test_max_window_sum_typical():
    assert max_window_sum([2, 1, 5, 1, 3, 2], 3) == 9


def test_max_window_sum_k_equals_length():
    assert max_window_sum([4, -1, 2], 3) == 5


def test_max_window_sum_k_equals_one():
    assert max_window_sum([5, 9, 2, 7], 1) == 9


def test_max_window_sum_single_element():
    assert max_window_sum([5], 1) == 5


def test_max_window_sum_handles_negatives():
    assert max_window_sum([-2, -1, -5, -1], 2) == -3


def test_max_window_sum_rejects_k_too_large():
    with pytest.raises(ValueError):
        max_window_sum([1, 2], 3)


def test_max_window_sum_rejects_k_zero():
    with pytest.raises(ValueError):
        max_window_sum([1, 2, 3], 0)


def test_max_window_sum_efficiency_large_input():
    n, k = 200_000, 1000
    nums = [1] * n
    nums[150_000:150_000 + k] = [5] * k  # one obviously-best window
    assert max_window_sum(nums, k) == 5 * k


def test_moving_averages_typical():
    assert moving_averages([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_moving_averages_window_equals_length():
    assert moving_averages([5, 5, 5], 3) == [5.0]


def test_moving_averages_window_of_one():
    assert moving_averages([1, 2, 3], 1) == [1.0, 2.0, 3.0]


def test_moving_averages_result_length():
    result = moving_averages(list(range(10)), 4)
    assert len(result) == 10 - 4 + 1


def test_moving_averages_rejects_bad_k():
    with pytest.raises(ValueError):
        moving_averages([1, 2, 3], 5)


def test_moving_averages_efficiency_large_input():
    n, k = 200_000, 1000
    nums = list(range(n))
    result = moving_averages(nums, k)
    assert len(result) == n - k + 1
    assert result[0] == sum(range(k)) / k
