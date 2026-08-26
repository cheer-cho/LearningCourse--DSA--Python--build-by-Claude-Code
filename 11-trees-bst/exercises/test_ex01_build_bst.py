import pytest
from ex01_build_bst import BST, tree_from_level_array, tree_to_level_array


def test_tree_from_level_array_empty():
    assert tree_from_level_array([]) is None


def test_tree_from_level_array_simple():
    root = tree_from_level_array([1, 2, 3])
    assert root.value == 1
    assert root.left.value == 2
    assert root.right.value == 3


def test_tree_from_level_array_with_gaps():
    root = tree_from_level_array([1, 2, None, 3])
    assert root.left.value == 2
    assert root.left.left.value == 3
    assert root.left.right is None
    assert root.right is None


def test_tree_from_level_array_single_node():
    root = tree_from_level_array([7])
    assert root.value == 7
    assert root.left is None
    assert root.right is None


def test_tree_to_level_array_empty():
    assert tree_to_level_array(None) == []


def test_tree_to_level_array_simple():
    root = tree_from_level_array([1, 2, 3])
    assert tree_to_level_array(root) == [1, 2, 3]


def test_tree_to_level_array_trims_trailing_none():
    root = tree_from_level_array([1, 2, None, 3])
    assert tree_to_level_array(root) == [1, 2, None, 3]


def test_round_trip_single_node():
    assert tree_to_level_array(tree_from_level_array([5])) == [5]


def test_bst_insert_and_contains():
    bst = BST()
    for v in [5, 3, 8, 1, 4]:
        bst.insert(v)
    assert bst.contains(4)
    assert not bst.contains(100)


def test_bst_insert_ignores_duplicates():
    bst = BST()
    bst.insert(5)
    bst.insert(5)
    assert bst.to_sorted_array() == [5]


def test_bst_contains_empty_tree():
    bst = BST()
    assert not bst.contains(1)


def test_bst_min_max():
    bst = BST()
    for v in [5, 3, 8, 1, 9]:
        bst.insert(v)
    assert bst.min_value() == 1
    assert bst.max_value() == 9


def test_bst_min_on_empty_raises():
    bst = BST()
    with pytest.raises(ValueError):
        bst.min_value()


def test_bst_max_on_empty_raises():
    bst = BST()
    with pytest.raises(ValueError):
        bst.max_value()


def test_bst_to_sorted_array():
    bst = BST()
    for v in [5, 3, 8, 1, 4, 9, 7]:
        bst.insert(v)
    assert bst.to_sorted_array() == [1, 3, 4, 5, 7, 8, 9]


def test_bst_to_sorted_array_empty():
    bst = BST()
    assert bst.to_sorted_array() == []
