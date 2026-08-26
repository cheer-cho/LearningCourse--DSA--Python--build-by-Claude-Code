# Scenario: relabeling at most k tiles in a row to all match, maximizing
# the run length. Pattern: variable-size window where validity is
# "window_size - most_common_count_in_window <= k" (you'd need to edit
# every OTHER character to make the window uniform).
# Run: uv run pytest 05-sliding-window -k ex04


def longest_uniform_with_k_edits(s: str, k: int) -> int:
    """Return the length of the longest substring of `s` that can be
    made all-one-character by changing at most `k` characters in it.

    Classic subtlety: track `max_freq`, the highest single-character
    count seen in ANY window so far during this sweep. When the window
    becomes invalid, shrink by one from the left WITHOUT recomputing
    `max_freq` from the shrunken window. `max_freq` can go stale (too
    high for the current window) — that's fine: the window size only
    ever grows again once it can beat the best length already found,
    and a stale (too-high) `max_freq` only makes the validity check
    stricter, never lets an invalid window slip through as valid. So
    correctness holds even though `max_freq` is sometimes wrong for the
    literal current window.

    longest_uniform_with_k_edits("aabccbb", 2) -> 5   ("bccbb" -> "bbbbb", 2 edits)
    longest_uniform_with_k_edits("aaaa", 0) -> 4
    longest_uniform_with_k_edits("", 2) -> 0
    longest_uniform_with_k_edits("abcde", 0) -> 1

    Raises `ValueError` if `k` is negative.

    Target: O(n) time, O(alphabet size) space.
    """
    raise NotImplementedError
