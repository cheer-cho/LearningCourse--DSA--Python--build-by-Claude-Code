# Scenario: rebuild a tree from two of its traversal orders — the way a
# lossless serialization format would reconstruct the original shape.
# Concepts: preorder gives roots in the order they're first visited;
# inorder splits each root's values into "left subtree" / "right
# subtree"; an index map turns "find the root's position in inorder"
# from O(n) into O(1), which is the whole ballgame at scale.
# Run: uv run pytest 11-trees-bst -k ex08

from __future__ import annotations

from ex01_build_bst import TreeNode


def build_from_pre_in(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Reconstruct the unique binary tree whose preorder and inorder
    traversals are `preorder` and `inorder`. Values are unique within
    the tree.

    Naive approach: `inorder.index(root_value)` plus slicing new lists
    at every call — O(n) per lookup/slice, O(n^2) overall. Build a
    value -> inorder-index map ONCE up front, and pass (lo, hi) index
    bounds into the recursion instead of slicing new lists, to hit
    O(n). A large balanced-tree test times out a naive version.

    build_from_pre_in([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        -> tree_from_level_array([3, 9, 20, None, None, 15, 7])
    build_from_pre_in([], []) -> None

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError
