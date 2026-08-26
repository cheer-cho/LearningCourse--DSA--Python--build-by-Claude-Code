# Scenario: find every occurrence of a pattern inside a large text
# without re-reading characters at every start position. Pattern:
# rolling hash (Rabin-Karp) -- slide the window in O(1), verify on
# every hash hit (collisions happen; never trust a hash match alone).
# Run: uv run pytest 21-advanced-structures-strings -k ex05

from __future__ import annotations

BASE = 31
MOD = 1_000_000_007


def find_all(text: str, pattern: str) -> list[int]:
    """Return every 0-indexed start position where `pattern` occurs
    in `text` (occurrences may overlap), using a rolling hash to
    filter candidates and verifying each hash hit against the real
    characters before reporting it.

    Recipe:
    1. Precompute `BASE ** (len(pattern) - 1) mod MOD` once (a plain
       loop -- this is the same repeated-multiplication idea as
       module 08's `power_mod`).
    2. Compute the pattern's hash and the FIRST window's hash.
    3. Slide right one character at a time: drop the leaving
       character's contribution, shift, add the entering character
       -- all mod `MOD`. Compare to the pattern hash; on a match,
       verify the actual substring before recording it.

    find_all("abracadabra", "abra") -> [0, 7]
    find_all("aaaa", "aa") -> [0, 1, 2]   (overlapping matches count)
    find_all("hello", "") -> []
    find_all("hi", "hello") -> []           (pattern longer than text)

    Target: O(n + m) expected time (n = len(text), m = len(pattern)),
    O(1) extra space beyond the result list.
    """
    raise NotImplementedError


def count_repeated_windows(dna: str, k: int) -> int:
    """Count how many DISTINCT length-`k` substrings of `dna` appear
    more than once (i.e. how many k-length "windows" are repeated
    somewhere else in the string).

    Slide a rolling hash across every window in one pass, collecting
    hashes in a set (or counting them); a k-length substring repeats
    when its hash has already been seen. Track SEEN and REPEATED as
    two sets, only doing the expensive real-substring comparison when
    a hash collides, the same collision-honesty rule as `find_all`.

    count_repeated_windows("AAAAA", 2) -> 1     ("AA" repeats; only
        one DISTINCT repeated window, even though "AA" occurs 4 times)
    count_repeated_windows("ACGTACGT", 4) -> 1  ("ACGT" repeats once)
    count_repeated_windows("ACGT", 10) -> 0     (k longer than dna)

    Target: O(n) expected time (n = len(dna)), O(n) space.
    """
    raise NotImplementedError
