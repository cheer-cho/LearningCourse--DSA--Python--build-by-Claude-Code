from ex01_build_bst import TreeNode, tree_from_level_array, tree_to_level_array
from ex08_construct_tree import build_from_pre_in


def test_build_from_pre_in_typical():
    root = build_from_pre_in([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_level_array(root) == [3, 9, 20, None, None, 15, 7]


def test_build_from_pre_in_empty():
    assert build_from_pre_in([], []) is None


def test_build_from_pre_in_single_node():
    root = build_from_pre_in([5], [5])
    assert tree_to_level_array(root) == [5]


def test_build_from_pre_in_left_skewed():
    root = build_from_pre_in([3, 2, 1], [1, 2, 3])
    assert tree_to_level_array(root) == [3, 2, None, 1]


def test_build_from_pre_in_right_skewed():
    root = build_from_pre_in([1, 2, 3], [1, 2, 3])
    assert tree_to_level_array(root) == [1, None, 2, None, 3]


def test_build_from_pre_in_matches_tree_from_level_array():
    original = tree_from_level_array([5, 3, 8, 1, 4, 7, 9])
    # Traversals of `original`, computed independently of ex03's functions.
    preorder = [5, 3, 1, 4, 8, 7, 9]
    inorder = [1, 3, 4, 5, 7, 8, 9]
    rebuilt = build_from_pre_in(preorder, inorder)
    assert tree_to_level_array(rebuilt) == tree_to_level_array(original)


def _inorder_values(node: TreeNode | None) -> list[int]:
    if node is None:
        return []
    return _inorder_values(node.left) + [node.value] + _inorder_values(node.right)


def _preorder_values(node: TreeNode | None) -> list[int]:
    if node is None:
        return []
    return [node.value] + _preorder_values(node.left) + _preorder_values(node.right)


def _build_balanced(values: list[int]) -> TreeNode | None:
    if not values:
        return None
    mid = len(values) // 2
    node = TreeNode(values[mid])
    node.left = _build_balanced(values[:mid])
    node.right = _build_balanced(values[mid + 1 :])
    return node


def test_build_from_pre_in_survives_large_balanced_tree():
    # `inorder.index(v)` is O(n) per call; called once per node, that's
    # O(n^2) regardless of tree shape. A precomputed index map keeps this
    # instant even at 10,000 nodes; a naive version is dramatically slower.
    n = 10_000
    original = _build_balanced(list(range(n)))
    preorder = _preorder_values(original)
    inorder = _inorder_values(original)

    rebuilt = build_from_pre_in(preorder, inorder)

    assert _inorder_values(rebuilt) == inorder
    assert _preorder_values(rebuilt) == preorder
