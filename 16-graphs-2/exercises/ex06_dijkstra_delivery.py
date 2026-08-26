# Scenario: a delivery hub needs to know how long a package takes to
# reach every warehouse in a road network with different travel times
# per road, and the exact route to one specific warehouse.
# Pattern: Dijkstra's algorithm -- BFS's weighted upgrade, always
# expanding the cheapest known frontier via a min-heap.
# Run: uv run pytest 16-graphs-2 -k ex06


def delivery_times(n: int, edges: list[tuple[int, int, int]], source: int) -> dict[int, int]:
    """`edges` is a list of `(u, v, time)` DIRECTED edges (u -> v takes
    `time`) over nodes `0..n-1`. Return a dict mapping every node to
    its shortest travel time from `source`; unreachable nodes map to
    -1. `source` itself maps to 0.

    Min-heap of `(distance, node)`, seeded with `(0, source)`. Pop the
    cheapest entry; if its distance is worse than the best already
    recorded for that node, it's a STALE entry left over from an
    earlier, since-improved push -- skip it (lazy-deletion pattern,
    cheaper than a heap that supports decrease-key). Otherwise relax
    every outgoing edge: if going through this node beats the
    neighbor's current best, push the improved distance.

    delivery_times(3, [(0, 1, 4), (0, 2, 1), (2, 1, 1)], 0)
        -> {0: 0, 1: 2, 2: 1}   (0->2->1 costs 2, beats 0->1 direct at 4)
    delivery_times(3, [(0, 1, 5)], 0) -> {0: 0, 1: 5, 2: -1}

    Target: O(e log e) time, O(n + e) space.
    """
    raise NotImplementedError


def shortest_route(n: int, edges: list[tuple[int, int, int]], a: int, b: int) -> list[int] | None:
    """Same graph shape as `delivery_times`. Return the actual shortest
    path from `a` to `b` as a list of nodes `[a, ..., b]`, or None if
    `b` is unreachable from `a`. If `a == b`, return `[a]`.

    Run Dijkstra from `a`, but track a `parent` map alongside distances
    (whenever you relax an edge into an improved distance, record where
    it came from). Once done, walk `parent` backward from `b` to `a`
    and reverse the result.

    shortest_route(3, [(0, 1, 4), (0, 2, 1), (2, 1, 1)], 0, 1)
        -> [0, 2, 1]
    shortest_route(2, [], 0, 1) -> None

    Target: O(e log e) time, O(n + e) space.
    """
    raise NotImplementedError
