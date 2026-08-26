# Checkpoint 11 — Company org chart
#
# Model a company as a binary tree: each OrgNode is one person with up to
# two direct reports stored as `left`/`right` (this simplified org chart
# caps every manager at two reports). Combines every pattern from this
# module: counting, depth, root-to-node path, BFS-by-level, and general
# (non-BST) LCA via the two-value DFS trick.
# Run: uv run pytest 11-trees-bst -k checkpoint

from __future__ import annotations


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
    """Total number of people in the org, including `root`.

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def management_depth(root: OrgNode | None) -> int:
    """Number of levels in the org, from the CEO (`root`) down to the
    most junior report. Empty org -> 0.

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def chain_of_command(root: OrgNode | None, name: str) -> list[str]:
    """Return the path of names from `root` down to `name`, inclusive
    on both ends. Return `[]` if `name` isn't in the org.

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError


def meetings_by_level(root: OrgNode | None) -> list[list[str]]:
    """Group names level by level (BFS), root first, left to right
    within a level — handy for scheduling "all managers at depth d"
    meetings.

    Target complexity: O(n) time, O(n) space
    """
    raise NotImplementedError


def common_manager(root: OrgNode | None, a: str, b: str) -> str | None:
    """Return the name of the lowest common manager of `a` and `b` —
    the deepest node with both as descendants (a person counts as
    their own manager here). This is a general tree, not a BST, so
    there's no ordering to exploit: recurse into both children and
    combine ("if I find `a` on one side and `b` on the other, I AM the
    answer" — the classic two-value DFS). Return None if either name
    is missing from the org.

    Target complexity: O(n) time, O(h) space
    """
    raise NotImplementedError
