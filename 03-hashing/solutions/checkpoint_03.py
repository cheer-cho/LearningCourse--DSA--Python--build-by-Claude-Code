Event = tuple[str, str]


def action_counts(events: list[Event]) -> dict[str, int]:
    # Pattern: counting map over the action field.
    # Time: O(n). Space: O(k) distinct actions.
    counts: dict[str, int] = {}
    for _user, action in events:
        counts[action] = counts.get(action, 0) + 1
    return counts


def first_unique_user(events: list[Event]) -> str | None:
    # Pattern: counting map (over users) + a second pass to preserve
    # first-appearance order, same shape as ex01's first_unique_index.
    # Time: O(n). Space: O(k) distinct users.
    counts: dict[str, int] = {}
    for user, _action in events:
        counts[user] = counts.get(user, 0) + 1

    for user, _action in events:
        if counts[user] == 1:
            return user
    return None


def users_by_action(events: list[Event]) -> dict[str, list[str]]:
    # Pattern: grouping by key, same shape as group_anagrams.
    # Time: O(n). Space: O(n).
    groups: dict[str, list[str]] = {}
    for user, action in events:
        groups.setdefault(action, []).append(user)
    return groups


def has_duplicate_burst(events: list[Event], k: int) -> bool:
    # Pattern: last-seen-index map, keyed on the (user, action) tuple.
    # Time: O(n). Space: O(n).
    last_seen: dict[Event, int] = {}
    for i, event in enumerate(events):
        if event in last_seen and i - last_seen[event] <= k:
            return True
        last_seen[event] = i
    return False
