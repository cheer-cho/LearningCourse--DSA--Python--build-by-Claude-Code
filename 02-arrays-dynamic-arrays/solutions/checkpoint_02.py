class Shelf[T]:
    # Pattern: dynamic array from scratch, trimmed to push/pop/get. Same
    # amortized argument as ex01's DynamicArray: doubling makes resizes
    # exponentially rarer, so the average push cost over n pushes is O(1).
    # get/size/capacity: O(1) time, O(1) space.
    # push/pop: O(1) amortized time, O(1) amortized space.

    def __init__(self) -> None:
        self._capacity = 1
        self._length = 0
        self._buffer: list[T | None] = [None] * self._capacity

    def size(self) -> int:
        return self._length

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> T:
        if index < 0 or index >= self._length:
            raise IndexError(f"index {index} out of bounds for size {self._length}")
        return self._buffer[index]  # type: ignore[return-value]

    def push(self, item: T) -> None:
        if self._length == self._capacity:
            new_capacity = self._capacity * 2
            new_buffer: list[T | None] = [None] * new_capacity
            for i in range(self._length):
                new_buffer[i] = self._buffer[i]
            self._buffer = new_buffer
            self._capacity = new_capacity
        self._buffer[self._length] = item
        self._length += 1

    def pop(self) -> T:
        if self._length == 0:
            raise IndexError("pop from empty Shelf")
        self._length -= 1
        item = self._buffer[self._length]
        self._buffer[self._length] = None
        return item  # type: ignore[return-value]


def restock_merge(a: list[int], b: list[int]) -> list[int]:
    # Pattern: linear merge (ex04). Two pointers walk both sorted lists;
    # the smaller head is always the next smallest element overall.
    # Time: O(m + n). Space: O(m + n) for the result.
    result: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def compact(slots: list[int | None]) -> int:
    # Pattern: reader/writer two-index sweep (ex03). `write` only
    # advances past occupied slots, packing them at the front in order.
    # Time: O(n). Space: O(1) extra.
    write = 0
    for read in range(len(slots)):
        if slots[read] is not None:
            slots[write] = slots[read]
            write += 1
    return write


def rotate_display(items: list[str], k: int) -> None:
    # Pattern: triple-reversal rotation (ex02). Reverse the whole list,
    # then reverse each of the two resulting segments — no second list.
    # Time: O(n). Space: O(1) extra.
    n = len(items)
    if n == 0:
        return
    k %= n
    if k == 0:
        return

    def reverse_range(start: int, end: int) -> None:
        left, right = start, end
        while left < right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1

    reverse_range(0, n - 1)
    reverse_range(0, k - 1)
    reverse_range(k, n - 1)
