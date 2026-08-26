from __future__ import annotations

BASE = 31
MOD = 1_000_000_007


def _char_code(ch: str) -> int:
    return ord(ch) + 1  # +1 so 'a'/chr(0) never contributes 0


def find_all(text: str, pattern: str) -> list[int]:
    # Pattern: rolling hash (Rabin-Karp). Slide the window hash in
    # O(1) per step (drop leaving char, shift, add entering char);
    # verify the real substring on every hash hit -- a match is a
    # CANDIDATE, not a confirmed answer, until verified.
    # Complexity: O(n + m) expected time, O(1) extra space (the
    # `slice` verification is O(m) but only on the rare hash hit).
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    high_power = 1
    for _ in range(m - 1):
        high_power = (high_power * BASE) % MOD

    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * BASE + _char_code(pattern[i])) % MOD
        window_hash = (window_hash * BASE + _char_code(text[i])) % MOD

    matches: list[int] = []
    for start in range(n - m + 1):
        if window_hash == pattern_hash and text[start : start + m] == pattern:
            matches.append(start)
        if start < n - m:
            window_hash = (
                (window_hash - _char_code(text[start]) * high_power) * BASE
                + _char_code(text[start + m])
            ) % MOD

    return matches


def count_repeated_windows(dna: str, k: int) -> int:
    # Pattern: rolling hash into a hash map. One O(n) pass, sliding
    # the hash in O(1) per step; the real substring comparison (O(k))
    # only runs when a hash has been seen before -- collision
    # honesty, same rule as find_all -- so the expensive slice is
    # rare, not routine.
    # Complexity: O(n) expected time, O(n) space.
    n = len(dna)
    if k <= 0 or k > n:
        return 0

    high_power = 1
    for _ in range(k - 1):
        high_power = (high_power * BASE) % MOD

    window_hash = 0
    for i in range(k):
        window_hash = (window_hash * BASE + _char_code(dna[i])) % MOD

    first_start_of_hash: dict[int, int] = {}
    repeated: set[str] = set()

    def record(hash_value: int, start: int) -> None:
        first_start = first_start_of_hash.get(hash_value)
        if first_start is None:
            first_start_of_hash[hash_value] = start
            return
        if dna[first_start : first_start + k] == dna[start : start + k]:
            repeated.add(dna[start : start + k])

    record(window_hash, 0)
    for start in range(1, n - k + 1):
        window_hash = (
            (window_hash - _char_code(dna[start - 1]) * high_power) * BASE
            + _char_code(dna[start + k - 1])
        ) % MOD
        record(window_hash, start)

    return len(repeated)
