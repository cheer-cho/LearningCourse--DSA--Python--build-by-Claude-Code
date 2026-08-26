# Scenario: choosing two support pillars along a coastline (given their
# heights) to maximize the rectangular pool of water they can hold
# between them. Pattern: two pointers, opposite ends, exchange
# argument.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex05


def max_container(heights: list[int]) -> int:
    """Return the most water two pillars can hold between them.

    `heights[i]` is the pillar height at position `i`. Choosing pillars
    `i < j` holds `min(heights[i], heights[j]) * (j - i)` water (the
    shorter pillar caps how high the water can rise; the gap between
    them is the width). Return the maximum over every possible pair.

    WHY moving the shorter pointer is safe: start `left` and `right` at
    the two ends (the widest possible container) and always move the
    pointer at the SHORTER pillar inward. Keeping the shorter pillar in
    place and moving the other one can only shrink the width while the
    bottleneck height stays capped by that same short pillar (or gets
    worse if the new pillar is even shorter) — so it can never beat the
    current area. Moving the shorter pillar is the only move that has
    any chance of finding a taller wall and a bigger area. Every pair
    that gets skipped this way is provably no better than one already
    seen.

    max_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    max_container([1, 1]) -> 1

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
