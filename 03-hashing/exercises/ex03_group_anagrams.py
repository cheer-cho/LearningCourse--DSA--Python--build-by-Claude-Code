# Scenario: a word-game app wants to cluster words that use exactly the
# same letters (e.g. for a "find all anagrams of my rack" feature).
# Pattern: grouping by a canonical key.
# Run: uv run pytest 03-hashing -k ex03


def is_anagram(a: str, b: str) -> bool:
    """Return True if `a` and `b` use exactly the same letters with the
    same multiplicities (ignoring order). Case-sensitive: "Eat" and
    "ate" are NOT anagrams here.

    is_anagram("listen", "silent") -> True
    is_anagram("cat", "act") -> True
    is_anagram("cat", "cats") -> False

    Target: O(n) time, O(1) extra space (26-letter counts) if inputs
    are lowercase a-z; O(n log n) if you sort instead — either is fine.
    """
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group `words` so that every group contains only mutual anagrams
    of each other. Every input word appears in exactly one group.

    Two canonical keys both work and either is accepted: the word's
    letters sorted into a string (`"".join(sorted(word))`), or a
    26-count tuple. Order of groups, and order of words WITHIN a
    group, does not matter — tests compare the groups as sets.

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]   (any order)
    group_anagrams([]) -> []

    Target: O(n * k log k) time (n words, k = max word length using the
    sorted-key approach), O(n * k) space.
    """
    raise NotImplementedError
