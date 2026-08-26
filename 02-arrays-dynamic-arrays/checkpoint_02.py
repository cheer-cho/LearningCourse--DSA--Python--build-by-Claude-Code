# Checkpoint 02 — Inventory Shelf
#
# A warehouse shelf needs to hold a growing number of items without ever
# knowing its final size up front, plus a few free functions for restocking
# and rearranging the shelf. This combines everything from this module:
# the dynamic array idea (rebuilt here, simplified), the reader/writer
# in-place sweep, linear merge, and the triple-reversal rotation trick.
# Run: uv run pytest 02-arrays-dynamic-arrays -k checkpoint


class Shelf[T]:
    """A growable shelf backed by a fixed-capacity buffer that doubles
    when full — the same idea as `DynamicArray` in ex01, trimmed down to
    just what the warehouse needs: push, pop, get, size.

    The backing buffer must only ever be indexed, never grown with a
    built-in append. Starts at capacity 1 and doubles on overflow.
    """

    def __init__(self) -> None:
        """Create an empty shelf with capacity 1.

        Shelf() -> size 0, capacity 1
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of items currently on the shelf.

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def capacity(self) -> int:
        """Return the current size of the backing buffer.

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def get(self, index: int) -> T:
        """Return the item at `index`. Raises IndexError if `index` is
        negative or >= size().

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def push(self, item: T) -> None:
        """Place `item` on the shelf, doubling capacity first if the
        buffer is full.

        Target complexity: O(1) amortized time, O(1) amortized space.
        """
        raise NotImplementedError

    def pop(self) -> T:
        """Remove and return the most recently placed item. Raises
        IndexError if the shelf is empty.

        Target complexity: O(1) time, O(1) space.
        """
        raise NotImplementedError


def restock_merge(a: list[int], b: list[int]) -> list[int]:
    """`a` and `b` are ascending-sorted lists of item IDs. Return a new
    ascending-sorted list combining both, as if merging a delivery batch
    `b` into existing sorted stock `a`. Does not modify `a` or `b`.

    restock_merge([1, 4, 6], [2, 3, 9]) -> [1, 2, 3, 4, 6, 9]
    restock_merge([], [5]) -> [5]

    Target complexity: O(m + n) time, O(m + n) space.
    """
    raise NotImplementedError


def compact(slots: list[int | None]) -> int:
    """`slots` represents shelf positions; an empty position holds `None`.
    Remove the empty slots in place, packing the occupied slots at the
    front in their original relative order. Return the new logical
    length (the count of occupied slots). Positions past the returned
    length are left in an unspecified state.

    slots = [7, None, 3, None, 9]; compact(slots) -> 3
        and slots[:3] == [7, 3, 9]
    slots = [None, None]; compact(slots) -> 0

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def rotate_display(items: list[str], k: int) -> None:
    """Rotate the shelf's front-facing display `items` right by `k`
    positions, in place, using the triple-reversal trick (no second
    list). `k` may exceed len(items) — treat it mod len(items).

    items = ["a", "b", "c", "d"]; rotate_display(items, 1)
        -> items is now ["d", "a", "b", "c"]

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
