# Scenario: balloons are strung along a wall, each spanning a
# horizontal range; an arrow shot straight up at position x pops every
# balloon whose range contains x. Pattern: sort-by-end interval
# scheduling, point-containment variant.
# Run: uv run pytest 17-greedy-intervals -k ex07


def min_arrows(balloon_ranges: list[list[int]]) -> int:
    """Each balloon is `[start, end]`, the horizontal range it spans
    (inclusive). An arrow fired at position `x` pops every balloon
    with `start <= x <= end`. Return the minimum number of arrows
    needed to pop every balloon. Unlike `merge_intervals`/
    `max_non_overlapping`, touching balloons (`[1, 2]` and `[2, 3]`)
    DO count as hit by one shared arrow at position `2` — an arrow is
    a POINT, and `2` lies inside both ranges. (This is the deliberate
    contrast pinned in LESSON.md: range-overlap excludes touching,
    point-containment includes it.)

    Sort by end. Shoot the first arrow at the first balloon's end
    position. Any later balloon whose start is <= that arrow position
    is already popped — skip it. The moment a balloon's start is past
    the current arrow, it needs a new arrow, fired at THAT balloon's
    end.

    min_arrows([[1, 6], [2, 8], [7, 12], [10, 16]]) -> 2
    min_arrows([[1, 2], [2, 3], [3, 4]]) -> 2   (arrow at x=2 pops
        [1,2] and [2,3] since both contain 2; [3,4] needs a second
        arrow — it does NOT contain 2)
    min_arrows([]) -> 0

    Target: O(n log n) time (the sort), O(1) extra space.
    """
    raise NotImplementedError
