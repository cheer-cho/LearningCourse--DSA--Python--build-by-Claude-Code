# Scenario: study a tree the way LeetCode does — flat level-order arrays
# in, a linked node structure out. Every later exercise in this module
# builds trees with tree_from_level_array and reads them back with
# tree_to_level_array, so get these right first.
# Concepts: binary tree nodes, BST insert/search, inorder = sorted order.
# Run: uv run pytest 11-trees-bst -k ex01

from __future__ import annotations


class TreeNode:
    """A binary tree node: a value plus a left and right child (or None)."""

    def __init__(
        self,
        value: int,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"


def tree_from_level_array(values: list[int | None]) -> TreeNode | None:
    """Build a binary tree from a LeetCode-style level-order array.

    `values` lists nodes level by level, left to right; `None` marks a
    missing child. A node listed as `None` never gets children of its
    own entries in `values` (matches LeetCode's convention exactly).

    tree_from_level_array([]) -> None
    tree_from_level_array([1, 2, 3]) -> node 1 with left=2, right=3
    tree_from_level_array([1, 2, None, 3]) -> 1.left=2, 2.left=3, 1.right=None

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError


def tree_to_level_array(root: TreeNode | None) -> list[int | None]:
    """Inverse of tree_from_level_array: flatten a tree back into a
    level-order array, trimmed of trailing `None` values (matches
    LeetCode's canonical output format).

    tree_to_level_array(None) -> []
    tree_to_level_array(tree_from_level_array([1, 2, 3])) -> [1, 2, 3]
    tree_to_level_array(tree_from_level_array([1, 2, None, 3])) -> [1, 2, None, 3]

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError


class BST:
    """A binary search tree over int values. Duplicates are ignored:
    inserting a value that's already present leaves the tree unchanged."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        """Insert `value`, preserving the BST invariant. No-op if
        `value` is already present.

        Target complexity: O(h) time, O(h) space (recursion), h = height
        """
        raise NotImplementedError

    def contains(self, value: int) -> bool:
        """Return whether `value` exists in the tree.

        Target complexity: O(h) time, O(1) space (iterative)
        """
        raise NotImplementedError

    def min_value(self) -> int:
        """Return the smallest value in the tree. Raise ValueError if
        the tree is empty.

        Target complexity: O(h) time, O(1) space
        """
        raise NotImplementedError

    def max_value(self) -> int:
        """Return the largest value in the tree. Raise ValueError if
        the tree is empty.

        Target complexity: O(h) time, O(1) space
        """
        raise NotImplementedError

    def to_sorted_array(self) -> list[int]:
        """Return every value in ascending order. An inorder traversal
        gets this for free by exploiting the BST invariant.

        Target complexity: O(n) time, O(n) space
        """
        raise NotImplementedError
