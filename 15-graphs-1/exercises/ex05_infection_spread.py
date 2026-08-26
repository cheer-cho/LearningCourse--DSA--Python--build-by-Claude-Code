# Scenario: a datacenter security tool models malware spreading between
# adjacent servers on a rack grid, and a robot needs the shortest path
# out of a maze. Pattern: multi-source BFS; single-source BFS distance.
# Run: uv run pytest 15-graphs-1 -k ex05


def minutes_to_infect(grid: list[list[int]]) -> int:
    """`grid` cells: `0` = empty rack slot, `1` = healthy server,
    `2` = infected server. Every minute, infection spreads from each
    infected server to its 4-directional healthy-server neighbors
    (all infections spread simultaneously, one step per minute — NOT
    one server infected at a time). Return the number of minutes for
    every healthy server to become infected, or `-1` if some healthy
    server can never be reached. If there are no healthy servers to
    begin with, return `0`.

    Seed a BFS queue with ALL initially-infected servers at distance 0
    (multi-source BFS) rather than running separate BFS per source —
    the simultaneous spread IS the multi-source wavefront.

    minutes_to_infect([
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]) -> 4

    minutes_to_infect([[2, 1], [0, 1]]) -> 2
        ((0,1) is infected at minute 1; (1,1) is only reachable
        through (0,1), so it turns at minute 2; (1,0) is empty and
        blocks spread — it's never infected and never passes the
        infection along)

    minutes_to_infect([[2, 0, 1]]) -> -1
        (the healthy server at (0,2) is separated from (0,0) by an
        empty slot at (0,1) — empty slots block spread, they don't
        relay it, so (0,2) can never be reached)

    minutes_to_infect([[0, 0], [0, 0]]) -> 0   (no healthy servers)

    Target: O(rows * cols) time, O(rows * cols) space.
    """
    raise NotImplementedError


def shortest_exit(maze: list[list[int]], start: tuple[int, int]) -> int:
    """`maze` cells: `0` = open, `1` = wall. An "exit" is any OPEN cell
    on the maze's border (row 0, last row, column 0, or last column).
    Return the fewest 4-directional moves from `start` to reach ANY
    exit cell (0 if `start` itself is already an exit), or `-1` if no
    exit is reachable. `start` is guaranteed to be an open cell.

    shortest_exit([
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    ], (1, 1)) -> -1
        (walled in on all sides, no border cell reachable)

    shortest_exit([
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ], (1, 1)) -> 1
        ((1, 2) is open and on the border (last column) — one move)

    shortest_exit([[0]], (0, 0)) -> 0   (start is itself a border cell)

    Target: O(rows * cols) time, O(rows * cols) space — plain BFS
    distance from `start`, stopping at the first border cell dequeued.
    """
    raise NotImplementedError
