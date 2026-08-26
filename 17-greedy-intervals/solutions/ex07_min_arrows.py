def min_arrows(balloon_ranges: list[list[int]]) -> int:
    # Pattern: sort-by-end scheduling, point-containment variant.
    # An arrow at the current balloon's end position pops every later
    # balloon whose start is <= that position (touching counts as
    # hit — the arrow is a point, inclusive at both range ends).
    # Complexity: O(n log n) time (the sort), O(1) extra space.
    if not balloon_ranges:
        return 0

    balloons_sorted = sorted(balloon_ranges, key=lambda balloon: balloon[1])
    arrows = 1
    arrow_position = balloons_sorted[0][1]

    for start, end in balloons_sorted[1:]:
        if start > arrow_position:
            arrows += 1
            arrow_position = end

    return arrows
