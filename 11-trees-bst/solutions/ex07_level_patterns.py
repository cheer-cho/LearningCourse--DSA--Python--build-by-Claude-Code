from __future__ import annotations

from collections import deque

from ex01_build_bst import TreeNode


def right_side_view(root: TreeNode | None) -> list[int]:
    # Pattern: BFS by level, keep only the last value seen at each
    # level. O(n) time, O(n) space.
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return result


def level_averages(root: TreeNode | None) -> list[float]:
    # Pattern: BFS by level, accumulate sum/count per level. O(n) time,
    # O(n) space.
    if root is None:
        return []
    result: list[float] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.value
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level_sum / level_size)
    return result


def zigzag_levels(root: TreeNode | None) -> list[list[int]]:
    # Pattern: BFS by level, flipping the append side of the level
    # buffer each pass instead of reversing afterward. O(n) time, O(n) space.
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        level: deque[int] = deque()
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.value)
            else:
                level.appendleft(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result
