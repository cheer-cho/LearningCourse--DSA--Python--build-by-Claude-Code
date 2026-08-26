# Scenario: a "did you mean...?" dictionary that supports single-character
# wildcards, like a crossword solver checking `c.t` against known words.
# Pattern: trie + DFS branching (a '.' fans out to every child instead of
# following one).
# Run: uv run pytest 13-tries -k ex02


class WordDictionary:
    """A dictionary of words supporting exact AND wildcard lookup, where
    '.' in a search pattern matches any single character.

    Build it on the same trie shape as ex01 — the only new idea is that
    `search` becomes a small DFS: a literal character follows one child,
    a '.' tries every child.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add_word(self, word: str) -> None:
        """Add `word` to the dictionary. Same contract as `Trie.insert`
        in ex01 (idempotent; "" is a valid word).

        Target complexity: O(L) time, L = len(word).
        """
        raise NotImplementedError

    def search(self, pattern: str) -> bool:
        """Return True if any added word matches `pattern`, where '.'
        matches exactly one arbitrary character and every other
        character must match literally. `pattern` must match the FULL
        word — no partial/prefix matches.

        add_word("bad"); search("b.d") -> True   ("bad" matches)
        add_word("bad"); search("ba") -> False    (wrong length)
        add_word("bad"); search("...") -> True    (three dots, three letters)
        add_word("bad"); search("....") -> False  (four dots, no 4-letter word)

        Target complexity: O(L) time best case (no dots); up to
        O(alphabet_size^dots * L) worst case (pattern of all dots),
        since each dot forks the search into every child.
        """
        raise NotImplementedError
