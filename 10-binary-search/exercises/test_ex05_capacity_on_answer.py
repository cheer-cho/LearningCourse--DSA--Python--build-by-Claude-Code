from ex05_capacity_on_answer import min_capacity, split_min_largest


def test_min_capacity_typical():
    assert min_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15


def test_min_capacity_second_example():
    assert min_capacity([3, 2, 2, 4, 1, 4], 3) == 6


def test_min_capacity_third_example():
    assert min_capacity([1, 2, 3, 1, 1], 4) == 3


def test_min_capacity_one_day_needs_full_sum():
    weights = [4, 8, 15, 16]
    assert min_capacity(weights, 1) == sum(weights)


def test_min_capacity_one_day_per_package_needs_heaviest():
    weights = [4, 8, 15, 16, 23, 42]
    assert min_capacity(weights, len(weights)) == max(weights)


def test_min_capacity_single_package():
    assert min_capacity([7], 1) == 7


def test_min_capacity_large_array_is_fast():
    weights = list(range(1, 100_001))
    cap = min_capacity(weights, 1000)
    assert cap >= max(weights)


def test_split_min_largest_typical():
    assert split_min_largest([7, 2, 5, 10, 8], 2) == 18


def test_split_min_largest_single_part_is_full_sum():
    nums = [1, 2, 3, 4, 5]
    assert split_min_largest(nums, 1) == sum(nums)


def test_split_min_largest_one_part_per_element():
    nums = [1, 4, 4]
    assert split_min_largest(nums, 3) == 4


def test_split_min_largest_k_equals_length_uses_max_element():
    nums = [10, 1, 1, 1, 1]
    assert split_min_largest(nums, len(nums)) == max(nums)


def test_split_min_largest_large_array_is_fast():
    nums = list(range(1, 50_001))
    largest = split_min_largest(nums, 100)
    assert largest >= max(nums)
    assert largest <= sum(nums)
