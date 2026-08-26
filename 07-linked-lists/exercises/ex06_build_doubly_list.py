# Scenario: build a doubly linked list with head/tail SENTINEL nodes,
# so every insert/remove is branch-free — no "is this the first/last
# node?" checks anywhere. Concepts: sentinel nodes, prev/next pointer
# surgery, O(1) removal given a node reference.
# Run: uv run pytest 07-linked-lists -k ex06

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

    def push_front(self, value: int) -> DListNode:
        """Insert `value` right after the head sentinel. Returns the
        new node so callers can hold onto it for O(1) removal later.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def push_back(self, value: int) -> DListNode:
        """Insert `value` right before the tail sentinel. Returns the
        new node.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def pop_front(self) -> int:
        """Remove and return the value nearest the front.

        Raises IndexError if the list is empty.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def pop_back(self) -> int:
        """Remove and return the value nearest the back.

        Raises IndexError if the list is empty.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def remove_node(self, node: DListNode) -> None:
        """Remove a specific node in O(1) — the whole point of a
        doubly linked list. `node` must currently belong to this list
        and must not be a sentinel.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def to_array(self) -> list[int]:
        """Return values front-to-back as a plain list (skips both
        sentinels).

        Target: O(n) time, O(n) space.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of real (non-sentinel) elements.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError
