# Scenario: a monitoring system reports the running median latency
# after every request, without ever re-sorting the full request log.
# Pattern: two-heaps running median (HARD -- the two-heaps trick shows
# up any time you need a live "middle" of a growing stream).
# Run: uv run pytest 12-heaps-priority-queues -k ex06


class MedianFinder:
    """Tracks the median of a stream of numbers using two heaps kept
    balanced against each other:

    - `lows`: a MAX-heap holding the smaller half of the numbers.
    - `highs`: a MIN-heap holding the larger half.

    The invariant to maintain after every `add`:
    1. Every value in `lows` <= every value in `highs`.
    2. The heap sizes differ by at most 1 (`lows` may hold exactly one
       more than `highs`, never the other way around).

    With that invariant, the median is always at the top of one or
    both heaps -- no scan needed. Rebalance by pushing the new value
    into ONE heap, then, if that broke the "lows <= highs" ordering or
    the size balance, popping the top and pushing it across to the
    other heap.

    Python's `heapq` is a min-heap only; simulate `lows` as a
    max-heap by negating every value going in and out.

    Target complexity: `add` O(log n), `median` O(1).
    """

    def __init__(self) -> None:
        """Start with an empty stream."""
        raise NotImplementedError

    def add(self, num: int) -> None:
        """Add `num` to the stream, then rebalance the two heaps so
        the invariant above holds.

        mf = MedianFinder()
        mf.add(5); mf.add(1); mf.add(3)
        mf.median() -> 3.0
        """
        raise NotImplementedError

    def median(self) -> float:
        """Return the median of every number added so far.

        Even count -> average of the two middle values.
        Odd count -> the single middle value.
        Raise `ValueError` if nothing has been added yet.

        mf = MedianFinder(); mf.add(1); mf.add(2)
        mf.median() -> 1.5
        """
        raise NotImplementedError
