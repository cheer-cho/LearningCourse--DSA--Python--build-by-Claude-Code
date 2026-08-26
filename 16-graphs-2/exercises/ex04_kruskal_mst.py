# Scenario: an ISP wants to connect every neighborhood to the network
# for the least total cable cost, given a list of candidate links and
# their prices. Pattern: minimum spanning tree via Kruskal's algorithm
# (sort edges by weight, union-find skips edges that would close a
# cycle).
# Run: uv run pytest 16-graphs-2 -k ex04


def min_connection_cost(n: int, weighted_edges: list[tuple[int, int, int]]) -> int | None:
    """`weighted_edges` is a list of `(u, v, cost)` for an undirected
    graph over nodes `0..n-1`. Return the total cost of a minimum
    spanning tree connecting all `n` nodes, or None if the graph is
    disconnected (no spanning tree exists).

    Sort edges by cost ascending. Walk them in order, using YOUR
    UnionFind -- `from ex02_build_union_find import UnionFind` (this is
    the payoff for building it in ex02): union `u` and `v` if they
    aren't already connected (adds the edge to the MST and its cost to
    the running total), skip the edge if they are (adding it would
    only create a cycle -- never helps a *minimum* spanning tree). Stop
    early once `n - 1` edges have been added. After processing, if
    fewer than `n - 1` edges were added, the graph doesn't have a
    single spanning tree -- return None.

    min_connection_cost(4, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10)])
        -> 6   (skip the 10-cost edge -- it would only close a cycle)
    min_connection_cost(4, [(0, 1, 1), (2, 3, 1)]) -> None  (disconnected)
    min_connection_cost(3, [(0, 1, 5), (0, 1, 2), (1, 2, 1)])
        -> 3   (duplicate edge (0,1): cheaper one wins by sort order)

    Target: O(e log e) time (dominated by the sort), O(n) extra space.
    """
    raise NotImplementedError
