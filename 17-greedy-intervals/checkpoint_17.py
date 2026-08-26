# Checkpoint 17 — Conference planner
#
# A conference has many proposed talks; several people each have a
# personal calendar of busy slots; a hallway coffee cart tracks net
# energy (caffeine minus crash) throughout the day. Build four
# planning tools, each a variation on a pattern from this module:
#   - plan_day: sort-by-end interval scheduling (ex06 shape)
#   - rooms_needed: start/end event sweep (ex06 shape)
#   - merge_busy: sort-by-start interval merge (ex05 shape)
#   - coffee_run: Kadane's running-best with bounds (ex01 shape)
#
# Touching intervals (one ends exactly where another begins) are NOT
# overlapping, course-wide — see LESSON.md.
#
# Run: uv run pytest 17-greedy-intervals -k checkpoint_17


def plan_day(talks: list[tuple[str, int, int]]) -> list[str]:
    """`talks` is a list of `(title, start, end)`. One person wants to
    attend as many FULL talks as possible without any two overlapping
    (touching back-to-back talks are both attendable). Return the
    titles of the chosen talks, in the order they'd be attended
    (sorted by end time — the greedy selection order).

    plan_day([("A", 1, 3), ("B", 2, 4), ("C", 3, 6), ("D", 5, 7)]) ->
        ["A", "C"]

    Target: O(n log n) time, O(n) space.
    """
    raise NotImplementedError


def rooms_needed(talks: list[tuple[str, int, int]]) -> int:
    """Return the minimum number of simultaneous rooms needed so every
    talk in `talks` can run (i.e. the maximum number of talks
    overlapping at any single instant). Touching talks (one ends
    exactly when another starts) may share a room.

    rooms_needed([("A", 0, 30), ("B", 5, 10), ("C", 15, 20)]) -> 2

    Target: O(n log n) time, O(n) space. Must stay fast on 100,000+
    talks (see the efficiency test).
    """
    raise NotImplementedError


def merge_busy(calendars: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    """`calendars` is a list of people's calendars; each calendar is a
    list of `(start, end)` busy slots for that person (each person's
    own slots may already overlap each other or not — don't assume
    anything about the input's order or overlap). Flatten every busy
    slot from every calendar together and return the merged,
    sorted-by-start result — the combined "someone is busy" windows.
    Touching slots stay separate (not merged), same rule as
    `merge_intervals` in ex05.

    merge_busy([[(1, 3), (5, 8)], [(2, 4), (9, 10)]]) ->
        [(1, 4), (5, 8), (9, 10)]

    Target: O(n log n) time where n = total slots across all
    calendars, O(n) space.
    """
    raise NotImplementedError


def coffee_run(energy_levels: list[int]) -> tuple[int, int, int]:
    """`energy_levels[i]` is the net caffeine effect (can be negative,
    a crash) during hour `i` of a workday. Return
    `(best_total, start_hour, end_hour)` describing the best
    contiguous stretch of hours to be at peak energy (both indices
    inclusive). `energy_levels` has at least one hour.

    This is Kadane's algorithm in disguise — see ex01.

    coffee_run([3, -1, -2, 5, 2, -4, 3]) -> (7, 0, 4)

    Target: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
