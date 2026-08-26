from __future__ import annotations

from ex06_build_doubly_list import DoublyLinkedList


class PlayQueue:
    """An "up next" queue for a music player, plus a capped play
    history.

    `add_last`/`play_next` make it behave like a plain queue.
    `play_now` lets a song jump the line. `remove` pulls a song out by
    name wherever it sits. Every song that finishes `play_next`-ing
    joins `history` — capped at `history_capacity` entries, LRU-
    eviction style: the OLDEST recorded play falls off once history is
    full, regardless of how many times a song has played since.

    `remove` and `history` only use the public DoublyLinkedList API
    (push/pop at the ends) — no direct node access needed. Both use the
    same trick: pop off the front, inspect/collect, push back what
    should stay. That keeps the whole queue's internals private while
    still hitting the target complexities.
    """

    def __init__(self, history_capacity: int) -> None:
        self._queue = DoublyLinkedList()
        self._history = DoublyLinkedList()
        self._history_capacity = history_capacity

    def add_last(self, song: str) -> None:
        # O(1) time, O(1) space.
        self._queue.push_back(song)

    def play_next(self) -> str:
        # O(1) time, O(1) space.
        song = self._queue.pop_front()
        self._record_play(song)
        return song

    def play_now(self, song: str) -> None:
        # O(1) time, O(1) space.
        self._queue.push_front(song)

    def remove(self, song: str) -> bool:
        # Pattern: rotate the queue through itself. Pop every node off
        # the front (capturing the ORIGINAL size first, since the queue
        # shrinks and regrows as we go), skip the first match, push
        # everything else back onto the back in the same relative
        # order. O(n) time, O(1) extra space.
        original_size = self._queue.size()
        found = False
        for _ in range(original_size):
            value = self._queue.pop_front()
            if not found and value == song:
                found = True
                continue
            self._queue.push_back(value)
        return found

    def history(self, k: int) -> list[str]:
        # Pattern: same rotate trick as remove, but on `_history` and
        # bounded by k instead of a full pass — pop the k most-recent
        # (front) entries off, collect them, then push them back in
        # reverse so the front order is restored. O(k) time, O(k) space.
        limit = min(k, self._history.size())
        recent = []
        for _ in range(limit):
            recent.append(self._history.pop_front())
        for song in reversed(recent):
            self._history.push_front(song)
        return recent

    def _record_play(self, song: str) -> None:
        # Bounded, most-recent-first history: push to the front, evict
        # the back once we exceed capacity. O(1) time, O(1) space.
        self._history.push_front(song)
        if self._history.size() > self._history_capacity:
            self._history.pop_back()
