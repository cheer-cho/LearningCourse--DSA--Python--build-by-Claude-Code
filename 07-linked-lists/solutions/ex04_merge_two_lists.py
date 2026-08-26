from __future__ import annotations

from ex01_build_singly_list import ListNode


def merge_sorted(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    # Pattern: dummy head + two pointers, always attaching the smaller
    # of the two current nodes and advancing that list. No new nodes.
    # O(n + m) time, O(1) space.
    dummy = ListNode(0)
    tail = dummy
    while a is not None and b is not None:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    # Pattern: gap pointer. Advance `lead` n steps ahead of `trail`
    # (both starting from a dummy head), then move both together until
    # lead runs off the end — trail.next is now the node to remove.
    # O(n) time, O(1) space, single pass.
    dummy = ListNode(0, next=head)
    lead: ListNode | None = dummy
    trail = dummy
    for _ in range(n):
        lead = lead.next
    while lead.next is not None:
        lead = lead.next
        trail = trail.next
    trail.next = trail.next.next
    return dummy.next
