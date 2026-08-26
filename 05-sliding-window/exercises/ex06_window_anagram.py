# Scenario: an intrusion-detection scan looking for any rearrangement of
# a known signature inside a long log line. Pattern: fixed-size window +
# frequency compare, kept O(1) per step with a running "how many
# characters currently match" counter instead of re-comparing full
# frequency tables at every position.
# Run: uv run pytest 05-sliding-window -k ex06


def contains_permutation(needle: str, haystack: str) -> bool:
    """Return True if any contiguous substring of `haystack` is a
    permutation (character-for-character rearrangement, same
    multiplicities) of `needle`.

    Slide a window of size `len(needle)` across `haystack`. Keep a
    frequency count of `needle` and of the current window, plus a
    `matches` counter of how many characters currently have equal
    counts in both — update `matches` by at most a constant amount per
    add/remove instead of comparing the whole frequency tables each
    step.

    contains_permutation("abc", "eidbacoo") -> True   ("bac" at index 3)
    contains_permutation("ab", "eidboaoo") -> False
    contains_permutation("", "anything") -> True
    contains_permutation("abc", "ab") -> False   (needle longer than haystack)

    Target: O(n + m) time where n = len(haystack), m = len(needle).
    """
    raise NotImplementedError
