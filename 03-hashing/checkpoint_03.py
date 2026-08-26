# Checkpoint 03 — Log analytics
#
# You're given a list of (user, action) event pairs from a server log,
# e.g. [("ada", "login"), ("bo", "login"), ("ada", "logout")]. Build the
# four analytics functions below. Every one of them is a hash-map
# pattern from this module (counting, grouping, or last-seen-index) —
# nothing new to learn, just combine what you already have.
# Run: uv run pytest 03-hashing -k checkpoint

Event = tuple[str, str]


def action_counts(events: list[Event]) -> dict[str, int]:
    """Return a dict mapping each action to how many times it occurs
    across all events (counting pattern).

    action_counts([("ada", "login"), ("bo", "login"), ("ada", "logout")])
        -> {"login": 2, "logout": 1}
    action_counts([]) -> {}

    Target: O(n) time, O(k) space (k = distinct actions).
    """
    raise NotImplementedError


def first_unique_user(events: list[Event]) -> str | None:
    """Return the first user (by order of first appearance in `events`)
    who appears in exactly ONE event total. Return None if every user
    appears more than once, or `events` is empty.

    first_unique_user(
        [("ada", "login"), ("bo", "login"), ("ada", "logout"), ("cy", "login")]
    ) -> "bo"    # ada appears twice; bo is the first user with only 1 event

    Target: O(n) time, O(k) space (k = distinct users).
    """
    raise NotImplementedError


def users_by_action(events: list[Event]) -> dict[str, list[str]]:
    """Group users by the action they performed (grouping pattern).
    For each action, list the users who performed it, in the order
    those events occur in `events` (a user appears once per matching
    event — if they performed the same action three times, they show
    up three times in that action's list).

    users_by_action([("ada", "login"), ("bo", "login"), ("ada", "logout")])
        -> {"login": ["ada", "bo"], "logout": ["ada"]}

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def has_duplicate_burst(events: list[Event], k: int) -> bool:
    """Return True if the same (user, action) pair occurs twice within
    `k` events of each other (index distance <= k) anywhere in
    `events`. This is the last-seen-index pattern, keyed on the whole
    (user, action) pair instead of a single value.

    has_duplicate_burst(
        [("ada", "login"), ("bo", "login"), ("ada", "login")], 2
    ) -> True    # ada/login repeats at distance 2
    has_duplicate_burst(
        [("ada", "login"), ("bo", "login"), ("ada", "login")], 1
    ) -> False   # distance 2 > k

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError
