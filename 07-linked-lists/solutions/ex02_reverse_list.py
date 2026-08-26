from __future__ import annotations

from ex01_build_singly_list import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    # Pattern: pointer surgery — walk once, flipping each node's next
    # pointer to point backward, saving the forward link before
    # overwriting it. O(n) time, O(1) space.
    prev: ListNode | None = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    # Pattern: reverse the rest of the list first, then fix up the
    # link between this node and the (now-reversed) rest.
    # O(n) time, O(n) space (recursion stack, one frame per node).
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
