from ex06_target_sum_ways import ways_to_target


def test_ways_to_target_classic_example():
    assert ways_to_target([1, 1, 1, 1, 1], 3) == 5


def test_ways_to_target_with_a_zero():
    assert ways_to_target([1, 0], 1) == 2


def test_ways_to_target_all_zeros():
    assert ways_to_target([0, 0, 0], 0) == 8


def test_ways_to_target_unreachable_target():
    assert ways_to_target([1], 2) == 0


def test_ways_to_target_negative_target_is_symmetric():
    assert ways_to_target([1, 1, 1, 1, 1], -3) == ways_to_target([1, 1, 1, 1, 1], 3)


def test_ways_to_target_odd_combined_sum_is_impossible():
    assert ways_to_target([1, 2], 0) == 0


def test_ways_to_target_single_number_matches_target():
    assert ways_to_target([5], 5) == 1
    assert ways_to_target([5], -5) == 1


def test_ways_to_target_empty_nums_zero_target():
    assert ways_to_target([], 0) == 1
