class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.is_end = False
        self.count = 0


def _build(words: list[str]) -> _Node:
    root = _Node()
    for word in words:
        node = root
        node.count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _Node()
            node = node.children[ch]
            node.count += 1
        node.is_end = True
    return root


def shortest_unique_prefix(words: list[str]) -> list[str]:
    # Pattern: PrefixCounter idea (ex03) reused — build once, then per
    # word walk until the pass-through counter hits 1 (no one else is
    # down here). Falls back to the full word if that never happens
    # (the word is a prefix of another, so it never gets sole custody
    # of any node, not even its own last one).
    # O(N) time/space, N = total characters across `words`.
    root = _build(words)
    result = []
    for word in words:
        node = root
        prefix = word
        for i, ch in enumerate(word):
            node = node.children[ch]
            if node.count == 1:
                prefix = word[: i + 1]
                break
        result.append(prefix)
    return result


def longest_common_prefix_all(words: list[str]) -> str:
    # Pattern: build the trie, then walk its spine — follow the one
    # child a node has for as long as there's exactly one child and no
    # word ends there. Branching or an early word-end caps the shared
    # prefix. O(N) time, N = total characters across `words`.
    if not words:
        return ""

    root = _build(words)
    chars: list[str] = []
    node = root
    while len(node.children) == 1 and not node.is_end:
        (ch, child), = node.children.items()
        chars.append(ch)
        node = child
    return "".join(chars)
