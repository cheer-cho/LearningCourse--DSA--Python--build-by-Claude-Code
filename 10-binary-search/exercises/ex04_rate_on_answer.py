# Scenario: an overnight batch cluster must clear `piles` of queued jobs
# (one pile per machine-hour, one pile at a time) within `h` hours. You
# choose the processing rate (jobs/hour) once, for every pile. Pattern:
# search on the answer — binary search over a numeric range using a
# monotone feasibility predicate `can(rate)`, not over the array itself.
# Run: uv run pytest 10-binary-search -k ex04


def min_rate(piles: list[int], h: int) -> int:
    """Return the minimum integer processing rate `r` (jobs/hour) such
    that a machine working through `piles` one pile at a time (each pile
    takes `ceil(pile / r)` hours at rate `r`) finishes ALL piles within
    `h` hours total.

    `piles` has at least one pile, every pile size is >= 1, and
    `h >= len(piles)` (so a feasible rate always exists).

    The predicate `can(r)` = "total hours at rate r is <= h" is monotone:
    raising `r` never increases the hours needed. Binary-search the
    smallest `r` in `[1, max(piles)]` with `can(r)` true.

    min_rate([3, 6, 7, 11], 8) -> 4
    min_rate([30, 11, 23, 4, 20], 5) -> 30
    min_rate([1, 1, 1], 3) -> 1

    Target: O(n log(max(piles))) time, O(1) space.
    """
    raise NotImplementedError
