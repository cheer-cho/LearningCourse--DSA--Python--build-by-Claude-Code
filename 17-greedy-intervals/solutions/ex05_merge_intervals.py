def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # Pattern: sort-by-start interval merge. Extend the current merged
    # interval while the next interval's start is STRICTLY less than
    # its end (overlap); touching (start == end) closes it out instead.
    # Complexity: O(n log n) time (the sort), O(n) space.
    if not intervals:
        return []

    intervals_sorted = sorted(intervals, key=lambda interval: interval[0])
    merged = [list(intervals_sorted[0])]

    for start, end in intervals_sorted[1:]:
        last = merged[-1]
        if start < last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])

    return merged


def insert_interval(sorted_intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    # Pattern: three-phase linear scan (no re-sort). Phase 1: copy
    # intervals entirely before `new`. Phase 2: fold every overlapping
    # interval into `new`'s bounds. Phase 3: copy intervals entirely
    # after `new`.
    # Complexity: O(n) time, O(n) space.
    result: list[list[int]] = []
    i = 0
    n = len(sorted_intervals)
    new_start, new_end = new

    while i < n and sorted_intervals[i][1] <= new_start:
        result.append(sorted_intervals[i])
        i += 1

    while i < n and sorted_intervals[i][0] < new_end:
        new_start = min(new_start, sorted_intervals[i][0])
        new_end = max(new_end, sorted_intervals[i][1])
        i += 1
    result.append([new_start, new_end])

    while i < n:
        result.append(sorted_intervals[i])
        i += 1

    return result
