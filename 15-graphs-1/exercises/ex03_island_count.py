# Scenario: satellite imagery is processed into a 0/1 grid (1 = land,
# 0 = water); a mapping tool needs island counts and sizes. Pattern:
# grid-as-graph, flood fill (DFS or BFS), visited discipline.
# Run: uv run pytest 15-graphs-1 -k ex03


def count_islands(grid: list[list[int]]) -> int:
    """Count the number of islands in `grid`. An island is a maximal
    group of `1` cells connected 4-directionally (up/down/left/right,
    not diagonally). `grid` is non-empty and rectangular.

    Use iterative DFS or BFS (explicit stack/queue) rather than
    recursive DFS — grids in this exercise can be large enough that
    recursion would hit Python's recursion limit (see LESSON.md
    gotchas).

    count_islands([
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]) -> 2

    count_islands([[0, 0], [0, 0]]) -> 0

    Target: O(rows * cols) time, O(rows * cols) space (visited set /
    grid mutation, worst case one giant island).
    """
    raise NotImplementedError


def max_island_area(grid: list[list[int]]) -> int:
    """Return the area (cell count) of the largest island in `grid`
    (0 if there are no islands at all). Same adjacency rule as
    `count_islands`.

    max_island_area([
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]) -> 3   (the top-left island: (0,0),(0,1),(1,0))

    max_island_area([[0, 0], [0, 0]]) -> 0

    Target: O(rows * cols) time, O(rows * cols) space.
    """
    raise NotImplementedError
