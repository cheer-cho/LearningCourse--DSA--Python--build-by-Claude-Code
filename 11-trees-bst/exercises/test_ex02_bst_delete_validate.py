from ex01_build_bst import tree_from_level_array, tree_to_level_array
from ex02_bst_delete_validate import delete_value, is_valid_bst


def test_delete_leaf():
    root = tree_from_level_array([5, 3, 8])
    result = delete_value(root, 3)
    assert tree_to_level_array(result) == [5, None, 8]


def test_delete_node_with_one_child():
    root = tree_from_level_array([5, 3, 8, 2])
    result = delete_value(root, 3)
    assert tree_to_level_array(result) == [5, 2, 8]


def test_delete_node_with_two_children_uses_successor():
    root = tree_from_level_array([5, 3, 8, 2, 4])
    result = delete_value(root, 3)
    assert tree_to_level_array(result) == [5, 4, 8, 2]


def test_delete_root_with_two_children():
    root = tree_from_level_array([5, 3, 8])
    result = delete_value(root, 5)
    assert tree_to_level_array(result) == [8, 3]


def test_delete_missing_value_is_a_no_op():
    root = tree_from_level_array([5, 3, 8])
    result = delete_value(root, 100)
    assert tree_to_level_array(result) == [5, 3, 8]


def test_delete_from_empty_tree():
    assert delete_value(None, 5) is None


def test_delete_only_node():
    root = tree_from_level_array([5])
    assert delete_value(root, 5) is None


def test_is_valid_bst_true_for_valid_tree():
    assert is_valid_bst(tree_from_level_array([5, 1, 8])) is True


def test_is_valid_bst_catches_grandchild_violation():
    # 4 is a valid left child of 8, but 8 is 5's right child, so every
    # node under 8 must be > 5. 4 breaks that two levels up.
    root = tree_from_level_array([5, 1, 8, None, None, 4])
    assert is_valid_bst(root) is False


def test_is_valid_bst_single_node():
    assert is_valid_bst(tree_from_level_array([5])) is True


def test_is_valid_bst_empty_tree():
    assert is_valid_bst(None) is True


def test_is_valid_bst_rejects_duplicate_values():
    root = tree_from_level_array([5, 5])
    assert is_valid_bst(root) is False


def test_is_valid_bst_accepts_skewed_valid_tree():
    root = tree_from_level_array([5, None, 6, None, 7, None, 8])
    assert is_valid_bst(root) is True
