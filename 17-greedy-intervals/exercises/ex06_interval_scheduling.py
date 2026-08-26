# Scenario: a single conference room has many booking requests, and
# the venue wants to know both the biggest non-overlapping subset it
# can accept and how many rooms it would need to accept ALL of them.
# Pattern: sort-by-end interval scheduling (the exchange-argument
# showcase for this module) plus a start/end event sweep.
# Run: uv run pytest 17-greedy-intervals -k ex06


def max_non_overlapping(intervals: list[list[int]]) -> int:
    """Each interval is `[start, end]`. Return the maximum number of
    intervals you can select such that no two selected intervals
    overlap. Touching intervals (one ends exactly where another
    begins) do NOT overlap and may both be selected.

    Sort by END time. Greedily select the next interval whose start is
    >= the end of the last selected interval. The exchange argument:
    among any set of intervals available at a given point, the one
    ending soonest leaves the most room for everything scheduled
    after it, so it can always safely be the next pick — see
    LESSON.md for the full argument.

    max_non_overlapping([[1, 2], [2, 3], [3, 4], [1, 4]]) -> 3
        (picks [1,2], [2,3], [3,4] — all touching, none overlapping;
        [1,4] is skipped since it overlaps every one of them)
    max_non_overlapping([]) -> 0

    Target: O(n log n) time (the sort), O(1) extra space.
    """
    raise NotImplementedError


def min_removals(intervals: list[list[int]]) -> int:
    """Return the minimum number of intervals to remove so that none
    of the remaining intervals overlap (same touching rule as
    `max_non_overlapping`). This is exactly `n - max_non_overlapping`
    — whatever isn't kept in the best non-overlapping subset must be
    removed, and keeping fewer than the maximum only forces MORE
    removals.

    min_removals([[1, 2], [2, 3], [3, 4], [1, 3]]) -> 1
    min_removals([[1, 2], [1, 2], [1, 2]]) -> 2
    min_removals([]) -> 0

    Target: O(n log n) time, O(1) extra space.
    """
    raise NotImplementedError


def can_attend_all(intervals: list[list[int]]) -> bool:
    """Return whether one person could attend every interval in
    `intervals` in full — i.e. whether NO two intervals overlap.
    Touching intervals (`[1,2]` then `[2,3]`) are attendable
    back-to-back and do not block this.

    Sort by start; if any interval's start is strictly less than the
    previous interval's end, that's an overlap.

    can_attend_all([[1, 2], [2, 3], [3, 4]]) -> True
    can_attend_all([[1, 3], [2, 4]]) -> False
    can_attend_all([]) -> True

    Target: O(n log n) time, O(1) extra space.
    """
    raise NotImplementedError


def min_rooms(intervals: list[list[int]]) -> int:
    """Return the minimum number of rooms needed to hold every
    interval in `intervals` simultaneously bookable (i.e. the maximum
    number of intervals overlapping at any single instant). Touching
    intervals (one ends exactly when another starts) do NOT need
    separate rooms — the room that just freed up may be reused
    immediately.

    Start/end event sweep: turn every interval into a `(+1, start)`
    and a `(-1, end)` event, sort all events by time, and — CRITICAL —
    process end events before start events when times tie (that's
    what makes touching intervals share a room instead of needing two).
    Walk the sorted events keeping a running count and its maximum. A
    two-heap (or heap-of-end-times) approach is also acceptable if you
    prefer that shape.

    min_rooms([[0, 30], [5, 10], [15, 20]]) -> 2
    min_rooms([[1, 2], [2, 3]]) -> 1     (touching: reuse the room)
    min_rooms([]) -> 0

    Target: O(n log n) time, O(n) space. Must stay fast on 100,000+
    intervals (see the efficiency test).
    """
    raise NotImplementedError
