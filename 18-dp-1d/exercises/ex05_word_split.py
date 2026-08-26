# Scenario: a password-reset service wants to know if a string COULD be
# split into a sequence of dictionary words (any word reusable any
# number of times) -- not which split, just whether one exists.
# Pattern: "can it be done" DP -- a reachability question over prefixes.
# Run: uv run pytest 18-dp-1d -k ex05

from __future__ import annotations


def can_segment(s: str, words: list[str]) -> bool:
    """Return True if `s` can be split into a sequence of one or more
    words from `words` (each word reusable any number of times, in any
    order), with no leftover characters. Return False otherwise.

    STATE: dp[i] = True if the PREFIX s[:i] (length i) can be fully
    split into dictionary words.
    CHOICE: for a prefix of length i, try every earlier split point j
    such that s[:j] is already known splittable AND s[j:i] is itself a
    whole dictionary word.
    RECURRENCE: dp[i] = any(dp[j] and s[j:i] in word_set for j in
    range(i)). Build `word_set = set(words)` first so each membership
    check is O(1) instead of O(len(words)).
    BASE CASE: dp[0] = True (the empty prefix is trivially "split" —
    zero words used).

    can_segment("dogcat", ["dog", "cat"]) -> True
    can_segment("dogcatapp", ["dog", "cat", "app", "cats"]) -> True
    can_segment("catsandog", ["cats", "dog", "sand", "and", "cat"]) -> False
    can_segment("", ["a"]) -> True

    Target: O(n^2) time (n = len(s)), O(n) space.
    """
    raise NotImplementedError
