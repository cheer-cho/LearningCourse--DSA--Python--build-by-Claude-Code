from ex05_smallest_window_sum import shortest_subarray_at_least


def test_shortest_subarray_at_least_typical():
    assert shortest_subarray_at_least([2, 3, 1, 2, 4, 3], 7) == 2


def test_shortest_subarray_at_least_unreachable_target():
    assert shortest_subarray_at_least([1, 1, 1], 10) == 0


def test_shortest_subarray_at_least_single_element_meets_target():
    assert shortest_subarray_at_least([5], 5) == 1


def test_shortest_subarray_at_least_whole_array_needed():
    assert shortest_subarray_at_least([1, 1, 1, 1], 4) == 4


def test_shortest_subarray_at_least_empty_array():
    assert shortest_subarray_at_least([], 1) == 0


def test_shortest_subarray_at_least_target_met_by_first_element():
    assert shortest_subarray_at_least([1, 2, 3], 1) == 1


def test_shortest_subarray_at_least_efficiency_large_input():
    n = 200_000
    nums = [1] * n
    assert shortest_subarray_at_least(nums, n - 1) == n - 1
