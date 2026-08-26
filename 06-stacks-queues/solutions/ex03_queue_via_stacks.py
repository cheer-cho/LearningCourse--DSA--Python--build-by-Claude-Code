class QueueFromStacks[T]:
    # Pattern: two stacks — "in" absorbs every enqueue in O(1); "out"
    # serves every dequeue. When "out" runs dry, pour all of "in" into
    # it; each element moves from "in" to "out" at most once across its
    # whole lifetime, so the total pouring work over n calls is O(n) —
    # amortized O(1) per dequeue (module 01's amortized argument again).
    # Complexity: enqueue O(1) worst case; dequeue amortized O(1).

    def __init__(self) -> None:
        self._in: list[T] = []
        self._out: list[T] = []

    def enqueue(self, value: T) -> None:
        self._in.append(value)

    def _pour_if_needed(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def dequeue(self) -> T:
        self._pour_if_needed()
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def front(self) -> T:
        self._pour_if_needed()
        if not self._out:
            raise IndexError("front of empty queue")
        return self._out[-1]

    def is_empty(self) -> bool:
        return not self._in and not self._out

    def size(self) -> int:
        return len(self._in) + len(self._out)
