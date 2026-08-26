# Scenario: timed set 2 of 3 — SIX independent MEDIUM problems, fresh
# scenarios, no pattern labels attached. Restate, brute force, name a
# pattern + cue, THEN code. Timebox ~25 min each.
# Run: uv run pytest 22-capstone-interview-sets -k ex02


def longest_run_at_most_k_genres(genres: list[str], k: int) -> int:
    """A DJ set's playlist log records one genre tag per track played,
    in play order. Find the length of the longest contiguous run of
    tracks that contains AT MOST `k` distinct genres.

    Params:
        genres: genre tag per track, in play order.
        k: max distinct genres allowed in the run, k >= 0.
    Returns:
        length of the longest such contiguous run (0 if k == 0 or
        genres is empty).

    longest_run_at_most_k_genres(
        ["house", "house", "techno", "trance", "house"], 2
    ) -> 3   (the run ["house", "house", "techno"])
    longest_run_at_most_k_genres(["a", "b", "c"], 1) -> 1

    Target complexity: O(n) time, O(k) space.
    """
    raise NotImplementedError


def buildings_until_taller(heights: list[int]) -> list[int]:
    """A city skyline is given left to right as building heights. For
    each building, find how many buildings ahead (to the right) you
    must look until one is STRICTLY taller. If none is taller, use 0.

    Params:
        heights: building heights, left to right.
    Returns:
        for each index i, the number of steps to the first j > i with
        heights[j] > heights[i], or 0 if no such j exists.

    buildings_until_taller([3, 1, 4, 2, 5]) -> [2, 1, 2, 1, 0]
    buildings_until_taller([5, 4, 3]) -> [0, 0, 0]

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def top_k_frequent_skus(scans: list[str], k: int) -> list[str]:
    """A warehouse scanner logs the SKU scanned each time an item
    leaves the shelf. Return the `k` most frequently scanned SKUs,
    ordered by frequency descending; ties broken by SKU ascending.

    Params:
        scans: SKU string logged once per scan.
        k: how many top SKUs to return, 1 <= k <= number of distinct SKUs.
    Returns:
        list of k SKU strings, most frequent first.

    top_k_frequent_skus(["A", "B", "A", "C", "B", "A"], 2) -> ["A", "B"]
    top_k_frequent_skus(["X", "Y", "Z"], 2) -> ["X", "Y"]

    Target complexity: O(n log k) time, O(n) space.
    """
    raise NotImplementedError


def station_run_order(
    num_stations: int, prerequisites: list[tuple[int, int]]
) -> list[int] | None:
    """An assembly line has `num_stations` stations, labeled
    0..num_stations-1. Each pair `(a, b)` in `prerequisites` means
    station `a` cannot run until station `b` has run. Find a valid run
    order for ALL stations, or None if the prerequisites are
    contradictory (a cycle).

    When more than one station is ready to run at the same time, run
    the LOWEST-numbered one first (for a deterministic answer).

    Params:
        num_stations: number of stations.
        prerequisites: list of (station, must_run_before_it) pairs.
    Returns:
        a valid run order covering every station, or None if impossible.

    station_run_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)]) -> [0, 1, 2, 3]
    station_run_order(2, [(0, 1), (1, 0)]) -> None

    Target complexity: O(V + E) time, O(V + E) space.
    """
    raise NotImplementedError


def min_notes_for_amount(denominations: list[int], amount: int) -> int:
    """A cash machine dispenses an exact `amount` using an UNLIMITED
    supply of the given note `denominations`. Find the minimum number
    of notes needed, or -1 if it's impossible.

    Params:
        denominations: distinct positive note values available.
        amount: target amount to dispense, amount >= 0.
    Returns:
        fewest notes summing to exactly amount, or -1 if impossible.

    min_notes_for_amount([1, 5, 10, 25], 30) -> 2
    min_notes_for_amount([5, 10], 3) -> -1
    min_notes_for_amount([1, 5, 10, 25], 0) -> 0

    Target complexity: O(amount * len(denominations)) time, O(amount) space.
    """
    raise NotImplementedError


def unique_arrangements(fragment: str) -> list[str]:
    """A lab tool needs every DISTINCT ordering of the letters in a
    short DNA `fragment` (letters may repeat, e.g. "AAT"). Return all
    unique arrangements, sorted alphabetically.

    Params:
        fragment: a short string, letters may repeat, len <= 8.
    Returns:
        every distinct permutation of `fragment`, sorted alphabetically.

    unique_arrangements("AAT") -> ["AAT", "ATA", "TAA"]
    unique_arrangements("AB") -> ["AB", "BA"]

    Target complexity: O(n! * n / duplicates) time in the worst case
    (bounded by len(fragment) <= 8), O(n! * n) space for the output.
    """
    raise NotImplementedError
