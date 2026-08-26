from ex01_build_bst import tree_from_level_array
from ex07_level_patterns import level_averages, right_side_view, zigzag_levels


def test_right_side_view_typical():
    root = tree_from_level_array([1, 2, 3, None, 5, None, 4])
    assert right_side_view(root) == [1, 3, 4]


def test_right_side_view_empty():
    assert right_side_view(None) == []


def test_right_side_view_left_only_branch():
    root = tree_from_level_array([1, 2, None, 3])
    assert right_side_view(root) == [1, 2, 3]


def test_right_side_view_single_node():
    assert right_side_view(tree_from_level_array([1])) == [1]


def test_level_averages_typical():
    root = tree_from_level_array([3, 9, 20, None, None, 15, 7])
    assert level_averages(root) == [3.0, 14.5, 11.0]


def test_level_averages_empty():
    assert level_averages(None) == []


def test_level_averages_single_node():
    assert level_averages(tree_from_level_array([5])) == [5.0]


def test_zigzag_levels_typical():
    root = tree_from_level_array([3, 9, 20, None, None, 15, 7])
    assert zigzag_levels(root) == [[3], [20, 9], [15, 7]]


def test_zigzag_levels_empty():
    assert zigzag_levels(None) == []


def test_zigzag_levels_single_node():
    assert zigzag_levels(tree_from_level_array([1])) == [[1]]


def test_zigzag_levels_four_levels_alternates_back_and_forth():
    root = tree_from_level_array([1, 2, 3, 4, 5, 6, 7, 8])
    assert zigzag_levels(root) == [[1], [3, 2], [4, 5, 6, 7], [8]]
