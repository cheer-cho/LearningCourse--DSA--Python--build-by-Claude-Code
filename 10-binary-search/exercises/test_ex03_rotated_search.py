from ex03_rotated_search import min_in_rotated, search_rotated


def test_min_in_rotated_typical_rotation():
    assert min_in_rotated([4, 5, 6, 7, 0, 1, 2]) == 0


def test_min_in_rotated_zero_rotation():
    assert min_in_rotated([1, 2, 3, 4, 5]) == 1


def test_min_in_rotated_two_elements():
    assert min_in_rotated([2, 1]) == 1


def test_min_in_rotated_single_element():
    assert min_in_rotated([9]) == 9


def test_min_in_rotated_rotation_by_one():
    assert min_in_rotated([2, 3, 4, 5, 1]) == 1


def test_min_in_rotated_large_rotation_is_fast():
    n = 200_000
    pivot = 137_842
    nums = list(range(pivot, n)) + list(range(pivot))
    assert min_in_rotated(nums) == 0


def test_search_rotated_target_in_right_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_search_rotated_target_in_left_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_search_rotated_target_missing():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_search_rotated_zero_rotation():
    assert search_rotated([1, 2, 3, 4, 5], 5) == 4


def test_search_rotated_single_element_hit():
    assert search_rotated([1], 1) == 0


def test_search_rotated_single_element_miss():
    assert search_rotated([1], 0) == -1


def test_search_rotated_two_elements():
    assert search_rotated([3, 1], 1) == 1
    assert search_rotated([3, 1], 3) == 0


def test_search_rotated_large_array_is_fast():
    n = 200_000
    pivot = 61_337
    nums = list(range(pivot, n)) + list(range(pivot))
    assert search_rotated(nums, 5) == n - pivot + 5
    assert search_rotated(nums, -1) == -1
