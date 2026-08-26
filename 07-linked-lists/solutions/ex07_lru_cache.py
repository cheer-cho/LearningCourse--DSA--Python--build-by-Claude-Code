from __future__ import annotations

from ex06_build_doubly_list import DListNode, DoublyLinkedList


class LRUCache:
    """A fixed-capacity cache: `get` and `put` are both O(1), and once
    `capacity` is exceeded the LEAST recently used entry is evicted.

    Anatomy: a hash map from key -> doubly linked node (O(1) lookup),
    plus a doubly linked list ordered by recency (front = most recently
    used, back = least recently used), reused from ex06. Each node's
    value is a (key, value) pair so an eviction can also drop the
    matching hash-map entry.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._map: dict[int, DListNode] = {}
        self._list = DoublyLinkedList()

    def _touch(self, key: int, value: int) -> None:
        # Move `key` to most-recently-used: drop its old node, push a
        # fresh one to the front, and repoint the map at it. Both
        # remove_node and push_front are O(1), so this whole "move to
        # front" is O(1).
        node = self._map[key]
        self._list.remove_node(node)
        self._map[key] = self._list.push_front((key, value))

    def get(self, key: int) -> int:
        # Pattern: hash map for O(1) existence + lookup, then move the
        # hit to the front since it was just used. O(1) time/space.
        if key not in self._map:
            return -1
        _key, value = self._map[key].value
        self._touch(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        # Pattern: overwrite-and-touch if the key exists; otherwise
        # evict the back (least recently used) if full, then insert at
        # the front. O(1) time/space.
        if key in self._map:
            self._touch(key, value)
            return

        if len(self._map) >= self._capacity:
            evicted_key, _evicted_value = self._list.pop_back()
            del self._map[evicted_key]

        self._map[key] = self._list.push_front((key, value))
