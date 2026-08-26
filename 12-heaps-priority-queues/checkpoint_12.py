# Checkpoint 12 — ER triage
#
# An emergency room serves patients by SEVERITY first (higher number =
# more critical), and by arrival order (FIFO) among patients who tie
# on severity. This combines everything from the module: a priority
# queue for the ordering, and a tuple key to pin the tie-break so two
# patients who arrive at the same severity never get compared to each
# other in an undefined way.
# Run: uv run pytest 12-heaps-priority-queues -k checkpoint


class TriageQueue:
    """A priority queue of waiting patients.

    Serves the highest-severity patient first; among patients with
    equal severity, serves whoever arrived first (FIFO). Build the
    heap key as `(-severity, timestamp, ...)` -- negate severity so a
    MIN-heap (`heapq`) behaves like a max-heap on severity, and use
    `timestamp` as the tie-break so equal severities never fall
    through to comparing anything else.

    Target complexity: `arrive` O(log n), `next_patient` O(log n),
    `waiting_count` O(1).
    """

    def __init__(self) -> None:
        """Start with an empty waiting room."""
        raise NotImplementedError

    def arrive(self, name: str, severity: int, timestamp: float) -> None:
        """Register a new patient. Higher `severity` is more urgent.
        `timestamp` only needs to be comparable and increasing with
        real arrival order (e.g. a counter or a Unix timestamp).

        q = TriageQueue()
        q.arrive("Alice", severity=3, timestamp=1.0)
        """
        raise NotImplementedError

    def next_patient(self) -> str:
        """Remove and return the name of the next patient to be seen:
        highest severity first, earliest `timestamp` breaks ties.
        Raise `IndexError` if no one is waiting.

        q = TriageQueue()
        q.arrive("Alice", severity=2, timestamp=1.0)
        q.arrive("Bob", severity=5, timestamp=2.0)
        q.next_patient() -> "Bob"     (higher severity)
        q.next_patient() -> "Alice"
        """
        raise NotImplementedError

    def waiting_count(self) -> int:
        """Return how many patients are currently waiting.

        q = TriageQueue()
        q.arrive("Alice", severity=1, timestamp=1.0)
        q.waiting_count() -> 1
        """
        raise NotImplementedError


def k_most_urgent(records: list[tuple[str, int, float]], k: int) -> list[str]:
    """Given `records` of `(name, severity, timestamp)` (unordered,
    not yet in a TriageQueue), return the names of the `k` most urgent
    patients, MOST urgent first -- same ordering rule as `TriageQueue`:
    higher severity first, earlier timestamp breaks ties.

    `k` is between 1 and `len(records)`.

    k_most_urgent(
        [("Alice", 2, 1.0), ("Bob", 5, 2.0), ("Cy", 5, 0.5)], 2
    ) -> ["Cy", "Bob"]   (both severity 5, Cy arrived first)

    Target complexity: O(n log k) time, O(k) extra space.
    """
    raise NotImplementedError
