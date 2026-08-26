def plan_day(talks: list[tuple[str, int, int]]) -> list[str]:
    # Pattern: sort-by-end interval scheduling (ex06 shape). The talk
    # ending soonest always leaves the most room for what follows.
    # Complexity: O(n log n) time, O(n) space.
    talks_sorted = sorted(talks, key=lambda talk: talk[2])
    chosen: list[str] = []
    last_end = float("-inf")

    for title, start, end in talks_sorted:
        if start >= last_end:
            chosen.append(title)
            last_end = end

    return chosen


def rooms_needed(talks: list[tuple[str, int, int]]) -> int:
    # Pattern: start/end event sweep (ex06 shape). End events are
    # processed before start events at a tied timestamp so a room
    # freed by an ending talk is reusable by one starting at the same
    # instant (touching, not overlapping).
    # Complexity: O(n log n) time, O(n) space.
    if not talks:
        return 0

    events: list[tuple[int, int]] = []
    for _title, start, end in talks:
        events.append((start, 1))
        events.append((end, 0))
    events.sort(key=lambda event: (event[0], event[1]))

    rooms = 0
    max_rooms = 0
    for _time, kind in events:
        rooms += 1 if kind == 1 else -1
        max_rooms = max(max_rooms, rooms)

    return max_rooms


def merge_busy(calendars: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    # Pattern: sort-by-start interval merge (ex05 shape), applied to
    # the flattened union of every calendar's slots.
    # Complexity: O(n log n) time, O(n) space (n = total slots).
    all_slots = [slot for calendar in calendars for slot in calendar]
    if not all_slots:
        return []

    slots_sorted = sorted(all_slots, key=lambda slot: slot[0])
    merged = [list(slots_sorted[0])]

    for start, end in slots_sorted[1:]:
        last = merged[-1]
        if start < last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])

    return [tuple(slot) for slot in merged]


def coffee_run(energy_levels: list[int]) -> tuple[int, int, int]:
    # Pattern: Kadane's running-best with bounds (ex01 shape).
    # Complexity: O(n) time, O(1) extra space.
    best = cur = energy_levels[0]
    best_start = best_end = cur_start = 0

    for i in range(1, len(energy_levels)):
        level = energy_levels[i]
        if cur + level < level:
            cur = level
            cur_start = i
        else:
            cur = cur + level
        if cur > best:
            best = cur
            best_start = cur_start
            best_end = i

    return (best, best_start, best_end)
