# Scenario: splice two independently-built sorted chains into one
# sorted chain, and trim a chain relative to its end — one-pass
# pointer-surgery drills. Concepts: dummy head, node splicing, a gap
# pointer N nodes ahead of a trailing pointer.
# Run: uv run pytest 07-linked-lists -k ex04

from __future__ import annotations

from ex01_build_singly_list import ListNode


def merge_sorted(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Merge two ascending sorted chains into one ascending sorted chain.

    Splices the EXISTING nodes from `a` and `b` together — never
    allocates a new ListNode. Use a dummy head so the first node isn't
    a special case.

    merge_sorted(from_array([1, 3, 5]), from_array([2, 4])) -> chain reading [1, 2, 3, 4, 5]
    merge_sorted(None, from_array([1])) -> chain reading [1]
    merge_sorted(None, None) -> None

    Target: O(n + m) time, O(1) space.
    """
    raise NotImplementedError


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the n-th node from the end (1-indexed) and return the
    (possibly new) head. `n` is always valid: 1 <= n <= length.

    One pass: advance a lead pointer n steps ahead of a trail pointer,
    then move both together until lead falls off the end — trail now
    sits right before the node to remove. Use a dummy head so removing
    the actual head is not a special case.

    remove_nth_from_end(from_array([1, 2, 3, 4, 5]), 2) -> chain reading [1, 2, 3, 5]
    remove_nth_from_end(from_array([1]), 1) -> None

    Target: O(n) time, O(1) space, single pass.
    """
    raise NotImplementedError
