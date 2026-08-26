# Scenario: an in-memory cache that must answer get/put in O(1) and
# forget its least-recently-used entry once it's full — the reason hash
# maps and doubly linked lists get paired up in the first place.
# Concepts: hash map -> node, doubly linked list with sentinels, LRU
# eviction, move-to-front on access.
# Run: uv run pytest 07-linked-lists -k ex07

from __future__ import annotations


class LRUCache:
    """A fixed-capacity cache: `get` and `put` are both O(1), and once
    `capacity` is exceeded the LEAST recently used entry is evicted.

    Anatomy: a hash map from key -> doubly linked node (O(1) lookup),
    plus a doubly linked list ordered by recency (front = most recently
    used, back = least recently used). Every successful get/put moves
    that key's node to the front. Reuses (or re-implements) the
    doubly linked list from ex06.
    """

    def __init__(self, capacity: int) -> None:
        """`capacity` is the maximum number of entries the cache holds
        before it starts evicting. `capacity` >= 1.
        """
        raise NotImplementedError

    def get(self, key: int) -> int:
        """Return the value stored for `key`, or -1 if `key` is absent.
        A successful get counts as a "use" — it refreshes `key` to
        most-recently-used.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        """Store `value` under `key`, refreshing `key` to
        most-recently-used. If `key` already exists, overwrite its
        value. If inserting a NEW key would exceed capacity, evict the
        least-recently-used entry first.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError
