# Scenario: detect structural properties of a chain using two pointers
# moving at different speeds — no counting pass, no extra memory.
# Concepts: fast & slow pointers, Floyd's cycle detection.
# Run: uv run pytest 07-linked-lists -k ex03

from __future__ import annotations

from ex01_build_singly_list import ListNode


def middle_node(head: ListNode | None) -> ListNode | None:
    """Return the middle node of a singly linked list.

    For an EVEN-length list, return the SECOND of the two middle nodes
    (e.g. for [1, 2, 3, 4], return the node holding 3).

    middle_node(from_array([1, 2, 3])) -> node holding 2
    middle_node(from_array([1, 2, 3, 4])) -> node holding 3
    middle_node(None) -> None

    Target: O(n) time, O(1) space, one pass.
    """
    raise NotImplementedError


def has_cycle(head: ListNode | None) -> bool:
    """Return True if the list loops back on itself anywhere.

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def cycle_start(head: ListNode | None) -> ListNode | None:
    """Return the node where a cycle begins, or None if there is no
    cycle.

    This is Floyd's algorithm, phase 2: after the tortoise and hare
    meet inside the cycle, reset one pointer to `head` and advance both
    pointers one step at a time — they meet again exactly at the
    cycle's start node.

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
