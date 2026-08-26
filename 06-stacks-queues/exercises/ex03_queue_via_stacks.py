# Scenario: reimplement a FIFO queue using only two LIFO stacks, as if
# Stack were the only container available. Concepts: amortized analysis
# (module 01) applied to a real data structure, not just a dynamic array.
# Run: uv run pytest 06-stacks-queues -k ex03


class QueueFromStacks[T]:
    """FIFO queue built from two stacks: an "in" stack for enqueue, an
    "out" stack for dequeue.

    enqueue always pushes onto the "in" stack — O(1). dequeue pops from
    the "out" stack; when "out" is empty, everything is poured from
    "in" into "out" first (popping "in" and pushing "out" reverses the
    order, so the oldest item ends up on top of "out", ready to pop).

    Each element is moved from "in" to "out" at most once in its
    lifetime, so across n operations the total pouring work is O(n) —
    amortized O(1) per dequeue, even though any single dequeue can
    occasionally cost O(n) (same shape of argument as the dynamic
    array's amortized O(1) push from module 01/02: rare expensive
    operations, spread thin across every call).

    Target complexity: enqueue O(1) worst case; dequeue amortized O(1).
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, value: T) -> None:
        """Add `value` at the back of the queue."""
        raise NotImplementedError

    def dequeue(self) -> T:
        """Remove and return the value at the front of the queue.

        Raises IndexError if the queue is empty.
        """
        raise NotImplementedError

    def front(self) -> T:
        """Return the value at the front of the queue without removing it.

        Raises IndexError if the queue is empty.
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the queue holds no elements."""
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently stored."""
        raise NotImplementedError
