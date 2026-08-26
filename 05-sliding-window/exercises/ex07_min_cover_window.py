# Scenario: picking the shortest clip from a transcript that still
# contains every word of a required-phrase list, with repeats respected.
# Pattern: HARD variable-size window with need/have counters, shrink
# while the window still satisfies every requirement.
# Run: uv run pytest 05-sliding-window -k ex07


def min_window_cover(s: str, t: str) -> str:
    """Return the shortest contiguous substring of `s` that contains
    every character of `t`, counting multiplicity (two `'a'`s in `t`
    means the substring needs at least two `'a'`s). Return "" if no
    such substring exists, or if `t` is empty.

    Keep a `need` count per character (from `t`) and a `have` count per
    character (current window), plus a `satisfied` counter of how many
    distinct characters currently meet their `need`. Grow the right
    edge until `satisfied == len(need)`, then shrink the left edge
    while it stays fully satisfied, recording the shortest window seen.

    min_window_cover("ADOBECODEBANC", "ABC") -> "BANC"
    min_window_cover("a", "aa") -> ""
    min_window_cover("abc", "") -> ""

    Target: O(n + m) time where n = len(s), m = len(t).
    """
    raise NotImplementedError
