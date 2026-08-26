from __future__ import annotations


def failure_table(pattern: str) -> list[int]:
    # Pattern: KMP failure function -- table[i] = length of the
    # longest proper prefix of pattern[0..i] that is also a proper
    # suffix of it ("longest border"). Built with a self-referential
    # two-pointer scan: when characters mismatch, fall back to the
    # border of the shorter match already found instead of restarting.
    # Complexity: O(m) time (amortized -- `border` only ever
    # decreases inside the while loop, and increases by at most 1 per
    # outer step), O(m) space.
    m = len(pattern)
    table = [0] * m
    border = 0

    for i in range(1, m):
        while border > 0 and pattern[border] != pattern[i]:
            border = table[border - 1]
        if pattern[border] == pattern[i]:
            border += 1
        table[i] = border

    return table


def kmp_find_all(text: str, pattern: str) -> list[int]:
    # Pattern: KMP search. The failure table lets the text pointer
    # `i` move strictly forward: on a mismatch, fall back the pattern
    # pointer `j` to `table[j - 1]` instead of re-reading `text[i]`.
    # Complexity: O(n + m) time guaranteed, O(m) space
    # (n = len(text), m = len(pattern)).
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    table = failure_table(pattern)
    matches: list[int] = []
    j = 0

    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = table[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            matches.append(i - j + 1)
            j = table[j - 1]

    return matches
