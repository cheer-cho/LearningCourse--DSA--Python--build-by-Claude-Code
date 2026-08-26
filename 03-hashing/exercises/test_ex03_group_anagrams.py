from ex03_group_anagrams import group_anagrams, is_anagram


def _as_comparable(groups: list[list[str]]) -> set[frozenset[str]]:
    return {frozenset(group) for group in groups}


def test_is_anagram_true_case():
    assert is_anagram("listen", "silent") is True


def test_is_anagram_different_lengths():
    assert is_anagram("cat", "cats") is False


def test_is_anagram_same_word():
    assert is_anagram("abc", "abc") is True


def test_is_anagram_case_sensitive():
    assert is_anagram("Eat", "ate") is False


def test_is_anagram_empty_strings():
    assert is_anagram("", "") is True


def test_group_anagrams_typical():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    expected = [{"eat", "tea", "ate"}, {"tan", "nat"}, {"bat"}]
    assert _as_comparable(result) == {frozenset(g) for g in expected}


def test_group_anagrams_empty_list():
    assert group_anagrams([]) == []


def test_group_anagrams_no_anagrams_each_alone():
    words = ["dog", "cat", "bird"]
    result = group_anagrams(words)
    assert _as_comparable(result) == {frozenset([w]) for w in words}


def test_group_anagrams_every_word_covered_exactly_once():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    flattened = [w for group in result for w in group]
    assert sorted(flattened) == sorted(words)


def test_group_anagrams_duplicate_words():
    words = ["aa", "aa", "ab"]
    result = group_anagrams(words)
    flattened = sorted(w for group in result for w in group)
    assert flattened == sorted(words)
    # the two "aa" entries must land in the same group
    aa_group = next(g for g in result if "aa" in g)
    assert aa_group.count("aa") == 2
