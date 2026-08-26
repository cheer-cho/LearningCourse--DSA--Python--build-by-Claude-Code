from ex04_knapsack_01 import can_partition_equal, max_value


def test_max_value_classic_example():
    assert max_value([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


def test_max_value_second_example():
    assert max_value([2, 3, 4], [3, 4, 5], 5) == 7


def test_max_value_no_items():
    assert max_value([], [], 10) == 0


def test_max_value_zero_capacity():
    assert max_value([1, 2, 3], [10, 20, 30], 0) == 0


def test_max_value_single_item_fits():
    assert max_value([5], [100], 5) == 100


def test_max_value_single_item_does_not_fit():
    assert max_value([10], [100], 5) == 0


def test_max_value_never_double_counts_an_item():
    # each item usable at most once -- capacity for two copies of item 0
    # is available, but only one copy legally exists.
    assert max_value([3], [10], 6) == 10


def test_can_partition_equal_classic_true():
    assert can_partition_equal([1, 5, 11, 5]) is True


def test_can_partition_equal_classic_false():
    assert can_partition_equal([1, 2, 3, 5]) is False


def test_can_partition_equal_two_equal_numbers():
    assert can_partition_equal([2, 2]) is True


def test_can_partition_equal_empty_is_vacuously_true():
    assert can_partition_equal([]) is True


def test_can_partition_equal_single_element_is_false():
    assert can_partition_equal([4]) is False


def test_can_partition_equal_efficiency_large_input():
    # 300 ones: brute-force subset enumeration (2**300) is impossible, but
    # the O(n * sum) subset-sum DP (sum = 300) finishes instantly.
    nums = [1] * 300
    assert can_partition_equal(nums) is True
