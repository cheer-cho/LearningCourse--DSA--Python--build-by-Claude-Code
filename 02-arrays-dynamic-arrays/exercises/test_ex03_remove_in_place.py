from ex03_remove_in_place import dedupe_sorted, remove_value


def test_remove_value_typical_packs_survivors_in_order():
    nums = [3, 2, 3, 5]
    new_len = remove_value(nums, 3)
    assert new_len == 2
    assert nums[:new_len] == [2, 5]


def test_remove_value_all_match_leaves_empty():
    nums = [1, 1, 1]
    assert remove_value(nums, 1) == 0


def test_remove_value_none_match_keeps_all_in_order():
    nums = [4, 5, 6]
    new_len = remove_value(nums, 9)
    assert new_len == 3
    assert nums[:new_len] == [4, 5, 6]


def test_remove_value_empty_list():
    nums: list[int] = []
    assert remove_value(nums, 9) == 0


def test_remove_value_single_matching_element():
    nums = [7]
    assert remove_value(nums, 7) == 0


def test_remove_value_single_non_matching_element():
    nums = [7]
    new_len = remove_value(nums, 8)
    assert new_len == 1
    assert nums[:new_len] == [7]


def test_dedupe_sorted_typical():
    nums = [1, 1, 2, 2, 3]
    new_len = dedupe_sorted(nums)
    assert new_len == 3
    assert nums[:new_len] == [1, 2, 3]


def test_dedupe_sorted_no_duplicates():
    nums = [1, 2, 3]
    new_len = dedupe_sorted(nums)
    assert new_len == 3
    assert nums[:new_len] == [1, 2, 3]


def test_dedupe_sorted_all_equal():
    nums = [4, 4, 4, 4]
    new_len = dedupe_sorted(nums)
    assert new_len == 1
    assert nums[:new_len] == [4]


def test_dedupe_sorted_empty_list():
    nums: list[int] = []
    assert dedupe_sorted(nums) == 0


def test_dedupe_sorted_single_element():
    nums = [5]
    new_len = dedupe_sorted(nums)
    assert new_len == 1
    assert nums[:new_len] == [5]


def test_dedupe_sorted_negatives_and_duplicates():
    nums = [-3, -3, -1, 0, 0, 0, 2]
    new_len = dedupe_sorted(nums)
    assert new_len == 4
    assert nums[:new_len] == [-3, -1, 0, 2]
