from __future__ import annotations

from collections import deque

from ex01_build_bst import TreeNode


def preorder(root: TreeNode | None) -> list[int]:
    # Pattern: DFS, visit-then-recurse, accumulating into one shared list.
    # Concatenating fresh lists at every call (`[v] + left + right`) looks
    # tempting but is O(n^2) on a skewed tree — each concatenation copies
    # its whole left operand. Append-in-place keeps it true O(n) time.
    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return
        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def inorder(root: TreeNode | None) -> list[int]:
    # Pattern: DFS, recurse-visit-recurse, same accumulator trick as
    # preorder. O(n) time, O(h) space (call stack).
    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return
        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result


def postorder(root: TreeNode | None) -> list[int]:
    # Pattern: DFS, recurse-recurse-visit, same accumulator trick.
    # O(n) time, O(h) space (call stack).
    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return
        visit(node.left)
        visit(node.right)
        result.append(node.value)

    visit(root)
    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    # Pattern: explicit stack standing in for the call stack — walk left
    # to the bottom, then pop/visit/step-right. O(n) time, O(h) space.
    result: list[int] = []
    stack: list[TreeNode] = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.value)
        node = node.right
    return result


def level_order(root: TreeNode | None) -> list[list[int]]:
    # Pattern: BFS with a queue, snapshotting the queue's length at the
    # start of each level to know where that level ends. O(n) time/space.
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result
