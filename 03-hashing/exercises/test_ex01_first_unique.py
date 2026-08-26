from ex01_first_unique import first_unique_index, majority_item


def test_first_unique_index_typical():
    assert first_unique_index("swiss") == 1


def test_first_unique_index_unique_is_later():
    assert first_unique_index("aabbc") == 4


def test_first_unique_index_all_repeat():
    assert first_unique_index("aabb") == -1


def test_first_unique_index_empty_string():
    assert first_unique_index("") == -1


def test_first_unique_index_single_character():
    assert first_unique_index("z") == 0


def test_first_unique_index_all_unique_picks_first():
    assert first_unique_index("abcdef") == 0


def test_majority_item_typical():
    assert majority_item([2, 2, 1, 2, 3]) == 2


def test_majority_item_single_element():
    assert majority_item([7]) == 7


def test_majority_item_all_same():
    assert majority_item([4, 4, 4, 4]) == 4


def test_majority_item_negative_numbers():
    assert majority_item([-1, -1, -1, 2, 3]) == -1


def test_majority_item_majority_at_end():
    assert majority_item([1, 2, 3, 3, 3, 3, 3]) == 3
