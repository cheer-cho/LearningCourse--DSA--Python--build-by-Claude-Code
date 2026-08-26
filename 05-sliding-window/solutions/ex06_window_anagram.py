def contains_permutation(needle: str, haystack: str) -> bool:
    # Pattern: fixed-size window + frequency compare, kept O(1) per step
    # with a `matched` counter (how many distinct chars currently have
    # equal counts in `need` and the window) instead of comparing full
    # frequency tables every slide. Time: O(n + m). Space: O(alphabet).
    m, n = len(needle), len(haystack)
    if m == 0:
        return True
    if m > n:
        return False

    need: dict[str, int] = {}
    for ch in needle:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)

    window: dict[str, int] = {}
    matched = 0

    for right in range(n):
        ch = haystack[right]
        if ch in need:
            window[ch] = window.get(ch, 0) + 1
            if window[ch] == need[ch]:
                matched += 1
            elif window[ch] == need[ch] + 1:
                matched -= 1

        if right >= m:
            left_ch = haystack[right - m]
            if left_ch in need:
                if window[left_ch] == need[left_ch]:
                    matched -= 1
                window[left_ch] -= 1
                if window[left_ch] == need[left_ch]:
                    matched += 1

        if right >= m - 1 and matched == required:
            return True

    return False
