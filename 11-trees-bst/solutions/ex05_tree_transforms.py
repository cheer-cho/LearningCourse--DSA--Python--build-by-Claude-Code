from __future__ import annotations

from ex01_build_bst import TreeNode


def invert(root: TreeNode | None) -> TreeNode | None:
    # Pattern: bottom-up DFS — invert both children first, then swap
    # them onto this node. O(n) time, O(h) space.
    if root is None:
        return None
    root.left, root.right = invert(root.right), invert(root.left)
    return root


def is_same_tree(a: TreeNode | None, b: TreeNode | None) -> bool:
    # Pattern: DFS in lockstep over both trees, short-circuiting on the
    # first mismatch. O(min(n, m)) time, O(h) space.
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.value == b.value and is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)


def is_subtree(root: TreeNode | None, sub: TreeNode | None) -> bool:
    # Pattern: try is_same_tree at every node of `root` — an O(m) check
    # at up to O(n) candidate roots. O(n * m) time, O(h_root + h_sub) space.
    if sub is None:
        return True
    if root is None:
        return False
    if is_same_tree(root, sub):
        return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)


def is_symmetric(root: TreeNode | None) -> bool:
    # Pattern: is_same_tree's mirrored twin — compare left vs right
    # pairwise, but cross the children (left.left with right.right,
    # left.right with right.left). O(n) time, O(h) space.
    def mirror(a: TreeNode | None, b: TreeNode | None) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.value == b.value and mirror(a.left, b.right) and mirror(a.right, b.left)

    return root is None or mirror(root.left, root.right)
