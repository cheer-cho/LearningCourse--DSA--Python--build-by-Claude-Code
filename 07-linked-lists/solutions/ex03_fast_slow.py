from __future__ import annotations

from ex01_build_singly_list import ListNode


def middle_node(head: ListNode | None) -> ListNode | None:
    # Pattern: fast & slow pointers. fast moves 2 steps per tick, slow
    # moves 1. When fast falls off the end, slow sits at the (second)
    # middle. O(n) time, O(1) space, one pass.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_cycle(head: ListNode | None) -> bool:
    # Pattern: Floyd's cycle detection. If fast ever equals slow after
    # the first step, they met inside a cycle. O(n) time, O(1) space.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def cycle_start(head: ListNode | None) -> ListNode | None:
    # Pattern: Floyd's phase 2. Phase 1 finds a meeting point inside
    # the cycle (or proves there isn't one); phase 2 resets one pointer
    # to head and advances both one step at a time — they meet again
    # exactly at the cycle's start. O(n) time, O(1) space.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            pointer = head
            while pointer is not slow:
                pointer = pointer.next
                slow = slow.next
            return pointer
    return None
