# Scenario: a university's course catalog, where some courses require
# others first. Pattern: topological sort via Kahn's algorithm
# (in-degrees + queue) on a directed graph.
# Run: uv run pytest 16-graphs-2 -k ex01


def build_order(n: int, prereqs: list[tuple[int, int]]) -> list[int] | None:
    """Return a valid course order for courses `0..n-1`, or None if no
    valid order exists (the prerequisites form a cycle).

    `prereqs` is a list of `(course, prereq)` pairs: to take `course`
    you must take `prereq` first. There may be zero prereqs for a
    course, and a course with no incoming or outgoing edges may appear
    anywhere in the returned order.

    Use Kahn's algorithm: compute in-degree for every course, seed a
    queue with every course whose in-degree is 0, then repeatedly pop a
    course, append it to the order, and decrement the in-degree of
    everything it unlocks -- pushing newly-zero courses onto the queue.
    If the final order has fewer than `n` courses, a cycle blocked some
    of them -- return None.

    build_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)])
        -> [0, 1, 2, 3] (one valid order; [0, 2, 1, 3] is also valid)
    build_order(2, [(0, 1), (1, 0)]) -> None  (cycle)
    build_order(3, []) -> [0, 1, 2]  (any order of independent courses)

    Target: O(n + e) time, O(n + e) space, where e = len(prereqs).
    """
    raise NotImplementedError


def can_finish(n: int, prereqs: list[tuple[int, int]]) -> bool:
    """Return True if all `n` courses can be completed -- i.e. the
    prerequisite graph has no cycle -- False otherwise.

    can_finish(2, [(1, 0)]) -> True
    can_finish(2, [(0, 1), (1, 0)]) -> False

    Target: O(n + e) time, O(n + e) space.
    """
    raise NotImplementedError
