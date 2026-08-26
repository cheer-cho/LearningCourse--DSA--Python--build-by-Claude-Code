# Checkpoint 06 — Editor session
#
# A minimal text editor's undo/redo history (two stacks of prior
# document states), plus the classic stock-span problem (a monotonic
# stack) — this pulls together both structures the module is named
# for.
# Run: uv run pytest 06-stacks-queues -k checkpoint


class EditorHistory:
    """A minimal text editor session with undo/redo.

    `self.text` holds the current document content (starts as `""`).
    `type` appends text; `delete_last` removes the single last
    character. Both are undoable via `undo`/`redo`, backed by two
    stacks: an undo stack of prior document states, and a redo stack of
    states that were undone.

    The classic subtlety: typing something NEW after an undo clears the
    redo stack — you can't redo into a future that no longer exists
    once you've branched off in a new direction with fresh input.

    Target complexity: type/delete_last/undo/redo all O(1) amortized
    per call (each state push/pop is O(1) — the same amortized
    argument as a dynamic array's push, from module 01/02).
    """

    def __init__(self) -> None:
        """Start an empty document with no undo/redo history."""
        raise NotImplementedError

    def type(self, text: str) -> None:
        """Append `text` to the document. Clears the redo stack.

        e = EditorHistory(); e.type("cat") -> e.text == "cat"
        """
        raise NotImplementedError

    def delete_last(self) -> None:
        """Remove the single last character of the document, if any.

        Deleting from an already-empty document does nothing — no
        history entry is recorded, so a following undo skips right
        past it.
        """
        raise NotImplementedError

    def undo(self) -> None:
        """Revert the last `type`/`delete_last` change, if any.

        Undoing with no history does nothing.
        """
        raise NotImplementedError

    def redo(self) -> None:
        """Reapply the last change undone by `undo`, if any.

        Redoing with no undone history does nothing.
        """
        raise NotImplementedError


def spans(prices: list[int]) -> list[int]:
    """Return the stock-span for each day: the number of consecutive
    days ending at and including that day (counting backward) for which
    the price stayed <= that day's price.

    spans([100, 80, 60, 70, 60, 75, 85]) -> [1, 1, 1, 2, 1, 4, 6]
    spans([10, 10, 10]) -> [1, 2, 3]
    spans([5, 4, 3, 2, 1]) -> [1, 1, 1, 1, 1]
    spans([]) -> []

    Target complexity: O(n) time, O(n) space — a monotonic stack of
    (index, price) pairs, each pushed and popped at most once.
    """
    raise NotImplementedError
