# Scenario: one stock, one allowed buy and one allowed sell, in that
# order. Pattern: same-direction sweep where the left edge of the window
# is "the best buy price seen so far" — a window that only ever grows or
# resets, never shrinks step by step.
# Run: uv run pytest 05-sliding-window -k ex02


def max_profit(prices: list[int]) -> int:
    """Return the max profit from buying once and selling once later
    (sell day must come after buy day). Return 0 if no profit is
    possible (e.g. prices only fall).

    Track the minimum price seen so far as you sweep left to right —
    that minimum IS the left edge of the best window ending at the
    current day.

    max_profit([7, 1, 5, 3, 6, 4]) -> 5   (buy at 1, sell at 6)
    max_profit([7, 6, 4, 3, 1]) -> 0      (falling only, never sell)
    max_profit([]) -> 0
    max_profit([5]) -> 0

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
