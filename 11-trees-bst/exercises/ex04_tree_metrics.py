# Scenario: quick health checks on trees loaded from tree_from_level_array
# — how deep, how big, how lopsided, and how far apart can two nodes be.
# Concepts: bottom-up recursion (compute each subtree's answer once, never
# recompute it from an ancestor), diameter via a height helper with a
# side-channel running max.
# Run: uv run pytest 11-trees-bst -k ex04

from __future__ import annotations

from ex01_build_bst import TreeNode


def max_depth(root: TreeNode | None) -> int:
    """Number of nodes on the longest root-to-leaf path. Empty tree -> 0.

    max_depth(tree_from_level_array([1, 2, 3, 4])) -> 3

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def count_nodes(root: TreeNode | None) -> int:
    """Total number of nodes in the tree.

    count_nodes(tree_from_level_array([1, 2, 3])) -> 3

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def is_balanced(root: TreeNode | None) -> bool:
    """A tree is height-balanced if, for EVERY node, the heights of its
    left and right subtrees differ by at most 1.

    Compute heights bottom-up in a single pass. Recomputing height()
    from scratch at every node (the top-down way) is O(n^2) on a skewed
    tree; tests build a large skewed tree that only a true bottom-up,
    single-pass version survives quickly.

    is_balanced(tree_from_level_array([1, 2, 3])) -> True

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def diameter(root: TreeNode | None) -> int:
    """The diameter is the number of EDGES on the longest path between
    any two nodes in the tree — the path need not pass through the root.

    Reuse the bottom-up height idea: at each node, the best path
    THROUGH that node is left_height + right_height. Track the running
    max as a side effect while computing heights in one pass.

    diameter(tree_from_level_array([1, 2, 3, 4, 5])) -> 3

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError
