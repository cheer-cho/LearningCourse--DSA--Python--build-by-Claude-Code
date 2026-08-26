# Checkpoint 16 -- City infrastructure
#
# A city planning department is juggling four graph problems at once:
# in what ORDER must construction projects run given their
# dependencies, what's the CHEAPEST way to wire every district into
# the power grid, how FAST does a signal reach every district from the
# hub, and -- as cable gets built incrementally -- are two districts
# on the SAME network yet? One tool per algorithm from this module:
#   - project_order: topological sort (Kahn's algorithm)
#   - cheapest_grid: minimum spanning tree (Kruskal, via your UnionFind)
#   - fastest_signal: Dijkstra's shortest path
#   - same_network: union-find batch queries
#
# Run: uv run pytest 16-graphs-2 -k checkpoint_16


def project_order(projects: list[str], deps: list[tuple[str, str]]) -> list[str] | None:
    """`projects` are unique project names. `deps` is a list of
    `(project, prereq)` pairs: `project` cannot start until `prereq` is
    finished. Return a valid build order (every project appears
    exactly once, every prereq before its dependent), or None if the
    dependencies contain a cycle.

    Same shape as ex01's `build_order`, but over names instead of
    `0..n-1` indices -- map each name to an index, run Kahn's
    algorithm, then map the resulting index order back to names.

    project_order(["wiring", "foundation", "roof"],
                   [("wiring", "foundation"), ("roof", "wiring")])
        -> ["foundation", "wiring", "roof"]
    project_order(["a", "b"], [("a", "b"), ("b", "a")]) -> None

    Target: O(n + e) time, O(n + e) space.
    """
    raise NotImplementedError


def cheapest_grid(n: int, routes: list[tuple[int, int, int]]) -> int | None:
    """`routes` is a list of `(district_a, district_b, cost)` candidate
    cable routes over districts `0..n-1`. Return the total cost of the
    cheapest way to connect every district (a minimum spanning tree),
    or None if it's impossible to connect them all.

    Same shape as ex04's `min_connection_cost` -- sort by cost, use
    YOUR `UnionFind` (imported above) to skip any route that would
    only close a cycle.

    cheapest_grid(3, [(0, 1, 4), (1, 2, 4), (0, 2, 9)]) -> 8
    cheapest_grid(3, [(0, 1, 4)]) -> None  (district 2 unreachable)

    Target: O(e log e) time, O(n) extra space.
    """
    raise NotImplementedError


def fastest_signal(n: int, routes: list[tuple[int, int, int]], hub: int) -> dict[int, int]:
    """`routes` is the same `(a, b, cost)` list as `cheapest_grid`, but
    here `cost` means signal travel time and every route works in
    BOTH directions (undirected). Return a dict mapping every district
    to its fastest signal time from `hub`; unreachable districts map
    to -1. `hub` maps to 0.

    Same shape as ex06's `delivery_times`, but build an undirected
    adjacency list (push each route into BOTH endpoints' lists) before
    running Dijkstra with a lazy-deletion min-heap.

    fastest_signal(3, [(0, 1, 4), (1, 2, 4), (0, 2, 9)], 0)
        -> {0: 0, 1: 4, 2: 8}

    Target: O(e log e) time, O(n + e) space.
    """
    raise NotImplementedError


def same_network(
    n: int, built_routes: list[tuple[int, int]], queries: list[tuple[int, int]]
) -> list[bool]:
    """`built_routes` is a list of `(a, b)` cable routes ALREADY
    installed between districts `0..n-1` (unweighted -- built or not).
    `queries` is a list of `(a, b)` pairs asking "are these two
    districts on the same network yet?" Return a list of booleans, one
    per query, in query order.

    Build a `UnionFind(n)`, union every built route once, then answer
    each query with `connected` -- this is the entire point of having
    built union-find from scratch in ex02: O(alpha(n)) per query
    instead of a fresh BFS/DFS per query.

    same_network(4, [(0, 1), (1, 2)], [(0, 2), (0, 3)]) -> [True, False]

    Target: O((n + e + q) * alpha(n)) time, O(n) extra space, where
    e = len(built_routes), q = len(queries).
    """
    raise NotImplementedError
