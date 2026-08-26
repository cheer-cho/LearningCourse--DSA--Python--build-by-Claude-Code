class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.is_end = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = _Node()

    def add_word(self, word: str) -> None:
        # Pattern: identical to Trie.insert (ex01). O(L) time/space.
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, pattern: str) -> bool:
        # Pattern: DFS over the trie. A literal character narrows to one
        # child (same as a plain trie walk); a '.' fans out and tries
        # every child, short-circuiting on the first match.
        # O(L) best case; O(alphabet^dots * L) worst case (all dots).
        def dfs(node: _Node, i: int) -> bool:
            if i == len(pattern):
                return node.is_end
            ch = pattern[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)

        return dfs(self.root, 0)
