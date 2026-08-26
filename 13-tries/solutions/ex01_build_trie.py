class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Pattern: standard trie insert — walk the chain of characters,
        # creating a node whenever the next character isn't already a
        # child, then flag the last node as a word ending.
        # O(L) time/space, L = len(word).
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _walk(self, prefix: str) -> TrieNode | None:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        # Pattern: walk the exact chain, then require is_end — a node
        # existing only means "some longer word passes through here."
        # O(L) time, O(1) space.
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        # Pattern: walk the exact chain; existing at all is enough —
        # unlike search, we don't care whether a word ends here.
        # O(L) time, O(1) space.
        return self._walk(prefix) is not None
