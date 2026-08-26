from __future__ import annotations

from ex01_build_bst import TreeNode


def max_depth(root: TreeNode | None) -> int:
    # Pattern: bottom-up DFS — "trust the subtree" for left and right,
    # combine with +1. O(n) time, O(h) space.
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def count_nodes(root: TreeNode | None) -> int:
    # Pattern: bottom-up DFS, same shape as max_depth. O(n) time, O(h) space.
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_balanced(root: TreeNode | None) -> bool:
    # Pattern: single bottom-up pass computing height AND balance
    # together, short-circuiting with a -1 sentinel the moment any
    # subtree is found unbalanced. O(n) time, O(h) space — vs. O(n^2) for
    # a version that calls a separate height() at every node.
    def height(node: TreeNode | None) -> int:
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


def diameter(root: TreeNode | None) -> int:
    # Pattern: bottom-up height helper with a closured running max — the
    # diameter through any node is left_height + right_height, checked
    # once per node as heights are computed. O(n) time, O(h) space.
    best = 0

    def height(node: TreeNode | None) -> int:
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best
