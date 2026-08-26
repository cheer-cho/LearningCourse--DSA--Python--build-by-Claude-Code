# Scenario: a room-booking system needs to collapse overlapping
# reservation windows, and insert a new reservation into an
# already-sorted, already-merged schedule. Pattern: sort-by-start
# interval merging.
# Run: uv run pytest 17-greedy-intervals -k ex05


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Each interval is `[start, end]` (both inclusive-style bounds on
    a timeline; `start <= end`). Merge every pair of OVERLAPPING
    intervals and return the resulting list, sorted by start.
    Touching intervals (one ends exactly where another begins, e.g.
    `[1, 2]` and `[2, 3]`) do NOT count as overlapping and stay
    separate in the output.

    Sort by start first. Walk the sorted list keeping a "current"
    merged interval; if the next interval's start is STRICTLY less
    than the current interval's end, they overlap — extend the
    current interval's end to the larger of the two. Otherwise close
    the current interval out and start a new one.

    merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) ->
        [[1, 6], [8, 10], [15, 18]]
    merge_intervals([[1, 2], [2, 3]]) -> [[1, 2], [2, 3]]   (touching)
    merge_intervals([]) -> []

    Target: O(n log n) time (the sort), O(n) space for the output.
    """
    raise NotImplementedError


def insert_interval(sorted_intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    """`sorted_intervals` is already sorted by start AND already fully
    merged (no two overlap, per the same touching-is-not-overlapping
    rule as `merge_intervals`). Insert `new` (a single `[start, end]`
    interval, not necessarily fitting the sort order) and return the
    resulting fully-merged, sorted list. Do NOT re-sort from scratch —
    a linear three-phase scan is the point of this exercise.

    Three phases over `sorted_intervals`, in order: (1) intervals
    entirely before `new` (their end is strictly less than `new`'s
    start) — copy as-is; (2) intervals overlapping `new` — fold each
    one into `new`'s bounds (`new`'s start/end absorb them) instead of
    copying; (3) intervals entirely after `new` — copy as-is. `new`
    (possibly grown by phase 2) is emitted between phase 1 and phase 3.

    insert_interval([[1, 3], [6, 9]], [2, 5]) -> [[1, 5], [6, 9]]
    insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]) ->
        [[1, 2], [3, 10], [12, 16]]
    insert_interval([], [5, 7]) -> [[5, 7]]

    Target: O(n) time, O(n) space for the output.
    """
    raise NotImplementedError
