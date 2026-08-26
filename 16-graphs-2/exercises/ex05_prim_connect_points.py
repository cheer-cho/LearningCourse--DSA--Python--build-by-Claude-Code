# Scenario: an electrician wants the cheapest way to wire together a
# set of rooftop solar panels, where the cost between any two panels is
# their Manhattan distance. Pattern: minimum spanning tree via Prim's
# algorithm (grow one tree, always adding the cheapest edge out of it,
# using a min-heap as the frontier).
# Run: uv run pytest 16-graphs-2 -k ex05


def min_cost_connect_points(points: list[tuple[int, int]]) -> int:
    """`points` are 2D coordinates, at least one point. Every pair of
    points is implicitly connected by an edge whose weight is their
    Manhattan distance (`|x1 - x2| + |y1 - y2|`) -- a complete graph
    with `n * (n - 1) / 2` edges that is never built explicitly. Return
    the total cost of a minimum spanning tree connecting all points.

    Prim's algorithm: start from point 0, keep a min-heap of
    `(distance, point_index)` edges reaching OUT of the current tree
    into the rest of the graph, and a `visited` set. Repeatedly pop the
    cheapest edge; if it lands on an already-visited point, discard it
    (lazy deletion -- cheaper than removing it from the heap up
    front); otherwise mark the point visited, add its cost to the
    total, and push a fresh edge to every still-unvisited point from
    it. Stop once every point is visited.

    min_cost_connect_points([(0, 0), (2, 2), (3, 10), (5, 2), (7, 0)])
        -> 20
    min_cost_connect_points([(0, 0)]) -> 0

    Why Prim here rather than Kruskal (ex04): the graph is DENSE
    (n^2/2 edges) and implicit. Kruskal needs every edge materialized
    and sorted up front -- O(n^2) memory and O(n^2 log n) time before
    the algorithm even starts choosing edges. Prim only ever computes
    distances from points already IN the tree to points not yet in
    it, discovering edges on demand instead of all at once.

    Target: O(n^2 log n) time, O(n^2) heap space worst case (bounded by
    lazy-skipping stale entries rather than removing them).
    """
    raise NotImplementedError
