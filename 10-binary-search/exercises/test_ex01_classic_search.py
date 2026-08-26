from ex01_classic_search import binary_search, count_occurrences


def test_binary_search_finds_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_finds_first_and_last():
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 9) == 4


def test_binary_search_missing_returns_minus_one():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_empty_array():
    assert binary_search([], 4) == -1


def test_binary_search_single_element_hit_and_miss():
    assert binary_search([42], 42) == 0
    assert binary_search([42], 1) == -1


def test_binary_search_target_below_and_above_range():
    nums = [10, 20, 30]
    assert binary_search(nums, 0) == -1
    assert binary_search(nums, 100) == -1


def test_binary_search_with_duplicates_returns_a_valid_index():
    nums = [2, 2, 2, 2]
    idx = binary_search(nums, 2)
    assert 0 <= idx < len(nums)
    assert nums[idx] == 2


def test_binary_search_large_sorted_array_is_fast():
    nums = list(range(0, 2_000_000, 2))  # 1_000_000 even numbers
    assert binary_search(nums, 1_999_998) == 999_999
    assert binary_search(nums, 1_999_999) == -1


def test_count_occurrences_typical():
    assert count_occurrences([1, 2, 2, 2, 3, 4], 2) == 3


def test_count_occurrences_not_present():
    assert count_occurrences([1, 2, 2, 2, 3, 4], 5) == 0


def test_count_occurrences_empty_array():
    assert count_occurrences([], 1) == 0


def test_count_occurrences_all_equal():
    assert count_occurrences([7, 7, 7, 7, 7], 7) == 5


def test_count_occurrences_single_occurrence():
    assert count_occurrences([1, 2, 3, 4], 3) == 1


def test_count_occurrences_target_below_and_above_range():
    nums = [5, 5, 6, 7, 7, 7]
    assert count_occurrences(nums, 1) == 0
    assert count_occurrences(nums, 100) == 0


def test_count_occurrences_large_array_is_fast():
    nums = sorted([i % 1000 for i in range(1_000_000)])
    assert count_occurrences(nums, 500) == 1000
