# Scenario: prune and audit BSTs built from tree_from_level_array — delete
# a node while preserving the BST invariant, and catch trees that only
# look valid at a glance.
# Concepts: BST delete (leaf / one-child / two-children), bounds-based
# validation (the "child ok, grandchild wrong" trap).
# Run: uv run pytest 11-trees-bst -k ex02

from __future__ import annotations

from ex01_build_bst import TreeNode


def delete_value(root: TreeNode | None, value: int) -> TreeNode | None:
    """Delete the node holding `value` from a BST rooted at `root`,
    returning the (possibly new) root. No-op if `value` isn't present.

    Three cases:
    - leaf: drop it (parent points to None).
    - one child: splice it out (parent points straight to the child).
    - two children: replace the value with its inorder successor (the
      min of the right subtree), then delete that successor value from
      the right subtree — which always lands in the leaf/one-child case.

    delete_value(tree_from_level_array([5, 3, 8]), 3)
        -> tree_from_level_array([5, None, 8])

    Target complexity: O(h) time, O(h) space
    """
    raise NotImplementedError


def is_valid_bst(root: TreeNode | None) -> bool:
    """Return whether `root` satisfies the BST invariant: EVERY left
    descendant of a node is strictly less than it, and EVERY right
    descendant is strictly greater — not just its direct children.
    There are no duplicates in a valid BST here.

    Trap: checking only `node.left.value < node.value < node.right.value`
    passes trees where a grandchild breaks the invariant set two levels
    up. Track a running (low, high) bound through the recursion instead.

    is_valid_bst(tree_from_level_array([5, 1, 8])) -> True
    is_valid_bst(tree_from_level_array([5, 1, 8, None, None, 4])) -> False
        # 4 sits under 8 (5's right child), so it must be > 5. It isn't.

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError
