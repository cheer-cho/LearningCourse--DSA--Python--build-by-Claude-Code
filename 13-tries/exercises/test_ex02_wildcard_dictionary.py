from ex02_wildcard_dictionary import WordDictionary


def test_exact_match():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("bad") is True


def test_no_match_for_unrelated_word():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("dad") is False


def test_single_wildcard_matches():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("b.d") is True


def test_wildcard_no_match_by_length_shorter():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("ba") is False


def test_wildcard_no_match_by_length_longer():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("badd") is False


def test_all_dots_matches_any_word_of_that_length():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("...") is True


def test_all_dots_rejects_wrong_length():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("....") is False


def test_multiple_words_disambiguate_with_wildcards():
    wd = WordDictionary()
    for word in ["bad", "bat", "cat", "cot"]:
        wd.add_word(word)
    assert wd.search("ba.") is True   # bad, bat
    assert wd.search(".at") is True   # bat, cat
    assert wd.search("c.t") is True   # cat, cot
    assert wd.search("d..") is False  # nothing starts with d


def test_empty_pattern_matches_only_empty_word():
    wd = WordDictionary()
    wd.add_word("")
    assert wd.search("") is True


def test_empty_pattern_false_when_empty_word_never_added():
    wd = WordDictionary()
    wd.add_word("bad")
    assert wd.search("") is False


def test_search_on_empty_dictionary():
    wd = WordDictionary()
    assert wd.search("a") is False
    assert wd.search(".") is False


def test_add_word_is_idempotent():
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("bad")
    assert wd.search("bad") is True
