# Scenario: build the singly linked list from raw nodes — the structure
# every later exercise in this module operates on. Concepts: ListNode,
# push/pop at both ends, linear search, tail-pointer bookkeeping.
# Run: uv run pytest 07-linked-lists -k ex01

from __future__ import annotations


class ListNode:
    """A single link in a singly linked list: one value, one pointer
    forward. Every later exercise in this module imports this class
    instead of redefining it.
    """

    def __init__(self, value: int, next: ListNode | None = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.value!r})"


def from_array(values: list[int]) -> ListNode | None:
    """Build a chain of ListNodes from a plain Python list, head first.

    from_array([1, 2, 3]) -> ListNode(1) -> ListNode(2) -> ListNode(3) -> None
    from_array([]) -> None

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def to_array(head: ListNode | None) -> list[int]:
    """Walk a chain of ListNodes and collect their values into a list.

    to_array(from_array([1, 2, 3])) -> [1, 2, 3]
    to_array(None) -> []

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


class SinglyLinkedList:
    """A singly linked list with head AND tail pointers, so push_back is
    O(1) instead of walking the whole list to find the end.
    """

    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self._size = 0

    def push_front(self, value: int) -> None:
        """Insert `value` as the new first element.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def push_back(self, value: int) -> None:
        """Insert `value` as the new last element, using the tail
        pointer — must NOT walk the list to find the end.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def pop_front(self) -> int:
        """Remove and return the first value.

        Raises IndexError if the list is empty.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def find(self, value: int) -> ListNode | None:
        """Return the first node holding `value`, or None if absent.

        Target: O(n) time, O(1) space.
        """
        raise NotImplementedError

    def delete_value(self, value: int) -> bool:
        """Remove the first node holding `value`. Return True if a node
        was removed, False if `value` was never found. Must correctly
        fix `self.tail` if the removed node was the last one (and reset
        it to None if the list becomes empty).

        Target: O(n) time, O(1) space.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently in the list.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def to_array(self) -> list[int]:
        """Return the list's values front-to-back as a plain list.

        Target: O(n) time, O(n) space.
        """
        raise NotImplementedError
