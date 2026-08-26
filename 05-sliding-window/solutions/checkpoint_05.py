def worst_minute(counts: list[int]) -> int:
    # Pattern: fixed-size sliding window (size 60). Same add/drop update
    # as ex01's max_window_sum. Time: O(n). Space: O(1).
    n = len(counts)
    if n < 60:
        raise ValueError("need at least 60 seconds of data")

    window_sum = sum(counts[:60])
    best = window_sum
    for right in range(60, n):
        window_sum += counts[right] - counts[right - 60]
        best = max(best, window_sum)
    return best


def longest_within_budget(counts: list[int], budget: int) -> int:
    # Pattern: variable-size window, shrink-while-invalid (sum > budget).
    # Safe because every count >= 0, so shrinking only lowers the sum.
    # Guard `left <= right` so a negative budget (never satisfiable)
    # can't shrink the window past the current right edge.
    # Time: O(n). Space: O(1).
    left = 0
    total = 0
    best = 0
    for right, count in enumerate(counts):
        total += count
        while total > budget and left <= right:
            total -= counts[left]
            left += 1
        best = max(best, right - left + 1)
    return best


def shortest_breach(counts: list[int], threshold: int) -> int:
    # Pattern: variable-size window, INVERTED shrink rule — shrink WHILE
    # the sum still meets threshold, to find the shortest such window.
    # Guard `left <= right` so a threshold every window already meets
    # (e.g. 0 or negative) can't shrink the window past the right edge.
    # Time: O(n). Space: O(1).
    left = 0
    total = 0
    best: int | None = None
    for right, count in enumerate(counts):
        total += count
        while total >= threshold and left <= right:
            length = right - left + 1
            if best is None or length < best:
                best = length
            total -= counts[left]
            left += 1
    return best if best is not None else 0


def has_pattern_burst(counts: list[int], pattern: list[int]) -> bool:
    # Pattern: fixed-size window + frequency compare with an O(1)
    # `matched` counter, same shape as ex06's contains_permutation but
    # over integers. Time: O(n + m). Space: O(distinct values).
    m, n = len(pattern), len(counts)
    if m == 0:
        return True
    if m > n:
        return False

    need: dict[int, int] = {}
    for value in pattern:
        need[value] = need.get(value, 0) + 1
    required = len(need)

    window: dict[int, int] = {}
    matched = 0

    for right in range(n):
        value = counts[right]
        if value in need:
            window[value] = window.get(value, 0) + 1
            if window[value] == need[value]:
                matched += 1
            elif window[value] == need[value] + 1:
                matched -= 1

        if right >= m:
            left_value = counts[right - m]
            if left_value in need:
                if window[left_value] == need[left_value]:
                    matched -= 1
                window[left_value] -= 1
                if window[left_value] == need[left_value]:
                    matched += 1

        if right >= m - 1 and matched == required:
            return True

    return False
