# Scenario: reverse a chain of ListNodes in place — the move that
# `reorder-list` (ex05) later reuses on the second half. Concepts:
# iterative pointer rewiring, recursion over a linked structure.
# Run: uv run pytest 07-linked-lists -k ex02

from __future__ import annotations

from ex01_build_singly_list import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list iteratively and return the new head.

    Rewires each node's `next` pointer in place — does not allocate any
    new nodes. The original head becomes the new tail.

    reverse_list(from_array([1, 2, 3])) -> chain reading [3, 2, 1]
    reverse_list(None) -> None
    reverse_list(from_array([5])) -> chain reading [5]

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list recursively and return the new head.

    Same contract as reverse_list, implemented with recursion instead of
    an explicit loop.

    reverse_list_recursive(from_array([1, 2, 3])) -> chain reading [3, 2, 1]

    Target: O(n) time, O(n) space (the call stack).
    """
    raise NotImplementedError
