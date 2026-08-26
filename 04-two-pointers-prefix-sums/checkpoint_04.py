# Checkpoint 04 -- Elevation survey
#
# A hiking club logs trail data as plain int lists. Four unrelated
# questions come up about the same kind of data, and together they use
# every pattern from this module: opposite-ends two pointers, in-place
# reader/writer compaction, prefix-sum range queries, and the pivot-
# index trick.
# Run: uv run pytest 04-two-pointers-prefix-sums -k checkpoint

GAP_SENTINEL = -1  # marks a missing/broken sensor reading; real
# elevation readings in this survey are always >= 0.


def flat_pairs(sorted_readings: list[int], target: int) -> list[tuple[int, int]]:
    """Find every pair of waypoints whose elevations sum to `target`.

    `sorted_readings` is sorted ascending and contains DISTINCT
    elevation values. Return every pair of indices `(i, j)` with
    `i < j` such that `sorted_readings[i] + sorted_readings[j] ==
    target`, using an opposite-ends two-pointer scan (O(n), no nested
    loop). Order the pairs by increasing `i`.

    flat_pairs([100, 150, 200, 250, 300], 450) -> [(1, 4), (2, 3)]
    flat_pairs([1, 2, 3], 10) -> []

    Target complexity: O(n) time, O(1) extra space (excluding output).
    """
    raise NotImplementedError


def compact_gaps(readings: list[int]) -> int:
    """Mutate `readings` in place, moving every valid (non-sentinel)
    reading to the front, preserving their original relative order.

    A reading equal to `GAP_SENTINEL` marks a broken sensor and should
    be dropped. Same-direction reader/writer pattern. Returns the count
    of valid readings kept; `readings[:count]` holds them in order
    (the remaining slots are leftovers and don't need any particular
    value).

    readings = [10, GAP_SENTINEL, 12, GAP_SENTINEL, 15]
    compact_gaps(readings) -> 3
    readings[:3] == [10, 12, 15]

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


class RangeGain:
    """Precompute once, then answer "net elevation gain over this
    stretch of the survey" in O(1) per query -- the prefix-sum
    pattern.

    `readings[k]` is the elevation CHANGE recorded during segment `k`
    of the survey (the climb, positive or negative, from waypoint `k`
    to waypoint `k + 1`). `query(i, j)` returns the net gain across
    segments `i..j` inclusive.

    rg = RangeGain([3, -1, 2, -4, 5])
    rg.query(0, 2) -> 4     # 3 + -1 + 2
    rg.query(1, 4) -> 2     # -1 + 2 + -4 + 5

    Target complexity: build O(n) time / O(n) space; query O(1) time.
    """

    def __init__(self, readings: list[int]) -> None:
        raise NotImplementedError

    def query(self, i: int, j: int) -> int:
        raise NotImplementedError


def balanced_checkpoint(readings: list[int]) -> int:
    """Return the leftmost segment index where the total gain of every
    segment before it equals the total gain of every segment after it
    (the segment at that index is excluded from both sides). Return -1
    if no such index exists.

    `readings[k]` is the elevation change of segment `k`, same as in
    `RangeGain`.

    balanced_checkpoint([2, 1, -1, 4, 2, -3]) -> 1
    balanced_checkpoint([1, 2, 3]) -> -1

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
