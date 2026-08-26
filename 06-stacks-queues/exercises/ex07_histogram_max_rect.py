# Scenario: a skyline-rendering tool needs the single largest rectangle
# that fits under a bar chart's silhouette. Concepts: monotonic stack of
# INDEXES, "for each bar, how far can it stretch before hitting
# something shorter on either side?" Classic hard pattern.
# Run: uv run pytest 06-stacks-queues -k ex07


def largest_rectangle(heights: list[int]) -> int:
    """Return the area of the largest rectangle that fits under the
    histogram described by `heights` (each bar has width 1).

    Key insight: picture the rectangle whose height equals `heights[i]`
    for some bar `i` — the SHORTEST bar in that rectangle. Its width is
    the distance between the nearest strictly-shorter bar to the left
    and the nearest strictly-shorter bar to the right, because every
    bar strictly between those two boundaries is >= heights[i], so a
    rectangle of that height spans the whole gap.

    A monotonic (non-decreasing) stack of indexes finds both boundaries
    in one left-to-right pass: when the incoming bar is shorter than
    the bar on top of the stack, the top bar's RIGHT boundary is the
    incoming bar's index — pop it and compute its area right then (its
    left boundary is whatever is now exposed on the stack below it). A
    sentinel bar of height 0, conceptually appended past the end,
    forces every bar still on the stack to be popped and closed out.

    largest_rectangle([2, 1, 5, 6, 2, 3]) -> 10   (bars of height 5 and 6)
    largest_rectangle([2, 4]) -> 4
    largest_rectangle([1, 1, 1, 1]) -> 4
    largest_rectangle([]) -> 0

    Target complexity: O(n) time, O(n) space — each index is pushed and
    popped at most once.
    """
    raise NotImplementedError
