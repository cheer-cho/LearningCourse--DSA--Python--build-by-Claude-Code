def longest_unique(s: str) -> int:
    # Pattern: variable-size window, shrink-while-invalid. State is the
    # last-seen index of each character, so when a repeat shows up we
    # jump `left` straight past it instead of shrinking one step at a
    # time. Time: O(n). Space: O(min(n, alphabet size)).
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
