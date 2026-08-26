def is_anagram(a: str, b: str) -> bool:
    # Pattern: canonical form comparison. Sorting both strings gives the
    # same result iff they use the same letters with the same counts.
    # Time: O(k log k) for length k. Space: O(k).
    return sorted(a) == sorted(b)


def group_anagrams(words: list[str]) -> list[list[str]]:
    # Pattern: grouping by key. Each word's sorted letters form a
    # canonical key; words sharing a key are mutual anagrams.
    # Time: O(n * k log k). Space: O(n * k).
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
