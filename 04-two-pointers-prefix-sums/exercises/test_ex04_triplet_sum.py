from ex04_triplet_sum import three_sum_zero


def test_three_sum_zero_typical():
    result = three_sum_zero([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([(-1, -1, 2), (-1, 0, 1)])


def test_three_sum_zero_all_same_value():
    assert three_sum_zero([0, 0, 0]) == [(0, 0, 0)]


def test_three_sum_zero_no_triplet():
    assert three_sum_zero([1, 2, 3]) == []


def test_three_sum_zero_empty_list():
    assert three_sum_zero([]) == []


def test_three_sum_zero_fewer_than_three_elements():
    assert three_sum_zero([1, -1]) == []


def test_three_sum_zero_no_duplicate_triplets_from_repeats():
    result = three_sum_zero([-2, 0, 0, 2, 2])
    assert sorted(result) == sorted([(-2, 0, 2)])


def test_three_sum_zero_multiple_distinct_triplets():
    result = three_sum_zero([-4, -1, -1, 0, 1, 2])
    assert sorted(result) == sorted([(-1, -1, 2), (-1, 0, 1)])
