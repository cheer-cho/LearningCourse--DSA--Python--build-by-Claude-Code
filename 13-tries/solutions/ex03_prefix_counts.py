class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.is_end = False
        self.count = 0  # words that pass through this node


class PrefixCounter:
    def __init__(self) -> None:
        self.root = _Node()

    def insert(self, word: str) -> None:
        # Pattern: trie insert, but every node visited (root included)
        # gets its pass-through counter bumped, so a later prefix lookup
        # never has to rescan the subtree. O(L) time/space.
        node = self.root
        node.count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _Node()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def _walk(self, prefix: str) -> _Node | None:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def count_starting_with(self, prefix: str) -> int:
        # Pattern: walk to the prefix's node, read its precomputed
        # counter. No subtree scan. O(P) time, P = len(prefix).
        node = self._walk(prefix)
        return node.count if node is not None else 0

    def autocomplete(self, prefix: str, k: int) -> list[str]:
        # Pattern: walk to the prefix's node (O(P)), then DFS its
        # subtree in sorted child order. Visiting is_end before
        # recursing yields words in alphabetical order for free — a
        # word is always lexicographically <= any longer word sharing
        # its prefix. Stop the moment k results are collected.
        # O(P + M) time, M = characters across the results returned.
        node = self._walk(prefix)
        if node is None or k <= 0:
            return []

        results: list[str] = []

        def dfs(current: _Node, path: str) -> None:
            if len(results) >= k:
                return
            if current.is_end:
                results.append(path)
                if len(results) >= k:
                    return
            for ch in sorted(current.children):
                if len(results) >= k:
                    return
                dfs(current.children[ch], path + ch)

        dfs(node, prefix)
        return results
