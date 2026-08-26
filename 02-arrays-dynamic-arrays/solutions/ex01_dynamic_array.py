class DynamicArray[T]:
    # Pattern: dynamic array from scratch (fixed-capacity buffer + doubling
    # resize). A single push can cost O(n) when it triggers a resize, but
    # resizes get exponentially rarer, so the AVERAGE cost per push over
    # any sequence of n pushes is O(1) — amortized analysis.
    # get/set/size/capacity: O(1) time, O(1) space (no resize involved).
    # push/pop: O(1) amortized time, O(1) amortized space.

    def __init__(self) -> None:
        self._capacity = 1
        self._length = 0
        self._buffer: list[T | None] = [None] * self._capacity

    def __len__(self) -> int:
        return self._length

    def size(self) -> int:
        return self._length

    def capacity(self) -> int:
        return self._capacity

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self._length:
            raise IndexError(f"index {index} out of bounds for size {self._length}")

    def get(self, index: int) -> T:
        self._check_index(index)
        return self._buffer[index]  # type: ignore[return-value]

    def set(self, index: int, value: T) -> None:
        self._check_index(index)
        self._buffer[index] = value

    def _grow(self, new_capacity: int) -> None:
        new_buffer: list[T | None] = [None] * new_capacity
        for i in range(self._length):
            new_buffer[i] = self._buffer[i]
        self._buffer = new_buffer
        self._capacity = new_capacity

    def push(self, value: T) -> None:
        if self._length == self._capacity:
            self._grow(self._capacity * 2)
        self._buffer[self._length] = value
        self._length += 1

    def pop(self) -> T:
        if self._length == 0:
            raise IndexError("pop from empty DynamicArray")
        self._length -= 1
        value = self._buffer[self._length]
        self._buffer[self._length] = None  # drop the reference
        return value  # type: ignore[return-value]
