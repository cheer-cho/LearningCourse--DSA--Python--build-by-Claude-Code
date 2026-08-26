# Scenario: four ways to read the same tree back out — three DFS orders
# plus BFS level order — the building blocks every later tree problem in
# this module reaches for.
# Concepts: preorder/inorder/postorder DFS, iterative DFS with an explicit
# stack, BFS level order with a queue.
# Run: uv run pytest 11-trees-bst -k ex03

from __future__ import annotations

from ex01_build_bst import TreeNode


def preorder(root: TreeNode | None) -> list[int]:
    """Visit node, then left subtree, then right subtree.

    preorder(tree_from_level_array([1, 2, 3])) -> [1, 2, 3]

    Target complexity: O(n) time, O(h) space (call stack)
    """
    raise NotImplementedError


def inorder(root: TreeNode | None) -> list[int]:
    """Visit left subtree, then node, then right subtree.

    inorder(tree_from_level_array([2, 1, 3])) -> [1, 2, 3]

    Target complexity: O(n) time, O(h) space (call stack)
    """
    raise NotImplementedError


def postorder(root: TreeNode | None) -> list[int]:
    """Visit left subtree, then right subtree, then node.

    postorder(tree_from_level_array([1, 2, 3])) -> [2, 3, 1]

    Target complexity: O(n) time, O(h) space (call stack)
    """
    raise NotImplementedError


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """Same order as inorder(), but with an explicit stack instead of
    recursion: walk left as far as possible (pushing as you go), then
    pop-visit-step-right.

    inorder_iterative(tree_from_level_array([2, 1, 3])) -> [1, 2, 3]

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def level_order(root: TreeNode | None) -> list[list[int]]:
    """BFS level order: one inner list per depth, values left to right.

    level_order(tree_from_level_array([1, 2, 3, 4])) -> [[1], [2, 3], [4]]
    level_order(None) -> []

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError
