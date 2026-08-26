# Checkpoint 08 — File tree
#
# A file-tree node is a dict: {"name": str, "size": int, "children":
# list[node]}. A file (leaf) has an empty "children" list; a directory's
# own "size" is typically 0, but total_size still adds it in, so the
# functions below work for any size value on any node.
#
# tree = {
#     "name": "root", "size": 0, "children": [
#         {"name": "notes.txt", "size": 120, "children": []},
#         {"name": "sub", "size": 0, "children": [
#             {"name": "photo.png", "size": 2048, "children": []},
#         ]},
#     ],
# }
#
# This checkpoint is module 11's warm-up: trees are recursive-by-nature
# data, and one test builds a tree deep enough that a naive recursive
# walk would overflow Python's default recursion limit (1000) — use the
# recursion -> iteration recipe from ex06 (explicit stack), or document
# why plain recursion is safe for your chosen depth.
# Run: uv run pytest 08-recursion-divide-conquer -k checkpoint

from typing import Any

FileNode = dict[str, Any]


def total_size(tree: FileNode) -> int:
    """Return the sum of "size" across `tree` and every descendant.

    total_size({"name": "a", "size": 5, "children": []}) -> 5
    total_size({"name": "r", "size": 0, "children": [
        {"name": "a", "size": 5, "children": []},
        {"name": "b", "size": 3, "children": []},
    ]}) -> 8

    Target: O(n) time, O(d) space, n = node count, d = max depth.
    """
    raise NotImplementedError


def max_tree_depth(tree: FileNode) -> int:
    """Return the depth of `tree`. A node with no children has depth 1;
    each level of children adds 1.

    max_tree_depth({"name": "a", "size": 5, "children": []}) -> 1
    max_tree_depth({"name": "r", "size": 0, "children": [
        {"name": "a", "size": 0, "children": [
            {"name": "b", "size": 1, "children": []},
        ]},
    ]}) -> 3

    Target: O(n) time, O(d) space.
    """
    raise NotImplementedError


def find_path(tree: FileNode, name: str) -> list[str] | None:
    """Return the list of names from `tree`'s root down to (and
    including) the first node named `name`, found via a depth-first,
    children-in-order search. Return None if no node has that name.

    find_path({"name": "r", "size": 0, "children": [
        {"name": "a", "size": 0, "children": [
            {"name": "b", "size": 1, "children": []},
        ]},
    ]}, "b") -> ["r", "a", "b"]
    find_path({"name": "r", "size": 0, "children": []}, "missing") -> None

    Target: O(n) time, O(d) space.
    """
    raise NotImplementedError


def largest_file(tree: FileNode) -> str:
    """Return the name of the leaf (a node with an empty "children"
    list) with the largest "size" anywhere in `tree`. Directories
    (nodes WITH children) are never candidates, even if their own
    "size" is large. Ties: return whichever leaf is encountered first in
    a depth-first, children-in-order traversal.

    Every well-formed tree has at least one leaf (children lists are
    finite, so some node's must eventually be empty) — including `tree`
    itself, if it has no children — so this always returns a name.

    largest_file({"name": "r", "size": 0, "children": [
        {"name": "a.txt", "size": 5, "children": []},
        {"name": "b.txt", "size": 9, "children": []},
    ]}) -> "b.txt"
    largest_file({"name": "solo.txt", "size": 0, "children": []}) -> "solo.txt"

    Target: O(n) time, O(d) space.
    """
    raise NotImplementedError
