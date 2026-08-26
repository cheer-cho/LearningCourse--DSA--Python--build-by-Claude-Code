from ex01_kadane_max_run import best_trades_unlimited, max_subarray_bounds, max_subarray_sum


def test_max_subarray_sum_typical():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_sum_all_negative_returns_least_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1


def test_max_subarray_sum_single_element():
    assert max_subarray_sum([5]) == 5


def test_max_subarray_sum_all_positive_is_full_array():
    assert max_subarray_sum([1, 2, 3, 4]) == 10


def test_max_subarray_sum_all_equal():
    assert max_subarray_sum([2, 2, 2, 2]) == 8


def test_max_subarray_sum_efficiency_large_input():
    n = 200_000
    nums = [-1] * n
    nums[100_000:100_100] = [5] * 100  # one obviously-best window
    assert max_subarray_sum(nums) == 500


def test_max_subarray_bounds_typical():
    result = max_subarray_bounds([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == (6, 3, 6)


def test_max_subarray_bounds_bounds_are_consistent_with_sum():
    nums = [1, -2, 3, 4, -1, 2]
    best, start, end = max_subarray_bounds(nums)
    assert sum(nums[start : end + 1]) == best


def test_max_subarray_bounds_single_element():
    assert max_subarray_bounds([5]) == (5, 0, 0)


def test_max_subarray_bounds_all_negative():
    best, start, end = max_subarray_bounds([-5, -1, -3])
    assert best == -1
    assert start == end == 1


def test_best_trades_unlimited_typical():
    assert best_trades_unlimited([7, 1, 5, 3, 6, 4]) == 7


def test_best_trades_unlimited_never_profitable():
    assert best_trades_unlimited([7, 6, 4, 3, 1]) == 0


def test_best_trades_unlimited_empty():
    assert best_trades_unlimited([]) == 0


def test_best_trades_unlimited_single_day():
    assert best_trades_unlimited([5]) == 0


def test_best_trades_unlimited_strictly_increasing():
    assert best_trades_unlimited([1, 2, 3, 4, 5]) == 4


def test_best_trades_unlimited_efficiency_large_input():
    n = 200_000
    prices = list(range(n))  # strictly increasing: every day is a gain
    assert best_trades_unlimited(prices) == n - 1
