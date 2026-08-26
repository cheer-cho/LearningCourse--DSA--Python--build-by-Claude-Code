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
    # Pattern: build front-to-back, tracking the last node so each new
    # node attaches in O(1) instead of walking from the head each time.
    # O(n) time, O(n) space (n new nodes).
    head: ListNode | None = None
    tail: ListNode | None = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_array(head: ListNode | None) -> list[int]:
    # Pattern: linear walk, collecting values as we go.
    # O(n) time, O(n) space (the output list).
    values = []
    cur = head
    while cur is not None:
        values.append(cur.value)
        cur = cur.next
    return values


class SinglyLinkedList:
    """A singly linked list with head AND tail pointers, so push_back is
    O(1) instead of walking the whole list to find the end.
    """

    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self._size = 0

    def push_front(self, value: int) -> None:
        # Pattern: new node's next = old head, then move head. O(1).
        node = ListNode(value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def push_back(self, value: int) -> None:
        # Pattern: use the stored tail pointer — never walk. O(1).
        node = ListNode(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_front(self) -> int:
        # Pattern: detach head, fix tail if the list just became empty.
        # O(1) time, O(1) space.
        if self.head is None:
            raise IndexError("pop_front from empty SinglyLinkedList")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return node.value

    def find(self, value: int) -> ListNode | None:
        # Pattern: linear scan, no shortcuts possible without an index.
        # O(n) time, O(1) space.
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def delete_value(self, value: int) -> bool:
        # Pattern: track prev while scanning so we can splice the
        # victim out; fix tail if we removed the last node.
        # O(n) time (search), O(1) space.
        prev: ListNode | None = None
        cur = self.head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def size(self) -> int:
        return self._size

    def to_array(self) -> list[int]:
        return to_array(self.head)
