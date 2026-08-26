from __future__ import annotations

from ex01_build_bst import TreeNode


def delete_value(root: TreeNode | None, value: int) -> TreeNode | None:
    # Pattern: recursive BST descent to find the target, then one of three
    # splice strategies. The two-children case swaps in the inorder
    # successor (min of the right subtree) and deletes it from there,
    # which is guaranteed to be a leaf/one-child case. O(h) time/space.
    if root is None:
        return None
    if value < root.value:
        root.left = delete_value(root.left, value)
    elif value > root.value:
        root.right = delete_value(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.value = successor.value
        root.right = delete_value(root.right, successor.value)
    return root


def is_valid_bst(root: TreeNode | None) -> bool:
    # Pattern: DFS carrying a shrinking (low, high) bound — the trap this
    # exercise flags is checking only immediate children instead of every
    # ancestor's bound. O(n) time, O(h) space.
    def check(node: TreeNode | None, low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.value < high):
            return False
        return check(node.left, low, node.value) and check(node.right, node.value, high)

    return check(root, float("-inf"), float("inf"))
