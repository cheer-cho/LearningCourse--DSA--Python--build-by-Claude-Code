from ex01_sorted_pair_target import pair_sum_sorted


def test_pair_sum_sorted_typical():
    assert pair_sum_sorted([2, 7, 11, 15], 9) == (0, 1)


def test_pair_sum_sorted_no_match():
    assert pair_sum_sorted([1, 2, 3], 100) is None


def test_pair_sum_sorted_negatives():
    assert pair_sum_sorted([-3, -1, 0, 2, 5], 2) == (0, 4)


def test_pair_sum_sorted_empty_list():
    assert pair_sum_sorted([], 5) is None


def test_pair_sum_sorted_single_element():
    assert pair_sum_sorted([5], 5) is None


def test_pair_sum_sorted_duplicates():
    assert pair_sum_sorted([1, 1, 1], 2) == (0, 2)


def test_pair_sum_sorted_match_at_ends():
    assert pair_sum_sorted([1, 2, 3, 4, 100], 101) == (0, 4)


def test_pair_sum_sorted_efficiency_on_large_sorted_input():
    n = 200_000
    nums = list(range(n))
    # nums[i] == i, so nums[l] + nums[r] == l + r. Only findable by
    # scanning toward the middle in O(n); a naive O(n^2) pair scan
    # would be far too slow at this size.
    assert pair_sum_sorted(nums, 300_000) == (100_001, 199_999)
