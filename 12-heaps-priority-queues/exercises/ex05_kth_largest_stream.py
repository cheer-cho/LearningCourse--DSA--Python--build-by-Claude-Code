# Scenario: a leaderboard service must answer "what's the kth-highest
# score right now?" after every new score comes in, without re-sorting
# the whole leaderboard each time. Pattern: size-k min-heap kept alive
# across calls (the streaming version of ex03/ex04's top-k inversion).
# Run: uv run pytest 12-heaps-priority-queues -k ex05


class KthLargest:
    """Tracks the kth-largest value seen so far across a stream of
    numbers, using a MIN-heap capped at size `k`.

    Why a min-heap: the kth largest overall is always the SMALLEST
    value currently inside your top-k window -- exactly what a
    size-k min-heap keeps at its root.

    It is guaranteed that `add` is never called before at least `k`
    numbers (counting `initial`) have been seen in total, so the kth
    largest is always well-defined when `add` returns.

    Target complexity: `add` is O(log k) time; O(k) space overall.
    """

    def __init__(self, k: int, initial: list[int]) -> None:
        """Seed the tracker with `k` and a starting list of numbers.

        KthLargest(2, [4, 5, 8, 2]) then .add(3) -> 4
        """
        raise NotImplementedError

    def add(self, val: int) -> int:
        """Add `val` to the stream and return the current kth-largest
        value.

        kl = KthLargest(3, [4, 5, 8, 2])
        kl.add(3)  -> 4   (stream is now [4,5,8,2,3], 3rd largest = 4)
        kl.add(5)  -> 5
        kl.add(10) -> 5
        kl.add(9)  -> 8
        """
        raise NotImplementedError
