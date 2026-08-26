# Scenario: timed set 3 of 3 — FOUR independent HARD problems, fresh
# scenarios, no pattern labels attached. Restate, brute force, name a
# pattern + cue, THEN code. Timebox ~40 min each. Efficiency tests are
# mandatory for this set — a naive approach must be infeasible.
# Run: uv run pytest 22-capstone-interview-sets -k ex03


def max_survival_value(weights: list[int], values: list[int], capacity: int) -> int:
    """A summit-bound hiker is packing a single backpack. Each
    candidate gear item `i` has a `weight` and a survival `value`;
    each item can be packed AT MOST once. Choose a subset of items
    whose total weight fits within `capacity`, maximizing total value.

    Params:
        weights: weight of each item, weights[i] >= 0.
        values: survival value of each item, same length as weights.
        capacity: max total weight the pack can hold, capacity >= 0.
    Returns:
        the maximum achievable total value.

    max_survival_value([1, 3, 4, 5], [1, 4, 5, 7], 7) -> 9
    max_survival_value([2, 2, 2], [3, 3, 3], 1) -> 0

    Target complexity: O(n * capacity) time, O(capacity) space.
    """
    raise NotImplementedError


def cheapest_delivery_with_stops(
    num_hubs: int,
    routes: list[tuple[int, int, int]],
    src: int,
    dst: int,
    max_stops: int,
) -> int:
    """A courier network has `num_hubs` hubs (0..num_hubs-1) connected
    by one-way `routes` of `(from_hub, to_hub, cost)`. Find the
    cheapest total cost to deliver a package from `src` to `dst` using
    AT MOST `max_stops` intermediate transfer hubs (so at most
    `max_stops + 1` route legs).

    Params:
        num_hubs: number of hubs.
        routes: directed edges (from_hub, to_hub, cost), cost >= 0.
        src: starting hub.
        dst: destination hub.
        max_stops: max intermediate hubs allowed, max_stops >= 0.
    Returns:
        the cheapest total cost within the stop limit, or -1 if
        unreachable within that limit.

    cheapest_delivery_with_stops(
        4, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 1
    ) -> 200
    cheapest_delivery_with_stops(
        4, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 0
    ) -> 500
    cheapest_delivery_with_stops(2, [], 0, 1, 5) -> -1

    Target complexity: O(max_stops * len(routes)) time, O(num_hubs) space.
    """
    raise NotImplementedError


class LatencyMedianTracker:
    """A live esports broadcast tracks player-to-server latency (ms)
    as measurements stream in, and reports the running median after
    every measurement.

    Target complexity: `add` O(log n), `median` O(1).
    """

    def __init__(self) -> None:
        """Start with no measurements recorded."""
        raise NotImplementedError

    def add(self, value: float) -> None:
        """Record a new latency measurement.

        t = LatencyMedianTracker()
        t.add(5); t.add(2); t.add(8)
        """
        raise NotImplementedError

    def median(self) -> float:
        """Return the median of all measurements recorded so far.
        For an even count, return the average of the two middle
        values. Raise `ValueError` if no measurements have been added.

        t = LatencyMedianTracker()
        t.add(5); t.median() -> 5
        t.add(2); t.median() -> 3.5
        t.add(8); t.median() -> 5
        """
        raise NotImplementedError


def find_signature_occurrences(log: str, signature: str) -> list[int]:
    """A security tool scans a huge log string for every occurrence
    (including overlapping ones) of a suspicious `signature`
    substring.

    Params:
        log: the text to scan.
        signature: non-empty substring to find, len(signature) >= 1.
    Returns:
        every 0-based start index where `signature` occurs in `log`,
        in ascending order (empty list if it never occurs).

    find_signature_occurrences("abcabcabc", "abc") -> [0, 3, 6]
    find_signature_occurrences("aaaaa", "aa") -> [0, 1, 2, 3]
    find_signature_occurrences("hello", "xyz") -> []

    Target complexity: O(len(log) + len(signature)) time,
    O(len(signature)) space.
    """
    raise NotImplementedError
