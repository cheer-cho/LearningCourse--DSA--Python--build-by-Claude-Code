# Scenario: dedup-checking a live text stream — how long a run can you
# read before a character repeats? Pattern: variable-size window, shrink
# while invalid, state = last-seen index (or a plain set) of characters
# currently in the window.
# Run: uv run pytest 05-sliding-window -k ex03


def longest_unique(s: str) -> int:
    """Return the length of the longest substring of `s` with no
    repeated characters.

    Grow the right edge every step; when the incoming character is
    already in the window, jump `left` to just past its last-seen
    position (don't shrink one character at a time).

    longest_unique("abcabcbb") -> 3   ("abc")
    longest_unique("bbbbb") -> 1      ("b")
    longest_unique("") -> 0
    longest_unique("dvdf") -> 3       ("vdf")

    Target: O(n) time, O(min(n, alphabet size)) space.
    """
    raise NotImplementedError
