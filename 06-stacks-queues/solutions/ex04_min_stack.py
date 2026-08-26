class MinStack:
    # Pattern: an auxiliary "running minimum" stack kept in lockstep
    # with the value stack. Push writes min(value, current_min); pop
    # drops both stacks together, so duplicate/repeated minimums need
    # no special-case decrement bookkeeping.
    # Complexity: O(1) time per op, O(n) space.

    def __init__(self) -> None:
        self._values: list[int] = []
        self._mins: list[int] = []

    def push(self, value: int) -> None:
        current_min = value if not self._mins else min(value, self._mins[-1])
        self._values.append(value)
        self._mins.append(current_min)

    def pop(self) -> int:
        if not self._values:
            raise IndexError("pop from empty stack")
        self._mins.pop()
        return self._values.pop()

    def peek(self) -> int:
        if not self._values:
            raise IndexError("peek from empty stack")
        return self._values[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("get_min from empty stack")
        return self._mins[-1]

    def size(self) -> int:
        return len(self._values)

    def is_empty(self) -> bool:
        return not self._values
