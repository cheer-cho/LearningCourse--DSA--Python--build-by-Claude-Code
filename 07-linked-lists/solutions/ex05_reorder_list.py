from __future__ import annotations

from ex01_build_singly_list import ListNode
from ex02_reverse_list import reverse_list
from ex03_fast_slow import middle_node


def reorder(head: ListNode | None) -> None:
    # Pattern: combine three earlier moves. Find the middle (fast/slow),
    # split into two halves, reverse the second half (pointer surgery),
    # then interleave the two halves one node at a time.
    # O(n) time, O(1) space.
    if head is None or head.next is None:
        return

    mid = middle_node(head)
    second = mid.next
    mid.next = None  # split the list into first (head..mid) and second
    second = reverse_list(second)

    first = head
    while second is not None:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next
