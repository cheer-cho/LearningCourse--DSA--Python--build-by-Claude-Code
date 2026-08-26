# Checkpoint 07 — PlayQueue
#
# A music player's "up next" queue, built on the doubly linked list from
# ex06: songs enqueue at the back, "play now" jumps a song to the
# front, any song can be pulled out of the queue by name, and the
# player keeps a capped, most-recent-first history of what it already
# played.
# Run: uv run pytest 07-linked-lists -k checkpoint

from __future__ import annotations


class PlayQueue:
    """An "up next" queue for a music player, plus a capped play
    history.

    `add_last`/`play_next` make it behave like a plain queue.
    `play_now` lets a song jump the line. `remove` pulls a song out by
    name wherever it sits. Every song that finishes `play_next`-ing
    joins `history` — capped at `history_capacity` entries, LRU-
    eviction style: the OLDEST recorded play falls off once history is
    full, regardless of how many times a song has played since.
    """

    def __init__(self, history_capacity: int) -> None:
        """`history_capacity` is the max number of past plays
        `history()` remembers. `history_capacity` >= 1.
        """
        raise NotImplementedError

    def add_last(self, song: str) -> None:
        """Add `song` to the back of the upcoming queue.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def play_next(self) -> str:
        """Pop the front of the upcoming queue, record it as played,
        and return it. Raises IndexError if the queue is empty.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def play_now(self, song: str) -> None:
        """Push `song` onto the FRONT of the upcoming queue, so it
        plays next. Does not touch history — it hasn't played yet.

        Target: O(1) time, O(1) space.
        """
        raise NotImplementedError

    def remove(self, song: str) -> bool:
        """Remove the first (closest to the front) queued occurrence of
        `song`. Return True if something was removed, False if `song`
        isn't in the upcoming queue.

        Target: O(n) time, O(1) space.
        """
        raise NotImplementedError

    def history(self, k: int) -> list[str]:
        """Return up to the last `k` played songs, most-recently-played
        first. `k` may exceed how much history exists (or exceed
        `history_capacity`) — just return whatever is available.

        Target: O(k) time, O(k) space.
        """
        raise NotImplementedError
