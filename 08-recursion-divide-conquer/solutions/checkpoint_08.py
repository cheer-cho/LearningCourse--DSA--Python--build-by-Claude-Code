# All four functions use the ex06 recipe (explicit stack instead of the
# call stack) rather than plain recursion: the deep-chain test builds a
# 3,000-node tree, well past Python's default recursion limit (1000), so
# a recursive walk would raise RecursionError. Every traversal below
# pushes a node's children in REVERSED order before popping, so the
# stack still visits them left-to-right (matching a recursive pre-order
# walk) — this keeps "first encountered" tie-breaks well-defined.
#
# Time: O(n) for every function, n = node count.
# Space: O(d) for the explicit stack, d = tree depth (worst case O(n) for
# find_path/largest_file's path/child bookkeeping on a single-branch
# chain, same shape a recursive call stack would use).

from typing import Any

FileNode = dict[str, Any]


def total_size(tree: FileNode) -> int:
    total = 0
    stack: list[FileNode] = [tree]
    while stack:
        node = stack.pop()
        total += node["size"]
        stack.extend(node["children"])
    return total


def max_tree_depth(tree: FileNode) -> int:
    deepest = 0
    stack: list[tuple[FileNode, int]] = [(tree, 1)]
    while stack:
        node, depth = stack.pop()
        deepest = max(deepest, depth)
        for child in node["children"]:
            stack.append((child, depth + 1))
    return deepest


def find_path(tree: FileNode, name: str) -> list[str] | None:
    stack: list[tuple[FileNode, list[str]]] = [(tree, [tree["name"]])]
    while stack:
        node, path = stack.pop()
        if node["name"] == name:
            return path
        for child in reversed(node["children"]):
            stack.append((child, path + [child["name"]]))
    return None


def largest_file(tree: FileNode) -> str:
    # A well-formed tree always has >= 1 leaf (children lists are
    # finite), so best_name is guaranteed to be set by the time we
    # return — the loop always visits at least `tree` itself.
    best_name = ""
    best_size: int | None = None
    stack: list[FileNode] = [tree]
    while stack:
        node = stack.pop()
        if not node["children"]:
            if best_size is None or node["size"] > best_size:
                best_name = node["name"]
                best_size = node["size"]
        else:
            stack.extend(reversed(node["children"]))
    return best_name
