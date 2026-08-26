# Scenario: a budget traveler wants the cheapest flight route between
# two cities, but is only willing to make at most k layovers.
# Pattern: Bellman-Ford-style edge relaxation, bounded to k+1 rounds --
# Dijkstra's "always take the globally cheapest frontier" greedy choice
# can lock in a path that uses too many stops before a cheaper,
# stop-limited alternative is ever considered.
# Run: uv run pytest 16-graphs-2 -k ex07


def cheapest_within_k_stops(
    n: int, flights: list[tuple[int, int, int]], src: int, dst: int, k: int
) -> int | None:
    """`flights` is a list of `(u, v, price)` DIRECTED edges over
    cities `0..n-1`. Return the cheapest total price from `src` to
    `dst` using AT MOST `k` stops (layovers) -- i.e. at most `k + 1`
    edges/flights. Return None if no such route exists.

    Start with `dist = [inf] * n` except `dist[src] = 0`. Repeat
    `k + 1` times: make a COPY of `dist` (call it `dist_next`), and for
    every edge `(u, v, price)`, if `dist[u] + price < dist_next[v]`,
    update `dist_next[v]`. Replace `dist` with `dist_next` after each
    full round. Each round adds at most one more edge to any path,
    which is exactly what caps the route at `k + 1` edges.

    Why plain Dijkstra fails here: Dijkstra finalizes the globally
    cheapest distance to each node as soon as it's popped, with no
    notion of "how many edges did it take to get here." A route that's
    cheaper overall but uses more than `k` stops would get finalized
    first and shadow a valid, stop-limited (if pricier) alternative --
    Dijkstra has no way to also track "and did it fit in the stop
    budget?" for every competing path.

    Why the copy matters: relaxing edges in place within one round
    would let a single round chain multiple edges together (`u -> v`
    then immediately `v -> w` using the JUST-updated `dist[v]`),
    silently allowing more hops than the round count intends.

    cheapest_within_k_stops(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 1)
        -> 200   (0->1->2, exactly 1 stop, fits the budget)
    cheapest_within_k_stops(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 0)
        -> 500   (0 stops means 0->1->2 is disallowed; take the direct flight)
    cheapest_within_k_stops(2, [], 0, 1, 5) -> None

    Target: O(k * e) time, O(n) space.
    """
    raise NotImplementedError
