# Scenario: build the engine every other exercise in this module rests
# on. Pattern: binary min-heap as a flat array (parent i -> children
# 2i+1, 2i+2), sift up on push, sift down on pop, bottom-up heapify.
# FROM SCRATCH: no `heapq`, no other library heap.
# Run: uv run pytest 12-heaps-priority-queues -k ex01


class MinHeap:
    """A binary min-heap backed by a plain Python list.

    The smallest value pushed so far is always available at the root
    in O(1). `push` and `pop` each cost O(log n); `heapify` builds a
    heap from an existing list in O(n).

    Target complexity: push/pop O(log n), peek/size O(1),
    heapify O(n) time, O(1) extra space (in place).
    """

    def __init__(self) -> None:
        """Create an empty heap."""
        raise NotImplementedError

    def push(self, val: int) -> None:
        """Insert `val`, then sift it up until the heap property holds.

        h = MinHeap()
        h.push(5); h.push(1); h.push(3)
        h.peek() -> 1
        """
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the smallest value.

        Move the last element into the root's slot, shrink by one,
        then sift down. Raise `IndexError` if the heap is empty.

        h = MinHeap(); h.push(5); h.push(1); h.push(3)
        h.pop() -> 1
        h.pop() -> 3
        """
        raise NotImplementedError

    def peek(self) -> int:
        """Return (without removing) the smallest value.

        Raise `IndexError` if the heap is empty.

        h = MinHeap(); h.push(4)
        h.peek() -> 4
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return how many elements are currently in the heap.

        h = MinHeap(); h.push(1); h.push(2)
        h.size() -> 2
        """
        raise NotImplementedError

    @classmethod
    def heapify(cls, nums: list[int]) -> "MinHeap":
        """Build a MinHeap from `nums` in O(n) — NOT by pushing one at
        a time (that would cost O(n log n)).

        Copy `nums` into the internal array, then sift down every node
        that has children, starting from the last parent and working
        back to the root. `nums` itself must be left unmodified.

        MinHeap.heapify([5, 1, 3]).peek() -> 1
        MinHeap.heapify([]).size() -> 0
        """
        raise NotImplementedError
