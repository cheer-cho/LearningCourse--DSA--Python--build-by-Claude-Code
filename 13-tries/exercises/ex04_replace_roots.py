# Scenario: a search engine's query normalizer stems each word down to
# the shortest known root it recognizes ("running" -> "run"), so
# "running shoes" and "run shoes" hit the same index entries.
# Pattern: build a trie of roots, walk each sentence word to its first
# end-of-word marker (the walk hits the SHORTEST matching root first).
# Run: uv run pytest 13-tries -k ex04


def replace_with_roots(roots: list[str], sentence: str) -> str:
    """Replace every word in `sentence` with the shortest string in
    `roots` that is a prefix of it, if one exists; words with no
    matching root are left untouched. Words are separated by single
    spaces; return the rebuilt sentence the same way.

    replace_with_roots(["cat", "bat", "rat"],
                        "the cattle was rattled by the battery")
        -> "the cat was rat by the bat"
    replace_with_roots(["a"], "a aa aaa")
        -> "a a a"              (shortest root "a" wins for all three)
    replace_with_roots(["catt"], "cat")
        -> "cat"                ("catt" is not a prefix of "cat")
    replace_with_roots([], "the cattle was rattled")
        -> "the cattle was rattled"   (no roots -> nothing changes)

    Build a trie out of `roots` once, then for each sentence word walk
    the trie character by character and stop at the FIRST is_end node
    reached — that's necessarily the shortest matching root, since a
    trie walk visits shorter prefixes before longer ones.

    Target complexity: O(R + S) time, R = total characters across all
    roots (building the trie once), S = total characters across the
    sentence (each word walked at most to its own length).
    """
    raise NotImplementedError
