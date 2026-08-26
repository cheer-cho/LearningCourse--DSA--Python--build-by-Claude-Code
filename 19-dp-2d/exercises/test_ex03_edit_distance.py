from ex03_edit_distance import edit_distance


def test_edit_distance_classic_horse_to_ros():
    assert edit_distance("horse", "ros") == 3


def test_edit_distance_intention_to_execution():
    assert edit_distance("intention", "execution") == 5


def test_edit_distance_from_empty_string():
    assert edit_distance("", "abc") == 3


def test_edit_distance_to_empty_string():
    assert edit_distance("abc", "") == 3


def test_edit_distance_identical_strings():
    assert edit_distance("abc", "abc") == 0


def test_edit_distance_both_empty():
    assert edit_distance("", "") == 0


def test_edit_distance_single_replace():
    assert edit_distance("a", "b") == 1


def test_edit_distance_is_symmetric():
    assert edit_distance("kitten", "sitting") == edit_distance("sitting", "kitten")
