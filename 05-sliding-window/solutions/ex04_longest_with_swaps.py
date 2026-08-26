def longest_uniform_with_k_edits(s: str, k: int) -> int:
    # Pattern: variable-size window, shrink-while-invalid. Validity is
    # window_size - max_freq <= k. `max_freq` is only ever updated
    # upward and is allowed to go stale after a shrink — that only makes
    # the check stricter, never lets an invalid window pass, and the
    # window size we report never shrinks below a length already beaten.
    # Time: O(n). Space: O(alphabet size).
    if k < 0:
        raise ValueError("k must be non-negative")

    counts: dict[str, int] = {}
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_freq = max(max_freq, counts[ch])

        window_size = right - left + 1
        if window_size - max_freq > k:
            left_ch = s[left]
            counts[left_ch] -= 1
            left += 1

        best = max(best, right - left + 1)
    return best
