# Scenario: build the core trie from scratch — the node type and the
# three ops (insert / exact search / prefix search) every later exercise
# in this module builds on. Pattern: prefix tree, shared-node walk.
# Run: uv run pytest 13-tries -k ex01


class TrieNode:
    """One node of a trie: a map from the next character to its child
    node, plus a flag marking "a word ends exactly here."

    A node can be BOTH a complete word's ending AND a waypoint toward
    longer words at the same time (e.g. "car" inside "car"/"card").
    """

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    """A prefix tree over strings, built from `TrieNode`s.

    Every word hangs off a shared `root` (representing the empty
    prefix). Words that share a prefix share the nodes for that
    prefix — that sharing is what makes prefix queries O(L) instead
    of O(n * L) for n stored words.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Add `word` to the trie, creating any missing nodes along
        the way. Inserting a word that's already present is a no-op
        (idempotent). Inserting `""` marks the root itself as an end.

        Target complexity: O(L) time, O(L) space (worst case, if no
        node along the path already existed), where L = len(word).
        """
        raise NotImplementedError

    def search(self, word: str) -> bool:
        """Return True if `word` was inserted exactly (not just as a
        prefix of something longer).

        search("car") after insert("car"), insert("card") -> True
        search("ca") after the same inserts -> False (never inserted alone)
        search("") -> True only if "" was itself inserted.

        Target complexity: O(L) time, O(1) space, L = len(word).
        """
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        """Return True if any inserted word begins with `prefix`
        (the word equal to `prefix` counts too).

        starts_with("ca") after insert("car") -> True
        starts_with("") -> True always, even on an empty trie.

        Target complexity: O(L) time, O(1) space, L = len(prefix).
        """
        raise NotImplementedError
