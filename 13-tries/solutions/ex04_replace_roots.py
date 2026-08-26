class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.is_end = False


def replace_with_roots(roots: list[str], sentence: str) -> str:
    # Pattern: trie of roots, then one walk per sentence word, stopping
    # at the first is_end node — a trie walk reaches shorter matching
    # prefixes before longer ones, so "first end reached" IS "shortest
    # matching root," no comparison needed.
    # O(R + S) time: R = total root characters (build once), S = total
    # sentence characters (each word walked at most to its own length).
    root_node = _Node()
    for root in roots:
        node = root_node
        for ch in root:
            if ch not in node.children:
                node.children[ch] = _Node()
            node = node.children[ch]
        node.is_end = True

    def shortest_root(word: str) -> str:
        node = root_node
        for i, ch in enumerate(word):
            if ch not in node.children:
                return word
            node = node.children[ch]
            if node.is_end:
                return word[: i + 1]
        return word

    return " ".join(shortest_root(word) for word in sentence.split(" "))
