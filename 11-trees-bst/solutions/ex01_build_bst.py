from __future__ import annotations

from collections import deque


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
    # Pattern: BFS construction. Each node dequeued in turn claims the next
    # one or two entries in `values` as its children. O(n) time/space —
    # every entry is visited exactly once.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.popleft()
        if i < n:
            left_value = values[i]
            i += 1
            if left_value is not None:
                node.left = TreeNode(left_value)
                queue.append(node.left)
        if i < n:
            right_value = values[i]
            i += 1
            if right_value is not None:
                node.right = TreeNode(right_value)
                queue.append(node.right)
    return root


def tree_to_level_array(root: TreeNode | None) -> list[int | None]:
    # Pattern: BFS flatten, mirroring construction. Missing children are
    # recorded as a single `None` slot without expanding further (a `None`
    # node has no children of its own). Trim trailing Nones at the end to
    # match LeetCode's canonical, minimal representation. O(n) time/space.
    if root is None:
        return []
    result: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.value)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


class BST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        # Pattern: recursive BST descent — go left/right by comparison,
        # rebuild the path back up. Duplicates are dropped silently.
        # O(h) time, O(h) space (call stack).
        self.root = self._insert(self.root, value)

    def _insert(self, node: TreeNode | None, value: int) -> TreeNode:
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def contains(self, value: int) -> bool:
        # Pattern: iterative BST descent, O(h) time, O(1) space.
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def min_value(self) -> int:
        # Pattern: leftmost node holds the minimum. O(h) time, O(1) space.
        if self.root is None:
            raise ValueError("tree is empty")
        node = self.root
        while node.left is not None:
            node = node.left
        return node.value

    def max_value(self) -> int:
        # Pattern: rightmost node holds the maximum. O(h) time, O(1) space.
        if self.root is None:
            raise ValueError("tree is empty")
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def to_sorted_array(self) -> list[int]:
        # Pattern: inorder traversal — a BST's inorder walk is always
        # sorted. O(n) time, O(n) space.
        result: list[int] = []

        def inorder(node: TreeNode | None) -> None:
            if node is None:
                return
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)

        inorder(self.root)
        return result
