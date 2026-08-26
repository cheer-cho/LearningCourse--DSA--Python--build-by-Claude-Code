from ex01_build_bst import tree_from_level_array
from ex03_traversals import inorder, inorder_iterative, level_order, postorder, preorder


def test_preorder_typical():
    root = tree_from_level_array([1, 2, 3, 4, 5])
    assert preorder(root) == [1, 2, 4, 5, 3]


def test_preorder_empty():
    assert preorder(None) == []


def test_preorder_single_node():
    assert preorder(tree_from_level_array([1])) == [1]


def test_inorder_typical():
    root = tree_from_level_array([2, 1, 3])
    assert inorder(root) == [1, 2, 3]


def test_inorder_empty():
    assert inorder(None) == []


def test_postorder_typical():
    root = tree_from_level_array([1, 2, 3])
    assert postorder(root) == [2, 3, 1]


def test_postorder_empty():
    assert postorder(None) == []


def test_inorder_iterative_matches_recursive():
    root = tree_from_level_array([5, 3, 8, 1, 4, 7, 9])
    assert inorder_iterative(root) == inorder(root) == [1, 3, 4, 5, 7, 8, 9]


def test_inorder_iterative_empty():
    assert inorder_iterative(None) == []


def test_inorder_iterative_single_node():
    assert inorder_iterative(tree_from_level_array([1])) == [1]


def test_inorder_iterative_left_skewed():
    root = tree_from_level_array([3, 2, None, 1])
    assert inorder_iterative(root) == [1, 2, 3]


def test_level_order_typical():
    root = tree_from_level_array([1, 2, 3, 4])
    assert level_order(root) == [[1], [2, 3], [4]]


def test_level_order_empty():
    assert level_order(None) == []


def test_level_order_single_node():
    assert level_order(tree_from_level_array([1])) == [[1]]
