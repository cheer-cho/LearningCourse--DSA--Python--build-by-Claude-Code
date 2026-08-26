# Scenario: an image editor's "paint bucket" tool, and a board game's
# "capture surrounded territory" rule. Pattern: grid-as-graph flood
# fill; the second function needs the "invert the question" trick.
# Run: uv run pytest 15-graphs-1 -k ex04


def flood_fill(image: list[list[int]], r: int, c: int, color: int) -> list[list[int]]:
    """Classic paint-bucket fill: starting at `(r, c)`, change every
    cell 4-directionally connected to `(r, c)` that shares
    `image[r][c]`'s ORIGINAL color to `color`. Return the modified
    grid (mutating and returning `image` in place is fine).

    If `image[r][c]` already equals `color`, return `image` unchanged
    (an infinite-loop trap otherwise: filling a region with the color
    it already is would keep "discovering" already-correct neighbors
    forever without a base-case check).

    flood_fill([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ], 0, 0, 2) -> [
        [2, 2, 0],
        [2, 2, 0],
        [0, 0, 1],
    ]

    Target: O(rows * cols) time, O(rows * cols) space worst case.
    """
    raise NotImplementedError


def capture_regions(board: list[list[str]]) -> list[list[str]]:
    """Board of `'X'` and `'O'` characters. Flip every `'O'` to `'X'`
    UNLESS that `'O'` is connected (4-directionally, through other
    `'O'`s) to the board's border — border-connected regions survive
    uncaptured. Return the modified board (mutating and returning
    `board` in place is fine).

    The insight: instead of checking "is this region surrounded?"
    (hard to test directly — you'd have to trace every region's full
    boundary), INVERT the question: find every 'O' reachable from the
    border first (those survive), then flip everything else. Anything
    not reachable from the border is, by definition, fully enclosed.

    capture_regions([
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]) -> [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    (the O at (3,1) touches the border directly, so it survives; the
    other two O's are fully enclosed and get captured)

    Target: O(rows * cols) time, O(rows * cols) space.
    """
    raise NotImplementedError
