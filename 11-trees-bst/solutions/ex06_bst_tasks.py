from __future__ import annotations

from ex01_build_bst import TreeNode


def kth_smallest(root: TreeNode | None, k: int) -> int:
    # Pattern: iterative inorder with an explicit stack, stopping the
    # instant the k-th value pops. O(h + k) time, O(h) space.
    stack: list[TreeNode] = []
    node = root
    count = 0
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.value
        node = node.right
    raise ValueError("k is out of range for this tree")


def lca_bst(root: TreeNode, a: int, b: int) -> int:
    # Pattern: ordering-guided descent — the BST invariant tells us
    # which side both targets must be on, until they split. O(h) time,
    # O(1) space.
    node: TreeNode | None = root
    while node is not None:
        if a < node.value and b < node.value:
            node = node.left
        elif a > node.value and b > node.value:
            node = node.right
        else:
            return node.value
    raise ValueError("values not found in tree")


def range_sum_bst(root: TreeNode | None, lo: int, hi: int) -> int:
    # Pattern: pruned DFS — only recurse into a subtree that could
    # possibly contain values in [lo, hi]. O(h + k) time, O(h) space.
    if root is None:
        return 0
    total = 0
    if root.value > lo:
        total += range_sum_bst(root.left, lo, hi)
    if lo <= root.value <= hi:
        total += root.value
    if root.value < hi:
        total += range_sum_bst(root.right, lo, hi)
    return total
