from ex02_boundaries import insert_position, lower_bound, upper_bound


def test_lower_bound_at_first_duplicate():
    assert lower_bound([1, 3, 3, 3, 5], 3) == 1


def test_lower_bound_value_absent_falls_between():
    assert lower_bound([1, 3, 3, 3, 5], 4) == 4


def test_lower_bound_value_below_everything():
    assert lower_bound([1, 3, 3, 3, 5], 0) == 0


def test_lower_bound_value_above_everything():
    assert lower_bound([1, 3, 3, 3, 5], 9) == 5


def test_lower_bound_empty_array():
    assert lower_bound([], 5) == 0


def test_lower_bound_all_equal_array():
    assert lower_bound([4, 4, 4, 4], 4) == 0


def test_upper_bound_after_last_duplicate():
    assert upper_bound([1, 3, 3, 3, 5], 3) == 4


def test_upper_bound_value_absent_falls_between():
    assert upper_bound([1, 3, 3, 3, 5], 4) == 4


def test_upper_bound_value_below_everything():
    assert upper_bound([1, 3, 3, 3, 5], 0) == 0


def test_upper_bound_value_above_everything():
    assert upper_bound([1, 3, 3, 3, 5], 9) == 5


def test_upper_bound_empty_array():
    assert upper_bound([], 5) == 0


def test_upper_bound_all_equal_array():
    assert upper_bound([4, 4, 4, 4], 4) == 4


def test_insert_position_existing_value_goes_leftmost():
    assert insert_position([1, 3, 5, 5, 7], 5) == 2


def test_insert_position_between_values():
    assert insert_position([1, 3, 5, 7], 6) == 3


def test_insert_position_before_first():
    assert insert_position([1, 3, 5, 7], 0) == 0


def test_insert_position_after_last():
    assert insert_position([1, 3, 5, 7], 100) == 4


def test_insert_position_empty_array():
    assert insert_position([], 4) == 0


def test_boundaries_agree_on_large_array():
    nums = sorted(i // 3 for i in range(300_000))  # each value repeats 3x
    assert lower_bound(nums, 50_000) == 150_000
    assert upper_bound(nums, 50_000) == 150_003
