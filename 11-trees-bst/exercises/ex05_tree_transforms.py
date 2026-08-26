# Scenario: reshape and compare trees loaded from tree_from_level_array —
# mirror one, check if two trees match exactly, find one tree lurking
# inside another, check whether a tree mirrors itself.
# Concepts: recursive tree comparison, in-place mirroring, "is X inside Y"
# via is_same_tree tried at every candidate root.
# Run: uv run pytest 11-trees-bst -k ex05

from __future__ import annotations

from ex01_build_bst import TreeNode


def invert(root: TreeNode | None) -> TreeNode | None:
    """Mirror the tree in place: swap every node's left and right
    child, recursively. Returns `root` (now inverted) for convenience.

    invert(tree_from_level_array([1, 2, 3])) -> tree_from_level_array([1, 3, 2])

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def is_same_tree(a: TreeNode | None, b: TreeNode | None) -> bool:
    """Return whether two trees are structurally identical with the
    same value at every position.

    is_same_tree(tree_from_level_array([1, 2]), tree_from_level_array([1, 2])) -> True
    is_same_tree(tree_from_level_array([1, 2]), tree_from_level_array([1, None, 2])) -> False

    Target complexity: O(min(n, m)) time, O(h) space
    """
    raise NotImplementedError


def is_subtree(root: TreeNode | None, sub: TreeNode | None) -> bool:
    """Return whether `sub` matches some node's ENTIRE subtree in
    `root` (not a subsequence of values — shape and values must match
    exactly from that node down). An empty `sub` always matches.

    is_subtree(tree_from_level_array([3, 4, 5, 1, 2]), tree_from_level_array([4, 1, 2])) -> True

    Target complexity: O(n * m) time, O(h_root + h_sub) space (n, m = node counts)
    """
    raise NotImplementedError


def is_symmetric(root: TreeNode | None) -> bool:
    """Return whether the tree is a mirror of itself around its center
    (the left subtree is the mirror image of the right subtree).

    is_symmetric(tree_from_level_array([1, 2, 2, 3, 4, 4, 3])) -> True
    is_symmetric(tree_from_level_array([1, 2, 2, None, 3, None, 3])) -> False

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError
