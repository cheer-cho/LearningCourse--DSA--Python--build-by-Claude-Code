class Stack[T]:
    # Pattern: array-backed LIFO via Python's built-in dynamic array
    # (list). append/pop from the end are both O(1) amortized because
    # list is already a resizing array (module 02) — wrapping it with a
    # restricted push/pop/peek API is all that's needed.
    # Complexity: O(1) time per op, O(n) space.

    def __init__(self) -> None:
        self._data: list[T] = []

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data


class CircularQueue[T]:
    # Pattern: ring buffer — pre-sized fixed array plus a head index and
    # a count. Dequeue advances head mod capacity instead of shifting
    # elements, so wrap-around never costs more than O(1) per call.
    # Complexity: O(1) time per op, O(capacity) space.

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data: list[T | None] = [None] * capacity
        self._head = 0
        self._count = 0

    def enqueue(self, value: T) -> None:
        if self.is_full():
            raise OverflowError("enqueue on full queue")
        tail = (self._head + self._count) % self._capacity
        self._data[tail] = value
        self._count += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._count -= 1
        return value

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._data[self._head]

    def size(self) -> int:
        return self._count

    def is_full(self) -> bool:
        return self._count == self._capacity

    def is_empty(self) -> bool:
        return self._count == 0
