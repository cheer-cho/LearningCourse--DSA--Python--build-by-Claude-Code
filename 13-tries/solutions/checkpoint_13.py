class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.is_end = False
        self.count = 0  # times a word passing through here was indexed


class SearchBox:
    # Pattern: one trie backs all four operations — is_end drives
    # match/suggest membership, the pass-through counter drives
    # popularity, and a sorted-child DFS drives suggest. Nothing here
    # is new; it's ex01 (build) + ex02 (wildcard) + ex03 (counts)
    # fused onto a single node type.

    def __init__(self) -> None:
        self.root = _Node()

    def index(self, word: str) -> None:
        # O(L) time, L = len(word).
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

    def suggest(self, prefix: str, k: int) -> list[str]:
        # O(P + M) time: walk to the prefix node, then DFS in sorted
        # child order, stopping as soon as k words are collected.
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

    def match(self, pattern: str) -> bool:
        # O(L) best case, O(alphabet^dots * L) worst case — '.' fans
        # out to every child instead of following one.
        def dfs(node: _Node, i: int) -> bool:
            if i == len(pattern):
                return node.is_end
            ch = pattern[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)

        return dfs(self.root, 0)

    def popularity(self, prefix: str) -> int:
        # O(P) time — read the precomputed counter, no subtree scan.
        node = self._walk(prefix)
        return node.count if node is not None else 0
