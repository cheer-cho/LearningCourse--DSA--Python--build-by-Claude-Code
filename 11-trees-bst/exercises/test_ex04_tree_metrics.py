import time

from ex01_build_bst import TreeNode, tree_from_level_array
from ex04_tree_metrics import count_nodes, diameter, is_balanced, max_depth


def _build_perfect_tree(depth: int) -> TreeNode | None:
    """A complete/perfect binary tree of the given depth (every level full,
    every subtree's height exactly matches its sibling's)."""
    if depth == 0:
        return None
    node = TreeNode(0)
    node.left = _build_perfect_tree(depth - 1)
    node.right = _build_perfect_tree(depth - 1)
    return node


def _build_hidden_imbalance_tree(depth: int) -> TreeNode:
    # A fully-skewed chain looks like the obvious "worst case" for a
    # naive top-down is_balanced, but it isn't: the root's own height
    # check sees the huge left/right height gap immediately and returns
    # False after a single O(n) pass -- no repeated work ever happens.
    #
    # This tree is the opposite shape: a perfect tree, so every node's
    # two children have exactly matching heights and the local
    # diff-check passes all the way down -- except at ONE node, deep on
    # the rightmost path, whose right child is pruned away entirely.
    # That node's OWN height is unchanged (still governed by its left
    # child, which still reaches full depth), so every ancestor above it
    # sees a perfectly matched pair of heights and keeps recursing: the
    # imbalance is invisible until you are standing right on top of it.
    # A naive solution that recomputes height() from scratch at every
    # node has to fully re-walk most of the tree (real, repeated O(n)
    # work at nearly every level -> O(n log n) total) before it ever
    # reaches that one node. The O(n) bottom-up solution finds it in a
    # single pass.
    root = _build_perfect_tree(depth)
    node = root
    for _ in range(depth - 3):
        node = node.right
    node.right = None
    return root


def test_max_depth_typical():
    assert max_depth(tree_from_level_array([1, 2, 3, 4])) == 3


def test_max_depth_empty():
    assert max_depth(None) == 0


def test_max_depth_single_node():
    assert max_depth(tree_from_level_array([1])) == 1


def test_count_nodes_typical():
    assert count_nodes(tree_from_level_array([1, 2, 3, 4, 5])) == 5


def test_count_nodes_empty():
    assert count_nodes(None) == 0


def test_count_nodes_single_node():
    assert count_nodes(tree_from_level_array([1])) == 1


def test_is_balanced_true_for_balanced_tree():
    assert is_balanced(tree_from_level_array([1, 2, 3, 4, 5, 6, 7])) is True


def test_is_balanced_false_for_lopsided_tree():
    root = tree_from_level_array([1, 2, None, 3, None, 4])
    assert is_balanced(root) is False


def test_is_balanced_empty_tree():
    assert is_balanced(None) is True


def test_is_balanced_single_node():
    assert is_balanced(tree_from_level_array([1])) is True


def test_is_balanced_survives_large_hidden_imbalance():
    # See _build_hidden_imbalance_tree: a perfect (shallow-looking)
    # tree of depth 21 (~2M nodes) whose one true imbalance is buried on
    # the rightmost path, undetectable from any ancestor above it. A
    # naive top-down solution (recompute height() from scratch at every
    # node) has to redo real work at nearly every level before reaching
    # it -- measured at >1s locally. A bottom-up single pass (the O(n)
    # target) finds it in ~0.1-0.2s. Recursion only goes 21 deep here,
    # so no recursion-limit bump is needed.
    root = _build_hidden_imbalance_tree(21)
    start = time.perf_counter()
    result = is_balanced(root)
    elapsed = time.perf_counter() - start
    assert result is False
    assert elapsed < 1.0  # generous ceiling -- the O(n) target is comfortably under this


def test_diameter_straight_line():
    root = tree_from_level_array([1, 2, None, 3])
    assert diameter(root) == 2


def test_diameter_through_root():
    root = tree_from_level_array([1, 2, 3, 4, 5])
    assert diameter(root) == 3


def test_diameter_not_through_root():
    # Longest path is 5-3-2-4 (3 edges), entirely below the root; the
    # root has no right child, so it can't be part of a path that
    # crosses from a right subtree to a left subtree.
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    assert diameter(root) == 3


def test_diameter_single_node():
    assert diameter(tree_from_level_array([1])) == 0


def test_diameter_empty():
    assert diameter(None) == 0
