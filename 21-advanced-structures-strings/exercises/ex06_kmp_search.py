# Scenario: find every occurrence of a pattern in a huge text with a
# GUARANTEED linear time bound -- no collision risk, unlike ex05's
# Rabin-Karp. Pattern: KMP (Knuth-Morris-Pratt), built on the
# "failure function" (longest proper prefix that's also a suffix).
# Run: uv run pytest 21-advanced-structures-strings -k ex06

from __future__ import annotations


def failure_table(pattern: str) -> list[int]:
    """Return the KMP failure table for `pattern`: `table[i]` is the
    length of the longest string that is BOTH a proper prefix and a
    proper suffix (a "border") of `pattern[0..i]` (inclusive).

    "Proper" means the border can't be the entire `pattern[0..i]`
    itself -- a single character (`i == 0`) always has `table[0] = 0`
    since it has no proper border at all.

    failure_table("ababaca") -> [0, 0, 1, 2, 3, 0, 1]
    failure_table("aaaa") -> [0, 1, 2, 3]
    failure_table("abcd") -> [0, 0, 0, 0]
    failure_table("") -> []

    Target: O(m) time, O(m) space (m = len(pattern)).
    """
    raise NotImplementedError


def kmp_find_all(text: str, pattern: str) -> list[int]:
    """Return every 0-indexed start position where `pattern` occurs
    in `text` (occurrences may overlap), using the failure table so
    the pointer into `text` NEVER moves backward.

    Walk `text` with pointer `i`, `pattern` with pointer `j`. Match ->
    advance both. Mismatch with `j > 0` -> fall back
    `j = failure_table(pattern)[j - 1]` WITHOUT moving `i`. Mismatch
    with `j == 0` -> advance `i`. `j` reaching `len(pattern)` ->
    record a match at `i - j + 1`, then fall back
    `j = failure_table(pattern)[j - 1]` to keep scanning for
    overlapping matches.

    kmp_find_all("ababcababcababc", "ababc") -> [0, 5, 10]
    kmp_find_all("aaaa", "aa") -> [0, 1, 2]   (overlapping matches count)
    kmp_find_all("hello", "") -> []
    kmp_find_all("hi", "hello") -> []           (pattern longer than text)

    Target: O(n + m) time, guaranteed (never degrades), O(m) space
    (n = len(text), m = len(pattern)).
    """
    raise NotImplementedError
