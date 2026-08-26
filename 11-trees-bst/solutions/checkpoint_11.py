from __future__ import annotations

from collections import deque


class OrgNode:
    """One person in the org chart: a name plus up to two direct
    reports (`left`, `right`)."""

    def __init__(
        self,
        name: str,
        left: OrgNode | None = None,
        right: OrgNode | None = None,
    ) -> None:
        self.name = name
        self.left = left
        self.right = right


def headcount(root: OrgNode | None) -> int:
    # Pattern: bottom-up DFS. O(n) time, O(h) space.
    if root is None:
        return 0
    return 1 + headcount(root.left) + headcount(root.right)


def management_depth(root: OrgNode | None) -> int:
    # Pattern: bottom-up DFS. O(n) time, O(h) space.
    if root is None:
        return 0
    return 1 + max(management_depth(root.left), management_depth(root.right))


def chain_of_command(root: OrgNode | None, name: str) -> list[str]:
    # Pattern: DFS carrying the current path, backtracking (popping) on
    # dead ends so the path is only ever "root to current node".
    # O(n) time, O(h) space.
    def find(node: OrgNode | None, path: list[str]) -> list[str] | None:
        if node is None:
            return None
        path.append(node.name)
        if node.name == name:
            return list(path)
        found = find(node.left, path) or find(node.right, path)
        path.pop()
        return found

    return find(root, []) or []


def meetings_by_level(root: OrgNode | None) -> list[list[str]]:
    # Pattern: BFS with a queue, one level per pass. O(n) time, O(n) space.
    if root is None:
        return []
    result: list[list[str]] = []
    queue: deque[OrgNode] = deque([root])
    while queue:
        level: list[str] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.name)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result


def common_manager(root: OrgNode | None, a: str, b: str) -> str | None:
    # Pattern: two-value DFS. At each node, ask both children "did you
    # find a or b down there?" If one side found one and the other side
    # found the other, this node is the split point (the answer). If a
    # node's own name is a or b, it counts as having found itself.
    # O(n) time, O(h) space.
    def contains(node: OrgNode | None, name: str) -> bool:
        if node is None:
            return False
        return node.name == name or contains(node.left, name) or contains(node.right, name)

    if not contains(root, a) or not contains(root, b):
        return None

    def find_lca(node: OrgNode | None) -> OrgNode | None:
        if node is None or node.name in (a, b):
            return node
        left = find_lca(node.left)
        right = find_lca(node.right)
        if left is not None and right is not None:
            return node
        return left if left is not None else right

    result = find_lca(root)
    return result.name if result is not None else None
