# Scenario: a text editor highlights every palindromic run in a string
# and reports the longest one.
# Pattern: palindrome DP via expand-around-center -- still fundamentally
# a 2-D idea (position x radius), collapsed to O(1) space per center.
# Run: uv run pytest 19-dp-2d -k ex07

from __future__ import annotations


def count_palindromic_substrings(s: str) -> int:
    """Count all palindromic SUBSTRINGS of `s` (contiguous runs that
    read the same forwards and backwards). Every position is its own
    occurrence, even for a repeated character -- "aaa" has 6: "a"
    (x3), "aa" (x2), "aaa".

    Method: expand-around-center. Every palindrome has a center -- a
    single character (odd length) or the gap between two characters
    (even length). For each of the 2n - 1 centers, expand outward while
    both ends match, counting one palindrome per successful expansion.

    Note the substring/subsequence distinction from the lesson: this is
    substrings only (contiguous) -- LCS-style subsequence DP would
    answer a different question.

    count_palindromic_substrings("abc") -> 3   ("a", "b", "c")
    count_palindromic_substrings("aaa") -> 6
    count_palindromic_substrings("aba") -> 4   ("a","b","a","aba")

    Target: O(n^2) time, O(1) space.
    """
    raise NotImplementedError


def longest_palindromic_substring(s: str) -> str:
    """Return the longest palindromic substring of `s` (non-empty). If
    several substrings share the maximum length, return the one that
    starts at the smallest index.

    Either approach is accepted for this function:
    - expand-around-center (same technique as
      `count_palindromic_substrings`, tracking the best (start, length)
      seen) -- O(n^2) time, O(1) space; OR
    - a full O(n^2)-space table dp[i][j] = "is s[i:j+1] a palindrome",
      filled by increasing substring length -- O(n^2) time, O(n^2)
      space. Strictly worse on space for the same time, which is why
      expand-around-center is the one worth reaching for by default.

    longest_palindromic_substring("babad") -> "bab"
    longest_palindromic_substring("cbbd") -> "bb"
    longest_palindromic_substring("a") -> "a"
    longest_palindromic_substring("ac") -> "a"

    Target: O(n^2) time, O(1) space (expand-around-center).
    """
    raise NotImplementedError
