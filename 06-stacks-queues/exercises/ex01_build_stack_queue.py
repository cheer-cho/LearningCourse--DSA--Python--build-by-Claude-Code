# Scenario: build the two workhorse containers everything else in this
# module leans on — a LIFO Stack and a fixed-capacity, wrap-around
# CircularQueue. Concepts: array-backed storage, amortized vs strict
# O(1) ops, ring-buffer index math.
# Run: uv run pytest 06-stacks-queues -k ex01


class Stack[T]:
    """LIFO stack backed by a plain Python list (a dynamic array).

    push/pop/peek/size/is_empty. Popping or peeking an empty stack is a
    programmer error, not a normal outcome — raise IndexError.

    Target complexity: every method O(1) time (push is amortized O(1),
    same as list.append from module 02); O(n) space for n elements.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, value: T) -> None:
        """Push `value` onto the top of the stack.

        A push immediately followed by peek() always returns `value`.
        """
        raise NotImplementedError

    def pop(self) -> T:
        """Remove and return the top value.

        Stack().pop() -> raises IndexError (underflow: nothing to pop).
        """
        raise NotImplementedError

    def peek(self) -> T:
        """Return the top value without removing it.

        Raises IndexError on an empty stack.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently stored."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the stack holds no elements."""
        raise NotImplementedError


class CircularQueue[T]:
    """Fixed-capacity FIFO queue backed by a pre-sized ring buffer.

    enqueue/dequeue/front/size/is_full/is_empty. The backing storage is
    a list pre-sized to `capacity` at construction time and never
    resized. Elements are never shifted — dequeue just advances a head
    index (mod capacity), so interleaved enqueue/dequeue wrap-around
    stays O(1) per call, however many times the buffer wraps.

    Target complexity: every method O(1) time, O(capacity) space.
    """

    def __init__(self, capacity: int) -> None:
        """Create an empty queue that can hold at most `capacity` items.

        `capacity` is always >= 1.
        """
        raise NotImplementedError

    def enqueue(self, value: T) -> None:
        """Add `value` at the back of the queue.

        Raises OverflowError if the queue is already at capacity.
        """
        raise NotImplementedError

    def dequeue(self) -> T:
        """Remove and return the value at the front of the queue.

        Raises IndexError if the queue is empty.
        """
        raise NotImplementedError

    def front(self) -> T:
        """Return the front value without removing it.

        Raises IndexError if the queue is empty.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently stored."""
        raise NotImplementedError

    def is_full(self) -> bool:
        """Return True if the queue is at capacity."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the queue holds no elements."""
        raise NotImplementedError
