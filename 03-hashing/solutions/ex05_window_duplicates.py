def has_nearby_duplicate(nums: list[int], k: int) -> bool:
    # Pattern: last-seen-index map. Only the most recent occurrence of a
    # value can be the closest one, so overwriting on every sighting is
    # safe and keeps the map at O(distinct values) entries.
    # Time: O(n). Space: O(n).
    last_seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        if value in last_seen and i - last_seen[value] <= k:
            return True
        last_seen[value] = i
    return False


def first_repeated_within(stream: list[int], k: int) -> int | None:
    # Pattern: last-seen-index map, same idea as has_nearby_duplicate but
    # returning the value instead of a boolean.
    # Time: O(n). Space: O(n).
    last_seen: dict[int, int] = {}
    for i, value in enumerate(stream):
        if value in last_seen and i - last_seen[value] <= k:
            return value
        last_seen[value] = i
    return None
