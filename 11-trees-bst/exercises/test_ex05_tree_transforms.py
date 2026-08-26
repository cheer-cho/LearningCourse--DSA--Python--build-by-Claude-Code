from ex01_build_bst import tree_from_level_array, tree_to_level_array
from ex05_tree_transforms import invert, is_same_tree, is_subtree, is_symmetric


def test_invert_typical():
    root = tree_from_level_array([1, 2, 3])
    result = invert(root)
    assert tree_to_level_array(result) == [1, 3, 2]


def test_invert_deeper_tree():
    root = tree_from_level_array([4, 2, 7, 1, 3, 6, 9])
    result = invert(root)
    assert tree_to_level_array(result) == [4, 7, 2, 9, 6, 3, 1]


def test_invert_empty():
    assert invert(None) is None


def test_invert_single_node():
    root = tree_from_level_array([1])
    assert tree_to_level_array(invert(root)) == [1]


def test_is_same_tree_identical():
    a = tree_from_level_array([1, 2, 3])
    b = tree_from_level_array([1, 2, 3])
    assert is_same_tree(a, b) is True


def test_is_same_tree_different_shape():
    a = tree_from_level_array([1, 2])
    b = tree_from_level_array([1, None, 2])
    assert is_same_tree(a, b) is False


def test_is_same_tree_different_values():
    a = tree_from_level_array([1, 2, 3])
    b = tree_from_level_array([1, 2, 4])
    assert is_same_tree(a, b) is False


def test_is_same_tree_both_empty():
    assert is_same_tree(None, None) is True


def test_is_subtree_true():
    root = tree_from_level_array([3, 4, 5, 1, 2])
    sub = tree_from_level_array([4, 1, 2])
    assert is_subtree(root, sub) is True


def test_is_subtree_false_partial_match():
    # sub's shape doesn't match exactly (that node has an extra descendant)
    root = tree_from_level_array([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub = tree_from_level_array([4, 1, 2])
    assert is_subtree(root, sub) is False


def test_is_subtree_empty_sub_is_always_true():
    root = tree_from_level_array([3, 4, 5])
    assert is_subtree(root, None) is True


def test_is_subtree_empty_root_nonempty_sub():
    assert is_subtree(None, tree_from_level_array([1])) is False


def test_is_symmetric_true():
    root = tree_from_level_array([1, 2, 2, 3, 4, 4, 3])
    assert is_symmetric(root) is True


def test_is_symmetric_false():
    root = tree_from_level_array([1, 2, 2, None, 3, None, 3])
    assert is_symmetric(root) is False


def test_is_symmetric_empty():
    assert is_symmetric(None) is True


def test_is_symmetric_single_node():
    assert is_symmetric(tree_from_level_array([1])) is True
