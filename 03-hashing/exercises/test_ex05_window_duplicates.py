from ex05_window_duplicates import first_repeated_within, has_nearby_duplicate


def test_has_nearby_duplicate_within_distance():
    assert has_nearby_duplicate([1, 2, 3, 1], 3) is True


def test_has_nearby_duplicate_too_far_apart():
    assert has_nearby_duplicate([1, 2, 3, 1], 2) is False


def test_has_nearby_duplicate_no_repeat_at_all():
    assert has_nearby_duplicate([1, 2, 3], 1) is False


def test_has_nearby_duplicate_empty_list():
    assert has_nearby_duplicate([], 5) is False


def test_has_nearby_duplicate_adjacent_equal_elements():
    assert has_nearby_duplicate([7, 7], 1) is True


def test_has_nearby_duplicate_k_zero_never_true():
    assert has_nearby_duplicate([1, 1], 0) is False


def test_has_nearby_duplicate_uses_closest_occurrence():
    # 9 appears at 0, 5, 6 -- indices 5 and 6 are within k=1 even though
    # 0 and 5 are not.
    assert has_nearby_duplicate([9, 1, 2, 3, 4, 9, 9], 1) is True


def test_first_repeated_within_typical():
    assert first_repeated_within([5, 6, 5, 7], 2) == 5


def test_first_repeated_within_too_far_apart():
    assert first_repeated_within([5, 6, 7, 5], 2) is None


def test_first_repeated_within_empty_stream():
    assert first_repeated_within([], 3) is None


def test_first_repeated_within_no_repeats():
    assert first_repeated_within([1, 2, 3, 4], 2) is None


def test_first_repeated_within_reports_earliest_detected():
    # 2 repeats at index 3 (distance 2), 1 repeats at index 4 (distance 4,
    # too far with k=2). The first VALID repeat detected while scanning
    # is the 2 at index 3.
    assert first_repeated_within([1, 2, 3, 2, 1], 2) == 2
