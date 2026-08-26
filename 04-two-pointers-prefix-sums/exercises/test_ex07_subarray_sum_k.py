from ex07_subarray_sum_k import count_subarrays_with_sum


def test_count_subarrays_with_sum_typical():
    assert count_subarrays_with_sum([1, 1, 1], 2) == 2


def test_count_subarrays_with_sum_disjoint_matches():
    assert count_subarrays_with_sum([1, 2, 3], 3) == 2


def test_count_subarrays_with_sum_with_negatives():
    assert count_subarrays_with_sum([1, -1, 0], 0) == 3


def test_count_subarrays_with_sum_empty_list():
    assert count_subarrays_with_sum([], 0) == 0


def test_count_subarrays_with_sum_no_match():
    assert count_subarrays_with_sum([1, 2, 3], 100) == 0


def test_count_subarrays_with_sum_negative_target():
    assert count_subarrays_with_sum([3, -2, -1, 4], -3) == 1


def test_count_subarrays_with_sum_whole_array_only():
    assert count_subarrays_with_sum([5], 5) == 1


def test_count_subarrays_with_sum_zeros_everywhere():
    assert count_subarrays_with_sum([0, 0, 0], 0) == 6


def test_count_subarrays_with_sum_efficiency_on_large_input():
    n = 200_000
    nums = [1] * n
    k = 5
    # A subarray of all 1s sums to k exactly when it has length k;
    # there are (n - k + 1) starting positions for such a subarray.
    # An O(n^2) brute-force scan of every subarray would be far too
    # slow at this size.
    assert count_subarrays_with_sum(nums, k) == n - k + 1
