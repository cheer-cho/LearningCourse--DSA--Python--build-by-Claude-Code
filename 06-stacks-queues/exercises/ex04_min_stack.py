# Scenario: an undo-friendly calculator needs O(1) access to "the
# smallest value currently on the stack," after any sequence of pushes
# and pops. Concepts: an auxiliary stack that tracks a running aggregate.
# Run: uv run pytest 06-stacks-queues -k ex04


class MinStack:
    """Stack that also answers "what's the minimum value right now?" in
    O(1), even after arbitrarily interleaved push/pop.

    Track a second, parallel stack: `_mins[i]` is the minimum of every
    value pushed so far at or below `_values[i]`. Pushing `value` also
    pushes `min(value, current_min)` onto `_mins`; popping pops both
    stacks together, so `_mins[-1]` always reflects exactly what's left
    — including duplicate minimums, with no special-case decrement
    logic needed when the min itself gets popped.

    Target complexity: push/pop/peek/get_min all O(1) time, O(n) space.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, value: int) -> None:
        """Push `value` onto the stack."""
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the top value.

        Raises IndexError if the stack is empty.
        """
        raise NotImplementedError

    def peek(self) -> int:
        """Return the top value without removing it.

        Raises IndexError if the stack is empty.
        """
        raise NotImplementedError

    def get_min(self) -> int:
        """Return the minimum value currently on the stack, in O(1).

        Raises IndexError if the stack is empty.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of elements currently on the stack."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the stack holds no elements."""
        raise NotImplementedError
