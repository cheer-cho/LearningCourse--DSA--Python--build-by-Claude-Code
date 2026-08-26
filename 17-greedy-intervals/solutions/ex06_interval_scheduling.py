def max_non_overlapping(intervals: list[list[int]]) -> int:
    # Pattern: sort-by-end interval scheduling — the exchange-argument
    # showcase (LESSON.md). The interval ending soonest always leaves
    # at least as much room for everything scheduled after it as any
    # other choice would, so it's always safe to take.
    # Complexity: O(n log n) time (the sort), O(1) extra space.
    if not intervals:
        return 0

    intervals_sorted = sorted(intervals, key=lambda interval: interval[1])
    count = 0
    last_end = float("-inf")

    for start, end in intervals_sorted:
        if start >= last_end:
            count += 1
            last_end = end

    return count


def min_removals(intervals: list[list[int]]) -> int:
    # Pattern: complement of max_non_overlapping — whatever isn't kept
    # in the largest non-overlapping subset must be removed.
    # Complexity: O(n log n) time, O(1) extra space.
    return len(intervals) - max_non_overlapping(intervals)


def can_attend_all(intervals: list[list[int]]) -> bool:
    # Pattern: sort-by-start overlap detection. Touching (start ==
    # previous end) is allowed; only a strictly earlier start overlaps.
    # Complexity: O(n log n) time, O(1) extra space.
    if len(intervals) <= 1:
        return True

    intervals_sorted = sorted(intervals, key=lambda interval: interval[0])
    for i in range(1, len(intervals_sorted)):
        if intervals_sorted[i][0] < intervals_sorted[i - 1][1]:
            return False
    return True


def min_rooms(intervals: list[list[int]]) -> int:
    # Pattern: start/end event sweep. Sorting end-events before
    # start-events at a tied timestamp is what lets a room freed by an
    # ending meeting be reused immediately by one starting at the same
    # instant (touching, not overlapping).
    # Complexity: O(n log n) time, O(n) space.
    if not intervals:
        return 0

    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, 0))
    # sort by time; at a tie, end events (0) come before start events (1)
    events.sort(key=lambda event: (event[0], event[1]))

    rooms = 0
    max_rooms = 0
    for _time, kind in events:
        rooms += 1 if kind == 1 else -1
        max_rooms = max(max_rooms, rooms)

    return max_rooms
