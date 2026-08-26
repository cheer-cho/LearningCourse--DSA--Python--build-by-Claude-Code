def min_window_cover(s: str, t: str) -> str:
    # Pattern: HARD variable-size window with need/have counters. Grow
    # the right edge until every character requirement is satisfied,
    # then shrink the left edge while it stays satisfied, recording the
    # shortest window along the way. Time: O(n + m). Space: O(alphabet).
    if not t or not s:
        return ""

    need: dict[str, int] = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)

    window: dict[str, int] = {}
    satisfied = 0
    best_len: int | None = None
    best_start = 0
    left = 0

    for right, ch in enumerate(s):
        if ch in need:
            window[ch] = window.get(ch, 0) + 1
            if window[ch] == need[ch]:
                satisfied += 1

        while satisfied == required:
            if best_len is None or (right - left + 1) < best_len:
                best_len = right - left + 1
                best_start = left

            left_ch = s[left]
            if left_ch in need:
                if window[left_ch] == need[left_ch]:
                    satisfied -= 1
                window[left_ch] -= 1
            left += 1

    if best_len is None:
        return ""
    return s[best_start : best_start + best_len]
