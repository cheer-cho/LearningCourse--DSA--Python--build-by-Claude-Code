# Checkpoint 21 -- Metrics service
#
# A lightweight metrics service combining every tool from this
# module: two range trees (sum + min) for record/window_total/
# window_low, and a string-matching algorithm (your choice) for
# scanning logs, plus a max-window-sum tool (your choice) for
# spotting the busiest stretch of readings.
#
# Run: uv run pytest 21-advanced-structures-strings -k checkpoint_21

from __future__ import annotations


class MetricsBoard:
    """A metrics board tracking a fixed-size array of sensor values,
    supporting fast point updates and two kinds of range query, plus
    log scanning and busiest-window detection.

    Internally, keep TWO range trees (segment trees, or one segment
    tree + one Fenwick tree -- your call) built over `initial_values`:
    one that merges by sum (for `window_total`) and one that merges
    by min (for `window_low`). `record` must update BOTH.

    Target complexity: O(n) build.
    """

    def __init__(self, initial_values: list[int]) -> None:
        """Build the board over `initial_values` (at least one
        element).

        MetricsBoard([5, 2, 8, 1, 9]).window_total(0, 4) -> 25
        """
        raise NotImplementedError

    def record(self, i: int, v: int) -> None:
        """Set the sensor at index `i` to value `v` (a point update).
        Both internal trees must reflect the change afterward.

        board = MetricsBoard([5, 2, 8, 1, 9])
        board.record(2, 100)
        board.window_total(0, 4) -> 117
        board.window_low(0, 4) -> 1

        Target: O(log n) time.
        """
        raise NotImplementedError

    def window_total(self, i: int, j: int) -> int:
        """Return the SUM of sensor values in `[i, j]`, inclusive.

        Target: O(log n) time.
        """
        raise NotImplementedError

    def window_low(self, i: int, j: int) -> int:
        """Return the MINIMUM sensor value in `[i, j]`, inclusive.

        Target: O(log n) time.
        """
        raise NotImplementedError

    def alert_scan(self, log_text: str, signature: str) -> list[int]:
        """Return every 0-indexed start position where `signature`
        occurs in `log_text` (independent of the board's own sensor
        data -- this is a standalone string-search utility living on
        the same class).

        Use EITHER Rabin-Karp OR KMP -- your choice. Whichever you
        pick, name it and justify the choice in ONE sentence in this
        docstring (edit this line before submitting).

        alert_scan("ERROR: disk full ERROR: disk full", "ERROR") ->
            [0, 17]
        alert_scan("all clear", "ERROR") -> []

        Target: O(n + m) time (n = len(log_text), m = len(signature)).
        """
        raise NotImplementedError

    def busiest_window(self, readings: list[int], k: int) -> int:
        """Return the maximum SUM over any contiguous window of size
        `k` in `readings` (independent of the board's own sensor
        data). `readings` has at least `k` elements.

        Use EITHER a monotonic deque OR a prefix-sum scan -- your
        choice. Whichever you pick, name it and justify the choice in
        ONE sentence in this docstring (edit this line before
        submitting; hint -- sum is invertible, unlike min/max).

        busiest_window([1, 4, 2, 9, 7, 3], 3) -> 19   (window [9,7,3])

        Target: O(n) time.
        """
        raise NotImplementedError
