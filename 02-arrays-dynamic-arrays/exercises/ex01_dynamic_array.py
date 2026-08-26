# Scenario: build the resizable array that every list/vector type in every
# language is secretly running underneath. Concepts: fixed-capacity backing
# buffer, bounds-checked get/set, doubling resize, amortized O(1) push.
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex01


class DynamicArray[T]:
    """A resizable array built from scratch on top of a fixed-size buffer.

    The backing buffer is allocated once per capacity and only ever
    INDEXED — never grown with a built-in `append`/`insert`. Growth
    happens by allocating a brand-new, bigger buffer and copying every
    existing element into it (see `_grow`).

    Starts at capacity 1. Whenever a push would overflow the buffer, the
    capacity doubles before the write happens.
    """

    def __init__(self) -> None:
        """Create an empty array with capacity 1.

        DynamicArray() -> size 0, capacity 1
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of elements currently stored (not capacity).

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently stored (not capacity).

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def capacity(self) -> int:
        """Return the current size of the backing buffer.

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def get(self, index: int) -> T:
        """Return the element at `index`.

        Raises IndexError if `index` is negative or >= size().

        arr = DynamicArray(); arr.push(9)
        arr.get(0) -> 9
        arr.get(1) -> raises IndexError

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def set(self, index: int, value: T) -> None:
        """Overwrite the element at `index` with `value`.

        Raises IndexError if `index` is negative or >= size(). Does not
        change size() — `set` can never grow the array, only `push` can.

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def push(self, value: T) -> None:
        """Append `value` at the end, doubling capacity first if the
        buffer is full (size() == capacity()).

        arr = DynamicArray()
        arr.push(1); arr.capacity() -> 1
        arr.push(2); arr.capacity() -> 2
        arr.push(3); arr.capacity() -> 4

        Target complexity: O(1) amortized time, O(1) amortized space.
        """
        raise NotImplementedError

    def pop(self) -> T:
        """Remove and return the last element.

        Raises IndexError if the array is empty. Capacity never shrinks
        on pop — only push grows it.

        arr = DynamicArray(); arr.push(5)
        arr.pop() -> 5
        arr.pop() -> raises IndexError

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError
