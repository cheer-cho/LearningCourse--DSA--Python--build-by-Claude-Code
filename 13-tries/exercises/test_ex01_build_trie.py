from ex01_build_trie import Trie


def test_search_finds_inserted_word():
    trie = Trie()
    trie.insert("car")
    assert trie.search("car") is True


def test_search_rejects_word_never_inserted():
    trie = Trie()
    trie.insert("car")
    assert trie.search("care") is False


def test_search_rejects_prefix_that_was_never_its_own_word():
    trie = Trie()
    trie.insert("card")
    assert trie.search("car") is False


def test_car_and_card_are_independent():
    trie = Trie()
    trie.insert("car")
    trie.insert("card")
    assert trie.search("car") is True
    assert trie.search("card") is True
    assert trie.search("ca") is False
    assert trie.search("cards") is False


def test_starts_with_matches_stored_prefix():
    trie = Trie()
    trie.insert("card")
    assert trie.starts_with("car") is True
    assert trie.starts_with("card") is True


def test_starts_with_rejects_unrelated_prefix():
    trie = Trie()
    trie.insert("card")
    assert trie.starts_with("cat") is False


def test_starts_with_empty_prefix_is_always_true():
    trie = Trie()
    assert trie.starts_with("") is True
    trie.insert("car")
    assert trie.starts_with("") is True


def test_insert_empty_word_makes_it_searchable():
    trie = Trie()
    trie.insert("")
    assert trie.search("") is True


def test_search_empty_string_false_when_never_inserted():
    trie = Trie()
    trie.insert("car")
    assert trie.search("") is False


def test_insert_is_idempotent():
    trie = Trie()
    trie.insert("car")
    trie.insert("car")
    assert trie.search("car") is True


def test_shared_prefix_nodes_do_not_leak_between_words():
    trie = Trie()
    trie.insert("care")
    assert trie.search("car") is False
    assert trie.starts_with("car") is True


def test_multiple_unrelated_words():
    trie = Trie()
    for word in ["car", "card", "care", "dog"]:
        trie.insert(word)
    for word in ["car", "card", "care", "dog"]:
        assert trie.search(word) is True
    assert trie.search("do") is False
    assert trie.starts_with("do") is True
    assert trie.starts_with("z") is False
