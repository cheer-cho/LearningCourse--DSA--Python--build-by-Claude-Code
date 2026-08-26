# Checkpoint 13 — Search-box engine
#
# Combine every trie idea from this module into one class powering a
# search box: index words, suggest completions, wildcard-match a
# pattern, and report how many indexed words share a prefix. Same trie,
# four views into it.
# Run: uv run pytest 13-tries -k checkpoint


class SearchBox:
    """A search-box backend: index words once, then answer completion,
    wildcard, and popularity queries against them — all off one shared
    trie (node = children map + is_end flag + pass-through counter).
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def index(self, word: str) -> None:
        """Add `word` to the index. Idempotent: indexing the same word
        twice counts it twice for `popularity` (like a search log —
        indexing it again means it was searched/added again), but
        `suggest`/`match` still only ever list it once.

        Target complexity: O(L) time, L = len(word).
        """
        raise NotImplementedError

    def suggest(self, prefix: str, k: int) -> list[str]:
        """Return up to `k` distinct indexed words starting with
        `prefix`, in alphabetical order. `[]` if none match.

        Target complexity: O(P + M) time, P = len(prefix), M =
        characters across the (at most k) words returned.
        """
        raise NotImplementedError

    def match(self, pattern: str) -> bool:
        """Return True if any indexed word matches `pattern`, where
        '.' matches any single character and every other character
        must match literally (same contract as ex02's `search`).

        Target complexity: O(L) best case, up to O(alphabet^dots * L)
        worst case, L = len(pattern).
        """
        raise NotImplementedError

    def popularity(self, prefix: str) -> int:
        """Return how many times indexed words starting with `prefix`
        were indexed in total (repeated `index` calls on the same word
        each count).

        Target complexity: O(P) time, P = len(prefix).
        """
        raise NotImplementedError
