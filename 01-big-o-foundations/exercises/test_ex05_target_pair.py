from ex05_target_pair import has_pair_brute, has_pair_fast


def test_has_pair_brute_finds_a_pair():
    assert has_pair_brute([2, 7, 11, 15], 9) is True


def test_has_pair_brute_no_pair_exists():
    assert has_pair_brute([1, 2, 3], 100) is False


def test_has_pair_brute_duplicate_values_at_different_positions_count():
    assert has_pair_brute([3, 3], 6) is True


def test_has_pair_brute_single_element_cannot_pair_with_itself():
    assert has_pair_brute([5], 10) is False


def test_has_pair_brute_empty_list():
    assert has_pair_brute([], 0) is False


def test_has_pair_brute_negative_numbers_and_zero_target():
    assert has_pair_brute([-3, 4, 1, -1], 0) is True


def test_has_pair_fast_finds_a_pair():
    assert has_pair_fast([2, 7, 11, 15], 9) is True


def test_has_pair_fast_no_pair_exists():
    assert has_pair_fast([1, 2, 3], 100) is False


def test_has_pair_fast_duplicate_values_at_different_positions_count():
    assert has_pair_fast([3, 3], 6) is True


def test_has_pair_fast_single_element_cannot_pair_with_itself():
    assert has_pair_fast([5], 10) is False


def test_has_pair_fast_empty_list():
    assert has_pair_fast([], 0) is False


def test_has_pair_fast_negative_numbers_and_zero_target():
    assert has_pair_fast([-3, 4, 1, -1], 0) is True


def test_has_pair_fast_large_input_is_fast():
    nums = list(range(200_000))
    assert has_pair_fast(nums, 399_997) is True  # 199998 + 199999
    assert has_pair_fast(nums, 999_999) is False  # unreachable, forces a full scan
