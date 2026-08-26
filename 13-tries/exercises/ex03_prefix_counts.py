# Scenario: the backend for a search box's "N results" and "top
# suggestions" hints — count how many indexed words share a prefix, and
# list a few of them, without ever rescanning the whole word list.
# Pattern: trie with a pass-through counter on every node.
# Run: uv run pytest 13-tries -k ex03


class PrefixCounter:
    """A trie where every node also tracks how many inserted words pass
    through it (i.e. have it on their path) — not just whether a word
    ends there.

    That per-node counter is the whole trick: `count_starting_with`
    doesn't walk the subtree and count matches, it just walks TO the
    prefix's node and reads the counter already sitting there.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str) -> None:
        """Add `word`, incrementing the pass-through counter on every
        node along its path (including the final, word-ending node).

        Target complexity: O(L) time, L = len(word).
        """
        raise NotImplementedError

    def count_starting_with(self, prefix: str) -> int:
        """Return how many inserted words start with `prefix` (a word
        equal to `prefix` counts). 0 if `prefix` was never walked (no
        inserted word goes through it).

        insert("car"); insert("card"); insert("cat")
        count_starting_with("ca") -> 3
        count_starting_with("car") -> 2
        count_starting_with("z") -> 0

        Target complexity: O(P) time, P = len(prefix) — independent of
        how many words match or how many words are stored in total.
        """
        raise NotImplementedError

    def autocomplete(self, prefix: str, k: int) -> list[str]:
        """Return up to `k` complete words that start with `prefix`, in
        alphabetical order. Fewer than `k` if fewer words match; `[]` if
        none do.

        insert("car"); insert("card"); insert("care")
        autocomplete("car", 2) -> ["car", "card"]
        autocomplete("car", 10) -> ["car", "card", "care"]
        autocomplete("dog", 5) -> []

        Target complexity: O(P + M) time, P = len(prefix), M = total
        characters across the (at most k) words returned — walk to the
        prefix's node once, then DFS its subtree in sorted child order,
        stopping as soon as k words are collected.
        """
        raise NotImplementedError
