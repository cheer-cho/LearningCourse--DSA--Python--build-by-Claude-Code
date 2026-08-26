# Scenario: three classic "read a tree level by level" problems — the
# same BFS frontier each time, only what you keep per level changes.
# Concepts: BFS level order, per-level aggregation, alternating output
# order.
# Run: uv run pytest 11-trees-bst -k ex07

from __future__ import annotations

from ex01_build_bst import TreeNode


def right_side_view(root: TreeNode | None) -> list[int]:
    """Return the values visible from the right side, top to bottom:
    the last node visited at each level.

    right_side_view(tree_from_level_array([1, 2, 3, None, 5, None, 4])) -> [1, 3, 4]

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError


def level_averages(root: TreeNode | None) -> list[float]:
    """Return the average value at each level, top to bottom.

    level_averages(tree_from_level_array([3, 9, 20, None, None, 15, 7])) -> [3.0, 14.5, 11.0]

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError


def zigzag_levels(root: TreeNode | None) -> list[list[int]]:
    """Return level order, but alternate direction each level: level 0
    left-to-right, level 1 right-to-left, level 2 left-to-right, and
    so on.

    zigzag_levels(tree_from_level_array([3, 9, 20, None, None, 15, 7])) -> [[3], [20, 9], [15, 7]]

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError
