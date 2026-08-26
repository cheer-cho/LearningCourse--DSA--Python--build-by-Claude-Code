# Scenario: BST-specific shortcuts — none of these would be efficient on
# a plain (non-BST) tree, because they all lean on the ordering invariant
# to skip whole subtrees.
# Concepts: inorder traversal with an early stop, ordering-guided LCA
# walk, pruned range sum.
# Run: uv run pytest 11-trees-bst -k ex06

from __future__ import annotations

from ex01_build_bst import TreeNode


def kth_smallest(root: TreeNode | None, k: int) -> int:
    """Return the k-th smallest value (1-indexed) in a BST. Stop the
    inorder walk as soon as the k-th value is found instead of
    collecting the whole traversal. Raise ValueError if `k` is out of
    range for the tree.

    kth_smallest(tree_from_level_array([5, 3, 8, 1, 4]), 2) -> 3

    Target complexity: O(h + k) time, O(h) space
    """
    raise NotImplementedError


def lca_bst(root: TreeNode, a: int, b: int) -> int:
    """Return the value of the lowest common ancestor of `a` and `b` in
    a BST (both values are guaranteed present). Walk down from the
    root using the ordering: if both targets are smaller than the
    current node, go left; if both are larger, go right; otherwise
    you've found the split point — that node is the answer.

    lca_bst(tree_from_level_array([6, 2, 8, 0, 4, 7, 9]), 0, 4) -> 2

    Target complexity: O(h) time, O(1) space (iterative)
    """
    raise NotImplementedError


def range_sum_bst(root: TreeNode | None, lo: int, hi: int) -> int:
    """Sum every node value in the inclusive range [lo, hi].

    Prune: if a node's value is <= lo, its entire left subtree can
    only hold smaller values — skip it. Symmetrically for `hi` and the
    right subtree. This pruning is exactly why a BST beats a plain
    hash set for range queries: a hash set has no order to prune with.

    range_sum_bst(tree_from_level_array([10, 5, 15, 3, 7, None, 18]), 6, 15) -> 32

    Target complexity: O(h + k) time, O(h) space (k = nodes visited in range)
    """
    raise NotImplementedError
