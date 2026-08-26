from __future__ import annotations


class DListNode:
    """A doubly linked node: a value plus pointers both directions."""

    def __init__(self, value: int | None = None) -> None:
        self.value = value
        self.prev: DListNode | None = None
        self.next: DListNode | None = None

    def __repr__(self) -> str:
        return f"DListNode({self.value!r})"


class DoublyLinkedList:
    """A doubly linked list with permanent head/tail SENTINEL nodes.

    The sentinels never hold real data — `self._head` is always just
    before the first real element, `self._tail` always just after the
    last. Every insert/remove only ever touches `.prev`/`.next`
    pointers, so there is never a null-check for "am I at the
    front/back?" — that's the entire point of sentinels.
    """

    def __init__(self) -> None:
        self._head = DListNode()
        self._tail = DListNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def _insert_between(self, value: int, before: DListNode, after: DListNode) -> DListNode:
        node = DListNode(value)
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node
        self._size += 1
        return node

    def push_front(self, value: int) -> DListNode:
        # Pattern: splice a new node right after the head sentinel — no
        # "is the list empty?" branch needed. O(1) time, O(1) space.
        return self._insert_between(value, self._head, self._head.next)

    def push_back(self, value: int) -> DListNode:
        # Pattern: splice a new node right before the tail sentinel.
        # O(1) time, O(1) space.
        return self._insert_between(value, self._tail.prev, self._tail)

    def pop_front(self) -> int:
        # Pattern: remove the sentinel's neighbor. O(1) time, O(1) space.
        if self._size == 0:
            raise IndexError("pop_front from empty DoublyLinkedList")
        node = self._head.next
        self.remove_node(node)
        return node.value

    def pop_back(self) -> int:
        # Pattern: remove the tail sentinel's neighbor. O(1) time, O(1) space.
        if self._size == 0:
            raise IndexError("pop_back from empty DoublyLinkedList")
        node = self._tail.prev
        self.remove_node(node)
        return node.value

    def remove_node(self, node: DListNode) -> None:
        # Pattern: bypass node by linking its neighbors to each other —
        # no search needed since we already hold the node.
        # O(1) time, O(1) space.
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self._size -= 1

    def to_array(self) -> list[int]:
        # O(n) time, O(n) space.
        values = []
        cur = self._head.next
        while cur is not self._tail:
            values.append(cur.value)
            cur = cur.next
        return values

    def size(self) -> int:
        return self._size
